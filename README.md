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
| `what-is-wakeelbano/` | "What does it do for me?" — one section per user type (the page an AI assistant should quote) |
| `methodology/` | How guides are researched, sourced and corrected (trust / E-E-A-T signal) |
| `resources/` | Free official legal research sources in Pakistan |
| `admin/` | Control room: join requests, job applications, posted jobs, profiles and ratings (Supabase login, noindex) |
| `jobs/` | **Job market + lawyer directory**: 18 sourced legal openings, 6 paid tasks, 8 lawyer profiles, apply / post / rate flows |
| `family/` | Family law hub + khula and divorce, maintenance, child custody, dower |
| `service/` | Service law hub + labour court, wrongful termination, salary recovery |
| `civil/` | Civil and property hub + specific performance, injunction (Order XXXIX), execution (Order XXI), partition |
| `scripts/content_pages.py` | Core page copy and data — the file to edit for content changes |
| `scripts/content_pages_more.py` | Wave-2 pages (drafts, case law, practice, Karachi) plus extra hub tiles |
| `404.html` | Not-found page (noindex) |
| `CNAME` | GitHub Pages custom domain: `wakeelbano.com` |
| `scripts/build_pages.py` | Generator: writes every content page, `404.html`, `CNAME`, `sitemap.xml`, `robots.txt`, `llms.txt`, `llms-full.txt` |
| `scripts/build_jobs.py` | Builds `jobs/index.html` from the template + data |
| `scripts/build_admin.py` | Builds `admin/index.html` (the control room) |
| `scripts/jobs_template.html` | The job-market page template (HTML + app JS) |
| `scripts/jobs_data.py` | Job, task and lawyer datasets — edit here |
| `assets/wb-db.js` | Data layer: Supabase when configured, localStorage otherwise |
| `assets/supabase-config.js` | Where the Supabase URL and anon key go (empty = demo mode) |
| `supabase/schema.sql` | Database tables, rating rules and RLS policies |
| `supabase/seed.sql` | Generated seed data (`scripts/gen_supabase.py`) |
| `supabase/README.md` | 10-minute database setup guide |
| `scripts/validate.py` | Checks broken internal links, JSON-LD validity, one `<h1>`/title/canonical per page, dead links in `llms.txt` |
| `scripts/repair_quotes.py` | Utility: converts unescaped straight quotes in content text to typographic quotes |
| `scripts/push.sh` | Commit + push using a token in `.secrets/gh_token` |
| `scripts/set_verification.py` | `google=CODE bing=CODE` → writes the meta tags site-wide, rebuilds, validates |
| `marketing/distribution-plan.md` | Ready-to-post LinkedIn / Reddit / Quora / Facebook copy + the links/mentions plan |
| `scripts/db.py` | Database helper: `counts`, `rows`, `insert`, `update`, `delete`, `sql` (keys from `.secrets/`) |
| `research/` | Demand research (what Pakistani lawyers search, pain points) behind the content plan |

**Size of the site:** 52 indexable URLs — home, job market, 7 hubs, 42 guides, about, plus a 404.

## The job market (`jobs/`)

`scripts/build_jobs.py` holds three datasets — `JOBS` (real openings aggregated from public
listings, each with `src` and `url` back to the original posting), `TASKS` (paid freelance work
posted through the platform) and `LAWYERS` (profiles with skills, cases handled, chamber and
rating). The page is a single self-contained app:

- filter jobs by city, area of law, type and free text
- lawyer directory with profile drawers, star ratings and written reviews
- recruiters post a job; lawyers apply; a recruiter rates the lawyer after the work is completed
- "My profile" builds a lawyer profile (skills, cases, chamber, rate)

**Storage:** `assets/wb-db.js` is the only place that talks to the database. With a Supabase URL
and anon key in `assets/supabase-config.js` it runs **live** (shared jobs, profiles, applications
and ratings); with them empty it falls back to `localStorage` so the page always works.
Setup: see `supabase/README.md` (10 minutes, free tier).

One rating per completed job is enforced by `unique (lawyer_id, job_id)` in the schema — that
constraint, not the UI, is what makes ratings trustworthy.

**Job freshness:** listings are dated and each links to its source. Re-run the aggregation
monthly and delete expired entries — a stale job list destroys trust faster than a short one.

### Coverage (what "no job is missed" honestly means)

Listings come from `scripts/jobs_data.py` (the original 18) plus `scripts/jobs_data_more.py`
(42 more, ids `j19`–`j60`). Sources: Rozee.pk, Indeed Pakistan, Glassdoor PK, LinkedIn Jobs,
legalalphabet, Mustakbil, jobz.pk, BeBee, law-firm career pages (HKN, JSA, ZM Law), SECP,
FPSC/PPSC, Ministry of Law and the NIRC.

No aggregator is exhaustive — plenty of chambers never advertise. The page therefore states its
sources openly and lets any lawyer post a missing opening in three minutes. Postings that have
closed are set to `status = 'closed'` in the database and appear in the "Closed — but keep the
route" block instead of the open list (currently PPSC Ad 08/2026 and the FPSC cycle).

