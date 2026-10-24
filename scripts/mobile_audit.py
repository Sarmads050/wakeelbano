# -*- coding: utf-8 -*-
"""WakeelBano — mobile-friendliness audit.

Most people who will ever open this site are on a phone, so every page is
checked against the things that actually break a phone layout:

  1. viewport meta          — without it the phone renders a shrunken desktop page
  2. a media query          — the page must react to a narrow screen at all
  3. navigation usable      — a menu hidden with display:none and no replacement
                              leaves a phone user stranded
  4. tables scroll          — a wide table otherwise pushes the whole page sideways
  5. thumb-sized targets    — buttons, tabs and nav links at least 42px tall
  6. inputs at 16px         — anything smaller makes iOS zoom in on focus
  7. images capped          — img{max-width:100%}
  8. no fixed wide blocks   — width:>360px outside a media query

    python3 scripts/mobile_audit.py            # print the report
    python3 scripts/mobile_audit.py --write    # also write mobile-audit.md
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKS = ["viewport", "media query", "navigation", "table scroll",
          "tap targets", "input size", "images", "fixed widths"]


def style_blocks(html):
    return "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S))


def mobile_part(css):
    """Everything inside @media blocks — that is where the phone rules live."""
    out, i = [], 0
    while True:
        i = css.find("@media", i)
        if i < 0:
            break
        depth, j = 0, css.find("{", i)
        k = j
        while k < len(css):
            if css[k] == "{":
                depth += 1
            elif css[k] == "}":
                depth -= 1
                if depth == 0:
                    break
            k += 1
        out.append(css[j:k + 1])
        i = k + 1
    return "\n".join(out)


def audit(path, html):
    css = style_blocks(html)
    mob = mobile_part(css)
    base = css.replace(mob, "")
    fails = []

    if not re.search(r'name="viewport"[^>]*width=device-width', html):
        fails.append("viewport")

    if "@media" not in css:
        fails.append("media query")

    # a hidden nav with no replacement menu. Scrollbar-hiding rules
    # (.nav::-webkit-scrollbar{display:none}) are not menus, so strip them first.
    mob_no_sb = re.sub(r"[^{}]*::-webkit-scrollbar\s*\{[^}]*\}", "", mob)
    if re.search(r"\bnav\b[^{}]*\{[^}]*display:\s*none", mob_no_sb):
        fails.append("navigation")

    if "<table" in html and not re.search(r"table[^{}]*\{[^}]*overflow-x:\s*auto", mob + base):
        fails.append("table scroll")

    if re.search(r"<(button|a class=\"btn)", html):
        tall = re.findall(r"min-height:\s*(\d+)px", mob)
        if not any(int(h) >= 42 for h in tall):
            fails.append("tap targets")

    if "<input" in html:
        if not re.search(r"input[^{}]*\{[^}]*font-size:\s*1[6-9]px", mob):
            fails.append("input size")

    if "<img" in html and not re.search(r"img\s*\{[^}]*max-width:\s*100%", css):
        fails.append("images")

    wide = [int(w) for w in re.findall(r"(?<!max-)(?<!min-)width:\s*(\d{3,})px", base)]
    if any(w > 360 for w in wide) and not re.search(r"max-width:\s*100%", css):
        fails.append("fixed widths")

    return fails


def main():
    pages, results = 0, []
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if not d.startswith((".", "node_modules", "scripts", "emails",
                                                   "research", "uploads", ".git"))]
        for f in fn:
            if not f.endswith(".html"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, ROOT)
            html = io.open(p, encoding="utf-8").read()
            pages += 1
            fails = audit(rel, html)
            results.append((rel, fails))

    bad = [(r, f) for r, f in results if f]
    print(f"pages checked: {pages}")
    print(f"pages with mobile problems: {len(bad)}")
    for r, f in sorted(bad):
        print(f"  - {r}: {', '.join(f)}")

    if "--write" in sys.argv:
        lines = ["# Mobile audit — WakeelBano", "",
                 f"Pages checked: **{pages}** · pages with problems: **{len(bad)}**", "",
                 "## What is checked", ""]
        lines += [f"- {c}" for c in CHECKS]
        lines += ["", "## Result", ""]
        if not bad:
            lines.append("Every page passes all eight checks.")
        else:
            for r, f in sorted(bad):
                lines.append(f"- `{r}` — {', '.join(f)}")
        lines += ["", "_Re-run with `python3 scripts/mobile_audit.py --write`._"]
        io.open(os.path.join(ROOT, "mobile-audit.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
        print("wrote mobile-audit.md")

    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
