# -*- coding: utf-8 -*-
"""
WakeelSaathi — static page builder.
scripts/content_pages.py se content uthata hai aur self-contained HTML pages banata hai
(inline CSS — koi external dependency nahi), plus sitemap.xml aur robots.txt.

Usage: python3 scripts/build_pages.py
"""
import io, os, json, html
import content_pages as C

BASE = "https://wakeelsaathi.com/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "WakeelSaathi"

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
.crumbs a{border:0;color:var(--muted)}
.crumbs a:hover{color:var(--navy)}
.crumbs span{color:#98A4B0}
.hero{background:linear-gradient(160deg,#0B1B2B,#15354D);color:#fff;padding:34px 0 40px;margin-bottom:34px}
.hero .kicker{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold2);font-weight:800}
.hero h1{font-size:clamp(26px,3.6vw,40px);margin:10px 0 12px;color:#fff}
.hero p{color:#C8D7E3;font-size:16.5px;max-width:720px;margin:0}
.hero .meta{margin-top:16px;font-size:12.5px;color:#93A6B5;display:flex;gap:16px;flex-wrap:wrap}
h2{font-size:clamp(20px,2.4vw,26px);margin:34px 0 12px}
h3{font-size:18px;margin:22px 0 8px}
p{margin:0 0 14px}
ul,ol{margin:0 0 16px;padding-left:22px}
li{margin:6px 0}
table.tbl{width:100%;border-collapse:collapse;margin:8px 0 18px;font-size:14.5px;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;display:table}
table.tbl th{background:#F3F0E9;text-align:left;padding:11px 13px;font-size:12.5px;letter-spacing:.04em;text-transform:uppercase;color:#4A5763;border-bottom:1px solid var(--line)}
table.tbl td{padding:11px 13px;border-bottom:1px solid #F0EBE0;vertical-align:top}
table.tbl tr:last-child td{border-bottom:0}
ol.steps{counter-reset:s;list-style:none;padding:0}
ol.steps li{counter-increment:s;position:relative;padding:12px 16px 12px 50px;background:#fff;border:1px solid var(--line);border-radius:12px;margin:0 0 10px}
ol.steps li:before{content:counter(s);position:absolute;left:14px;top:12px;width:24px;height:24px;border-radius:7px;background:var(--gold-soft);border:1px solid #EBD9A4;color:var(--navy);font-weight:800;font-size:13px;display:grid;place-items:center}
.callout{background:var(--gold-soft);border:1px solid #EBD9A4;border-radius:12px;padding:14px 16px;font-size:14.5px;margin:16px 0;color:#5F4A00}
.mini{font-size:13px;color:var(--muted)}
.card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px;box-shadow:0 1px 2px rgba(11,27,43,.04),0 8px 24px rgba(11,27,43,.05)}
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
.tile{background:#fff;border:1px solid var(--line);border-radius:13px;padding:17px;display:block;border-bottom:1px solid var(--line);transition:transform .14s,border-color .14s}
.tile:hover{transform:translateY(-2px);border-color:var(--gold)}
.tile b{display:block;font-family:Georgia,serif;font-size:16px;color:var(--navy);margin-bottom:4px}
.tile span{font-size:13px;color:var(--muted)}
.disclaimer{background:#fff;border:1px dashed #D8CFBC;border-radius:12px;padding:16px;font-size:13px;color:#4A5763;margin:30px 0}
.related{margin:26px 0}
footer{background:#08131F;color:#93A6B5;padding:32px 0 22px;margin-top:50px;font-size:13.5px}
footer .fg{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:26px;margin-bottom:20px}
footer h5{color:#fff;font-size:11px;letter-spacing:.16em;text-transform:uppercase;margin:0 0 10px}
footer a{color:#A9BAC8;display:block;padding:3px 0;border:0;font-size:13px}
footer a:hover{color:var(--gold2)}
footer .fb{border-top:1px solid rgba(255,255,255,.1);padding-top:14px;font-size:12px}
@media(max-width:820px){.grid,.grid.two{grid-template-columns:1fr}footer .fg{grid-template-columns:1fr}.top nav{display:none}}
"""

NAV = """<nav>
<a href="{root}index.html#career">Career</a>
<a href="{root}case-law/index.html">Case Law</a>
<a href="{root}drafts/index.html">Drafts</a>
<a href="{root}karachi/lawyer-jobs/index.html">Jobs</a>
<a href="{root}index.html#pricing">Pricing</a>
<a class="cta" href="{root}index.html#join">Join free</a>
</nav>"""

FOOTER = """<footer><div class="wrap">
<div class="fg">
  <div>
    <b style="color:#fff;font-family:Georgia,serif;font-size:18px">WakeelSaathi</b>
    <p style="max-width:300px;font-size:13px;margin-top:8px">Pakistan ke wakeelon ka ecosystem — sanad se career tak. Mentor, rehail, kaam aur pehchaan, ek jagah. Karachi se shuru.</p>
  </div>
  <div><h5>Career</h5>
    <a href="{root}career/law-gat/index.html">Law-GAT</a>
    <a href="{root}career/bar-council-enrollment/index.html">Enrollment</a>
    <a href="{root}career/lawyer-salary-pakistan/index.html">Salary</a>
    <a href="{root}career/high-court-license/index.html">High Court license</a>
  </div>
  <div><h5>Karachi</h5>
    <a href="{root}karachi/lawyer-jobs/index.html">Lawyer jobs</a>
    <a href="{root}karachi/lawyer-room-for-rent/index.html">Room / seat share</a>
    <a href="{root}case-law/index.html">Case law</a>
    <a href="{root}drafts/index.html">Drafts</a>
  </div>
</div>
<div class="fb">© 2026 WakeelSaathi · Legal information only, not legal advice · Bar Council rules ka ehtiram</div>
</div></footer>"""


def esc(t):
    return html.escape(t, quote=True)


def page(title, desc, slug, body, canonical, schema=None, og_type="article"):
    depth = slug.count("/")
    root = "../" * depth
    sch = ""
    if schema:
        sch = ('<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + "</script>")
    return f"""<!DOCTYPE html>
<html lang="en-PK">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{BASE}{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0B1B2B">
<meta name="geo.region" content="PK-SD"><meta name="geo.placename" content="Karachi">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{BASE}{canonical}">
<meta property="og:locale" content="en_PK">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E%3Crect width='48' height='48' rx='12' fill='%230F2537'/%3E%3Cpath d='M24 10v26M14 16h20M17 38h14' stroke='%23E7CE7A' stroke-width='2.4' stroke-linecap='round'/%3E%3C/svg%3E">
<style>{CSS}</style>
{sch}
</head>
<body>
<header class="top"><div class="top-in">
  <a class="brand" href="{root}index.html"><b>WakeelSaathi</b><small>Wakeel ka pehla saathi</small></a>
  {NAV.format(root=root)}
</div></header>
{body}
{FOOTER.format(root=root)}
</body>
</html>"""


def crumbs(slug, title):
    parts = [("Home", "../../index.html" if slug.count("/") >= 2 else ("../index.html" if slug.count("/") == 1 else "index.html"))]
    segs = slug.split("/")[:-1]  # folder names
    up = "../" * (len(segs))
    # build breadcrumb trail for known 2-level slugs
    labels = {"case-law": "Case Law", "drafts": "Drafts", "career": "Career", "karachi": "Karachi"}
    trail = ""
    for i, s in enumerate(segs):
        upath = "../" * (len(segs) - i) + "index.html"
        lab = labels.get(s, s.title())
        trail += f' <span>›</span> <a href="{upath}">{lab}</a>'
    return f'<div class="wrap"><div class="crumbs"><a href="{parts[0][1]}">Home</a>{trail} <span>›</span> <span>{esc(title)}</span></div></div>'


def faq_html(faqs):
    if not faqs:
        return ""
    items = "".join(
        f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)
    return f'<section class="faq"><h2>FAQ</h2>{items}</section>'


def faq_schema(url, faqs):
    if not faqs:
        return None
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
    }


def build_article(p):
    slug = p["slug"]
    depth = slug.count("/")
    root = "../" * depth
    secs = ""
    for sec in p["sections"]:
        if sec.get("h2"):
            secs += f'<h2>{sec["h2"]}</h2>\n'
        secs += sec["html"] + "\n"
    rel = ""
    if p.get("related"):
        tiles = ""
        for t, u in p["related"]:
            tiles += f'<a class="tile" href="{root}{u}"><b>{t}</b><span>Parhein →</span></a>'
        rel = f'<div class="related"><h2>Related guides</h2><div class="grid">{"".join(tiles)}</div></div>'
    body = f"""
{crumbs(slug, p["h1"])}
<section class="hero"><div class="wrap">
  <div class="kicker">{p.get("kicker","Guide")}</div>
  <h1>{p["h1"]}</h1>
  <p>{p["lede"]}</p>
  <div class="meta"><span>WakeelSaathi · Karachi</span><span>Last updated: October 2026</span><span>Reading time: ~5 min</span></div>
</div></section>
<main class="wrap">
<article>
{secs}
<div class="cta-box">
  <div><h3>{C.CTA["title"]}</h3><p>{C.CTA["text"]}</p></div>
  <a class="btn" href="{root}index.html#join">Free account →</a>
</div>
{rel}
<div class="disclaimer">{C.DISCLAIMER}</div>
</article>
</main>"""

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Article",
             "headline": p["h1"],
             "description": p["desc"],
             "inLanguage": "en-PK",
             "mainEntityOfPage": {"@type": "WebPage", "@id": BASE + p["url"]},
             "author": {"@type": "Organization", "name": "WakeelSaathi"},
             "publisher": {"@type": "Organization", "name": "WakeelSaathi"},
             "dateModified": "2026-10-24",
             "about": {"@type": "Thing", "name": p.get("kicker", "Legal information")}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
                {"@type": "ListItem", "position": 2, "name": p["h1"], "item": BASE + p["url"]},
            ]},
        ] + ([faq_schema(p["url"], p.get("faqs"))] if p.get("faqs") else []),
    }
    return page(p["title"], p["desc"], slug, body, p["url"], schema)


def build_hub(p):
    slug = p["slug"]
    root = "../" * slug.count("/")
    tiles = ""
    for t, d, u in p.get("children", []):
        tiles += f'<a class="tile" href="{u}"><b>{t}</b><span>{d}</span></a>'
    secs = f'<div class="grid two" style="margin-bottom:26px">{"".join(tiles)}</div>'
    for sec in p["sections"]:
        if sec.get("h2"):
            secs += f'<h2>{sec["h2"]}</h2>\n'
        secs += sec["html"] + "\n"
    rel = ""
    if p.get("related"):
        rt = "".join(f'<a class="tile" href="{u}"><b>{t}</b><span>Parhein →</span></a>' for t, u in p["related"])
        rel = f'<div class="related"><h2>Related</h2><div class="grid two">{rt}</div></div>'
    body = f"""
{crumbs(slug, p["h1"])}
<section class="hero"><div class="wrap">
  <div class="kicker">{p.get("kicker","Library")}</div>
  <h1>{p["h1"]}</h1>
  <p>{p["lede"]}</p>
  <div class="meta"><span>WakeelSaathi · Karachi</span><span>Last updated: October 2026</span></div>
</div></section>
<main class="wrap">
{secs}
<div class="cta-box">
  <div><h3>{C.CTA["title"]}</h3><p>{C.CTA["text"]}</p></div>
  <a class="btn" href="{root}index.html#join">Free account →</a>
</div>
{rel}
<div class="disclaimer">{C.DISCLAIMER}</div>
</main>"""
    schema = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": p["h1"],
        "description": p["desc"],
        "url": BASE + p["url"],
        "inLanguage": "en-PK",
        "isPartOf": {"@type": "WebSite", "name": SITE, "url": BASE},
    }
    return page(p["title"], p["desc"], slug, body, p["url"], schema)


def main():
    urls = [("", "1.0", "weekly")]
    # hubs
    for h in C.HUBS:
        out = os.path.join(ROOT, h["slug"])
        os.makedirs(os.path.dirname(out), exist_ok=True)
        io.open(out, "w", encoding="utf-8").write(build_hub(h))
        urls.append((h["url"], "0.9", "weekly"))
        print("hub  ", h["slug"])
    # articles
    for p in C.PAGES:
        out = os.path.join(ROOT, p["slug"])
        os.makedirs(os.path.dirname(out), exist_ok=True)
        io.open(out, "w", encoding="utf-8").write(build_article(p))
        urls.append((p["url"], "0.8", "monthly"))
        print("page ", p["slug"])

    # sitemap
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, pr, cf in urls:
        sm.append("  <url>")
        sm.append(f"    <loc>{BASE}{u}</loc>")
        sm.append("    <lastmod>2026-10-24</lastmod>")
        sm.append(f"    <changefreq>{cf}</changefreq>")
        sm.append(f"    <priority>{pr}</priority>")
        sm.append("  </url>")
    sm.append("</urlset>")
    io.open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")

    robots = f"""User-agent: *
Allow: /

Sitemap: {BASE}sitemap.xml
"""
    io.open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(robots)
    print(f"\n{len(urls)} URLs in sitemap · robots.txt written")


if __name__ == "__main__":
    main()
