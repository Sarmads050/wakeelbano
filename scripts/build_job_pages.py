# -*- coding: utf-8 -*-
"""WakeelBano — one page per open job: /jobs/<id>/

Why pages instead of a popup: a lawyer can share the link on WhatsApp, Google can
index it (each page carries JobPosting structured data), and the apply button is
on the page itself so nobody has to hunt for it.

    python3 scripts/build_job_pages.py

Pages are written to jobs/<id>/index.html. Closed postings get no page.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import build_pages as BP  # noqa: E402  (reuses page(), CSS, NAV, FOOTER)
from jobs_data import JOBS as _BASE  # noqa: E402
from jobs_data_more import EXTRA_JOBS  # noqa: E402
from jobs_normalize import job_type, sector  # noqa: E402
from jobs_apply_info import how_to_apply  # noqa: E402
from job_page_css import CSS as JOB_CSS  # noqa: E402

CLOSED_IDS = {"j59", "j60"}

EMPLOYMENT = {
    "Full-time": "FULL_TIME",
    "Part-time": "PART_TIME",
    "Contract": "CONTRACTOR",
    "Remote": "FULL_TIME",
    "Per case": "PER_ATTEMPT",
    "Internship": "INTERN",
    "Trainee": "INTERN",
    "Government": "FULL_TIME",
}

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def pretty(d):
    try:
        y, m, day = str(d)[:10].split("-")
        return f"{int(day)} {MONTHS[int(m) - 1]} {y}"
    except Exception:
        return ""


def esc(t):
    return (str(t or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def normalise(job):
    j = dict(job)
    j["job_type"] = job_type(job.get("type") or job.get("job_type"))
    j["sector"] = sector(j)
    j["how_to_apply"] = how_to_apply({"source": job.get("src"), "org": job.get("org"),
                                      "title": job.get("t")})
    j["deadline"] = job.get("deadline")
    return j


def salary_node(pay):
    """Only when the listing states a range. Never invented."""
    if not pay or pay.lower().startswith("not stated"):
        return None
    digits = "".join(ch if ch.isdigit() else " " for ch in pay).split()
    nums = [int(x) for x in digits if x.isdigit() and len(x) >= 3]
    if not nums:
        return None
    node = {"@type": "MonetaryAmount", "currency": "PKR",
            "value": {"@type": "QuantitativeValue", "unitText": "MONTH"}}
    if len(nums) >= 2:
        node["value"]["minValue"] = min(nums[0], nums[1])
        node["value"]["maxValue"] = max(nums[0], nums[1])
    else:
        node["value"]["value"] = nums[0]
    return node


def days_to(d):
    try:
        import datetime
        y, m, day = [int(x) for x in str(d)[:10].split("-")]
        left = (datetime.date(y, m, day) - datetime.date.today()).days
        return left
    except Exception:
        return None


def deadline_block(job):
    left = days_to(job.get("deadline"))
    if left is None:
        return ('<div class="deadline none"><div><b>Last date: not stated on the listing</b>'
                'Open the source page and check the closing date there before you apply — '
                'government posts in particular close without notice.</div></div>')
    pretty_d = pretty(job["deadline"])
    if left < 0:
        return (f'<div class="deadline none"><div><b>This post has closed</b>'
                f'The listing closed on {pretty_d}. The page is kept so you can see the route '
                f'and apply in the next cycle.</div></div>')
    if left <= 10:
        return (f'<div class="deadline urgent"><div><b>Closing soon — {left} day'
                f'{"s" if left != 1 else ""} left</b>Last date is {pretty_d}. Apply now.</div></div>')
    return (f'<div class="deadline"><div><b>Last date: {pretty_d}</b>'
            f'You have {left} days. Confirm on the source page before applying.</div></div>')


def build(job, all_jobs):
    j = normalise(job)
    jid = j["id"]
    slug = f"jobs/{jid}/"
    root = "../../"
    url = BP.BASE + slug

    apply_href = esc(j["url"]) if j["url"] else f"{root}jobs/#jobs"
    apply_text = "Apply here &rarr;"
    external = ' target="_blank" rel="nofollow noopener"' if j["url"] else ""

    same = [o for o in all_jobs if o["id"] != jid and o.get("area") == job.get("area")][:3]
    more = "".join(
        f'<a class="tile" href="{root}jobs/{esc(o["id"])}/index.html">'
        f'<b>{esc(o["t"])}</b><span>{esc(o["org"])} · {esc(o["city"])} · {esc(o["pay"])}</span></a>'
        for o in same)

    how = esc(j["how_to_apply"])
    pay = esc(j["pay"] or "Not stated")
    exp = esc(j["exp"] or "Not stated")

    body = f"""
<div class="job-page">
<section class="hero"><div class="wrap">
  <div class="kicker">{esc(j["sector"])} &middot; {esc(j["city"])}</div>
  <h1>{esc(j["t"])}</h1>
  <p class="org-line">{esc(j["org"])} <span>&middot; hiring in {esc(j["city"])}</span></p>
  <div class="pills">
    <span class="pill gold">{esc(j["job_type"])}</span>
    <span class="pill">{esc(j["area"])}</span>
    <span class="pill ghost">Experience: {exp}</span>
    <span class="pill ghost">Posted {esc(pretty(j["posted"]))}</span>
  </div>
</div></section>

