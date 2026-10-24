# -*- coding: utf-8 -*-
"""
WakeelBano — static page builder (SEO + GEO).
Content lives in scripts/content_pages.py. Output: self-contained HTML pages,
sitemap.xml, robots.txt (AI crawlers allowed), llms.txt and llms-full.txt.

Usage: python3 scripts/build_pages.py
"""
import io, os, json, html, posixpath
import content_pages as C

from site_config import SITE_URL, GOOGLE_VERIFY, BING_VERIFY, SOCIAL  # noqa: E402

BASE = SITE_URL
BRAND = "WakeelBano"
TODAY = "2026-10-24"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSS = """
:root{--navy:#0B1B2B;--navy2:#12293D;--navy3:#1B3A52;--gold:#C9A227;--gold2:#E7CE7A;--gold-soft:#FBF3DC;
--cream:#FAF7F1;--ink:#0F1C2A;--muted:#5E6B78;--line:#E6DFD2;--green:#1F7A5C}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--cream);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;font-size:16.5px;line-height:1.65;-webkit-font-smoothing:antialiased}
h1,h2,h3,.serif{font-family:Georgia,"Times New Roman",serif;font-weight:700;letter-spacing:-.01em;line-height:1.22;margin:0}
a{color:#1B4E7A;text-decoration:none;border-bottom:1px solid rgba(27,78,122,.25)}
a:hover{color:var(--navy);border-bottom-color:var(--gold)}
header.top{position:sticky;top:0;z-index:50;background:rgba(11,27,43,.97);border-bottom:1px solid rgba(201,162,39,.3)}
.top-in{max-width:1080px;margin:0 auto;padding:0 20px;height:62px;display:flex;align-items:center;gap:14px}
.brand{display:flex;align-items:center;gap:9px;color:#fff;border:0}
.brand b{font-family:Georgia,serif;font-size:19px}
.brand small{display:block;font-size:9px;letter-spacing:.2em;color:var(--gold2);text-transform:uppercase;font-weight:700;margin-top:-3px}
.top nav{margin-left:auto;display:flex;gap:4px;flex-wrap:wrap}
.top nav a{color:#C8D3DC;font-size:13px;font-weight:600;padding:7px 10px;border-radius:8px;border:0}
.top nav a:hover{background:rgba(255,255,255,.08);color:#fff}
.top .cta{background:linear-gradient(180deg,#DDB845,#BE9A1F);color:#2A1F00;font-weight:800;padding:8px 14px;border-radius:9px;font-size:13px;border:0}
.wrap{max-width:1000px;margin:0 auto;padding:0 20px}
.crumbs{font-size:12.5px;color:var(--muted);padding:16px 0 0}
.crumbs a{border:0;color:var(--muted)}.crumbs a:hover{color:var(--navy)}
.crumbs span{color:#98A4B0}
.hero{background:linear-gradient(160deg,#0B1B2B,#15354D);color:#fff;padding:34px 0 38px;margin-bottom:32px}
.hero .kicker{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold2);font-weight:800}
.hero h1{font-size:clamp(26px,3.6vw,39px);margin:10px 0 12px;color:#fff}
.hero p{color:#C8D7E3;font-size:16.5px;max-width:740px;margin:0}
.answer{background:rgba(255,255,255,.08);border-left:3px solid var(--gold);border-radius:10px;padding:14px 16px;margin:16px 0 0;font-size:16px;color:#EAF1F6;max-width:820px}
.hero .meta{margin-top:16px;font-size:12.5px;color:#93A6B5;display:flex;gap:16px;flex-wrap:wrap}
h2{font-size:clamp(20px,2.4vw,26px);margin:34px 0 10px}
h3{font-size:18px;margin:22px 0 8px}
p{margin:0 0 14px}
ul,ol{margin:0 0 16px;padding-left:22px}
li{margin:6px 0}
table.tbl{width:100%;border-collapse:collapse;margin:8px 0 18px;font-size:14.5px;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden}
table.tbl th{background:#F3F0E9;text-align:left;padding:11px 13px;font-size:12.5px;letter-spacing:.04em;text-transform:uppercase;color:#4A5763;border-bottom:1px solid var(--line)}
table.tbl td{padding:11px 13px;border-bottom:1px solid #F0EBE0;vertical-align:top}
table.tbl tr:last-child td{border-bottom:0}
ol.steps{counter-reset:s;list-style:none;padding:0}
ol.steps li{counter-increment:s;position:relative;padding:12px 16px 12px 50px;background:#fff;border:1px solid var(--line);border-radius:12px;margin:0 0 10px}
ol.steps li:before{content:counter(s);position:absolute;left:14px;top:12px;width:24px;height:24px;border-radius:7px;background:var(--gold-soft);border:1px solid #EBD9A4;color:var(--navy);font-weight:800;font-size:13px;display:grid;place-items:center}
.callout{background:var(--gold-soft);border:1px solid #EBD9A4;border-radius:12px;padding:14px 16px;font-size:14.5px;margin:16px 0;color:#5F4A00}
.mini{font-size:13px;color:var(--muted)}
.facts{background:#fff;border:1px solid var(--line);border-radius:14px;padding:6px 18px;margin:8px 0 24px}
.facts h2{margin:16px 0 6px;font-size:17px;font-family:inherit;letter-spacing:.04em;text-transform:uppercase;color:#4A5763}
.facts dl{margin:0;display:grid;grid-template-columns:220px 1fr;gap:0}
.facts dt{font-size:13.5px;color:var(--muted);padding:8px 0;border-top:1px solid #F0EBE0}
.facts dd{margin:0;font-size:14px;padding:8px 0;border-top:1px solid #F0EBE0;font-weight:600;color:var(--navy)}
.cta-box{background:linear-gradient(150deg,#0B1B2B,#17394F);color:#fff;border-radius:16px;padding:24px;margin:36px 0;display:flex;gap:20px;align-items:center;justify-content:space-between;flex-wrap:wrap}
.cta-box h3{color:#fff;margin:0 0 6px;font-size:20px}
.cta-box p{margin:0;color:#BFCFDC;font-size:14px}
.cta-box a.btn{background:linear-gradient(180deg,#DDB845,#BE9A1F);color:#2A1F00;font-weight:800;padding:12px 20px;border-radius:10px;border:0;font-size:14px;white-space:nowrap}
.faq details{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin-bottom:10px}
.faq summary{font-weight:700;cursor:pointer;font-size:15.5px;list-style:none}
.faq summary::-webkit-details-marker{display:none}
.faq summary:before{content:"+";color:var(--gold);font-weight:800;margin-right:9px}
.faq details[open] summary:before{content:"–"}
.faq p{margin:10px 0 0;font-size:14.5px;color:#3E4C59}
.grid{display:grid;gap:14px;grid-template-columns:repeat(3,1fr)}
.grid.two{grid-template-columns:repeat(2,1fr)}
.tile{background:#fff;border:1px solid var(--line);border-radius:13px;padding:17px;display:block;transition:transform .14s,border-color .14s}
.tile:hover{transform:translateY(-2px);border-color:var(--gold)}
.tile b{display:block;font-family:Georgia,serif;font-size:16px;color:var(--navy);margin-bottom:4px}
.tile span{font-size:13px;color:var(--muted)}
.sources{background:#fff;border:1px solid var(--line);border-radius:13px;padding:6px 18px;margin:20px 0}
.sources h2{font-size:17px;font-family:inherit;letter-spacing:.04em;text-transform:uppercase;color:#4A5763;margin:16px 0 4px}
.sources ul{list-style:none;padding:0;margin:0 0 12px}
.sources li{padding:8px 0;border-top:1px solid #F0EBE0;font-size:14px}
.sources li i{font-style:normal;color:var(--muted);font-size:12px}
.disclaimer{background:#fff;border:1px dashed #D8CFBC;border-radius:12px;padding:16px;font-size:13px;color:#4A5763;margin:30px 0}
.related{margin:26px 0}
footer{background:#08131F;color:#93A6B5;padding:32px 0 22px;margin-top:50px;font-size:13.5px}
footer .fg{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:26px;margin-bottom:20px}
footer h5{color:#fff;font-size:11px;letter-spacing:.16em;text-transform:uppercase;margin:0 0 10px}
footer a{color:#A9BAC8;display:block;padding:3px 0;border:0;font-size:13px}
footer a:hover{color:var(--gold2)}
footer .fb{border-top:1px solid rgba(255,255,255,.1);padding-top:14px;font-size:12px}
@media(max-width:820px){.grid,.grid.two{grid-template-columns:1fr}footer .fg{grid-template-columns:1fr}.top nav{display:none}.facts dl{grid-template-columns:1fr}.facts dt{border-top:1px solid #F0EBE0}}
"""

