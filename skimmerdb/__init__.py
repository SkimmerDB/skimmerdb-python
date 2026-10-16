"""SkimmerDB: search for your apps and AI agents.

    from skimmerdb import SkimmerDB

    db = SkimmerDB("tb_...")                 # or SKIMMERDB_KEY in the environment
    ns = db.namespace("support")             # the first write makes it
    ns.write([{"id": "t-1", "text": "Refund requested for order ACME-1042", "meta": {"status": "open"}}])
    for hit in ns.search("refund", filter={"status": "open"}).hits:
        print(hit.id, hit.line)

This file is the thin, hand-written layer. Every API operation is also available directly,
generated from the OpenAPI document (https://api.skimmerdb.com/openapi.json) in skimmerdb._api:
``db.api`` is its authenticated client, e.g.

    from skimmerdb._api.api.search import search
    search.sync(name="support", client=db.api, body=SearchRequest(q="refund"))
"""

from __future__ import annotations

import json
import os
import time
from typing import Any, Iterable, Mapping, Optional, Sequence

import httpx

from ._api import AuthenticatedClient, Client
from ._api.api.accounts import get_me, login as _login, signup as _signup
from ._api.api.documents import delete_documents, get_document, update_documents, write_documents
from ._api.api.keys import create_key
from ._api.api.namespaces import create_namespace, delete_namespace, get_namespace, list_namespaces
from ._api.api.search import count as _count, search as _search, warm_namespace
from ._api.api.sql_beta import query_sql
from ._api.api.usage import get_usage
from ._api.models import (
    CountRequest,
    CountResult,
    CreateNamespace,
    DeleteRequest,
    KeyRequest,
    LoginRequest,
    Me,
    Namespace as NamespaceInfo,
    NamespaceList,
    SearchRequest,
    SearchResult,
    SignupRequest,
    SqlRequest,
    SqlResult,
    StoredDocument,
    UpdateRequest,
    Usage,
    WarmRequest,
    WarmResult,
    WriteRequest,
    WriteResult,
)

__all__ = ["SkimmerDB", "Namespace", "SkimmerDBError", "DEFAULT_URL"]

# The generator names the answers' "next" field next_ (it shadows a builtin); .next reads it too.
SearchResult.next = property(lambda self: self.next_)  # type: ignore[attr-defined]
NamespaceList.next = property(lambda self: self.next_)  # type: ignore[attr-defined]
__version__ = "0.1.0"

DEFAULT_URL = "https://api.skimmerdb.com"


class SkimmerDBError(Exception):
    """An error answer: ``status`` (HTTP), ``message`` (the server's sentence), ``code`` (a
    word to act on: not_found, invalid, rate_limited, namespace_limit, write_busy, ...),
    ``fields`` (invalid input: field -> what's wrong) and ``retry_after`` (seconds, on 429)."""

    def __init__(self, status: int, message: str, retry_after: Optional[float] = None, code: str = "", fields: Optional[dict] = None):
        super().__init__(f"{status} {code}: {message}" if code else f"{status}: {message}")
        self.status = status
        self.message = message
        self.code = code
        self.fields = fields or {}
        self.retry_after = retry_after


def _error(res: Any) -> SkimmerDBError:
    body: Any = {}
    try:
        body = json.loads(res.content or b"{}")
    except ValueError:
        body = {"error": (res.content or b"").decode("utf-8", "replace")[:200]}
    if not isinstance(body, dict):
        body = {}
    ra = res.headers.get("retry-after") if res.headers else None
    code = int(res.status_code)
    return SkimmerDBError(code, str(body.get("error") or f"request failed ({code})"), float(ra) if ra else None, str(body.get("code") or ""), body.get("fields") if isinstance(body.get("fields"), dict) else None)


def _call(fn: Any, retries: int = 3, **kwargs: Any) -> Any:
    """Calls a generated operation's sync_detailed; returns the parsed answer, raises
    SkimmerDBError otherwise. 429 and 503 are retried (after Retry-After, or backing off)."""
    for attempt in range(retries + 1):
        res = fn.sync_detailed(**kwargs)
        code = int(res.status_code)
        if 200 <= code < 300:
            return res.parsed
        err = _error(res)
        if code in (429, 503) and attempt < retries:
            time.sleep(err.retry_after if err.retry_after else 0.25 * 2**attempt)
            continue
        raise err
    raise AssertionError("unreachable")


