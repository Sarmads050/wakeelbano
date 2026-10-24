# -*- coding: utf-8 -*-
"""Wave 5: civil and property litigation guides, plus pre-arrest bail.

Property and civil suits carry the highest fees in Pakistani practice, and the four
documents that decide most of them (specific performance, injunction, execution,
partition) are the ones juniors are asked to draft first.
"""

CIVIL_HUB = {
    "slug": "civil/index.html",
    "url": "civil/",
    "title": "Civil and Property Litigation in Pakistan — The Four Core Suits",
    "h1": "Civil and Property Litigation in Pakistan",
    "desc": "The four suits that carry most civil practice in Pakistan: specific performance of an agreement to sell, injunction and stay orders, execution of a decree, and partition of joint property. Procedure, documents and drafting.",
    "kicker": "Civil litigation library",
    "answer": "Most civil litigation in Pakistan turns on four suits: specific performance to force a sale that was agreed but not completed, an injunction to stop the other side acting while the suit runs, execution to actually recover what a decree gave you, and partition to divide jointly owned property. Each has its own limitation, court fee and document bundle.",
    "children": [
        ("Specific performance", "Specific Relief Act 1877 — forcing the sale that was agreed", "../civil/specific-performance/index.html"),
        ("Injunction and stay orders", "Order XXXIX CPC — the three tests a court applies", "../civil/order-39-injunction/index.html"),
        ("Execution of a decree", "Order XXI CPC — how a decree actually becomes money", "../civil/order-21-execution/index.html"),
        ("Partition of joint property", "Co-owned property, shares and the preliminary decree", "../civil/partition-suit/index.html"),
    ],
    "sections": [
        {"h2": "What decides which of these suits you file?",
         "answer": "What the client actually wants: the property, the money, protection while the case runs, or a clean division.",
         "html": """
<table class="tbl">
<thead><tr><th>What the client wants</th><th>The suit</th><th>Limitation to check first</th></tr></thead>
<tbody>
<tr><td>The property they agreed to buy</td><td>Specific performance</td><td>Runs from the date fixed for performance</td></tr>
<tr><td>The other side stopped from acting</td><td>Injunction / stay order</td><td>With the main suit; delay is fatal to the relief</td></tr>
<tr><td>To actually get the money or possession a decree gave</td><td>Execution</td><td>Runs from the date of the decree</td></tr>
<tr><td>A defined share instead of joint ownership</td><td>Partition</td><td>When the plaintiff is denied his share</td></tr>
</tbody>
</table>
<div class="callout"><b>Limitation is where these cases are lost.</b> Before drafting anything, open the Limitation Act 1908 and fix the date the clock started. Then decide the court fee, because a suit undervalued will be returned at scrutiny.</div>
"""},
        {"h2": "What documents should the file contain before you draft?",
         "answer": "The document that proves the right, proof of payment, the notice, and a current certificate of title or revenue record.",
         "html": """
<ul>
<li><b>The agreement or title document</b> — sale agreement, sale deed, allotment letter, lease, or the revenue record.</li>
<li><b>Proof of payment</b> — receipts, bank transfers, cheques, and the seller's written acknowledgement.</li>
<li><b>The notice</b> — the demand made, and proof it was delivered.</li>
<li><b>Title and encumbrance</b> — current fard, registry extract, and any prior litigation on the property.</li>
<li><b>Correspondence</b> — messages and letters showing what each side agreed and refused.</li>
</ul>
"""},
    ],
    "faqs": [
        ("Do property suits always go to the civil court?", "Usually the civil court of the district where the property is situated, but revenue matters, rent matters and family property disputes can go elsewhere. Check jurisdiction and forum first."),
        ("How long does a civil suit take in Karachi?", "A contested property suit commonly runs several years through the trial court and the first appeal. Complete documents and a clean valuation shorten it more than anything else."),
    ],
    "related": [("Case law library", "../case-law/index.html"),
                ("Draft library", "../drafts/index.html")],
}

