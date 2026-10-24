# -*- coding: utf-8 -*-
"""
WakeelBano — landing page content (easy English, answer-first / GEO-optimised).
Har page: H1 -> direct answer (1-2 lines) -> question-style H2s with answer-first paragraphs
-> key facts (numbers/dates for AI extraction) -> named sources (citation triad) -> FAQs -> related.
Koi invented citation nahi: sirf statutory framework, method, aur official source links.
"""

BRAND = "WakeelBano"
BASE = "https://wakeelbano.com/"

DISCLAIMER = ("<b>Legal information, not legal advice.</b> This page explains how the law is structured and how to "
              "research it. We do not reproduce judgments or invent citations. Always verify sections, fees and "
              "procedures on the official website of the Sindh Bar Council, Pakistan Bar Council, HEC or the relevant "
              "court, because these details change.")

CTA = {"title": "Create your free WakeelBano account",
       "text": "Chamber matching, legal jobs across Pakistan, paid work and legal research tools. Always free for junior lawyers."}

SOURCES_COMMON = [
    ("Legal Practitioners and Bar Councils Act, 1973", "http://nasirlawsite.com/laws/baract.htm", "statute"),
    ("Sindh Bar Council — advocate verification portal", "https://advocates.sindhbarcouncil.org/", "official register"),
    ("Law and Justice Commission of Pakistan — women in the justice sector report (2024)", "https://ljcp.gov.pk/", "report"),
    ("Sindh Minimum Wages notification, 1 July 2026 — Sindh Labour Department", "https://lhr.sindh.gov.pk/", "notification"),
]


# ---------------------------------------------------------------- hubs
HUBS = [
    {
        "slug": "case-law/index.html",
        "url": "case-law/",
        "title": "Case Law Pakistan — Section-wise Research Guides | WakeelBano",
        "h1": "Case Law Pakistan",
        "desc": "Section-wise case law research guides for Pakistani lawyers: 302 PPC, 489-F PPC and 497 CrPC bail. Free databases, a four-step research method and a citation checklist.",
        "kicker": "Research library",
        "answer": "Pakistani lawyers search for case law more than anything else. This library shows where to find judgments, how to verify a citation, and how to use an authority in court.",
        "children": [
            ("302 PPC case law", "Qatl-i-amd: elements, qisas and the research method", "../case-law/302-ppc/index.html"),
            ("489-F PPC case law", "Cheque dishonour: complaint, defence and research", "../case-law/489-f/index.html"),
            ("497 CrPC case law", "Bail in non-bailable offences: grounds and authorities", "../case-law/497-crpc/index.html"),
        ],
        "sections": [
            {"h2": "Where can Pakistani lawyers find case law for free?",
             "answer": "The Supreme Court and every High Court publish judgments free on their official websites. Commercial databases add citation search on top of that.",
             "html": """
<table class="tbl">
<thead><tr><th>Source</th><th>What you get</th><th>Cost</th></tr></thead>
<tbody>
<tr><td>Supreme Court of Pakistan</td><td>Judgments, cause lists, case status</td><td>Free</td></tr>
<tr><td>High Courts (Sindh, Lahore, Peshawar, Balochistan, Islamabad) and the Federal Shariat Court</td><td>Reported judgments and orders</td><td>Free</td></tr>
<tr><td>Law databases (Pakistan Law Site, Pak Legal Database, LegalSearch)</td><td>PLD, SCMR, YLR and CLC citation search</td><td>Free or subscription</td></tr>
<tr><td>PLJ, published by the Punjab Bar Council section</td><td>Pakistan Law Journal citations</td><td>Subscription</td></tr>
<tr><td>AI research tools (LawGPT, DigiLawyer, Conclavity, PakLegalAI)</td><td>Fast first-pass research and drafting hints</td><td>Free or paid</td></tr>
</tbody>
</table>
"""},
            {"h2": "What is the fastest reliable way to research a section?",
             "answer": "Read the bare Act first, list each element as a separate issue, then look for five to eight leading judgments that deal with those issues.",
             "html": """
<ol class="steps">
<li><b>Frame the section.</b> Read the exact text of the bare Act and write the elements out as separate issues.</li>
<li><b>Hunt headnotes.</b> Search the section number with the key words you identified. Prefer Supreme Court authority, then your own High Court.</li>
<li><b>Extract the ratio.</b> One line per judgment: the principle the court applied. You rarely need a full case summary.</li>
<li><b>Distinguish.</b> Write down how your facts differ from each authority. This is the step AI cannot do for you, and the step judges test.</li>
</ol>
<div class="callout"><b>Verification rule:</b> Check every citation in three places — the citation number, the operative part of the judgment, and its current status after any appeal or review.</div>
"""},
            {"h2": "Why does WakeelBano not reproduce judgments?",
             "answer": "Because a wrong or invented citation damages a lawyer in court. We explain the framework and the method, and link you to the official source where the judgment can be read.",
             "html": """
<p>Reported judgments sit inside law reporters that carry their own editorial rights, and AI tools sometimes generate
citations that do not exist. Instead of reproducing text, we give you the statutory framework, an issue map, the
research method and a verification checklist — then link to the court's own publication.</p>
"""},
        ],
        "faqs": [
            ("Is WakeelBano free for lawyers?", "Yes. Every research guide on this site is free and needs no account. Junior lawyers get the full platform free."),
            ("Can I cite an authority I found through an AI tool?", "Not without checking it. Open the original judgment, confirm the citation and the operative paragraph, then check whether it has been reviewed or distinguished."),
        ],
        "related": [("Bail application format", "../drafts/bail-application-format/index.html"),
                    ("Legal notice format", "../drafts/legal-notice-format/index.html")],
    },
    {
        "slug": "drafts/index.html",
        "url": "drafts/",
        "title": "Legal Draft Formats in Pakistan — Bail, Notice, Plaint, Vakalatnama",
        "h1": "Legal Drafts Library",
        "desc": "Court-tested structures for Pakistani legal drafts: bail application, legal notice, civil plaint and vakalatnama. Every section, clause and common filing mistake explained.",
        "kicker": "Draft library",
        "answer": "Drafting is learned from structure, not from photocopies. Each guide here breaks a document into its required parts and lists the mistakes that get filings returned.",
        "children": [
            ("Bail application format", "Sections 496, 497 and 498 CrPC — structure and grounds", "../drafts/bail-application-format/index.html"),
            ("Legal notice format", "Recovery, cheque and rent notices, with proof of delivery", "../drafts/legal-notice-format/index.html"),
            ("Plaint format", "Order VII CPC — what a plaint must contain", "../drafts/plaint-format/index.html"),
            ("Vakalatnama format", "Authority, acceptance and stamp", "../drafts/vakalatnama-format/index.html"),
        ],
        "sections": [
            {"h2": "What do all court drafts have in common?",
             "answer": "Every court document follows the same skeleton: heading, title, facts, numbered grounds, legal basis, prayer and annexures. Only the labels change.",
             "html": """
<ol class="steps">
<li><b>Heading</b> — court, case number and parties.</li>
<li><b>Title</b> — what the document is and under which provision.</li>
<li><b>Facts</b> — dated and relevant, nothing extra.</li>
<li><b>Grounds or averments</b> — numbered, one point per paragraph.</li>
<li><b>Legal basis</b> — only sections and authorities you have verified yourself.</li>
<li><b>Prayer</b> — specific, and quantified where money is claimed.</li>
<li><b>Verification and annexures.</b></li>
</ol>
"""},
        ],
        "faqs": [
            ("Can I download ready-made templates?", "We publish structures and checklists rather than fill-in-the-blank templates, because a draft that ignores your facts is dangerous. Use the AI Kit to produce a first draft, then edit it yourself."),
        ],
        "related": [("Case law library", "../case-law/index.html"), ("AI Kit", "../index.html#ai-kit")],
    },
    {
        "slug": "career/index.html",
        "url": "career/",
        "title": "Legal Career in Pakistan — Law-GAT, Enrollment, Salary, Licence",
        "h1": "Career: From Sanad to the High Court",
        "desc": "The full Pakistani legal career path: Law-GAT, bar council enrollment, pupillage, realistic salary ranges and the High Court licence — stage by stage.",
        "kicker": "Career",
        "answer": "Becoming a practising lawyer in Pakistan takes about six years: five years of LLB, the Law-GAT, a six-month pupillage and enrollment with a provincial bar council.",
        "children": [
            ("Law-GAT 2026", "Test date, syllabus, past papers and result", "../career/law-gat/index.html"),
            ("Bar council enrollment", "Eligibility, documents, pupillage and fees", "../career/bar-council-enrollment/index.html"),
            ("How to become a lawyer", "Roadmap from 12th grade to the Supreme Court", "../career/how-to-become-lawyer-pakistan/index.html"),
            ("Lawyer salary in Pakistan", "Realistic ranges and the reason they are low", "../career/lawyer-salary-pakistan/index.html"),
            ("High Court licence", "Two years of practice, the process and the record", "../career/high-court-license/index.html"),
        ],
        "sections": [
            {"h2": "How long does each stage take?",
             "answer": "Five years for the LLB, one test cycle for the Law-GAT, six prescribed months of pupillage, then two years of practice before a High Court licence.",
             "html": """
<table class="tbl">
<thead><tr><th>Stage</th><th>Typical duration</th></tr></thead>
<tbody>
<tr><td>LLB</td><td>5 years</td></tr>
<tr><td>Law-GAT</td><td>Depends on the HEC test cycle</td></tr>
<tr><td>Pupillage</td><td>6 months (prescribed)</td></tr>
<tr><td>Lower court licence</td><td>After enrollment</td></tr>
<tr><td>High Court licence</td><td>After 2 years of practice</td></tr>
<tr><td>Supreme Court</td><td>After 7 years as a High Court advocate</td></tr>
</tbody>
</table>
"""},
        ],
        "faqs": [
            ("What is the first step after 12th grade?", "Get admission to a recognised LLB programme. Before you commit, spend one summer interning in a chamber so you know what the work actually feels like."),
            ("Is the Law-GAT compulsory?", "The prescribed test must be passed before enrollment as an advocate under Pakistan Bar Council rules. Confirm the current requirement with your provincial bar council."),
        ],
        "related": [("Lawyer jobs in Karachi", "../karachi/lawyer-jobs/index.html"),
                    ("Legal jobs in Pakistan", "../jobs/index.html")],
    },
    {
        "slug": "karachi/index.html",
        "url": "karachi/",
        "title": "Lawyers in Karachi — Jobs, Rooms and Chamber Sharing | WakeelBano",
        "h1": "Karachi for Lawyers",
        "desc": "Practical Karachi guides for lawyers: chamber and firm jobs, pupillage, the City Courts filing system and the routes that actually lead to paid work.",
        "kicker": "Karachi",
        "answer": "Karachi is where most Pakistani lawyers start, and three decisions shape the first year: which court you commit to, what you can afford to rent, and whose network you join.",
        "children": [
            ("Lawyer jobs in Karachi", "Chambers, firms, in-house and freelance work", "../karachi/lawyer-jobs/index.html"),
            ("Legal jobs in Pakistan", "Karachi, Lahore, Islamabad and remote", "../jobs/index.html"),
            ("Case law library", "Section-wise research guides", "../case-law/index.html"),
        ],
        "sections": [
            {"h2": "What are the three decisions that matter most?",
             "answer": "Pick one court, keep your living cost low enough to survive a small stipend, and build a referral network deliberately rather than hoping for one.",
             "html": """
<ol class="steps">
<li><b>Choose a court.</b> City Courts, Malir or the Sindh High Court. Mastery of one court beats rushing between five.</li>
<li><b>Cut the commute.</b> A chamber close to the courts saves hours a week; those hours are the difference between watching and drafting.</li>
<li><b>Build your network on purpose.</b> Chamber seniors, the bar room and your batchmates are the three channels that actually send work.</li>
</ol>
"""},
        ],
        "faqs": [
            ("How does a new lawyer find work in Karachi?", "Chambers rarely advertise. Visit with a CV, ask for pupillage, and use the Karachi jobs page for the firms and companies that do advertise."),
            ("Where are legal jobs in Karachi advertised?", "Mostly they are not. Chambers hire through visits and referrals. Firms and companies do advertise, but the hidden market is much larger."),
        ],
        "related": [("Lawyer jobs in Karachi", "../karachi/lawyer-jobs/index.html"),
                    ("Legal jobs in Pakistan", "../jobs/index.html")],
    },
]


