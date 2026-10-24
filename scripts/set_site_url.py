# -*- coding: utf-8 -*-
"""Point the whole site at a new public URL.

Usage:  python3 scripts/set_site_url.py https://wakeelbano.com/

Rewrites scripts/site_config.py and the hard-coded URLs in index.html, then
rebuilds every generated page (canonicals, sitemap, robots, llms.txt).
"""
import io, os, re, sys, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWN = ["https://wakeelbano.com", "https://sarmads050.github.io/wakeelbano",
         "https://www.wakeelbano.com"]


def main():
    if len(sys.argv) != 2 or not sys.argv[1].startswith("http"):
        print("usage: python3 scripts/set_site_url.py https://wakeelbano.com/")
        return 1
    new = sys.argv[1].rstrip("/") + "/"
    new_root = new.rstrip("/")

    cfg = os.path.join(ROOT, "scripts", "site_config.py")
    s = io.open(cfg, encoding="utf-8").read()
    s = re.sub(r'SITE_URL = ".*?"', f'SITE_URL = "{new}"', s)
    io.open(cfg, "w", encoding="utf-8").write(s)

    idx = os.path.join(ROOT, "index.html")
    h = io.open(idx, encoding="utf-8").read()
    for old in KNOWN:
        if old.rstrip("/") == new_root:
            continue
        h = h.replace(old + "/", new)
        h = h.replace(old, new_root)
    io.open(idx, "w", encoding="utf-8").write(h)

    print(f"SITE_URL -> {new}")
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build_pages.py")], check=True)
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "validate.py")], check=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