NAV = """<nav>
<a href="{root}index.html#career">Career</a>
<a href="{root}case-law/index.html">Case Law</a>
<a href="{root}drafts/index.html">Drafts</a>
<a href="{root}jobs/index.html">Jobs</a>
<a href="{root}family/index.html">Family</a>
<a href="{root}service/index.html">Service</a>
<a href="{root}about/index.html">About</a>
<a class="cta" href="{root}index.html#join">Join free</a>
</nav>"""

FOOTER = """<footer><div class="wrap">
<div class="fg">
  <div>
    <b style="color:#fff;font-family:Georgia,serif;font-size:18px">WakeelBano</b>
    <p style="max-width:310px;font-size:13px;margin-top:8px">Pakistan's career platform for lawyers — chambers, housing, paid work and research, in one place. Starting in Karachi.</p>
  </div>
  <div><h5>Career</h5>
    <a href="{root}career/law-gat/index.html">Law-GAT</a>
    <a href="{root}career/bar-council-enrollment/index.html">Enrollment</a>
    <a href="{root}career/lawyer-salary-pakistan/index.html">Salary</a>
    <a href="{root}career/high-court-license/index.html">High Court licence</a>
  </div>
  <div><h5>Karachi</h5>
    <a href="{root}karachi/lawyer-jobs/index.html">Lawyer jobs</a>
    <a href="{root}karachi/lawyer-room-for-rent/index.html">Rooms and seat share</a>
    <a href="{root}case-law/index.html">Case law</a>
    <a href="{root}about/index.html">About</a>
  </div>
</div>
<div class="fb">© 2026 WakeelBano · Legal information only, not legal advice · We respect bar council rules</div>
</div></footer>"""


