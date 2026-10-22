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
from typing import Any, Iterable, Iterator, Mapping, Optional, Sequence

import httpx

from ._api import AuthenticatedClient, Client
from ._api.api.accounts import get_me, login as _login, signup as _signup
from ._api.api.documents import delete_documents, get_document, import_bucket as _import_bucket, update_documents, write_documents
from ._api.api.embeddings import delete_embedding_key, list_embedding_keys, set_embedding_key
from ._api.api.keys import create_key
from ._api.api.namespaces import create_namespace, delete_namespace, get_namespace, list_namespaces, update_namespace
from ._api.api.search import count as _count, search as _search, warm_namespace
from ._api.api.sql_beta import create_export, get_export, query_sql
from ._api.api.usage import get_usage
from ._api.models import (
    BucketImportRequest,
    BucketImportResult,
    CountRequest,
    CountResult,
    CreateNamespace,
    DeleteRequest,
    EmbeddingKey,
    EmbeddingKeyList,
    EmbeddingKeyRequest,
    Export,
    ExportRequest,
    KeyRequest,
    LoginRequest,
    Me,
    Namespace as NamespaceInfo,
    NamespaceList,
    NamespacePatch,
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
Export.bytes = property(lambda self: self.bytes_)  # type: ignore[attr-defined]
BucketImportResult.next = property(lambda self: self.next_)  # type: ignore[attr-defined]
BucketImportResult.bytes = property(lambda self: self.bytes_)  # type: ignore[attr-defined]
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
        semantic: Optional[str] = None,
        **options: Any,
    ) -> SearchResult:
        """Exact text (literal, ignoring case) or regex, newest first; with ``vector`` (or
        ``semantic``, a text, in a namespace with an embedding model), the nearest documents
        (``q`` and ``filter`` narrow them: hybrid). ``.hits``, and ``.next_`` to pass as
        ``cursor`` for the next page. Options: nprobe, rerank, full."""
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
        if semantic is not None:
            body["semantic"] = semantic
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

    def sql_rows(self, query: str) -> Iterator[dict]:
        """(beta) A query's rows as they're streamed (NDJSON: no 10,000-row cap), one dict a row."""
        return self.db._sql_rows(f"/v1/namespaces/{self.name}/sql", query)

    def write_stream(self, docs: Iterable[Any], *, wait: bool = False) -> dict:
        """Writes any number of documents in one streamed request (NDJSON, written in batches
        of 50,000 as the server reads them; each batch atomic, the stream not). Returns
        {"written", "batches", "lines", "version", ...}."""
        def body() -> Iterator[bytes]:
            buf: list = []
            size = 0
            for d in docs:
                line = json.dumps(_doc(d), separators=(",", ":")) + "\n"
                buf.append(line)
                size += len(line)
                if size >= 1 << 20:
                    yield "".join(buf).encode()
                    buf, size = [], 0
            if buf:
                yield "".join(buf).encode()
        url = f"{self.db.base_url}/v1/namespaces/{self.name}/docs/stream" + ("?wait=true" if wait else "")
        res = self.db._http.post(url, content=body(), headers={"Content-Type": "application/x-ndjson"})
        if res.status_code != 200:
            raise _error(res)
        return res.json()

    def import_bucket(
        self,
        path: str,
        s3: Mapping[str, str],
        *,
        id: str = "",
        text: Sequence[str] = (),
        format: str = "",
        schema: str = "",
        after: str = "",
        follow: bool = True,
    ) -> list[BucketImportResult]:
        """Imports CSV, NDJSON or Parquet files from your own bucket: s3://bucket/key, a prefix
        (s3://bucket/dir/) or a pattern (s3://bucket/dir/*.parquet). s3 holds region,
        access_key_id, secret_access_key (and session_token), plus endpoint for an S3-compatible
        service (Cloudflare R2: "https://<account>.r2.cloudflarestorage.com", region "auto"; B2,
        MinIO, Wasabi, GCS). Each request takes up to 100 files / 4 GB; with follow (the default) it
        goes on from each answer's next until every file is in. The answers, in order."""
        out: list[BucketImportResult] = []
        while True:
            body = {"path": path, "s3": dict(s3), "id": id, "text": list(text), "format": format, "schema": schema, "after": after}
            r = _call(_import_bucket, name=self.name, client=self.db.api, body=BucketImportRequest.from_dict(body))
            out.append(r)
            after = r.next
            if not follow or not after:
                return out

    def warm(self, queries: Sequence[str] = ()) -> WarmResult:
        """Opens the namespace ahead of queries (and fetches what these searches need)."""
        return _call(warm_namespace, name=self.name, client=self.db.api, body=WarmRequest.from_dict({"queries": list(queries)}))

    # ---- the namespace itself
    def set_embedding(self, provider: Optional[str], model: Optional[str] = None) -> NamespaceInfo:
        """Sets or changes the model documents' text is embedded with (provider openai, voyage,
        gemini or cohere with your own key, or skimmerdb, hosted); ``None`` stops embedding. The
        model must make vectors of the namespace's length."""
        embed: Optional[dict] = None
        if provider:
            embed = {"provider": provider}
            if model:
                embed["model"] = model
        return _call(update_namespace, name=self.name, client=self.db.api, body=NamespacePatch.from_dict({"embed": embed}))

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

    def create_namespace(
        self, name: str, *, dims: Optional[int] = None, metric: str = "cosine", embed: Optional[Mapping[str, Any]] = None, exist_ok: bool = False
    ) -> Namespace:
        """Creates a namespace. ``dims``: vectors of that length (yours). ``embed``: documents'
        text embedded for you, with your own provider key (``{"provider": "openai"}``, voyage,
        gemini, cohere) or hosted at cost (``{"provider": "skimmerdb"}``); then
        ``search(semantic="...")``."""
        body: dict = {"name": name}
        if dims:
            body["vector"] = {"dims": dims, "metric": metric}
        if embed:
            body["embed"] = dict(embed)
        try:
            _call(create_namespace, client=self.api, body=CreateNamespace.from_dict(body))
        except SkimmerDBError as e:
            if not (exist_ok and e.status == 409):
                raise
        return Namespace(self, name)

    def namespaces(self, *, after: str = "", limit: int = 100) -> NamespaceList:
        return _call(list_namespaces, client=self.api, after=after, limit=limit)

    def set_embedding_key(self, provider: str, key: str) -> EmbeddingKey:
        """Stores your own key for an embedding provider (openai, voyage, gemini or cohere):
        checked with the provider, kept encrypted, never shown again. Needs an admin key."""
        return _call(set_embedding_key, provider=provider, client=self.api, body=EmbeddingKeyRequest(key=key))

    def embedding_keys(self) -> EmbeddingKeyList:
        return _call(list_embedding_keys, client=self.api)

    def delete_embedding_key(self, provider: str) -> None:
        _call(delete_embedding_key, provider=provider, client=self.api)

    # ---- SQL across namespaces: streamed answers and exports (beta)
    def sql_rows(self, query: str) -> Iterator[dict]:
        """(beta) A query over your namespaces (by name), its rows streamed (NDJSON, no row
        cap), one dict a row. A failure midway raises SkimmerDBError (never a short answer)."""
        return self._sql_rows("/v1/sql", query)

    def _sql_rows(self, path: str, query: str) -> Iterator[dict]:
        with self._http.stream("POST", self.base_url + path, json={"sql": query}, headers={"Accept": "application/x-ndjson"}) as res:
            if res.status_code != 200:
                res.read()
                raise _error(res)
            try:
                for line in res.iter_lines():
                    if not line:
                        continue
                    row = json.loads(line)
                    if isinstance(row, dict) and set(row) >= {"error", "code"} and len(row) == 2:
                        raise SkimmerDBError(422, str(row["error"]), None, str(row["code"]))
                    yield row
            except httpx.HTTPError as e:
                raise SkimmerDBError(503, f"the answer was cut short: {e}") from e

    def export(self, query: str, *, format: str = "csv", destination: Optional[str] = None, s3: Optional[Mapping[str, str]] = None) -> Export:
        """(beta) Starts an export of a query's answer (csv, ndjson or parquet): poll export_status
        (or wait_export), then download_export. Kept 24 hours. With destination
        ("s3://bucket/key", or ending in / for a made name) and s3 (keys, as import_bucket takes),
        the file is delivered to your own bucket instead (AWS S3, R2, B2, MinIO, ...)."""
        body: dict = {"sql": query, "format": format}
        if destination is not None:
            body["destination"] = {"path": destination, "s3": dict(s3 or {})}
        return _call(create_export, client=self.api, body=ExportRequest.from_dict(body))

    def export_status(self, id: str) -> Export:
        return _call(get_export, id=id, client=self.api)

    def wait_export(self, id: str, *, timeout: float = 3600.0, poll: float = 1.0) -> Export:
        """Waits until the export is done (raises SkimmerDBError when it failed)."""
        end = time.monotonic() + timeout
        while True:
            e = self.export_status(id)
            if e.status == "done":
                return e
            if e.status in ("failed", "expired"):
                raise SkimmerDBError(422, f"the export {e.status}: {e.error}")
            if time.monotonic() > end:
                raise SkimmerDBError(504, "the export didn't finish in time")
            time.sleep(poll)

    def download_export(self, id: str, path: str) -> int:
        """Downloads a done export to path, resuming (Range) after a broken transfer; the
        file's size."""
        size = int(self.export_status(id).bytes)
        have = os.path.getsize(path) if os.path.exists(path) else 0
        if have > size:
            have = 0
            open(path, "wb").close()
        for attempt in range(6):
            if have >= size:
                return size
            headers = {"Range": f"bytes={have}-"} if have > 0 else {}
            try:
                with self._http.stream("GET", f"{self.base_url}/v1/sql/exports/{id}/download", headers=headers) as res:
                    if res.status_code not in (200, 206):
                        res.read()
                        raise _error(res)
                    with open(path, "ab" if have > 0 else "wb") as f:
                        for chunk in res.iter_bytes():
                            f.write(chunk)
                            have += len(chunk)
            except httpx.HTTPError:
                time.sleep(0.5 * 2**attempt)
        if have < size:
            raise SkimmerDBError(503, "the download kept breaking off: run it again (it resumes)")
        return size

    @property
    def _http(self) -> httpx.Client:
        if getattr(self, "_http_client", None) is None:
            self._http_client = httpx.Client(headers={"Authorization": f"Bearer {self.key}"}, timeout=httpx.Timeout(300.0, connect=30.0))
        return self._http_client

    def me(self) -> Me:
        return _call(get_me, client=self.api)

    def usage(self) -> Usage:
        return _call(get_usage, client=self.api)
