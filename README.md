# skimmerdb

Python client for [SkimmerDB](https://skimmerdb.com): a hosted search database for apps and AI
agents. Make a namespace per user, task or project, write documents, and find them by exact
text or regex with metadata filters, count them, search them by vector (alone or hybrid), or
query their metadata with SQL (beta). An idle namespace costs only the bytes it stores.

## Quick start

```sh
pip install skimmerdb
```

```python
from skimmerdb import SkimmerDB

db = SkimmerDB("tb_...")                      # or set SKIMMERDB_KEY
ns = db.namespace("support")                  # the first write makes it
ns.write([{"id": "t-1", "text": "Refund requested for order ACME-1042", "meta": {"status": "open"}}])
for hit in ns.search("refund", filter={"status": "open"}).hits:
    print(hit.id, hit.line)
```

No key yet? Make one at [skimmerdb.com](https://skimmerdb.com/signup), or from Python:

```python
db = SkimmerDB.signup("you@example.com", "a long password")   # one call
print(db.key)                                 # full access, shown once: keep it
app_key = db.create_key("my agent")           # a write key for an app or agent (can't make keys)
```

## More

```python
ns.write(docs, deletes=["t-2"], wait=True)    # put and delete; wait: searchable before it answers
ns.update([{"id": "t-1", "meta": {"status": "closed"}}])   # meta merged key by key
ns.delete(["t-1"])

res = ns.search("E[0-9]{3}", regex=True, filter={"priority": {"gte": 1, "lt": 4}}, limit=50)
res.hits, res.next                            # pass res.next as cursor= for the next page
ns.count("refund")                            # exact
ns.get("t-1").text

# vectors: the first write with vectors creates the namespace with their length
notes = db.namespace("notes")
notes.write([{"id": "n-1", "text": "Webhook timeouts", "vector": embedding}])
notes.search(vector=query_embedding, q="timeout", filter={"team": "api"}, limit=10)

# SQL over the documents' metadata (beta)
ns.sql("SELECT status, COUNT(*) FROM docs WHERE contains(text, 'refund') GROUP BY status").rows

db.namespaces(), db.usage(), db.me()
```

Errors raise `skimmerdb.SkimmerDBError` with `.status`, `.code` (`not_found`, `invalid`, `rate_limited`, `namespace_limit`, ...), `.message`, `.fields` (invalid input) and `.retry_after`; 429 and
503 answers are retried for you (after `Retry-After`) up to 3 times.

It talks to `https://api.skimmerdb.com`; point it at another server with `base_url=` or `SKIMMERDB_URL` (e.g. `http://127.0.0.1:8080`).

## The whole API

Every operation in the [API reference](https://docs.skimmerdb.com/api) is generated
from the [OpenAPI document](https://api.skimmerdb.com/openapi.json) into `skimmerdb._api`
(httpx, attrs models, sync and async), named by its operationId:

```python
from skimmerdb._api.api.search import search
from skimmerdb._api.models import SearchRequest

res = search.sync(name="support", client=db.api, body=SearchRequest(q="refund", limit=5))
res = await search.asyncio(name="support", client=db.api, body=SearchRequest(q="refund"))
```

`skimmerdb/_api` is generated: don't edit it by hand.

## Tests

The tests run against a SkimmerDB server given by `SKIMMERDB_URL` (they sign up throwaway
accounts, so don't point them at production) and are skipped when none answers. They run
against a local server before every release.

```sh
pip install -e '.[test]'
SKIMMERDB_URL=http://127.0.0.1:8080 python -m pytest -q
```

## Source

This repository is a snapshot of the client published with each release; `skimmerdb/_api` is generated
from the OpenAPI document, so changes to it come from the API. Issues and pull requests to the
hand-written layer (`skimmerdb/__init__.py`) are welcome: https://github.com/SkimmerDB/skimmerdb-python