PAGES_5 = [
    {
        "slug": "civil/specific-performance/index.html",
        "url": "civil/specific-performance/",
        "title": "Specific Performance in Pakistan — Forcing the Sale That Was Agreed",
        "h1": "Specific Performance in Pakistan",
        "desc": "How specific performance works in Pakistan under the Specific Relief Act 1877: ready and willing, limitation, the notice, court fee, defences that succeed, and the drafting checklist.",
        "kicker": "Civil litigation",
        "answer": "Specific performance asks the court to force the seller to transfer property that was agreed to be sold. The buyer must prove a valid agreement, that he was ready and willing to perform, that he did perform or tendered performance, and that he asked for the transfer within limitation.",
        "facts": [
            ("Statute", "Specific Relief Act 1877, section 12"),
            ("Plaintiff must prove", "Agreement, readiness and willingness, tender of price, and limitation"),
            ("Limitation", "Runs from the date fixed for performance; check the Limitation Act 1908 before drafting"),
            ("Court fee", "Ad valorem on the value of the property — check the provincial Court Fees Act"),
            ("Most common defence", "The buyer was never ready and willing, or the suit is time-barred"),
            ("Alternative relief", "Damages or refund, pleaded in the same suit"),
        ],
        "sections": [
            {"h2": "What must the buyer prove?",
             "answer": "Four things: a concluded agreement, readiness and willingness, actual tender or an excuse for not tendering, and that the suit is within time.",
             "html": """
<ol class="steps">
<li><b>Agreement</b> — written and signed, identifying the property precisely, with the price and the date fixed for performance.</li>
<li><b>Readiness and willingness</b> — money available, no legal bar on the buyer, and conduct consistent with wanting to complete.</li>
<li><b>Tender</b> — offer of the balance price to the seller, or proof of why no tender was possible.</li>
<li><b>Notice</b> — a written demand giving the seller a final opportunity before filing.</li>
<li><b>Limitation</b> — the date the clock started, calculated and pleaded in the plaint itself.</li>
</ol>
<div class="callout"><b>The evidence that decides these cases:</b> bank statements or a sale of other assets showing the buyer had the money. A buyer who cannot show funds on the date of performance loses, even with a perfectly drafted agreement.</div>
"""},
            {"h2": "Which defences actually succeed?",
             "answer": "Readiness and willingness, limitation, a defective or incomplete agreement, a third-party purchaser without notice, and the seller's own incapacity to transfer.",
             "html": """
<table class="tbl">
<thead><tr><th>Defence</th><th>What the defendant must show</th></tr></thead>
<tbody>
<tr><td>Not ready and willing</td><td>The buyer had no funds and never tendered the balance</td></tr>
<tr><td>Time-barred</td><td>The date fixed for performance is older than the limitation period</td></tr>
<tr><td>No concluded agreement</td><td>Essential terms were still being negotiated</td></tr>
<tr><td>Third-party rights</td><td>A bona fide purchaser bought the property before the suit and without notice</td></tr>
<tr><td>Impossibility</td><td>The property was already lawfully transferred or is no longer the seller's</td></tr>
</tbody>
</table>
<p>Courts treat the remedy as discretionary, so even a good claim can be refused where damages are the fairer outcome.</p>
"""},
            {"h2": "What is the drafting checklist?",
             "answer": "Identify the property exactly, plead the agreement and its performance dates, plead readiness and willingness, attach the documents, and quantify the court fee.",
             "html": """
<ul>
<li><b>Property description</b> — plot number, area, scheme, survey number and boundaries, matching the revenue record.</li>
<li><b>Agreement details</b> — date, price, payment schedule, date of performance, possession.</li>
<li><b>Performance pleaded</b> — what was paid, what was tendered, when, and how.</li>
<li><b>Readiness and willingness</b> — a specific paragraph with the evidence of funds.</li>
<li><b>Notice</b> — date, mode and proof of service.</li>
<li><b>Relief</b> — specific performance, or in the alternative refund with damages, plus costs and any injunction.</li>
<li><b>Court fee</b> — correct ad valorem valuation, or the suit is returned at scrutiny.</li>
</ul>
"""},
        ],
        "faqs": [
            ("Is specific performance a right or a discretion?", "It is a discretionary remedy. The court can refuse it and award damages or refund instead, which is why the alternative relief must always be pleaded."),
            ("Can it be claimed over agricultural land?", "Depends on the transaction, the revenue record and any statutory restriction on transfer. Check the provincial law on agricultural land before drafting."),
            ("What if the seller has already sold to someone else?", "The buyer's remedy may shift to damages, and the third party's status as a bona fide purchaser without notice becomes the central question. Act fast and consider an injunction."),
        ],
        "sources": [
            ("Specific Relief Act 1877", "http://nasirlawsite.com/laws/sra.htm", "statute"),
            ("Limitation Act 1908", "http://nasirlawsite.com/laws/lim.htm", "statute"),
            ("Code of Civil Procedure 1908", "http://nasirlawsite.com/laws/cpc.htm", "statute"),
        ],
        "related": [
            ("Injunction and stay orders", "civil/order-39-injunction/index.html"),
            ("Plaint format", "drafts/plaint-format/index.html"),
            ("Civil litigation library", "civil/index.html"),
        ],
    },
    {
        "slug": "civil/order-39-injunction/index.html",
        "url": "civil/order-39-injunction/",
        "title": "Injunction in Pakistan — Order XXXIX CPC, Stay Orders and the Three Tests",
        "h1": "Injunction and Stay Orders (Order XXXIX CPC)",
        "desc": "How injunctions work in Pakistan: the three tests under Order XXXIX CPC, temporary and permanent injunction, status quo orders, and the drafting that gets a stay granted.",
        "kicker": "Civil litigation",
        "answer": "A court grants a temporary injunction under Order XXXIX CPC when the plaintiff shows a prima facie case, irreparable loss that cannot be compensated in money, and that the balance of convenience favours protecting the property or the position until the suit is decided.",
        "facts": [
            ("Statute", "Code of Civil Procedure 1908, Order XXXIX rules 1 and 2"),
            ("Three tests", "Prima facie case, irreparable loss, balance of convenience"),
            ("Types", "Temporary (during the suit) and permanent (in the decree)"),
            ("Speed matters", "Delay in applying is itself an argument against the relief"),
            ("Practical form", "Status quo orders are the most common relief granted"),
            ("Cost", "Court fee on the application, plus an ad interim order that can be appealed"),
        ],
        "sections": [
            {"h2": "What are the three tests a court applies?",
             "answer": "Prima facie case, irreparable injury, and the balance of convenience — all three, not just one.",
             "html": """
<table class="tbl">
<thead><tr><th>Test</th><th>What it means in practice</th></tr></thead>
<tbody>
<tr><td><b>Prima facie case</b></td><td>The documents show a real question to try — not a certain win, but more than a suspicion</td></tr>
<tr><td><b>Irreparable injury</b></td><td>Harm that money cannot fix, such as construction, demolition, or transfer to a third party</td></tr>
<tr><td><b>Balance of convenience</b></td><td>Who suffers more if the court gets it wrong — usually settled by maintaining the existing position</td></tr>
</tbody>
</table>
<div class="callout"><b>The most common outcome in Pakistan</b> is a status quo order: nobody changes the position on the ground until the suit is decided. Ask for it in clear words in the application.</div>
"""},
            {"h2": "How is the application drafted?",
             "answer": "Facts, the right relied on, the three tests with documents, the urgency, and a prayer that says exactly what must not happen.",
             "html": """
<ol class="steps">
<li><b>Title and application number</b> — in the pending suit, under Order XXXIX rules 1 and 2.</li>
<li><b>Facts</b> — dated and short, with the documents that prove the right.</li>
<li><b>Prima facie case</b> — a separate paragraph, referring to specific annexures.</li>
<li><b>Irreparable loss</b> — say what will be lost and why money is not enough.</li>
<li><b>Balance of convenience</b> — show that the other side loses nothing by waiting, and you lose everything.</li>
<li><b>Conduct and delay</b> — explain any gap between the cause of action and the application.</li>
<li><b>Prayer</b> — "restrain the defendant from … selling / constructing / alienating / dispossessing" and status quo.</li>
<li><b>Affidavit and annexures</b> — a supporting affidavit, properly attested.</li>
</ol>
"""},
            {"h2": "Why are injunction applications refused?",
             "answer": "Delay, no clear right, disputed questions of fact that need trial, and a prayer that is too vague to enforce.",
             "html": """
<ul>
<li><b>Delay</b> — a plaintiff who waits six months has answered the urgency question himself.</li>
<li><b>No demonstrable right</b> — the documents do not show title, possession or a concluded agreement.</li>
<li><b>Money is enough</b> — where compensation can fix the loss, an injunction usually will not.</li>
<li><b>Vague prayer</b> — an order the defendant cannot understand is an order the court will not pass.</li>
<li><b>Concealment</b> — an application that hides an earlier suit or an earlier transfer is dismissed with costs.</li>
</ul>
"""},
        ],
        "faqs": [
            ("What is the difference between a temporary and a permanent injunction?", "A temporary injunction under Order XXXIX protects the position while the suit is pending. A permanent injunction is granted in the decree itself after trial, and is the final relief."),
            ("Can an injunction order be appealed?", "An order granting or refusing a temporary injunction is appealable under Order XLIII CPC. Check the appeal route and limitation immediately if the order goes against your client."),
            ("What if the other side disobeys the order?", "Apply for contempt and for attachment under Order XXXIX rule 2-A. Keep a dated record of the breach, with photographs and witnesses."),
        ],
        "sources": [
            ("Code of Civil Procedure 1908 — Order XXXIX", "http://nasirlawsite.com/laws/cpc.htm", "statute"),
            ("Specific Relief Act 1877 — injunctions", "http://nasirlawsite.com/laws/sra.htm", "statute"),
        ],
        "related": [
            ("Specific performance", "civil/specific-performance/index.html"),
            ("Affidavit format", "drafts/affidavit-format/index.html"),
            ("Civil litigation library", "civil/index.html"),
        ],
    },
    {
        "slug": "civil/order-21-execution/index.html",
        "url": "civil/order-21-execution/",
        "title": "Execution of a Decree in Pakistan — Order XXI CPC",
        "h1": "Execution of a Decree (Order XXI CPC)",
        "desc": "A decree is not money. How execution works in Pakistan: the execution petition, limitation, attachment of property, objections, and why so many decrees never get enforced.",
        "kicker": "Civil litigation",
        "answer": "Execution is the process of enforcing a decree that has already been passed. The decree-holder files an execution petition under Order XXI CPC, applies for attachment and sale of the judgment-debtor's property or for delivery of possession, and does it within the limitation period that runs from the decree.",
        "facts": [
            ("Statute", "Code of Civil Procedure 1908, Order XXI"),
            ("Who files", "The decree-holder, in the court that passed the decree or the court that can execute it"),
            ("Limitation", "Runs from the date of the decree — check the Limitation Act 1908 immediately"),
            ("Main remedies", "Attachment and sale of property, delivery of possession, arrest in some cases"),
            ("Common obstacle", "Objections to attachment, and property already transferred to a third party"),
            ("Best practice", "Start execution early; a decree-holder who waits loses assets to other creditors"),
        ],
        "sections": [
            {"h2": "How does an execution petition work?",
             "answer": "Identify the decree and what remains unpaid, list the judgment-debtor's assets, and ask for the specific mode of execution.",
             "html": """
<ol class="steps">
<li><b>Decree details</b> — suit number, date of decree, and the exact amount or relief still unexecuted.</li>
<li><b>Calculation</b> — principal, costs and any interest the decree allows, on one page.</li>
<li><b>Assets</b> — property, bank accounts, vehicles or business interests, with evidence such as a fard or registration record.</li>
<li><b>Mode of execution</b> — attachment and sale, delivery of possession, or both.</li>
<li><b>Notice</b> — the court issues notice to the judgment-debtor, who may object.</li>
<li><b>Follow through</b> — sale proclamation, auction, and confirmation before the money reaches your client.</li>
</ol>
<div class="callout"><b>Where decrees die:</b> the decree-holder does not identify any asset. An execution petition that names no property is a piece of paper. Do the asset work before you file.</div>
"""},
            {"h2": "What objections can the judgment-debtor raise?",
             "answer": "That the decree is satisfied, that the property is exempt or belongs to a third party, or that the execution is barred by limitation.",
             "html": """
<table class="tbl">
<thead><tr><th>Objection</th><th>How the decree-holder answers it</th></tr></thead>
<tbody>
<tr><td>Decree already satisfied</td><td>Demand the receipts; check the court record for any deposit</td></tr>
<tr><td>Property belongs to a third party</td><td>Trace the title and the timing of any transfer after the suit began</td></tr>
<tr><td>Property is exempt</td><td>Check the exemption list in the CPC; some property cannot be attached</td></tr>
<tr><td>Execution time-barred</td><td>Show the date of the decree and any earlier execution application that kept it alive</td></tr>
</tbody>
</table>
"""},
            {"h2": "What should a lawyer tell the client before filing suit?",
             "answer": "A decree is only worth what can be recovered. Identify assets at the start, and consider attachment before judgment.",
             "html": """
<ul>
<li><b>Realistic advice</b> — a decree against a person with no assets is not a win.</li>
<li><b>Attachment before judgment</b> — under Order XXXVIII CPC, where the defendant may dispose of property to defeat a decree.</li>
<li><b>Cost-benefit</b> — execution fees, publication costs and auction expenses add up.</li>
<li><b>Timing</b> — every month of delay is another chance for the debtor to transfer the property.</li>
</ul>
"""},
        ],
        "faqs": [
            ("Can a decree be executed in another city?", "Yes. A decree can be transferred for execution to the court that has jurisdiction over the judgment-debtor's property or person. Apply for transfer and follow the record."),
            ("What is attachment before judgment?", "An order under Order XXXVIII CPC preventing a defendant from disposing of property so that a future decree can be satisfied. It requires evidence that the defendant intends to obstruct execution."),
            ("Does interest keep running?", "Only as the decree provides. Read the decree carefully and calculate exactly what it allows before you claim a figure."),
        ],
        "sources": [
            ("Code of Civil Procedure 1908 — Order XXI and XXXVIII", "http://nasirlawsite.com/laws/cpc.htm", "statute"),
            ("Limitation Act 1908", "http://nasirlawsite.com/laws/lim.htm", "statute"),
        ],
        "related": [
            ("Specific performance", "civil/specific-performance/index.html"),
            ("Injunction and stay orders", "civil/order-39-injunction/index.html"),
            ("Civil litigation library", "civil/index.html"),
        ],
    },
    {
        "slug": "civil/partition-suit/index.html",
        "url": "civil/partition-suit/",
        "title": "Partition Suit in Pakistan — Dividing Joint Property",
        "h1": "Partition of Joint Property in Pakistan",
        "desc": "How a partition suit works in Pakistan: co-owners, undivided shares, the preliminary and final decree, the revenue record, and why most family property disputes start here.",
        "kicker": "Civil litigation",
        "answer": "A partition suit asks the court to divide jointly owned property according to each owner's share. The court first passes a preliminary decree declaring the shares, then appoints a commission to divide the property by metes and bounds, and finally passes a final decree.",
        "facts": [
            ("Statute", "Code of Civil Procedure 1908, Order XX rule 18; substantive right under the relevant personal law"),
            ("Who can sue", "Any co-owner who is denied his share"),
            ("First step", "A preliminary decree that fixes each party's share"),
            ("Second step", "A commission to divide the property, or sale where division is not possible"),
            ("Key document", "The revenue record (fard) and the title deed"),
            ("Practical point", "Partition is a right; a co-owner cannot be forced to stay in joint ownership"),
        ],
        "sections": [
            {"h2": "How does a partition suit proceed?",
             "answer": "Shares are fixed first, then the property is divided by a commission, and the final decree puts each owner in possession of his portion.",
             "html": """
<ol class="steps">
<li><b>Plead the shares</b> — how the property came to be jointly owned, and the exact share of each party.</li>
<li><b>Attach the record</b> — fard, sale deeds, inheritance documents and any earlier family settlement.</li>
<li><b>Preliminary decree</b> — the court declares the shares of all co-owners.</li>
<li><b>Commission</b> — a local commissioner examines whether physical division is possible.</li>
<li><b>Division or sale</b> — if division is possible, the property is divided; if not, it may be sold and proceeds shared.</li>
<li><b>Final decree and possession</b> — each owner gets possession of his portion, with a mutation where needed.</li>
</ol>
<div class="callout"><b>Time saver:</b> a clear fard and an agreed family tree at the start can cut a year out of a partition suit. Most delay comes from disputes about who the heirs are, not about the property.</div>
"""},
            {"h2": "What documents decide a partition case?",
             "answer": "The revenue record, the title documents, the family tree, and any previous settlement or mutation.",
             "html": """
<ul>
<li><b>Fard / record of rights</b> — current entries, and the history of mutations.</li>
<li><b>Title deeds</b> — sale deeds, allotment letters, or inheritance mutations.</li>
<li><b>Family tree</b> — with CNIC numbers, agreed if possible, since it fixes the shares.</li>
<li><b>Prior settlements</b> — any written family arrangement, and whether it was acted upon.</li>
<li><b>Possession evidence</b> — who has been in occupation, and of which portion.</li>
</ul>
"""},
            {"h2": "Can one co-owner sell his share without asking the others?",
             "answer": "A co-owner can generally transfer his own undivided share, but the purchaser steps into his shoes as a co-owner — which is why partition suits often follow such a sale.",
             "html": """
<p>The buyer acquires the seller's share, with all its disputes. That is why prudent buyers insist on a partition or a written family settlement before paying. Where a co-owner has sold without disclosing the joint ownership, the other co-owners may have separate claims, including for the specific portion they occupied.</p>
"""},
        ],
        "faqs": [
            ("Is a court fee payable on a partition suit?", "Court fee rules differ by province and by whether the plaintiff is in possession of his share. Check the provincial Court Fees Act and the value fixed in the plaint."),
            ("Can partition be refused?", "Partition is generally a right of a co-owner, but the court may refuse division where it would destroy the value of the property, and order a sale instead."),
            ("What if the property cannot be physically divided?", "The court can order a sale and distribution of the proceeds, or allot a portion to one co-owner with compensation to the others."),
        ],
        "sources": [
            ("Code of Civil Procedure 1908 — Order XX rule 18", "http://nasirlawsite.com/laws/cpc.htm", "statute"),
            ("Limitation Act 1908", "http://nasirlawsite.com/laws/lim.htm", "statute"),
        ],
        "related": [
            ("Specific performance", "civil/specific-performance/index.html"),
            ("Plaint format", "drafts/plaint-format/index.html"),
            ("Civil litigation library", "civil/index.html"),
        ],
    },
    {
        "slug": "case-law/498-crpc/index.html",
        "url": "case-law/498-crpc/",
        "title": "498 CrPC — Pre-Arrest Bail in Pakistan, Step by Step",
        "h1": "498 CrPC — Pre-Arrest Bail",
        "desc": "How pre-arrest bail works in Pakistan: the exceptional nature of the relief, the grounds, the documents, what to file before the High Court, and the mistakes that get it refused.",
        "kicker": "Case law · Criminal",
        "answer": "Pre-arrest bail under section 498 CrPC is an exceptional remedy. The applicant must show that the case is mala fide, that he has been implicated to harass him, or that there are exceptional circumstances — and courts treat it as a last resort, not as a routine step after an FIR.",
        "facts": [
            ("Statute", "Criminal Procedure Code 1898, section 498"),
            ("Nature", "Exceptional and discretionary — not a matter of right"),
            ("Grounds", "Mala fide, ulterior motive, no reasonable likelihood of arrest, or exceptional circumstances"),
            ("Forum", "Sessions court or High Court, depending on the case and stage"),
            ("Key documents", "FIR, applicant's account, and material showing the motive"),
            ("Risk", "An application that fails can smooth the way for arrest"),
        ],
        "sections": [
            {"h2": "When does pre-arrest bail actually succeed?",
             "answer": "When the applicant shows the case itself is an abuse of process, or that the facts do not fit the offence alleged at all.",
             "html": """
<ul>
<li><b>Mala fide</b> — the FIR follows a property dispute, a family dispute or a refusal to pay, and the criminal case is pressure.</li>
<li><b>No connection to the offence</b> — the applicant is named but the material shows he was elsewhere or had no role.</li>
<li><b>Delay and conduct</b> — the applicant appears before the court voluntarily and has not absconded.</li>
<li><b>Exceptional circumstances</b> — age, health, or a purely civil dispute dressed as a crime.</li>
</ul>
<div class="callout"><b>Honest advice to the client:</b> pre-arrest bail is not a routine step. If the facts genuinely attract the offence, an unsuccessful application weakens the later regular bail application.</div>
"""},
            {"h2": "What should the file contain?",
             "answer": "The FIR, the applicant's own account, the documents behind the dispute, and anything that shows when and why the complaint appeared.",
             "html": """
<ol class="steps">
<li>Certified copy of the FIR, with the date and the police station.</li>
<li>The applicant's account, in an affidavit, dated and specific.</li>
<li>The underlying documents — the sale agreement, the cheque, the family dispute, the prior civil suit.</li>
<li>Evidence of the motive — messages, prior complaints, the timeline of the dispute.</li>
<li>Any order already passed in related proceedings.</li>
<li>A short chronology, because these applications are decided on the story the documents tell.</li>
</ol>
"""},
            {"h2": "What are the procedural steps?",
             "answer": "File before the appropriate court, serve notice, argue interim protection, and expect conditions on any relief granted.",
             "html": """
<ul>
<li><b>Forum</b> — sessions court or High Court, depending on the offence and where the case is pending.</li>
<li><b>Interim protection</b> — ask for protection until the next date, or the purpose of the application is defeated.</li>
<li><b>Conditions</b> — courts usually impose conditions such as joining the investigation and not leaving the jurisdiction.</li>
<li><b>Duration</b> — relief is normally time-bound, and the applicant must then seek regular bail.</li>
<li><b>Compliance</b> — a breach of any condition is itself a reason to cancel the relief.</li>
</ul>
"""},
        ],
        "faqs": [
            ("Is pre-arrest bail a right?", "No. It is an exceptional discretionary relief, granted where the process of law is being misused. Regular bail after arrest is a different application with different tests."),
            ("Can it be filed directly in the High Court?", "It can, but practice varies with the case and the stage. Follow the route used in your own court and check the current rules before filing."),
            ("What happens if the application is dismissed?", "The applicant loses the protection of the court and the arrest may follow. That is why the documents — not the drafting — decide whether to file at all."),
        ],
        "sources": [
            ("Criminal Procedure Code 1898 — sections 496 to 498", "http://nasirlawsite.com/laws/crpc.htm", "statute"),
            ("Supreme Court of Pakistan — reported judgments", "https://www.supremecourt.gov.pk/", "court website"),
        ],
        "related": [
            ("497 CrPC — bail case law", "case-law/497-crpc/index.html"),
            ("Bail application format", "drafts/bail-application-format/index.html"),
            ("Case law library", "case-law/index.html"),
        ],
    },
]

HUB_ADDITIONS_5 = {
    "case-law/index.html": [
        ("498 CrPC — pre-arrest bail", "Exceptional relief: grounds, documents and the risks", "../case-law/498-crpc/index.html"),
    ],
}
