# -*- coding: utf-8 -*-
"""WakeelBano — layout audit. Finds the things a screenshot shows and a CSS review misses.

For every page type, at three widths (desktop 1280, tablet 768, phone 390) it reports:

  overflow     the page scrolls sideways
  overlap      two text blocks sit on top of each other
  clipped      a box whose content is taller than the box (text spills out)
  offscreen    an element that starts outside the viewport

    python3 scripts/layout_audit.py            # summary
    python3 scripts/layout_audit.py --shots    # also save screenshots
"""
import os
import sys

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = os.path.join(ROOT, "layout-shots")

PAGES = [
    ("index.html", "home"),
    ("jobs/index.html", "jobs"),
    ("jobs/j13/index.html", "job-detail"),
    ("tools/index.html", "tools"),
    ("career/index.html", "career-hub"),
    ("career/lawyer-salary-pakistan/index.html", "guide"),
    ("drafts/vakalatnama-format/index.html", "draft"),
    ("case-law/302-ppc/index.html", "case-law"),
    ("karachi/index.html", "karachi-hub"),
    ("about/index.html", "about"),
    ("admin/index.html", "admin"),
    ("404.html", "404"),
]
WIDTHS = [(1280, "desktop"), (768, "tablet"), (390, "phone")]

# --all: one representative of every page template on the site
PAGES_ALL = PAGES + [
    ("career/law-gat/index.html", "career-step"),
    ("drafts/vakalatnama-format/index.html", "draft2"),
    ("case-law/302-ppc/index.html", "case-law2"),
    ("civil/order-39-injunction/index.html", "civil-guide"),
    ("family/khula-divorce-pakistan/index.html", "family-guide"),
    ("karachi/index.html", "karachi2"),
    ("jobs/j01/index.html", "job-detail2"),
    ("what-is-wakeelbano/index.html", "what-is"),
    ("resources/index.html", "resources"),
    ("methodology/index.html", "methodology"),
    ("service/index.html", "service"),
    ("career/how-to-become-lawyer-pakistan/index.html", "long-guide"),
]

PROBE = r"""() => {
  const vw = window.innerWidth, vh = window.innerHeight;
  const problems = {overflow: 0, overlap: [], clipped: [], offscreen: []};

  problems.overflow = Math.max(0, document.documentElement.scrollWidth - vw);

  const inScroller = el => {
    for (let p = el.parentElement; p; p = p.parentElement) {
      const cs = getComputedStyle(p);
      if (cs.overflowX === 'auto' || cs.overflowX === 'scroll') return true;
    }
    return false;
  };
  const skip = el => {
    const cs = getComputedStyle(el);
    if (cs.position === 'fixed' || cs.position === 'absolute') return true;
    if (cs.display === 'none' || cs.visibility === 'hidden' || cs.opacity === '0') return true;
    if (cs.display === 'inline') return true;          // inline text runs legitimately share a line
    if (inScroller(el)) return true;                    // a scrollable strip is allowed to run off
    const d = el.closest('details');                    // closed accordion content is not painted
    if (d && !d.open && el.tagName !== 'SUMMARY') return true;
    const tag = el.tagName;
    return ['SCRIPT','STYLE','SVG','PATH','RECT','BR','HR','IMG','HEAD','META','LINK'].includes(tag);
  };

  const leaves = [];
  document.querySelectorAll('body *').forEach(el => {
    if (skip(el)) return;
    const t = (el.textContent || '').trim();
    if (!t) return;
    // only blocks that directly hold text
    const ownText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1);
    if (!ownText) return;
    const r = el.getBoundingClientRect();
    if (r.width < 4 || r.height < 4) return;
    leaves.push({el, r, tag: el.tagName, cls: (el.className || '').toString().slice(0, 28), t: t.slice(0, 32)});
  });

  // overlap between blocks that are not in the same line of descent
  for (let i = 0; i < leaves.length; i++) {
    for (let j = i + 1; j < leaves.length; j++) {
      const a = leaves[i], b = leaves[j];
      if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
      const ox = Math.min(a.r.right, b.r.right) - Math.max(a.r.left, b.r.left);
      const oy = Math.min(a.r.bottom, b.r.bottom) - Math.max(a.r.top, b.r.top);
      if (ox > 8 && oy > 8) {
        problems.overlap.push({a: a.tag + '.' + a.cls + ' "' + a.t + '"',
                               b: b.tag + '.' + b.cls + ' "' + b.t + '"',
                               ox: Math.round(ox), oy: Math.round(oy)});
      }
      if (problems.overlap.length > 6) break;
    }
    if (problems.overlap.length > 6) break;
  }

  // clipped: content taller than the box, and the box is not allowed to scroll
  document.querySelectorAll('body *').forEach(el => {
    if (skip(el)) return;
    const cs = getComputedStyle(el);
    if (cs.overflow === 'auto' || cs.overflow === 'scroll' || cs.overflowX === 'auto') return;
    if (el.scrollHeight - el.clientHeight > 6 && cs.overflow === 'hidden') {
      problems.clipped.push(el.tagName + '.' + (el.className || '').toString().slice(0, 28) +
                            ' content ' + el.scrollHeight + 'px in ' + el.clientHeight + 'px');
    }
  });

  document.querySelectorAll('body *').forEach(el => {
    if (skip(el)) return;
    const r = el.getBoundingClientRect();
    if (r.width && (r.right > vw + 2 || r.left < -2)) {
      problems.offscreen.push(el.tagName + '.' + (el.className || '').toString().slice(0, 28) +
                              ' x=' + Math.round(r.left) + '..' + Math.round(r.right));
    }
  });

  // holes: a big dead gap between two consecutive sibling blocks
  const holes = [];
  document.querySelectorAll('main *, section, .wrap, .grid, body > div').forEach(box => {
    if (box.tagName === 'DETAILS' && !box.open) return;   // closed accordion has no visible gap
    const bd = box.closest('details');
    if (bd && !bd.open && box.tagName !== 'DETAILS') return;
    const kids = [...box.children].filter(k => {
      const cs = getComputedStyle(k);
      if (cs.position === 'absolute' || cs.position === 'fixed') return false;
      if (cs.display === 'none') return false;
      const r = k.getBoundingClientRect();
      return r.height > 12;
    });
    if (kids.length < 2) return;
    for (let i = 0; i + 1 < kids.length; i++) {
      const a = kids[i].getBoundingClientRect(), b = kids[i + 1].getBoundingClientRect();
      const gap = Math.round(b.top - a.bottom);
      if (gap > 200) {
        holes.push(box.tagName + '.' + (box.className || '').toString().slice(0, 22) +
                   ': ' + gap + 'px gap after ' + kids[i].tagName + '.' +
                   (kids[i].className || '').toString().slice(0, 20));
      }
    }
  });
  problems.holes = [...new Set(holes)].slice(0, 4);

  // spill: a child painted outside its card/panel box
  const spills = [];
  document.querySelectorAll('body *').forEach(el => {
    const cs = getComputedStyle(el);
    if (cs.overflow !== 'visible') return;
    if (cs.overflowX === 'auto' || cs.overflowX === 'scroll') return;  // the strip itself may be wider
    if (inScroller(el)) return;                          // scroll strips legitimately extend
    const sd = el.closest('details');                    // closed accordion content is not painted
    if (sd && !sd.open) return;
    if (!(cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none' ||
          cs.borderTopWidth !== '0px' || cs.borderRadius !== '0px')) return;
    if (el.children.length === 0) return;
    const r = el.getBoundingClientRect();
    if (r.height < 20 || r.width < 40) return;
    let bottom = -1e9, right = -1e9;
    for (const d of el.querySelectorAll('*')) {
      const dcs = getComputedStyle(d);
      if (dcs.position === 'absolute' || dcs.position === 'fixed' || dcs.display === 'none') continue;
      if (dcs.display === 'inline') continue;
      if (inScroller(d)) continue;              // text inside a scroll strip is meant to run on
      const dd = d.closest('details');          // closed accordion content is not painted
      if (dd && !dd.open && d.tagName !== 'SUMMARY') continue;
      const dr = d.getBoundingClientRect();
      if (!dr.height) continue;
      bottom = Math.max(bottom, dr.bottom); right = Math.max(right, dr.right);
    }
    if (bottom - r.bottom > 8 || right - r.right > 8) {
      spills.push(el.tagName + '.' + (el.className || '').toString().slice(0, 24) +
                  ' by ' + Math.round(Math.max(bottom - r.bottom, right - r.right)) + 'px');
    }
  });
  problems.spills = [...new Set(spills)].slice(0, 4);

  const uniq = a => [...new Set(a)];
  problems.overlap = uniq(problems.overlap.map(o => JSON.stringify(o))).slice(0, 5).map(JSON.parse);
  problems.clipped = uniq(problems.clipped).slice(0, 5);
  problems.offscreen = uniq(problems.offscreen).slice(0, 5);
  return problems;
}"""


