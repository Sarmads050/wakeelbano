# Pakistani Wakeel Google par kya dhoondta hai?
### Data report — October 2026 · Name aur SEO decisions ke liye

---

## 0. Method (aur us ki limit — pehle imaandari)

| Kya measure kiya | Kaise |
|---|---|
| **Actual query demand** | Google Autocomplete API, `gl=PK`, live — jo 10 suggestions aate hain wo *real queries* hain jinke volumes sab se zyada hain |
| **Relative interest** | Google Trends (geo = PK, last 12 months), 5 keywords per group |
| **Collision check** | Har naam ke liye `.pk`, `.com.pk`, `.com` live DNS + Verisign RDAP + site content check |
| **Market context** | Newspapers, Bar Council data, competitor scan (17+ platforms) |

**Limit jo main chhupa nahi raha:** Pakistan ke liye paid keyword-volume tool (Ahrefs/Semrush) ka access nahi hai. Trends **absolute volume nahi** deta — sirf "is group mein kaun zyada hai" batata hai (0–100 index). Is liye neeche har number ke saath likha hai ke wo kis group ka hai. Autocomplete + Trends dono mila kar **ranking** sahi hai, **exact monthly searches** nahi.

---

## 1. Ek line ka jawab

> **Lawyer khud Google par sab se zyada "case law" dhoondta hai** (section-wise, Urdu mein, PDF, "search site").
> Us ke baad **"law gat"** (entry exam — har naya graduate), phir **"bar council"** (enrollment number/check/status),
> aur us ke baad **drafting formats** (bail application format, legal notice format, plaint format, vakalatnama format).
> Aur ek chauka dene wali baat: **"lawyer" shabd "wakeel" se 3.6 guna zyada search hota hai.**

---

## 2. Ranking — lawyer-side searches (jo wakeel khud karta hai)

### #1 — CASE LAW (sab se bara, evergreen)

Autocomplete (`case law pakistan`, `302 case law`):
```
case law pakistan
 ├ case laws pakistan pdf
 ├ 302 case law pakistan in urdu      ← Urdu mein! Awam + juniors dono
 ├ case law search pakistan
 ├ case law site pakistan
 ├ case law website pakistan
 ├ 324 case law pakistan in urdu
 ├ property case law pakistan
 └ tax case laws pakistan

302 case law
 ├ 302 case law pakistan in urdu      ← #1 suggestion
 ├ 302 ppc case laws
 └ section 302 case laws
```
Trends (group A = case law, law gat, 302 case law, bail application, legal drafting):
**case law = 50 (highest) · law gat = 23 · baqi teen ≈ 0**

Related queries: `what is case law` (100), `case law search` (21).
Trends (group B = divorce, case law, legal notice, plaint format, vakalatnama):
**case law = 25 → 50%** of that group, yani still #2 after "divorce".

**Matlab:** har criminal/civil section ke liye "**<section> case law pakistan in urdu**" ek chalta hua query hai — 302, 324, 489-F, 497 waghera. Ye **section-wise landing pages** ka pura SEO blueprint hai.

---

### #2 — LAW-GAT (sab se bara SPIKE, har saal do baar)

Autocomplete (`law gat`):
```
law gat last date to apply
law gat test result 9 august 2026
law gat test date 2026 registration
law gat test fees
law gat test past paper
law gat test answer key
law gat time
```
Trends group A mein: **law gat = 23** (case law ke aadhe se zyada — aur ye sirf students ka segment hai!)
Related queries: `law gat test` (100), `law gat hec` (74), `law gat result` (42), `law gat key` (38), `law gat test date` (32), `law gat past papers` (29), `law gat registration` (25), `law gat syllabus` (25).

**Rising queries:** `law gat result 2026` = **+303,200%**, `law gat key 21 december 2025` = +75,450%.
Yani **result ke din traffic phat jata hai.** Ye annual traffic bomb hai — jo bhi site "Law-GAT result / answer key / past papers / syllabus" par rank kare, us ke paas hazaron law students aa jate hain.

---

### #3 — BAR COUNCIL / ENROLLMENT (sanad ka raasta)

