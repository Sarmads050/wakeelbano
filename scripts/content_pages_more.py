# -*- coding: utf-8 -*-
"""Wave 2 content for WakeelBano: high-demand drafts, case law and career pages.

Kept in a separate module so the main content file stays readable. Imported by
content_pages.py and merged into PAGES / hub children.

Rules: no invented citations, no reproduced judgments, statute anchors only,
typographic quotes inside strings.
"""

MORE_PAGES = [
    # ------------------------------------------------------------ case law
    {
        "slug": "case-law/420-ppc/index.html",
        "url": "case-law/420-ppc/",
        "title": "420 PPC Case Law Pakistan — Cheating and Dishonest Inducement",
        "h1": "420 PPC Case Law — Cheating and Dishonest Inducement",
        "desc": "Section 420 PPC explained: what the prosecution must prove, the punishment, how it differs from 406 and 489-F, and where to find reported judgments in Pakistan.",
        "kicker": "Case law · Criminal",
        "answer": "Section 420 PPC punishes cheating that dishonestly induces the victim to deliver property. The prosecution must prove a false representation, dishonest intention at the time of the promise, and delivery of property as a result. Punishment is up to seven years and fine.",
        "facts": [
            ("Statute", "Pakistan Penal Code 1860, section 420"),
            ("Offence", "Cheating and thereby dishonestly inducing delivery of property"),
            ("Punishment", "Imprisonment up to 7 years and fine"),
            ("Nature", "Cognizable, non-bailable, compoundable with the court's permission"),
            ("Key proof point", "Dishonest intention existing at the time the promise was made"),
            ("Most common defence", "The transaction was a civil dispute dressed as a criminal case"),
        ],
        "sections": [
            {"h2": "What must the prosecution prove under section 420 PPC?",
             "answer": "Four elements: a deception, a dishonest or fraudulent intention at that moment, delivery of property as a consequence, and the resulting loss.",
             "html": """
<ol class="steps">
<li><b>Deception</b> — a false or misleading representation, express or implied, made knowingly.</li>
<li><b>Inducement</b> — the complainant relied on it and handed over money or property.</li>
<li><b>Dishonest intention at the time</b> — the intent existed when the promise was made, not afterwards.</li>
<li><b>Damage or loss</b> — the property was delivered and the complainant suffered.</li>
</ol>
<div class="callout"><b>The decisive question</b> in almost every 420 case is the fourth element in reverse: was there a dishonest intention when the money was taken, or did a commercial deal simply fail later? Courts read the whole conduct — the agreement, the payments, the correspondence — not just one broken promise.</div>
"""},
            {"h2": "How is section 420 different from 406 PPC and 489-F PPC?",
             "answer": "420 is about being tricked into parting with property, 406 is about betraying trust after property is handed over, and 489-F is about a cheque that bounces.",
             "html": """
<table class="tbl">
<thead><tr><th>Section</th><th>Core idea</th><th>Typical facts</th></tr></thead>
<tbody>
<tr><td><b>420 PPC</b></td><td>Deception before delivery</td><td>A buyer induces payment by showing a forged allotment letter</td></tr>
<tr><td><b>406 PPC</b></td><td>Entrustment, then dishonest misappropriation</td><td>A partner keeps money collected on behalf of the firm</td></tr>
<tr><td><b>489-F PPC</b></td><td>A dishonoured cheque given to discharge an obligation</td><td>A cheque returned unpaid for insufficient funds</td></tr>
</tbody>
</table>
<p>Charges are sometimes added together, but each needs its own evidence. Adding 406 to a 420 FIR does not save a weak deception case.</p>
"""},
            {"h2": "Which reported judgments should you actually read?",
             "answer": "Read the leading Supreme Court judgments on dishonest intention and on the criminal-versus-civil divide, then read two from your own High Court on your facts.",
             "html": """
<p>Do not rely on a citation you have not opened. Work in this order:</p>
<ul>
<li>Search <b>PLD, SCMR and CLD</b> for the phrase <i>dishonest intention at the inception</i> — that is the language judgments actually use.</li>
<li>Add your subject matter to the search: <i>420 PPC</i> plus <i>agreement to sell</i>, <i>construction contract</i> or <i>investment</i>. Facts decide these cases.</li>
<li>Prefer a <b>two-judge or three-judge Supreme Court decision</b> over a single-judge High Court note when you need a principle.</li>
<li>Check that the judgment has not been overruled — read the later cases that cite it.</li>
</ul>
<div class="callout"><b>Verification rule:</b> every citation you put in a bail application, complaint or written argument must be traced to the report itself, with page number. AI tools invent citations; the discipline is yours.</div>
"""},
            {"h2": "How do defence counsel usually attack a 420 case?",
             "answer": "By showing the dispute is civil, that the intention was honest at the time, that accounts were maintained, or that the complainant was a business party who took a commercial risk.",
             "html": """
<ul>
<li><b>The transaction was commercial</b> — a loan, a partnership or a sale that later failed.</li>
<li><b>No deception</b> — every document was genuine and the complainant knew the position.</li>
<li><b>Intention was honest</b> — part payments, continued dealings and messages showing good faith.</li>
<li><b>Accounts exist</b> — the money is traceable and the dispute is about calculation.</li>
<li><b>Delay and motive</b> — the complaint was filed after pressure, negotiation or a counter-dispute.</li>
</ul>
"""},
            {"h2": "What is the practical research method for a 420 file?",
             "answer": "Build a chronology first, then a document bundle, then search authority on the exact fact pattern you have.",
             "html": """
<ol class="steps">
<li>Chronology: every date, payment, message and document on one page.</li>
<li>Identify the single representation you say was false, and quote the document that contains it.</li>
<li>List the evidence proving intention at that date — not later conduct alone.</li>
<li>Search case law on the same subject matter, not on 420 in general.</li>
<li>Confirm limitation, forum and the FIR or complaint route with your senior before filing.</li>
</ol>
"""},
        ],
        "faqs": [
            ("Is 420 PPC bailable?", "It is generally treated as non-bailable, but bail is a matter of judicial discretion and depends on the facts. Always check the current schedule of the Criminal Procedure Code and the practice of your court rather than assuming."),
            ("Can a 420 case be settled between the parties?", "Compounding is possible only with the permission of the court, and it does not erase the record automatically. Take your senior's advice before any compromise."),
            ("Can the same transaction give rise to a civil suit and a criminal case?", "Yes in principle, but courts are alert to criminal complaints used purely to pressure a civil debtor. The test remains dishonest intention at the inception."),
            ("Where can a lawyer in Karachi read 420 judgments free?", "PLD, SCMR and CLD volumes in a chamber or bar library, and the official Supreme Court and Sindh High Court websites for recent reported judgments. Always verify the copy you use."),
        ],
        "sources": [
            ("Pakistan Penal Code 1860 — section 420 text", "http://nasirlawsite.com/laws/ppc.htm", "statute"),
            ("Supreme Court of Pakistan — reported judgments", "https://www.supremecourt.gov.pk/", "court website"),
            ("Sindh High Court — judgments", "https://sindhhighcourt.gov.pk/", "court website"),
        ],
        "related": [
            ("406 PPC — criminal breach of trust", "case-law/406-ppc/index.html"),
            ("489-F PPC — cheque dishonour", "case-law/489-f/index.html"),
            ("Legal notice format", "drafts/legal-notice-format/index.html"),
        ],
    },
    {
        "slug": "case-law/406-ppc/index.html",
        "url": "case-law/406-ppc/",
        "title": "406 PPC Case Law Pakistan — Criminal Breach of Trust",
        "h1": "406 PPC Case Law — Criminal Breach of Trust",
        "desc": "Section 406 PPC explained: entrustment, dishonest misappropriation, punishment up to three years, how it differs from 420 and 489-F, and how to research the offence.",
        "kicker": "Case law · Criminal",
        "answer": "Section 406 PPC punishes criminal breach of trust: property is handed over in trust, and the person entrusted then dishonestly misappropriates, converts or disposes of it. Punishment is up to three years, or fine, or both.",
        "facts": [
            ("Statute", "Pakistan Penal Code 1860, section 406"),
            ("Offence", "Criminal breach of trust"),
            ("Punishment", "Up to 3 years imprisonment, or fine, or both"),
            ("First element", "Entrustment — the property must be handed over with confidence"),
            ("Second element", "Dishonest misappropriation, conversion or disposal"),
            ("Common example", "Money collected on behalf of a firm, committee or family and not accounted for"),
        ],
        "sections": [
            {"h2": "What are the two elements of section 406?",
             "answer": "Entrustment and dishonest misappropriation. Remove either one and the offence collapses into a civil claim.",
             "html": """
<table class="tbl">
<thead><tr><th>Element</th><th>What proof is needed</th></tr></thead>
<tbody>
<tr><td><b>Entrustment</b></td><td>Delivery of property with confidence for a purpose — a receipt, an agreement, a bank trail, a written acknowledgement</td></tr>
<tr><td><b>Dishonest misappropriation</b></td><td>Use or disposal inconsistent with the purpose: denial of receipt, false accounts, sale of entrusted goods, refusal to return with dishonest intent</td></tr>
</tbody>
</table>
<div class="callout"><b>Note the direction of the offence.</b> In 420 the victim is tricked before handing over property; in 406 the property is handed over honestly and betrayed afterwards.</div>
"""},
            {"h2": "Why is 406 so often dismissed as a civil dispute?",
             "answer": "Because a failure to pay back is not automatically a crime. Courts look for dishonest intention, not only a broken promise to return money.",
             "html": """
<ul>
<li>A loan not repaid is a civil debt, unless dishonest intention is shown.</li>
<li>Disputes about accounts, profit shares and calculations belong in a civil court.</li>
<li>Written acknowledgements and admissions change the picture materially — keep them.</li>
<li>Where the money is traceable and part of it was returned, the dishonest-intent argument weakens.</li>
</ul>
"""},
            {"h2": "How should you research a 406 matter?",
             "answer": "Search on the entrustment document and the mode of misappropriation, not on the section number alone.",
             "html": """
<ol class="steps">
<li>Isolate the document that proves entrustment. Without it, rethink the case.</li>
<li>Set out precisely what was misappropriated and when the purpose was departed from.</li>
<li>Search judgments using the words of the offence: <i>entrustment</i>, <i>misappropriation</i>, <i>criminal breach of trust</i>, combined with your subject such as <i>partnership</i> or <i>employment</i>.</li>
<li>Read any authority that treats a similar fact pattern as civil, and address it in your own arguments.</li>
</ol>
"""},
        ],
        "faqs": [
            ("Is 406 compoundable?", "Compounding is allowed only with the permission of the court. Ask your senior and check the current schedule before advising anyone."),
            ("What is the punishment under section 406 PPC?", "Up to three years imprisonment, or fine, or both, for the general offence. Sections 407 to 409 deal with aggravated cases involving higher punishment."),
            ("Can an employer file a 406 case against an employee over salary advances?", "It depends on evidence of entrustment and dishonest intent. Salary advances and disputed dues are usually civil matters unless there is clear evidence of misappropriation."),
        ],
        "sources": [
            ("Pakistan Penal Code 1860 — sections 405 to 409", "http://nasirlawsite.com/laws/ppc.htm", "statute"),
            ("Supreme Court of Pakistan — reported judgments", "https://www.supremecourt.gov.pk/", "court website"),
        ],
        "related": [
            ("420 PPC — cheating", "case-law/420-ppc/index.html"),
            ("497 CrPC — bail", "case-law/497-crpc/index.html"),
            ("Written statement format", "drafts/written-statement-format/index.html"),
        ],
    },
    {
        "slug": "case-law/506-ppc/index.html",
        "url": "case-law/506-ppc/",
        "title": "506 PPC Case Law Pakistan — Criminal Intimidation",
        "h1": "506 PPC Case Law — Criminal Intimidation",
        "desc": "Section 506 PPC explained: what counts as a criminal threat, the two punishment levels, how threats are proved, and how to research criminal intimidation cases in Pakistan.",
        "kicker": "Case law · Criminal",
        "answer": "Section 506 PPC punishes criminal intimidation: threatening injury to a person, their reputation or their property to cause alarm or to force an act. Punishment is up to two years or fine, rising to seven years where the threat is of death or grievous injury.",
        "facts": [
            ("Statute", "Pakistan Penal Code 1860, section 506"),
            ("Offence", "Criminal intimidation"),
            ("Basic punishment", "Up to 2 years imprisonment, or fine, or both"),
            ("Aggravated punishment", "Up to 7 years and fine where death or grievous hurt is threatened"),
            ("Usual proof", "Screenshots, call recordings, witnesses, written communication"),
            ("Common defence", "The words were a general expression of anger, not a threat"),
        ],
        "sections": [
            {"h2": "What makes something a criminal threat?",
             "answer": "Three ingredients: a threat of injury, made with intent to cause alarm or to pressurise the person, and communication of that threat to the person concerned.",
             "html": """
<ul>
<li><b>Threat of injury</b> to body, reputation or property — including a threat to expose or defame.</li>
<li><b>Intention</b> — to cause alarm, or to compel an act or omission.</li>
<li><b>Communication</b> — the person threatened must learn of it; a message that never reaches anyone is not intimidation.</li>
</ul>
<p>Words spoken in anger with no target, intent or follow-through are usually not enough. Context decides.</p>
"""},
            {"h2": "Which punishment applies?",
             "answer": "Two years in the ordinary case, seven years where the threat is of death or grievous injury.",
             "html": """
<table class="tbl">
<thead><tr><th>Threat</th><th>Punishment</th></tr></thead>
<tbody>
<tr><td>Any injury to person, reputation or property</td><td>Up to 2 years, or fine, or both</td></tr>
<tr><td>Death, or grievous injury, or destruction of property by fire</td><td>Up to 7 years and fine</td></tr>
</tbody>
</table>
"""},
            {"h2": "How is a threat proved in practice?",
             "answer": "By preserving the communication properly, and by showing the effect it had on the complainant.",
             "html": """
<ol class="steps">
<li>Preserve the original device and the raw file — a screenshot alone invites challenge.</li>
<li>Note the date, time, number and identity of the sender.</li>
<li>Record the complainant's reaction: did they change behaviour, pay the money demanded, move house?</li>
<li>Find a witness who was told about the threat at the time.</li>
<li>Do not edit, annotate or forward a compromised copy to the court; produce the original.</li>
</ol>
<div class="callout"><b>Practice point:</b> threats connected to extortion, land grabbing or demand for money often carry other charges as well. Read the whole FIR before deciding the defence.</div>
"""},
        ],
        "faqs": [
            ("Is 506 bailable?", "Ordinarily 506 is considered bailable, but the aggravated form can change the position. Confirm against the current Criminal Procedure Code schedule."),
            ("Can I file a private complaint for a threat?", "Yes. A complaint can be filed before the competent magistrate, along with a police complaint. Follow the path your senior advises given the evidence."),
            ("Are WhatsApp messages enough as evidence?", "They can be, if the original device is produced and the identity of the sender is established. Electronic evidence needs careful handling under the Qanun-e-Shahadat 1984."),
        ],
        "sources": [
            ("Pakistan Penal Code 1860 — sections 503 to 506", "http://nasirlawsite.com/laws/ppc.htm", "statute"),
            ("Sindh High Court — judgments", "https://sindhhighcourt.gov.pk/", "court website"),
        ],
        "related": [
            ("420 PPC — cheating", "case-law/420-ppc/index.html"),
            ("Bail application format", "drafts/bail-application-format/index.html"),
            ("Legal notice format", "drafts/legal-notice-format/index.html"),
        ],
    },

    # ------------------------------------------------------------ drafts
    {
        "slug": "drafts/written-statement-format/index.html",
        "url": "drafts/written-statement-format/",
        "title": "Written Statement Format Pakistan — Order VIII CPC",
        "h1": "Written Statement Format (Pakistan)",
        "desc": "How to draft a written statement under Order VIII CPC in Pakistan: the paragraphs defendants forget, the admission-and-denial discipline, set-off and counter-claim, and filing mistakes.",
        "kicker": "Draft library",
        "answer": "A written statement is the defendant's reply to a plaint. It must deal with every allegation paragraph by paragraph, raise the legal objections first, and add a set-off or counter-claim only where the facts justify one. Order VIII CPC governs it.",
        "facts": [
            ("Governing law", "Code of Civil Procedure 1908, Order VIII"),
            ("Who files it", "The defendant, after service of summons and the plaint"),
            ("Time", "Within the period fixed by the court on service — often 30 days"),
            ("Shape", "Paragraph-by-paragraph reply matching the plaint, plus separate grounds"),
            ("Failure to file", "The court may proceed ex parte or decide on the record"),
            ("Verification", "Required, with signature of the defendant and the advocate"),
        ],
        "sections": [
            {"h2": "What must a written statement contain?",
             "answer": "Preliminary objections, the reply to each plaint paragraph, fresh facts relied on, any set-off or counter-claim, and a verification.",
             "html": """
<ol class="steps">
<li><b>Heading and title</b> — court, case number, parties, and the title Written Statement.</li>
<li><b>Preliminary objections</b> — jurisdiction, limitation, maintainability, cause of action, valuation, non-joinder of parties.</li>
<li><b>Reply on merits</b> — numbered to match the plaint, not the defendant's story.</li>
<li><b>Additional facts</b> — facts the defendant will prove, each in its own paragraph.</li>
<li><b>Set-off or counter-claim</b> — only if a separate, quantified claim exists.</li>
<li><b>Verification</b> — that the contents are true to the defendant's belief, with the signature and place and date of signing.</li>
</ol>
"""},
            {"h2": "Why do courts reject so many written statements?",
             "answer": "Usually because allegations are answered vaguely instead of being admitted or denied, and because the reply does not follow the plaint paragraph by paragraph.",
             "html": """
<div class="callout"><b>The rule to remember:</b> silence is not a denial. An allegation that is not specifically denied or expressly admitted is likely to be taken as admitted. Every paragraph needs one of three answers — admitted, denied, or not admitted for want of knowledge.</div>
<ul>
<li>Do not write a general denial of the entire plaint.</li>
<li>Do not answer with a legal argument where a fact was alleged.</li>
<li>Do not raise a set-off without a figure and a basis.</li>
<li>Do not leave preliminary objections buried in the middle of the merits.</li>
</ul>
"""},
            {"h2": "What is the difference between a set-off and a counter-claim?",
             "answer": "A set-off defends with a reciprocal debt; a counter-claim makes a claim of its own, and needs court fees and separate relief.",
             "html": """
<table class="tbl">
<thead><tr><th>Feature</th><th>Set-off (Order VIII rule 6)</th><th>Counter-claim (Order VIII rule 6-A)</th></tr></thead>
<tbody>
<tr><td>Purpose</td><td>Extinguish or reduce the plaintiff's claim</td><td>Obtain relief against the plaintiff</td></tr>
<tr><td>Effect</td><td>Defence only</td><td>Treated as a separate suit</td></tr>
<tr><td>Court fee</td><td>Generally not on the set-off</td><td>Required, like a plaint</td></tr>
<tr><td>Risk</td><td>Lost if not pleaded</td><td>Lost if not pleaded in the reply, though the court has power to allow later</td></tr>
</tbody>
</table>
"""},
            {"h2": "What are the most common drafting mistakes?",
             "answer": "Mismatched paragraph numbering, missing verification, no date or place, inconsistent facts against the earlier reply, and unsigned annexures.",
             "html": """
<ul>
<li>Paragraph numbers that do not correspond with the plaint — the court cannot follow the reply.</li>
<li>Verification that does not state what is admitted and what is denied.</li>
<li>Facts pleaded without any witness or document to prove them.</li>
<li>Raising limitation in the merits instead of in the preliminary objections.</li>
<li>Copying a format from another case, leaving another party's name or facts inside.</li>
</ul>
"""},
        ],
        "faqs": [
            ("What happens if the written statement is not filed in time?",
             "The court may decide the suit without it, or may allow filing subject to costs and conditions. Time limits are applied strictly in commercial cases; always check the order passed in your specific matter."),
            ("Can a written statement be amended later?",
             "Yes, the court may allow amendment under Order VI rule 17, but not to change the case completely or where it is barred by limitation. Amendment is discretionary."),
            ("Does a counter-claim need separate court fees?",
             "Yes. A counter-claim is treated as a plaint for the purposes of the Civil Courts Ordinance 1962 and the Court Fees Act, and relief in it is independent of the defence."),
        ],
        "sources": [
            ("Code of Civil Procedure 1908 — Order VIII", "http://nasirlawsite.com/laws/cpc.htm", "statute"),
            ("Sindh High Court — judgments on civil pleadings", "https://sindhhighcourt.gov.pk/", "court website"),
        ],
        "related": [
            ("Plaint format", "drafts/plaint-format/index.html"),
            ("Affidavit format", "drafts/affidavit-format/index.html"),
            ("Vakalatnama format", "drafts/vakalatnama-format/index.html"),
        ],
    },
    {
        "slug": "drafts/affidavit-format/index.html",
        "url": "drafts/affidavit-format/",
        "title": "Affidavit Format Pakistan — Court and General Affidavits",
        "h1": "Affidavit Format (Pakistan)",
        "desc": "How to prepare an affidavit in Pakistan: the deponent, statement of truth, jurat, attestation before a notary and the mistakes that make an affidavit worthless.",
        "kicker": "Draft library",
        "answer": "An affidavit is a written statement of facts that the deponent swears or affirms to be true before an authorised officer. It must identify the deponent, state facts in numbered paragraphs, show the place and date of swearing, and carry the jurat and the attestation.",
        "facts": [
            ("Statutes", "Oaths Act 1873; Code of Civil Procedure 1908, Order XIX"),
            ("Who can attest", "Notary public, oath commissioner, or a court officer empowered to administer oaths"),
            ("Contents", "Facts only, in the deponent's own knowledge unless stated on belief"),
            ("Numbering", "Paragraph-wise, complete sentences, no argument or opinion"),
            ("Annexures", "Documents exhibited and referred to in the body"),
            ("Consequence", "A false affidavit exposes the deponent to proceedings for perjury"),
        ],
        "sections": [
            {"h2": "What is the structure of a valid affidavit?",
             "answer": "Title, description of the deponent, numbered facts, annexures, jurat, and the attestation block.",
             "html": """
<ol class="steps">
<li><b>Title</b> — court and case, or, for a general affidavit, the purpose in one line.</li>
<li><b>Deponent details</b> — full name, age, CNIC number and occupation, and place of residence.</li>
<li><b>Opening</b> — that the deponent is competent to swear the affidavit and understands the facts.</li>
<li><b>Numbered paragraphs</b> — one fact per paragraph, chronologically ordered.</li>
<li><b>Source of knowledge</b> — say where the fact comes from, and mark believed facts as stated on belief.</li>
<li><b>Exhibits</b> — each document named and marked as an annexure.</li>
<li><b>Jurat</b> — sworn or affirmed at a named place on a stated date, before a named officer.</li>
</ol>
<div class="callout"><b>Common failure:</b> the deponent signs but the officer's attestation, seal or licence number is missing. That single omission can push an affidavit out of consideration.</div>
"""},
            {"h2": "What must the jurat say?",
             "answer": "It must record that the contents were read over and explained to the deponent, that the deponent understood them, and that the oath was taken before the named officer on a stated date.",
             "html": """
<p>A workable jurat in Pakistani practice reads, in substance:</p>
<table class="tbl">
<tbody>
<tr><td><b>Verified</b></td><td>that the contents were read over and explained to the deponent, who understood them, and that the statement is true to the best of the deponent's knowledge, information and belief.</td></tr>
<tr><td><b>Sworn / affirmed</b></td><td>at [place] on [date] before [name and designation of the attesting officer].</td></tr>
<tr><td><b>Signature</b></td><td>of the deponent, with the officer's signature, stamp and licence number.</td></tr>
</tbody>
</table>
<p>Where the deponent cannot read, the officer must record that the affidavit was read and explained in a language the deponent understands.</p>
"""},
            {"h2": "Which mistakes make an affidavit risky?",
             "answer": "Opinion instead of fact, facts the deponent cannot know, legal argument, no exhibit labels, and conflicting statements in an earlier affidavit.",
             "html": """
<ul>
<li><b>Opinion and law</b> — the affidavit is for facts; arguments belong in the plaint or application.</li>
<li><b>Hearsay without disclosure</b> — always state the source.</li>
<li><b>Over-claiming</b> — anything false or reckless invites proceedings for perjury and destroys credibility.</li>
<li><b>Unlabelled annexures</b> — refer to documents by annexure letter in the body.</li>
<li><b>Stale templates</b> — depends on the court; a district court affidavit and a High Court affidavit differ in heading and sometimes in format requirements.</li>
</ul>
"""},
        ],
        "faqs": [
            ("Can an affidavit be sworn in English if the deponent only speaks Urdu?",
             "It can, but the officer must record that it was read over and explained in a language the deponent understood. Otherwise the affidavit is open to challenge."),
            ("Does an affidavit need stamp paper?",
             "In Pakistani practice court affidavits are usually prepared on plain paper and attested by a notary or oath commissioner, while some purpose-specific affidavits are executed on stamp paper. Confirm the local requirement with the office of the court or the sub-registrar."),
            ("Is an affidavit evidence on its own?",
             "Not automatically. It is used where the law or the court's order permits, and the deponent can still be required to appear for cross-examination. Read Order XIX CPC and the court's specific order."),
        ],
        "sources": [
            ("Oaths Act 1873", "http://nasirlawsite.com/laws/oaths.htm", "statute"),
            ("Code of Civil Procedure 1908 — Order XIX (affidavits)", "http://nasirlawsite.com/laws/cpc.htm", "statute"),
            ("Qanun-e-Shahadat Order 1984", "http://nasirlawsite.com/laws/qso.htm", "statute"),
        ],
        "related": [
            ("Written statement format", "drafts/written-statement-format/index.html"),
            ("Power of attorney format", "drafts/power-of-attorney-format/index.html"),
            ("Plaint format", "drafts/plaint-format/index.html"),
        ],
    },
    {
        "slug": "drafts/rent-agreement-format/index.html",
        "url": "drafts/rent-agreement-format/",
        "title": "Rent Agreement Format Pakistan (Sindh) — Clauses That Matter",
        "h1": "Rent Agreement Format (Sindh)",
        "desc": "A rent agreement in Karachi: the clauses that prevent disputes — rent, security deposit, notice period, repairs, subletting — and the Sindh Rented Premises Ordinance 1979 rules.",
        "kicker": "Draft library",
        "answer": "A rent agreement in Sindh should state the parties, the premises, the rent and its due date, the security deposit and its return, the notice period for each side, who pays utilities and repairs, and whether subletting is allowed. The Sindh Rented Premises Ordinance 1979 governs tenancies.",
        "facts": [
            ("Governing law", "Sindh Rented Premises Ordinance 1979"),
            ("Who uses it", "Landlord and tenant, usually for 11 months or another agreed term"),
            ("Essentials", "Parties, premises, rent, deposit, duration, notice, repairs, utilities"),
            ("Dispute forum", "Rent controller / civil court, depending on the relief sought"),
            ("Stamp and registration", "Rates and requirements change — confirm with the sub-registrar"),
            ("Lawyer's role", "Drafting, checking title and authority, and advising on notice and eviction grounds"),
        ],
        "sections": [
            {"h2": "Which clauses prevent most rent disputes?",
             "answer": "Deposit return, notice period, repair responsibility, utility bills and subletting — the five clauses that lawyers most often find missing.",
             "html": """
<table class="tbl">
<thead><tr><th>Clause</th><th>What to write</th></tr></thead>
<tbody>
<tr><td><b>Deposit</b></td><td>Amount, what it can be adjusted against, and a clear deadline for return after vacant possession</td></tr>
<tr><td><b>Notice</b></td><td>How many days each side must give, and how the notice must be served</td></tr>
<tr><td><b>Repairs</b></td><td>Structural repairs to the landlord, day-to-day to the tenant, with a cost limit</td></tr>
<tr><td><b>Utilities</b></td><td>Who pays which meter, and what happens if the previous bill is unpaid</td></tr>
<tr><td><b>Subletting</b></td><td>Allowed or not, in plain words, with written consent required</td></tr>
<tr><td><b>Inspection</b></td><td>Right to inspect on notice, and photographs or a schedule of condition at handover</td></tr>
</tbody>
</table>
"""},
            {"h2": "What documents should a tenant check before signing?",
             "answer": "The landlord's title or authority to let, the CNIC of the landlord, the utility bills, and any prior tenancy or litigation on the premises.",
             "html": """
<ul>
<li><b>Ownership</b> — sale deed, allotment letter, or a lease in the landlord's name.</li>
<li><b>Authority</b> — if the signer is not the owner, a power of attorney or written authority from the owner.</li>
<li><b>Encumbrance</b> — any pending mortgage, court case or previous tenant dispute.</li>
<li><b>Identification</b> — CNIC copies signed across the photograph and attached to the agreement.</li>
<li><b>Inventory</b> — a signed list of fixtures, fittings and meter readings at handover.</li>
</ul>
<div class="callout"><b>For lawyers:</b> a short written note to the client listing these checks is better practice than a long oral explanation. Keep a signed copy on the file.</div>
"""},
            {"h2": "How does a tenancy end lawfully?",
             "answer": "By expiry of the term, by mutual agreement, or by notice as the agreement and the ordinance require — eviction on the street is not a lawful option.",
             "html": """
<ol class="steps">
<li>Serve notice in the manner the agreement requires, and keep proof of service.</li>
<li>State the ground relied on: expiry, non-payment, personal need, misuse of the premises.</li>
<li>Give a realistic date for vacant possession and settle the deposit against arrears.</li>
<li>If the tenant does not vacate, apply to the rent controller or the court on the available ground.</li>
<li>Do not change locks, cut water or disconnect utilities to force a vacancy; that creates a separate cause of action.</li>
</ol>
"""},
        ],
        "faqs": [
            ("Is an 11-month rent agreement required in Pakistan?",
             "An 11-month term is commonly used, partly to keep the agreement outside certain registration requirements for longer leases. Confirm the current stamp and registration position with the sub-registrar before relying on it."),
            ("What stamp duty applies to a rent agreement in Sindh?",
             "The rate depends on the term and the rent, and it is changed by notification. Check the current rates with the sub-registrar's office or the Sindh Stamp Rules rather than using an old figure."),
            ("Can a landlord keep the security deposit?",
             "Only to the extent of unpaid rent, bills or damage as stated in the agreement. A general retention without a written basis invites a claim."),
        ],
        "sources": [
            ("Sindh Rented Premises Ordinance 1979", "http://nasirlawsite.com/laws/srpo.htm", "statute"),
            ("Sindh government — stamp duty and registration", "https://sindh.gov.pk/", "provincial authority"),
        ],
        "related": [
            ("Legal notice format", "drafts/legal-notice-format/index.html"),
            ("Rooms and seat sharing in Karachi", "karachi/lawyer-room-for-rent/index.html"),
            ("Affidavit format", "drafts/affidavit-format/index.html"),
        ],
    },
    {
        "slug": "drafts/power-of-attorney-format/index.html",
        "url": "drafts/power-of-attorney-format/",
        "title": "Power of Attorney Format Pakistan — Mukhtar Nama",
        "h1": "Power of Attorney Format (Pakistan)",
        "desc": "Special and general power of attorney in Pakistan: what the Mukhtar Nama must state, attestation and registration, revocation, and the powers that are misused.",
        "kicker": "Draft library",
        "answer": "A power of attorney authorises one person to act for another. A special power of attorney is limited to particular acts, such as appearing in one case or executing one sale; a general power of attorney covers wider powers. It must identify the parties, list the powers, state the term, and be properly attested and, where required, registered.",
        "facts": [
            ("Statute", "Power of Attorney Act 1882; Registration Act 1908 for registration"),
            ("Two types", "Special (specific acts) and general (broad authority)"),
            ("Execution", "Signed by the donor, attested by witnesses, and notarised"),
            ("For court work", "The vakalatnama is used for representation, not a power of attorney"),
            ("For property", "Registration is normally required where the power concerns an immovable property"),
            ("Revocation", "In writing, communicated to the holder, and often registered if the original was registered"),
        ],
        "sections": [
            {"h2": "What must a power of attorney contain?",
             "answer": "Identity of donor and holder, an exact list of powers, any limits, the term, and a clear statement of when the authority ends.",
             "html": """
<ol class="steps">
<li><b>Title</b> — Special or General Power of Attorney, and its purpose.</li>
<li><b>Parties</b> — donor and attorney with full names, parentage, CNIC and address.</li>
<li><b>Recitals</b> — why the authority is being given, in one or two paragraphs.</li>
<li><b>Operative clauses</b> — numbered powers. Be exact: to sign, to sell, to appear, to receive.</li>
<li><b>Limits</b> — what the attorney may not do without fresh written authority.</li>
<li><b>Term and revocation</b> — duration and how it can be revoked.</li>
<li><b>Execution block</b> — donor's signature, witnesses, notary attestation, and registration endorsement where applicable.</li>
</ol>
"""},
            {"h2": "Special or general — which one should you draft?",
             "answer": "Choose the narrowest authority that does the job. A general power of attorney is the most abused document in property matters.",
             "html": """
<table class="tbl">
<thead><tr><th></th><th>Special</th><th>General</th></tr></thead>
<tbody>
<tr><td>Scope</td><td>One transaction, one case, one act</td><td>Wide, continuing authority</td></tr>
<tr><td>Risk</td><td>Low</td><td>High — misuse, unauthorised sales, borrowed signatures</td></tr>
<tr><td>Use it for</td><td>Selling one plot, appearing in one matter, collecting one payment</td><td>Managing affairs during a long absence, when there is no alternative</td></tr>
<tr><td>Lawyer's duty</td><td>Identify the donor and confirm the instructions directly</td><td>Insist on registration, a short term, and accounting obligations</td></tr>
</tbody>
</table>
<div class="callout"><b>Standing practice:</b> never execute a general power of attorney for immovable property on the strength of a phone instruction. Verify the donor in person or by a documented video call with CNIC.</div>
"""},
            {"h2": "How is it attested, registered and revoked?",
             "answer": "Signed before witnesses and a notary; registered where the transaction requires it; revoked in writing and, ideally, by a registered deed of revocation.",
             "html": """
<ul>
<li><b>Attestation</b> — witnesses must be present and must sign; the notary records the donor's identity.</li>
<li><b>Registration</b> — a power relating to immovable property is normally presented for registration before the sub-registrar.</li>
<li><b>Revocation</b> — a written deed, delivered to the attorney and notified to the parties who dealt on the strength of it; register the revocation if the original was registered.</li>
<li><b>Death of the donor</b> — the authority ends automatically. Ensure the record reflects it.</li>
</ul>
"""},
        ],
        "faqs": [
            ("Can a power of attorney be used to appear in court?",
             "A lawyer appears on a vakalatnama. A power of attorney may authorise someone to instruct a lawyer or act in related matters, but the vakalatnama is the document courts require for representation. Do not mix the two."),
            ("Is a power of attorney executed abroad valid in Pakistan?",
             "It can be, if it is executed and attested in the manner the law requires, and usually notarised and then authenticated through the Pakistani mission concerned. Confirm the current requirement with the sub-registrar and the consular section."),
            ("What if an attorney sells property beyond the powers granted?",
             "The transaction can be challenged on the ground that the act was outside the authority granted. Both the attorney and the purchaser may face consequences. Act quickly and preserve the original deed."),
        ],
        "sources": [
            ("Power of Attorney Act 1882", "http://nasirlawsite.com/laws/poa.htm", "statute"),
            ("Registration Act 1908", "http://nasirlawsite.com/laws/reg.htm", "statute"),
        ],
        "related": [
            ("Vakalatnama format", "drafts/vakalatnama-format/index.html"),
            ("Affidavit format", "drafts/affidavit-format/index.html"),
            ("Legal notice format", "drafts/legal-notice-format/index.html"),
        ],
    },
    {
        "slug": "drafts/legal-notice-reply-format/index.html",
        "url": "drafts/legal-notice-reply-format/",
        "title": "Legal Notice Reply Format Pakistan — How to Answer a Notice",
        "h1": "Legal Notice Reply Format (Pakistan)",
        "desc": "How to reply to a legal notice in Pakistan: what to admit, what to deny, which documents to attach, the time limit, and the mistakes that turn a reply into evidence against you.",
        "kicker": "Draft library",
        "answer": "A reply to a legal notice should be sent within the time given in the notice, deny the allegations specifically, state your own facts with dates, attach the documents you rely on, and keep the tone factual. Never admit a liability you have not verified, and never ignore a notice.",
        "facts": [
            ("Time to reply", "Within the period stated in the notice; 7 to 15 days is common"),
            ("Mode of reply", "Registered post with acknowledgement due, and a copy by email or courier"),
            ("Core content", "Paragraph-wise reply, own version of facts, documents, and a reserved-rights clause"),
            ("Evidence value", "An unreplied notice can support the sender's version; a careless reply can be used against you"),
            ("Drafting rule", "Admit only what is true and verified; deny everything else specifically"),
        ],
        "sections": [
            {"h2": "What should a reply to a legal notice contain?",
             "answer": "A paragraph-wise response, your own account of the facts, the documents that support it, and a clear position on what you are willing to do.",
             "html": """
<ol class="steps">
<li><b>Reference</b> — the notice's date, its reference number and the sender's name.</li>
<li><b>Paragraph-wise reply</b> — number each answer to match the notice.</li>
<li><b>Your version</b> — facts with dates and documents, in a separate section with a heading.</li>
<li><b>Legal position</b> — the sections or clauses you rely on, only if you are sure of them.</li>
<li><b>Offer or refusal</b> — say plainly whether you will pay, perform or deny, and on what terms.</li>
<li><b>Reservation</b> — that all rights and defences are reserved, and that the reply is without prejudice where that is genuinely intended.</li>
<li><b>Proof of dispatch</b> — keep the postal receipt and acknowledgement card.</li>
</ol>
"""},
            {"h2": "What should a reply never do?",
             "answer": "Never ignore it, never admit a debt you have not verified, never threaten, and never send it without proof of dispatch.",
             "html": """
<ul>
<li><b>Ignoring the notice</b> — silence is often read as acceptance in commercial disputes.</li>
<li><b>Emotional language</b> — the reply will be read in court years later; keep it factual.</li>
<li><b>Admitting liability casually</b> — an admission can be used against your client.</li>
<li><b>Raising every defence at once</b> — inconsistent defences weaken the strong one.</li>
<li><b>No proof of service</b> — a reply that cannot be shown to have been received is of little use.</li>
</ul>
<div class="callout"><b>Practical note:</b> many cheque cases turn on whether the notice of demand was properly served. Preserve the receipt, the tracking record and the returned envelope.</div>
"""},
            {"h2": "How long does the sender have to file after the notice?",
             "answer": "It depends on the statute behind the notice. For a dishonoured cheque under 489-F PPC practice, timing of the notice and the complaint matters; for civil claims, limitation runs from the cause of action.",
             "html": """
<p>Do not rely on a general figure. Check:</p>
<ul>
<li>The <b>statute</b> named in the notice, and whether it prescribes a period.</li>
<li>The <b>limitation</b> applicable to the underlying claim in the Limitation Act 1908.</li>
<li>The <b>date of service</b>, not the date of the letter.</li>
</ul>
"""},
        ],
        "faqs": [
            ("Should I reply to a legal notice if the claim is false?",
             "Yes. A short, specific denial with your documents is far safer than silence, which can be used to support the sender's story."),
            ("Can I reply myself without a lawyer?",
             "You can send a factual reply, but a badly worded admission can cost more than the fee. Have a lawyer read the notice before you answer it."),
            ("Does a reply stop the other side from going to court?",
             "No. It sets out your position, which may encourage settlement, but the sender can still file. The reply becomes part of the record."),
        ],
        "sources": [
            ("Limitation Act 1908", "http://nasirlawsite.com/laws/lim.htm", "statute"),
            ("Pakistan Penal Code 1860 — section 489-F", "http://nasirlawsite.com/laws/ppc.htm", "statute"),
        ],
        "related": [
            ("Legal notice format", "drafts/legal-notice-format/index.html"),
            ("489-F PPC — cheque dishonour", "case-law/489-f/index.html"),
            ("Written statement format", "drafts/written-statement-format/index.html"),
        ],
    },

    # ------------------------------------------------------------ career
    {
        "slug": "career/cause-list-tracking/index.html",
        "url": "career/cause-list-tracking/",
        "title": "Cause List Tracking Pakistan — Never Miss a Date Again",
        "h1": "Cause List Tracking for Pakistani Lawyers",
        "desc": "How Pakistani lawyers track cause lists and court dates: where cause lists are published, how to read them, a simple case-register system, and a daily routine that prevents missed hearings.",
        "kicker": "Career · Practice",
        "answer": "A cause list is the court's daily schedule of cases. Track it by checking the official court source for your court every evening, matching your case register against it, and confirming the result of each hearing the same day. Never depend on a client or a colleague to tell you a date.",
        "facts": [
            ("What it is", "The court's list of cases fixed for a particular day"),
            ("Where published", "Official court websites, court notice boards, and the bar association's list"),
            ("When to check", "The evening before, and again in the morning before appearing"),
            ("Core tool", "Your own case register: file number, next date, purpose, court, fee status"),
            ("Cost of a missed date", "Costs, ex parte orders, warrants, or dismissal for non-prosecution"),
            ("Best practice", "One source of truth, updated daily, backed up"),
        ],
        "sections": [
            {"h2": "Where are cause lists published in Pakistan?",
             "answer": "Official court websites publish daily and weekly cause lists; district courts rely heavily on notice boards and the bar association's list, and court staff can confirm a fixed date.",
             "html": """
<ul>
<li><b>Sindh High Court</b> — daily cause lists are published on the court's official website, normally in the evening for the next working day.</li>
<li><b>District and City Courts</b> — printed lists on the notice board, plus the list circulated at the bar room. Confirm with the reader or the court office.</li>
<li><b>Supreme Court</b> — cause lists are published on the Supreme Court website for each bench.</li>
<li><b>Special courts and tribunals</b> — check with the office directly; publication online is not guaranteed.</li>
</ul>
<div class="callout"><b>Verification rule:</b> treat any date received by WhatsApp as unconfirmed until you have seen it on the official list or been told by the court office. Screenshots get edited and forwarded with the wrong date.</div>
"""},
            {"h2": "How do you read a cause list quickly?",
             "answer": "Find your court and bench first, then scan for the case number — not the party names, which are often spelled inconsistently.",
             "html": """
<ol class="steps">
<li>Confirm the <b>court, bench and judge</b> heading. The same case can appear before a different bench.</li>
<li>Search the case <b>number</b> and <b>year</b>, then cross-check the parties.</li>
<li>Note the <b>serial number</b>, the <b>purpose</b> (arguments, evidence, order) and the <b>time slot</b> if shown.</li>
<li>Mark whether the matter is listed as <i>fixed</i> or in the <i>supplementary</i> list, which is often heard later in the day.</li>
<li>Write the serial number on your file cover before you leave the chamber.</li>
</ol>
"""},
            {"h2": "What should a simple case register contain?",
             "answer": "One line per case with the court, file number, parties, next date, purpose, fee position and what happened at the last hearing.",
             "html": """
<table class="tbl">
<thead><tr><th>Column</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Court, bench, judge</td><td>Decides where you stand at 9 a.m.</td></tr>
<tr><td>File and case number, year</td><td>The only reliable identifier in a cause list</td></tr>
<tr><td>Parties, short form</td><td>Quick recognition under time pressure</td></tr>
<tr><td>Next date and purpose</td><td>Drives the evening check</td></tr>
<tr><td>Last order, one line</td><td>Prevents repeating an argument already decided</td></tr>
<tr><td>Fee and payment status</td><td>Stops you appearing on an unpaid brief</td></tr>
<tr><td>Documents due</td><td>Ensures the file is complete before the date</td></tr>
</tbody>
</table>
<p>A spreadsheet is enough. The point is one register, updated the same day, not five notebooks and a phone gallery.</p>
"""},
            {"h2": "What is a workable daily routine?",
             "answer": "Evening: check tomorrow's lists against the register. Morning: re-check, then report each hearing result before you leave court.",
             "html": """
<ul>
<li><b>6 p.m.</b> — open the official list for each court where you have a matter tomorrow.</li>
<li><b>6.30 p.m.</b> — update the register, message the client the time and court, and prepare the file the night before.</li>
<li><b>8.30 a.m.</b> — re-check the supplementary list before entering the courtroom.</li>
<li><b>After each hearing</b> — write the one-line order and the next date in the register, not on a loose paper.</li>
<li><b>Weekly</b> — back up the register and review matters with no date for more than 30 days.</li>
</ul>
"""},
        ],
        "faqs": [
            ("What happens if a lawyer misses a hearing?",
             "The court may pass an ex parte order, dismiss the matter for non-prosecution, issue warrants, or impose costs. Recovery usually needs an application for restoration or recall, which costs time and money."),
            ("Can a client check the cause list themselves?",
             "They can read the public list, but the responsibility for tracking stays with the advocate. Set the expectation at the first meeting: dates are confirmed by the chamber, not by rumour."),
            ("Is there one app for all Pakistani cause lists?",
             "No single official app covers every court. Practitioners use the individual court websites plus their own register. Any third-party app should be treated as a convenience, never as the source of truth."),
        ],
        "sources": [
            ("Sindh High Court — cause lists and judgments", "https://sindhhighcourt.gov.pk/", "court website"),
            ("Supreme Court of Pakistan — cause lists", "https://www.supremecourt.gov.pk/", "court website"),
        ],
        "related": [
            ("First 30 days in a chamber", "career/first-30-days-in-chamber/index.html"),
            ("Karachi City Courts guide", "karachi/city-courts-guide/index.html"),
            ("High Court licence", "career/high-court-license/index.html"),
        ],
    },
    {
        "slug": "career/lawyer-cv-format/index.html",
        "url": "career/lawyer-cv-format/",
        "title": "Lawyer CV Format Pakistan — One Page That Gets a Reply",
        "h1": "Lawyer CV Format for Pakistan",
        "desc": "A one-page CV format for Pakistani law graduates and junior advocates: what chambers and firms actually look for, how to describe internships, and the mistakes that get a CV ignored.",
        "kicker": "Career · Entry",
        "answer": "A Pakistani legal CV should fit on one page: name and contact, bar enrollment status, education with grades, internships described by what you did, drafting and research skills, languages, and two referees. Chambers hire on demonstrated work, not adjectives.",
        "facts": [
            ("Length", "One page for students and juniors; two only after five years"),
            ("Order", "Contact, enrollment status, education, experience, skills, languages, referees"),
            ("What wins interviews", "Specific drafting and court exposure, with numbers"),
            ("What loses them", "Generic phrases such as hardworking, and no dates"),
            ("Attach", "A short covering note and, if asked, two writing samples"),
        ],
        "sections": [
            {"h2": "What should a one-page legal CV contain?",
             "answer": "Contact details, enrollment or Law-GAT status, education, internships with real descriptions, skills with evidence, languages, and referees.",
             "html": """
<ol class="steps">
<li><b>Header</b> — name, city, phone, professional email, LinkedIn URL. No photo unless asked.</li>
<li><b>Status line</b> — one line: LLB (year, university), Law-GAT status, Sindh Bar Council enrollment number if issued.</li>
<li><b>Education</b> — degree, institution, year, and grades if they are good.</li>
<li><b>Legal experience</b> — internships and pupillage: chamber or firm, court, dates, and what you drafted or observed.</li>
<li><b>Skills</b> — drafting, research databases, court filing, language, typing speed in Urdu and English.</li>
<li><b>Extras</b> — moots, publications, legal aid work, positions held.</li>
<li><b>Referees</b> — two, with designation and a working phone number, and their permission.</li>
</ol>
"""},
            {"h2": "How do you describe an internship properly?",
             "answer": "Use verbs and objects: what you drafted, for which court, how many, and under whose supervision.",
             "html": """
<table class="tbl">
<thead><tr><th>Weak</th><th>Strong</th></tr></thead>
<tbody>
<tr><td>Worked in a law chamber and learned a lot</td><td>Drafted 14 bail applications and 6 legal notices for a criminal practice at City Courts, Karachi; maintained a daily cause-list register for 40 files</td></tr>
<tr><td>Did research work</td><td>Prepared case-law memos on 489-F PPC and 497 CrPC, verifying every citation against PLD and SCMR volumes</td></tr>
<tr><td>Good communication skills</td><td>Drafted client correspondence in English and Urdu; translated a 12-page agreement for filing</td></tr>
</tbody>
</table>
<div class="callout"><b>Rule:</b> if a line cannot be proved in an interview with a document or a story, delete it.</div>
"""},
            {"h2": "What gets a junior CV rejected?",
             "answer": "No dates, unexplained gaps, invented experience, blurry formatting, and applying to chambers whose practice area is nowhere in the CV.",
             "html": """
<ul>
<li><b>Targeting nothing</b> — a criminal chamber reads a CV full of corporate tax work and moves on.</li>
<li><b>Vague claims</b> — every senior has heard I am a hardworking quick learner.</li>
<li><b>No writing sample</b> — if you claim drafting, keep two samples ready.</li>
<li><b>Careless errors</b> — a misspelt court name or a wrong case citation ends the conversation.</li>
<li><b>Wrong email</b> — a casual address costs interviews. Use name-based email.</li>
</ul>
"""},
        ],
        "faqs": [
            ("Should a fresh graduate include a photo on a legal CV?",
             "Usually not. Pakistani legal employers focus on education, drafting exposure and references. Keep the page clean and let the content speak."),
            ("Is it acceptable to email chambers directly?",
             "Yes. Keep the email to four lines: who you are, what you want, what you offer, and the attached CV. Then follow up once, in person, with a printed copy."),
            ("How long should a covering email be?",
             "Four to six lines. Seniors read on a phone between hearings. State your university, your enrollment status and which days you are available."),
        ],
        "sources": [
            ("Sindh Bar Council — enrollment and verification", "https://advocates.sindhbarcouncil.org/", "official register"),
            ("Higher Education Commission — degree verification", "https://www.hec.gov.pk/", "official"),
        ],
        "related": [
            ("Lawyer jobs in Karachi", "karachi/lawyer-jobs/index.html"),
            ("First 30 days in a chamber", "career/first-30-days-in-chamber/index.html"),
            ("Bar council enrollment", "career/bar-council-enrollment/index.html"),
        ],
    },
    {
        "slug": "career/first-30-days-in-chamber/index.html",
        "url": "career/first-30-days-in-chamber/",
        "title": "Your First 30 Days in a Chamber — A Junior Lawyer's Plan",
        "h1": "Your First 30 Days in a Chamber",
        "desc": "A week-by-week plan for a new pupil or junior advocate in Pakistan: what to learn, what to write down, how to be useful, and how to build a record that gets you a paid seat.",
        "kicker": "Career · Practice",
        "answer": "In your first 30 days, learn the court routine, build a personal precedent file, volunteer for drafting, and keep a written record of everything you did. Usefulness earns a stipend faster than waiting for one.",
        "facts": [
            ("Week 1", "Court geography, filing counter, cause list, chamber routine"),
            ("Week 2", "Read five complete files end to end and summarise each"),
            ("Week 3", "Draft three documents and have them corrected in red"),
            ("Week 4", "Ask for one independent task and deliver it early"),
            ("Keep forever", "A precedent file of your own corrected drafts"),
            ("Mistake to avoid", "Sitting silent, waiting to be taught"),
        ],
        "sections": [
            {"h2": "Week 1 — what should you learn first?",
             "answer": "Where things are and how the day runs: the courtrooms, the filing counter, the reader's office, the cause list, and the chamber's own routine.",
             "html": """
<ul>
<li>Walk the court complex with a clerk. Learn the filing counter, the copying agency, the stamp vendor and the library.</li>
<li>Ask which court the chamber appears in most, and read three days of cause lists for it.</li>
<li>Learn the chamber's filing system and never return a file to the wrong shelf.</li>
<li>Write down names and roles: reader, clerk, naib qasid, court stenographer.</li>
<li>Arrive before your senior, every day, in the first month.</li>
</ul>
"""},
            {"h2": "Week 2 — how do you learn from files?",
             "answer": "Read five complete files end to end, then write a one-page summary of each: parties, facts, stage, next date, and the weak point.",
             "html": """
<ol class="steps">
<li>Take a file that has reached arguments, not a brand-new one.</li>
<li>Read the plaint or FIR, the reply, the orders and the last application.</li>
<li>Write the chronology yourself — do not copy the senior's note.</li>
<li>Identify the single weakest link in the case and say why.</li>
<li>Compare your note with the senior's and ask what you missed.</li>
</ol>
<div class="callout"><b>Why this works:</b> in six months you will have read a hundred files and written a hundred summaries. That record is worth more to an employer than your transcript.</div>
"""},
            {"h2": "Week 3 — how do you start drafting?",
             "answer": "Copy the structure, not the facts. Draft by hand, get it corrected, and keep the corrected version in your own precedent file.",
             "html": """
<ul>
<li>Ask for a document you have seen before: a legal notice, an application for adjournment, a bail application.</li>
<li>Draft from the file, never from a template with someone else's facts left inside.</li>
<li>Submit with a note of the points you were unsure about — seniors respect flagged doubts.</li>
<li>Keep the corrected draft. Highlight every change you did not expect.</li>
<li>Never file anything you have not read end to end yourself.</li>
</ul>
"""},
            {"h2": "Week 4 — how do you become paid, not just present?",
             "answer": "Ask for one task you can own completely, deliver it early, and then ask directly about the terms of your seat.",
             "html": """
<ol class="steps">
<li>Volunteer for a research memo, a set of case summaries or a cause-list register.</li>
<li>Deliver a day before the deadline, with sources checked.</li>
<li>Ask for feedback in one question: what would make this usable as filed?</li>
<li>At the end of the month, ask about hours, stipend and what you will be taught.</li>
<li>Put the agreed terms in writing — even a short WhatsApp message that the senior confirms.</li>
</ol>
<div class="callout"><b>Reality check:</b> many chambers in Karachi pay nothing for the first months. Decide in advance how long you can sustain that, and plan the work-board income that covers the gap.</div>
"""},
        ],
        "faqs": [
            ("Should a pupil ask for a stipend in the first month?",
             "Not usually in the first week, but by the end of the first month it is reasonable to ask about terms. Ask in a scheduled conversation, not in the corridor, and be clear about what you are already delivering."),
            ("What if the chamber gives no work at all?",
             "Ask for specific work, and give a deadline you control. If nothing changes after six weeks, the seat is not a training seat, and it is reasonable to look elsewhere without burning the relationship."),
            ("How many hours should a junior expect to work?",
             "Court hours plus chamber hours, typically six days a week in a litigation practice. Agree the expectations in writing so that both sides know what the first year looks like."),
        ],
        "sources": [
            ("Legal Practitioners and Bar Councils Act 1973", "http://nasirlawsite.com/laws/baract.htm", "statute"),
            ("Sindh Bar Council — advocate verification portal", "https://advocates.sindhbarcouncil.org/", "official register"),
        ],
        "related": [
            ("Lawyer CV format", "career/lawyer-cv-format/index.html"),
            ("Cause list tracking", "career/cause-list-tracking/index.html"),
            ("Lawyer salary in Pakistan", "career/lawyer-salary-pakistan/index.html"),
        ],
    },

    # ------------------------------------------------------------ karachi
    {
        "slug": "karachi/chamber-seat-rent/index.html",
        "url": "karachi/chamber-seat-rent/",
        "title": "Lawyer Chamber for Rent in Karachi — Seat Share Guide",
        "h1": "Lawyer Chamber for Rent in Karachi",
        "desc": "What a chamber seat costs in Karachi, what to check before sharing a chamber, how seat sharing works between juniors, and the areas closest to City Courts and the Sindh High Court.",
        "kicker": "Karachi · Housing",
        "answer": "A shared chamber seat in Karachi usually costs Rs 6,000 to 15,000 a month, depending on the court vicinity, the size of the chamber and whether a clerk is included. Always agree in writing what the seat includes before paying.",
        "facts": [
            ("Typical seat share", "Rs 6,000 to 15,000 a month"),
            ("Usually included", "Desk, chair, cupboard, electricity, and shared use of the library"),
            ("Often extra", "Clerk's salary, stationery, internet, chamber maintenance"),
            ("Best locations", "Around City Courts, Saddar, Garden and near the Sindh High Court"),
            ("Usual arrangement", "Two or three juniors share one chamber and split the rent"),
            ("Written record needed", "Rent, inclusions, notice period, and who holds the key"),
        ],
        "sections": [
            {"h2": "What does a chamber seat actually cost?",
             "answer": "Between Rs 6,000 and Rs 15,000 a month for a shared seat, with the higher end near the High Court and in chambers with a library and clerk.",
             "html": """
<table class="tbl">
<thead><tr><th>Arrangement</th><th>Typical monthly cost</th><th>What you get</th></tr></thead>
<tbody>
<tr><td>Desk in a shared chamber</td><td>Rs 6,000 – 9,000</td><td>Desk, chair, cupboard, shared library</td></tr>
<tr><td>Seat plus clerk support</td><td>Rs 10,000 – 15,000</td><td>Adds filing, copying and cause-list help</td></tr>
<tr><td>Small independent chamber</td><td>Rs 20,000 and above</td><td>Own room, often with utilities separate</td></tr>
</tbody>
</table>
<p>Figures are indicative for 2026 and vary street to street. Treat them as a starting point for negotiation, not a rate card.</p>
"""},
            {"h2": "What should a junior check before sharing a chamber?",
             "answer": "Who the tenant of record is, what the rent includes, how the key is held, whether the senior is present daily, and whether client files will be safe.",
             "html": """
<ul>
<li><b>Tenancy</b> — the chamber's own lease and the person legally entitled to sublet space.</li>
<li><b>Inclusions</b> — electricity, internet, cleaning, clerk, stationery. Get a list, not a promise.</li>
<li><b>Security</b> — a locker or cupboard you alone can lock, and a written inventory.</li>
<li><b>Use of the library</b> — borrowing rules, and whether reports may leave the chamber.</li>
<li><b>Notice</b> — how many days must either side give before leaving.</li>
<li><b>Client meetings</b> — whether you may meet your own clients there, and at what hours.</li>
</ul>
<div class="callout"><b>Do not pay a deposit without a receipt that names the payer, the amount, the period covered and what the deposit secures.</b></div>
"""},
            {"h2": "How does seat sharing between juniors work in practice?",
             "answer": "Two or three juniors take one chamber, split the rent and utilities, and agree a rota for who receives clients and how files are stored.",
             "html": """
<ol class="steps">
<li>Agree the split in writing: rent, utilities, clerk, stationery.</li>
<li>Allocate desks and storage physically, so nothing is ambiguous.</li>
<li>Set rules on client meetings — booked slots, no overlapping appointments.</li>
<li>Keep separate files, in separately locked cupboards.</li>
<li>Fix an exit clause: 30 days' notice, deposit returned after the final utility bill.</li>
</ol>
"""},
            {"h2": "Is a chamber seat worth the money in the first year?",
             "answer": "Yes, if it puts you within walking distance of your court and gives you a place clients can visit. It is a cost of doing business, not a luxury.",
             "html": """
<p>Compare it with the alternative:</p>
<ul>
<li>Working from home means no walk-in clients and no library.</li>
<li>Paying for a separate room costs two to three times more for the same utility.</li>
<li>A shared seat near the court saves travel time, which is the scarcest resource of a junior.</li>
</ul>
<p>On a Rs 30,000 stipend, a Rs 8,000 seat is 27% of income — but it is the difference between being a lawyer with an address and one without.</p>
"""},
        ],
        "faqs": [
            ("Can a chamber seat be shared by a man and a woman advocate?",
             "Shared professional space is a matter for the parties to agree, and many chambers allocate separate desks and storage. What matters is a written arrangement that both sides are comfortable with; harassment at the workplace is separately governed by law."),
            ("Do I need a separate chamber to take my own clients?",
             "No, but you need a place where a client can sit and where your files are safe. Confirm with your senior or co-sharers that you may meet your own clients there."),
            ("What is a fair deposit for a chamber seat?",
             "Commonly one month's rent. Anything higher should be justified in writing and covered by a receipt that states the terms of return."),
        ],
        "sources": [
            ("Sindh Bar Council — Karachi bar associations", "https://advocates.sindhbarcouncil.org/", "official register"),
            ("Sindh High Court", "https://sindhhighcourt.gov.pk/", "court website"),
        ],
        "related": [
            ("Rooms and seat sharing in Karachi", "karachi/lawyer-room-for-rent/index.html"),
            ("Lawyer jobs in Karachi", "karachi/lawyer-jobs/index.html"),
            ("First 30 days in a chamber", "career/first-30-days-in-chamber/index.html"),
        ],
    },
    {
        "slug": "karachi/city-courts-guide/index.html",
        "url": "karachi/city-courts-guide/",
        "title": "Karachi City Courts Guide for New Lawyers",
        "h1": "Karachi City Courts: A Guide for New Lawyers",
        "desc": "A practical guide to the City Courts complex in Karachi for pupils and junior advocates: filing, cause lists, court etiquette, what to carry, and how to use the first month well.",
        "kicker": "Karachi · Practice",
        "answer": "The City Courts complex in Karachi is where most civil, criminal and family trials begin. New lawyers should learn the filing counter, the cause list, the courtrooms of their own cases and basic courtroom etiquette before anything else.",
        "facts": [
            ("What sits here", "Civil, criminal, family and miscellaneous trial matters"),
            ("Main tasks", "Filing, scrutiny, cause list, appearances, copies of orders"),
            ("First week goal", "Know the filing counter, the copying agency and your courtrooms"),
            ("Carry daily", "CNIC, bar card, vakalatnamas, court fee stamps, diary, cause list"),
            ("Timing", "Arrive before the court sits; the list is called early"),
            ("Local rules", "Filing requirements and scrutiny objections vary by court — read the notice board"),
        ],
        "sections": [
            {"h2": "What happens at the filing counter?",
             "answer": "Your plaint or application is presented, checked for court fee and annexures, and either registered or returned with objections.",
             "html": """
<ol class="steps">
<li>Complete the court fee and stamp requirements before you reach the counter.</li>
<li>Keep the plaint or petition, annexures, vakalatnama and identity documents in one tagged set.</li>
<li>Present the file; the office checks pagination, court fee and the list of documents.</li>
<li>If objections are raised, note them exactly and clear them the same day — do not wait for the next date.</li>
<li>Collect the receipt or diary number before you leave. Photograph it.</li>
</ol>
<div class="callout"><b>Most common objection:</b> missing court fee or an unnumbered annexure. Both are avoidable and both delay registration by days.</div>
"""},
            {"h2": "How should a junior behave inside a courtroom?",
             "answer": "Quietly, early and prepared: know your serial number, stand when your case is called, address the court with the correct title, and never interrupt another advocate.",
             "html": """
<ul>
<li>Enter before the court sits and take a seat at the back, not at the bar table.</li>
<li>Keep the file open at the last order, with the next date visible.</li>
<li>Stand and state your appearance briefly: name, party and capacity.</li>
<li>Never argue over another counsel's time. Wait your turn and ask politely for a pass.</li>
<li>Write the order down as it is dictated. Do not rely on memory or on a later copy.</li>
</ul>
"""},
            {"h2": "What should you carry every day?",
             "answer": "CNIC, bar card, vakalatnamas, court fee stamps, diary, cause list, pen, stapler, and the file for each matter listed that day.",
             "html": """
<table class="tbl">
<thead><tr><th>Item</th><th>Why</th></tr></thead>
<tbody>
<tr><td>CNIC and bar card</td><td>Needed at the gate and for identification before a court</td></tr>
<tr><td>Signed vakalatnamas</td><td>You cannot appear without authority on the file</td></tr>
<tr><td>Court fee stamps</td><td>Applications are often filed at short notice</td></tr>
<tr><td>Cause list copy</td><td>Fast scanning when the court is already sitting</td></tr>
<tr><td>Diary and two pens</td><td>Orders are dictated, not emailed</td></tr>
<tr><td>Stapler, tags, glue</td><td>Files are assembled in the corridor, not the chamber</td></tr>
</tbody>
</table>
"""},
            {"h2": "How do you use the first month at City Courts well?",
             "answer": "Attach yourself to one courtroom for a week, watch how matters are called, and record the phrases and steps you will need to copy.",
             "html": """
<ol class="steps">
<li>Spend a full week in one courtroom and write down the daily routine.</li>
<li>Learn how applications are moved: exemptions, adjournments, exhibits, orders.</li>
<li>Collect the standard forms actually used by that court's office.</li>
<li>Introduce yourself to the reader and the clerk — politely, once, with your name and chamber.</li>
<li>Build a personal list of the ten phrases you must be able to say without thinking.</li>
</ol>
"""},
        ],
        "faqs": [
            ("Do I need a separate licence to appear at City Courts in Karachi?",
             "A lower court advocate, licensed and enrolled through the provincial bar council, can appear before the civil and criminal courts. Confirm your own enrollment status with the Sindh Bar Council."),
            ("Can a pupil appear in court alone?",
             "A pupil appears with or under the supervision of the senior, in accordance with the chamber arrangement and the court's practice. Do not appear independently on a brief you are not authorised to handle."),
            ("Where can I get copies of orders?",
             "From the copying agency of the court concerned, on an application, once the order is on the file. Keep the receipt and follow up the same week."),
        ],
        "sources": [
            ("Sindh High Court — district judiciary information", "https://sindhhighcourt.gov.pk/", "court website"),
            ("Sindh Bar Council — advocate verification", "https://advocates.sindhbarcouncil.org/", "official register"),
        ],
        "related": [
            ("Cause list tracking", "career/cause-list-tracking/index.html"),
            ("Chamber for rent in Karachi", "karachi/chamber-seat-rent/index.html"),
            ("Bail application format", "drafts/bail-application-format/index.html"),
        ],
    },
]

