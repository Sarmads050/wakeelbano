# WakeelBano — wakeelbano.com

Career platform for Pakistani lawyers, starting in Karachi. It helps law students, fresh
graduates and junior advocates find a chamber and mentor, verified rooms and seat sharing
near the courts, paid drafting work, and free case law research guides.

- **Junior lawyers use it free.** Chambers, law firms, universities and sponsors pay.
- **Legal information only** — no legal advice, no client case referrals, no "best lawyer" rankings.
- **Language:** simple English across the whole site.

## What is in this repo

| Path | What it is |
|---|---|
| `index.html` | Single-file app prototype: home, problem research, career navigator, chamber match, rooms, work board, AI kit, growth school, pricing. Vanilla JS, no build step, works offline. |
| `case-law/` | Research hub + 302 PPC, 489-F PPC, 497 CrPC, 420 PPC, 406 PPC, 506 PPC pages |
| `drafts/` | Drafting hub + bail application, legal notice, notice reply, plaint, written statement, vakalatnama, affidavit, rent agreement, power of attorney |
| `career/` | Career hub + Law-GAT, enrollment, how to become a lawyer, salary, High Court licence, cause list tracking, lawyer CV, first 30 days in a chamber |
| `karachi/` | Karachi hub + lawyer jobs, lawyer room for rent, chamber seat rent, City Courts guide |
| `about/` | Entity page (what the platform is and does not do) |
| `scripts/content_pages.py` | Core page copy and data — the file to edit for content changes |
| `scripts/content_pages_more.py` | Wave-2 pages (drafts, case law, practice, Karachi) plus extra hub tiles |
| `404.html` | Not-found page (noindex) |
| `CNAME` | GitHub Pages custom domain: `wakeelbano.com` |
| `scripts/build_pages.py` | Generator: writes all 34 pages, `404.html`, `CNAME`, `sitemap.xml`, `robots.txt`, `llms.txt`, `llms-full.txt` |
| `scripts/validate.py` | Checks broken internal links, JSON-LD validity, one `<h1>`/title/canonical per page, dead links in `llms.txt` |
| `scripts/repair_quotes.py` | Utility: converts unescaped straight quotes in content text to typographic quotes |
| `scripts/push.sh` | Commit + push using a token in `.secrets/gh_token` |
| `research/` | Demand research (what Pakistani lawyers search, pain points) behind the content plan |

**Size of the site:** 33 indexable URLs — 1 home page, 4 hubs, 27 guides, 1 about page, plus a 404.

## Editing content

1. Edit `scripts/content_pages.py` (plain Python dicts — no HTML framework).
2. Rebuild and check:
   ```bash
   python3 scripts/build_pages.py
   python3 scripts/validate.py
   ```
3. Commit and push (`scripts/push.sh "your message"`).

### Page shape (`PAGES`, `HUBS`, `ABOUT`)

```python
{
  "slug": "career/law-gat/index.html",   # file path
  "url":  "career/law-gat/",             # canonical URL, relative to https://wakeelbano.com/
  "title": "<title> tag", "h1": "...", "desc": "meta description", "kicker": "Career · Entry",
  "answer": "1–2 sentence direct answer shown under the H1",   # GEO: the snippet AI engines quote
  "facts": [("Conducted by", "HEC with the Pakistan Bar Council"), ...],  # key-facts table
  "sections": [{"h2": "Question-style heading", "answer": "One-line answer", "html": "<p>...</p>"}],
  "faqs": [("Question?", "Answer.")],       # rendered + FAQPage JSON-LD
  "sources": [("Name", "https://…", "official")],   # named, linked external sources
  "related": [("Title", "career/.../index.html")]
}
```

## SEO and AI search (GEO)

Every page carries: one `<h1>`, a question-style H2 structure, a direct answer under the H1,
a key-facts table with real numbers and dates, named and linked sources, FAQ markup, an
Article + BreadcrumbList (+ FAQPage) JSON-LD graph, and a canonical URL.

`robots.txt` explicitly allows search and AI crawlers: `GPTBot`, `OAI-SearchBot`,
`ChatGPT-User`, `ClaudeBot`, `Claude-SearchBot`, `PerplexityBot`, `Perplexity-User`,
`Google-Extended`, `Applebot-Extended`, `Bingbot`, `CCBot`.

`llms.txt` (curated map with descriptions) and `llms-full.txt` (plain-text export of every
page) are generated on every build. Google does not read `llms.txt`; OpenAI and Microsoft
crawlers do.

### Keyword strategy (measured, not guessed)

Google Trends for Pakistan: `lawyer` indexes about 3.6× `wakeel`, while the brand carries
"wakeel" for topical relevance. Titles and H1s therefore use the English head terms
(`lawyer`, `advocate`, `case law`, `law gat`) that Pakistanis actually type, with Karachi
and section numbers for long-tail capture.

## Deploying

Static files — any host works. GitHub Pages: repository **Settings → Pages → Source:
Deploy from a branch → `main` / root**, then point the `wakeelbano.com` DNS records at
GitHub Pages. Custom domain files (`CNAME`) are not committed yet.

## Content rules (do not break these)

- No invented case citations, no reproduced judgments, no "#1 lawyer" claims.
- Every number is attributed; every page ends with a "legal information, not legal advice" note.
- No promises about case outcomes, and no client referral commission — that is touting.