def esc(t):
    return html.escape(t, quote=True)


def _verify_tags():
    out = ""
    if GOOGLE_VERIFY:
        out += f'\n<meta name="google-site-verification" content="{GOOGLE_VERIFY}">'
    if BING_VERIFY:
        out += f'\n<meta name="msvalidate.01" content="{BING_VERIFY}">'
    return out


def page(title, desc, slug, body, canonical, schema=None):
    root = "../" * slug.count("/")
    verify_tags = _verify_tags()
    sch = ('<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + "</script>") if schema else ""
    return f"""<!DOCTYPE html>
<html lang="en-PK">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{BASE}{canonical}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="theme-color" content="#0B1B2B">
<meta name="geo.region" content="PK-SD"><meta name="geo.placename" content="Karachi">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{BASE}{canonical}">
<meta property="og:locale" content="en_PK">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E%3Crect width='48' height='48' rx='12' fill='%230F2537'/%3E%3Cpath d='M24 10v26M14 16h20M17 38h14' stroke='%23E7CE7A' stroke-width='2.4' stroke-linecap='round'/%3E%3C/svg%3E">
<style>{CSS}</style>{verify_tags}
{sch}
</head>
<body>
<header class="top"><div class="top-in">
  <a class="brand" href="{root}index.html"><b>WakeelBano</b><small>Become a lawyer</small></a>
  {NAV.format(root=root)}
</div></header>
{body}
{FOOTER.format(root=root)}
</body>
</html>"""


def crumbs(root, title, segs=None):
    """Breadcrumb strip. segs = ancestor folder names of the current page."""
    segs = segs or []
    labels = {"case-law": "Case Law", "drafts": "Drafts", "career": "Career", "karachi": "Karachi"}
    trail = ""
    for i, sx in enumerate(segs):
        upath = root + "/".join(segs[: i + 1]) + "/index.html"
        trail += f' <span>\u203a</span> <a href="{upath}">{labels.get(sx, sx.title())}</a>'
    return f'<div class="wrap"><div class="crumbs"><a href="{root}index.html">Home</a>{trail} <span>\u203a</span> <span>{esc(title)}</span></div></div>'


def facts_html(facts):
    if not facts:
        return ""
    rows = "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in facts)
    return f'<div class="facts"><h2>Key facts</h2><dl>{rows}</dl></div>'


def sources_html(url_slug, sources):
    allsrc = list(sources or []) + list(C.SOURCES_COMMON)
    seen, items = set(), ""
    for name, link, kind in allsrc:
        if link in seen:
            continue
        seen.add(link)
        items += f'<li><a href="{link}" rel="nofollow noopener" target="_blank">{esc(name)}</a> <i>· {esc(kind)}</i></li>'
    return f'<div class="sources"><h2>Sources you can verify</h2><ul>{items}</ul></div>'


def faq_html(faqs):
    if not faqs:
        return ""
    items = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)
    return f'<section class="faq"><h2>Frequently asked questions</h2>{items}</section>'