# ---------------------------------------------------------------- articles
PAGES = [
    {
        "slug": "career/law-gat/index.html",
        "url": "career/law-gat/",
        "title": "Law-GAT 2026: Test Date, Syllabus, Past Papers and Result",
        "h1": "Law-GAT 2026 — the Law Graduate Assessment Test",
        "desc": "What Law-GAT is, who can sit it, how to register, what the syllabus covers, how to use past papers, and where to check your result. A complete guide for Pakistani law graduates.",
        "kicker": "Career · Entry",
        "answer": "Law-GAT is the assessment test that Pakistani law graduates must pass before enrolling as an advocate. It is conducted by HEC with the Pakistan Bar Council and is normally held twice a year.",
        "facts": [
            ("Conducted by", "Higher Education Commission (HEC) with the Pakistan Bar Council"),
            ("Frequency", "Usually twice a year; HEC confirms each cycle"),
            ("Required for", "Advocate enrollment with a provincial bar council"),
            ("Format", "Multiple-choice questions across core legal subjects"),
            ("Result", "Checked on the official HEC portal with roll number or CNIC"),
        ],
        "sections": [
            {"h2": "Who is eligible to sit the Law-GAT?",
             "answer": "Candidates need a recognised LLB or equivalent degree, identity documents and the prescribed fee. Final-year students can often apply, but confirm the current notification.",
             "html": """
<ul>
<li>A recognised <b>LLB</b>, or an equivalent degree accepted by the Pakistan Bar Council</li>
<li>CNIC and degree or transcript details</li>
<li>Registration fee for that cycle, paid through the route stated in the notification</li>
<li>Foreign degree holders must first complete HEC equivalence</li>
</ul>
<div class="callout"><b>Do this first:</b> read the current notification on HEC's official website. Do not trust dates forwarded on WhatsApp or published on blogs, including this page.</div>
"""},
            {"h2": "What does the syllabus cover?",
             "answer": "The test centres on core subjects: constitutional law, criminal law and procedure, civil law, the law of evidence and family law, plus legal English.",
             "html": """
<table class="tbl">
<thead><tr><th>Subject</th><th>What to revise</th></tr></thead>
<tbody>
<tr><td>Constitutional law</td><td>Fundamental rights, writ jurisdiction, key constitutional provisions</td></tr>
<tr><td>Criminal law</td><td>Core PPC offences (qatl, hurt, property) and CrPC procedure</td></tr>
<tr><td>Civil law</td><td>CPC (plaint, jurisdiction, appeals), Contract Act, Specific Relief</td></tr>
<tr><td>Law of evidence</td><td>Qanun-e-Shahadat 1984: relevancy, burden of proof, documents</td></tr>
<tr><td>Family law</td><td>MFLO 1961, dissolution of marriage, custody, maintenance</td></tr>
<tr><td>Legal English</td><td>Comprehension, legal terminology, drafting basics</td></tr>
</tbody>
</table>
"""},
            {"h2": "What is a realistic 60-day preparation plan?",
             "answer": "Spend the first ten days on bare Acts, the next fifteen on subject-wise practice questions, then past papers under time pressure, and the final week on revision only.",
             "html": """
<ol class="steps">
<li><b>Days 1–10:</b> read the bare Acts for PPC, CrPC and CPC. Turn key sections into flashcards.</li>
<li><b>Days 11–25:</b> subject-wise practice questions. Write down the <i>reason</i> for every wrong answer.</li>
<li><b>Days 26–40:</b> past papers under timed conditions. Keep a list of weak areas.</li>
<li><b>Days 41–52:</b> weak areas, plus evidence and family law.</li>
<li><b>Days 53–60:</b> revision and full-length mocks. Add no new material.</li>
</ol>
"""},
            {"h2": "Where do you check the result and answer key?",
             "answer": "Only on the official HEC result portal, using your roll number or CNIC. Result day traffic is heavy, so retry on the official portal rather than clicking on forwarded links.",
             "html": """
<p class="mini">Warning: any "leaked result" link shared before the official announcement is usually phishing. Log in only through the official portal.</p>
"""},
            {"h2": "What happens after you pass?",
             "answer": "You apply to your provincial bar council for enrollment, which includes a prescribed pupillage in a senior advocate's chamber.",
             "html": """
<p>In Sindh, the application goes to the Sindh Bar Council and includes a six-month pupillage, documents and the current fees.
The full sequence is in our <a href="../bar-council-enrollment/index.html">bar council enrollment guide</a>.</p>
"""},
        ],
        "faqs": [
            ("How many times a year is the Law-GAT held?", "Usually twice a year, but HEC confirms the schedule for each cycle. Always check the official notification."),
            ("Can I become an advocate without the Law-GAT?", "The prescribed test must be passed before enrollment as an advocate. Confirm the current requirement with your provincial bar council."),
            ("What if I fail?", "You can normally attempt the next cycle. Use the gap to work in a chamber: drafting practice helps both the retest and the pupillage that follows."),
            ("When is the result announced?", "The result timeline is set by HEC in each notification and published on its official portal."),
        ],
        "sources": [
            ("Higher Education Commission — Law-GAT notifications", "https://www.hec.gov.pk/", "official"),
            ("Pakistan Bar Council — enrollment rules and forms", "https://pakistanbarcouncil.org/", "official"),
        ],
        "related": [("Bar council enrollment guide", "career/bar-council-enrollment/index.html"),
                    ("Lawyer salary in Pakistan", "career/lawyer-salary-pakistan/index.html"),
                    ("High Court licence", "career/high-court-license/index.html")],
    },
    {
        "slug": "case-law/302-ppc/index.html",
        "url": "case-law/302-ppc/",
        "title": "302 PPC Case Law — Qatl-i-amd in Pakistan (Research Guide)",
        "h1": "302 PPC Case Law — Qatl-i-amd",
        "desc": "Section 302 PPC explained: punishment, the elements courts examine, qisas, waiver and compounding, plus how to research 302 case law in Pakistan properly.",
        "kicker": "Case law · Criminal",
        "answer": "Section 302 of the Pakistan Penal Code sets the punishment for qatl-i-amd (intentional murder). The court chooses between death as qisas, imprisonment for life, or a term of imprisonment, depending on the facts and on the qisas process.",
        "facts": [
            ("Statute", "Pakistan Penal Code 1860, Chapter XVI"),
            ("Definitions", "Section 300 defines qatl-i-amd and its exceptions"),
            ("Punishment", "Section 302 — death as qisas, life imprisonment, or a term of imprisonment"),
            ("Related sections", "299 (definitions), 301, 304, 305–310 (qisas, waiver, compounding)"),
            ("Most searched form", "\u201c302 case law pakistan in urdu\u201d"),
        ],
        "sections": [
            {"h2": "What does section 302 actually provide?",
             "answer": "It provides the punishment for qatl-i-amd: death as qisas where qisas is available, imprisonment for life where qisas is waived or not applicable, or imprisonment for a stated term.",
             "html": """
<p>The section cannot be read alone. The chain runs through section 299 (definitions), 300 (when culpable homicide becomes
qatl-i-amd), 301 (transfer of intent), 302 (punishment), and 304 to 310, which govern qisas, waiver and compounding.
Read the bare Act for the exact wording before you rely on any summary.</p>
"""},
            {"h2": "Which issues does the court decide in a 302 case?",
             "answer": "Four questions dominate: whether the offence is qatl-i-amd or a lesser form, whether each element is proved, whether qisas is available or waived, and whether a lesser conviction fits the record.",
             "html": """
<table class="tbl">
<thead><tr><th>Issue</th><th>What the court looks at</th></tr></thead>
<tbody>
<tr><td>Intent</td><td>Motive, weapon, site of injury, medical evidence</td></tr>
<tr><td>Proof of elements</td><td>Mens rea, act, causation, official and medical record</td></tr>
<tr><td>Qisas</td><td>Heirs, waiver, compounding under sections 305–310</td></tr>
<tr><td>Lesser conviction</td><td>Whether the record supports 304, 308 or a hurt offence instead</td></tr>
<tr><td>Evidence</td><td>Ocular testimony, delay in FIR, identification, recovery</td></tr>
</tbody>
</table>
"""},
            {"h2": "How do you research 302 case law in Pakistan?",
             "answer": "Search the court portals using section-based key words, start from headnotes, then read the operative paragraph of every judgment and confirm it has not been reviewed.",
             "html": """
<ol class="steps">
<li>Search the Supreme Court and High Court portals with: "302 PPC", "qatl-i-amd", "qisas", "waiver", "304 PPC", "benefit of doubt".</li>
<li>Use reporters such as PLD, SCMR and YLR to find the headnote, then read the operative part of the judgment itself.</li>
<li>Check whether a later bench has reviewed, overruled or distinguished the authority.</li>
<li>Prefer the binding authority of your own High Court before citing another province's judgment.</li>
</ol>
<div class="callout"><b>Never file a citation you have not opened.</b> AI tools can generate citations that do not exist, and a wrong citation is the fastest way to lose a judge's confidence.</div>
"""},
        ],
        "faqs": [
            ("What is the punishment under section 302 PPC?", "Death as qisas, imprisonment for life, or imprisonment for a stated term, depending on the facts and the qisas process. Always read the bare Act and the current authority."),
            ("Can qisas be waived in a 302 case?", "The qisas framework in sections 305 to 310 deals with waiver and compounding, and a waiver can change the sentence. The effect depends on your facts, so check the latest authority."),
            ("What is the difference between 302 and 324 PPC?", "Section 302 concerns qatl-i-amd and its punishment, while section 324 concerns an attempt to commit qatl. Compare the elements in the bare Act."),
        ],
        "sources": [
            ("Supreme Court of Pakistan — judgments", "https://www.supremecourt.gov.pk/", "official"),
            ("Sindh High Court — case law portal", "https://caselaw.shc.gov.pk/", "official"),
        ],
        "related": [("497 CrPC bail case law", "case-law/497-crpc/index.html"),
                    ("Bail application format", "drafts/bail-application-format/index.html"),
                    ("Case law library", "case-law/index.html")],
    },
    {
        "slug": "drafts/bail-application-format/index.html",
        "url": "drafts/bail-application-format/",
        "title": "Bail Application Format in Pakistan — Structure and Grounds",
        "h1": "Bail Application Format (Pakistan)",
        "desc": "How a bail application is structured in Pakistan: sections 496, 497 and 498 CrPC, the seven parts of the application, grounds the court actually hears, and common mistakes.",
        "kicker": "Drafts · Criminal",
        "answer": "A bail application in Pakistan has seven parts: heading, title, brief facts, numbered grounds, legal basis, prayer and annexures. The grounds must be tied to facts on the record, not to general statements.",
        "facts": [
            ("Bailable offences", "Section 496 CrPC"),
            ("Non-bailable offences", "Section 497 CrPC"),
            ("Sessions Court and High Court powers", "Section 498 CrPC"),
            ("Illegal detention", "Section 491 CrPC"),
            ("Bail after conviction", "Section 426 CrPC"),
        ],
        "sections": [
            {"h2": "Which section applies to your case?",
             "answer": "Read the sections in the FIR first: if the offence is bailable, section 496 applies; if it is non-bailable, section 497 applies and section 498 governs the higher courts.",
             "html": """
<table class="tbl">
<thead><tr><th>Provision</th><th>When it applies</th></tr></thead>
<tbody>
<tr><td>496 CrPC</td><td>Bailable offences</td></tr>
<tr><td>497 CrPC</td><td>Non-bailable offences, including the further-inquiry discretion</td></tr>
<tr><td>498 CrPC</td><td>Bail powers of the Sessions Court and High Court</td></tr>
<tr><td>491 CrPC</td><td>Illegal detention</td></tr>
<tr><td>426 CrPC</td><td>Suspension of sentence and bail pending appeal</td></tr>
</tbody>
</table>
"""},
            {"h2": "What does a well-drafted application look like?",
             "answer": "It is short. Four to six lines of facts, then numbered grounds, one legal point each, and a prayer that states exactly what the court should order.",
             "html": """
<ol class="steps">
<li><b>Heading:</b> court, case or FIR number, police station, sections and parties.</li>
<li><b>Title:</b> "Application for grant of bail under section ___ CrPC".</li>
<li><b>Brief facts:</b> the FIR version, the accused's role, the date of arrest and the custody period.</li>
<li><b>Grounds:</b> numbered, each one a separate legal point tied to the record.</li>
<li><b>Legal basis:</b> only provisions and authorities you have verified.</li>
<li><b>Prayer:</b> a clear request, plus any conditions you accept.</li>
<li><b>Verification, affidavit and vakalatnama.</b></li>
</ol>
"""},
            {"h2": "Which grounds does the court actually consider?",
             "answer": "Grounds that are documented: investigation already complete, no flight risk, weak or suspicious evidence, delay, parity with a co-accused, and health or age factors.",
             "html": """
<ul>
<li><b>Investigation complete</b> — no further recovery or interrogation is needed</li>
<li><b>No flight risk</b> — permanent address, family and roots in the community</li>
<li><b>Weak evidence</b> — point to specific gaps in the record, not to argument</li>
<li><b>Delay</b> — in the FIR, in arrest, or in trial</li>
<li><b>Parity</b> — a co-accused has already been granted bail, with the order cited</li>
<li><b>Health, age or gender</b> — supported by documents</li>
</ul>
<div class="callout"><b>Practice tip:</b> Attach facts to each ground. "The accused has been in custody for three days, the challan is filed and no recovery is on record" persuades; "the accused is innocent" does not.</div>
"""},
            {"h2": "What are the most common drafting mistakes?",
             "answer": "Confusing bail with acquittal, repeating the whole FIR, citing unverified authority, leaving the prayer vague and filing incomplete annexures.",
             "html": """
<p>Bail decides release during trial, not guilt. Keep the language to that question, and check court fee and stamp requirements
at the filing branch, because they vary by court and by the nature of the case.</p>
"""},
        ],
        "faqs": [
            ("Do bail applications have to be in English?", "Court filings are normally in English. An Urdu summary for the client is useful, but the filing itself follows the court's practice."),
            ("What is the difference between sections 497 and 498 CrPC?", "Section 497 sets out bail in non-bailable offences before the trial court, while section 498 gives the Sessions Court and High Court power to grant bail. The forum you choose decides which provision you rely on."),
            ("What if bail is refused?", "Read the reasons recorded in the order, strengthen the grounds with record-based facts, and consider the appellate forum. Check the procedure and limitation for your case type."),
        ],
        "sources": [
            ("Sindh High Court — rules and practice", "https://www.sindhhighcourt.gov.pk/", "official"),
            ("Pakistan Bar Council — professional conduct rules", "https://pakistanbarcouncil.org/", "official"),
        ],
        "related": [("497 CrPC case law", "case-law/497-crpc/index.html"),
                    ("Legal notice format", "drafts/legal-notice-format/index.html"),
                    ("302 PPC case law", "case-law/302-ppc/index.html")],
    },
    {
        "slug": "drafts/legal-notice-format/index.html",
        "url": "drafts/legal-notice-format/",
        "title": "Legal Notice Format in Pakistan — Recovery, Cheque and Rent",
        "h1": "Legal Notice Format (Pakistan)",
        "desc": "How to draft a legal notice in Pakistan: the nine required parts, how to prove delivery, what a 15-day period really means, and the mistakes that weaken a notice.",
        "kicker": "Drafts · Civil",
        "answer": "A legal notice is a formal written demand that sets out the facts, the default, the exact relief wanted and a deadline. Written properly, it ends many disputes before a suit is filed.",
        "facts": [
            ("Typical deadline", "15 days is common practice, but statutory periods vary"),
            ("Proof of delivery", "Registered post with acknowledgement due, or tracked courier"),
            ("Common uses", "Recovery of money, cheque dishonour, rent, contract breach, defamation"),
            ("No government fee", "The cost is professional fees and postage"),
        ],
        "sections": [
            {"h2": "When should a legal notice be sent?",
             "answer": "Before litigation, whenever a demand can still resolve the dispute, and whenever a statute requires prior notice as a condition for filing.",
             "html": """
<ul>
<li><b>Recovery of money</b> — unpaid loans, invoices or services</li>
<li><b>Cheque dishonour</b> — before a 489-F PPC complaint</li>
<li><b>Rent and eviction</b> — under the applicable rented premises law</li>
<li><b>Breach of contract</b> — demanding performance or accepting termination</li>
<li><b>Property and possession</b> — warning against unlawful dispossession</li>
<li><b>Defamation</b> — demanding a retraction</li>
</ul>
"""},
            {"h2": "What are the nine parts of a legal notice?",
             "answer": "Letterhead and date, correct addressee, subject line, chronology, the default, the exact demand, the deadline, the consequence and a reservation of rights.",
             "html": """
<ol class="steps">
<li>Letterhead, date and reference number</li>
<li>Full name and complete postal address of the addressee</li>
<li>A specific subject line, such as "Legal notice for recovery of Rs ___"</li>
<li>Chronology with dates: when the agreement was made, what was delivered, what remains due</li>
<li>The default or breach, tied to a clause or section</li>
<li>A precise demand: the exact amount or action</li>
<li>A deadline, commonly 15 days</li>
<li>The consequence of non-compliance, including costs</li>
<li>Reservation of rights and the advocate's signature</li>
</ol>
"""},
            {"h2": "How do you prove the notice was delivered?",
             "answer": "Send it by registered post with acknowledgement due or a tracked courier, and keep the receipt, the tracking record and a copy of the notice in your file.",
             "html": """
<p>In court, the first question is not what the notice said but whether it was served. Email or WhatsApp notices only work where the
contract or the law allows them, and even then you must keep the send confirmation and a screenshot.</p>
<div class="callout"><b>Note:</b> the date on the notice and the date of dispatch are different things. Courts look at both.</div>
"""},
            {"h2": "Is a 15-day period always required?",
             "answer": "No. Some statutes prescribe their own period, such as suits against the government, so check the specific section rather than assuming 15 days.",
             "html": """
<p>Fifteen days is a common practice for commercial demands. Where a statute sets a period, that period governs, and the
notice must comply with its form as well as its timing.</p>
"""},
        ],
        "faqs": [
            ("How much does a legal notice cost?", "There is no government fee. The cost is the advocate's professional fee plus registered post or courier charges. Court fee applies only when a suit or complaint is filed."),
            ("Can a legal notice be sent by WhatsApp?", "Only where the contract or the law permits electronic service, and only with proof of delivery saved. Registered post or courier remains the safer default."),
            ("Is a notice required before a cheque dishonour complaint?", "Practice and the facts of your case determine this. Check the section, the current approach of the courts, and keep proof that your demand reached the other side."),
        ],
        "sources": [
            ("Pakistan Post — registered post with acknowledgement due", "https://www.pakpost.gov.pk/", "service"),
            ("Sindh High Court — civil practice", "https://www.sindhhighcourt.gov.pk/", "official"),
        ],
        "related": [("489-F PPC case law", "case-law/489-f/index.html"),
                    ("Plaint format", "drafts/plaint-format/index.html"),
                    ("Bail application format", "drafts/bail-application-format/index.html")],
    },
    {
        "slug": "career/bar-council-enrollment/index.html",
        "url": "career/bar-council-enrollment/",
        "title": "Bar Council Enrollment in Pakistan — Step-by-Step Guide",
        "h1": "Bar Council Enrollment — the Full Route to Sanad",
        "desc": "How advocate enrollment works in Pakistan: eligibility under the 1973 Act, documents, the six-month pupillage, fees, the enrollment committee and licence verification.",
        "kicker": "Career · Licensing",
        "answer": "Enrollment as an advocate requires a recognised LLB, the prescribed test, a six-month pupillage in a senior advocate's chamber, the documents and fees, and clearance by the provincial bar council's enrollment committee.",
        "facts": [
            ("Governing law", "Legal Practitioners and Bar Councils Act, 1973 (sections 26 and 27)"),
            ("Minimum age", "21 years"),
            ("Pupillage", "6 months with a senior advocate, commonly 10 years' standing"),
            ("Regulator in Sindh", "Sindh Bar Council, Karachi"),
            ("Roll size", "Sindh Bar Council registration numbers passed 55,000 in 2026"),
        ],
        "sections": [
            {"h2": "Who is eligible for enrollment?",
             "answer": "A Pakistani or AJK citizen, at least 21 years old, holding a recognised LLB or Bar-at-Law, who has passed the prescribed test and meets the character requirements.",
             "html": """
<ul>
<li>Citizenship of Pakistan or Azad Jammu and Kashmir</li>
<li>Minimum age of 21 years</li>
<li>LLB or Bar-at-Law recognised by the Pakistan Bar Council</li>
<li>Prescribed test passed, under Pakistan Bar Council rules</li>
<li>No disqualification under sections 26 and 27 of the 1973 Act</li>
</ul>
<p class="mini">Holders of foreign degrees must first complete HEC and Pakistan Bar Council equivalence.</p>
"""},
            {"h2": "What is the step-by-step process?",
             "answer": "Pass the Law-GAT, complete six months of pupillage, prepare the document set, apply to the provincial bar council with the fees, appear before the enrollment committee, then collect the certificate and identity card.",
             "html": """
<ol class="steps">
<li><b>Law-GAT</b> — pass the test (see the <a href="../law-gat/index.html">Law-GAT guide</a>).</li>
<li><b>Pupillage</b> — six prescribed months in a senior's chamber.</li>
<li><b>Documents</b> — LLB degree and transcripts, CNIC, photographs, character certificate, test result and the prescribed forms.</li>
<li><b>Application</b> — file with the Sindh Bar Council in Sindh, with the enrollment fee, benevolent fund and other charges set by its rules.</li>
<li><b>Enrollment committee</b> — review and interview.</li>
<li><b>Certificate and identity card</b> — issued on approval.</li>
</ol>
<div class="callout"><b>Figures change:</b> fee amounts, challan routes and checklists are revised from time to time. Confirm the current requirements at the bar council office or website, not on a blog.</div>
"""},
            {"h2": "Why is pupillage the hardest step?",
             "answer": "Because there is no placement system. Pupillage is mandatory, but finding a chamber still depends almost entirely on personal contacts.",
             "html": """
<p>This is the gap WakeelBano exists to close. Practical ways to make pupillage count:</p>
<ul>
<li>Take a one-page CV to a chamber visit: what you want to learn, how much time you can give, which area interests you</li>
<li>Agree the terms at the start: hours, type of work, any stipend, and what you will be taught</li>
<li>Write one page of notes every day — six months later that record is worth more than the degree</li>
<li>Browse verified chambers in <a href="../../index.html#chambers">Chamber Match</a> on WakeelBano</li>
</ul>
"""},
            {"h2": "How do you verify an advocate's licence?",
             "answer": "Search the provincial bar council roll by name or registration number. In Sindh, the Sindh Bar Council publishes an advocate verification portal showing district, licence type and status.",
             "html": """
<p>Clients and employers should always verify against the roll rather than a screenshot. It is the simplest defence against
imposters, an issue the Sindh Bar Council has publicly flagged more than once.</p>
"""},
            {"h2": "What should you do in the first 90 days after enrollment?",
             "answer": "Commit to one court and a few case types, start a practice record, build a clean public profile, and tell twenty people in person what you do.",
             "html": """
<ul>
<li>Fix your court, area and case types — spreading thin does not generate income</li>
<li>Record every appearance and file, because the High Court licence will need that record</li>
<li>Set up a LinkedIn profile, WhatsApp Business and a verified listing</li>
<li>Tell your network directly: most first briefs come from referrals, not advertising</li>
</ul>
"""},
        ],
        "faqs": [
            ("How long does it take to become an advocate in Pakistan?", "A five-year LLB, the Law-GAT, six prescribed months of pupillage and the enrollment process: roughly six years in total, depending on individual timing."),
            ("Is the pupillage paid?", "Not necessarily. Some chambers pay a stipend and many do not, which is why agreeing the terms in writing at the start is important."),
            ("How much are enrollment fees?", "The enrollment fee, benevolent fund and other charges are set by bar council rules and are revised over time. Ask the Sindh Bar Council for the current challan and breakdown."),
            ("Can I practise in another province after enrolling in Sindh?", "Practice rights follow your enrollment and licence type. Confirm the position with the bar council concerned before taking instructions outside your province."),
        ],
        "sources": [
            ("Legal Practitioners and Bar Councils Act, 1973", "http://nasirlawsite.com/laws/baract.htm", "statute"),
            ("Sindh Bar Council — advocate verification", "https://advocates.sindhbarcouncil.org/", "official register"),
            ("Pakistan Bar Council — enrollment", "https://pakistanbarcouncil.org/", "official"),
        ],
        "related": [("Law-GAT guide", "career/law-gat/index.html"),
                    ("How to become a lawyer", "career/how-to-become-lawyer-pakistan/index.html"),
                    ("Lawyer salary in Pakistan", "career/lawyer-salary-pakistan/index.html")],
    },
    {
        "slug": "career/lawyer-salary-pakistan/index.html",
        "url": "career/lawyer-salary-pakistan/",
        "title": "Lawyer Salary in Pakistan 2026 — Junior, Firm and Independent",
        "h1": "Lawyer Salary in Pakistan (2026)",
        "desc": "Realistic lawyer salary ranges in Pakistan for 2026: pupillage, junior associates, law firms and independent practice, compared with the Sindh minimum wage.",
        "kicker": "Career · Money",
        "answer": "Most fresh lawyers in Pakistan earn between Rs 25,000 and Rs 50,000 a month, and many pupils are paid nothing at all, while the Sindh minimum wage for unskilled work is Rs 43,000.",
        "facts": [
            ("Pupillage", "Rs 0 to 25,000 a month"),
            ("Junior associate, litigation chamber", "Rs 25,000 to 50,000"),
            ("Law firm associate", "Rs 50,000 to 120,000+"),
            ("Mid-level, 3–7 years", "Rs 80,000 to 250,000"),
            ("Sindh minimum wage, 2026–27", "Rs 43,000 a month"),
        ],
        "sections": [
            {"h2": "What are the realistic salary ranges?",
             "answer": "Litigation chambers pay the least and law firms the most, with corporate and in-house roles paying more than chambers at every level of experience.",
             "html": """
<table class="tbl">
<thead><tr><th>Stage</th><th>Typical monthly (PKR)</th><th>Note</th></tr></thead>
<tbody>
<tr><td>Internship or pupillage</td><td>0 – 25,000</td><td>Frequently unpaid</td></tr>
<tr><td>Fresh associate, litigation chamber</td><td>25,000 – 50,000</td><td>Karachi and Lahore at the upper end</td></tr>
<tr><td>Corporate law firm associate</td><td>50,000 – 120,000+</td><td>Higher pay, longer hours</td></tr>
<tr><td>Mid-level, 3–7 years</td><td>80,000 – 250,000</td><td>Depends on firm type and client base</td></tr>
<tr><td>Independent practice</td><td>Variable</td><td>Fee per case; low at first, rising with reputation</td></tr>
</tbody>
</table>
<p class="mini">Ranges are indicative and drawn from public salary discussions, market reporting and practice observation between 2023 and 2026. Your city, firm and practice area will move the number.</p>
"""},
            {"h2": "Why is the pay so low compared with the minimum wage?",
             "answer": "Because Pakistani litigation uses a lump-sum fee per case rather than hourly billing, so a junior's time is a cost to the senior rather than billable revenue.",
             "html": """
<ul>
<li><b>Lump-sum fees:</b> there is no hourly billing culture in most chambers, so juniors are not revenue producers</li>
<li><b>Training period:</b> a fresh graduate typically needs one to two years to become useful</li>
<li><b>Retention:</b> many juniors leave within two years, which discourages investment</li>
<li><b>Supply:</b> thousands of graduates enter the market each year for a limited number of paid seats</li>
</ul>
<div class="callout"><b>Know your position:</b> put the chamber terms in writing. "You are here to learn" does not mean you cannot agree a minimum contribution towards expenses and a clear scope of training.</div>
"""},
            {"h2": "How can a junior lawyer increase income?",
             "answer": "Specialise in one area, master one court, take remote drafting work from foreign firms, build a visible professional profile and use idle hours for paid research and drafting.",
             "html": """
<ol class="steps">
<li><b>Specialise.</b> A lawyer who does everything has no rate.</li>
<li><b>Master one court.</b> Learn its practice, its filing staff and its judges' expectations.</li>
<li><b>Add remote work.</b> Foreign firms pay in dollars for drafting, research and document review.</li>
<li><b>Be visible.</b> Educational content within professional conduct rules brings referrals.</li>
<li><b>Fill idle time.</b> The Kaam Board on WakeelBano lists paid drafting and research tasks.</li>
</ol>
"""},
            {"h2": "What is a good way to negotiate chamber terms?",
             "answer": "Offer a specific commitment in return for a specific arrangement: hours, learning scope and a minimum monthly amount, agreed in writing.",
             "html": """
<p>A workable opening: "I can commit six months, I want to work on drafting, research and court appearances, and I would
like a minimum of Rs ___ a month plus one study day a week." Specific candidates get taken seriously; candidates who only ask
about pay are replaced.</p>
"""},
        ],
        "faqs": [
            ("What is a fresh lawyer's salary in Pakistan?", "Usually Rs 25,000 to Rs 50,000 a month, depending on the city and the firm. Many chambers pay no stipend during pupillage."),
            ("Can a chamber legally pay below the minimum wage?", "This depends on how the relationship is classified and on the sector-specific rules. Many chambers treat juniors as trainees rather than employees. For your own position, take advice from a labour or employment lawyer."),
            ("How much do independent lawyers earn?", "There is no fixed figure. The first year or two is often very low, and income rises with reputation and case flow. Many lawyers supplement it with teaching, drafting or freelance work."),
        ],
        "sources": [
            ("Sindh minimum wage notification, effective 1 July 2026", "https://lhr.sindh.gov.pk/", "notification"),
            ("Dawn — junior lawyers' pay dispute (2023)", "https://www.dawn.com/news/1777625", "news"),
            ("Profit — the economics of junior lawyers (2023)", "https://profit.pakistantoday.com.pk/2023/11/12/cant-pay-the-bills-with-experience", "news"),
        ],
        "related": [("Lawyer jobs in Karachi", "karachi/lawyer-jobs/index.html"),
                    ("How to become a lawyer", "career/how-to-become-lawyer-pakistan/index.html"),
                    ("Legal jobs in Pakistan", "jobs/index.html")],
    },
    {
        "slug": "career/how-to-become-lawyer-pakistan/index.html",
        "url": "career/how-to-become-lawyer-pakistan/",
        "title": "How to Become a Lawyer in Pakistan — Complete Roadmap",
        "h1": "How to Become a Lawyer in Pakistan",
        "desc": "The full roadmap from 12th grade to the Supreme Court: LLB admission, Law-GAT, pupillage, enrollment, the High Court licence, and what to do at each stage.",
        "kicker": "Career · Roadmap",
        "answer": "To become a lawyer in Pakistan you need a five-year LLB, the Law-GAT, a six-month pupillage and enrollment with a provincial bar council, which takes about six years in total.",
        "facts": [
            ("First degree", "LLB, five years after intermediate"),
            ("Test", "Law-GAT, conducted by HEC with the Pakistan Bar Council"),
            ("Pupillage", "Six prescribed months in a senior's chamber"),
            ("First licence", "Advocate, enrolled with the provincial bar council"),
            ("High Court", "After two years of practice"),
        ],
        "sections": [
            {"h2": "What does the full roadmap look like?",
             "answer": "LLB, then the Law-GAT, then pupillage, then enrollment, then two years of practice before a High Court licence and seven more before the Supreme Court.",
             "html": """
<table class="tbl">
<thead><tr><th>Stage</th><th>Requirement</th><th>Time</th></tr></thead>
<tbody>
<tr><td>LLB</td><td>Intermediate plus a university admission test</td><td>5 years</td></tr>
<tr><td>Law-GAT</td><td>LLB and registration under the HEC notification</td><td>Per test cycle</td></tr>
<tr><td>Pupillage</td><td>A senior advocate's chamber</td><td>6 months</td></tr>
<tr><td>Enrollment</td><td>Documents, fees and committee review</td><td>A few months</td></tr>
<tr><td>High Court licence</td><td>Two years of practice and an application</td><td>2 years</td></tr>
<tr><td>Supreme Court</td><td>Seven years as a High Court advocate</td><td>7 years</td></tr>
</tbody>
</table>
"""},
            {"h2": "What should you look for in an LLB programme?",
             "answer": "A Pakistan Bar Council recognised university, a curriculum that includes supervised internships, and a location you can afford for five years.",
             "html": """
<ul>
<li><b>Recognition:</b> confirm HEC and Pakistan Bar Council recognition before paying any fee</li>
<li><b>Cost:</b> public colleges are far cheaper than private universities over five years</li>
<li><b>Practice exposure:</b> moots, internships and legal aid clinics matter more than the brochure</li>
<li><b>Test it first:</b> spend one summer in a chamber before committing five years</li>
</ul>
"""},
            {"h2": "What should you do during law school that pays off later?",
             "answer": "Complete three different internships, write drafts by hand, do two serious moots and read one judgment a day in English.",
             "html": """
<ol class="steps">
<li><b>Three internships</b> — a trial court chamber, a law firm and an in-house legal department.</li>
<li><b>Write drafts</b> — a plaint, written statement, bail application and notice every week, from scratch.</li>
<li><b>Moot twice</b> — oral advocacy confidence is built only by standing up.</li>
<li><b>Legal English</b> — one judgment and a five-line summary every day.</li>
<li><b>Pick an area</b> — match your interest with where the work actually is.</li>
</ol>
"""},
            {"h2": "Where do people lose the most time?",
             "answer": "They study without ever entering a chamber, rely on contacts instead of skills, refuse to specialise, and leave their documents incomplete.",
             "html": """
<p>Each of these costs months. A student who interns early, drafts weekly and keeps a clean document file moves through the
Law-GAT and enrollment significantly faster than one who starts preparing after graduation.</p>
"""},
        ],
        "faqs": [
            ("Can I become a lawyer after 10th grade?", "No. You need intermediate, then a five-year LLB. After 10th grade you can only take support roles such as a court clerk or office assistant."),
            ("Is it possible to study law in Urdu medium?", "The degree and court work are in English, so legal English has to be built. Many successful lawyers come from Urdu-medium backgrounds, but drafting and reading happen in English."),
            ("How much does it cost to become a lawyer?", "It varies widely: public law colleges are inexpensive, while private universities can cost several lakh over five years, before test fees, enrollment fees and pupillage costs."),
        ],
        "sources": [
            ("Higher Education Commission — recognised programmes", "https://www.hec.gov.pk/", "official"),
            ("Pakistan Bar Council — legal education", "https://pakistanbarcouncil.org/", "official"),
        ],
        "related": [("Bar council enrollment", "career/bar-council-enrollment/index.html"),
                    ("Law-GAT guide", "career/law-gat/index.html"),
                    ("Lawyer salary in Pakistan", "career/lawyer-salary-pakistan/index.html")],
    },
    {
        "slug": "karachi/lawyer-jobs/index.html",
        "url": "karachi/lawyer-jobs/",
        "title": "Lawyer Jobs in Karachi — Chambers, Firms and In-House",
        "h1": "Lawyer Jobs in Karachi",
        "desc": "Where legal jobs actually exist in Karachi: chambers, law firms, corporate legal departments and remote work, plus a CV structure and realistic salary expectations.",
        "kicker": "Karachi · Jobs",
        "answer": "Most legal jobs in Karachi are never advertised. Chambers hire through visits and referrals, so a one-page CV and a sample draft delivered in person works better than applying online.",
        "facts": [
            ("Hidden market", "Most chamber positions are filled through referrals"),
            ("Pupil or trainee", "Rs 0 to 25,000 a month"),
            ("Junior chamber associate", "Rs 25,000 to 50,000"),
            ("Law firm associate", "Rs 50,000 to 120,000+"),
            ("In-house, 0–2 years", "Rs 60,000 to 120,000"),
        ],
        "sections": [
            {"h2": "What kinds of legal jobs exist in Karachi?",
             "answer": "Six types: chamber associate, law firm associate, in-house counsel, public sector roles, court research assistantships and remote freelance work.",
             "html": """
<table class="tbl">
<thead><tr><th>Type</th><th>What the work looks like</th><th>Where</th></tr></thead>
<tbody>
<tr><td>Chamber associate or pupil</td><td>Drafting, research, appearances with a senior</td><td>City Courts and Sindh High Court chambers</td></tr>
<tr><td>Law firm associate</td><td>Corporate, tax, disputes and transactions</td><td>Karachi's commercial districts</td></tr>
<tr><td>In-house legal</td><td>Contracts, compliance, litigation management</td><td>Banks, telecom, FMCG, technology companies</td></tr>
<tr><td>Public sector</td><td>Prosecution, government legal drafting</td><td>Provincial and federal departments</td></tr>
<tr><td>Court research assistant</td><td>Research and drafting for judges</td><td>High Court and Supreme Court registries</td></tr>
<tr><td>Remote freelance</td><td>Drafting, research, document review</td><td>From home, for foreign clients</td></tr>
</tbody>
</table>
"""},
            {"h2": "How do you find the jobs that are never advertised?",
             "answer": "Visit chambers in person, ask your batchmates and seniors, watch the bar room notice board, and use verified listings rather than waiting for a job post.",
             "html": """
<ul>
<li>A senior or classmate who already knows your work</li>
<li>Chamber visits with a printed CV, which work better than email</li>
<li>Notice boards in the bar room and near the courts</li>
<li>Your law college alumni group</li>
<li>Verified chamber listings on WakeelBano</li>
</ul>
<div class="callout"><b>Red flag:</b> anyone charging a "placement fee" or promising a guaranteed job is almost always a fraud. Reputable chambers do not ask for money.</div>
"""},
            {"h2": "What should a one-page CV contain?",
             "answer": "Name and contact details, a line on your practice interest, verified counts of your drafting and court experience, internships, skills and a sample draft.",
             "html": """
<ul>
<li><b>Header:</b> name, phone, email, city and one line on your area of interest</li>
<li><b>Replace objectives with evidence:</b> "drafted 3 bail applications, 12 legal notices, observed 40+ appearances"</li>
<li><b>Internships:</b> chamber name, court, dates and what you actually did</li>
<li><b>Skills:</b> drafting types, research databases, languages</li>
<li><b>Education and status:</b> LLB, Law-GAT, pupillage stage</li>
<li><b>One sample draft attached</b> — it demonstrates ability faster than any claim</li>
</ul>
"""},
            {"h2": "What should you expect to be paid?",
             "answer": "Expect nothing to Rs 25,000 during pupillage, Rs 25,000 to 50,000 as a junior chamber associate, and more in firms and in-house roles.",
             "html": """
<p>For the full breakdown, see <a href="../../career/lawyer-salary-pakistan/index.html">lawyer salary in Pakistan</a>,
which explains why chambers pay what they pay.</p>
"""},
        ],
        "faqs": [
            ("How do I get my first legal job in Karachi?", "Go in person. Take a one-page CV and a sample draft to chambers near the courts you want to practise in, and ask your seniors for introductions. Referrals fill most openings."),
            ("Do law firms hire fresh graduates?", "Yes, but usually through internships first. A strong internship record and a writing sample matter more than grades alone."),
            ("Are remote legal jobs available in Pakistan?", "Yes. Foreign firms and legal process outsourcers hire Pakistani lawyers for drafting, research and document review, usually paid in dollars. Strong English and a writing sample are essential."),
        ],
        "sources": [
            ("Sindh High Court — cause lists and registries", "https://www.sindhhighcourt.gov.pk/", "official"),
            ("Karachi Bar Association — City Courts", "https://www.karachibarassociation.com/", "association"),
        ],
        "related": [("Lawyer salary in Pakistan", "career/lawyer-salary-pakistan/index.html"),
                    ("Legal jobs in Pakistan", "jobs/index.html"),
                    ("Bar council enrollment", "career/bar-council-enrollment/index.html")],
    },

    {
        "slug": "career/high-court-license/index.html",
        "url": "career/high-court-license/",
        "title": "High Court Licence in Pakistan — Requirements and Process",
        "h1": "High Court Licence (Advocate High Court)",
        "desc": "How to obtain a High Court licence in Pakistan: two years of practice, the application, fitness certificates, documents, and how to maintain a practice record from day one.",
        "kicker": "Career · Licensing",
        "answer": "A High Court licence requires at least two years of practice in the subordinate courts after enrollment, an application through the bar council, the required certificates and clearance by the High Court.",
        "facts": [
            ("Experience required", "Two years in subordinate courts"),
            ("Legal basis", "Section 27, Legal Practitioners and Bar Councils Act, 1973"),
            ("Application route", "Through the provincial bar council to the High Court"),
            ("Key documents", "Practice record, good standing and dues clearance certificates"),
            ("Supreme Court", "Requires seven years as a High Court advocate"),
        ],
        "sections": [
            {"h2": "What are the eligibility requirements?",
             "answer": "You must already be enrolled as an advocate, have practised for at least two years in the subordinate courts, and satisfy the application and fitness requirements of the High Court.",
             "html": """
<ul>
<li>Enrollment on the provincial bar council roll</li>
<li>At least two years of practice before subordinate courts</li>
<li>The prescribed application form and current fees</li>
<li>Fitness and character certificates, plus any interview the court requires</li>
</ul>
<p class="mini">Confirm current requirements and fees with the Sindh High Court and the Sindh Bar Council, because the process is updated from time to time.</p>
"""},
            {"h2": "What is the step-by-step process?",
             "answer": "Assemble your two-year practice record, file the application through the bar council, obtain the certificates, appear for review or interview, then collect the enrolment certificate.",
             "html": """
<ol class="steps">
<li>Build the practice record: case titles, courts, case numbers and your role in each matter</li>
<li>File the prescribed application through the bar council</li>
<li>Obtain good standing, dues clearance and character certificates</li>
<li>Complete the High Court's review or interview process</li>
<li>Receive the certificate of enrolment as an Advocate of the High Court</li>
</ol>
"""},
            {"h2": "How should you keep a practice record?",
             "answer": "Keep a simple register from your first day: date, court, case number, parties, your role and the outcome, with a scanned copy of each order.",
             "html": """
<table class="tbl">
<thead><tr><th>Column</th><th>What to record</th></tr></thead>
<tbody>
<tr><td>Date</td><td>The date of the hearing</td></tr>
<tr><td>Court and case number</td><td>Court name and the case or FIR number</td></tr>
<tr><td>Parties</td><td>The case title, kept private and never published</td></tr>
<tr><td>Your role</td><td>Drafting, research, appearance or assistance</td></tr>
<tr><td>Outcome</td><td>Adjournment, order or arguments heard</td></tr>
<tr><td>Copy</td><td>A scanned order sheet or file note</td></tr>
</tbody>
</table>
"""},
            {"h2": "What is the route to the Supreme Court?",
             "answer": "Seven years of practice as a High Court advocate, plus the prescribed fitness certificate, interviews and fees set by the Pakistan Bar Council.",
             "html": """
<p>The Supreme Court route also requires a list of independently conducted cases and judgments where you appeared as lead counsel.
The exact numbers and fees change, so confirm them with the Pakistan Bar Council before you begin.</p>
"""},
        ],
        "faqs": [
            ("How many years of practice are needed for a High Court licence?", "At least two years before the subordinate courts, under the Legal Practitioners and Bar Councils Act, 1973. Confirm the current requirement with your bar council."),
            ("Can I appear in the High Court without a High Court licence?", "No. Pleadings in the High Court require an Advocate High Court licence; a lower court advocate is limited to the subordinate courts."),
            ("What if I have no practice record?", "Try to reconstruct it from order sheets, court copies and your senior's confirmation. It is far easier to keep the register from day one."),
        ],
        "sources": [
            ("Sindh High Court — enrolment", "https://www.sindhhighcourt.gov.pk/", "official"),
            ("Legal Practitioners and Bar Councils Act, 1973", "http://nasirlawsite.com/laws/baract.htm", "statute"),
        ],
        "related": [("Bar council enrollment", "career/bar-council-enrollment/index.html"),
                    ("Lawyer salary in Pakistan", "career/lawyer-salary-pakistan/index.html"),
                    ("Law-GAT guide", "career/law-gat/index.html")],
    },
    {
        "slug": "drafts/vakalatnama-format/index.html",
        "url": "drafts/vakalatnama-format/",
        "title": "Vakalatnama Format in Pakistan — Clauses, Stamp and Acceptance",
        "h1": "Vakalatnama Format (Pakistan)",
        "desc": "What a vakalatnama must contain in Pakistan: client and advocate details, the scope of authority, acceptance, stamp requirements and the mistakes that get filings returned.",
        "kicker": "Drafts · Filing",
        "answer": "A vakalatnama authorises an advocate to appear, plead and act for a client in a specific case. It must identify the court, the case, the client and the advocate, and it must state the scope of authority.",
        "facts": [
            ("Purpose", "Authorises an advocate to act in a specific case"),
            ("Key clause", "Scope of authority — appear, plead, act, compromise"),
            ("Acceptance", "The advocate's acceptance, where the court requires it"),
            ("Stamp", "Set by the rules of the relevant court"),
        ],
        "sections": [
            {"h2": "What must a vakalatnama contain?",
             "answer": "Court and case details, client identity, advocate details with enrollment number, the scope of authority, acceptance, signature, date and the required stamp.",
             "html": """
<ol class="steps">
<li>The court's name and the case number or title</li>
<li>Client details: name, parentage, CNIC and address</li>
<li>Advocate details: name, enrollment number and chamber address</li>
<li>An authority clause stating exactly what is authorised</li>
<li>The advocate's acceptance, where required</li>
<li>Signatures and date</li>
<li>Stamp or court fee as the court's rules require</li>
<li>Witnesses or attestation, where required</li>
</ol>
"""},
            {"h2": "Why is the scope of authority the most important clause?",
             "answer": "Because “appear, plead and act” does not cover everything. Powers to compromise, withdraw or substitute must be stated explicitly.",
             "html": """
<ul>
<li>Filing an appeal</li>
<li>Leading evidence</li>
<li>Withdrawing the case</li>
<li>Compromising or settling the matter</li>
<li>Substituting another advocate</li>
</ul>
<div class="callout"><b>Practice tip:</b> State each power in plain English. Both the client and the court should read the same meaning from the document.</div>
"""},
            {"h2": "How does it differ by court?",
             "answer": "The format is broadly similar, but stamp requirements, acceptance clauses and the advocate's licence level change between subordinate courts, the High Court, the Supreme Court and tribunals.",
             "html": """
<table class="tbl">
<thead><tr><th>Court</th><th>What changes</th></tr></thead>
<tbody>
<tr><td>District and subordinate courts</td><td>Standard format; stamp per the court's rules</td></tr>
<tr><td>Sindh High Court</td><td>A High Court advocate's enrollment number is required</td></tr>
<tr><td>Supreme Court</td><td>Advocate-on-Record requirements and its own format</td></tr>
<tr><td>Tribunals</td><td>Each tribunal sets its own practice; ask the filing branch first</td></tr>
</tbody>
</table>
"""},
            {"h2": "What are the common mistakes?",
             "answer": "Wrong or missing case numbers, a client name that does not match the CNIC, no enrollment number, a missing acceptance clause and an incomplete address.",
             "html": """
<p>These errors get filings returned and waste a hearing date. An incomplete address is the most damaging, because court notices
and orders never reach the client.</p>
"""},
        ],
        "faqs": [
            ("What is a vakalatnama?", "A document by which a client authorises an advocate to appear, plead and act on their behalf in a particular case. Without it the advocate cannot file or plead the matter."),
            ("How much stamp does a vakalatnama need?", "Stamp and court fee depend on the court and the nature of the case. Confirm the current requirement at the court's filing branch."),
            ("Can two advocates be named on one vakalatnama?", "Practice normally names one advocate, with arrangements for another to assist or substitute. Check the relevant court's rules."),
        ],
        "sources": [
            ("Sindh High Court — filing requirements", "https://www.sindhhighcourt.gov.pk/", "official"),
        ],
        "related": [("Legal notice format", "drafts/legal-notice-format/index.html"),
                    ("Plaint format", "drafts/plaint-format/index.html"),
                    ("High Court licence", "career/high-court-license/index.html")],
    },
    {
        "slug": "case-law/489-f/index.html",
        "url": "case-law/489-f/",
        "title": "489-F PPC Case Law — Cheque Dishonour in Pakistan",
        "h1": "489-F PPC — Cheque Dishonour",
        "desc": "Section 489-F PPC explained: the offence of dishonestly issuing a cheque, the elements to prove, complaint preparation, common defences and how to research the case law.",
        "kicker": "Case law · Criminal",
        "answer": "Section 489-F of the Pakistan Penal Code deals with dishonestly issuing a cheque that is returned unpaid, where the person knew the funds were insufficient. Punishment includes imprisonment and a fine.",
        "facts": [
            ("Statute", "Pakistan Penal Code 1860, section 489-F"),
            ("Core element", "Dishonest intention when the cheque was issued"),
            ("Key documents", "Original cheque, bank return memo, proof of the debt, notice"),
            ("Searched as", "\u201c489-F case law\u201d, \u201ccheque bounce case Pakistan\u201d"),
        ],
        "sections": [
            {"h2": "What must be proved in a 489-F case?",
             "answer": "That the cheque was issued, that it related to a debt or obligation, that it was dishonestly issued, that it was returned unpaid, and that a demand was made.",
             "html": """
<table class="tbl">
<thead><tr><th>Element</th><th>Evidence usually relied on</th></tr></thead>
<tbody>
<tr><td>Issuance</td><td>The original cheque, signature and bank record</td></tr>
<tr><td>Debt or obligation</td><td>Agreement, invoice, receipt, message trail</td></tr>
<tr><td>Dishonest intention</td><td>Knowledge of insufficient funds, account history, conduct</td></tr>
<tr><td>Dishonour</td><td>The bank's return memo, with the reason stated</td></tr>
<tr><td>Demand</td><td>The notice and proof that it reached the other side</td></tr>
</tbody>
</table>
"""},
            {"h2": "What is the pre-complaint checklist?",
             "answer": "Secure the original cheque, obtain the return memo, assemble proof of the underlying debt, send a demand notice and confirm the limitation period and the correct forum.",
             "html": """
<ol class="steps">
<li>The original cheque, plus copies</li>
<li>The bank return memo — the stated reason matters enormously</li>
<li>Proof of the debt: agreement, invoices, ledgers, messages</li>
<li>A legal notice with proof of delivery</li>
<li>The limitation period, checked against the section and current case law</li>
<li>The competent court, determined by territorial jurisdiction</li>
</ol>
"""},
            {"h2": "What defences are commonly raised?",
             "answer": "That the cheque was given as security rather than for a debt, that no debt is proved, that the signature is not the client's, or that the dispute is essentially civil.",
             "html": """
<ul>
<li>The cheque was a <b>security cheque</b>, not payment for a debt</li>
<li>The underlying <b>debt is not proved</b></li>
<li>The <b>signature</b> is disputed</li>
<li>The element of <b>dishonest intention</b> is missing</li>
<li>The <b>demand procedure</b> was not followed</li>
<li>A <b>civil dispute</b> has been given a criminal colour</li>
</ul>
<p class="mini">Research key words: "489-F PPC", "security cheque", "dishonest intention", "quantum of sentence", "compounding".</p>
"""},
            {"h2": "Should the client pursue criminal, civil, or both?",
             "answer": "It depends what the client wants: punishment or recovery. Many matters end in a recorded settlement, and the client should decide the objective before filing.",
             "html": """
<p>Criminal and civil remedies run on different tracks with different outcomes and timelines. Explain both clearly, including
the cost of each, before the client commits.</p>
"""},
        ],
        "faqs": [
            ("What is the punishment under 489-F PPC?", "The section provides imprisonment and a fine. Read the bare Act for the exact wording and check current authority, since sentencing depends on the facts."),
            ("What is a security cheque?", "A cheque handed over as a guarantee rather than to discharge a debt. That distinction affects whether dishonest intention can be established, so research the case law carefully."),
            ("Can a cheque case be settled?", "Yes, frequently. Any settlement should be recorded in writing and given effect through the court's process."),
        ],
        "sources": [
            ("Sindh High Court — case law portal", "https://caselaw.shc.gov.pk/", "official"),
            ("Supreme Court of Pakistan — judgments", "https://www.supremecourt.gov.pk/", "official"),
        ],
        "related": [("Legal notice format", "drafts/legal-notice-format/index.html"),
                    ("302 PPC case law", "case-law/302-ppc/index.html"),
                    ("Case law library", "case-law/index.html")],
    },
    {
        "slug": "case-law/497-crpc/index.html",
        "url": "case-law/497-crpc/",
        "title": "497 CrPC Case Law — Bail in Non-Bailable Offences",
        "h1": "497 CrPC — Bail Case Law",
        "desc": "Section 497 CrPC explained for Pakistani practice: bail in non-bailable offences, the further-inquiry discretion, the grounds courts weigh, and how to research the authorities.",
        "kicker": "Case law · Criminal",
        "answer": "Section 497 CrPC governs bail in non-bailable offences. The court weighs the nature of the offence, the evidence on record, and whether further inquiry is needed before deciding.",
        "facts": [
            ("Bailable offences", "Section 496 CrPC"),
            ("Non-bailable offences", "Section 497 CrPC"),
            ("Higher courts", "Section 498 CrPC"),
            ("Most cited ground", "Further inquiry under the second part of section 497"),
        ],
        "sections": [
            {"h2": "How does the section work in practice?",
             "answer": "It sets a general rule against bail in serious offences, then gives the court discretion where further inquiry is warranted or where the section itself allows it.",
             "html": """
<p>Read the bare Act for the exact text and sub-clauses. Practice varies, so always prefer the binding authority of your own
High Court when you prepare the grounds.</p>
<div class="callout"><b>Remember:</b> bail decides release during trial, not guilt. Keep the application and the arguments on that question.</div>
"""},
            {"h2": "Which issues does the court weigh?",
             "answer": "The nature and gravity of the offence, the strength of the evidence, the stage of investigation, flight risk, parity with co-accused and any specific grounds the section allows.",
             "html": """
<table class="tbl">
<thead><tr><th>Issue</th><th>What to examine</th></tr></thead>
<tbody>
<tr><td>Nature of offence</td><td>Whether it carries death or life imprisonment</td></tr>
<tr><td>Further inquiry</td><td>Whether the record leaves a genuine question to be tried</td></tr>
<tr><td>Investigation</td><td>Challan filed, recovery complete, custody period</td></tr>
<tr><td>Flight risk</td><td>Permanent address, family and community ties</td></tr>
<tr><td>Parity</td><td>A co-accused has been granted bail, with the order cited</td></tr>
<tr><td>Delay</td><td>Delay in trial or prolonged custody</td></tr>
</tbody>
</table>
"""},
            {"h2": "How do you research bail authorities efficiently?",
             "answer": "Search by key words on the court portals, read the operative paragraph rather than the headnote, and confirm each authority has not been reviewed or distinguished.",
             "html": """
<ol class="steps">
<li>Key words: "497 CrPC", "further inquiry", "prohibitory clause", "bail — recovery", "bail — challan".</li>
<li>Start with the Supreme Court, then apply your own High Court's binding authority.</li>
<li>Read the paragraph the court actually relied on, not the summary.</li>
<li>Check the current status: review, larger bench, or later distinguishing cases.</li>
</ol>
"""},
            {"h2": "Where is the drafting guidance?",
             "answer": "The structure of the application and the grounds that work are set out in our bail application format guide.",
             "html": """
<p>See <a href="../../drafts/bail-application-format/index.html">bail application format in Pakistan</a> for the
seven-part structure, the sections involved and the filing mistakes to avoid.</p>
"""},
        ],
        "faqs": [
            ("When is bail granted under section 497 CrPC?", "When the court is satisfied on the facts and the record, commonly where further inquiry is warranted or where the section permits it. Always check the latest binding authority for your facts."),
            ("What does further inquiry mean?", "It refers to the discretion in the second part of section 497, where the record leaves a question that requires determination. Read the exact text of the section."),
            ("Where is a refusal of bail challenged?", "Usually before the Sessions Court or the High Court under section 498 CrPC. Confirm the procedure and limitation for your case type."),
        ],
        "sources": [
            ("Sindh High Court — case law portal", "https://caselaw.shc.gov.pk/", "official"),
            ("Supreme Court of Pakistan — judgments", "https://www.supremecourt.gov.pk/", "official"),
        ],
        "related": [("Bail application format", "drafts/bail-application-format/index.html"),
                    ("302 PPC case law", "case-law/302-ppc/index.html"),
                    ("Case law library", "case-law/index.html")],
    },
    {
        "slug": "drafts/plaint-format/index.html",
        "url": "drafts/plaint-format/",
        "title": "Plaint Format in Pakistan — Order VII CPC Requirements",
        "h1": "Plaint Format (Order VII CPC)",
        "desc": "What a civil plaint must contain in Pakistan under Order VII CPC: parties, cause of action, jurisdiction, valuation, court fee, limitation, prayer and verification.",
        "kicker": "Drafts · Civil",
        "answer": "A plaint is the document that starts a civil suit. Under Order VII CPC it must state the parties, the facts, the cause of action, jurisdiction, valuation, limitation and the relief sought.",
        "facts": [
            ("Governed by", "Code of Civil Procedure 1908, Order VII"),
            ("Must state", "Parties, facts, cause of action, jurisdiction, valuation, limitation, relief"),
            ("Court fee", "Depends on the suit's nature and valuation"),
            ("Government suits", "Usually require prior notice under the CPC"),
        ],
        "sections": [
            {"h2": "What must a plaint contain?",
             "answer": "The court, the parties, the subject matter, dated facts, the cause of action, jurisdiction, valuation and court fee, limitation, the relief, verification and the document list.",
             "html": """
<ul>
<li>The court's name</li>
<li>Plaintiff and defendant details, with addresses</li>
<li>The suit's title and subject matter</li>
<li>The cause of action: when, where and how it arose, with dates</li>
<li>Jurisdiction: territorial and pecuniary, with reasons</li>
<li>Valuation and the court fee paid</li>
<li>The relief claimed, quantified where money is involved</li>
<li>Limitation</li>
<li>Verification and the list of documents</li>
</ul>
"""},
            {"h2": "How should the plaint be structured?",
             "answer": "Follow the court's expected order: heading, parties, subject line, numbered facts, cause of action, jurisdiction and valuation, limitation, prayer, verification and annexures.",
             "html": """
<ol class="steps">
<li><b>Heading:</b> "In the Court of ___" with the suit number</li>
<li><b>Parties:</b> plaintiff versus defendants, with addresses</li>
<li><b>Subject:</b> one line, such as "Suit for recovery of Rs ___"</li>
<li><b>Facts:</b> numbered paragraphs in date order</li>
<li><b>Cause of action:</b> a separate heading</li>
<li><b>Jurisdiction and valuation:</b> a separate paragraph</li>
<li><b>Limitation:</b> a separate paragraph</li>
<li><b>Prayer:</b> numbered reliefs, plus costs</li>
<li><b>Verification, affidavit and documents</b></li>
</ol>
"""},
            {"h2": "Where do valuation and court fee go wrong?",
             "answer": "Under-valuing the suit or paying insufficient court fee leads to objections and delay, so confirm the current schedule at the filing branch.",
             "html": """
<ul>
<li>Court fee paid too low — an objection follows, and the date is lost</li>
<li>Wrong valuation — raises a question over pecuniary jurisdiction</li>
<li>Unquantified relief — creates a problem at the decree stage</li>
</ul>
<p class="mini">Court fee rules are set by statute and revised over time. Confirm the current position with the court, not with an old template.</p>
"""},
            {"h2": "What are the common mistakes?",
             "answer": "Mixing facts with the cause of action, omitting dates, leaving the relief vague, forgetting the document list and skipping the limitation paragraph.",
             "html": """
<p>Each omission becomes the first objection raised against the suit. A plaint that answers all nine requirements in order
survives scrutiny and reaches the merits faster.</p>
"""},
        ],
        "faqs": [
            ("What is the format of a plaint in Pakistan?", "Under Order VII CPC: court, parties, subject matter, numbered facts, cause of action, jurisdiction and valuation, limitation, prayer, verification and a list of documents."),
            ("How much court fee is payable?", "It depends on the nature and valuation of the suit. Confirm the current schedule with the relevant court's filing branch."),
            ("Can a plaint be amended?", "Generally yes, with the court's permission, but the earlier it is done the better. Amendments become harder once trial has progressed."),
        ],
        "sources": [
            ("Sindh High Court — civil practice and rules", "https://www.sindhhighcourt.gov.pk/", "official"),
        ],
        "related": [("Legal notice format", "drafts/legal-notice-format/index.html"),
                    ("Vakalatnama format", "drafts/vakalatnama-format/index.html"),
                    ("Case law library", "case-law/index.html")],
    },
]

