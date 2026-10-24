# -*- coding: utf-8 -*-
"""WakeelBano — real phone-width rendering check.

Static checks (scripts/mobile_audit.py) catch missing rules. This opens each page
in headless Chromium at a 390px viewport — an iPhone 12/13 — and measures what
the phone actually gets:

  * horizontal overflow: does the page scroll sideways? (the single worst mobile bug)
  * which element is wider than the screen
  * text smaller than 12px
  * tap targets under 40px tall
  * screenshots saved to mobile-shots/

    python3 scripts/shot_mobile.py
"""
import io
import os
import sys

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "mobile-shots")

PAGES = [
    ("index.html", "home"),
    ("jobs/index.html", "jobs"),
    ("jobs/j13/index.html", "job-detail"),
    ("career/lawyer-salary-pakistan/index.html", "guide-table"),
    ("drafts/vakalatnama-format/index.html", "draft"),
    ("case-law/302-ppc/index.html", "case-law"),
    ("admin/index.html", "admin"),
    ("404.html", "404"),
]

PROBE = """() => {
  const vw = window.innerWidth;
  const wide = [];
  document.querySelectorAll('body *').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width > vw + 1 && el.children.length === 0) {
      wide.push({tag: el.tagName.toLowerCase(), cls: el.className || '',
                 w: Math.round(r.width), text: (el.textContent||'').trim().slice(0,40)});
    }
  });
  const small = [];
  document.querySelectorAll('p,li,td,span,a,div').forEach(el => {
    if (!(el.textContent||'').trim() || el.children.length) return;
    const fs = parseFloat(getComputedStyle(el).fontSize);
    if (fs && fs < 12) small.push({fs: fs, text: (el.textContent||'').trim().slice(0,40)});
  });
  const tiny = [];
  const CONTROLS = '.btn,button,.tab,nav a,header a,.btn-apply,.btn-apply-bottom,.cta,.tile';
  document.querySelectorAll(CONTROLS).forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.height && r.height < 40 && r.width > 20) {
      tiny.push({h: Math.round(r.height), text: (el.textContent||'').trim().slice(0,32)});
    }
  });
  return {vw, scrollWidth: document.documentElement.scrollWidth,
          wide: wide.slice(0, 6), small: small.slice(0, 6), tiny: tiny.slice(0, 6)};
}"""


def main():
    os.makedirs(OUT, exist_ok=True)
    bad = 0
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for rel, name in PAGES:
            path = os.path.join(ROOT, rel)
            if not os.path.exists(path):
                print(f"skip {rel} (missing)")
                continue
            ctx = browser.new_context(viewport={"width": 390, "height": 844},
                                      device_scale_factor=2, is_mobile=True,
                                      has_touch=True)
            page = ctx.new_page()
            page.goto("file://" + path, wait_until="load")
            page.wait_for_timeout(1600)
            res = page.evaluate(PROBE)
            overflow = res["scrollWidth"] - res["vw"]
            flag = "OK  " if overflow <= 1 and not res["small"] else "FIX "
            if flag.strip() == "FIX":
                bad += 1
            print(f"{flag}{name:<12} width {res['vw']} scroll {res['scrollWidth']} "
                  f"overflow {overflow}px small-text {len(res['small'])}")
            for w in res["wide"]:
                print(f"      wide: <{w['tag']} class='{w['cls']}'> {w['w']}px — {w['text']!r}")
            for s in res["small"]:
                print(f"      small text {s['fs']}px — {s['text']!r}")
            if res["tiny"]:
                print(f"      small tap targets: {[t['text'] for t in res['tiny']]}")
            page.screenshot(path=os.path.join(OUT, f"{name}.png"), full_page=False)
            ctx.close()
        browser.close()
    print(f"\n{bad} page(s) need attention · screenshots in mobile-shots/")


if __name__ == "__main__":
    sys.exit(main())
