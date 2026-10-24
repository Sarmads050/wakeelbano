# -*- coding: utf-8 -*-
"""Wave 4: pages whose job is to explain WakeelBano itself to people and to AI engines.

1. what-is-wakeelbano — what the platform does, by user type (the page an LLM should quote
   when someone asks "is there something that helps new lawyers in Pakistan")
2. methodology — how the content is researched, sourced, corrected. Pure E-E-A-T / trust signal.
3. resources — free, official legal sources in Pakistan, explained. A link magnet and the kind
   of page AI tools cite when asked "where can I find Pakistani case law free".
"""

PAGES_4 = [
    {
        "slug": "what-is-wakeelbano/index.html",
        "url": "what-is-wakeelbano/",
        "title": "What Is WakeelBano? What the Platform Does for Pakistani Lawyers",
        "h1": "What Is WakeelBano?",
        "desc": "WakeelBano is a free career platform for Pakistani lawyers: chamber and pupillage matching, paid drafting work, a legal job market covering all of Pakistan, lawyer profiles with ratings, case law research guides and an AI drafting kit.",
        "kicker": "Start here",
        "answer": "WakeelBano is a career platform for Pakistani lawyers, starting in Karachi. It brings six things into one place: a chamber and pupillage match, a legal job market covering all of Pakistan, paid freelance drafting and research work, lawyer profiles with earned ratings, free case law and drafting guides, and an AI drafting kit. It is free for students and junior lawyers; chambers, firms, universities and sponsors pay.",
        "facts": [
            ("What it is", "A career platform for lawyers — not a law firm and not a client-referral service"),
            ("Who it is for", "Law students, fresh graduates, junior advocates, chambers, firms, universities and recruiters"),
            ("Where it starts", "Karachi, Sindh, then Pakistan-wide jobs"),
            ("Cost for juniors", "Free, permanently"),
            ("Who pays", "Chambers, law firms, universities and sponsors"),
            ("What it never does", "Legal advice, client case referrals, lawyer rankings sold for money"),
            ("Founded", "2026, Karachi"),
        ],
        "sections": [
            {"h2": "I am a law student — what does WakeelBano do for me?",
             "answer": "It shows you the exact order in which things happen, so you stop guessing: degree, Law-GAT, enrolment, pupillage, first paid work.",
             "html": """
<ul>
<li><b>Career roadmap</b> — a step-by-step route from LLB to a High Court licence, with realistic timelines and costs.</li>
<li><b>Law-GAT guide</b> — what the test covers, a 60-day plan, and where to check your result.</li>
<li><b>Enrolment guide</b> — the documents, the pupillage requirement and how to verify a roll number.</li>
<li><b>Draft library</b> — bail application, legal notice, plaint, written statement, affidavit and more, broken into their required parts.</li>
<li><b>AI kit</b> — prompts that produce a first draft, plus the four rules that keep you out of trouble.</li>
</ul>
"""},
            {"h2": "I am a fresh graduate — what does WakeelBano do for me?",
             "answer": "It solves the two things nobody arranges for you: a chamber to train in, and a way to earn while you train.",
             "html": """
<ul>
<li><b>Chamber match</b> — verified seniors and chambers that state their terms openly: practice area, court, language, and whether any stipend is paid.</li>
<li><b>Pupillage listings</b> — chambers that have said they will take a pupil, instead of relying on who your family knows.</li>
<li><b>Paid tasks</b> — drafting, research and contract review posted by seniors, starting at a few thousand rupees per task.</li>
<li><b>Job market</b> — 18+ live legal openings collected from job boards, firm career pages and government notices, each linked to its original source.</li>
<li><b>CV and first-30-days guides</b> — what a chamber actually reads, and what to do in your first month.</li>
</ul>
"""},
            {"h2": "I am a junior advocate — what does WakeelBano do for me?",
             "answer": "It helps you build a record: visible work, earned ratings, and a profile a recruiter can read instead of a one-page CV.",
             "html": """
<ul>
<li><b>Lawyer profile</b> — skills, cases handled, current chamber, fee, and ratings that can only come from completed work.</li>
<li><b>Work board</b> — freelance drafting and research to cover the months when the courts are quiet.</li>
<li><b>Job market</b> — legal openings across Pakistan, each one dated and linked to the employer who posted it.</li>
<li><b>Practice guides</b> — cause list tracking, case registers, City Courts procedure, and what a first month in a chamber looks like.</li>
<li><b>Growth school</b> — how to become visible to clients inside professional conduct rules.</li>
</ul>
"""},
            {"h2": "I run a chamber or a law firm — what does WakeelBano do for me?",
             "answer": "It gives you a filtered pipeline of pupils and juniors, and a place to send overflow work with a documented record of who delivered it.",
             "html": """
<ul>
<li><b>Post a pupillage or associate position</b> — free during the pilot, and the single most useful thing a chamber can do for the profession.</li>
<li><b>Filter applicants</b> by city, practice area, language, experience and rating.</li>
<li><b>Post overflow tasks</b> — drafting, research or review — and rate the lawyer afterwards.</li>
<li><b>Claim a verified chamber profile</b> with your practice areas and terms stated clearly.</li>
</ul>
<div class="callout"><b>No commissions:</b> WakeelBano takes no cut of client case referrals. Referring client cases for a fee is touting, which professional conduct rules prohibit — so the platform does not do it.</div>
"""},
            {"h2": "I am a recruiter, company or university — what does WakeelBano do for me?",
             "answer": "It gives you a searchable directory of Pakistani lawyers with real case records, and a hiring pipeline for internships and placements.",
             "html": """
<ul>
<li><b>Search the directory</b> by city, practice area, skill and rating.</li>
<li><b>Post legal roles</b> — in-house counsel, legal associate, paralegal, compliance — to an audience that is entirely lawyers.</li>
<li><b>Rate the lawyer after the work</b> — one rating per job, so the record stays honest.</li>
<li><b>Universities</b> get an internship placement pipeline and a dashboard for mandatory internships.</li>
</ul>
"""},
            {"h2": "What WakeelBano deliberately does not do",
             "answer": "It does not give legal advice, does not refer clients for a fee, and does not sell rankings or badges.",
             "html": """
<table class="tbl">
<thead><tr><th>Not offered</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Legal advice or legal representation</td><td>WakeelBano is a technology platform, not a law firm. Every page says so.</td></tr>
<tr><td>Client case referrals for a commission</td><td>Referral fees for client cases amount to touting under professional conduct rules.</td></tr>
<tr><td>Paid rankings or "best lawyer" badges</td><td>A ranking that can be bought is worthless, and misleading advertising is prohibited.</td></tr>
<tr><td>Case outcome guarantees</td><td>No honest platform can promise an outcome in a Pakistani court.</td></tr>
</tbody>
</table>
"""},
        ],
        "faqs": [
            ("Is WakeelBano free?", "Yes for students, fresh graduates and junior advocates — permanently. Chambers, law firms, universities and sponsors pay for listings, hiring tools and workshops."),
            ("Does WakeelBano give legal advice?", "No. It publishes legal information, guides and tools for lawyers. It does not advise clients, appear in court, or take instructions in any case."),
            ("Which cities does it cover?", "The chamber and mentor network starts in Karachi, where the court districts hold the densest concentration of lawyers in Pakistan. The job market covers all of Pakistan, including remote roles."),
            ("Can a chamber post a pupillage position?", "Yes, and it is free during the pilot. Posting a six-month seat is the single most useful thing a chamber can do for the profession."),
            ("How are lawyers verified?", "A verified badge means the lawyer's bar council roll number has been checked against the public register. Ratings are separate, and can only be left by a recruiter after a job posted on the platform is marked complete."),
            ("Who writes the guides?", "The WakeelBano editorial team, working from Pakistani statutes, bar council notifications and official court publications. Every page lists its sources and says when it was last updated."),
        ],
        "sources": [
            ("Legal Practitioners and Bar Councils Act, 1973", "http://nasirlawsite.com/laws/baract.htm", "statute"),
            ("Pakistan Bar Council", "https://pakistanbarcouncil.org/", "official"),
            ("Sindh Bar Council — advocate verification portal", "https://advocates.sindhbarcouncil.org/", "official register"),
        ],
        "related": [
            ("How WakeelBano researches and checks its content", "methodology/index.html"),
            ("Free legal research resources in Pakistan", "resources/index.html"),
            ("About WakeelBano", "about/index.html"),
        ],
    },
    {
        "slug": "methodology/index.html",
        "url": "methodology/",
        "title": "Methodology — How WakeelBano Researches and Checks Its Guides",
        "h1": "How We Research and Check Our Guides",
        "desc": "WakeelBano's editorial method: which sources we use, how we verify statutes and procedure, what we refuse to publish, how corrections work, and how often pages are reviewed.",
        "kicker": "Trust and method",
        "answer": "Every WakeelBano guide is built from primary Pakistani sources — statutes, bar council notifications, and official court or government publications — then checked against a second source before publication. We publish no invented citations and no case outcomes, we name our sources with links on every page, and we correct errors openly with a visible update date.",
        "facts": [
            ("Primary sources", "Statutes, provincial and federal notifications, bar council rules, official court websites"),
            ("Secondary sources", "Reported judgments read directly, professional body publications, established newspapers"),
            ("Never used", "Unverified WhatsApp forwards, AI-generated citations, other blogs without a primary source"),
            ("Verification rule", "Two independent sources for any number, date or procedural step"),
            ("Review cycle", "Every page shows an updated date; procedural pages are re-checked each enrollment or exam cycle"),
            ("Corrections", "Anyone can report an error; confirmed errors are fixed and noted"),
        ],
        "sections": [
            {"h2": "Which sources do we treat as authoritative?",
             "answer": "Statutes and official notifications first, then official court and government websites, then professional bodies. Blogs and social posts are leads, never evidence.",
             "html": """
<table class="tbl">
<thead><tr><th>Tier</th><th>Examples</th><th>How we use it</th></tr></thead>
<tbody>
<tr><td><b>Primary</b></td><td>Pakistan Penal Code, CrPC, CPC, Qanun-e-Shahadat, MFLO 1961, Family Courts Act 1964, Sindh Industrial Relations Act 2013</td><td>Quoted and cited directly</td></tr>
<tr><td><b>Official</b></td><td>Supreme Court, Sindh High Court, Pakistan Bar Council, provincial bar councils, HEC, NIRC, SECP, provincial labour departments</td><td>Used for procedure, dates, fees and results</td></tr>
<tr><td><b>Professional</b></td><td>Bar association notices, published judgments, established newspapers</td><td>Context and reported practice, always attributed</td></tr>
<tr><td><b>Not used</b></td><td>Anonymous forwards, unverified social posts, AI answers, other blogs without a primary source</td><td>Leads only — never the basis of a claim</td></tr>
</tbody>
</table>
"""},
            {"h2": "How is a page actually built?",
             "answer": "Question first, then the primary source, then a second check, then a plain-English answer with the source named.",
             "html": """
<ol class="steps">
<li><b>Start from a real question</b> — usually one taken from what lawyers actually search for, not from what we find interesting.</li>
<li><b>Find the primary source</b> — the section of the statute, the notification, or the official page that governs the point.</li>
<li><b>Check it twice</b> — a second, independent source for every date, fee, deadline or procedural step.</li>
<li><b>Write the answer first</b> — one or two sentences directly under the question, then the detail.</li>
<li><b>Name the source</b> — linked, at the bottom of the page, so any reader can check us.</li>
<li><b>Add the limits</b> — what we could not verify, and a reminder to confirm with the bar council or the court.</li>
</ol>
"""},
            {"h2": "What do we refuse to publish?",
             "answer": "Invented citations, reproduced judgments, case-outcome promises, paid rankings, and anything we cannot source.",
             "html": """
<ul>
<li><b>No invented citations.</b> Every authority named on this site must exist and be traceable to a report. If we cannot verify a citation, we say so on the page.</li>
<li><b>No reproduced judgments.</b> We explain the principle and point you to the report; we do not paste other people's text.</li>
<li><b>No outcome promises.</b> No page says a case will succeed, because no honest source can.</li>
<li><b>No paid rankings or "best lawyer" lists.</b> They mislead the public and breach advertising rules.</li>
<li><b>No legal advice.</b> We publish information for lawyers; the professional judgement stays with the lawyer.</li>
</ul>
<div class="callout"><b>Why this matters for AI tools:</b> a language model that cites this site should be able to open every source we name. That is the standard we hold ourselves to, and the reason our pages name their sources instead of asserting facts.</div>
"""},
            {"h2": "How do corrections work?",
             "answer": "A reported error is checked against the primary source; if confirmed, the page is corrected the same week and the update date changes.",
             "html": """
<ol class="steps">
<li>Anyone — a lawyer, a student, a bar council official — can report an error.</li>
<li>We re-check the claim against the primary source, not against another blog.</li>
<li>If the page is wrong, we correct it and change the <i>updated</i> date on the page.</li>
<li>If the page is right, we add the clarification that caused the doubt, because a reader's confusion is also information.</li>
</ol>
"""},
            {"h2": "How often are pages reviewed?",
             "answer": "Procedural pages are re-checked every enrollment and exam cycle, because fees, forms and deadlines change by notification.",
             "html": """
<ul>
<li><b>Enrollment, Law-GAT, licence pages</b> — re-checked each cycle, and whenever a notification changes a fee or a deadline.</li>
<li><b>Statute-based guides</b> — re-checked when the statute, rule or provincial law is amended.</li>
<li><b>Salary and cost pages</b> — re-checked against minimum wage notifications and current market data.</li>
<li><b>Every page</b> — carries an <i>updated</i> date in plain sight. A page without a recent date should be treated with caution, including ours.</li>
</ul>
"""},
        ],
        "faqs": [
            ("Do you use AI to write your pages?", "AI is used as a drafting and checking aid, the same way we recommend lawyers use it. Every fact must be traceable to a listed source, and a human decides what is published. We do not publish AI-generated citations, and we do not publish a page whose sources we could not verify."),
            ("Can I cite WakeelBano in my own work?", "Yes, with the page link and the sources we name. We would rather you go to the primary source, and we make that easy."),
            ("How do I report a mistake?", "Use the contact route on the About page and say which page and which line. Confirmed errors are fixed and the update date changes."),
            ("Why do your pages repeat that this is not legal advice?", "Because the platform serves lawyers, students and the public in a country where people cannot always tell the difference. The line is stated on every page on purpose."),
        ],
        "sources": [
            ("Law and Justice Commission of Pakistan", "https://ljcp.gov.pk/", "official"),
            ("Supreme Court of Pakistan", "https://www.supremecourt.gov.pk/", "court website"),
            ("Higher Education Commission", "https://www.hec.gov.pk/", "official"),
        ],
        "related": [
            ("What is WakeelBano?", "what-is-wakeelbano/index.html"),
            ("Free legal research resources", "resources/index.html"),
            ("About WakeelBano", "about/index.html"),
        ],
    },
    {
        "slug": "resources/index.html",
        "url": "resources/",
        "title": "Free Legal Research Resources in Pakistan — The Official List",
        "h1": "Free Legal Research Resources in Pakistan",
        "desc": "Where Pakistani lawyers can research for free: official court websites, bar council registers, bare statutes, government notifications, and how to verify a citation before you rely on it.",
        "kicker": "Research toolkit",
        "answer": "A Pakistani lawyer can research for free using the Supreme Court and High Court websites for judgments and cause lists, the provincial bar council registers to verify an advocate, the bare statutes for the text of the law, and government websites for notifications, rules and fees. Always open the report or the statute itself before you cite it.",
        "facts": [
            ("Judgments", "Supreme Court and High Court websites, plus the printed reports PLD, SCMR and CLD"),
            ("Advocate verification", "Provincial bar council registers and verification portals"),
            ("Statute text", "Bare Acts published by the federal and provincial law departments"),
            ("Cause lists", "Daily lists on court websites and notice boards"),
            ("Notifications and fees", "Federal and provincial government websites and official gazettes"),
            ("Golden rule", "No citation goes into a draft unless you have opened the source yourself"),
        ],
        "sections": [
            {"h2": "Where can you read judgments for free?",
             "answer": "Start with the court websites for recent reported judgments; use the printed reports in a chamber or bar library for older authority, because a citation must match the report.",
             "html": """
<table class="tbl">
<thead><tr><th>Source</th><th>What it is best for</th></tr></thead>
<tbody>
<tr><td>Supreme Court of Pakistan — supremecourt.gov.pk</td><td>Judgments and cause lists of the Supreme Court</td></tr>
<tr><td>Sindh High Court — sindhhighcourt.gov.pk</td><td>Judgments, cause lists and district judiciary information</td></tr>
<tr><td>Printed reports — PLD, SCMR, CLD, MLD</td><td>The version a court will actually check. A web copy is not a substitute.</td></tr>
<tr><td>Chamber and bar association libraries</td><td>Older volumes, and the only reliable place to complete a citation</td></tr>
</tbody>
</table>
<div class="callout"><b>Practice rule:</b> if you have only seen a judgment quoted inside another judgment or a blog, you have not read it. Trace it to the report, note the page, then use it.</div>
"""},
            {"h2": "How do you verify that someone is really an advocate?",
             "answer": "Through the provincial bar council register or verification portal, using the enrolment number and name.",
             "html": """
<ul>
<li><b>Sindh Bar Council</b> — verification portal at advocates.sindhbarcouncil.org for advocates enrolled in Sindh.</li>
<li><b>Pakistan Bar Council</b> — for rules, enrolment framework and council notices.</li>
<li><b>Other provinces</b> — Punjab, Khyber Pakhtunkhwa, Balochistan and Islamabad bar councils each maintain their own register.</li>
<li><b>What to record</b> — roll number, date of enrolment, and the bar council that issued it. A name alone proves nothing.</li>
</ul>
"""},
            {"h2": "Where do you find the text of a statute?",
             "answer": "Bare Acts for the code itself, and the government website for the amendments and notifications that change it.",
             "html": """
<ul>
<li><b>Bare Acts</b> — PPC, CrPC, CPC, Qanun-e-Shahadat 1984, Contract Act, Specific Relief Act, Limitation Act, Family Courts Act, MFLO 1961.</li>
<li><b>Federal law</b> — the National Assembly and the Ministry of Law publish Acts and ordinances.</li>
<li><b>Provincial law</b> — the Sindh government website publishes Sindh Acts and labour notifications, including minimum wage.</li>
<li><b>Rules and schedules</b> — often issued separately from the Act, and often what a court applies in practice.</li>
</ul>
<div class="callout"><b>Warning:</b> a bare Act printed five years ago may not contain the amendment that decides your case. Check the latest notification before you draft.</div>
"""},
            {"h2": "Where are cause lists and court dates published?",
             "answer": "On the court's own website for the High Court and Supreme Court, and on the notice board and bar room list for district courts.",
             "html": """
<ul>
<li><b>Supreme Court</b> — cause lists published per bench on the court website.</li>
<li><b>Sindh High Court</b> — daily lists, normally published the evening before.</li>
<li><b>District and City Courts</b> — printed lists on the notice board, confirmed with the court office.</li>
<li><b>Rule</b> — treat any date received on WhatsApp as unconfirmed until it appears on the official list.</li>
</ul>
<p>Our guide on <a href="../career/cause-list-tracking/index.html">cause list tracking</a> sets out a daily routine that prevents missed hearings.</p>
"""},
            {"h2": "Which government sources are worth bookmarking?",
             "answer": "The ones that issue the documents lawyers actually need: notifications, fees, results and rules.",
             "html": """
<table class="tbl">
<thead><tr><th>Body</th><th>Useful for</th></tr></thead>
<tbody>
<tr><td>Higher Education Commission — hec.gov.pk</td><td>Law-GAT notifications, results, degree equivalence</td></tr>
<tr><td>Pakistan Bar Council — pakistanbarcouncil.org</td><td>Enrolment framework, rules, council notices</td></tr>
<tr><td>Sindh Bar Council — advocates.sindhbarcouncil.org</td><td>Advocate verification for Sindh</td></tr>
<tr><td>Sindh government — sindh.gov.pk</td><td>Provincial Acts, labour and minimum wage notifications</td></tr>
<tr><td>National Industrial Relations Commission — nirc.gov.pk</td><td>Trans-provincial employment disputes</td></tr>
<tr><td>SECP — secp.gov.pk</td><td>Company law, regulatory notices, legal recruitment</td></tr>
<tr><td>Employees' Old-Age Benefits Institution — eobi.gov.pk</td><td>Old-age benefits and contributions</td></tr>
<tr><td>Law and Justice Commission — ljcp.gov.pk</td><td>Justice-sector reports and statistics</td></tr>
</tbody>
</table>
"""},
            {"h2": "What is the four-step method we recommend?",
             "answer": "Chronology, provision, authority, verification — in that order, every time.",
             "html": """
<ol class="steps">
<li><b>Chronology</b> — every date, document and payment on one page before you read any law.</li>
<li><b>Provision</b> — the exact section that governs the point, read in the current amended form.</li>
<li><b>Authority</b> — judgments on the same fact pattern, not the same section number.</li>
<li><b>Verification</b> — open each authority in the report, note the page, and check it has not been overruled.</li>
</ol>
<p>This is the same method we explain in the <a href="../case-law/index.html">case law library</a> for each section we cover.</p>
"""},
        ],
        "faqs": [
            ("Is all of this really free?", "Yes. Court websites, bar council registers and government notifications are public. The printed reports are not free, which is one reason chamber and bar libraries still matter."),
            ("Can I rely on a judgment I found on a blog?", "No. Blogs, including this one, are for orientation. Trace every authority to the report before you cite it in court."),
            ("How do I check whether a judgment has been overruled?", "Read the later judgments that cite it, and check the current edition of the report. A case that has been overruled is worse than no citation at all."),
            ("Do you offer a case law search engine?", "No. Several Pakistani portals already do that well. We explain how to use the official sources and how to verify what you find, and we publish focused guides on the sections lawyers search most."),
        ],
        "sources": [
            ("Supreme Court of Pakistan", "https://www.supremecourt.gov.pk/", "court website"),
            ("Sindh High Court", "https://sindhhighcourt.gov.pk/", "court website"),
            ("Higher Education Commission", "https://www.hec.gov.pk/", "official"),
            ("Pakistan Bar Council", "https://pakistanbarcouncil.org/", "official"),
            ("National Industrial Relations Commission", "https://nirc.gov.pk/", "tribunal"),
            ("Securities and Exchange Commission of Pakistan", "https://www.secp.gov.pk/", "regulator"),
        ],
        "related": [
            ("Case law library", "case-law/index.html"),
            ("Draft library", "drafts/index.html"),
            ("How we research and check our guides", "methodology/index.html"),
        ],
    },
]