def _base(url: Optional[str]) -> str:
    """The server's root: ``url``, else SKIMMERDB_URL, else https://api.skimmerdb.com (a
    trailing /v1 is dropped: the operations' paths carry it)."""
    u = (url or os.environ.get("SKIMMERDB_URL") or DEFAULT_URL).rstrip("/")
    return u[: -len("/v1")] if u.endswith("/v1") else u


def _doc(d: Any) -> dict:
    if isinstance(d, Mapping):
        return dict(d)
    if hasattr(d, "to_dict"):
        return d.to_dict()
    raise TypeError("a document is a dict: {'id': ..., 'text': ..., 'meta': {...}}")


class Namespace:
    """One namespace: ``db.namespace("support")``. Nothing is sent until you call a method;
    the server makes it on the first write if it doesn't exist (with vectors of the first
    vector's length when the documents have them; the answer's ``created`` says so)."""

    def __init__(self, db: "SkimmerDB", name: str):
        self.db = db
        self.name = name

    def __repr__(self) -> str:
        return f"Namespace({self.name!r})"

    # ---- writing
    def write(self, docs: Iterable[Any] = (), deletes: Sequence[str] = (), *, wait: bool = False) -> WriteResult:
        """Puts (inserts or replaces) documents and deletes ids: up to 10,000 a call.
        ``wait=True`` answers once they're searchable (they're durable either way)."""
        ds = [_doc(d) for d in docs]
        body: dict = {"wait": wait}
        if ds:
            body["docs"] = ds
        if deletes:
            body["deletes"] = list(deletes)
        return _call(write_documents, name=self.name, client=self.db.api, body=WriteRequest.from_dict(body))

    upsert = write

    def update(self, docs: Iterable[Any], *, wait: bool = False) -> WriteResult:
        """Changes existing documents: text replaced if given, meta merged key by key
        (None removes a key)."""
        return _call(update_documents, name=self.name, client=self.db.api, body=UpdateRequest.from_dict({"docs": [_doc(d) for d in docs], "wait": wait}))

    def delete(self, ids: Sequence[str], *, wait: bool = False) -> WriteResult:
        return _call(delete_documents, name=self.name, client=self.db.api, body=DeleteRequest.from_dict({"ids": list(ids), "wait": wait}))

    # ---- reading
    def search(
        self,
        q: str = "",
        *,
        filter: Optional[Mapping[str, Any]] = None,
        limit: Optional[int] = None,
        regex: bool = False,
        cursor: Optional[str] = None,
        vector: Optional[Sequence[float]] = None,
        **options: Any,
    ) -> SearchResult:
        """Exact text (literal, ignoring case) or regex, newest first; with ``vector``, the
        nearest documents (``q`` and ``filter`` narrow them: hybrid). ``.hits``, and ``.next``
        to pass as ``cursor`` for the next page. Options: nprobe, rerank, full."""
        body: dict = {"q": q}
        if regex:
            body["regex"] = True
        if filter:
            body["filter"] = dict(filter)
        if limit is not None:
            body["limit"] = limit
        if cursor:
            body["cursor"] = cursor
        if vector is not None:
            body["vector"] = [float(x) for x in vector]
        body.update(options)
        return _call(_search, name=self.name, client=self.db.api, body=SearchRequest.from_dict(body))

    def count(self, q: str = "", *, filter: Optional[Mapping[str, Any]] = None, regex: bool = False, exact: bool = True) -> int:
        """How many documents match (exactly; ``exact=False`` estimates). The full answer:
        ``count_result``."""
        return self.count_result(q, filter=filter, regex=regex, exact=exact).count

    def count_result(self, q: str = "", *, filter: Optional[Mapping[str, Any]] = None, regex: bool = False, exact: bool = True) -> CountResult:
        body: dict = {"q": q, "regex": regex, "exact": exact}
        if filter:
            body["filter"] = dict(filter)
        return _call(_count, name=self.name, client=self.db.api, body=CountRequest.from_dict(body))

    def get(self, id: str) -> StoredDocument:
        """One document, whole. Raises SkimmerDBError (404) when there's none."""
        return _call(get_document, name=self.name, id=id, client=self.db.api)

    def sql(self, query: str) -> SqlResult:
        """(beta) One SELECT ... FROM docs over the documents' metadata; ``.columns``, ``.rows``."""
        return _call(query_sql, name=self.name, client=self.db.api, body=SqlRequest(sql=query))

    def warm(self, queries: Sequence[str] = ()) -> WarmResult:
        """Opens the namespace ahead of queries (and fetches what these searches need)."""
        return _call(warm_namespace, name=self.name, client=self.db.api, body=WarmRequest.from_dict({"queries": list(queries)}))

    # ---- the namespace itself
    def info(self) -> NamespaceInfo:
        return _call(get_namespace, name=self.name, client=self.db.api)

    def drop(self) -> None:
        """Deletes the namespace and its documents, for good."""
        _call(delete_namespace, name=self.name, client=self.db.api)


