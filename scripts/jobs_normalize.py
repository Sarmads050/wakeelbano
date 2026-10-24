# -*- coding: utf-8 -*-
"""WakeelBano — clean up the job taxonomy so the filters on /jobs/ actually work.

Two problems this fixes:
  1. `job_type` values were free text ("Full-time · Onsite", "Permanent (PPSC)",
     "Associate or internship"), so the Type filter matched almost nothing.
     They are collapsed into eight canonical values.
  2. There was no way to separate law firms from in-house, government,
     immigration and remote work. A `sector` value is derived from the
     employer name and practice area.

Import `clean(job)` from the build scripts, or run this file to rewrite the
`job_type` / `sector` columns of the rows already in Supabase.

    python3 scripts/jobs_normalize.py            # dry run, prints a table
    python3 scripts/jobs_normalize.py --apply    # writes to Supabase
"""
import os
import sys

TYPES = ["Full-time", "Part-time", "Contract", "Remote",
         "Per case", "Internship", "Trainee", "Government"]

SECTORS = ["Law firm", "In-house", "Government", "Immigration", "Remote"]

GOV_ORGS = ("ppsc", "fpsc", "secp", "ministry of law", "cattle market",
            "exim bank", "state bank", "sbp", "nirc", "ombudsman", "courts",
            "attorney general", "law & justice", "law and justice")

INHOUSE_ORGS = ("jazz", "telenor", "ptcl", "hbl", "engro", "lucky cement",
                "yb group", "mtbc", "carecloud", "curemd", "zeta technologies",
                "anekor", "byonyks", "healthrix", "marie stopes", "perks hr",
                "hrhive", "avenair", "telecom infra", "hr force", "mks law")

IMMIGRATION_HINTS = ("immigration", "tashfeen", "aaraf", "visa", "migration")


def job_type(raw):
    t = (raw or "").lower()
    if "ppsc" in t or "fpsc" in t or "government" in t or "permanent" in t:
        return "Government"
    if "remote" in t:
        return "Remote"
    if "per case" in t or "per-case" in t:
        return "Per case"
    if "intern" in t:
        return "Internship"
    if "trainee" in t or "pupil" in t:
        return "Trainee"
    if "part-time" in t or "part time" in t or "retainer" in t:
        return "Part-time"
    if "contract" in t or "consult" in t:
        return "Contract"
    return "Full-time"


def sector(job):
    org = (job.get("org") or "").lower()
    area = (job.get("area") or "").lower()
    city = (job.get("city") or "").lower()
    tags = " ".join(job.get("tags") or []).lower()
    blob = f"{org} {area} {tags}"

    if any(g in blob for g in GOV_ORGS):
        return "Government"
    if any(i in blob for i in IMMIGRATION_HINTS):
        return "Immigration"
    if city == "remote" or job_type(job.get("job_type") or job.get("type")) == "Remote":
        return "Remote"
    if any(o in org for o in INHOUSE_ORGS):
        return "In-house"
    return "Law firm"


def clean(job):
    """Accepts either the build-script shape (t/exp/src/url) or the DB row shape."""
    out = dict(job)
    raw_type = out.get("job_type") or out.get("type") or ""
    out["job_type" if "job_type" in out or "job_type" not in out and "type" not in out else "type"] = job_type(raw_type)
    out["sector"] = sector(out)
    return out


def apply_to_db():
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    import db  # noqa: E402

    code, rows = db.rest("GET", "jobs?select=id,title,org,city,area,tags,job_type,sector")
    if code != 200:
        sys.exit(f"read failed: {code} {rows}")

    changed = 0
    for row in rows:
        new_t = job_type(row.get("job_type"))
        new_s = sector(row)
        if new_t == row.get("job_type") and new_s == row.get("sector"):
            continue
        changed += 1
        if "--apply" in sys.argv:
            c, body = db.rest("PATCH", f"jobs?id=eq.{row['id']}",
                              {"job_type": new_t, "sector": new_s}, prefer="return=minimal")
            print(f"{'ok ' if c in (200, 204) else 'ERR'} {row['id']:<4} {new_t:<11} {new_s:<11} {row['title'][:44]}")
        else:
            print(f"    {row['id']:<4} {new_t:<11} {new_s:<11} {row['title'][:44]}")
    print(f"{changed} row(s) {'updated' if '--apply' in sys.argv else 'would change'} of {len(rows)}")


if __name__ == "__main__":
    apply_to_db()