def main():
    shots = "--shots" in sys.argv
    pages = PAGES_ALL if "--all" in sys.argv else PAGES
    widths = [(1280, "desktop"), (390, "phone")] if "--fast" in sys.argv else WIDTHS
    if shots:
        os.makedirs(SHOTS, exist_ok=True)

    bad = 0
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for rel, name in pages:
            path = os.path.join(ROOT, rel)
            if not os.path.exists(path):
                continue
            for width, label in widths:
                ctx = browser.new_context(viewport={"width": width, "height": 900},
                                          is_mobile=width < 800, has_touch=width < 800)
                page = ctx.new_page()
                page.goto("file://" + path, wait_until="load")
                page.wait_for_timeout(2200)
                res = page.evaluate(PROBE)
                issues = []
                if res["overflow"] > 1:
                    issues.append(f"overflow {res['overflow']}px")
                if res["overlap"]:
                    issues.append(f"{len(res['overlap'])} overlap(s)")
                if res["clipped"]:
                    issues.append(f"{len(res['clipped'])} clipped")
                if res["offscreen"]:
                    issues.append(f"{len(res['offscreen'])} offscreen")
                if res.get("holes"):
                    issues.append(f"{len(res['holes'])} hole(s)")
                if res.get("spills"):
                    issues.append(f"{len(res['spills'])} spill(s)")
                status = "OK  " if not issues else "FIX "
                if issues:
                    bad += 1
                print(f"{status}{name:<12} {label:<8} {' · '.join(issues) if issues else 'clean'}")
                for o in res["overlap"]:
                    print(f"       overlap: {o['a']}  ×  {o['b']}  ({o['ox']}×{o['oy']}px)")
                for c in res["clipped"]:
                    print(f"       clipped: {c}")
                for c in res["offscreen"]:
                    print(f"       offscreen: {c}")
                for h in res.get("holes", []):
                    print(f"       hole: {h}")
                for sp in res.get("spills", []):
                    print(f"       spill: {sp}")
                if shots:
                    page.screenshot(path=os.path.join(SHOTS, f"{name}-{label}.png"), full_page=True)
                ctx.close()
        browser.close()

    print(f"\n{bad} page/width combination(s) need attention")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
