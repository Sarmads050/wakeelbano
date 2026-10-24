# -*- coding: utf-8 -*-
"""Validate the generated WakeelBano site: internal links, JSON-LD, H1/title/description."""
import io, json, os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_files = []
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if not d.startswith((".", "scripts", "research", "node_modules", ".git"))]
    for f in fn:
        if f.endswith(".html"):
            html_files.append(os.path.join(dp, f))

problems = []
pages = 0
for path in sorted(html_files):
    rel = os.path.relpath(path, ROOT)
    src = io.open(path, encoding="utf-8").read()
    pages += 1

    # --- JSON-LD ---
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
        try:
            json.loads(m.group(1))
        except Exception as e:
            problems.append(f"{rel}: JSON-LD error: {e}")

    # --- headings / meta ---
    h1 = len(re.findall(r"<h1[ >]", src))
    if h1 != 1:
        problems.append(f"{rel}: {h1} <h1> tags")
    if "<title>" not in src:
        problems.append(f"{rel}: no <title>")
    if 'name="description"' not in src:
        problems.append(f"{rel}: no meta description")
    if 'rel="canonical"' not in src:
        problems.append(f"{rel}: no canonical")

    # --- internal links (ignore anything inside <script> blocks: those are templates) ---
    markup = re.sub(r"<script.*?</script>", "", src, flags=re.S)
    for href in re.findall(r'href="([^"]+)"', markup):
        if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
            continue
        target, _, frag = href.partition("#")
        if not target:
            continue
        tp = os.path.normpath(os.path.join(os.path.dirname(path), target))
        if not os.path.exists(tp):
            problems.append(f"{rel}: broken link -> {href}")
        elif frag and tp.endswith(".html"):
            ts = io.open(tp, encoding="utf-8").read()
            ok = (f'id="{frag}"' in ts) or (f'data-v="{frag}"' in ts) \
                 or (os.path.basename(tp) == "index.html" and os.path.dirname(tp) == ROOT
                     and frag == "join" and "function openJoin" in ts)
            if not ok:
                problems.append(f"{rel}: missing anchor #{frag} in {os.path.relpath(tp, ROOT)}")

    # --- brand check ---
    if "WakeelSaathi" in src:
        problems.append(f"{rel}: old brand WakeelSaathi present")

# llms.txt links
ll = io.open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read()
for u in re.findall(r"\((https://wakeelbano\.com/[^)]*)\)", ll):
    rel = u.replace("https://wakeelbano.com/", "")
    if rel and not os.path.exists(os.path.join(ROOT, rel)):
        problems.append(f"llms.txt: dead link {u}")

print(f"pages checked: {pages}")
if problems:
    print(f"PROBLEMS ({len(problems)}):")
    for p in problems:
        print("  -", p)
    sys.exit(1)
print("OK: 0 broken internal links, 0 JSON-LD errors, exactly one H1 + title + canonical on every page")