# ---------------------------------------------------------------- about / entity page (AI answer target)
ABOUT = {
    "slug": "about/index.html",
    "url": "about/",
    "title": "About WakeelBano — Pakistan's Career Platform for Lawyers",
    "h1": "What is WakeelBano?",
    "desc": "WakeelBano is a Pakistani career platform for lawyers: chamber and mentor matching, a legal job market covering all of Pakistan, paid work, legal research guides and an AI kit for drafting.",
    "kicker": "About",
    "answer": "WakeelBano is a career platform for Pakistani lawyers, built for Karachi first. It helps new lawyers find a chamber and mentor, paid drafting work, legal jobs across Pakistan, and reliable research guidance — all free for junior lawyers.",
    "sections": [
        {"h2": "Who is WakeelBano for?",
         "answer": "Law students, fresh graduates, pupils and junior advocates in Pakistan, plus the chambers, law firms and universities that hire them.",
         "html": """
<ul>
<li><b>Law students</b> who need to know what to do before and after graduation</li>
<li><b>Fresh graduates</b> facing the Law-GAT, pupillage and enrollment process</li>
<li><b>Junior advocates</b> looking for chambers, paid work and better visibility</li>
<li><b>Seniors and firms</b> who need reliable juniors and a verified public profile</li>
<li><b>Law colleges</b> that must place students for mandatory internships</li>
</ul>
"""},
        {"h2": "How does WakeelBano make money?",
         "answer": "From chambers, firms, universities and sponsors — not from junior lawyers, who use the platform free.",
         "html": """
<table class="tbl">
<thead><tr><th>Stream</th><th>Who pays</th><th>Typical price (PKR)</th></tr></thead>
<tbody>
<tr><td>Chamber Pro subscription</td><td>Seniors and chambers</td><td>Rs 2,500 per month</td></tr>
<tr><td>Verified job posting</td><td>Chambers, firms and companies</td><td>Rs 1,500 per posting</td></tr>
<tr><td>Institution plan</td><td>Law colleges and firms</td><td>From Rs 60,000 per year</td></tr>
<tr><td>Workshops</td><td>Participants and sponsors</td><td>Rs 1,500 – 3,000 per seat</td></tr>
<tr><td>Kaam Board commission</td><td>Task posters</td><td>10 – 15% of the task value</td></tr>
</tbody>
</table>
<p class="mini">WakeelBano never charges a junior lawyer for a profile, a listing or a chamber match.</p>
"""},
        {"h2": "What does WakeelBano not do?",
         "answer": "It does not give legal advice, does not take commission on client case referrals, and does not publish or sell lawyer rankings.",
         "html": """
<p>Referral fees for client cases would amount to touting, which is prohibited under professional conduct rules. Any "best lawyer
in Pakistan" ranking would be misleading. We stay on the correct side of both lines: information, tools and verified connections
between lawyers.</p>
"""},
        {"h2": "How is content on this site produced?",
         "answer": "From primary sources — bare Acts, bar council notifications and court publications — with the source named on every page and an explicit verification instruction.",
         "html": """
<p>Our guides explain statutory frameworks and research method. We do not reproduce reported judgments, and we do not invent
citations. Every page carries a date, a scope note and links to the official source you can check yourself.</p>
"""},
        {"h2": "Where is WakeelBano based?",
         "answer": "Karachi, Sindh, with an initial focus on City Courts, the Sindh High Court and the districts around them.",
         "html": """
<p>The pilot starts in Karachi because that is where the largest concentration of new lawyers practises, and where the gap between
a law degree and paid work is widest. Expansion to Hyderabad, Sukkur, Lahore and Islamabad follows once the Karachi network is
verified and working.</p>
"""},
    ],
    "faqs": [
        ("Is WakeelBano a law firm?", "No. It is a technology platform. It does not provide legal advice, does not represent clients and does not act as an agent in any case."),
        ("Is WakeelBano free?", "Yes for students, fresh graduates and junior advocates. Chambers, firms, universities and sponsors pay for listings, subscriptions and workshops."),
        ("Does WakeelBano take a cut of a lawyer's fee?", "No. It never takes a share of a lawyer's professional fee, and never takes commission on client referrals."),
        ("Which cities does it cover?", "Karachi first, with Sindh districts next, then Lahore and Islamabad."),
    ],
    "sources": [
        ("Legal Practitioners and Bar Councils Act, 1973", "http://nasirlawsite.com/laws/baract.htm", "statute"),
        ("Sindh Bar Council", "https://advocates.sindhbarcouncil.org/", "official register"),
        ("Pakistan Bar Council", "https://pakistanbarcouncil.org/", "official"),
    ],
    "related": [("Case law library", "case-law/index.html"),
                ("Career guides", "career/index.html")],
}