# ------------------------------------------------------------ hub additions
HUB_ADDITIONS = {
    "case-law/index.html": [
        ("420 PPC — cheating", "Dishonest inducement, proof and the civil-versus-criminal divide", "../case-law/420-ppc/index.html"),
        ("406 PPC — breach of trust", "Entrustment and misappropriation, and why most such cases are called civil", "../case-law/406-ppc/index.html"),
        ("506 PPC — criminal intimidation", "Threats, proof and the two punishment levels", "../case-law/506-ppc/index.html"),
    ],
    "drafts/index.html": [
        ("Written statement format", "Order VIII CPC — the paragraph-by-paragraph reply", "../drafts/written-statement-format/index.html"),
        ("Affidavit format", "Jurat, attestation and the mistakes that void an affidavit", "../drafts/affidavit-format/index.html"),
        ("Rent agreement format", "Sindh tenancy clauses that prevent disputes", "../drafts/rent-agreement-format/index.html"),
        ("Power of attorney format", "Special versus general authority, and revocation", "../drafts/power-of-attorney-format/index.html"),
        ("Legal notice reply", "How to answer a notice without creating evidence against yourself", "../drafts/legal-notice-reply-format/index.html"),
    ],
    "career/index.html": [
        ("Cause list tracking", "Never miss a date: the daily routine that works", "../career/cause-list-tracking/index.html"),
        ("Lawyer CV format", "A one-page CV that gets a reply", "../career/lawyer-cv-format/index.html"),
        ("First 30 days in a chamber", "A week-by-week plan for a new pupil", "../career/first-30-days-in-chamber/index.html"),
    ],
    "karachi/index.html": [
        ("Chamber for rent", "Seat share costs and what to check before paying", "../karachi/chamber-seat-rent/index.html"),
        ("City Courts guide", "Filing, etiquette and the first month at City Courts", "../karachi/city-courts-guide/index.html"),
    ],
}