Autocomplete (`bar council enrollment`):
```
bar council enrollment number
bar council enrollment number check      ← verification intent
bar council enrollment fees
bar council enrollment form
bar council enrollment list
bar council enrollment status
bar council enrollment certificate
bar council enrollment procedure
```
Aur: `advocate license pakistan` → `lawyer license pakistan`, `advocate license fees`, `advocate salary in pakistan`.
`high court license pakistan` → `requirements for high court license in pakistan`, `how to get high court license in pakistan`, `supreme court license pakistan`.

Trends (group C = bar council, law gat, lawyer in karachi, lawyer salary, legal drafting course):
**bar council = 24 (highest) · law gat = 11**

**Matlab:** naya lawyer pehle **"license kaise"** dhoondta hai, phir **"salary kitni"**. Ye bilkul wo pain hai jis par aap ka Career Navigator bana hai.

---

### #4 — DRAFTING FORMATS (chhoti queries, magar sona)

Autocomplete — har ek ke andar 8–10 variations:
```
bail application  → draft · in urdu · format in pakistan pdf · format in urdu · format under section 497
legal notice      → format · in pakistan · format in urdu · for recovery of money · sample pakistan
plaint format     → in civil suit · in cpc · pdf · for recovery of money · cancellation of sale deed
vakalatnama       → meaning in english · format word · in urdu pdf · pdf download · criminal cases · supreme court
legal drafting    → course · course in pakistan · course in karachi · books pdf · samples in pakistan
```
Trends mein ye akelay **0** dikhte hain — yani absolute volume chhoti hai. **Magar:** jo banda "bail application format in urdu" search kar raha hai, wo **aaj court ja raha hai**. Ye highest-intent traffic hai.

Khaas baat: **"legal drafting course in karachi"** autocomplete mein maujood hai — aap ka paid workshop product literally demand par khara hai.

---

### #5 — COURT / CASE TRACKING (roz ka kaam)

```
sindh high court cause list
 ├ karachi · hyderabad · sukkur · larkana · mirpurkhas
 ├ today
 ├ advanced search
 └ case list search
```
Trends: Pakistan mein is ka volume chhota hai kyunke lawyers direct court ki site par jate hain (Google se nahi). **Magar ye daily-habit query hai** — yahi wo cheez hai jo app mein "rozana wapas" laati hai. SEO ke liye nahi, **product retention** ke liye important.

---

### #6 — CAREER / "KAISE BANE" (students ka rasta)

```
how to become a lawyer in pakistan
 ├ after 10th · after 12th
 ├ how to become a corporate lawyer in pakistan
 ├ criminal · tax · government
 └ how to become a successful lawyer in pakistan

wakeel kaise
 ├ wakeel kaise bane
 ├ sarkari vakil kaise bane
 └ wakeel ki complaint kaise kare      ← ye "complaint" intent note karein
```
Ye **blog/content** ka rasta hai, product ka nahi. Lekin yahi wo traffic hai jo funnel ke top par hai — student aaj "kaise bane" dhoondta hai, 2 saal baad aap ka paid user hota hai.

---

## 3. Sab se ahem finding: **"lawyer" vs "wakeel"**

Trends (group E, geo PK, 12 months):

| Query | Relative interest |
|---|---|
| **lawyer** | **79** ← sab se zyada |
| advocate | 66 |
| wakeel | 22 |
| qanoon | 6 |
| vakil | 4 |

**"lawyer" = 3.6× "wakeel"**, aur **"advocate" = 3× "wakeel"**.

Iska seedha SEO nateeja:
- Site ka title/H1 **"lawyer"** aur **"advocate"** words ke baghair adhoora hai
- Sirf "wakeel" par brand karna = 78% demand chhod dena
- Roman Urdu content zaroori hai, magar **English keyword + Urdu explainer** = best of both
- Pakistan mein log "**lawyer in karachi**", "**best lawyer in karachi**", "**family / divorce / khula / property lawyer in karachi**" search karte hain (autocomplete confirmed)

---

## 4. Do darwazay — strategi ka sab se important point