def org_node():
    node = {
        "@type": "Organization",
        "@id": BASE + "#org",
        "name": BRAND,
        "url": BASE,
        "description": ("Career platform for Pakistani lawyers: chamber and pupillage matching, "
                        "verified rooms and seat sharing, paid drafting work, a legal job market, "
                        "lawyer profiles with earned ratings, and free case law research guides."),
        "address": {"@type": "PostalAddress", "addressLocality": "Karachi",
                    "addressRegion": "Sindh", "addressCountry": "PK"},
    }
    if SOCIAL:
        node["sameAs"] = list(SOCIAL)
    return node


def child_url(parent_url, rel):
    """Resolve a hub child link (relative to the hub folder) to a root-relative URL."""
    folder = parent_url.rsplit("/", 1)[0] + "/"
    return posixpath.normpath(folder + rel)


def article_schema(p):
    graph = [{
        "@type": "Article",
        "headline": p["h1"],
        "description": p["desc"],
        "inLanguage": "en-PK",
        "mainEntityOfPage": {"@type": "WebPage", "@id": BASE + p["url"]},
        "author": {"@type": "Organization", "name": BRAND, "url": BASE},
        "publisher": org_node(),
        "datePublished": TODAY,
        "dateModified": TODAY,
        "about": {"@type": "Thing", "name": p.get("kicker", "Legal information")},
        "isAccessibleForFree": True,
    }, {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": p["h1"], "item": BASE + p["url"]},
        ],
    }]
    if p.get("faqs"):
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]],
        })
    return {"@context": "https://schema.org", "@graph": graph}


def build_article(p):
    slug = p["slug"]
    root = "../" * slug.count("/")
    secs = ""
    for sec in p["sections"]:
        if sec.get("h2"):
            secs += f'<h2>{sec["h2"]}</h2>\n'
        if sec.get("answer"):
            secs += f'<p><b>{sec["answer"]}</b></p>\n'
        secs += sec["html"] + "\n"
    rel = ""
    if p.get("related"):
        tiles = "".join(f'<a class="tile" href="{root}{u}"><b>{t}</b><span>Read the guide →</span></a>'
                        for t, u in p["related"])
        rel = f'<div class="related"><h2>Related guides</h2><div class="grid">{"".join(tiles)}</div></div>'
    answer = f'<div class="answer">{p["answer"]}</div>' if p.get("answer") else ""
    body = f"""
{crumbs(root, p["h1"], slug.split("/")[:-2])}
<section class="hero"><div class="wrap">
  <div class="kicker">{p.get("kicker","Guide")}</div>
  <h1>{p["h1"]}</h1>
  <p>{p["desc"]}</p>
  {answer}
  <div class="meta"><span>{BRAND} · Karachi</span><span>Updated: October 2026</span><span>Reading time: about 6 minutes</span></div>
</div></section>
<main class="wrap">
{facts_html(p.get("facts"))}
{secs}
<div class="cta-box">
  <div><h3>{C.CTA["title"]}</h3><p>{C.CTA["text"]}</p></div>
  <a class="btn" href="{root}index.html#join">Free account →</a>
</div>
{faq_html(p.get("faqs"))}
{sources_html(slug, p.get("sources"))}
{rel}
<div class="disclaimer">{C.DISCLAIMER}</div>
</main>"""
    return page(p["title"], p["desc"], slug, body, p["url"], article_schema(p))


