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
WELCOME_DAYS = 30   # first digest for a brand-new subscriber: last 30 days of jobs
MAX_JOBS = 0        # 0 = every matching opening, always
FEATURED = 8        # jobs shown as full cards; the rest get compact rows with the same details   # first digest for a brand-new subscriber: last 30 days of jobs


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


WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def pretty_date(value):
    d = parse_dt(str(value)[:10] + "T00:00:00+00:00") if value else None
    if not d:
        return None
    return f"{WEEKDAYS[d.weekday()]} {d.day} {MONTHS[d.month - 1]} {d.year}"


def days_left(value):
    d = parse_dt(str(value)[:10] + "T00:00:00+00:00") if value else None
    if not d:
        return None
    return (d - datetime.datetime.now(datetime.timezone.utc)).days


def closing_line(job):
    """Returns (text, is_urgent) for the last-date row."""
    left = days_left(job.get("deadline"))
    pretty = pretty_date(job.get("deadline"))
    if left is None:
        return "Last date not stated on the listing — confirm it on the source page before you apply.", False
    if left < 0:
        return f"Closed on {pretty}.", False
    if left == 0:
        return f"<b>Closes today</b> — {pretty}.", True
    if left <= 10:
        return f"<b>Closing soon</b> — {left} day{'s' if left != 1 else ''} left ({pretty}).", True
    return f"Last date: {pretty}.", False


def meta_line(label, value):
    if not value:
        return ""
    return (f'<tr><td style="padding:2px 0;font-size:14px;color:#7A8794;width:104px;'
            f'vertical-align:top">{label}</td>'
            f'<td style="padding:2px 0;font-size:15px;color:#1F2D3A">{value}</td></tr>')


def job_card(job, index, total):
    title = job.get("title") or "Legal opening"
    org = job.get("org") or ""
    city = job.get("city") or ""
    area = job.get("area") or ""
    jtype = job.get("job_type") or ""
    sector = job.get("sector") or ""
    exp = job.get("experience") or "Not stated"
    pay = job.get("pay") or "Not stated"
    posted = pretty_date(job.get("posted_at"))
    closing, urgent = closing_line(job)
    how = job.get("how_to_apply") or (
        "Open the original listing with the link below and apply through the employer's own channel.")
    url = job.get("source_url") or (SITE + "/jobs/")
    source = job.get("source") or "WakeelBano"

    badge = ""
    if urgent:
        badge = ('<span style="display:inline-block;background:#FDECEC;color:#9B1C1C;'
                 'font-size:12px;font-weight:700;padding:3px 8px;border-radius:99px;'
                 'margin-left:6px">&#9200; Urgent</span>')

    return f"""
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
           style="width:100%;margin:0 0 14px;border:1px solid #E3E8EE;border-radius:12px;background:#FFFFFF">
      <tr><td style="padding:16px 16px 6px">
        <div style="font-size:12px;color:#9AA6B2;letter-spacing:.09em;text-transform:uppercase;font-weight:700">Job {index} of {total}</div>
        <div style="font-size:18px;line-height:1.3;font-weight:700;color:#0B2545;margin-top:4px">{title}{badge}</div>
        <div style="font-size:15px;color:#3E4C59;margin-top:3px">{org}</div>
      </td></tr>
      <tr><td style="padding:4px 16px 0">
        <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="width:100%">
          {meta_line("Location", city)}
          {meta_line("Practice", area + ((" &middot; " + sector) if sector else ""))}
          {meta_line("Type", jtype)}
          {meta_line("Experience", exp)}
          {meta_line("Pay", pay)}
          {meta_line("Posted", posted)}
        </table>
      </td></tr>
      <tr><td style="padding:10px 16px 0">
        <div style="font-size:15px;line-height:1.5;color:{'#9B1C1C' if urgent else '#3E4C59'};background:{'#FDF3F3' if urgent else '#F7F9FB'};border-radius:8px;padding:10px 12px">
          {closing}
        </div>
      </td></tr>
      <tr><td style="padding:12px 16px 0">
        <div style="font-size:13px;font-weight:700;color:#0B2545;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px">How to apply</div>
        <div style="font-size:15px;line-height:1.55;color:#1F2D3A">{how}</div>
      </td></tr>
      <tr><td style="padding:14px 16px 16px">
        <a href="{url}" style="display:block;background:#0B2545;color:#FFFFFF;text-decoration:none;
           font-size:15px;font-weight:700;text-align:center;padding:13px 16px;border-radius:9px">
           Open this job &amp; apply &rarr;</a>
        <div style="font-size:12px;color:#9AA6B2;margin-top:8px;line-height:1.5">
          Source: {source} &middot; verify the deadline and salary on the source before applying.
        </div>
      </td></tr>
    </table>"""


def order_jobs(jobs):
    """Urgent deadlines first, then newest postings. A lawyer should never have to
    scroll past a job that closes tomorrow to reach one from last month."""
    def key(j):
        left = days_left(j.get("deadline"))
        urgent = left if left is not None and left >= 0 else 9999
        posted = str(j.get("posted_at") or "")
        return (urgent, [-ord(c) for c in posted])
    return sorted(jobs, key=key)


