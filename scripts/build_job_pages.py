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


def build(job, all_jobs):
    j = normalise(job)
    jid = j["id"]
    slug = f"jobs/{jid}/"
    root = "../../"
    url = BP.BASE + slug

    if j["deadline"]:
        deadline_html = (f'<span class="pill warn">Last date: {esc(pretty(j["deadline"]))}</span>')
    else:
        deadline_html = ('<span class="pill">Last date: not stated on the listing — '
                         'confirm on the source page</span>')

    apply_btn = (f'<a class="btn" style="font-size:16px;padding:15px 26px" href="{esc(j["url"])}" '
                 f'target="_blank" rel="nofollow noopener">Apply here →</a>' if j["url"]
                 else f'<a class="btn" style="font-size:16px;padding:15px 26px" href="{root}jobs/#jobs">'
                      f'Apply through WakeelBano →</a>')

    same = [o for o in all_jobs
            if o["id"] != jid and o.get("area") == job.get("area")][:4]
    more = "".join(
        f'<li><a href="{root}jobs/{esc(o["id"])}/index.html">{esc(o["t"])}</a> '
        f'<span style="color:#7A8794">— {esc(o["org"])}, {esc(o["city"])}</span></li>'
        for o in same)

    body = f"""
{BP.crumbs(root, esc(j["t"]), ["jobs"])}
<section class="hero"><div class="wrap">
  <div class="kicker">{esc(j["sector"])} · {esc(j["city"])}</div>
  <h1>{esc(j["t"])}</h1>
  <p>{esc(j["org"])} is hiring in {esc(j["city"])}. {esc(j["desc"])}</p>
</div></section>
<main class="wrap">
  <div class="facts">
    <div><b>Practice area</b><span>{esc(j["area"])}</span></div>
    <div><b>Type</b><span>{esc(j["job_type"])}</span></div>
    <div><b>Experience</b><span>{esc(j["exp"] or "Not stated")}</span></div>
    <div><b>Pay</b><span>{esc(j["pay"] or "Not stated")}</span></div>
    <div><b>Location</b><span>{esc(j["city"])}</span></div>
    <div><b>Posted</b><span>{esc(pretty(j["posted"]))}</span></div>
  </div>

  <p style="margin:0 0 22px">{deadline_html}</p>

  <h2>How to apply</h2>
  <p>{esc(j["how_to_apply"])}</p>
  <p style="margin:22px 0 8px">{apply_btn}</p>
  <p style="font-size:13px;color:#7A8794">
    This button opens the original listing at <b>{esc(j["src"])}</b> — the place where the
    application is actually made. Salaries and dates are copied from that listing; confirm them
    there before you apply. WakeelBano takes no fee from candidates or employers.
  </p>

  <h2>What the job involves</h2>
  <p>{esc(j["desc"])}</p>

  <h2>Good to know before you apply</h2>
  <ul>
    <li><b>Check the last date</b> on the source page — the listing is the only reliable date.</li>
    <li><b>Keep the documents ready</b>: one-page CV, LLB/LLM degree, enrolment certificate,
        CNIC, and for litigation roles a short drafting sample.</li>
    <li><b>Write the first line of your email for the reader</b>: the exact role, your enrolment
        year, and one case or transaction you handled.</li>
    <li><b>Do not pay anyone</b> for a legal job. No genuine chamber charges a joining fee.</li>
  </ul>

  {"<h2>Similar openings</h2><ul>" + more + "</ul>" if more else ""}

  <div class="cta-box">
    <div><h3>Get these jobs by email</h3>
      <p>Subscribe once and new legal jobs in your city and practice area arrive in your inbox.</p></div>
    <a class="btn" href="{root}jobs/#jobs" onclick="location.href='{root}jobs/';return false;">Set up job alerts →</a>
  </div>
</main>"""

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
                    {"@type": "ListItem", "position": 1, "name": "Home",
                     "item": BP.BASE},
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

    html = BP.page(title, desc, slug, body, slug, schema)
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
