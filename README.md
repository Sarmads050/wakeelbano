# WakeelSaathi — Pakistan ke Wakeelon ka Ecosystem

**Wakeel ka pehla saathi.** Pakistan ke naye wakeelon (aur Karachi khaas taur par) ke liye ek career-first
ecosystem: chamber/mentor matching, verified rehail (rooms + chamber-share), kaam board, case law aur draft
library, AI kit aur growth school.

> **Note:** Legal *information* platform hai — legal advice nahi deta, aur client case referral par commission nahi leta
> (ye Bar Council rules ke khilaf hoga).

---

## Repo ka structure

```
index.html                                  → Main app (single file, no dependencies)
case-law/index.html                         → Case law hub (SEO traffic engine)
  case-law/302-ppc/                         → 302 PPC qatl-i-amd research guide
  case-law/489-f/                           → Cheque dishonour 489-F
  case-law/497-crpc/                        → Bail 497 CrPC
drafts/index.html                           → Draft library hub
  drafts/bail-application-format/
  drafts/legal-notice-format/
  drafts/plaint-format/
  drafts/vakalatnama-format/
career/index.html                           → Career hub
  career/law-gat/                           → Law-GAT 2026
  career/bar-council-enrollment/
  career/how-to-become-lawyer-pakistan/
  career/lawyer-salary-pakistan/
  career/high-court-license/
karachi/index.html                          → Karachi hub
  karachi/lawyer-jobs/
  karachi/lawyer-room-for-rent/
robots.txt · sitemap.xml                    → SEO foundation
research/                                   → Deep research reports (market + search demand + naming)
scripts/build_pages.py                      → Landing pages generator (content → HTML)
scripts/content_pages.py                    → Saara page content (edit yahan)
scripts/rebrand.py                          → Brand/text replacement helper
scripts/push.sh                             → GitHub push helper
```

## Kaise chalayein

Koi build step ya server zaroori nahi — `index.html` browser mein kholein.

```bash
open index.html                  # macOS
xdg-open index.html              # Linux
python3 -m http.server 8000      # ya local server → http://localhost:8000
```

## Pages dobara generate karna

Landing pages **generator** se bante hain (taake header/footer/schema har page par consistent rahe):

```bash
cd scripts && python3 build_pages.py
```

- Content edit karein → `scripts/content_pages.py`
- Template / CSS / schema edit karein → `scripts/build_pages.py`
- Run karne par saari `index.html` files + `sitemap.xml` + `robots.txt` update ho jate hain

Har page **self-contained** hai (inline CSS, koi external font/CDN nahi) — is liye preview mein bhi
poora render hota hai aur GitHub Pages par bhi fast chalta hai.

## SEO foundation (already included)

| Cheez | Kahan |
|---|---|
| Title + meta description (har page) | generator |
| Canonical URLs | har page |
| Open Graph + Twitter cards | har page |
| JSON-LD: Organization, WebSite, LegalService, FAQPage | `index.html` |
| JSON-LD: Article + BreadcrumbList + FAQPage | har landing page |
| `robots.txt` + `sitemap.xml` | repo root |
| Internal linking (hub → page → related) | generator |
| Mobile-first, zero external assets (fast CWV) | inline CSS |

**Deploy hone ke baad ye karein:**
1. `sitemap.xml` mein domain confirm karein (abhi `https://wakeelsaathi.com/` placeholder hai)
2. [Google Search Console](https://search.google.com/search-console) mein site add karein + sitemap submit karein
3. Google Business Profile (agar physical presence ho) bana lein

## GitHub Pages par live karna

1. Repo → **Settings** → **Pages**
2. Source: **Deploy from a branch** → `main` → `/ (root)`
3. URL: `https://<username>.github.io/<repo>/`

Custom domain (wakeelsaathi.com) ke liye Pages settings mein domain add karein — DNS mein `CNAME` record
`<username>.github.io` par point karein, phir "Enforce HTTPS" on karein.

## Content ke usool

- **Koi invented citation nahi.** Landmark case names/citations reproduce nahi kiye jate — sirf research method,
  statutory framework aur official sources ke links.
- Har page par **disclaimer** (legal information, not legal advice) + "verify from official source".
- Fees, dates aur section requirements badalte hain — har page par "current notification confirm karein" likha hai.
- Client ke case outcomes, names ya confidential details kabhi publish na karein.

## Update workflow

1. Chat mein change batayein ("Law-GAT page par 2027 dates ka section add karo")
2. Content/template edit hota hai → `python3 scripts/build_pages.py`
3. Commit + push → GitHub Pages ~1 minute mein update

## Status

Prototype / demo. Backend, authentication, real verification pipeline aur payments abhi nahi hain.
