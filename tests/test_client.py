"""The client against a SkimmerDB test server: SKIMMERDB_URL (default http://127.0.0.1:8080).
It signs up a throwaway account, so never point it at production. Skipped when nothing answers.

    SKIMMERDB_URL=http://127.0.0.1:8080 python -m pytest -q
"""

import os
import uuid

import httpx
import pytest

from skimmerdb import SkimmerDB, SkimmerDBError
from skimmerdb._api.api.search import search as raw_search
from skimmerdb._api.models import SearchRequest

URL = os.environ.get("SKIMMERDB_URL", "http://127.0.0.1:8080")


def _up() -> bool:
    try:
        return httpx.get(URL + "/healthz", timeout=2).text == "ok"
    except httpx.HTTPError:
        return False


pytestmark = pytest.mark.skipif(not _up(), reason=f"no SkimmerDB server at {URL}")


@pytest.fixture(scope="module")
def db() -> SkimmerDB:
    return SkimmerDB.signup(f"py-{uuid.uuid4().hex[:10]}@example.com", "correct horse", base_url=URL)


def test_quickstart(db: SkimmerDB):
    ns = db.namespace("support")
    w = ns.write(
        [
            {"id": "t-1", "text": "Refund requested for order ACME-1042", "meta": {"status": "open", "priority": 3}},
            {"id": "t-2", "text": "Login fails with error E401 on mobile", "meta": {"status": "closed", "priority": 1}},
        ],
        wait=True,
    )
    assert w.written == 2
    assert w.created is True
    hits = ns.search("acme-1042", filter={"status": "open"}).hits
    assert [h.id for h in hits] == ["t-1"]
    assert hits[0].line == "Refund requested for order ACME-1042"
    assert hits[0].meta["priority"] == 3
    assert ns.search("E[0-9]{3}", regex=True, filter={"priority": {"gte": 1, "lt": 4}}).hits[0].match == "E401"
    assert ns.count("refund") == 1
    assert ns.count(filter={"status": ["open", "closed"]}) == 2
    doc = ns.get("t-1")
    assert doc.text == "Refund requested for order ACME-1042"
    assert doc.temperature == "warm"
    ns.write([{"id": "a/b c", "text": "an id with a slash and a space"}], wait=True)
    assert ns.get("a/b c").text == "an id with a slash and a space"
    ns.delete(["a/b c"], wait=True)


def test_paging_update_delete(db: SkimmerDB):
    ns = db.namespace("paging")
    ns.write([{"id": f"d-{i}", "text": f"note {i}"} for i in range(5)], wait=True)
    first = ns.search("note", limit=2)
    assert len(first.hits) == 2 and first.next
    second = ns.search("note", limit=10, cursor=first.next)
    assert len(second.hits) == 3 and second.next == ""
    ns.update([{"id": "d-1", "meta": {"tag": "x"}}], wait=True)
    assert ns.get("d-1").meta.to_dict() == {"tag": "x"}
    ns.delete(["d-1"], wait=True)
    with pytest.raises(SkimmerDBError) as e:
        ns.get("d-1")
    assert e.value.status == 404
    assert ns.count() == 4


def test_vectors_sql_and_info(db: SkimmerDB):
    notes = db.namespace("notes")
    notes.write(
        [
            {"id": "n-1", "text": "Webhook timeouts since Tuesday", "meta": {"team": "api"}, "vector": [0.12, -0.03, 0.99]},
            {"id": "n-2", "text": "Dark mode request", "meta": {"team": "web"}, "vector": [0.9, 0.1, 0.05]},
        ],
        wait=True,
    )
    hits = notes.search(vector=[0.1, 0.0, 0.98], limit=2).hits
    assert hits[0].id == "n-1" and hits[0].score > 0.9
    assert [h.id for h in notes.search("dark", vector=[0.1, 0.0, 0.98]).hits] == ["n-2"]
    sup = db.namespace("support")
    r = sup.sql("SELECT status, COUNT(*) AS n FROM docs GROUP BY status ORDER BY status")
    assert r.columns == ["status", "n"] and r.rows == [["closed", 1], ["open", 1]]
    assert notes.info().vector.dims == 3
    assert "notes" in [n.name for n in db.namespaces().namespaces]
    assert db.me().scope == "admin"
    app = SkimmerDB(db.create_key("app"), base_url=URL)
    assert app.me().scope == "write"
    with pytest.raises(SkimmerDBError) as e:
        app.create_key("more")
    assert e.value.status == 403 and e.value.code == "forbidden"
    assert db.usage().queries > 0
    notes.drop()


def test_errors_and_the_generated_layer(db: SkimmerDB):
    with pytest.raises(SkimmerDBError) as e:
        db.namespace("missing").search("x")
    assert e.value.status == 404 and e.value.code == "not_found" and e.value.message == "no such namespace"
    with pytest.raises(SkimmerDBError) as e:
        db.create_namespace("Bad Name")
    assert e.value.status == 422 and e.value.code == "invalid"
    with pytest.raises(SkimmerDBError) as e:
        SkimmerDB.signup("not-an-email", "1", base_url=URL)
    assert e.value.status == 422 and "password" in e.value.fields
    with pytest.raises(SkimmerDBError) as e:
        SkimmerDB("tb_nope", base_url=URL).namespaces()
    assert e.value.status == 401
    # every operation is there, generated: here search by hand
    res = raw_search.sync(name="support", client=db.api, body=SearchRequest(q="refund"))
    assert [h.id for h in res.hits] == ["t-1"]