| | **Lawyer-side** (aap ka user) | **Client-side** (aap ka paisa nahi, traffic hai) |
|---|---|---|
| Top queries | case law, law gat, bar council, drafting formats | **property** (51), **divorce** (58 vs case law 25), bail, inheritance, khula |
| Volume | Medium | **Zyada** — client-side bara hai |
| Intent | Learning, career, kaam | Fauran wakeel chahiye |
| Aap ke liye | **Product** (subscription, community, kaam) | **Sirf SEO traffic + trust** — yahan client leads bechna **touting** ban sakta hai |

> **Strategy:** Client-side content likhein (SEO ke liye, "property case law", "divorce procedure in pakistan" — Trends mein confirmed), magar us traffic ko **Lawyer-side product** ki taraf mod dein, **client leads ke paise na lein**.
> Ye ethically saaf hai aur long-term brand banata hai.

### Isse ek naya module banta hai
Aap ka plan 8 modules ka tha — **data kehti hai ek 9th module sab se bara traffic laayega:**

**"Case Law + Draft Library"** — section-wise case law pages ("302 PPC case law in Urdu", "489-F case law", "bail 497 case law"), aur ready draft templates (bail application, legal notice, plaint, vakalatnama).

- Ye **SEO ka engine** hai (lawyers yahan aayenge)
- Career/Rehail/Kaam **product** hai (yahan wo rukenge)
- Dono ek doosre ko feed karte hain
- ⚠️ Legal risk: case law copy karna copyrighted reporters (PLD/SCMR) se nahi, **public judgments** se — aur hamesha source link + "verify" disclaimer

---

## 5. Naam ke liye requirements (jo data se nikli hain)

1. **"lawyer"/"wakeel" ka signal** — naam mein ho to best, warna tagline mein zaroor
2. **Ek baar mein spell ho jaye** — WhatsApp par typing test
3. **Search collision na ho** — koi legal platform pehle se is naam par na ho
4. **Domain .pk + .com dono mil jayein** (ya kam az kam .pk)
5. **"Junior" ya "student" naam mein na ho** — kyunke **paisa seniors/firms se aata hai**, unhe bhi izzat ka naam chahiye
6. **Trademark-able** — generic word (adalat, wakeel, qanoon) trademark nahi hota

---

## 6. Naam candidates — live checked (October 2026)

> 🚨 **AHEM:** `sanad.com.pk` par pehle se ek **live competitor** hai — title: *"Sanad — Pakistani legal research"*, description: *"Research, check authorities, and draft on a citation-verified corpus of Pakistani law."*
> **"Sanad" naam ab out hai.** (Ye exactly wo cheez karta hai jo hum "Case Law" module mein soch rahe the.)

| # | Naam | Meaning | .pk | .com.pk | .com | Search collision | Score /10 |
|---|---|---|---|---|---|---|---|
| 1 | **Muqadma** | muqadma / case | ✅ | ✅ | ❌ | Bohat kam (Trends ≈ 0) | **8.6** |
| 2 | **WakeelSaathi** | wakeel ka saathi | ✅ | ✅ | ✅ | Kam | **8.2** |
| 3 | **Sanadnama** | sanad + document (safe side) | ✅ | ✅ | ✅ | Kam, magar "sanad" family se jura | **7.4** |
| 4 | **WakeelBano** | "wakeel ban jao" | ✅ | ✅ | ✅ | Kam | 6.8 |
| 5 | **Daftarkhana** | record room / office | ✅ | — | ❌ | "Daftar" par coworking brand (Daftarkhwan) — confusion | 6.0 |
| 6 | ~~Sanad~~ | — | ❌ live | ❌ live competitor | ❌ | **Disqualify** | 0 |
| 7 | ~~Adalat~~ | — | ❌ live "Legal services for Pakistan" | ❌ | ❌ | + BP medicine "Adalat LA" | 0 |
| 8 | ~~Tareeq / Tareekh~~ | tareekh (date) | tareeq ✅ / tareekh ❌ | — | ❌ | Spelling jhagra | 0 |

---

## 7. Recommendation — top 2

