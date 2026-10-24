# -*- coding: utf-8 -*-
"""WakeelBano — database helper for the agent.

Reads the Supabase URL and secret key from .secrets/ (gitignored, never in the repo).

Usage
-----
    python3 scripts/db.py counts
    python3 scripts/db.py rows jobs              [limit]
    python3 scripts/db.py delete jobs id=eq.probe1
    python3 scripts/db.py insert jobs '{"id":"x1","title":"..."}'
    python3 scripts/db.py update jobs id=eq.x1 '{"status":"closed"}'
    python3 scripts/db.py sql "select count(*) from jobs"     (needs .secrets/supabase_access_token)

Notes
-----
* Data changes (rows) work with the secret API key.
* Schema changes (create/alter table) need a Supabase personal access token
  (`sbp_...`, Dashboard → Account → Access Tokens) saved in
  .secrets/supabase_access_token — or run the SQL by hand in the SQL Editor.
"""
import io
import json
import os
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRETS = os.path.join(ROOT, ".secrets")


def read(name, required=True):
    path = os.path.join(SECRETS, name)
    if not os.path.exists(path):
        if required:
            sys.exit(f"missing {path}")
        return ""
    return io.open(path, encoding="utf-8").read().strip()


URL = (os.environ.get("SUPABASE_URL") or read("supabase_url", required=False) or "").rstrip("/")
KEY = os.environ.get("SUPABASE_KEY") or read("supabase_key", required=False) or ""
if not URL or not KEY:
    sys.exit("no Supabase credentials: set SUPABASE_URL / SUPABASE_KEY, or put them in .secrets/")
PROJECT_REF = URL.split("//")[-1].split(".")[0]


def rest(method, path, body=None, prefer=None):
    req = urllib.request.Request(f"{URL}/rest/v1/{path}", method=method)
    req.add_header("apikey", KEY)
    req.add_header("Authorization", f"Bearer {KEY}")
    req.add_header("Content-Type", "application/json")
    if prefer:
        req.add_header("Prefer", prefer)
    data = json.dumps(body).encode() if body is not None else None
    try:
        with urllib.request.urlopen(req, data, timeout=30) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw.strip() else None)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def sql(query):
    token = read("supabase_access_token", required=False)
    if not token:
        sys.exit("No personal access token at .secrets/supabase_access_token — "
                 "run this SQL in the Supabase SQL Editor instead:\n\n" + query)
    req = urllib.request.Request(
        f"https://api.supabase.com/v1/projects/{PROJECT_REF}/database/query",
        method="POST",
        data=json.dumps({"query": query}).encode())
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read().decode() or "null")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cmd = sys.argv[1]

    if cmd == "counts":
        for t in ("jobs", "tasks", "lawyers", "applications", "ratings", "profiles"):
            s, d = rest("GET", f"{t}?select=id")
            print(f"{t:14} {len(d) if isinstance(d, list) else d}  (http {s})")

    elif cmd == "rows":
        table = sys.argv[2]
        limit = sys.argv[3] if len(sys.argv) > 3 else "20"
        s, d = rest("GET", f"{table}?select=*&limit={limit}")
        print(json.dumps(d, indent=2, ensure_ascii=False) if isinstance(d, (list, dict)) else d)

    elif cmd == "delete":
        table, flt = sys.argv[2], sys.argv[3]
        s, d = rest("DELETE", f"{table}?{flt}", prefer="return=minimal")
        print(f"delete {table} where {flt} -> http {s}")

    elif cmd == "insert":
        table, row = sys.argv[2], json.loads(sys.argv[3])
        s, d = rest("POST", table, row, prefer="return=minimal")
        print(f"insert {table} -> http {s} {d or ''}")

    elif cmd == "update":
        table, flt, patch = sys.argv[2], sys.argv[3], json.loads(sys.argv[4])
        s, d = rest("PATCH", f"{table}?{flt}", patch, prefer="return=minimal")
        print(f"update {table} where {flt} -> http {s}")

    elif cmd == "sql":
        s, d = sql(" ".join(sys.argv[2:]))
        print(json.dumps(d, indent=2, ensure_ascii=False) if isinstance(d, (list, dict)) else d)

    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
