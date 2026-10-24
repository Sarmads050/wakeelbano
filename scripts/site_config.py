# -*- coding: utf-8 -*-
"""Single source of truth for the site's public URL.

Switch hosts with:  python3 scripts/set_site_url.py https://wakeelbano.com/
Must end with a trailing slash.
"""

SITE_URL = "https://sarmads050.github.io/wakeelbano/"

# Canonical domain we will move to once it is purchased (kept for reference).
PLANNED_URL = "https://wakeelbano.com/"

# --- search engine ownership checks -----------------------------------------
# Paste the values the consoles give you; scripts/set_verification.py does this for you.
GOOGLE_VERIFY = ""     # Google Search Console -> URL prefix -> HTML tag -> content="..."
BING_VERIFY = ""       # Bing Webmaster Tools -> Meta tag -> content="..."

# --- profile links used in Organization schema (sameAs) ---------------------
SOCIAL = []            # e.g. ["https://www.linkedin.com/company/wakeelbano"]