<main class="wrap">
  <div class="jobgrid">

    <div class="col-main">
      <div class="snap">
        <dl>
          <div class="cell"><dt>Practice area</dt><dd>{esc(j["area"])}</dd></div>
          {"" if j["sector"].lower() == j["area"].lower() else f'<div class="cell"><dt>Sector</dt><dd>{esc(j["sector"])}</dd></div>'}
          <div class="cell"><dt>Location</dt><dd>{esc(j["city"])}</dd></div>
          <div class="cell"><dt>Job type</dt><dd>{esc(j["job_type"])}</dd></div>
          <div class="cell"><dt>Experience</dt><dd>{exp}</dd></div>
          <div class="cell"><dt>Pay</dt><dd>{pay}</dd></div>
        </dl>
      </div>

      {deadline_block(j)}

      <h2>What the job involves</h2>
      <p class="lead">{esc(j["desc"])}</p>

      <h2>How to apply</h2>
      <p class="lead">{how}</p>
      <ol class="steps">
        <li><b>Open the original listing.</b> The button on the right (and at the bottom of this
            page) takes you straight to {esc(j["src"])}, where the application is actually made.
            WakeelBano is not an employer and takes no fee from candidates.</li>
        <li><b>Keep the papers ready.</b> One-page CV, LLB/LLM degree, Sindh Bar Council enrolment
            certificate, CNIC, and for litigation roles a short drafting sample.</li>
        <li><b>Write the first line for the reader.</b> Name the exact role, your enrolment year,
            and one case or transaction you handled. Two sentences are enough.</li>
        <li><b>Follow up once.</b> If there is no reply in a week, send one short email. Do not
            send a third.</li>
      </ol>

      <h2>Before you apply</h2>
      <ul class="check">
        <li><b>Confirm the last date</b> on the source page — that listing is the only reliable
            date, and some employers close early once they have enough applicants.</li>
        <li><b>Check the experience requirement</b> against your own record: this post asks for
            <b>{exp}</b>. If you are one year short, apply anyway and say why you are ready —
            many chambers are flexible about the number and firm about the writing.</li>
        <li><b>Never pay money</b> for a legal job or pupillage. No genuine chamber charges a
            joining fee, and a request for one is a scam.</li>
        <li><b>Keep a record.</b> Note where and when you applied, so a follow-up is easy and the
            next interview does not catch you out.</li>
      </ul>

      {"<h2>Similar openings</h2><div class=\"grid\">" + more + "</div>" if more else ""}

      <a class="btn-apply-bottom" href="{apply_href}"{external}>Apply here &rarr;</a>

      <div class="cta-box">
        <div><h3>Get jobs like this by email</h3>
          <p>Subscribe once and new legal jobs in your city and practice area arrive daily.</p></div>
        <a class="btn" href="{root}jobs/#jobs">Set up job alerts &rarr;</a>
      </div>
    </div>

    <aside class="col-side">
      <div class="applycard">
        <div class="pay"><small>Pay</small>{pay}</div>
        <div class="rowline"><span>Experience</span><b>{exp}</b></div>
        <div class="rowline"><span>Location</span><b>{esc(j["city"])}</b></div>
        <div class="rowline"><span>Type</span><b>{esc(j["job_type"])}</b></div>
        <div class="rowline"><span>Last date</span><b>{esc(pretty(j["deadline"])) if j["deadline"] else "Not stated"}</b></div>
        <a class="btn-apply" href="{apply_href}"{external}>{apply_text}</a>
        <p class="note">Opens the original listing on <b>{esc(j["src"])}</b>. No fee, no middleman —
        the application goes to the employer.</p>
        <div class="verified">&#10003; Sourced {esc(pretty(j["posted"]))} from {esc(j["src"])}</div>
      </div>
    </aside>

  </div>
</main>
</div>"""

    title = f"{j['t']} at {j['org']} — {j['city']} | {BP.BRAND}"
    desc = (f"{j['t']} at {j['org']}, {j['city']}. {j['exp'] or 'Experience not stated'}, "
            f"pay {j['pay'] or 'not stated'}. How to apply and the source link.")[:158]

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "JobPosting",
                "title": j["t"],
                "description": j["desc"],
                "datePosted": str(j["posted"])[:10],
                "employmentType": EMPLOYMENT.get(j["job_type"], "FULL_TIME"),
                "hiringOrganization": {"@type": "Organization", "name": j["org"]},
                "jobLocation": {
                    "@type": "Place",
                    "address": {"@type": "PostalAddress",
                                "addressLocality": j["city"],
                                "addressCountry": "PK"},
                },
                "url": url,
                "directApply": False,
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": BP.BASE},
                    {"@type": "ListItem", "position": 2, "name": "Legal jobs",
                     "item": BP.BASE + "jobs/"},
                    {"@type": "ListItem", "position": 3, "name": j["t"], "item": url},
                ],
            },
        ],
    }
    sal = salary_node(j["pay"])
    if sal:
        schema["@graph"][0]["baseSalary"] = sal
    if j["deadline"]:
        schema["@graph"][0]["validThrough"] = str(j["deadline"])[:10]

    html = BP.page(title, desc, slug, body, slug, schema, extra_css=JOB_CSS)
    out = os.path.join(ROOT, "jobs", jid)
    os.makedirs(out, exist_ok=True)
    io.open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)
    return slug


def main():
    jobs = [j for j in (_BASE + EXTRA_JOBS) if j["id"] not in CLOSED_IDS]
    slugs = [build(j, jobs) for j in jobs]
    print(f"{len(slugs)} job pages written under jobs/<id>/index.html")
    return slugs


if __name__ == "__main__":
    main()