# ---------------------------------------------------------------- wave 2
# Extra high-demand pages (drafts, case law, career, Karachi) plus new hub tiles.
from content_pages_more import MORE_PAGES, HUB_ADDITIONS

PAGES.extend(MORE_PAGES)
for _hub in HUBS:
    for _t, _d, _u in HUB_ADDITIONS.get(_hub["slug"], []):
        if all(c[0] != _t for c in _hub["children"]):
            _hub["children"].append((_t, _d, _u))


# ---------------------------------------------------------------- wave 3
# Family law and service/employment guides, with two new hubs.
from content_pages_family_service import PAGES_3, FAMILY_HUB, SERVICE_HUB

HUBS.extend([FAMILY_HUB, SERVICE_HUB])
PAGES.extend(PAGES_3)


# ---------------------------------------------------------------- wave 4
# Pages that explain the platform itself to readers and to AI engines.
from content_pages_resources import PAGES_4

PAGES.extend(PAGES_4)


# ---------------------------------------------------------------- wave 5
# Civil and property litigation hub, plus pre-arrest bail.
from content_pages_civil import PAGES_5, CIVIL_HUB, HUB_ADDITIONS_5

HUBS.append(CIVIL_HUB)
PAGES.extend(PAGES_5)
for _hub in HUBS:
    for _t, _d, _u in HUB_ADDITIONS_5.get(_hub["slug"], []):
        if all(c[0] != _t for c in _hub["children"]):
            _hub["children"].append((_t, _d, _u))
