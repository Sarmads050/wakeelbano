# -*- coding: utf-8 -*-
"""WakeelBano — work out *how to apply* and the *last date* for every job.

Two columns in `jobs` answer the questions a lawyer actually has before
applying, and both feed the alert email:

    how_to_apply  short instruction, derived from the source that listed the job
    deadline      last date, only where the source states one

Nothing here invents a date. If a listing does not give a closing date the
column stays empty and the email says "not stated on the listing — check the
source", which is the honest answer and keeps us from costing someone a job.

    python3 scripts/jobs_apply_info.py            # dry run
    python3 scripts/jobs_apply_info.py --apply    # write to Supabase
"""
import os
import sys

# Exact instructions per source. Keep them short: one line, no jargon.
BY_SOURCE = [
    ("rozee", "Apply on the Rozee.pk listing (link below). Keep a Rozee profile with your CV uploaded — most employers only reply through it."),
    ("indeed", "Apply on Indeed using the link below. Have a one-page PDF CV ready, plus a short writing sample."),
    ("legalalphabet", "Open the employer's own careers page from the link below before applying — the salary shown on the aggregator is indicative, not an offer."),
    ("glassdoor", "Apply through the Glassdoor link below. If the firm's own careers page is listed, apply there instead — it is checked more often."),
    ("linkedin", "Apply on LinkedIn, then send a short message to the hiring manager in the same thread — it doubles your chance of a reply."),
    ("ppsc", "Apply online at ppsc.gop.pk. The fee is paid through a PSID at any bank or via 1-Link; keep the challan copy."),
    ("fpsc", "Apply online at fpsc.gov.pk. Fee is paid through PSID or 1-Link; the online form is the only accepted route."),
    ("secp", "Apply through SECP's careers portal. Attach CV, degrees and a covering letter in one PDF."),
    ("ministry of law", "Apply through the National Job Portal (NJP). The advertisement PDF lists the exact documents required."),
    ("hkn", "Email your CV and a writing sample to the address on hkn.com.pk/careers — the writing sample decides the shortlist."),
    ("jsa", "Apply through jsalaw.com/careers. Their intake is interns only; passed-out LLBs are not eligible for that route."),
    ("zm law", "Apply through zmlaw.com.pk/careers-2 with CV and covering letter."),
    ("al haqq", "Apply through the firm's careers page with CV and a covering letter addressed to the partner."),
]

BY_ORG = [
    ("haidermota", "Partner-track hiring runs through the firm's own portal — apply there, not through the aggregator."),
    ("vellani", "Apply on the firm's own careers page; mention the exact practice group in your covering letter."),
    ("mandviwalla", "Apply on the firm's page or the listing below; a two-page CV and a drafting sample are expected."),
    ("surridge", "Apply to the firm directly with CV and a short covering letter."),
    ("riaa", "Apply through RIAA Barker Gillette's careers page; competition-law experience should be the first line of your CV."),
]

PUBLIC_INSTRUCTION = ("Open the original listing with the link below, check the requirements there, "
                      "and apply through the employer's own channel.")


def how_to_apply(job):
    blob = " ".join(str(job.get(k) or "") for k in ("source", "org", "title")).lower()
    for key, text in BY_ORG:
        if key in blob:
            return text
    for key, text in BY_SOURCE:
        if key in blob:
            return text
    return PUBLIC_INSTRUCTION


def deadline(job):
    """Only a date the source actually gives. Nothing guessed."""
    d = job.get("deadline")
    if d:
        return str(d)[:10]
    return None


def describe(job):
    return how_to_apply(job), deadline(job)


def apply_to_db():
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    import db  # noqa: E402

    code, rows = db.rest("GET", "jobs?select=id,title,org,source,how_to_apply,deadline")
    if code != 200:
        sys.exit(f"read failed: {code} {rows}")

    changed = 0
    for row in rows:
        hta = how_to_apply(row)
        if hta == row.get("how_to_apply"):
            continue
        changed += 1
        if "--apply" in sys.argv:
            c, _ = db.rest("PATCH", f"jobs?id=eq.{row['id']}", {"how_to_apply": hta},
                           prefer="return=minimal")
            if c not in (200, 204):
                print(f"ERR {row['id']}")
        else:
            print(f"    {row['id']:<4} {hta[:78]}")
    print(f"{changed} row(s) {'updated' if '--apply' in sys.argv else 'would change'} of {len(rows)}")


if __name__ == "__main__":
    apply_to_db()
