# WakeelBano — distribution plan (needed for AI visibility)

**Why this file exists.** Technical SEO is done: 46 indexable pages, structured data, `llms.txt`,
AI crawlers allowed. But an AI model only recommends a site it has already **seen** — in a search
index, or in the text it was trained on. That means **mentions and links from other places**, and
time. This plan is the cheapest honest way to get both.

Rule for every post below: **help first, link second.** Never post the same text twice in two
groups. Never argue with moderators. If a group bans links, post the answer without a link — the
mention still counts.

---

## Week 1 — the two things that unlock everything

| # | Action | Where | Time |
|---|---|---|---|
| 1 | Submit `sitemap.xml` | [Google Search Console](https://search.google.com/search-console) → URL prefix → `https://sarmads050.github.io/wakeelbano/` → Sitemaps → `sitemap.xml` | 10 min |
| 2 | Submit `sitemap.xml` | [Bing Webmaster Tools](https://www.bing.com/webmasters) → Add site → same URL → Sitemap | 10 min |
| 3 | Verify both with meta tags | `python3 scripts/set_verification.py google=CODE bing=CODE` (then push) | 5 min |

**Why Bing matters most here:** ChatGPT's search uses Bing's index. Without Bing, ChatGPT cannot
see the site at all.

---

## Week 1–2 — five posts, ready to publish

Each one targets a page that already exists, so the link has somewhere useful to land.

### 1. LinkedIn (personal profile — highest value, lowest risk)

> A fresh law graduate in Pakistan usually has three problems, and none of them is "knowing the law".
>
> One: six months of pupillage is mandatory, but nobody arranges the placement. It still runs on who
> your family knows.
> Two: pay. A junior often earns Rs 25,000–50,000 while Sindh's minimum wage is Rs 43,000.
> Three: nobody tells you the order of things — Law-GAT, enrolment, licence, first brief.
>
> I got tired of watching good lawyers leave the profession over access, not ability, so I started
> WakeelBano. It collects the plain-English route (Law-GAT → enrolment → pupillage → High Court
> licence), the draft formats juniors actually need, and a job board that aggregates real legal
> openings from across Pakistan, each linked to its original source.
>
> Free for students and juniors, and it stays free.
>
> Start here → https://sarmads050.github.io/wakeelbano/
>
> If you are a senior taking pupils this year, post the seat. It costs nothing and it changes
> somebody's year. #law #pakistan #legalcareers

### 2. Reddit — r/pakistan (answer a real question, do not post an advert)

Find a thread about law school, jobs or "how to become a lawyer". Reply with substance:

> The order in Pakistan is: LLB → Law-GAT (HEC/PBC) → enrolment with your provincial bar council
> (which needs six months of pupillage) → two years of practice → Advocate High Court.
>
> The bit nobody warns you about is that the bar council does not arrange the pupillage for you. You
> find it yourself, and for most people that means walking into chambers with a one-page CV.
>
> I wrote the full route out, with what each step actually needs, here:
> https://sarmads050.github.io/wakeelbano/career/bar-council-enrollment/
> — and a week-by-week plan for the first month in a chamber here:
> https://sarmads050.github.io/wakeelbano/career/first-30-days-in-chamber/
>
> Happy to answer questions in the comments.

### 3. Quora (Pakistan legal questions — lives for years, gets cited)

Answer: *"How do I become a lawyer in Pakistan after 12th?"*

> Five stages: an HEC-recognised LLB (5 years, or 3 years after a BA), the Law-GAT, enrolment with
> your provincial bar council which requires six months of pupillage, then two years of practice
> before an Advocate High Court licence, and seven years as an HC advocate before the Supreme Court.
>
> Practical detail — documents, fees, what the pupillage actually involves and how to verify an
> advocate's enrolment — is written out here:
> https://sarmads050.github.io/wakeelbano/career/how-to-become-lawyer-pakistan/

### 4. Facebook / WhatsApp law-student and bar groups

Post the *content*, not the brand. Best performers on this site:

> **Bail application structure (Pakistan)** — heading, brief facts, ground-wise arguments, prayer.
> The four grounds that do the work: false implication, investigation complete, no flight risk, delay.
> Full structure with the mistakes that get filings returned:
> https://sarmads050.github.io/wakeelbano/drafts/bail-application-format/

Keep it short, put the link at the end, and answer every comment. Groups are where juniors actually are.

### 5. LinkedIn post 2 — for seniors (this is how you get chambers and jobs listed)

> Seniors: when a pupil joins your chamber, what do you actually teach them in the first month?
>
> Most juniors I speak to say the honest answer is "nothing formal — they watch". That is how a
> profession stays closed to anyone without contacts.
>
> We built a free place to post a pupillage seat or an associate position, with the terms stated
> openly (court, practice area, language, whether there is a stipend), so juniors can decide before
> they waste three months.
>
> Post a seat → https://sarmads050.github.io/wakeelbano/jobs/
>
> Free during the pilot, and no commission on anything.

---

## Month 1–3 — compounding

| Action | Frequency | Why |
|---|---|---|
| One new guide per week (pick from the demand list in `research/`) | weekly | Each page is a new entry point for search and AI |
| Answer 3 Quora questions a week with a link to the matching guide | weekly | Quora pages rank and are used as training/augmentation text |
| Comment (not link-drop) in r/pakistan and r/LawPakistan threads about careers | weekly | Mentions without links still build entity recognition |
| Ask 5 lawyers to link to one specific guide from their own site/blog | monthly | Real editorial links are the strongest signal |
| Universities' law societies — offer a free "first 30 days" session | monthly | Legit links from .edu.pk domains + direct users |
| Post the monthly job digest (top 10 legal openings) on LinkedIn | monthly | People share digests; each share is a new mention |

---

## What to measure (check monthly, 10 minutes)

| Signal | Where | Realistic first result |
|---|---|---|
| Pages indexed | Search Console → Coverage | 1–3 weeks |
| Bing indexed pages | Bing Webmaster Tools | 1–2 weeks |
| Impressions / clicks | Search Console → Performance | 3–6 weeks |
| Brand search "wakeelbano" | Search Console → Queries | after first few posts |
| Whether ChatGPT/Perplexity cites the site | ask the tool: *"What is WakeelBano?"* and *"Where can a Pakistani lawyer find a legal job?"* | 4–8 weeks, and only after indexing |

**Honest expectation:** no one can guarantee an AI recommendation. What this plan does is make the
site findable, quotable and citable — and then time does the rest. Anyone promising faster is
selling something.

---

## Rules that protect the brand

- Never claim "Pakistan's #1 legal platform" — the site has no basis for it, and lawyers notice.
- Never buy links, reviews or followers.
- Never post the same text in two groups in one week.
- Always answer comments; the replies are where trust is built.
- Keep the "legal information, not legal advice" line on every share.