def job_row(job):
    """Compact row for the long tail: still carries location, experience, pay,
    last date and the apply instruction, just without the big card."""
    title = job.get("title") or "Legal opening"
    url = job.get("source_url") or (SITE + "/jobs/")
    closing, urgent = closing_line(job)
    bits = []
    for label, value in (("Location", job.get("city")),
                         ("Type", job.get("job_type")),
                         ("Experience", job.get("experience")),
                         ("Pay", job.get("pay"))):
        if value and value != "Not stated":
            bits.append(f"{label}: {value}")
    how = job.get("how_to_apply") or ""
    return f"""
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
           style="width:100%;border-top:1px solid #EDF1F4">
      <tr><td style="padding:13px 0">
        <a href="{url}" style="font-size:16px;font-weight:700;color:#0B2545;text-decoration:none;line-height:1.35">{title}</a>
        <div style="font-size:14px;color:#3E4C59;margin-top:2px">{job.get('org') or ''}</div>
        <div style="font-size:13px;color:#7A8794;margin-top:4px;line-height:1.5">{' &middot; '.join(bits)}</div>
        <div style="font-size:13px;color:{'#9B1C1C' if urgent else '#7A8794'};margin-top:3px;line-height:1.5">{closing}</div>
        <div style="font-size:13px;color:#5E6B78;margin-top:5px;line-height:1.5"><b style="color:#0B2545">How to apply:</b> {how}</div>
      </td></tr>
    </table>"""


def section(title, subtitle, body):
    return f"""
    <tr><td style="background:#FFFFFF;padding:18px 20px 0">
      <div style="font-size:17px;font-weight:700;color:#0B2545">{title}</div>
      {f'<div style="font-size:13.5px;color:#7A8794;margin-top:3px;line-height:1.5">{subtitle}</div>' if subtitle else ''}
    </td></tr>
    <tr><td style="background:#FFFFFF;padding:10px 20px 0">{body}</td></tr>"""


def email_html(sub, jobs, total_open=None):
    name = (sub.get("email") or "there").split("@")[0]
    head = f"{len(jobs)} legal job{'s' if len(jobs) != 1 else ''}"
    order = order_jobs(jobs)
    urgent = [j for j in order if (days_left(j.get("deadline")) is not None
                                   and 0 <= days_left(j.get("deadline")) <= 10)]
    rest = [j for j in order if j not in urgent]
    featured = rest[:max(0, FEATURED - len(urgent))]
    tail = [j for j in rest if j not in featured]

    blocks = []
    if urgent:
        blocks.append(section("&#9200; Closing soon",
                              "These have a stated last date within ten days. Apply first.",
                              "".join(job_card(j, i + 1, len(urgent)) for i, j in enumerate(urgent))))
    if featured:
        blocks.append(section("Newest openings", "Full details for each role.",
                              "".join(job_card(j, i + 1, len(featured)) for i, j in enumerate(featured))))
    if tail:
        blocks.append(section(f"All other openings ({len(tail)})",
                              "Location, experience, pay, last date and how to apply for every one of them.",
                              "".join(job_row(j) for j in tail)))
    cards = "".join(blocks)
    return f"""<!doctype html>
<html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>WakeelBano job alert</title></head>
<body style="margin:0;padding:0;background:#F1F4F7;-webkit-text-size-adjust:100%">
<div style="display:none;font-size:1px;color:#F1F4F7">{head} matched your filters</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#F1F4F7">
<tr><td align="center" style="padding:16px 10px">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
         style="width:100%;max-width:600px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif">

    <tr><td style="background:#0B2545;border-radius:14px 14px 0 0;padding:22px 20px">
      <div style="font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:#C8A24A;font-weight:700">WakeelBano</div>
      <div style="font-size:23px;line-height:1.25;font-weight:700;color:#FFFFFF;margin-top:6px">{head} for you</div>
      <div style="font-size:14px;color:#B8C7D4;margin-top:8px">
        {sub.get('city') or 'All cities'} &middot; {sub.get('area') or 'All areas'}{(' &middot; ' + sub['keyword']) if sub.get('keyword') else ''}
      </div>
    </td></tr>

    <tr><td style="background:#FFFFFF;padding:18px 20px 4px">
      <p style="font-size:15px;line-height:1.6;color:#3E4C59;margin:0 0 14px">
        Assalam-o-alaikum {name}, here are the openings that match your filters.
        Every one of them is a real listing, and the button in each card takes you to the original source.
      </p>
    </td></tr>

    {cards}

    <tr><td style="background:#FFFFFF;padding:6px 20px 20px">
      <a href="{SITE}/jobs/" style="display:block;background:#C8A24A;color:#0B2540;text-decoration:none;
         font-size:15px;font-weight:700;text-align:center;padding:13px 16px;border-radius:9px">
         See all {total_open or ''} openings on WakeelBano &rarr;</a>
    </td></tr>

    <tr><td style="background:#FFFFFF;border-radius:0 0 14px 14px;padding:0 20px 22px">
      <div style="border-top:1px solid #E3E8EE;padding-top:14px;font-size:12.5px;line-height:1.6;color:#8A97A4">
        You are getting this because you subscribed to job alerts on WakeelBano.
        Salaries and dates come from the source page — always confirm before applying.<br>
        To stop these emails, reply with <b>stop</b> and we remove the address the same day.
      </div>
    </td></tr>

    <tr><td style="padding:14px 20px;font-size:12px;color:#9AA6B2;text-align:center">
      WakeelBano &middot; <a href="{SITE}/jobs/" style="color:#7A8794">Jobs</a> &middot;
      <a href="{SITE}/" style="color:#7A8794">Home</a>
    </td></tr>

  </table>
</td></tr></table>
</body></html>"""


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
        fresh = order_jobs(fresh)
        if MAX_JOBS:
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
        sample = order_jobs(jobs)
        html = email_html({"email": args.to, "city": "All cities", "area": "All areas"},
                          sample, total_open=len(jobs))
        code, body = send_resend(key, args.to, "WakeelBano test alert", html)
        print(f"test email: {code} {body}")

    print(f"done · {sent} email(s) sent")


if __name__ == "__main__":
    main()