### 🥇 Muqadma — `muqadma.pk` + `muqadma.com.pk` dono free
- Har Pakistani wakeel **ek second** mein samajh jata hai — "muqadma" = case. Koi explanation nahi chahiye
- Search space saaf (Trends ≈ 0) → brand aap ka, confusion zero
- Product-y lagta hai: sponsors, universities, firms ke samne serious naam
- **Tagline:** *"Muqadma jeetne ke liye — career banane ke liye. Eik jagah."*
- Downside: naam "case" kehta hai, "career" nahi. Is liye tagline zaroori.
- Downside 2: transliteration variants (muqadma / muqadama) — domain par asar nahi, brand recall par thora

### 🥈 WakeelSaathi — `.com` + `.pk` + `.com.pk` **teeno free** (bohat rare)
- Kam-yaad, high-trust, community feel — bilkul aap ke mission ("aunko help karna") par
- "Saathi" = mentor, rehail partner, kaam dene wala — teeno theem ek lafz mein
- Naam mein "wakeel" hai → topical relevance free mil jata hai
- **Tagline:** *"Wakeel ka pehla saathi."*
- Downside: 2 lafz, thora vernacular — machli ke bazaar wali feel aa sakti hai agar design kamzor ho

### 🥉 Sanadnama — agar "sanad" wali kahani rakhni hai
Sanad + nama = sanad ki document. Competitor se 100% alag, magar aap ki mojooda branding ("Sanad milti hai, raasta hum dete hain") zinda rehti hai.

---

## 8. SEO blueprint (naam final hone ke baad full plan)

### Site structure (URL plan)
```
/                              → Home: "Pakistan ke wakeelon ka ecosystem"
/case-law/                     → HUB (ye traffic engine hai)
  /case-law/302-ppc/           → "302 PPC Case Law in Pakistan (Urdu)"
  /case-law/324-ppc/
  /case-law/489-f/
  /case-law/bail-497-crpc/
  /case-law/property/
/drafts/                       → HUB
  /drafts/bail-application-format-pakistan/
  /drafts/legal-notice-format-pakistan/
  /drafts/plaint-format-cpc/
  /drafts/vakalatnama-format/
/career/
  /career/how-to-become-a-lawyer-in-pakistan/
  /career/law-gat/             → dates, syllabus, past papers, result, answer key
  /career/bar-council-enrollment/
  /career/high-court-license/
  /career/lawyer-salary-in-pakistan/
/chambers/                     → Karachi district-wise (Punjab Colony, Garden, Saddar, Malir…)
/rooms/                        → "lawyer room for rent in Karachi"
/jobs/                         → "lawyer jobs in karachi" (autocomplete confirmed!)
/ai/                           → AI prompts + verification rules
```

### Title formula (data se banaya gaya)
```
[Primary keyword] — [Benefit] | [Brand]
"302 PPC Case Law in Pakistan (Urdu) — Section-wise Judgments | Muqadma"
"Law-GAT 2026: Dates, Syllabus, Past Papers & Result | Muqadma"
"Lawyer Jobs in Karachi — Chamber & Associate Positions | Muqadma"
```
Rule: **English keyword pehle, Urdu explainer andar** (kyunke "lawyer" 79 vs "wakeel" 22).

### Pehle 90 din ka content (demand order mein, sab autocomplete-confirmed)
| # | Page | Kis query se | Kab |
|---|---|---|---|
| 1 | Law-GAT 2026 hub | `law gat result 2026`, `past papers`, `syllabus` | Fauran (spike season) |
| 2 | Section 302 case law in Urdu | `302 case law pakistan in urdu` | Week 1 |
| 3 | Bail application format (Pakistan, PDF/Word) | `bail application format in pakistan pdf` | Week 1 |
| 4 | Legal notice format (Pakistan) | `legal notice format in pakistan` | Week 2 |
| 5 | Bar Council enrollment guide | `bar council enrollment number check` | Week 2 |
| 6 | Lawyer salary in Pakistan (2026) | `lawyer salary in pakistan`, `advocate salary` | Week 3 |
| 7 | How to become a lawyer (after 12th) | `how to become a lawyer in pakistan after 12th` | Week 3 |
| 8 | Lawyer jobs in Karachi | `lawyer jobs in karachi` | Week 4 |
| 9 | Room for lawyer in Karachi (Punjab Colony/Garden) | `room for rent karachi` + lawyer modifier | Week 4 |
| 10 | High Court license requirements | `how to get high court license in pakistan` | Week 5–6 |
| 11 | Vakalatnama format | `vakalatnama format word` | Week 6 |
| 12 | Legal drafting course in Karachi | `legal drafting course in karachi` | Workshop launch |

