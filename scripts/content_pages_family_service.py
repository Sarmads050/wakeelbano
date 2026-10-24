# -*- coding: utf-8 -*-
"""Wave 3 content: family law and service/employment guides.

These are the two practice areas where client demand in Pakistan is highest and
published, structured guidance is thinnest. Same rules as the rest of the site:
no invented citations, statute anchors only, typographic quotes inside strings.
"""

FAMILY_HUB = {
    "slug": "family/index.html",
    "url": "family/",
    "title": "Family Law Pakistan — Khula, Maintenance, Custody and Dower",
    "h1": "Family Law in Pakistan",
    "desc": "Plain-language guides to Pakistani family law: khula and divorce, maintenance, child custody, dower and the Family Courts procedure. Written for lawyers and for the client sitting in front of them.",
    "kicker": "Family law library",
    "answer": "Family cases in Pakistan run under the Muslim Family Laws Ordinance 1961, the Family Courts Act 1964 and the Guardians and Wards Act 1890. Almost every family suit begins with a family court and a mandatory pre-trial reconciliation.",
    "children": [
        ("Khula and divorce", "Grounds, procedure, notice to the union council and the 90-day period", "../family/khula-divorce-pakistan/index.html"),
        ("Maintenance", "Wife, children and parents — how quantum is calculated", "../family/maintenance-pakistan/index.html"),
        ("Child custody", "Hizanat, welfare of the child and visitation", "../family/child-custody-pakistan/index.html"),
        ("Dower and dowry", "Haq mehr, prompt and deferred, and recovery", "../family/dower-haq-mehr/index.html"),
    ],
    "sections": [
        {"h2": "Which court hears a family case?",
         "answer": "The family court established under the Family Courts Act 1964, sitting in the district where the parties reside or the cause of action arises.",
         "html": """
<p>Family courts deal with dissolution of marriage, dower, maintenance, restitution of conjugal rights, custody, guardianship, and the return of bridal gifts. A family suit is filed on a prescribed form, not an ordinary plaint, and the court must attempt reconciliation first.</p>
<div class="callout"><b>Practical point:</b> a family suit that is filed as an ordinary civil suit wastes months before it is returned at the scrutiny stage. Check the form and the court fee before you file.</div>
"""},
        {"h2": "How long does a family case take in Karachi?",
         "answer": "A contested khula or maintenance matter often runs from one to three years through the family court and the appeal, while an uncontested one can close in a few months.",
         "html": """
<p>Duration depends on service of notices, reconciliation attempts, evidence and adjournments. The single biggest factor you control is completeness of the file: correct addresses, CNIC copies, nikah nama, and a clear list of documents.</p>
"""},
    ],
    "faqs": [
        ("Can a woman file for khula without the husband's consent?", "Yes. Khula is a dissolution sought by the wife; the court decides it on the wife's statement, and the husband's consent is not a legal condition, though the court considers the return of dower. Confirm the current practice in your court before advising a client."),
        ("Are family cases heard in camera?", "Family courts generally sit in camera and publication of proceedings is restricted. Follow the court's direction in your own matter."),
    ],
    "related": [("Maintenance guide", "../family/maintenance-pakistan/index.html"),
                ("Child custody guide", "../family/child-custody-pakistan/index.html")],
}

SERVICE_HUB = {
    "slug": "service/index.html",
    "url": "service/",
    "title": "Service and Employment Law Pakistan — Labour Court, Termination, Salary",
    "h1": "Service and Employment Law in Pakistan",
    "desc": "Guides to Pakistani employment disputes: which forum hears them, when termination is unlawful, how unpaid salary is recovered, and what a junior lawyer should check before filing.",
    "kicker": "Service law library",
    "answer": "Employment disputes in Pakistan go to the labour court under the provincial industrial relations statutes, to the National Industrial Relations Commission for trans-provincial employers, or to the civil court where the employment is not covered by those laws. The correct forum is the first thing to check.",
    "children": [
        ("Labour court guide", "Which forum, which law, and how to file", "../service/labour-court-pakistan/index.html"),
        ("Wrongful termination", "Domestic inquiry, retrenchment and reinstatement", "../service/wrongful-termination-pakistan/index.html"),
        ("Salary recovery", "Unpaid wages, gratuity, provident fund and the claim route", "../service/salary-recovery-pakistan/index.html"),
    ],
    "sections": [
        {"h2": "Which forum hears an employment dispute?",
         "answer": "It depends on the employer, the province and the industry: labour court, NIRC, or the civil court.",
         "html": """
<table class="tbl">
<thead><tr><th>Employer</th><th>Typical forum</th></tr></thead>
<tbody>
<tr><td>Factory, commercial establishment or industrial undertaking in Sindh</td><td>Labour court under the Sindh Industrial Relations Act 2013</td></tr>
<tr><td>Trans-provincial or federal employer</td><td>National Industrial Relations Commission</td></tr>
<tr><td>Employer outside the industrial relations statutes (for example a small professional office)</td><td>Civil court, on contract and on the Payment of Wages Act 1936 where it applies</td></tr>
</tbody>
</table>
<div class="callout"><b>Check first:</b> whether the worker is covered by the provincial industrial relations law at all. Filing in the wrong forum costs months and a fresh limitation problem.</div>
"""},
    ],
    "faqs": [
        ("Is there a time limit to file an employment claim?", "Yes, and it is short. The provincial statutes set their own limitation periods, often measured in months from the date of the order or termination. Check the statute and the current notification before you tell a client anything."),
        ("Does a worker need a lawyer to file?", "Not legally in every forum, but an uncontested-looking case is often lost on procedure. A junior lawyer can add real value by getting the forum, the documents and the limitation right."),
    ],
    "related": [("Labour court guide", "../service/labour-court-pakistan/index.html"),
                ("Salary recovery", "../service/salary-recovery-pakistan/index.html")],
}