`scripts/jobs_normalize.py` collapses the free-text `job_type` values into eight canonical ones
(Full-time, Part-time, Contract, Remote, Per case, Internship, Trainee, Government) and derives a
`sector` (Law firm, In-house, Government, Immigration, Remote) so the filters work:

```bash
python3 scripts/jobs_normalize.py            # dry run
python3 scripts/jobs_normalize.py --apply    # rewrite job_type + sector in Supabase
```

### Job alerts (`jobs/` → "🔔 Job alerts" tab)

A lawyer subscribes with an email and/or a WhatsApp number plus city, area of law, stage and
optional keywords. Rows go to `public.subscribers` (SQL: `supabase/subscribers.sql`; anyone may
insert, only a signed-in admin may read or delete). The admin panel's **Job alerts** tab lists
them and can copy all emails / all numbers in one click.

Sending email digests:

```bash
python3 scripts/send_alerts.py --dry-run            # who would get what
python3 scripts/send_alerts.py                      # send via Resend
python3 scripts/send_alerts.py --to you@x.com --test
```

`send_alerts.py` needs `.secrets/resend_key` (Resend free tier: 100 emails/day, 3,000/month).
Until a sender domain is verified in Resend, only the account owner's own address can receive
mail — enough for testing. Each send stamps `last_sent_at`, so nobody gets the same job twice.

WhatsApp: the pilot uses the WakeelBano business number and the "Copy all WhatsApp numbers"
button in the admin panel; the Meta Cloud API can be wired into the same script later without
touching the database.

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

## Live URL and switching domain

`scripts/site_config.py` holds the single `SITE_URL` used for canonicals, Open Graph URLs,
the sitemap, `robots.txt` and `llms.txt`.

```bash
python3 scripts/set_site_url.py https://sarmads050.github.io/wakeelbano/   # current
python3 scripts/set_site_url.py https://wakeelbano.com/                    # when the domain is bought
```

The script rewrites `site_config.py` and the hard-coded URLs in `index.html`, then rebuilds and
validates every page. Nothing else needs to change when the custom domain goes live.

## Deploying

Static files — any host works. Currently live at
**https://sarmads050.github.io/wakeelbano/** (GitHub Pages, branch `main`, folder `/`).

When `wakeelbano.com` is bought:

1. `python3 scripts/set_site_url.py https://wakeelbano.com/`
2. DNS at the registrar: four A records for the apex (`185.199.108.153`, `185.199.109.153`,
   `185.199.110.153`, `185.199.111.153`) and `www` → CNAME → `sarmads050.github.io`
3. GitHub → Settings → Pages → Custom domain `wakeelbano.com`, then tick **Enforce HTTPS**
4. Rebuild with `CUSTOM_DOMAIN=wakeelbano.com python3 scripts/build_pages.py` to write the
   `CNAME` file into the repo

## Search console verification

1. Google Search Console → *Add property* → **URL prefix** → `https://sarmads050.github.io/wakeelbano/`
2. Bing Webmaster Tools → *Add site* → same URL (this one matters most: ChatGPT search reads Bing)
3. Copy the `content="..."` value each console gives you, then:

```bash
python3 scripts/set_verification.py google=THE_GOOGLE_CODE bing=THE_BING_CODE
bash scripts/push.sh "Add search console verification"
```

Wait for the GitHub Pages build, then press **Verify** in each console and submit
`sitemap.xml`. Codes live in `scripts/site_config.py` (`GOOGLE_VERIFY`, `BING_VERIFY`), so they
travel with every future build.

## Admin panel

1. Supabase → **Authentication → Users → Add user** → set an email and a strong password
   (turn off "send invite" — you just need the password login).
2. Open `https://sarmads050.github.io/wakeelbano/admin/` and sign in with those details.
3. You get five tabs: **Join requests** (from the "Join free" form), **Job applications**,
   **Jobs** (close or delete spam), **Lawyer profiles**, **Ratings**.
4. WhatsApp numbers are click-to-chat links.

The page is `noindex`, is not in the sitemap, and the browser only ever holds the publishable key —
row-level security in `supabase/leads-and-admin.sql` is what limits reads to a signed-in user.

## Keys and secrets

Everything secret lives in `.secrets/` and is gitignored — it is never committed and never
shipped to the browser:

| File | Contents |
|---|---|
| `.secrets/gh_token` | GitHub token used by `scripts/push.sh` |
| `.secrets/supabase_url` | Supabase project URL |
| `.secrets/supabase_key` | Supabase **secret** key — used only by `scripts/db.py` for data changes |
| `.secrets/supabase_access_token` | Optional Supabase personal access token, needed for schema (DDL) changes |

The browser only ever receives `assets/supabase-config.js`, which holds the **publishable** key.
That key is public by design; the row-level security rules in `supabase/schema.sql` decide what
it can read and write.

Rotate the secret key (Project Settings → API Keys → Revoke) whenever it may have been shared
outside `.secrets/`, then save the new value back into `.secrets/supabase_key`.

## Content rules (do not break these)

- No invented case citations, no reproduced judgments, no "#1 lawyer" claims.
- Every number is attributed; every page ends with a "legal information, not legal advice" note.
- No promises about case outcomes, and no client referral commission — that is touting.