### Technical SEO (Day 1 se)
- **Schema:** `LegalService` + `FAQPage` + `Article` + `BreadcrumbList` + `LocalBusiness` (Karachi)
- **Google Search Console** + sitemap.xml + robots.txt (abhi repo mein nahi hain — main bana dunga)
- **hreflang:** `en-PK` (aur Urdu pages `ur-PK` agar alag banayein)
- **Core Web Vitals:** single-file site already fast — images lazy, koi external font nahi
- **Internal linking:** har case-law page → Career Navigator + Kaam Board (funnel)
- **Backlinks:** Courting The Law, law college sites, bar association notices, guest posts

### Kya avoid karna hai
- "Pakistan ka #1 lawyer" type claims (misleading + Bar Council risk)
- Thin auto-generated case law pages (Google spam policy) — har page par actual judgment summary + source
- Client ke case outcomes par content (confidentiality)

---

## 9. Sources
- Google Autocomplete API (gl=PK) — live, Oct 2026
- Google Trends (geo=PK, 12-month, 5 keyword groups) — pulled Oct 2026
- [sanad.com.pk](https://sanad.com.pk) — competitor check (live)
- [adalat.pk](https://adalat.pk), [daftar.pk](https://daftar.pk) — collision check
- Autocomplete clusters: `case law pakistan`, `302 case law`, `law gat`, `bar council enrollment`, `bail application`, `legal notice`, `plaint format`, `vakalatnama`, `legal drafting`, `sindh high court cause list`, `lawyer in karachi`, `wakeel kaise`, `high court license pakistan`, `advocate license pakistan`, `how to become a lawyer in pakistan`
- Market context: pehli report (`research/pakistani-lawyers-deep-research.md`)

---

## 10. ✅ FINAL DECISION (Oct 2026)

**Naam: WakeelSaathi** — `wakeelsaathi.com` + `wakeelsaathi.pk` + `wakeelsaathi.com.pk` (teeno free verified)
**Tagline:** "Wakeel ka pehla saathi"
**SEO direction:** English keyword head (lawyer / advocate / case law / law gat) + Roman Urdu body —
kyunke "lawyer" (79) "wakeel" (22) se 3.6× zyada search hota hai. Brand mein "wakeel" hai, is liye topical
relevance free mil jati hai; content English keywords par target hoga.

**Rejected:** Sanad (live competitor sanad.com.pk), Adalat (live + medicine collision), Tareeq/Tareekh
(spelling conflict), Daftarkhana (Daftarkhwan coworking confusion).

**Build status:** SEO foundation (meta, canonical, OG, JSON-LD, sitemap, robots) + 15 landing pages live in repo.

---

## DECISION UPDATE (Oct 2026) — brand is WakeelBano, English-first, GEO layer

**Brand:** WakeelBano — `wakeelbano.com` (`.pk` and `.com.pk` also unregistered as of 24 Oct 2026).
"Wakeel" stays in the brand, so the keyword lives in every page title and URL.

**Language:** easy English everywhere. The earlier Roman Urdu draft is retired; the search
data still supports the choice, because English head terms dominate even in Pakistan.

**Keyword trade-off (stated openly to the user):** Google Trends PK indexes `lawyer` at 79
against `wakeel` at 22. The "wakeel" keyword the user asked for is therefore carried by the
brand and by section-level content, while titles/H1s use `lawyer`, `advocate`, `case law`,
`law gat` to win the search volume that actually exists.

**AI search (GEO):** the site now ships `llms.txt`, `llms-full.txt`, an AI-crawler-friendly
`robots.txt`, answer-first blocks under question headings, key-facts tables with sourced
numbers, FAQPage + Article + BreadcrumbList JSON-LD, and server-rendered HTML only.
Remaining off-site work: submit `sitemap.xml` to Bing Webmaster Tools (ChatGPT search reads
Bing's index) and to Google Search Console once the domain is live.
