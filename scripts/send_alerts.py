# -*- coding: utf-8 -*-
"""WakeelBano — job alert sender.

Reads subscribers and live jobs from Supabase, matches each subscriber's
filters, emails a digest of NEW openings, and records when they were last sent.

    python3 scripts/send_alerts.py --dry-run          # show what would go out
    python3 scripts/send_alerts.py                    # actually send
    python3 scripts/send_alerts.py --to me@x.com --test   # one test email

Email provider: Resend (free tier = 100 emails/day, 3,000/month).
Put the key in .secrets/resend_key  (Dashboard -> API Keys -> Create).
Verify wakeelbano.com — or the current sender domain — under Resend -> Domains,
then set EMAIL_FROM below. Until the domain is verified you can only send to
your own Resend account address; that is fine for testing.

Sending is idempotent: a subscriber only gets jobs posted after their
`last_sent_at` (or after their signup), so nothing is emailed twice.
"""
import argparse
import datetime
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import db  # noqa: E402

def from_address():
    """Sender address.

    Until a domain is verified in Resend you can only send from
    onboarding@resend.dev, and only to the address that owns the Resend
    account. After verifying wakeelbano.com, write the real sender into
    .secrets/resend_from, e.g.
        WakeelBano Job Alerts <alerts@wakeelbano.com>
    """
    if os.environ.get("RESEND_FROM"):
        return os.environ["RESEND_FROM"].strip()
    path = os.path.join(ROOT, ".secrets", "resend_from")
    if os.path.exists(path):
        return io.open(path, encoding="utf-8").read().strip()
    return "WakeelBano <onboarding@resend.dev>"
SITE = "https://sarmads050.github.io/wakeelbano"
MAX_JOBS = 12
WELCOME_DAYS = 30   # first digest for a brand-new subscriber: last 30 days of jobs


# ---------------------------------------------------------------- helpers
def resend_key():
    if os.environ.get("RESEND_KEY"):
        return os.environ["RESEND_KEY"].strip()
    path = os.path.join(ROOT, ".secrets", "resend_key")
    if not os.path.exists(path):
        return ""
    return io.open(path, encoding="utf-8").read().strip()


def get(table, query=""):
    code, body = db.rest("GET", f"{table}?{query}")
    if code != 200:
        sys.exit(f"GET {table} failed: {code} {body}")
    return body


def parse_dt(s):
    if not s:
        return None
    s = s.replace("Z", "+00:00")
    try:
        return datetime.datetime.fromisoformat(s)
    except ValueError:
        return None


def matches(sub, job):
    """Subscriber filters vs a job row. Empty filter = match everything."""
    def ok(field, value):
        f = (sub.get(field) or "").strip().lower()
        if not f or f in ("all cities", "all areas"):
            return True
        return f == (value or "").strip().lower()

    if not ok("city", job.get("city")):
        return False
    if not ok("area", job.get("area")):
        return False

    kw = (sub.get("keyword") or "").strip().lower()
    if kw:
        haystack = " ".join(str(job.get(k) or "") for k in
                            ("title", "org", "description", "tags", "area", "city", "job_type")).lower()
        if not any(w and w in haystack for w in kw.replace(",", " ").split()):
            return False

    level = (sub.get("level") or "").lower()
    exp = (job.get("experience") or "").lower()
    if "student" in level or "fresh" in level:
        # no experience requirement, or explicitly open to fresh graduates
        if any(w in exp for w in ("2+", "3+", "5+", "7+", "10+")):
            return False
    return True


def money(job):
    return job.get("pay") or "Not stated"