PAGES_3 = [
    # ------------------------------------------------------------------ family
    {
        "slug": "family/khula-divorce-pakistan/index.html",
        "url": "family/khula-divorce-pakistan/",
        "title": "Khula and Divorce in Pakistan — Procedure, Notice and Timeline",
        "h1": "Khula and Divorce in Pakistan",
        "desc": "How khula and divorce work in Pakistan: the family court suit, the union council notice, the 90-day reconciliation period, the return of dower, and the mistakes that delay a decree.",
        "kicker": "Family law",
        "answer": "Khula is a dissolution of marriage sought by the wife in the family court. Divorce by the husband is effected by pronouncing talaq and giving written notice to the union council, which then starts a 90-day reconciliation period before the divorce takes effect.",
        "facts": [
            ("Statutes", "Muslim Family Laws Ordinance 1961; Family Courts Act 1964"),
            ("Khula forum", "Family court, on the prescribed suit form"),
            ("Husband's talaq", "Written notice to the union council concerned"),
            ("Reconciliation period", "90 days under the 1961 Ordinance"),
            ("Dower on khula", "The court considers its return; it is not an automatic condition"),
            ("Usual documents", "Nikah nama, CNIC copies, marriage photographs, notice receipts"),
        ],
        "sections": [
            {"h2": "What is the difference between khula and talaq?",
             "answer": "Khula is initiated by the wife through the court; talaq is pronounced by the husband and becomes effective through the notice procedure.",
             "html": """
<table class="tbl">
<thead><tr><th></th><th>Khula</th><th>Talaq</th></tr></thead>
<tbody>
<tr><td>Who starts it</td><td>The wife, by a suit in the family court</td><td>The husband, by pronouncing talaq</td></tr>
<tr><td>Court involvement</td><td>Required — the court passes the decree</td><td>Not required to pronounce, but notice to the union council is required</td></tr>
<tr><td>Timing</td><td>Ends when the court dissolves the marriage</td><td>Effective after the 90-day period, unless the wife is pregnant</td></tr>
<tr><td>Dower</td><td>The court considers whether it should be returned</td><td>Dower remains payable unless already paid</td></tr>
</tbody>
</table>
"""},
            {"h2": "How does a khula suit actually proceed?",
             "answer": "Suit on the prescribed form, notice to the husband, a reconciliation attempt, the wife's statement, then a decree dissolving the marriage.",
             "html": """
<ol class="steps">
<li>File the suit in the family court with the nikah nama and the correct court fee.</li>
<li>The court issues notices and attempts reconciliation under the Family Courts Act 1964.</li>
<li>The wife's statement is recorded; in khula the court is not bound to the husband's consent.</li>
<li>The court frames the terms — dower, maintenance, custody — and passes a decree.</li>
<li>Send the decree to the union council so the record is updated and the iddat period runs correctly.</li>
</ol>
<div class="callout"><b>Drafting habit:</b> plead the dower position and custody in the same suit. Splitting them into separate cases costs the client money and time.</div>
"""},
            {"h2": "What does the husband's talaq require?",
             "answer": "A written notice to the chairman of the union council, a copy to the wife, and then the statutory 90-day reconciliation period.",
             "html": """
<ul>
<li>The notice must be in writing and delivered to the union council; keep the receipt and a copy.</li>
<li>The union council constitutes a reconciliation council and informs the wife.</li>
<li>The divorce takes effect on expiry of 90 days, or on the birth of a child if the wife is pregnant.</li>
<li>The wife's maintenance during iddat and the dower position should be settled in writing at the same time.</li>
<li>Registration of the divorce with the union council is a separate step — do not confuse it with the notice.</li>
</ul>
"""},
            {"h2": "Which mistakes delay a decree the most?",
             "answer": "Wrong forum, wrong suit form, an incomplete nikah nama, an unserved address, and mixing criminal and family proceedings without a plan.",
             "html": """
<ul>
<li><b>Filing as a civil suit</b> instead of on the family court form.</li>
<li><b>Address problems</b> — service failing because the address is a shop or a relative's house.</li>
<li><b>Dower left blank</b> in the plaint, so it cannot be decided in the same decree.</li>
<li><b>Custody forgotten</b> until after the decree, requiring a second case.</li>
<li><b>Anger in the pleadings</b> — allegations that cannot be proved weaken the case the court must decide.</li>
</ul>
"""},
        ],
        "faqs": [
            ("Can khula be granted against the husband's will?",
             "The court can dissolve the marriage on the wife's suit. The husband's consent is not a legal condition, although the court considers whether the dower should be returned. Follow the practice of your own court."),
            ("How long is iddat and does maintenance continue?",
             "Iddat is normally three menstrual cycles, or until delivery if the wife is pregnant. Maintenance during iddat is a separate entitlement from maintenance pending suit; plead both."),
            ("Does a khula decree end the husband's duty to pay child maintenance?",
             "No. A child's maintenance is the child's right and is decided separately from the marriage. Raise it in the decree rather than leaving it for a later case."),
        ],
        "sources": [
            ("Muslim Family Laws Ordinance 1961", "http://nasirlawsite.com/laws/mflo.htm", "statute"),
            ("Family Courts Act 1964", "http://nasirlawsite.com/laws/fca.htm", "statute"),
        ],
        "related": [
            ("Maintenance in Pakistan", "family/maintenance-pakistan/index.html"),
            ("Child custody", "family/child-custody-pakistan/index.html"),
            ("Dower and haq mehr", "family/dower-haq-mehr/index.html"),
        ],
    },
    {
        "slug": "family/maintenance-pakistan/index.html",
        "url": "family/maintenance-pakistan/",
        "title": "Maintenance in Pakistan — How Courts Fix the Amount",
        "h1": "Maintenance in Pakistan",
        "desc": "Maintenance for a wife, children and parents in Pakistan: what the court considers, how quantum is calculated, interim maintenance, the evidence to produce, and how arrears are enforced.",
        "kicker": "Family law",
        "answer": "A husband must maintain his wife and children, and a person of means must maintain parents who cannot support themselves. Pakistani courts fix the amount on the husband's income and the family's standard of living, and interim maintenance can be ordered while the suit continues.",
        "facts": [
            ("Statutes", "Muslim Family Laws Ordinance 1961, sections 9 and 9-A; Family Courts Act 1964"),
            ("Claimants", "Wife, children, and in some cases parents"),
            ("Key test", "Means of the husband against the needs and standard of living of the family"),
            ("Interim relief", "Available while the suit is pending"),
            ("Evidence", "Salary slips, bank statements, tax returns, property documents, business records"),
            ("Enforcement", "Arrears are recoverable; the court can order payment and, in some cases, attachment"),
        ],
        "sections": [
            {"h2": "How does a court decide the amount?",
             "answer": "It compares the husband's proven means with the family's reasonable needs and their prior standard of living; there is no fixed formula.",
             "html": """
<p>Courts look at income, visible assets, business profits and lifestyle, then compare them with rent, school fees, medical costs and food. A husband cannot reduce maintenance by simply claiming a low salary while his lifestyle shows otherwise.</p>
<table class="tbl">
<thead><tr><th>Factor</th><th>What the court looks at</th></tr></thead>
<tbody>
<tr><td>Income</td><td>Salary slips, bank statements, tax returns, business accounts</td></tr>
<tr><td>Assets and lifestyle</td><td>Property, vehicles, foreign travel, school of the children</td></tr>
<tr><td>Needs</td><td>Rent, utilities, education, medical expenses</td></tr>
<tr><td>Other dependants</td><td>Existing legal obligations of the husband</td></tr>
</tbody>
</table>
"""},
            {"h2": "Can a client get maintenance before the case ends?",
             "answer": "Yes. Interim maintenance can be granted while the suit is pending, and it is often the most useful order in the file.",
             "html": """
<ol class="steps">
<li>Plead interim maintenance in the suit or by a separate application.</li>
<li>Attach evidence of the husband's income — salary certificate, bank statement, tax return, or a business record.</li>
<li>Attach evidence of the family's expenses — rent agreement, school fee vouchers, medical bills.</li>
<li>Ask for the order to run from the date of application and to be paid monthly on a fixed date.</li>
<li>If it is not paid, apply for enforcement immediately rather than waiting for the next date.</li>
</ol>
"""},
            {"h2": "What documents make a maintenance case strong?",
             "answer": "Anything that proves income and anything that proves the family's expenses — both sides of the equation.",
             "html": """
<ul>
<li><b>Income</b> — salary slips, employment letter, bank statements, tax returns, business registration, property documents.</li>
<li><b>Expenses</b> — rent agreement, utility bills, school fee receipts, medical prescriptions and bills.</li>
<li><b>Status</b> — nikah nama, CNIC and B-form for children, and the birth certificate.</li>
<li><b>Conduct</b> — written demands for maintenance and any reply received.</li>
</ul>
<div class="callout"><b>Evidence tip:</b> a screenshot of a salary slip sent on WhatsApp is weak; a bank statement showing the credit is strong. Teach the client the difference before the hearing.</div>
"""},
        ],
        "faqs": [
            ("Does a working wife lose her right to maintenance?", "Not automatically. Her own income is a factor the court weighs, not an automatic bar. Plead and prove the standard of living the family had."),
            ("Can parents claim maintenance from their children?", "Yes. A person with means is obliged to maintain parents who cannot support themselves. The claim is usually brought in the family court."),
            ("What if the husband ignores the maintenance order?", "Apply for enforcement of arrears and ask for the remedies the court provides, which can include attachment of property. Keep a running account of unpaid amounts."),
        ],
        "sources": [
            ("Muslim Family Laws Ordinance 1961 — sections 9 and 9-A", "http://nasirlawsite.com/laws/mflo.htm", "statute"),
            ("Family Courts Act 1964", "http://nasirlawsite.com/laws/fca.htm", "statute"),
        ],
        "related": [
            ("Khula and divorce", "family/khula-divorce-pakistan/index.html"),
            ("Child custody", "family/child-custody-pakistan/index.html"),
            ("Family law library", "family/index.html"),
        ],
    },
    {
        "slug": "family/child-custody-pakistan/index.html",
        "url": "family/child-custody-pakistan/",
        "title": "Child Custody in Pakistan — Hizanat and the Welfare Principle",
        "h1": "Child Custody in Pakistan",
        "desc": "How custody works in Pakistan: hizanat, the welfare-of-the-child principle, ages and guardianship, visitation rights, and the evidence a custody case actually turns on.",
        "kicker": "Family law",
        "answer": "In Pakistan the mother normally has the right of hizanat (physical custody) of young children, while the father remains the natural guardian. Every custody decision is ultimately decided on the welfare of the child, not on the parents' wishes.",
        "facts": [
            ("Statutes", "Guardians and Wards Act 1890; Family Courts Act 1964"),
            ("Mother's hizanat", "Generally until a son is about 7 and a daughter reaches puberty, subject to the court's view of welfare"),
            ("Guardianship", "The father is normally the natural guardian for property and legal acts"),
            ("Deciding test", "Welfare of the minor, above the parents' rights"),
            ("Visitation", "The court fixes times and can enforce them"),
            ("Evidence", "School records, living arrangements, income, conduct, medical and support history"),
        ],
        "sections": [
            {"h2": "What does the welfare principle mean in practice?",
             "answer": "The court asks who can provide stability, schooling, care and a safe home — and it can depart from the usual age rules if the child's welfare requires it.",
             "html": """
<ul>
<li>Continuity of school and neighbourhood.</li>
<li>Who has actually been caring for the child day to day.</li>
<li>Housing, income and the ability to supervise.</li>
<li>Any risk of harm, neglect or exposure to conflict.</li>
<li>The child's own wishes, given weight according to age and understanding.</li>
</ul>
<div class="callout"><b>Common mistake:</b> treating custody as a prize to be won. Courts respond to a plan for the child's routine, not to allegations against the other parent.</div>
"""},
            {"h2": "Can the mother lose custody?",
             "answer": "Yes, if the court finds that the child's welfare requires it — for example where she remarries a person who is a stranger to the child, or cannot provide care, though each case is decided on its own facts.",
             "html": """
<p>Hizanat is a right that yields to welfare. Remarriage, relocation, neglect, or a home where the child cannot be properly supervised are all factors a court will examine. So are the father's conduct and his capacity to care for a young child.</p>
"""},
            {"h2": "How is visitation handled?",
             "answer": "The court fixes specific days and times, and can vary them; a party who obstructs visitation risks an adverse view in the custody decision.",
             "html": """
<ol class="steps">
<li>Ask for defined visitation in the decree, not a general statement of access.</li>
<li>Set out days, times, place of pick-up and return, and overnight arrangements.</li>
<li>Keep a written log of every visit and every missed visit.</li>
<li>If an order is breached, apply to the court promptly with the log.</li>
</ol>
"""},
        ],
        "faqs": [
            ("At what age does a boy go to the father?", "The usual guidance is around seven years for a son, with the court free to decide otherwise on welfare. Always argue welfare, not just the age rule."),
            ("Can a custody order be changed later?", "Yes. A change in circumstances — schooling, remarriage, relocation, the child's own wishes — can justify a fresh application."),
            ("Does custody decide guardianship too?", "No. Physical custody (hizanat) and legal guardianship are separate questions, and the father usually remains the natural guardian."),
        ],
        "sources": [
            ("Guardians and Wards Act 1890", "http://nasirlawsite.com/laws/gwa.htm", "statute"),
            ("Family Courts Act 1964", "http://nasirlawsite.com/laws/fca.htm", "statute"),
        ],
        "related": [
            ("Maintenance in Pakistan", "family/maintenance-pakistan/index.html"),
            ("Khula and divorce", "family/khula-divorce-pakistan/index.html"),
            ("Family law library", "family/index.html"),
        ],
    },
    {
        "slug": "family/dower-haq-mehr/index.html",
        "url": "family/dower-haq-mehr/",
        "title": "Haq Mehr (Dower) in Pakistan — Prompt, Deferred and Recovery",
        "h1": "Haq Mehr (Dower) in Pakistan",
        "desc": "Dower in Pakistani law: prompt and deferred mehr, how it is recorded in the nikah nama, how it is recovered, and how it interacts with khula and the wife's other claims.",
        "kicker": "Family law",
        "answer": "Dower (haq mehr) is a mandatory payment from the husband to the wife under the nikah, either prompt (mu'ajjal) or deferred (mu'ajjal). It is the wife's own property, can be recovered through the family court, and is not cancelled automatically by a khula decree.",
        "facts": [
            ("Nature", "A legal obligation, not a gift or a formality"),
            ("Two kinds", "Prompt mehr, payable on demand; deferred mehr, payable on death or dissolution"),
            ("Where recorded", "The nikah nama, in figures and words"),
            ("Recovery forum", "Family court, usually with the other matrimonial claims"),
            ("Effect of khula", "The court considers whether mehr should be returned; it is not automatically forfeited"),
            ("Interaction", "Independent of maintenance, which is a separate right"),
        ],
        "sections": [
            {"h2": "Prompt or deferred — why the distinction matters",
             "answer": "Prompt mehr can be demanded immediately; deferred mehr becomes payable on the dissolution of the marriage or the husband's death.",
             "html": """
<table class="tbl">
<thead><tr><th></th><th>Prompt (mu'ajjal)</th><th>Deferred (mu'ajjal)</th></tr></thead>
<tbody>
<tr><td>When payable</td><td>On demand, after the nikah</td><td>On dissolution or death</td></tr>
<tr><td>Common practice</td><td>Part of the mehr paid at marriage</td><td>The larger part, recorded in the nikah nama</td></tr>
<tr><td>Risk to the wife</td><td>May be waived if not claimed early</td><td>Recoverable from the estate</td></tr>
</tbody>
</table>
<div class="callout"><b>Drafting point:</b> if the nikah nama records a figure in words and a different figure in digits, expect a dispute. Check both before you file.</div>
"""},
            {"h2": "How is mehr recovered?",
             "answer": "By a suit in the family court, usually pleaded together with maintenance and the dissolution, and proved by the nikah nama and any receipts.",
             "html": """
<ol class="steps">
<li>Read the nikah nama carefully: amount, kind (prompt or deferred), and any conditions.</li>
<li>Plead the mehr claim in the same suit as dissolution or maintenance.</li>
<li>Attach the nikah nama and any evidence of part payment.</li>
<li>Ask for a clear decree amount, not a formula.</li>
<li>Plan enforcement at the time of filing, not after the decree.</li>
</ol>
"""},
            {"h2": "What happens to mehr in a khula?",
             "answer": "The court considers whether the wife should return the mehr as a condition of the dissolution; the classic position is that khula involves a return, but the court has discretion on the facts.",
             "html": """
<p>Do not tell a client that mehr is automatically lost, and do not tell her it is automatically kept. Plead the financial position, the length of the marriage and the reason for the breakdown, and let the court decide the terms. Record the outcome in the decree in figures.</p>
"""},
        ],
        "faqs": [
            ("Can mehr be waived?", "A wife may give up her mehr, but any waiver should be in writing and understood. Courts look closely at waivers signed under pressure."),
            ("Is mehr payable if the marriage was never consummated?", "The position depends on the facts and the kind of mehr. Plead the specific facts; do not generalise."),
            ("Does the widow inherit mehr from the estate?", "Deferred mehr is a debt on the estate and is dealt with alongside the inheritance claim. Handle both together."),
        ],
        "sources": [
            ("Muslim Family Laws Ordinance 1961", "http://nasirlawsite.com/laws/mflo.htm", "statute"),
            ("Family Courts Act 1964", "http://nasirlawsite.com/laws/fca.htm", "statute"),
        ],
        "related": [
            ("Khula and divorce", "family/khula-divorce-pakistan/index.html"),
            ("Maintenance in Pakistan", "family/maintenance-pakistan/index.html"),
            ("Family law library", "family/index.html"),
        ],
    },

    # ----------------------------------------------------------------- service
    {
        "slug": "service/labour-court-pakistan/index.html",
        "url": "service/labour-court-pakistan/",
        "title": "Labour Court in Pakistan — Which Forum and How to File",
        "h1": "Labour Court in Pakistan",
        "desc": "How to choose the right forum for an employment dispute in Pakistan: labour court, NIRC or civil court, the limitation period, the documents needed, and the first three steps to take.",
        "kicker": "Service law",
        "answer": "A labour dispute in Pakistan goes to the labour court under the provincial industrial relations law, to the National Industrial Relations Commission where the employer is trans-provincial or federal, or to the civil court where the employment is outside those statutes. Filing in the wrong forum is the most common fatal error.",
        "facts": [
            ("Sindh statute", "Sindh Industrial Relations Act 2013"),
            ("Federal / trans-provincial", "Industrial Relations Act 2012 and the NIRC"),
            ("Wage claims", "Payment of Wages Act 1936, where applicable"),
            ("Limitation", "Short and statute-specific — often months, not years"),
            ("First documents", "Appointment letter, salary slips, termination letter, correspondence"),
            ("Typical reliefs", "Reinstatement, back benefits, wages, compensation"),
        ],
        "sections": [
            {"h2": "Which forum applies to your client's employer?",
             "answer": "Provincial labour court for a local industrial or commercial establishment, NIRC for a trans-provincial employer, civil court where the statutes do not apply.",
             "html": """
<ol class="steps">
<li>Identify the employer's legal entity and where it operates.</li>
<li>Check whether the establishment is covered by the provincial industrial relations statute.</li>
<li>Check the worker's category — some categories are excluded from particular protections.</li>
<li>Confirm the limitation period in the statute that applies.</li>
<li>Only then draft the claim; the forum decides the form, the reliefs and the appeal route.</li>
</ol>
<div class="callout"><b>Verification rule:</b> the provincial statutes are amended by notification. Read the current text and the latest Sindh notification before you rely on a limitation period.</div>
"""},
            {"h2": "What documents should the file contain?",
             "answer": "Proof of employment, proof of wages, proof of the adverse order, and proof of any demand made before filing.",
             "html": """
<table class="tbl">
<thead><tr><th>Document</th><th>What it proves</th></tr></thead>
<tbody>
<tr><td>Appointment letter or contract</td><td>Employment, designation, salary, notice period</td></tr>
<tr><td>Salary slips and bank credits</td><td>Wages actually paid, and arrears</td></tr>
<tr><td>Termination letter or order</td><td>The date and the stated reason — key for limitation</td></tr>
<tr><td>Show-cause notice and reply</td><td>Whether a domestic inquiry happened at all</td></tr>
<tr><td>Written demand / notice</td><td>That the employer had a chance to settle</td></tr>
<tr><td>Attendance or duty records</td><td>Length of continuous service</td></tr>
</tbody>
</table>
"""},
            {"h2": "What are the first three steps after a termination?",
             "answer": "Secure the documents, fix the date and the limitation, and send a written demand so the record is clear.",
             "html": """
<ul>
<li><b>Secure</b> — collect every document and message before access is cut off.</li>
<li><b>Date</b> — note the exact date of the termination order and of any internal appeal.</li>
<li><b>Demand</b> — send a written demand for dues and reinstatement, and keep proof of dispatch.</li>
</ul>
<p>After that, file in the correct forum within limitation. Delay is the second most common reason good cases fail.</p>
"""},
        ],
        "faqs": [
            ("How long does a labour case take?", "Months to a few years depending on the forum, the evidence and adjournments. A complete file at the start shortens it more than anything else."),
            ("Can a worker claim without a written contract?", "Yes — employment can be proved by salary slips, bank credits, attendance records, identity cards and witnesses. Start collecting that evidence immediately."),
            ("Is there a fee to file?", "Court fees and professional costs vary by forum. Explain the cost to the client in writing before filing."),
        ],
        "sources": [
            ("Sindh Industrial Relations Act 2013 — Sindh government", "https://sindh.gov.pk/", "provincial authority"),
            ("National Industrial Relations Commission", "https://nirc.gov.pk/", "tribunal"),
            ("Payment of Wages Act 1936", "http://nasirlawsite.com/laws/pwa.htm", "statute"),
        ],
        "related": [
            ("Wrongful termination", "service/wrongful-termination-pakistan/index.html"),
            ("Salary recovery", "service/salary-recovery-pakistan/index.html"),
            ("Service law library", "service/index.html"),
        ],
    },
    {
        "slug": "service/wrongful-termination-pakistan/index.html",
        "url": "service/wrongful-termination-pakistan/",
        "title": "Wrongful Termination in Pakistan — Inquiry, Grounds and Relief",
        "h1": "Wrongful Termination in Pakistan",
        "desc": "What makes a termination unlawful in Pakistan: the domestic inquiry, show-cause notice, retrenchment rules, the reliefs a court can give, and the arguments that actually work.",
        "kicker": "Service law",
        "answer": "A termination is usually challenged on three grounds: there was no valid reason, there was no domestic inquiry or show-cause notice, or the retrenchment and notice rules were not followed. If the court agrees, the usual reliefs are reinstatement with back benefits, or compensation where reinstatement is not practical.",
        "facts": [
            ("Statutes", "Provincial industrial relations laws; federal law for trans-provincial employers"),
            ("Key procedural step", "Show-cause notice and a fair domestic inquiry before punishment"),
            ("Common defect", "Termination ordered without any inquiry record"),
            ("Typical reliefs", "Reinstatement, back benefits, wages, compensation"),
            ("Limitation", "Short — check the applicable statute before anything else"),
            ("Evidence to gather", "Charge sheet, inquiry report, termination order, service record"),
        ],
        "sections": [
            {"h2": "What must an employer prove?",
             "answer": "A valid reason, a fair opportunity to answer the allegation, and compliance with the procedure in the standing orders or the statute.",
             "html": """
<ol class="steps">
<li><b>Reason</b> — misconduct, inefficiency or redundancy, stated in writing.</li>
<li><b>Notice</b> — a show-cause notice with the specific allegation and the evidence.</li>
<li><b>Opportunity</b> — a reply, and a domestic inquiry where the rules require one.</li>
<li><b>Proportion</b> — the punishment must match the misconduct.</li>
<li><b>Procedure</b> — notice, dues and the statutory formalities for retrenchment.</li>
</ol>
<div class="callout"><b>Where cases are won:</b> in the inquiry record. Ask for the original inquiry file in the first hearing — its absence is often the whole case.</div>
"""},
            {"h2": "What arguments work for the worker?",
             "answer": "No inquiry, no notice, a punishment that does not fit the allegation, victimisation for union or complaint activity, and dues withheld after termination.",
             "html": """
<ul>
<li><b>No inquiry</b> — a termination letter with no prior proceedings.</li>
<li><b>No specific allegation</b> — a vague charge that could not be answered.</li>
<li><b>Disproportionate punishment</b> — dismissal for a minor first offence.</li>
<li><b>Victimisation</b> — timing that follows a complaint, a union role or a wage demand.</li>
<li><b>Withheld dues</b> — salary, gratuity and provident fund, which are separate claims.</li>
</ul>
"""},
            {"h2": "What relief can a court give?",
             "answer": "Reinstatement with back benefits, or compensation instead of reinstatement, plus the unpaid dues the evidence supports.",
             "html": """
<p>Reinstatement is the classic relief, but courts also award compensation where the relationship has broken down or the employer no longer exists in the same form. Plead both: reinstatement as the primary relief and compensation in the alternative, and quantify the dues with a calculation sheet.</p>
"""},
        ],
        "faqs": [
            ("Does resigning end the claim?", "A resignation signed under pressure, or obtained without explaining the consequences, can be challenged. Gather evidence of the circumstances and file promptly."),
            ("Can an employee be terminated without notice?", "Only where the statute or the contract permits it, for example in a proven case of serious misconduct after a proper inquiry. Otherwise notice or pay in lieu is required."),
            ("Is a domestic inquiry always necessary?", "It depends on the applicable standing orders and statute, but its absence is the most common defect courts examine. Always check the inquiry record first."),
        ],
        "sources": [
            ("Sindh Industrial Relations Act 2013 — Sindh government", "https://sindh.gov.pk/", "provincial authority"),
            ("National Industrial Relations Commission", "https://nirc.gov.pk/", "tribunal"),
        ],
        "related": [
            ("Labour court guide", "service/labour-court-pakistan/index.html"),
            ("Salary recovery", "service/salary-recovery-pakistan/index.html"),
            ("Service law library", "service/index.html"),
        ],
    },
    {
        "slug": "service/salary-recovery-pakistan/index.html",
        "url": "service/salary-recovery-pakistan/",
        "title": "Salary Recovery in Pakistan — Unpaid Wages, Gratuity and Benefits",
        "h1": "Salary Recovery in Pakistan",
        "desc": "How to recover unpaid salary in Pakistan: the claim route under the Payment of Wages Act and the labour court, gratuity and provident fund, provident fund records, and the evidence that proves arrears.",
        "kicker": "Service law",
        "answer": "Unpaid wages are recovered by a claim in the labour court or under the Payment of Wages Act where it applies, supported by salary slips, bank credits and attendance records. Gratuity, provident fund and other statutory dues are usually claimed in the same proceedings.",
        "facts": [
            ("Statutes", "Payment of Wages Act 1936; provincial industrial relations laws; Employees' Old-Age Benefits Act"),
            ("Forum", "Labour court, or the authority under the Payment of Wages Act"),
            ("Proof of arrears", "Salary slips, bank statements, attendance records, employer's ledger"),
            ("Other dues", "Gratuity, provident fund, leave encashment, notice pay"),
            ("Limitation", "Short — check the statute immediately"),
            ("Best evidence", "A bank statement showing the monthly credit, then a gap"),
        ],
        "sections": [
            {"h2": "How do you prove arrears?",
             "answer": "By showing what was payable and what was not paid: the agreed salary, the period worked, and the absence of credit in the bank.",
             "html": """
<table class="tbl">
<thead><tr><th>Claim</th><th>Evidence</th></tr></thead>
<tbody>
<tr><td>Unpaid salary</td><td>Salary slips, bank statements, appointment letter, attendance</td></tr>
<tr><td>Overtime</td><td>Attendance or duty rosters, wage rate</td></tr>
<tr><td>Gratuity</td><td>Length of continuous service, last drawn wage</td></tr>
<tr><td>Provident fund</td><td>Fund statements, deductions shown in salary slips</td></tr>
<tr><td>Notice pay</td><td>Contract, termination letter, date of departure</td></tr>
</tbody>
</table>
<div class="callout"><b>Preparation tip:</b> build a one-page calculation sheet — month, amount due, amount paid, shortfall. Courts and employers both settle faster when the arithmetic is on one page.</div>
"""},
            {"h2": "What should a lawyer do in the first week?",
             "answer": "Freeze the evidence, calculate the claim, and send a written demand to the employer.",
             "html": """
<ol class="steps">
<li>Collect every salary slip, bank statement and message before the client's access is cut off.</li>
<li>Prepare the calculation sheet and get the client to sign it.</li>
<li>Send a written demand with a deadline, by a mode that gives proof of delivery.</li>
<li>Confirm the forum and the limitation period.</li>
<li>File, and claim interest or compensation where the statute allows it.</li>
</ol>
"""},
            {"h2": "What if the employer says the worker abandoned the job?",
             "answer": "The burden shifts to the record: attendance, leave applications, messages and witnesses decide whether the worker left or was pushed out.",
             "html": """
<ul>
<li>Attendance registers and gate records.</li>
<li>Leave applications and approvals.</li>
<li>Messages showing the employer's instructions up to the last day.</li>
<li>Witnesses who saw the worker on site after the alleged abandonment.</li>
</ul>
"""},
        ],
        "faqs": [
            ("Can salary be recovered after the company closes?", "Recovery becomes harder but is not impossible — the entity's status, its assets and the liability of office-bearers matter. Act quickly."),
            ("Is gratuity payable to every employee?", "Entitlement depends on the applicable statute, the length of service and the employer's coverage. Check the specific law for that establishment."),
            ("Do I need a lawyer for a small claim?", "Not always, but a well-drafted demand and a correct calculation often produce a settlement without litigation — and that is usually the fastest money for the client."),
        ],
        "sources": [
            ("Payment of Wages Act 1936", "http://nasirlawsite.com/laws/pwa.htm", "statute"),
            ("Employees' Old-Age Benefits Institution", "https://www.eobi.gov.pk/", "statutory body"),
            ("Sindh government — labour department", "https://sindh.gov.pk/", "provincial authority"),
        ],
        "related": [
            ("Labour court guide", "service/labour-court-pakistan/index.html"),
            ("Wrongful termination", "service/wrongful-termination-pakistan/index.html"),
            ("Legal notice format", "drafts/legal-notice-format/index.html"),
        ],
    },
]
