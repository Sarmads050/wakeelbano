# -*- coding: utf-8 -*-
"""Set the Google / Bing ownership verification codes and rebuild.

Usage:
    python3 scripts/set_verification.py google=abc123xyz
    python3 scripts/set_verification.py bing=1A2B3C4D5E
    python3 scripts/set_verification.py google=abc123 bing=1A2B3C

Google Search Console  -> Add property -> URL prefix -> HTML tag
                          the content="..." value is the code
Bing Webmaster Tools   -> Add site -> Meta tag -> content="..." value is the code

The codes are written to scripts/site_config.py and into index.html (the hand-written
home page), then every generated page is rebuilt so the tag appears site-wide.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = os.path.join(ROOT, "scripts", "site_config.py")
HOME = os.path.join(ROOT, "index.html")


def set_cfg(key, value):
    s = io.open(CFG, encoding="utf-8").read()
    s2 = re.sub(rf'^{key} = ".*?"', f'{key} = "{value}"', s, flags=re.M)
    if s2 == s and f'{key} = "{value}"' not in s:
        sys.exit(f"could not find {key} in site_config.py")
    io.open(CFG, "w", encoding="utf-8").write(s2)


def set_home(meta_name, value):
    h = io.open(HOME, encoding="utf-8").read()
    tag = f'<meta name="{meta_name}" content="{value}">'
    # remove an older version of the same tag, then insert before the canonical link
    h = re.sub(rf'<meta name="{meta_name}" content="[^"]*">\n?', "", h)
    if '<link rel="canonical"' in h:
        h = h.replace('<link rel="canonical"', tag + '\n<link rel="canonical"', 1)
    else:
        h = h.replace("<head>", "<head>\n" + tag, 1)
    io.open(HOME, "w", encoding="utf-8").write(h)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    did = []
    for arg in sys.argv[1:]:
        if "=" not in arg:
            sys.exit(f"bad argument: {arg} (expected key=value)")
        key, value = arg.split("=", 1)
        value = value.strip()
        if key == "google":
            set_cfg("GOOGLE_VERIFY", value)
            set_home("google-site-verification", value)
            did.append(f"Google verification set ({value[:8]}…)")
        elif key == "bing":
            set_cfg("BING_VERIFY", value)
            set_home("msvalidate.01", value)
            did.append(f"Bing verification set ({value[:8]}…)")
        elif key == "social":
            s = io.open(CFG, encoding="utf-8").read()
            links = re.findall(r'https?://[^"\']+', value)
            s = re.sub(r"^SOCIAL = \[.*?\]", "SOCIAL = " + repr(links), s, flags=re.M | re.S)
            io.open(CFG, "w", encoding="utf-8").write(s)
            did.append(f"social links set: {len(links)}")
        else:
            sys.exit(f"unknown key: {key} (use google=, bing= or social=)")

    for line in did:
        print(line)

    import subprocess
    for script in ("build_pages.py", "build_jobs.py", "validate.py"):
        subprocess.run([sys.executable, os.path.join(ROOT, "scripts", script)], check=True)
    print("Rebuilt and validated. Commit and push, then press Verify in the console.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
