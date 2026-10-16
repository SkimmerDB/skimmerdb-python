# From nothing to a first search: sign up (the answer has your key), write, search.
# SKIMMERDB_URL=http://127.0.0.1:8080 python examples/onboarding.py you@example.com 'a password'
import sys
from skimmerdb import SkimmerDB

db = SkimmerDB.signup(sys.argv[1], sys.argv[2])     # one call: account + full-access key
print("your key (shown once):", db.key)
ns = db.namespace("support")                         # the first write makes it
ns.write([{"id": "t-1", "text": "Refund requested for order ACME-1042", "meta": {"status": "open"}}], wait=True)
print([h.id for h in ns.search("refund").hits])
