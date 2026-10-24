# -*- coding: utf-8 -*-
"""Build jobs/index.html from scripts/jobs_template.html + scripts/jobs_data.py.

The page talks to Supabase through assets/wb-db.js when assets/supabase-config.js
holds a URL and anon key, and otherwise runs in local demo mode.
"""
import io, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_config import SITE_URL            # noqa: E402
from jobs_data import JOBS, TASKS, LAWYERS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = SITE_URL
TODAY = "2026-10-24"
DATA = {"jobs": JOBS, "tasks": TASKS, "lawyers": LAWYERS}


def main():
    tpl = io.open(os.path.join(ROOT, "scripts", "jobs_template.html"), encoding="utf-8").read()
    html = (tpl
            .replace("__BASE__", BASE)
            .replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
            .replace("__NJ__", str(len(JOBS)))
            .replace("__NT__", str(len(TASKS)))
            .replace("__NL__", str(len(LAWYERS)))
            .replace("__TODAY__", TODAY))
    out = os.path.join(ROOT, "jobs", "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    io.open(out, "w", encoding="utf-8").write(html)
    print(f"jobs/index.html written ({len(JOBS)} openings, {len(TASKS)} tasks, {len(LAWYERS)} profiles)")


if __name__ == "__main__":
    main()