class SkimmerDB:
    """A connection with an API key (``key``, else ``SKIMMERDB_KEY``) to
    https://api.skimmerdb.com (``base_url``, else ``SKIMMERDB_URL``)."""

    def __init__(self, key: Optional[str] = None, *, base_url: Optional[str] = None, timeout: float = 30.0):
        key = key or os.environ.get("SKIMMERDB_KEY", "")
        if not key:
            raise SkimmerDBError(401, "no API key: pass SkimmerDB(key) or set SKIMMERDB_KEY (make one at https://skimmerdb.com/dashboard)")
        self.key = key
        self.base_url = _base(base_url)
        self.api = AuthenticatedClient(base_url=self.base_url, token=key, timeout=httpx.Timeout(timeout), raise_on_unexpected_status=False)

    def __repr__(self) -> str:
        return f"SkimmerDB({self.base_url!r})"

    @classmethod
    def signup(cls, email: str, password: str, name: Optional[str] = None, *, base_url: Optional[str] = None) -> "SkimmerDB":
        """Makes an account: a ready connection with its first key, full access (``db.key``;
        keep it, it's shown only once). Give apps and agents narrower keys (``db.create_key``)."""
        url = _base(base_url)
        anon = Client(base_url=url, raise_on_unexpected_status=False)
        res = _call(_signup, retries=0, client=anon, body=SignupRequest(email=email, name=name or email.split("@")[0], password=password))
        return cls(res.key, base_url=url)

    @classmethod
    def login(cls, email: str, password: str, *, base_url: Optional[str] = None, key_name: str = "default") -> "SkimmerDB":
        """Logs in and makes a new API key (scope write) with it."""
        url = _base(base_url)
        anon = Client(base_url=url, raise_on_unexpected_status=False)
        token = _call(_login, client=anon, body=LoginRequest(email=email, password=password)).token
        owner = AuthenticatedClient(base_url=url, token=token, raise_on_unexpected_status=False)
        key = _call(create_key, client=owner, body=KeyRequest.from_dict({"name": key_name})).key
        return cls(key, base_url=url)

    def create_key(self, name: str = "default", *, scope: str = "write", namespaces: Sequence[str] = (), **caps: int) -> str:
        """A new API key (needs an admin key): scope read, write or admin, optionally limited to
        some namespaces (names or "prefix*") and capped (rate_per_s, cap_queries, cap_writes).
        The key is returned once."""
        body: dict = {"name": name, "scope": scope, "namespaces": list(namespaces)}
        body.update(caps)
        return _call(create_key, client=self.api, body=KeyRequest.from_dict(body)).key

    def namespace(self, name: str) -> Namespace:
        return Namespace(self, name)

    def create_namespace(self, name: str, *, dims: Optional[int] = None, metric: str = "cosine", exist_ok: bool = False) -> Namespace:
        """Creates a namespace (``dims``: give it vectors of that length)."""
        body: dict = {"name": name}
        if dims:
            body["vector"] = {"dims": dims, "metric": metric}
        try:
            _call(create_namespace, client=self.api, body=CreateNamespace.from_dict(body))
        except SkimmerDBError as e:
            if not (exist_ok and e.status == 409):
                raise
        return Namespace(self, name)

    def namespaces(self, *, after: str = "", limit: int = 100) -> NamespaceList:
        return _call(list_namespaces, client=self.api, after=after, limit=limit)

    def me(self) -> Me:
        return _call(get_me, client=self.api)

    def usage(self) -> Usage:
        return _call(get_usage, client=self.api)
