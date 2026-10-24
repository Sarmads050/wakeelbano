# WakeelBano — job coverage audit & alerts setup
_24 October 2026 · live at https://sarmads050.github.io/wakeelbano/_

## 1. Coverage: what changed

The jobs page went from **18 openings to 58 open + 2 closed-reference = 60 sourced listings**.

| Group | Count | Examples |
|---|---|---|
| Law firms | 25 | Haidermota (partner-track + banking), Vellani (projects, M&A), Mandviwalla, RIAA Barker Gillette (competition), Surridge & Beecheno (shipping, IP), HKN (3 trainee tiers), ZM Law, JSA, Irfan & Faran, Khalid Law Firm |
| In-house / corporate | 22 | Jazz (3), Telenor, PTCL (2), SBP, HBL (2), Engro (2), Lucky Cement, MTBC / CareCloud, CureMD, Marie Stopes, Byonyks, Zeta |
| Government | 8 | SECP (7 posts), Punjab Cattle Market, EXIM Bank, PPSC, FPSC |
| Immigration | 3 | Aaraf, Tashfeen, confidential Australian immigration role |
| Remote | 2 | Muzy & Meraris, Denovo |

New filter set: **city · area of law · sector · type · free text**, where sector = Law firm / In-house / Government / Immigration / Remote.

### The honest answer to "are we missing jobs?"

No aggregator sees everything. LinkedIn Pakistan shows roughly 300 legal roles, Indeed 400–600,
Glassdoor 420+ — and those numbers include roles that do not need a law degree, while many
Karachi chambers never advertise at all. So instead of claiming completeness, the page now:

1. lists every source by name (Rozee, Indeed, Glassdoor, LinkedIn, legalalphabet, Mustakbil,
   jobz.pk, BeBee, firm career pages, SECP, FPSC/PPSC, Ministry of Law, NIRC);
2. says plainly that no aggregator is exhaustive;
3. lets any lawyer post a missing opening in three minutes;
4. moves closed government cycles into a **"Closed — but keep the route"** block, so PPSC and
   FPSC are still useful to a reader who wants to know when the next cycle opens.

Closed items kept for reference: PPSC Advertisement 08/2026 — Law Officer ×3, CMIT, Rs 115,000,
closed 3 Sep 2026; FPSC consolidated cycle, closed 31 Aug 2026.

## 2. Job alerts — how they work now

**Subscribe** → jobs page → **🔔 Job alerts** tab. A lawyer enters email and/or WhatsApp number,
city, area of law, stage, optional keywords. Saved to `public.subscribers`.

**Admin** → **Job alerts** tab (new) lists every subscriber and can copy all emails or all
WhatsApp numbers in one click.

**Email digest** → `scripts/send_alerts.py`. Matches each subscriber's filters against live jobs
posted after their last digest, sends an HTML email, stamps `last_sent_at` so nobody gets the
same job twice.

```bash
python3 scripts/send_alerts.py --dry-run     # preview
python3 scripts/send_alerts.py               # send
```

**WhatsApp (chosen: manual pilot)** → admin panel → *Copy all WhatsApp numbers* → send from the
WakeelBano business number. No Meta approval needed, works today; the Cloud API can be dropped
into the same script later without changing the database.

## 3. What is blocked on one thing from you

Email sending needs a key. It takes about five minutes:

1. Go to **resend.com** → sign up free (3,000 emails/month, 100/day — plenty for the pilot).
2. **API Keys → Create API Key** → copy it (starts with `re_`).
3. Paste it in this chat, or save it as `.secrets/resend_key`. It is gitignored and never
   touches the repo or the browser.
4. Then run `python3 scripts/send_alerts.py --to your@email.com --test` — the test email arrives
   in seconds.

Until a domain is verified in Resend, only your own address can receive mail. Verifying
`wakeelbano.com` after you buy it takes one DNS record and unlocks sending to everyone.

## 4. Current state

- 58 open jobs, 2 closed-reference, 6 freelance tasks, 8 lawyer profiles
- subscribers table live, RLS on: anyone may subscribe, only a signed-in admin may read or delete
- admin panel: joins · applications · jobs · profiles · ratings · **job alerts**
- 54 pages validated, 0 broken links, deploy `success`