def build_hub(p):
    slug = p["slug"]
    root = "../" * slug.count("/")
    tiles = "".join(f'<a class="tile" href="{u}"><b>{t}</b><span>{d}</span></a>' for t, d, u in p.get("children", []))
    secs = f'<div class="grid two" style="margin-bottom:26px">{tiles}</div>' if tiles else ""
    for sec in p["sections"]:
        if sec.get("h2"):
            secs += f'<h2>{sec["h2"]}</h2>\n'
        if sec.get("answer"):
            secs += f'<p><b>{sec["answer"]}</b></p>\n'
        secs += sec["html"] + "\n"
    rel = ""
    if p.get("related"):
        rt = "".join(f'<a class="tile" href="{u}"><b>{t}</b><span>Read the guide →</span></a>' for t, u in p["related"])
        rel = f'<div class="related"><h2>Related</h2><div class="grid two">{rt}</div></div>'
    answer = f'<div class="answer">{p["answer"]}</div>' if p.get("answer") else ""
    body = f"""
{crumbs(root, p["h1"], slug.split("/")[:-2])}
<section class="hero"><div class="wrap">
  <div class="kicker">{p.get("kicker","Library")}</div>
  <h1>{p["h1"]}</h1>
  <p>{p["desc"]}</p>
  {answer}
  <div class="meta"><span>{BRAND} · Karachi</span><span>Updated: October 2026</span></div>
</div></section>
<main class="wrap">
{secs}
<div class="cta-box">
  <div><h3>{C.CTA["title"]}</h3><p>{C.CTA["text"]}</p></div>
  <a class="btn" href="{root}index.html#join">Free account →</a>
</div>
{faq_html(p.get("faqs"))}
{rel}
<div class="disclaimer">{C.DISCLAIMER}</div>
</main>"""
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "CollectionPage", "name": p["h1"], "description": p["desc"], "url": BASE + p["url"],
             "inLanguage": "en-PK", "isPartOf": {"@type": "WebSite", "name": BRAND, "url": BASE},
             "dateModified": TODAY},
            {"@type": "ItemList", "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": t, "url": BASE + child_url(p["url"], u)}
                for i, (t, d, u) in enumerate(p.get("children", []))]},
        ],
    }
    return page(p["title"], p["desc"], slug, body, p["url"], schema)


def build_about(p):
    p = dict(p)
    p.setdefault("facts", [
        ("What it is", "A career platform for Pakistani lawyers"),
        ("Based in", "Karachi, Sindh, Pakistan"),
        ("Free for", "Students, fresh graduates and junior advocates"),
        ("Paid by", "Chambers, law firms, universities and sponsors"),
        ("Does not do", "Legal advice, client case referrals, lawyer rankings"),
    ])
    return build_article(p)


def write_llms_txt(urls):
    """Curated llms.txt plus a plain-text export, both generated from content_pages."""
    core = [
        (BASE, "What WakeelBano is: a career platform for Pakistani lawyers; who it serves and how it is funded."),
        (BASE + "about/", "Entity page: what the platform does, what it deliberately does not do, and how content is produced."),
    ]
    out = [f"# {BRAND}", "",
           "> Career platform for Pakistani lawyers, starting in Karachi. It helps law students, fresh graduates and "
           "junior advocates find a chamber and mentor, verified rooms and seat sharing near the courts, paid drafting "
           "work, and free case law research guides. Junior lawyers use it free; chambers, firms and universities pay.",
           "",
           "Key facts: founded 2026, based in Karachi, Sindh, Pakistan. Legal information only, not legal advice. "
           "No commission on client case referrals, and no lawyer rankings. Guidance is drawn from Pakistani statutes, "
           "bar council notifications and official court publications, with sources listed on every page.",
           "", "## Core pages"]
    for u, d in core:
        out.append(f"- [{d}]({u})")
    out.append("")
    for h in C.HUBS:
        out.append(f"## {h['h1']} ({BASE}{h['url']})")
        out.append(f"- [{h['desc']}]({BASE}{h['url']})")
        for t, d, u in h.get("children", []):
            out.append(f"- [{t}: {d}]({BASE}{child_url(h['url'], u)})")
        out.append("")
    out.append("## Jobs and hiring")
    out.append(f"- [Legal jobs in Pakistan, freelance tasks and the lawyer directory]({BASE}jobs/) — aggregated openings with links to the original postings, lawyer profiles with skills, cases handled and ratings, and hiring tools for chambers and firms.")
    out.append("")
    out += ["## Optional", f"- [Sitemap]({BASE}sitemap.xml)", f"- [Full text export]({BASE}llms-full.txt)", ""]
    io.open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write("\n".join(out))

    # llms-full.txt — expanded plain-text export of every page
    import re as _re
    full = [f"# {BRAND} — full text export", "",
            f"Public content from {BASE.replace('https://', '').rstrip('/')}, in plain text for AI agents and researchers.", ""]
    for p in [C.ABOUT] + C.PAGES:
        full.append(f"## {p['h1']}")
        full.append(f"URL: {BASE}{p['url']}")
        full.append("")
        if p.get("answer"):
            full.append(p["answer"])
            full.append("")
        for k, v in p.get("facts", []):
            full.append(f"- {k}: {v}")
        for sec in p["sections"]:
            if sec.get("h2"):
                full.append(f"### {sec['h2']}")
            if sec.get("answer"):
                full.append(sec["answer"])
            txt = _re.sub(r"<[^>]+>", " ", sec["html"])
            full.append(_re.sub(r"\s+", " ", txt).strip())
            full.append("")
        for q, a in p.get("faqs", []):
            full.append(f"Q: {q}")
            full.append(f"A: {a}")
            full.append("")
        full.append("")
    io.open(os.path.join(ROOT, "llms-full.txt"), "w", encoding="utf-8").write("\n".join(full))


