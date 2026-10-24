# WakeelBano — homepage review and what the site still needs
_Written as if running the community, not selling a product. 24 October 2026._

## 1. What the first page says today

The current homepage is honest and well written, but it is built like a **pitch**: hero →
"eight modules" → problem research → comparison with other platforms → pricing. It answers
"what is this company?" A lawyer standing in a corridor at 9 a.m. is asking a different question:
**"what do I do today?"**

Three specific problems:

1. **It sells before it serves.** The first action offered is "Create a free account" — a commitment
   asked for before any value is given. Most visitors will not sign up to read.
2. **Nothing changes when you come back.** No new jobs, no new questions, no dates. There is no
   reason to open it twice, and a career site lives or dies on the second visit.
3. **No proof of people.** 230,879 enrolled lawyers is a national statistic, not evidence that
   anyone is here. A community needs faces, names and answers — even if it starts with five.

What is genuinely strong and should be kept: the ethics stance (no commission, no rankings), the
"what we do not do" box, and the fact that every job links to its source.

## 2. How the first page should look

See `concepts/homepage-concept.html` for the working mockup (mobile-first, checked at 390px).

Order of the page, and the reason for each block:

| Block | What it does | Why it earns the space |
|---|---|---|
| **Top bar** with Karachi + English/اردو | Sets place and language before anything else | A Karachi junior reads Urdu faster than English law-school English |
| **Hero: "What do you need today?"** with four task cards — Find a job / Join a chamber / Get paid drafting work / Research a matter, each with a live count | Turns the homepage into a menu of actions | The site becomes a tool on the first screen, not a brochure |
| **Trust line under the cards** — no commission, no rankings for sale, free for juniors | The differentiator, in one line | It is the thing that makes a senior recommend it to a junior |
| **Live strip** — 4 new jobs · 2 closing this week · PPSC opens in 11 days | A reason to return every morning | Daily habit is the whole game |
| **"Every number can be checked"** — 4 verifiable counters, each with its method | Proof instead of adjectives | Lawyers are trained to ask for the source |
| **Fresh jobs** with closing dates | Immediate value, no signup | The single most useful thing on the site |
| **Your stage** — student → graduated → junior → High Court → own chamber, with "you are here" | Makes the site different for a 2nd-year student and a 4-year advocate | The audience is not one audience |
| **Community** — Ask a senior (3 live questions) + events calendar | The part a product cannot fake | This is what makes it a community instead of a job board |
| **What we will never do** — the ethics block | Public promise, stated plainly | Reputation is the asset |
| **Employer band** — post a job free for 30 days | Funds the site without charging juniors | The only sustainable model here |

Changes in emphasis from the current page: the "eight modules" grid and the competitor comparison
move off the homepage (they belong on `/about/`), and pricing moves to its own page. Nobody becomes
a member because of a pricing table.

## 3. What is still missing — in priority order

### Now (before promoting the site to anyone)

1. **Urdu / English toggle.** Even partial Urdu for the career pages. This is the single biggest
   access issue for Karachi juniors.
2. **WhatsApp channel for jobs.** In Pakistan, a job reaches people through WhatsApp forwards, not
   email. One broadcast channel, one message a day, same content as the email digest.
3. **Chamber directory for Karachi.** Name, area, which courts, whether they take pupils, what
   documents they ask for, and how to approach them. Twelve chambers verified is worth more than
   a thousand scraped listings.
4. **Ask a senior (Q&A).** Start with ten questions you can answer yourself as the founder, then
   invite three seniors to answer. Publish with the answerer's enrolment year.
5. **Pupillage tracker.** A simple dated checklist per user: enrolment date, six months counted,
   cases attended, drafts made. This is what they actually need in month one.

### Next (months 2–4)

6. **Salary and stipend board** — anonymous reports ("firm type, years, city, monthly pay"), shown
   only once there are enough reports to protect the reporter.
7. **Court tools:** cause-list tracker, court holiday calendar, filing-fee calculator by court.
8. **Women lawyers section** — harassment complaint routes, chambers that have implemented the
   mechanism, returnship after a career break.
9. **Events and workshops with attendance records** — drafting clinics, mock interviews, cause-list
   walkthroughs. This is also how chambers discover juniors.
10. **Verified lawyer profiles with earned ratings** (already built) promoted properly: rating only
    after a completed job, plus a writing sample attached to the profile.

### Later (months 5+)

11. **Employer dashboard** — post a job, shortlist, mark hired; hiring data feeds the salary board.
12. **District expansion** — Hyderabad, Sukkur, then Lahore and Islamabad; each needs a local
    verifier or it becomes another scraped list.
13. **Alumni and referral loop** — a senior who found a junior here should be able to say so.

## 4. Two hard rules for whoever runs this

- **Publish nothing you cannot source.** Jobs, salaries and deadlines carry a link or a date, or
  they do not go up. This is already enforced by the build scripts; keep it that way.
- **Never take money from a junior.** The moment a junior pays for a listing, a match or a rating,
  the community stops trusting the platform and the chamber network stops recommending it.

## 5. What to do with this concept

If the direction is right, the next step is to rebuild `index.html` on this structure with the real
counts pulled from Supabase, keeping the existing jobs page, job pages, guides and admin panel as
they are. That is a contained change — one file plus a build script — and everything already
published stays where it is.