def email_html(sub, jobs):
    name = (sub.get("email") or "").split("@")[0]
    rows = []
    for j in jobs:
        rows.append(f"""
        <tr><td style="padding:14px 0;border-bottom:1px solid #E6EAEE">
          <a href="{j.get('source_url') or SITE + '/jobs/'}" style="color:#0B2545;font-size:16px;font-weight:700;text-decoration:none">{j.get('title')}</a>
          <div style="color:#3E4C59;font-size:14px;margin-top:3px">{j.get('org')} &middot; {j.get('city')} &middot; {j.get('area')}</div>
          <div style="color:#5E6B78;font-size:13px;margin-top:3px">{money(j)} &middot; {j.get('experience') or 'Any'} &middot; posted {(j.get('posted_at') or 'recently')[:10]}</div>
          <div style="color:#7A8794;font-size:12px;margin-top:4px">Source: {j.get('source') or 'see listing'}</div>
        </td></tr>""")
    return f"""<!doctype html><html><body style="margin:0;background:#F4F6F8;font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif">
  <div style="max-width:600px;margin:0 auto;padding:24px">
    <div style="background:#0B2545;color:#fff;padding:22px 24px;border-radius:12px 12px 0 0">
      <div style="font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:#C8A24A">WakeelBano</div>
      <div style="font-size:22px;font-weight:700;margin-top:6px">New legal jobs for you</div>
    </div>
    <div style="background:#fff;padding:24px;border-radius:0 0 12px 12px">
      <p style="font-size:15px;color:#3E4C59;margin:0 0 8px">Assalam-o-alaikum {name},</p>
      <p style="font-size:15px;color:#3E4C59;margin:0 0 18px">{len(jobs)} new opening{'s' if len(jobs) != 1 else ''} matched your filters
        ({sub.get('city') or 'All cities'} &middot; {sub.get('area') or 'All areas'}{' &middot; ' + sub['keyword'] if sub.get('keyword') else ''}).</p>
      <table width="100%" cellpadding="0" cellspacing="0">{''.join(rows)}</table>
      <p style="margin:22px 0 0"><a href="{SITE}/jobs/" style="background:#C8A24A;color:#0B2545;font-weight:700;text-decoration:none;padding:12px 20px;border-radius:8px;display:inline-block">See all openings</a></p>
      <p style="font-size:12px;color:#7A8794;margin-top:22px;border-top:1px solid #E6EAEE;padding-top:14px">
        You are getting this because you subscribed on WakeelBano.
        Salaries and dates come from the source page — always check before applying.
        To stop these emails, reply with "stop" — we remove the address the same day.
      </p>
    </div>
  </div></body></html>"""


def send_resend(key, to, subject, html):
    import urllib.error
    import urllib.request
    body = json.dumps({"from": from_address(), "to": [to], "subject": subject, "html": html}).encode()
    req = urllib.request.Request("https://api.resend.com/emails", data=body, method="POST")
    req.add_header("Authorization", f"Bearer {key}")
    req.add_header("Content-Type", "application/json")
    # Resend sits behind Cloudflare, which rejects the default urllib user agent
    # with a misleading 403 / error code 1010. A named agent sails through.
    req.add_header("User-Agent", "WakeelBano/1.0")
    req.add_header("Accept", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--to", help="send a single test email to this address")
    ap.add_argument("--since", help="ISO date lower bound instead of last_sent_at")
    args = ap.parse_args()

    key = resend_key()
    if not args.dry_run and not key:
        sys.exit("missing .secrets/resend_key — create a free Resend key, or run with --dry-run")

    subs = get("subscribers", "status=eq.active&select=*")
    jobs = get("jobs", "status=eq.live&select=*")
    print(f"subscribers: {len(subs)} · live jobs: {len(jobs)}")

    floor = parse_dt(args.since) if args.since else None
    sent = 0
    for sub in subs:
        if not sub.get("email"):
            continue
        first = not sub.get("last_sent_at")
        cutoff = parse_dt(sub.get("last_sent_at"))
        if not cutoff:
            # A subscriber who has never had a digest should get a welcome batch of
            # recent openings, not silence because no job was posted after signup.
            signed = parse_dt(sub.get("created_at")) or datetime.datetime.now(datetime.timezone.utc)
            cutoff = signed - datetime.timedelta(days=WELCOME_DAYS)
        if floor and floor < cutoff:
            cutoff = floor
        fresh = [j for j in jobs
                 if matches(sub, j)
                 and (not cutoff or (parse_dt(j.get("created_at")) or datetime.datetime.now(datetime.timezone.utc)) > cutoff)]
        fresh = fresh[:MAX_JOBS]
        if not fresh:
            print(f"  - {sub['email']}: nothing new")
            continue
        subject = (f"Welcome to WakeelBano alerts — {len(fresh)} legal job"
                   f"{'s' if len(fresh) != 1 else ''} for you") if first else (
                  f"{len(fresh)} new legal job{'s' if len(fresh) != 1 else ''} on WakeelBano")
        html = email_html(sub, fresh)
        if args.dry_run:
            print(f"  * would send to {sub['email']}: {subject}")
            for j in fresh:
                print(f"      - {j.get('title')} @ {j.get('org')} ({j.get('city')})")
            continue
        code, body = send_resend(key, sub["email"], subject, html)
        if code in (200, 201):
            db.rest("PATCH", f"subscribers?id=eq.{sub['id']}",
                    {"last_sent_at": datetime.datetime.now(datetime.timezone.utc).isoformat()},
                    prefer="return=minimal")
            print(f"  + sent to {sub['email']}")
            sent += 1
        else:
            print(f"  ! failed {sub['email']}: {code} {body}")

    if args.to and args.test and key:
        html = email_html({"email": args.to, "city": "All cities", "area": "All areas"}, jobs[:5])
        code, body = send_resend(key, args.to, "WakeelBano test alert", html)
        print(f"test email: {code} {body}")

    print(f"done · {sent} email(s) sent")


if __name__ == "__main__":
    main()