def main():
    urls = [("", "1.0", "weekly"), ("jobs/", "0.9", "daily")]

    for h in C.HUBS:
        out = os.path.join(ROOT, h["slug"])
        os.makedirs(os.path.dirname(out), exist_ok=True)
        io.open(out, "w", encoding="utf-8").write(build_hub(h))
        urls.append((h["url"], "0.9", "weekly"))
        print("hub  ", h["slug"])

    for p in C.PAGES:
        out = os.path.join(ROOT, p["slug"])
        os.makedirs(os.path.dirname(out), exist_ok=True)
        io.open(out, "w", encoding="utf-8").write(build_article(p))
        urls.append((p["url"], "0.8", "monthly"))
        print("page ", p["slug"])

    a = C.ABOUT
    out = os.path.join(ROOT, a["slug"])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    io.open(out, "w", encoding="utf-8").write(build_about(a))
    urls.append((a["url"], "0.9", "monthly"))
    print("page ", a["slug"])

    # 404 page (GitHub Pages serves this for any unknown path)
    body404 = """
<section class="hero"><div class="wrap">
  <div class="kicker">404</div>
  <h1>This page does not exist</h1>
  <p>The link may be old, or the page may have moved. Everything on WakeelBano is reachable from the guides below.</p>
  <div class="answer">Start with the case law library, the draft formats or the career roadmap — the three places lawyers go first.</div>
</div></section>
<main class="wrap">
  <div class="grid">
    <a class="tile" href="case-law/index.html"><b>Case law library</b><span>302 PPC, 489-F, 497 CrPC and 420 PPC research guides</span></a>
    <a class="tile" href="drafts/index.html"><b>Draft formats</b><span>Bail, notice, plaint, vakalatnama and more</span></a>
    <a class="tile" href="career/index.html"><b>Career roadmap</b><span>Law-GAT, enrollment, High Court licence</span></a>
  </div>
  <p style="margin-top:24px"><a href="index.html">Return to the home page</a></p>
</main>"""
    io.open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(
        page("Page not found — WakeelBano", "That page does not exist. Start from the case law library, the draft formats or the career roadmap.",
             "", body404, "404.html").replace('<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">',
                                              '<meta name="robots" content="noindex, follow">'))
    print("file   404.html")

    # CNAME is written only when the custom domain is actually live.
    # Usage: CUSTOM_DOMAIN=wakeelbano.com python3 scripts/build_pages.py
    custom = os.environ.get("CUSTOM_DOMAIN", "").strip()
    cname_path = os.path.join(ROOT, "CNAME")
    if custom:
        io.open(cname_path, "w", encoding="utf-8").write(custom + "\n")
        print("file   CNAME -> " + custom)
    elif os.path.exists(cname_path):
        os.remove(cname_path)
        print("file   CNAME removed (no custom domain)")

    # sitemap
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, pr, cf in urls:
        sm += ["  <url>", f"    <loc>{BASE}{u}</loc>", f"    <lastmod>{TODAY}</lastmod>",
               f"    <changefreq>{cf}</changefreq>", f"    <priority>{pr}</priority>", "  </url>"]
    sm.append("</urlset>")
    io.open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")

    # robots.txt — search engines AND AI answer engines explicitly allowed
    robots = f"""# WakeelBano — crawlers welcome. We publish original, sourced information for lawyers.

# Search engines
User-agent: *
Allow: /

# AI answer engines and assistants (citation welcome)
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Perplexity-User
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: Bingbot
Allow: /
User-agent: CCBot
Allow: /

Sitemap: {BASE}sitemap.xml
# AI content map: {BASE}llms.txt
"""
    io.open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(robots)

    write_llms_txt(urls)
    print(f"\n{len(urls)} URLs in sitemap · robots.txt and llms.txt written")


if __name__ == "__main__":
    main()
