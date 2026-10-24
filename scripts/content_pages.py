# -*- coding: utf-8 -*-
"""
WakeelSaathi — landing page content.
Har page: SEO title, meta description, H1, sections (HTML), FAQs (FAQPage schema), internal links.
Legal facts hamesha "verify from official source" ke saath — koi invented citation nahi.
"""

DISCLAIMER = ("<b>Legal information, not legal advice.</b> Ye page sirf general information aur research guidance deta hai. "
              "Koi judgment ya citation reproduce nahi kiya gaya — har authority <b>original official source</b> se verify karein. "
              "Section numbers, fees aur procedures waqt ke saath badalte hain: Sindh Bar Council, Pakistan Bar Council, "
              "HEC aur mutaliqa court ki official website/office se tasdeeq karein.")

CTA = {
    "title": "WakeelSaathi par muft account banayein",
    "text": "Chamber match, verified rehail, kaam board aur AI kit — junior lawyers ke liye hamesha free.",
}

HUB_CASE_LAW = {
    "slug": "case-law/index.html",
    "url": "case-law/",
    "title": "Case Law Pakistan — Section-wise Judgment Guides | WakeelSaathi",
    "h1": "Case Law Pakistan",
    "desc": "Section-wise case law research guides for Pakistani lawyers: 302 PPC, 489-F PPC, 497 CrPC bail. Free databases, search method aur verification checklist.",
    "kicker": "Research library",
    "lede": "Pakistan mein wakeel ki sab se zyada search ki jane wali cheez: <b>case law</b>. Yahan section-wise research guides hain — kahan se search karein, kaise verify karein, aur court mein kaise use karein.",
    "is_hub": True,
    "childs": [
        ("302 PPC case law", "Qatl-i-amd 302 PPC — elements, research method, Urdu guide", "case-law/302-ppc/index.html"),
        ("489-F PPC case law", "Cheque dishonour 489-F — complaint, defence aur research", "case-law/489-f/index.html"),
        ("497 CrPC bail case law", "Non-bailable offence mein bail — grounds aur authorities", "case-law/497-crpc/index.html"),
    ],
    "sections": [
        {"h2": "Pakistan mein case law kahan se milega (free aur paid)", "html": """
<table class="tbl">
<thead><tr><th>Source</th><th>Kya milta hai</th><th>Cost</th></tr></thead>
<tbody>
<tr><td>Supreme Court of Pakistan website</td><td>Judgments, cause lists, case status</td><td>Free</td></tr>
<tr><td>Federal Shariat Court &amp; High Courts (SHC, LHC, PHC, BHC, IHC)</td><td>Reported judgments, orders</td><td>Free</td></tr>
<tr><td>Pakistan Law Site / Pak Law Database / LegalSearch</td><td>PLD, SCMR, YLR, CLC citations + search</td><td>Free / subscription</td></tr>
<tr><td>PLJ (Punjab Bar Council section)</td><td>Pakistan Law Journal citations</td><td>Subscription</td></tr>
<tr><td>AI research tools (LawGPT, DigiLawyer, Conclavity, PakLegalAI)</td><td>Fast drafting + citation hints</td><td>Free / paid</td></tr>
</tbody>
</table>
<p class="mini">Note: AI tools ka output <b>hamesha verify</b> karein. Fake citation court mein aap ki izzat kha jata hai.</p>
"""},
        {"h2": "4-step research method (jo junior ko koi nahi sikhata)", "html": """
<ol class="steps">
<li><b>Section framing:</b> Pehle bare act ka exact text parhein. Elements alag likhein — har element ek issue hai.</li>
<li><b>Headnote hunting:</b> Digest/law site par section number + key words (e.g. "302 PPC qisas waiver") search karein. 5–8 leading judgments chunein — Supreme Court pehle, phir apna High Court.</li>
<li><b>Ratio extract:</b> Har judgment se ek line: court ne kya principle diya. Poora case summary likhne ki zaroorat nahi.</li>
<li><b>Distinguish:</b> Apne facts se farq likhein. Yehi courtroom mein kaam aata hai — aur yehi wo hissa hai jo AI nahi kar sakta.</li>
</ol>
<div class="callout"><b>Verification rule:</b> Har citation teen jagah check karein — citation number, judgment ka operative part, aur latest status (appealed/reviewed).</div>
"""},
        {"h2": "Client-side search aur lawyer-side search ka farq", "html": """
<p>Pakistan mein "property" aur "divorce" jaise client queries ki tadaad lawyer ki research queries se bhi zyada hai. Magar un topics par content likhte waqt yaad rakhein: <b>case outcome guarantee karna, client ke naam/facts share karna, aur "best lawyer" type dawe</b> Bar Council rules aur professional ethics ke khilaf hain. Hum sirf <b>legal information</b> dete hain.</p>
"""},
    ],
    "faqs": [
        ("Kya WakeelSaathi case law download deta hai?", "Hum judgments reproduce nahi karte. Har page research method, statutory framework aur verification checklist deta hai, aur official source ke links deta hai jahan se aap original judgment parh sakte hain."),
        ("Pakistan mein case law free mein kahan milta hai?", "Supreme Court aur High Courts ki official websites par judgments free milte hain. PLD/SCMR jaise reporters subscription par hote hain. Kayi free portals bhi citation search dete hain — har source ki authenticity khud check karein."),
        ("AI se case law research karna theek hai?", "Tool ke taur par theek hai, authority ke taur par nahi. AI first draft aur direction de sakta hai, magar har citation original judgment se verify karna lawyer ki zimmedari hai."),
    ],
}

PAGES = [
    # ---------------- 1. LAW-GAT ----------------
    {
        "slug": "career/law-gat/index.html",
        "url": "career/law-gat/",
        "title": "Law-GAT 2026: Test Date, Syllabus, Past Papers & Result",
        "h1": "Law-GAT 2026 — Pakistan ka Law Graduate Assessment Test",
        "desc": "Law-GAT kya hai, kaun de sakta hai, test date aur registration, syllabus, past papers, result aur answer key kahan se check karein. Naye law graduates ke liye mukammal guide.",
        "kicker": "Career · Entry",
        "lede": "LLB ke baad sanad ka pehla darwaza: <b>Law-GAT</b>. Har saal hazaron graduates isi test ke intezaar mein hote hain — aur sab se zyada search bhi yahi hoti hai.",
        "sections": [
            {"h2": "Law-GAT kya hai?", "html": """
<p><b>Law-GAT</b> (Law Graduate Assessment Test) ek assessment test hai jo <b>Higher Education Commission (HEC)</b> Pakistan Bar Council ke saath mil kar leta hai. Iska maqsad ye check karna hai ke law graduate ke paas practice ke liye bunyadi legal knowledge hai ya nahi.</p>
<p>Pakistan Bar Council ke rules ke mutabiq advocate enroll hone ke liye law degree ke saath prescribed test pass karna zaroori hai. Test generally saal mein do baar hota hai — magar <b>exact dates, fees aur registration window har cycle mein badalte hain</b>.</p>
<div class="callout"><b>Sab se pehle ye karein:</b> HEC ki official website par current Law-GAT notification dekhein. Kisi bhi WhatsApp forward ya blog ki date par bharosa na karein — including is page par.</div>
"""},
            {"h2": "Eligibility — kaun apply kar sakta hai", "html": """
<ul>
<li>Recognized university se <b>LLB</b> (ya equivalent, jo Pakistan Bar Council ne recognize kiya ho)</li>
<li>Final year ke students bhi aksar apply karte hain — <b>current notification check karein</b></li>
<li>CNIC / identity documents aur degree/transcript ki details</li>
<li>Prescribed test fee — bank challan ya online (cycle ke hisaab se)</li>
</ul>
<p class="mini">Foreign degree holders ke liye HEC/PBC ki equivalence requirement alag hoti hai — pehle wo process complete karein.</p>
"""},
            {"h2": "Syllabus — kis cheez par focus karein", "html": """
<p>Law-GAT aam taur par <b>multiple choice questions</b> par mabni hota hai aur bunyadi legal subjects cover karta hai. Aam taur par in areas par focus hota hai (current syllabus HEC se confirm karein):</p>
<table class="tbl">
<thead><tr><th>Area</th><th>Kya revise karein</th></tr></thead>
<tbody>
<tr><td>Constitutional law</td><td>Fundamental rights, writ jurisdiction, key constitutional provisions</td></tr>
<tr><td>Criminal law</td><td>PPC ke bunyadi sections, qatl/hurt/property offences, CrPC procedure</td></tr>
<tr><td>Civil law</td><td>CPC (plaint, jurisdiction, appeals), Contract Act, Specific Relief</td></tr>
<tr><td>Evidence</td><td>Qanun-e-Shahadat 1984 — relevancy, burden of proof, documentary evidence</td></tr>
<tr><td>Family &amp; personal law</td><td>MFLO 1961, dissolution of marriage, custody, maintenance</td></tr>
<tr><td>Legal English</td><td>Comprehension, legal terms, drafting basics</td></tr>
</tbody>
</table>
"""},
            {"h2": "60-din ka study plan", "html": """
<ol class="steps">
<li><b>Din 1–10:</b> Bare acts parhein — PPC, CrPC, CPC ke key sections. Notes flashcards mein banayein.</li>
<li><b>Din 11–25:</b> Subject-wise MCQs. Har ghalti ka <b>reason</b> likhein, sirf answer nahi.</li>
<li><b>Din 26–40:</b> Past papers (timed). Weak areas ki list banayein.</li>
<li><b>Din 41–52:</b> Weak areas + Qanun-e-Shahadat aur family law par focus.</li>
<li><b>Din 53–60:</b> Sirf revision + full-length mocks. Naya material nahi.</li>
</ol>
"""},
            {"h2": "Result aur answer key kahan check karein", "html": """
<p>Result aur answer key <b>sirf HEC ki official website/portal</b> se check karein. Result ke din traffic bohat zyada hota hai — page slow ho to official portal par thori der baad try karein. Roll number / CNIC required hota hai.</p>
<p class="mini">⚠️ Result declare hone se pehle kisi "leaked result" link par click na karein — ye phishing ka aam tareeqa hai.</p>
"""},
            {"h2": "Test pass karne ke baad kya?", "html": """
<p>Law-GAT pass karne ke baad aap <b>provincial bar council</b> (Sindh mein Sindh Bar Council) mein advocate enrollment ke liye apply karte hain, jismein <b>senior advocate ke chamber mein pupillage</b> shamil hai. Us ka poora step-by-step plan hamare <a href="../bar-council-enrollment/index.html">Bar Council enrollment guide</a> mein hai.</p>
"""},
        ],
        "faqs": [
            ("Law-GAT kitni baar hota hai?", "Aam taur par saal mein do baar, magar exact schedule HEC har cycle mein notify karta hai. Current dates HEC ki official website se confirm karein."),
            ("Kya Law-GAT ke bina advocate ban sakte hain?", "Pakistan Bar Council ke rules ke mutabiq enrollment ke liye prescribed test pass karna zaroori hai. Apni province ke bar council ki current requirement confirm karein."),
            ("Law-GAT fail ho jaye to kya karein?", "Aam taur par next cycle mein dobara appear ho sakta hai. Beech ke waqt mein drafting, research aur chamber internship par kaam karein — next attempt aur pupillage dono ke liye faida hoga."),
            ("Law-GAT ka result kab aata hai?", "Result ka waqt HEC ke notification se maloom hota hai. Sirf official portal par check karein."),
        ],
        "related": [("Bar Council enrollment guide", "career/bar-council-enrollment/index.html"),
                    ("Lawyer salary in Pakistan", "career/lawyer-salary-pakistan/index.html"),
                    ("High Court license kaise milega", "career/high-court-license/index.html")],
    },

    # ---------------- 2. 302 PPC ----------------
    {
        "slug": "case-law/302-ppc/index.html",
        "url": "case-law/302-ppc/",
        "title": "302 PPC Case Law in Pakistan (Urdu Guide) | Section 302",
        "h1": "302 PPC Case Law — Qatl-i-amd (Pakistan)",
        "desc": "Section 302 PPC qatl-i-amd: punishment, elements, qisas aur waiver, aur 302 case law Pakistan mein kaise research karein — Urdu guide with verification checklist.",
        "kicker": "Case law · Criminal",
        "lede": "<b>302 PPC</b> Pakistan Penal Code ka sab se ahem aur sab se zyada research kiya jane wala section: <b>qatl-i-amd</b> (intentional murder) ki saza.",
        "sections": [
            {"h2": "Section 302 PPC — statutory framework", "html": """
<p>Pakistan Penal Code 1860 ke <b>Chapter XVI</b> (Offences affecting the human body) mein qatl ke offences hain. <b>Section 300</b> qatl-i-amd ki definition aur exceptions deta hai, <b>Section 301</b> qatl-i-amd ke case mein saza ka taayun karta hai jab maqsool shakhs ke ilawa koi aur marta hai, aur <b>Section 302</b> qatl-i-amd ki saza bayan karta hai.</p>
<p>302 ke mutabiq saza in sooraton mein di jati hai (bare act ka exact text zaroor parhein):</p>
<ul>
<li><b>Death as qisas</b> — jahan qisas ka raasta kushada ho</li>
<li><b>Imprisonment for life</b> — jahan qisas maaf ho jaye ya na ho</li>
<li>Ya <b>imprisonment</b> ek muddat tak, jo qanoon mein di gayi hai</li>
</ul>
<p class="mini">Saza ka taayun bohat had tak <b>qisas</b> ke system par depend karta hai — Section 299 (definitions), 305 (proof of qisas), 306 (waiver), 308 (alternate), 309/310 (compounding) isi chain ka hissa hain. Ye sab bare act se parhein.</p>
"""},
            {"h2": "Research ke liye issue map", "html": """
<p>302 ke case mein court aam taur par in questions par likhta hai — inhe issues ki tarah le kar authorities dhoondein:</p>
<table class="tbl">
<thead><tr><th>Issue</th><th>Kya dekhein</th></tr></thead>
<tbody>
<tr><td>Qatl-i-amd ya qatl-i-khata?</td><td>Niyat, weapon, injury ka maqam, medical evidence</td></tr>
<tr><td>Zaroori elements ka proof</td><td>Mens rea, actus reus, causation, medical/official evidence</td></tr>
<tr><td>Qisas ki eligibility</td><td>Heirs, waiver, compounding (sections 305–310)</td></tr>
<tr><td>Alternative conviction</td><td>Record se 302 ke bajaye kam section (304/308/337) ban sakta hai ya nahi</td></tr>
<tr><td>Evidence ki qadr</td><td>Ocular evidence, delay in FIR, identification, recovery</td></tr>
</tbody>
</table>
"""},
            {"h2": "Pakistan mein 302 case law kaise search karein", "html": """
<ol class="steps">
<li>Supreme Court / High Court portal par judgment text search karein — keywords: "302 PPC", "qatl-i-amd", "qisas", "waiver", "304 PPC", "benefit of doubt".</li>
<li>PLD, SCMR, YLR jaise reporters mein <b>headnote</b> se shuru karein, phir judgment ka operative part parhein.</li>
<li>Har authority ka <b>latest status</b> check karein — shayad larger bench ne review kar diya ho.</li>
<li>Apne High Court (Karachi ke liye Sindh High Court) ki binding precedents pehle chunein.</li>
</ol>
<div class="callout"><b>Warning:</b> Kisi bhi case citation ko bina original judgment dekhe file mein na lagayein. AI tools citation bana sakte hain — galat citation court mein sab se bara nuqsan hai.</div>
"""},
            {"h2": "Urdu mein research note kaise banayein", "html": """
<p>Bohat seniors Urdu mein note maangte hain. Structure ye rakhein: <b>facts ek para → issues numbered → har issue par authority (ek line ratio) → apna point → conclusion</b>. Har authority ke saath citation aur paragraph number likhein taake court mein reference di ja sake.</p>
"""},
        ],
        "faqs": [
            ("302 PPC ki saza kya hai?", "Section 302 qatl-i-amd ke liye death as qisas, imprisonment for life, ya qanoon mein di gayi muddat tak imprisonment ki saza bayan karta hai. Exact wording aur qisas ke rules ke liye bare act (sections 299–310) parhein aur latest precedent dekhein."),
            ("Kya 302 mein qisas maaf ho sakti hai?", "Qisas ka system sections 305 se 310 tak regulate hota hai, jismein waiver aur compounding shamil hain. Is surat mein saza badal sakti hai — apne facts par latest authority zaroor check karein."),
            ("302 case law Urdu mein kahan milega?", "Judgments ka original text English mein hota hai. Urdu guides aur summaries milti hain, magar court mein cite karne ke liye original judgment hi use karein. Official court websites free search deti hain."),
            ("302 aur 324 mein kya farq hai?", "302 qatl-i-amd (murder) ki saza ka section hai, jab ke 324 attempt to commit qatl (ya qatl ki koshish) se mutalliq hai. Dono bare act se parh kar elements compare karein."),
        ],
        "related": [("497 CrPC bail case law", "case-law/497-crpc/index.html"),
                    ("Bail application format", "drafts/bail-application-format/index.html"),
                    ("Case law hub", "case-law/index.html")],
    },

    # ---------------- 3. BAIL APPLICATION ----------------
    {
        "slug": "drafts/bail-application-format/index.html",
        "url": "drafts/bail-application-format/",
        "title": "Bail Application Format in Pakistan (PDF & Word Guide)",
        "h1": "Bail Application Format — Pakistan",
        "desc": "Bail application ka format Pakistan mein: 496, 497, 498 CrPC ke farq, application ka structure, grounds, aur common mistakes — junior lawyer ke liye practical guide.",
        "kicker": "Drafts · Criminal",
        "lede": "Bail application wo pehli drafting hai jo har junior lawyer se maangi jati hai. Format ration se nahi aata — <b>structure aur grounds</b> se aata hai.",
        "sections": [
            {"h2": "Pehle section samjhein — bailable, non-bailable, aur konsa bail?", "html": """
<table class="tbl">
<thead><tr><th>Section</th><th>Kis surat mein</th></tr></thead>
<tbody>
<tr><td>496 CrPC</td><td>Bailable offence mein bail (aam taur par as of right)</td></tr>
<tr><td>497 CrPC</td><td>Non-bailable offence mein bail — court ki discretion, aur kuch cases mein special rules</td></tr>
<tr><td>498 CrPC</td><td>Sessions Court / High Court ko bail ka power</td></tr>
<tr><td>491 CrPC</td><td>Illegal detention ke khilaf (habeas corpus)</td></tr>
<tr><td>426 CrPC</td><td>Conviction ke baad appeal mein suspension of sentence/bail</td></tr>
</tbody>
</table>
<p class="mini">Pehle FIR ke sections dekhein aur tay karein ke offence bailable hai ya non-bailable — ghalat section par application dene se waqt zaya hota hai.</p>
"""},
            {"h2": "Application ka standard structure", "html": """
<ol class="steps">
<li><b>Heading:</b> Court ka naam, case number/FIR number, police station, section(s), aur parties.</li>
<li><b>Title:</b> "Application for grant of bail under section ___ CrPC on behalf of the accused".</li>
<li><b>Brief facts:</b> 4–6 lines — FIR version, accused ka role, arrest ki date, custody ki muddat.</li>
<li><b>Grounds:</b> numbered — har ground ek separate legal point.</li>
<li><b>Legal basis:</b> sirf wahi sections/authorities jo aap ne khud verify kiye hain.</li>
<li><b>Prayer:</b> clear — "accused ko bail par release kiya jaye" + conditions.</li>
<li><b>Verification + affidavit + vakalatnama</b> attached.</li>
</ol>
"""},
            {"h2": "Grounds jo court sunta hai (facts ke saath, sirf dawa nahi)", "html": """
<ul>
<li><b>Investigation mukammal</b> — accused se mazeed recovery/pur-tashaddud ki zaroorat nahi</li>
<li><b>Bail ke baad farar ka koi asar</b> nahi — roots in society, permanent address, family</li>
<li><b>Evidence kamzor ya sirf suspicion</b> — record se uthaye gaye sample points</li>
<li><b>Delay in FIR / delay in arrest</b> — dates ke saath</li>
<li><b>Co-accused ko bail mil chuki hai</b> — parity, judgment ka reference</li>
<li><b>Medical / age / health</b> — documented grounds</li>
<li><b>Remand aur custody ki muddat</b> — trial mein deri</li>
</ul>
<div class="callout"><b>Practice tip:</b> Grounds ko <b>facts</b> se bandhein: "accused 3 din se custody mein hai, challan pesh ho chuka hai, record par koi recovery nahi" — aisi lines court zyada sunti hain.</div>
"""},
            {"h2": "Common mistakes jo application kamzor karti hain", "html": """
<ul>
<li>Bail aur "acquittal" ki baat mix karna — bail ka maqsad trial ke doran release hai, bari nahi.</li>
<li>Grounds mein poori FIR dobara likhna (justice ke liye facts ka summary kaafi hai).</li>
<li>Bina verified authority cite karna.</li>
<li>Prayer vague chhorna — court ko exactly batayein kya chahiye.</li>
<li>Court fee/stamp aur annexures ka adhoora set.</li>
</ul>
"""},
            {"h2": "Court fee, stamp aur annexures", "html": """
<p>Court fee aur stamp paper ki zaroorat <b>court aur case ki qism</b> ke hisaab se badalti hai. Mutaliqa court ke filing branch se current requirement confirm karein — aur application ki copies (court + opponent) tayyar rakhein.</p>
"""},
        ],
        "faqs": [
            ("Bail application format Pakistan mein kahan milega?", "Har court ka apna practice hota hai. Neeche wahi structure use karein jo courts accept karte hain: heading, facts, numbered grounds, prayer, verification. WakeelSaathi par AI Kit se pehla draft ban sakta hai — final draft hamesha apni review se."),
            ("Bail application Urdu mein likh sakte hain?", "Aam taur par applications English mein likhi jati hain, magar kuch courts/Urdu ki ijazat dete hain. Apne court ke practice ke mutabiq chalein. Aam aadmi ko samjhane ke liye Urdu summary alag se dein."),
            ("497 aur 498 CrPC mein kya farq hai?", "497 non-bailable offences mein trial court ke bail ka framework deta hai; 498 Sessions Court aur High Court ko bail ke powers deta hai. Aap ki application ka authority depends karta hai ke aap kis court mein ja rahe hain."),
            ("Bail ki application reject ho jaye to kya karein?", "Record par reasons dekhein, grounds ko facts ke saath mazboot karein, aur appellate forum (Sessions/High Court) ka raasta dekhein. Har step par limitation aur procedure verify karein."),
        ],
        "related": [("497 CrPC case law", "case-law/497-crpc/index.html"),
                    ("Legal notice format", "drafts/legal-notice-format/index.html"),
                    ("302 PPC case law", "case-law/302-ppc/index.html")],
    },

    # ---------------- 4. LEGAL NOTICE ----------------
    {
        "slug": "drafts/legal-notice-format/index.html",
        "url": "drafts/legal-notice-format/",
        "title": "Legal Notice Format in Pakistan (Recovery, Cheque, Rent)",
        "h1": "Legal Notice Format — Pakistan",
        "desc": "Legal notice format Pakistan mein: recovery of money, cheque dishonour aur rent ke notices ka structure, 15-din ka rule, delivery proof aur common mistakes.",
        "kicker": "Drafts · Civil",
        "lede": "Legal notice case ka pehla marhala hai — aur bohat dafa pura case <b>notice par hi hal</b> ho jata hai. Format se zyada matter us ke andar ka precision karta hai.",
        "sections": [
            {"h2": "Legal notice kab bhejni chahiye", "html": """
<ul>
<li><b>Recovery of money</b> — udhaar, invoice, services ka payment</li>
<li><b>Cheque dishonour</b> — 489-F PPC ka raasta (complaint se pehle notice dena practice hai)</li>
<li><b>Rent / eviction</b> — Sindh Rented Premises Ordinance ke under procedure</li>
<li><b>Contract breach</b> — performance ka demand ya termination</li>
<li><b>Property / possession</b> — illegal dispossession ki warning</li>
<li><b>Defamation</b> — retraction ka demand</li>
</ul>
"""},
            {"h2": "Notice ka standard structure", "html": """
<ol class="steps">
<li><b>Letterhead + date + reference number</b></li>
<li><b>Addressee</b> — poora naam aur mukammal pata (registered address best)</li>
<li><b>Subject line:</b> "Legal notice for recovery of Rs ___" — seedha aur specific</li>
<li><b>Chronology:</b> dates ke saath facts — agreement kab hua, kya diya, kya baqi hai</li>
<li><b>Default ya breach:</b> kya ghalat hua aur kaunsa clause/section</li>
<li><b>Demand:</b> exact amount, ya exact action, aur <b>reasonable time</b> (aam taur par 15 din)</li>
<li><b>Consequence:</b> "is ke bawajood adaigi na hui to qanooni karrawai hogi, jiske tamam kharchay aap par honge"</li>
<li><b>Reservation of rights</b> — aage mazeed legal action ka haq mehfooz</li>
<li><b>Signature + advocate ki details</b></li>
</ol>
"""},
            {"h2": "Delivery proof — notice ka sab se ahem hissa", "html": """
<p>Court mein notice ka sab se bara sawal hota hai: <b>"bheja gaya ya nahi?"</b> Is liye:</p>
<ul>
<li><b>Registered post with acknowledgement due (AD)</b> — receipt aur AD card sambhal ke rakhein</li>
<li><b>Courier</b> — tracking + delivery slip, company ka letterhead</li>
<li><b>Email/WhatsApp</b> — sirf tab jab contract mein allowed ho; screenshot + sent confirmation</li>
<li><b>Notice ki copy</b> apni file mein, dispatch proof ke saath</li>
</ul>
<div class="callout"><b>Note:</b> Notice par likhi hui date aur dispatch ki date alag hoti hai. Court dono dekhti hai.</div>
"""},
            {"h2": "15 din ka rule — aur kya galat samajha jata hai", "html": """
<p>Har notice mein 15 din lazmi nahi hota — ye <b>case ki qism aur qanoon</b> par depend karta hai (maslan kuch statutory notices ke liye makhsoos muddat hoti hai, jaise sarkari idaron ke khilaf suits mein). <b>Reasonable time</b> dena aam practice hai, magar section-specific requirement bare act se check karein.</p>
"""},
            {"h2": "Common mistakes", "html": """
<ul>
<li>Amount ke figures aur words mein farq</li>
<li>Ghalat addressee ya purana pata → notice "serve" nahi hota</li>
<li>Facts mein koi date ghalat → opponent ka pehla attack</li>
<li>Demand vague ("qanooni karrawai") bina amount/action ke</li>
<li>Threat ya dhamki ki zaban — professional tone rakhein</li>
</ul>
"""},
        ],
        "faqs": [
            ("Legal notice ka format Pakistan mein kya hota hai?", "Structure: letterhead, date, addressee ka mukammal pata, subject line, dates ke saath facts, default/breach, clear demand, time period, consequence, reservation of rights, aur signature. Ye format courts aur opponents dono ke liye clear hota hai."),
            ("Legal notice bhejne ki koi fee hoti hai?", "Koi sarkari fee nahi hoti. Kharcha advocate ki professional fee aur registered post/courier ka hota hai. Court fee sirf suit/complaint file karne par lagti hai."),
            ("Kya WhatsApp par legal notice bhej sakte hain?", "Aam taur par registered post/courier reliable hota hai. WhatsApp/email sirf tab jab contract ya law mein allowed ho, aur proof (screenshot + delivery confirmation) save ho."),
            ("Cheque bounce case mein notice zaroori hai?", "489-F PPC ke complaint mein notice dene ki practice aur facts par depend karta hai. Apni facts par court ka latest approach aur section ka text check karein, aur proof of delivery rakhein."),
        ],
        "related": [("Cheque dishonour 489-F case law", "case-law/489-f/index.html"),
                    ("Plaint format", "drafts/plaint-format/index.html"),
                    ("Bail application format", "drafts/bail-application-format/index.html")],
    },

    # ---------------- 5. BAR COUNCIL ENROLLMENT ----------------
    {
        "slug": "career/bar-council-enrollment/index.html",
        "url": "career/bar-council-enrollment/",
        "title": "Bar Council Enrollment in Pakistan — Step by Step Guide 2026",
        "h1": "Bar Council Enrollment — Sanad ka poora raasta",
        "desc": "Advocate enrollment kaise hota hai: eligibility, documents, 6 mahine ki pupillage, fees, enrollment number check, aur Sindh Bar Council ka process — step by step.",
        "kicker": "Career · Licensing",
        "lede": "Law degree aur sanad ke darmiyan jo process hai, wo kisi ne aap ko theek se nahi bataya. Yahan poora raasta hai — <b>documents se verification tak</b>.",
        "sections": [
            {"h2": "Eligibility (Legal Practitioners &amp; Bar Councils Act, 1973)", "html": """
<ul>
<li>Pakistan (ya AJK) ka shehri</li>
<li>Kam az kam <b>21 saal</b> ki umar</li>
<li>Pakistan Bar Council se recognized <b>LLB ya Bar-at-Law</b></li>
<li>Prescribed <b>test</b> (Law-GAT) pass — PBC rules ke mutabiq</li>
<li>Character/fitness requirements aur koi disqualification na hona (Act ke sections 26 &amp; 27)</li>
</ul>
<p class="mini">Foreign degree walon ke liye PBC/HEC ki equivalence alag process hai — pehle wo complete karein.</p>
"""},
            {"h2": "Step-by-step process", "html": """
<ol class="steps">
<li><b>Law-GAT</b> — pass karein (dekhein <a href="../law-gat/index.html">Law-GAT guide</a>).</li>
<li><b>Senior advocate ka chamber</b> — <b>6 mahine ki pupillage</b> prescribed hai, generally 10 saal standing wale senior ke saath.</li>
<li><b>Documents tayyar karein</b> — LLB degree + transcripts, CNIC, photographs, character certificate, test result, aur prescribed forms.</li>
<li><b>Provincial bar council</b> (Sindh mein Sindh Bar Council) ko application — fees: enrollment fee bar council kay rules ke mutabiq (PBC aur provincial hissa alag), plus benevolent fund.</li>
<li><b>Enrollment Committee / interview</b> — fitness aur training ka review.</li>
<li><b>Certificate + ID card</b> — sanad aur advocate ID issue hoti hai.</li>
</ol>
<div class="callout"><b>Fees aur forms har saal update ho sakte hain.</b> Current fee, challan aur checklist bar council ke office/website se confirm karein — kisi blog ki purani list par na chalein.</div>
"""},
            {"h2": "Pupillage — jahan sab se zyada log phanste hain", "html": """
<p>Pupillage ka matlab hai kisi senior ke chamber mein baith kar case files, drafting, court appearances aur client handling seekhna. Masla ye hai ke <b>placement ka koi system nahi</b> — sab reference se hota hai.</p>
<p><b>Isay practical banayein:</b></p>
<ul>
<li>Chamber visit se pehle ek page ki CV — kya seekhna hai, kitna waqt de sakte hain, kis area mein interest hai</li>
<li>Shuru mein hi tay karein: timing, kaam ki qism, stipend (agar ho), aur kya sikhaya jayega</li>
<li>Roz ek page ka note — kaun sa case, kya hua, kya seekha (6 mahine baad ye aap ki asli degree hogi)</li>
<li>WakeelSaathi par <a href="../../index.html#mentors">Chamber Match</a> se verified chambers ki list dekh sakte hain</li>
</ul>
"""},
            {"h2": "Enrollment number check aur verification", "html": """
<p>Aap ka enrollment number aur status <b>provincial bar council ke roll</b> par hota hai. Sindh ke liye Sindh Bar Council ka advocate verification portal maujood hai jahan naam, registration number, district aur license type (LC/HC) search ho sakta hai.</p>
<p>Client ya employer verification chahe to <b>roll se cross-check</b> karein — screenshots par bharosa na karein. Ye fake lawyers aur imposters ke khilaf sab se aasaam tareeqa hai.</p>
"""},
            {"h2": "Enrollment ke baad pehle 90 din", "html": """
<ul>
<li>Apna <b>court, area aur case type</b> fix karein — sab jagah bhaagna income nahi deta</li>
<li>Apna record rakhein — har appearance, har file (High Court license ke liye practice record chahiye hoga)</li>
<li>Ek saaf profile banayein: LinkedIn + WhatsApp Business + verified listing</li>
<li>20 logon ko personally batayein — pehla case referral se aata hai, ad se nahi</li>
</ul>
"""},
        ],
        "faqs": [
            ("Advocate banne ke liye kitne saal lagte hain?", "LLB (aam taur par 5 saal) + Law-GAT + 6 mahine pupillage + enrollment process. Total aam taur par 6 saal ke qareeb. Individual timings bar council ke process par depend karti hain."),
            ("Pupillage kitne mahine ki hoti hai?", "Prescribed pupillage aam taur par 6 mahine ki hai, senior advocate ke chamber mein. Exact requirement apne provincial bar council ke current rules se confirm karein."),
            ("Kya pupillage ke doran stipend milta hai?", "Koi lazmi nahi. Kuch chambers stipend dete hain, bohat nahi dete. Isi liye shuru mein terms likh lena behtar hai. WakeelSaathi par chambers apne terms khud likhte hain."),
            ("Enrollment ke liye kitni fee lagti hai?", "Enrollment fee, benevolent fund aur other charges bar council ke rules ke mutabiq hote hain aur waqt ke saath badalte hain. Sindh Bar Council se current challan/breakdown confirm karein."),
        ],
        "related": [("Law-GAT guide", "career/law-gat/index.html"),
                    ("How to become a lawyer in Pakistan", "career/how-to-become-lawyer-pakistan/index.html"),
                    ("Lawyer salary in Pakistan", "career/lawyer-salary-pakistan/index.html")],
    },

    # ---------------- 6. LAWYER SALARY ----------------
    {
        "slug": "career/lawyer-salary-pakistan/index.html",
        "url": "career/lawyer-salary-pakistan/",
        "title": "Lawyer Salary in Pakistan 2026 — Junior, Mid, Senior",
        "h1": "Lawyer Salary in Pakistan (2026)",
        "desc": "Pakistan mein lawyer ki salary: fresh graduate, junior associate, litigation chamber, corporate firm aur independent practice ke realistic ranges. Sindh minimum wage se comparison.",
        "kicker": "Career · Money",
        "lede": "Sab se zyada poocha jane wala sawal, aur sab se zyada jhoot bola jane wala jawab. Yahan <b>realistic numbers</b> hain — aur woh wajah jis ki bina par ye numbers aise hain.",
        "sections": [
            {"h2": "Realistic ranges (2026)", "html": """
<table class="tbl">
<thead><tr><th>Stage</th><th>Typical monthly (PKR)</th><th>Note</th></tr></thead>
<tbody>
<tr><td>Internship / pupillage</td><td>0 – 25,000</td><td>Bohat chambers mein zero; kuch mein stipend</td></tr>
<tr><td>Fresh associate (litigation chamber)</td><td>25,000 – 50,000</td><td>Karachi/Lahore mein upper end</td></tr>
<tr><td>Corporate law firm associate</td><td>50,000 – 120,000+</td><td>Top firms zyada, working hours bhi zyada</td></tr>
<tr><td>Mid-level (3–7 saal)</td><td>80,000 – 250,000</td><td>Firm type aur client base par depend</td></tr>
<tr><td>Independent practice</td><td>Variable</td><td>Fee per case; pehle saal bohat kam, phir reputation se barhta hai</td></tr>
</tbody>
</table>
<p class="mini">Numbers indicative hain — city, firm, practice area aur aap ki negotiation par depend karte hain. Source: public salary discussions, industry reporting aur market observation (2023–2026).</p>
"""},
            {"h2": "Sindh minimum wage se comparison — asli tasveer", "html": """
<p>Sindh mein unskilled worker ka minimum wage <b>Rs 43,000</b> (2026-27) hai. Yani ek <b>5 saal padha hua law graduate</b> aksar us se kam par kaam kar raha hota hai — aur kai jagah "salary" ke bajaye "<b>stipend</b>" keh kar minimum wage law ko bypass kiya jata hai.</p>
<div class="callout"><b>Apne haq janу:</b> Chamber terms likhwaayein. “Aap seekh rahe hain” ka matlab ye nahi ke kuch bhi na mile — kam az kam transport/kharcha aur clear learning scope tay karein.</div>
"""},
            {"h2": "Salary kam kyun hoti hai (structural wajah)", "html": """
<ul>
<li><b>Lump-sum per-case fee:</b> Pakistan mein hourly billing aam nahi. Senior ke liye junior ka waqt "revenue" nahi, "cost" hota hai.</li>
<li><b>Training period:</b> Fresh graduate ko productive hone mein aam taur par 1–2 saal lagte hain.</li>
<li><b>Retention:</b> Juniors 1–2 saal mein chale jate hain, is liye firms invest karne se katraate hain.</li>
<li><b>Supply:</b> Har saal hazaron graduates, magar paid seats kam.</li>
</ul>
"""},
            {"h2": "Income barhane ke 5 practical raaste", "html": """
<ol class="steps">
<li><b>Ek practice area mein specialise</b> — "sab kuch" karne wale ki koi rate nahi hoti.</li>
<li><b>Court-specific mastery</b> — ek court, us ki practice, us ke judges ki expectations.</li>
<li><b>Remote legal work</b> — foreign firms ke liye drafting/research (Upwork, direct clients). Rates USD mein.</li>
<li><b>Content + visibility</b> — jo wakeel online samajh aata hai, us ke paas referral aata hai (rules ke andar rehte hue).</li>
<li><b>Kaam Board</b> — khali waqt mein seniors ka overflow drafting/research kaam.</li>
</ol>
"""},
            {"h2": "Negotiation script (jo kaam karti hai)", "html": """
<p><b>Interview/chamber meeting mein:</b> "Sir, main 6 mahine aap ke saath serious commitment kar raha hoon. Main drafting, research aur court appearance par kaam karna chahta hoon. Iske liye minimum monthly ___ aur hafte mein ek din study/CPD ka rakh sakte hain?"</p>
<p>Specific demand + specific commitment = serious candidate. Sirf "kitna milega?" poochne wala candidate replace ho jata hai.</p>
"""},
        ],
        "faqs": [
            ("Fresh lawyer ki salary Pakistan mein kitni hoti hai?", "Aam taur par Rs 25,000–50,000 per month, city aur firm par depend. Bohat chambers mein pupillage ke doran stipend zero bhi hota hai. Corporate firms mein range zyada hoti hai."),
            ("Kya lawyer ki salary minimum wage se kam ho sakti hai?", "Legal position aur employment classification par depend karta hai — bohat chambers juniors ko “trainee/stipend” treat karte hain. Apni situation ke liye kisi labour/employment lawyer se proper advice lein."),
            ("Independent practice mein kitna milta hai?", "Koi fixed jawab nahi. Pehle 1–2 saal aksar bohat kam, phir reputation aur case flow ke saath barhta hai. Kai wakeel side income (teaching, drafting, freelance) se guzara karte hain."),
            ("Corporate aur litigation salary mein farq kyun hai?", "Corporate firms hourly/retainer billing aur international clients par chalte hain, is liye associate ki value measurable hoti hai. Litigation mein lump-sum per-case fee model hai."),
        ],
        "related": [("Lawyer jobs in Karachi", "karachi/lawyer-jobs/index.html"),
                    ("How to become a lawyer", "career/how-to-become-lawyer-pakistan/index.html"),
                    ("Room for rent for lawyers", "karachi/lawyer-room-for-rent/index.html")],
    },

    # ---------------- 7. HOW TO BECOME A LAWYER ----------------
    {
        "slug": "career/how-to-become-lawyer-pakistan/index.html",
        "url": "career/how-to-become-lawyer-pakistan/",
        "title": "How to Become a Lawyer in Pakistan (After 12th) — 2026 Guide",
        "h1": "How to Become a Lawyer in Pakistan",
        "desc": "12th ke baad lawyer kaise banein: LLB admission, Law-GAT, pupillage, bar council enrollment, High Court license — poora roadmap timeline ke saath.",
        "kicker": "Career · Roadmap",
        "lede": "School/college se Supreme Court tak — poora raasta, kis stage par kya chahiye, aur kahan log waqt zaya karte hain.",
        "sections": [
            {"h2": "Poora roadmap ek nazar mein", "html": """
<table class="tbl">
<thead><tr><th>Stage</th><th>Kya chahiye</th><th>Waqt</th></tr></thead>
<tbody>
<tr><td>1. LLB</td><td>12th/intermediate + recognized university ka admission test</td><td>5 saal (ya 3 saal after BA)</td></tr>
<tr><td>2. Law-GAT</td><td>LLB + HEC notification ke mutabiq registration</td><td>Cycle ke hisaab se</td></tr>
<tr><td>3. Pupillage</td><td>Senior advocate (aam taur par 10+ saal standing) ka chamber</td><td>6 mahine (prescribed)</td></tr>
<tr><td>4. Enrollment</td><td>Documents + fees + committee review</td><td>Kuch mahine</td></tr>
<tr><td>5. Lower court practice</td><td>Sanad + court work</td><td>2 saal</td></tr>
<tr><td>6. High Court license</td><td>2 saal practice + application + fitness</td><td>—</td></tr>
<tr><td>7. Supreme Court</td><td>HC advocate ke taur par 7 saal practice</td><td>—</td></tr>
</tbody>
</table>
"""},
            {"h2": "12th ke baad: LLB admission", "html": """
<ul>
<li><b>Universities:</b> Karachi mein Karachi University, S.M. Law College, Hamdard, Iqra, SZABIST, Bahria, aur bohat se private law colleges. HEC/PBC recognized hona lazmi hai.</li>
<li><b>Duration:</b> 5 saal ka LLB programme (HEC ke revised curriculum ke mutabiq internship bhi shamil hai).</li>
<li><b>Fees:</b> Government colleges sasti, private universities bohat mehngi — 5 saal ka total lakhon mein.</li>
<li><b>Degree se pehle:</b> Ho sakta hai to ek internship zaroor karein — ye aap ka faisla badal sakta hai.</li>
</ul>
"""},
            {"h2": "Law school mein kya karein jo baad mein kaam aaye", "html": """
<ol class="steps">
<li><b>Teen mukhtalif internships</b> — trial court chamber, law firm, aur in-house legal department.</li>
<li><b>Drafting likhna seekhein</b> — photocopy se copy nahi. Har hafte ek draft: plaint, written statement, bail, notice.</li>
<li><b>Moot court</b> — do moots, serious wale. Oral advocacy ka confidence yahan banta hai.</li>
<li><b>Legal English</b> — roz 20 minute ek judgment + 5-line summary.</li>
<li><b>Ek practice area pehchannein</b> — interest + market demand dono dekhein.</li>
</ol>
"""},
            {"h2": "Kahan log sab se zyada waqt zaya karte hain", "html": """
<ul>
<li><b>Sirf padhai, zero internship</b> — degree mil jati hai, kaam karna nahi aata</li>
<li><b>Sirf "connections" par bharosa</b> — network zaroori hai, magar skill ke baghair network bhi kaam nahi karta</li>
<li><b>Har practice area ek saath</b> — 3 saal baad bhi koi pehchaan nahi banti</li>
<li><b>Documents ka adhoora set</b> — enrollment mein mahine zaya</li>
</ul>
"""},
            {"h2": "Law ke baghair bhi legal career?", "html": """
<p>Haan: paralegal, legal researcher, court clerk (munshi) ka kaam, legal content writing, compliance, aur legal tech. Ye entry points hain — kuch log inhi se LLB karte hain, kuch inhi mein aa jate hain. Magar advocate ka darja sirf LLB + enrollment se milta hai.</p>
"""},
        ],
        "faqs": [
            ("12th ke baad lawyer banne mein kitne saal lagte hain?", "5 saal LLB + Law-GAT + 6 mahine pupillage + enrollment process — total aam taur par 6 saal ke qareeb, individual timings par depend."),
            ("Kya 10th ke baad lawyer ban sakte hain?", "Nahi. Advocate banne ke liye 12th/intermediate ke baad LLB degree zaroori hai. 10th ke baad aap entry-level legal support roles (office assistant, file clerk) mein ja sakte hain."),
            ("Kya lawyer banne ke liye Urdu medium se ho sakta hai?", "Degree English medium mein hoti hai, is liye legal English par kaam karna padega. Urdu medium walay bohat se wakeel kamyab hain — magar drafting aur reading English mein karni hoti hai."),
            ("Lawyer ki starting salary kitni hoti hai?", "Rs 25,000–50,000 per month aam range hai, city aur firm par depend. Corporate firms zyada dete hain."),
        ],
        "related": [("Bar Council enrollment", "career/bar-council-enrollment/index.html"),
                    ("Law-GAT guide", "career/law-gat/index.html"),
                    ("Lawyer salary in Pakistan", "career/lawyer-salary-pakistan/index.html")],
    },

    # ---------------- 8. LAWYER JOBS KARACHI ----------------
    {
        "slug": "karachi/lawyer-jobs/index.html",
        "url": "karachi/lawyer-jobs/",
        "title": "Lawyer Jobs in Karachi — Chamber, Firm & In-House 2026",
        "h1": "Lawyer Jobs in Karachi",
        "desc": "Karachi mein lawyer jobs: chambers, law firms, corporate in-house, legal freelancing aur internship. Kahan apply karein, CV kaise banayein, aur salary expectations.",
        "kicker": "Karachi · Jobs",
        "lede": "Karachi mein “lawyer jobs” ki search har mahine chalti hai — magar sab se zyada kaam <b>un jobs</b> ka hota hai jo advertise hi nahi hotin.",
        "sections": [
            {"h2": "Job ki 6 qismein", "html": """
<table class="tbl">
<thead><tr><th>Type</th><th>Kya karna hota hai</th><th>Kahan</th></tr></thead>
<tbody>
<tr><td>Chamber associate / pupil</td><td>Drafting, research, court appearances senior ke saath</td><td>City Courts, Sindh High Court vicinity chambers</td></tr>
<tr><td>Law firm associate</td><td>Corporate, tax, disputes, transaction side</td><td>Karachi ke commercial areas</td></tr>
<tr><td>In-house legal</td><td>Contracts, compliance, litigation management</td><td>Banks, telecom, FMCG, IT companies</td></tr>
<tr><td>Government / public sector</td><td>Prosecution, AG office, legal drafting units</td><td>Provincial aur federal departments</td></tr>
<tr><td>Court research assistant</td><td>Judges ke liye research aur drafting</td><td>High Court / Supreme Court registries</td></tr>
<tr><td>Freelance / remote</td><td>Drafting, research, document review (foreign clients)</td><td>Ghar se — Upwork etc.</td></tr>
</tbody>
</table>
"""},
            {"h2": "Hidden job market — asli mauqay kahan hain", "html": """
<p>Karachi mein aam taur par 70–80% chamber positions <b>advertise nahi</b> hotin. Wo aise milti hain:</p>
<ul>
<li>Senior ya classmate jo aap ko jaanta hai</li>
<li>Chamber visit — CV haath mein le kar (email se zyada kaam karta hai)</li>
<li>Court ke deewar/electric pole par lagay chhote notices, aur bar room ki notice board</li>
<li>Law college ka alumni group</li>
<li>WakeelSaathi jaisi verified listing jahan chamber apna zaroorat likhta hai</li>
</ul>
<div class="callout"><b>Yaad rakhein:</b> Paisa maangne wale “job agent” fake hote hain. Koi serious chamber job ke liye pehle paisa nahi maangta.</div>
"""},
            {"h2": "CV jo kaam karti hai (1 page)", "html": """
<ul>
<li><b>Header:</b> naam, phone, email, city, aur ek line — kaunsa area</li>
<li><b>Objectives ki jagah "what I can do":</b> "3 bail applications, 12 legal notices drafted, 40+ court appearances observed"</li>
<li><b>Internships</b> — chamber ka naam, court, dates, kya kaam kiya</li>
<li><b>Skills:</b> drafting types, research databases (PLD/SCMR, law sites), zaban (Urdu/English/Sindhi)</li>
<li><b>Education + enrollment status</b> (Law-GAT, pupillage stage)</li>
<li><b>Ek sample draft attach</b> — aap ki asli ability sab se zyada yahi dikhati hai</li>
</ul>
"""},
            {"h2": "Salary expectations (realistic)", "html": """
<ul>
<li>Pupil / trainee: Rs 0–25,000 (kai jagah zero)</li>
<li>Junior associate (chamber): Rs 25,000–50,000</li>
<li>Law firm associate: Rs 50,000–120,000+</li>
<li>In-house (0–2 saal): Rs 60,000–120,000</li>
</ul>
<p class="mini">Detailed breakdown: <a href="../../career/lawyer-salary-pakistan/index.html">Lawyer salary in Pakistan</a>.</p>
"""},
        ],
        "faqs": [
            ("Karachi mein lawyer ki job kaise mile?", "Sab se effective tareeqa chamber visit + referral hai: seniors ko personally milna, ek page CV aur ek sample draft ke saath. Online listings madad karti hain magar hidden market bara hai."),
            ("Kya fresh graduate ko job milti hai?", "Pupillage/associate positions milti hain, magar paid hona guaranteed nahi. Pehle 1–2 saal seekhne par focus karein aur terms likhwaayein."),
            ("Lawyer job ke liye paisa dena chahiye?", "Nahi. Koi bhi “job guarantee” ya “placement fee” maangne wala shakhs aam taur par fake hota hai. Reputed chamber paisa nahi maangta."),
            ("Remote legal jobs Pakistan mein mil sakti hain?", "Haan — foreign law firms ke liye drafting, research aur document review. English skill aur sample work zaroori hai. Rates aam taur par USD mein hote hain."),
        ],
        "related": [("Lawyer salary in Pakistan", "career/lawyer-salary-pakistan/index.html"),
                    ("Room for rent in Karachi", "karachi/lawyer-room-for-rent/index.html"),
                    ("Bar Council enrollment", "career/bar-council-enrollment/index.html")],
    },

    # ---------------- 9. ROOM FOR RENT ----------------
    {
        "slug": "karachi/lawyer-room-for-rent/index.html",
        "url": "karachi/lawyer-room-for-rent/",
        "title": "Room for Rent in Karachi for Lawyers — Punjab Colony, Garden",
        "h1": "Wakeel ke liye Room / Seat Share — Karachi",
        "desc": "Karachi mein lawyer ke liye room, PG aur chamber seat share: Punjab Colony, Garden, Saddar, Malir, Gulshan ke budget ranges, kya check karein aur broker se kaise bachein.",
        "kicker": "Karachi · Rehail",
        "lede": "Naye wakeel ki sab se bari tension: <b>rehail</b>. Rs 30,000 ki income par Karachi mein room milna mushkil hai — magar network wale log ye masla hal kar lete hain. Hum wahi network formal bana rahe hain.",
        "sections": [
            {"h2": "Budget ka haqeeqat-based breakdown", "html": """
<table class="tbl">
<thead><tr><th>Option</th><th>Typical monthly (PKR)</th><th>Note</th></tr></thead>
<tbody>
<tr><td>Shared room (2 log)</td><td>8,000 – 15,000</td><td>Sab se sasta; utilities alag ya shamil</td></tr>
<tr><td>PG / hostel (khana shamil)</td><td>10,000 – 20,000</td><td>Clean, security, magar rules</td></tr>
<tr><td>Single room in shared flat</td><td>14,000 – 25,000</td><td>Punjab Colony, Garden, Jamshed Road</td></tr>
<tr><td>Separate small flat</td><td>25,000 – 45,000</td><td>Deposit alag (2–3 mahine)</td></tr>
<tr><td>Chamber seat share (court ke qareeb)</td><td>6,000 – 15,000</td><td>Desk + cupboard + library access</td></tr>
</tbody>
</table>
<p class="mini">Rs 30,000 stipend par: rehail 12–18k + khana 8–12k + transport 4–6k = pehle mahine hi tight. Is liye <b>seat share + shared room</b> ka combination sab se practical hai.</p>
"""},
            {"h2": "Kaun se ilaqay court ke liye behtar hain", "html": """
<ul>
<li><b>Punjab Colony / Garden</b> — City Courts aur Saddar ke qareeb, lawyers ka ghana network, khana sasta</li>
<li><b>Saddar</b> — har jagah se transport, magar raat mein shor aur bheer</li>
<li><b>Jamshed Road / Patel Para</b> — darmiyani budget, court aur SHC dono ka access</li>
<li><b>Malir</b> — Malir court ke liye, sasta, magar City Courts door</li>
<li><b>Gulshan-e-Iqbal</b> — behtar rehail, magar roz safar aur bara kharcha</li>
<li><b>Clifton / Defence</b> — high court ke qareeb, magar junior ke budget se bahar</li>
</ul>
"""},
            {"h2": "Room lete waqt 8 cheezein check karein", "html": """
<ol class="steps">
<li><b>Malik ki identity</b> — CNIC dekhein aur note karein (owner hai ya sub-letter?)</li>
<li><b>Rent agreement</b> — likha hua, 2 copies, duration aur advance clear</li>
<li><b>Bijli ka bill</b> — separate meter hai ya shared? Rate kaun tay karta hai?</li>
<li><b>Paani</b> — tanki, timing aur quality (Karachi ka sab se bara issue)</li>
<li><b>Security</b> — gate, guard, lock, aur raat mein entry ka system</li>
<li><b>Deposit ki wapsi</b> — kab aur kis condition par? Likhein.</li>
<li><b>Notice period</b> — kitne mahine pehle batana hoga (dono taraf)</li>
<li><b>Study/work environment</b> — file rakhne ki jagah, light, internet</li>
</ol>
<div class="callout"><b>Khatoon lawyers ke liye:</b> family building, warden, security guard aur separate entrance zaroor check karein. Sirf "safe hai" kehne par bharosa na karein — visit karein, doosri residents se poochein.</div>
"""},
            {"h2": "Broker ke bajaye kya karein", "html": """
<ul>
<li>Chamber ke seniors aur colleagues se poochein — unke paas khali seat ka pata hota hai</li>
<li>Law college ke alumni group aur bar room notice board</li>
<li>Direct owner se deal karein — "commission" dene se pehle sochein</li>
<li>WakeelSaathi Rehail listings — <b>verified</b>, area aur budget filter ke saath</li>
</ul>
<p class="mini">⚠️ Kabhi bhi room dekhne se pehle advance/booking payment na karein. Advance hamesha agreement ke baad.</p>
"""},
        ],
        "faqs": [
            ("Karachi mein wakeel ke liye sasta room kahan milega?", "Punjab Colony, Garden, Jamshed Road aur Malir mein shared rooms aam taur par Rs 8,000–25,000 per month milte hain. Court ke qareeb chamber seat share Rs 6,000–15,000 mein milta hai."),
            ("Chamber seat share kya hota hai?", "Ek chamber mein 2–3 wakeel desk aur space share karte hain aur rent/kharcha taqseem karte hain. Naye wakeel ke liye ye sab se sasta tareeqa hai court ke qareeb rehne ka."),
            ("Kya bina rent agreement room le sakte hain?", "Technically le sakte hain, magar ye risky hai — deposit, notice period aur bills par jhagra ho jata hai. Likha hua agreement dono taraf ki hifazat hai."),
            ("Female lawyer ke liye safe rehail kaise dhoondein?", "Family building, warden ya security guard, separate entrance aur verified owner — ye check karein. Ek visit karein aur mojooda residents se baat karein. Verified listings par hi bharosa karein."),
        ],
        "related": [("Lawyer jobs in Karachi", "karachi/lawyer-jobs/index.html"),
                    ("Lawyer salary in Pakistan", "career/lawyer-salary-pakistan/index.html"),
                    ("Bar Council enrollment", "career/bar-council-enrollment/index.html")],
    },

    # ---------------- 10. HIGH COURT LICENSE ----------------
    {
        "slug": "career/high-court-license/index.html",
        "url": "career/high-court-license/",
        "title": "High Court License in Pakistan — Requirements & Process",
        "h1": "High Court License (Advocate High Court)",
        "desc": "High Court license Pakistan: 2 saal practice ki requirement, application process, fitness certificate, documents aur practice record kaise maintain karein.",
        "kicker": "Career · Licensing",
        "lede": "Lower court se High Court — ye promotion nahi, naya license hai. 2 saal ka practice record aaj se maintain karna shuru karein, warna baad mein jodna mushkil hota hai.",
        "sections": [
            {"h2": "Eligibility", "html": """
<ul>
<li>Advocate ke taur par enrollment (provincial bar council roll par)</li>
<li><b>Kam az kam 2 saal</b> subordinate courts mein practice (Act ke section 27 ke mutabiq)</li>
<li>Prescribed application form + fees</li>
<li>High Court ki fitness/character requirements aur interview (agar required ho)</li>
</ul>
<p class="mini">Exact requirements aur current fees Sindh High Court / Sindh Bar Council se confirm karein.</p>
"""},
            {"h2": "Process", "html": """
<ol class="steps">
<li><b>Practice record tayyar karein</b> — 2 saal ke cases ki list: title, court, case number, aap ka role.</li>
<li><b>Application</b> (prescribed form) bar council ke through High Court ko.</li>
<li><b>Certificates</b> — good standing, dues clearance, aur character/fitness.</li>
<li><b>Review / interview</b> — court ke process ke mutabiq.</li>
<li><b>Certificate issue</b> — High Court advocate ke taur par enrollment.</li>
</ol>
"""},
            {"h2": "Practice record — jo aaj banana chahiye", "html": """
<p>Agar aap aaj se ye register maintain karein, 2 saal baad aap ka kaam aasan ho jayega:</p>
<table class="tbl">
<thead><tr><th>Column</th><th>Kya likhein</th></tr></thead>
<tbody>
<tr><td>Date</td><td>Peshì ki tareekh</td></tr>
<tr><td>Court &amp; case no.</td><td>Court ka naam, case/FIR number</td></tr>
<tr><td>Parties</td><td>Title (client ki ijazat ke baghair public share na karein)</td></tr>
<tr><td>Aap ka role</td><td>Drafting / research / appearance / assistance</td></tr>
<tr><td>Outcome</td><td>Adjournment, order, arguments</td></tr>
<tr><td>Copy</td><td>Order sheet/file ka scan</td></tr>
</tbody>
</table>
"""},
            {"h2": "Supreme Court tak ka raasta", "html": """
<p>Advocate Supreme Court banne ke liye aam taur par <b>High Court advocate ke taur par 7 saal</b> ki practice aur prescribed process (fitness certificate, interviews, fees) chahiye. Detail hamesha Pakistan Bar Council se confirm karein — requirements aur fees waqt ke saath badalte hain.</p>
"""},
        ],
        "faqs": [
            ("High Court license ke liye kitne saal chahiye?", "Legal Practitioners and Bar Councils Act ke mutabiq subordinate courts mein kam az kam 2 saal ki practice chahiye. Current requirements bar council se confirm karein."),
            ("Kya High Court license ke bina High Court mein appear ho sakta hai?", "Nahi — High Court mein plead karne ke liye Advocate High Court ka license chahiye. Lower court advocate sirf subordinate courts tak appear kar sakta hai."),
            ("Practice record na ho to kya karein?", "Order sheets, court copies aur senior ki tasdeeq se record reconstruct karne ki koshish karein. Isi liye aaj se register maintain karna zaroori hai."),
            ("High Court license ki fee kitni hai?", "Fee waqt ke saath badalti hai. Sindh Bar Council / High Court ki current fee schedule check karein."),
        ],
        "related": [("Bar Council enrollment", "career/bar-council-enrollment/index.html"),
                    ("Lawyer salary in Pakistan", "career/lawyer-salary-pakistan/index.html"),
                    ("Law-GAT guide", "career/law-gat/index.html")],
    },

    # ---------------- 11. VAKALATNAMA ----------------
    {
        "slug": "drafts/vakalatnama-format/index.html",
        "url": "drafts/vakalatnama-format/",
        "title": "Vakalatnama Format in Pakistan (Word, English & Urdu)",
        "h1": "Vakalatnama Format — Pakistan",
        "desc": "Vakalatnama ka format Pakistan mein: must clauses, Supreme Court aur High Court ke liye differences, stamp aur acceptance, aur common ghaltiyan.",
        "kicker": "Drafts · Filing",
        "lede": "Vakalatnama chhoti document hai — magar adhoori hone par case ki pehli date par hi masla aa jata hai.",
        "sections": [
            {"h2": "Vakalatnama mein kya hona chahiye", "html": """
<ol class="steps">
<li><b>Court ka naam</b> aur case number/title</li>
<li><b>Client ki details</b> — naam, parentage, CNIC, address</li>
<li><b>Advocate ki details</b> — naam, enrollment number, chamber address</li>
<li><b>Authorization clause</b> — "I authorize the above-named advocate to appear, plead and act on my behalf" — scope likha ho (appear, plead, act, compromise?)</li>
<li><b>Acceptance</b> — advocate ka acceptance (kai courts mein zaroori)</li>
<li><b>Signature + date</b> — client (aur advocate)</li>
<li><b>Stamp/court fee</b> — court ke rules ke mutabiq</li>
<li><b>Witnesses / attestation</b> — jahan required</li>
</ol>
"""},
            {"h2": "Scope of authority — sab se ahem clause", "html": """
<p>"Appear, plead and act" ka matlab har cheez nahi hota. Agar client chahta hai ke advocate <b>compromise ya settlement</b> kar sake, to ye alag se likha jana chahiye. Isi tarah:</p>
<ul>
<li>Appeal file karne ka haq</li>
<li>Evidence led karne ka haq</li>
<li>Case withdraw karne ka haq</li>
<li>Kisi doosre advocate ko substitute karne ka haq</li>
</ul>
<div class="callout"><b>Practice tip:</b> Scope ko italic/underline na karein — bas clear English mein likhein. Court aur client dono ko ek hi cheez samajh aani chahiye.</div>
"""},
            {"h2": "Court ke hisaab se farq", "html": """
<table class="tbl">
<thead><tr><th>Court</th><th>Note</th></tr></thead>
<tbody>
<tr><td>District / subordinate courts</td><td>Aam format; stamp/court fee court ke rules ke mutabiq</td></tr>
<tr><td>Sindh High Court</td><td>High Court advocate ka enrollment number; filing branch ka current requirement check karein</td></tr>
<tr><td>Supreme Court</td><td>Advocate-on-Record / Advocate Supreme Court ki requirement; apna makhsoos format</td></tr>
<tr><td>Tribunals (service, tax, etc.)</td><td>Har tribunal ka apna practice; pehle filing branch se poochein</td></tr>
</tbody>
</table>
"""},
            {"h2": "Common mistakes", "html": """
<ul>
<li>Case number ghalat ya khali</li>
<li>Client ka naam CNIC se match nahi karta</li>
<li>Advocate ka enrollment number nahi likha</li>
<li>Acceptance clause missing — filing branch wapas kar deti hai</li>
<li>Pata adhoora — notice/order client tak nahi pahunchta</li>
<li>Stamp/fee ki qism ghalat</li>
</ul>
"""},
            {"h2": "Vakalatnama cancel ya change karna", "html": """
<p>Agar client advocate badalna chahta hai, to courts ka apna process hai (no objection / discharge application). Ye process court ke rules aur case ki stage par depend karta hai — bina cause list/order ki copy ke koi step na lein.</p>
"""},
        ],
        "faqs": [
            ("Vakalatnama kya hoti hai?", "Vakalatnama ek document hai jisse client apne advocate ko court mein us ki taraf se appear, plead aur act karne ka ikhtiyar deta hai. Iske baghair advocate court mein case file/plead nahi kar sakta."),
            ("Vakalatnama par stamp kitna lagta hai?", "Court aur case ki qism ke hisaab se stamp/court fee alag hoti hai. Mutaliqa court ke filing branch se current requirement confirm karein."),
            ("Kya vakalatnama Urdu mein ho sakti hai?", "Aam practice English mein hai. Agar Urdu chahiye to upar English version rakhein aur neeche Urdu translation — court ki requirement pehle confirm karein."),
            ("Ek case mein do advocates ho sakte hain?", "Aam taur par vakalatnama ek advocate ke naam hoti hai; doosre advocate ko assist karne ke liye alag arrangement ya substitution hota hai. Court ke rules check karein."),
        ],
        "related": [("Legal notice format", "drafts/legal-notice-format/index.html"),
                    ("Plaint format", "drafts/plaint-format/index.html"),
                    ("High Court license", "career/high-court-license/index.html")],
    },

    # ---------------- 12. 489-F ----------------
    {
        "slug": "case-law/489-f/index.html",
        "url": "case-law/489-f/",
        "title": "489-F PPC Case Law — Cheque Dishonour in Pakistan",
        "h1": "489-F PPC — Cheque Dishonour Case Law",
        "desc": "Section 489-F PPC: cheque dishonour ka offence, elements, complaint kaise file hoti hai, defence aur research guide — Pakistani lawyers ke liye.",
        "kicker": "Case law · Criminal",
        "lede": "<b>489-F PPC</b> Pakistan ka sab se zyada file hone wale criminal complaints mein se ek: <b>cheque ka dishonour</b>. Yahan legal framework aur research method.",
        "sections": [
            {"h2": "Section 489-F ka framework", "html": """
<p>Pakistan Penal Code ka section <b>489-F</b> us shakhs se mutalliq hai jo <b>dishonestly</b> cheque issue karta hai — qarz ki adaigi ya kisi obligation ki poorai ke liye — jab usay maloom ho ke us ke account mein funds kafi nahi hain ya cheque return ho jayega.</p>
<p>Is offence ki saza mein imprisonment, fine, ya dono shamil hain (bare act ka exact text aur duration parhein). Cheque dishonour ke civil aur criminal dono pehlu hote hain — dono ka apna raasta hota hai.</p>
<div class="callout"><b>Note:</b> Ye page legal information deta hai, complaint ka draft nahi. Har case ke facts alag hote hain — apne case par tayari ke liye verified authorities aur apne senior ki guidance zaroor lein.</div>
"""},
            {"h2": "Elements jinhe prove karna hota hai", "html": """
<table class="tbl">
<thead><tr><th>Element</th><th>Kya dekha jata hai</th></tr></thead>
<tbody>
<tr><td>Cheque ka issue hona</td><td>Original cheque, signature, bank record</td></tr>
<tr><td>Qarz ya obligation</td><td>Agreement, invoice, receipt, WhatsApp/email trail</td></tr>
<tr><td>Dishonest intention</td><td>Funds ki kami ka ilm, account history, conduct</td></tr>
<tr><td>Return / dishonour</td><td>Bank ka return memo — reason clearly likha ho</td></tr>
<tr><td>Notice / demand</td><td>Notice ki copy + delivery proof (facts par depend)</td></tr>
</tbody>
</table>
"""},
            {"h2": "Complaint se pehle ka checklist", "html": """
<ol class="steps">
<li><b>Original cheque</b> aur us ki copy sambhal ke rakhein</li>
<li><b>Bank ka return memo</b> — reason (insufficient funds, signature mismatch, account closed, stop payment) bohat ahem hai</li>
<li><b>Qarz ka proof</b> — agreement, invoice, ledgers, messages</li>
<li><b>Notice</b> — legal notice bhejein aur delivery proof rakhein</li>
<li><b>Limitation</b> — kis muddat mein complaint file ho sakti hai, ye section aur case law se check karein</li>
<li><b>Forum</b> — competent court ka taayun (territorial jurisdiction)</li>
</ol>
"""},
            {"h2": "Defence ke aam pehlu (research ke liye)", "html": """
<ul>
<li>Cheque <b>security</b> ke taur par diya gaya tha, qarz ki adaigi ke liye nahi</li>
<li>Qarz ka <b>proof nahi</b> — sirf cheque ka hona kafi nahi</li>
<li><b>Signature</b> client ka nahi (forgery ka sawal)</li>
<li><b>Dishonest intention</b> ka element missing</li>
<li><b>Notice/demand</b> ka procedure follow nahi hua</li>
<li>Civil dispute ko criminal rang dena</li>
</ul>
<p class="mini">In points par authority dhoondte waqt keywords: "489-F PPC", "security cheque", "dishonest intention", "quantum of sentence", "compounding".</p>
"""},
            {"h2": "Civil aur criminal — dono ka faisla", "html": """
<p>Cheque dishonour par aksar do raaste chalte hain: <b>criminal complaint (489-F)</b> aur <b>civil suit/recovery</b>. Dono ke maqsad aur natije alag hote hain. Client ko pehle hi saaf bata dein ke wo kya chahta hai — saza, ya paisa wapas. Bohat cases mein settlement hi practical natija hota hai.</p>
"""},
        ],
        "faqs": [
            ("489-F PPC mein saza kya hai?", "Is offence par imprisonment aur/ya fine ki saza hai. Exact duration aur wording bare act se parhein aur latest precedent dekhein — courts facts ke hisaab se saza tay karti hain."),
            ("Cheque bounce par police case ho sakta hai?", "489-F ke under complaint ka raasta hota hai. Kya police station jaana behtar hai ya court mein complaint — ye facts aur aap ke legal strategy par depend karta hai. Apne senior se mashwara lein."),
            ("Security cheque aur qarz ka cheque mein kya farq hai?", "Security cheque aam taur par guarantee ke taur par diya jata hai, jab ke qarz ka cheque obligation ki adaigi ke liye hota hai. Ye farq dishonest intention aur qarz ke proof par asar daalta hai — is par case law zaroor dekhein."),
            ("Kya cheque bounce case settle ho sakta hai?", "Haan, aksar cases settlement par khatam hote hain. Settlement ka record likha hua hona chahiye aur court ke process ke mutabiq hona chahiye."),
        ],
        "related": [("Legal notice format", "drafts/legal-notice-format/index.html"),
                    ("302 PPC case law", "case-law/302-ppc/index.html"),
                    ("Case law hub", "case-law/index.html")],
    },
]

# ---------- hubs (parent pages) ----------
HUBS = [
    {
        "slug": "case-law/index.html",
        "url": "case-law/",
        "title": "Case Law Pakistan — Section-wise Research Guides | WakeelSaathi",
        "h1": "Case Law Pakistan",
        "desc": "Section-wise case law research guides for Pakistani lawyers: 302 PPC, 489-F PPC, 497 CrPC. Free databases, search method aur verification checklist.",
        "kicker": "Research library",
        "lede": "Pakistan mein wakeel ki sab se zyada search ki jane wali cheez: <b>case law</b>. Yahan section-wise research guides hain — kahan se search karein, kaise verify karein, court mein kaise use karein.",
        "children": [
            ("302 PPC case law", "Qatl-i-amd — elements, qisas aur research method", "../case-law/302-ppc/index.html"),
            ("489-F PPC case law", "Cheque dishonour — complaint, defence aur research", "../case-law/489-f/index.html"),
            ("497 CrPC bail case law", "Non-bailable offence mein bail ke grounds", "../case-law/497-crpc/index.html"),
        ],
        "sections": [
            {"h2": "Pakistan mein case law kahan se milega", "html": """
<table class="tbl">
<thead><tr><th>Source</th><th>Kya milta hai</th><th>Cost</th></tr></thead>
<tbody>
<tr><td>Supreme Court of Pakistan</td><td>Judgments, cause lists, case status</td><td>Free</td></tr>
<tr><td>High Courts (SHC, LHC, PHC, BHC, IHC) &amp; FSC</td><td>Reported judgments aur orders</td><td>Free</td></tr>
<tr><td>Law databases (Pakistan Law Site, Pak Legal Database, LegalSearch)</td><td>PLD, SCMR, YLR, CLC citations</td><td>Free / subscription</td></tr>
<tr><td>PLJ (Punjab Bar Council section)</td><td>Pakistan Law Journal</td><td>Subscription</td></tr>
<tr><td>AI research tools</td><td>Fast research aur drafting hints</td><td>Free / paid</td></tr>
</tbody>
</table>
<p class="mini">AI ka output hamesha original judgment se verify karein. Galat citation court mein sab se bara nuqsan hai.</p>
"""},
            {"h2": "4-step research method", "html": """
<ol class="steps">
<li><b>Section framing</b> — bare act ka text parhein, elements alag likhein</li>
<li><b>Headnote hunting</b> — section + keywords se 5–8 leading judgments chunein (Supreme Court pehle)</li>
<li><b>Ratio extract</b> — har judgment se ek line ka principle</li>
<li><b>Distinguish</b> — apne facts se farq likhein; yahi courtroom mein kaam aata hai</li>
</ol>
"""},
        ],
        "faqs": [
            ("Pakistan mein case law free mein kahan milta hai?", "Supreme Court aur High Courts ki official websites par judgments free milte hain. Law databases citation search dete hain — kuch free, kuch subscription par."),
            ("Kya WakeelSaathi judgments reproduce karta hai?", "Nahi. Hum research method aur statutory framework dete hain, aur official source ke links dete hain jahan se aap original judgment parh sakte hain."),
        ],
        "related": [("Bail application format", "../drafts/bail-application-format/index.html"),
                    ("Legal notice format", "../drafts/legal-notice-format/index.html")],
    },
    {
        "slug": "drafts/index.html",
        "url": "drafts/",
        "title": "Legal Draft Formats Pakistan — Bail, Notice, Plaint, Vakalatnama",
        "h1": "Legal Drafts Library",
        "desc": "Pakistan ke court drafts ka structure aur checklist: bail application, legal notice, plaint aur vakalatnama. Format, clauses aur common mistakes.",
        "kicker": "Draft library",
        "lede": "Drafting photocopy se nahi, <b>structure</b> se seekhi jati hai. Har draft ka skeleton, clauses aur ghaltiyan — yahan.",
        "children": [
            ("Bail application format", "496/497/498 CrPC — structure aur grounds", "../drafts/bail-application-format/index.html"),
            ("Legal notice format", "Recovery, cheque, rent — 15 din aur delivery proof", "../drafts/legal-notice-format/index.html"),
            ("Plaint format", "CPC Order VII — plaint ka structure", "../drafts/plaint-format/index.html"),
            ("Vakalatnama format", "Authority, acceptance aur stamp", "../drafts/vakalatnama-format/index.html"),
        ],
        "sections": [
            {"h2": "Har draft ka bunyadi skeleton", "html": """
<ol class="steps">
<li><b>Heading</b> — court, case number, parties</li>
<li><b>Title</b> — document kya hai aur kis section ke under</li>
<li><b>Facts</b> — dates ke saath, sirf relevant</li>
<li><b>Grounds / averments</b> — numbered, har point alag</li>
<li><b>Legal basis</b> — sirf verified sections/authorities</li>
<li><b>Prayer</b> — clear aur specific</li>
<li><b>Verification + annexures</b></li>
</ol>
"""},
        ],
        "faqs": [
            ("Kya yahan se draft download kar sakte hain?", "Hum structure aur checklist dete hain — copy-paste templates nahi, kyunke har case ke facts alag hote hain. Pehla draft banane ke liye AI Kit use karein, final draft apni review se."),
        ],
        "related": [("Case law hub", "../case-law/index.html"), ("AI Kit", "../index.html#aikit")],
    },
    {
        "slug": "karachi/index.html",
        "url": "karachi/",
        "title": "Karachi Lawyers — Jobs, Rehail & Chamber Share | WakeelSaathi",
        "h1": "Karachi — Wakeelon ka Shehar",
        "desc": "Karachi mein lawyer jobs, room for rent, chamber seat share aur court-wise practice guide. Punjab Colony, Garden, Saddar, Malir aur Gulshan ke liye practical guides.",
        "kicker": "Karachi",
        "lede": "Karachi mein practice karna alag game hai: court ka intekhab, rehail ka budget aur reference ka network. Yahan shehar-specific guides.",
        "children": [
            ("Lawyer jobs in Karachi", "Chamber, firm, in-house aur freelancing", "../karachi/lawyer-jobs/index.html"),
            ("Room / seat share", "Punjab Colony, Garden, Saddar, Malir", "../karachi/lawyer-room-for-rent/index.html"),
            ("Case law library", "Section-wise research guides", "../case-law/index.html"),
        ],
        "sections": [
            {"h2": "Karachi mein practice — 3 faislay jo sab kuch tay karte hain", "html": """
<ol class="steps">
<li><b>Court ka intekhab:</b> City Courts, Malir, ya Sindh High Court. Ek court mein mastery > paanch courts mein bhaagna.</li>
<li><b>Rehail ka budget:</b> court ke qareeb sasta rehail = roz ka safar aur waqt bachta hai. Seat share sab se practical option hai.</li>
<li><b>Network:</b> Karachi mein kaam reference se aata hai. Chamber, bar room aur batchmates — teeno ko systematically use karein.</li>
</ol>
"""},
        ],
        "faqs": [
            ("Karachi mein naye lawyer ke liye sab se sasta rehail option kya hai?", "Chamber seat share (Rs 6,000–15,000 per month) + shared room (Rs 8,000–15,000). Isse court ke qareeb rehna aur kharcha dono manage ho jata hai."),
            ("Karachi mein lawyer jobs kahan milti hain?", "Chambers (City Courts/SHC ke qareeb), law firms, banks aur companies ke legal departments, aur government offices. Bohat positions advertise nahi hotin — chamber visit aur referral sab se effective hai."),
        ],
        "related": [("Lawyer jobs in Karachi", "../karachi/lawyer-jobs/index.html"),
                    ("Room for rent", "../karachi/lawyer-room-for-rent/index.html")],
    },
    {
        "slug": "career/index.html",
        "url": "career/",
        "title": "Legal Career Pakistan — Law-GAT, Enrollment, Salary, License",
        "h1": "Career — Sanad se High Court tak",
        "desc": "Pakistan mein legal career ka poora raasta: Law-GAT, bar council enrollment, pupillage, salary expectations aur High Court license.",
        "kicker": "Career",
        "lede": "Har stage ka apna process hai — aur kisi ne aap ko theek se nahi bataya. Yahan har step ka guide.",
        "children": [
            ("Law-GAT 2026", "Test date, syllabus, past papers, result", "../career/law-gat/index.html"),
            ("Bar Council enrollment", "Eligibility, documents, pupillage, fees", "../career/bar-council-enrollment/index.html"),
            ("How to become a lawyer", "12th se Supreme Court tak roadmap", "../career/how-to-become-lawyer-pakistan/index.html"),
            ("Lawyer salary in Pakistan", "Realistic ranges aur structural wajah", "../career/lawyer-salary-pakistan/index.html"),
            ("High Court license", "2 saal practice, process aur record", "../career/high-court-license/index.html"),
        ],
        "sections": [
            {"h2": "Timeline ek nazar mein", "html": """
<table class="tbl">
<thead><tr><th>Stage</th><th>Waqt</th></tr></thead>
<tbody>
<tr><td>LLB</td><td>5 saal</td></tr>
<tr><td>Law-GAT</td><td>Cycle ke mutabiq</td></tr>
<tr><td>Pupillage</td><td>6 mahine (prescribed)</td></tr>
<tr><td>Lower court license</td><td>Enrollment ke baad</td></tr>
<tr><td>High Court license</td><td>2 saal practice ke baad</td></tr>
<tr><td>Supreme Court</td><td>7 saal HC practice ke baad</td></tr>
</tbody>
</table>
"""},
        ],
        "faqs": [
            ("Legal career ka pehla step kya hai?", "12th ke baad recognized LLB programme. Us se pehle ek internship karein taake aap ko pata ho ke ye field aap ke liye hai ya nahi."),
            ("Kya bina Law-GAT advocate ban sakte hain?", "Pakistan Bar Council ke rules ke mutabiq prescribed test pass karna zaroori hai. Current requirement apne bar council se confirm karein."),
        ],
        "related": [("Lawyer jobs in Karachi", "../karachi/lawyer-jobs/index.html"),
                    ("Room for rent", "../karachi/lawyer-room-for-rent/index.html")],
    },
]

# ---------------- extra pages (hub links ko complete karne ke liye) ----------------
PAGES.extend([
    {
        "slug": "case-law/497-crpc/index.html",
        "url": "case-law/497-crpc/",
        "title": "497 CrPC Case Law — Bail in Non-Bailable Offence (Pakistan)",
        "h1": "497 CrPC — Bail Case Law (Pakistan)",
        "desc": "Section 497 CrPC Pakistan: non-bailable offence mein bail ka framework, 497(2) ka scope, grounds aur research guide with verification checklist.",
        "kicker": "Case law · Criminal",
        "lede": "<b>497 CrPC</b> wo section hai jis par har criminal lawyer ka roz ka kaam chalta hai: non-bailable offence mein bail.",
        "sections": [
            {"h2": "Framework — 496, 497 aur 498", "html": """
<p>Criminal Procedure Code ka bail ka chapter aam taur par in sections par khara hai: <b>496</b> (bailable offences), <b>497</b> (non-bailable offences) aur <b>498</b> (Sessions Court / High Court ke powers).</p>
<p>Section 497 aam taur par do hisson mein samjha jata hai: pehla hissa jab accused ko bail na milne ka general rule, aur doosra (aksar <b>497(2)</b> kaha jane wala hissa) jahan court ko discretion milta hai jab record se further inquiry ka maqam banta ho.</p>
<div class="callout"><b>Zaroori:</b> Section ka exact text aur us ki sub-clauses bare act se parhein. Har provincial/court practice mein interpretation ka farq ho sakta hai — apne High Court ki binding authorities dekhein.</div>
"""},
            {"h2": "Bail ke grounds — issue map", "html": """
<table class="tbl">
<thead><tr><th>Issue</th><th>Kya dekhna hai</th></tr></thead>
<tbody>
<tr><td>Nature of offence</td><td>Death/life imprisonment wala offence? Prohibitory clause ka scope</td></tr>
<tr><td>Further inquiry</td><td>Record se sawal ubnay ka maqam — kya evidence primâ facie nahi banta</td></tr>
<tr><td>Investigation status</td><td>Challan pesh, recovery ho chuki, custody ki muddat</td></tr>
<tr><td>Flight risk</td><td>Permanent address, family, roots in society</td></tr>
<tr><td>Parity</td><td>Co-accused ko bail mil chuki hai</td></tr>
<tr><td>Health / age / gender</td><td>Documented grounds jo section mein specifically mention hon</td></tr>
<tr><td>Delay in trial</td><td>Custody ki muddat vs trial ki raftaar</td></tr>
</tbody>
</table>
"""},
            {"h2": "Research kaise karein", "html": """
<ol class="steps">
<li>Keywords: "497 CrPC", "further inquiry", "prohibitory clause", "bail — deep-rooted enmity", "bail — recovery", "bail — challan".</li>
<li>Pehle <b>Supreme Court</b>, phir apne <b>High Court</b> ki authorities — binding hierarchy yaad rakhein.</li>
<li>Har authority ka operative paragraph parhein — headnote par bharosa na karein.</li>
<li>Latest status check karein: review, larger bench, ya subsequent distinguishing cases.</li>
</ol>
"""},
            {"h2": "Application likhne se pehle", "html": """
<p>Bail application ka format aur grounds ka structure hamare <a href="../../drafts/bail-application-format/index.html">Bail application format</a> page par hai. Yaad rakhein: bail ka maqsad trial ke doran release hai — acquittal nahi. Application ki zaban wahi rakhein.</p>
"""},
        ],
        "faqs": [
            ("497 CrPC mein bail kab milti hai?", "Court facts aur record dekh kar faisla karti hai — aam taur par jahan further inquiry ka maqam ho, ya section mein di gayi specific sooraten maujood hon. Apne facts par latest binding authority zaroor check karein."),
            ("497(2) ka kya matlab hai?", "Ye aam taur par section 497 ke us hisse ko kaha jata hai jahan court ko further inquiry ka maqam banne par bail ka discretion milta hai. Exact wording bare act se parhein."),
            ("Bail reject ho to kahan appeal karein?", "Aam taur par Sessions Court ya High Court ka raasta hota hai (498 CrPC). Procedure aur limitation apne case ki qism ke mutabiq verify karein."),
        ],
        "related": [("Bail application format", "drafts/bail-application-format/index.html"),
                    ("302 PPC case law", "case-law/302-ppc/index.html"),
                    ("Case law hub", "case-law/index.html")],
    },
    {
        "slug": "drafts/plaint-format/index.html",
        "url": "drafts/plaint-format/",
        "title": "Plaint Format in Pakistan (CPC Order VII) — Civil Suit",
        "h1": "Plaint Format — Pakistan (CPC)",
        "desc": "Plaint ka format Pakistan mein: Order VII CPC ke requirements, suit valuation, court fee, jurisdiction, cause of action aur common mistakes.",
        "kicker": "Drafts · Civil",
        "lede": "Civil suit ka pehla document: <b>plaint</b>. Agar plaint kamzor hai to poora case kamzor hai — aur isi ghalti ka sudhaar baad mein mushkil hota hai.",
        "sections": [
            {"h2": "Order VII CPC ke bunyadi requirements", "html": """
<ul>
<li>Court ka naam</li>
<li>Plaintiff aur defendant ki details (naam, description, address)</li>
<li><b>Suit ka title</b> aur subject matter</li>
<li><b>Cause of action</b> — kab, kahan aur kaise paida hua (dates ke saath)</li>
<li><b>Jurisdiction</b> — court ko kyun ikhtiyar hai (territorial + pecuniary)</li>
<li><b>Suit valuation</b> aur court fee</li>
<li><b>Relief</b> (prayer) — precise aur quantified jahan possible ho</li>
<li><b>Limitation</b> — suit kab tak file ho sakta hai</li>
<li>Verification + list of documents</li>
</ul>
"""},
            {"h2": "Structure jo courts expect karti hain", "html": """
<ol class="steps">
<li><b>Heading:</b> "In the Court of ___" + suit number</li>
<li><b>Parties:</b> plaintiff vs defendants, addresses</li>
<li><b>Suit for:</b> ek line — "Suit for recovery of Rs ___" ya "Suit for specific performance"</li>
<li><b>Facts:</b> numbered paragraphs, chronological</li>
<li><b>Cause of action:</b> alag heading, dates ke saath</li>
<li><b>Jurisdiction &amp; valuation:</b> alag paragraph</li>
<li><b>Limitation:</b> alag paragraph</li>
<li><b>Prayer:</b> numbered reliefs + costs</li>
<li><b>Verification + affidavit + documents</b></li>
</ol>
"""},
            {"h2": "Court fee aur valuation — sab se zyada ghaltiyan yahan", "html": """
<p>Court fee suit ki qism aur valuation par depend karti hai (Sindh mein Court Fees Act ke framework ke mutabiq). Ghalti se:</p>
<ul>
<li>Court fee kam lag gayi → objection aur deri</li>
<li>Valuation ghalat → pecuniary jurisdiction ka sawal</li>
<li>Relief quantify nahi kiya → decree ka masla</li>
</ul>
<p class="mini">Filing branch se current fee schedule confirm karein — ye waqt ke saath badalta hai.</p>
"""},
            {"h2": "Sarkari fard ke khilaf suit — special notice", "html": """
<p>Sarkar ya kisi public officer ke khilaf suit mein aam taur par <b>pehle notice</b> dena zaroori hota hai (CPC ka mutalliqa section). Notice ki muddat aur form section se check karein — warna suit maintainability par sawal uthta hai.</p>
"""},
            {"h2": "Common mistakes", "html": """
<ul>
<li>Cause of action aur facts mix karna</li>
<li>Dates nahi likhna ("kuch arsa pehle" jaise alfaaz)</li>
<li>Relief mein "jo court munasib samjhe" likh dena bina specific demand</li>
<li>Documents ki list na lagana</li>
<li>Limitation par koi paragraph nahi</li>
<li>Verification ka format ghalat</li>
</ul>
"""},
        ],
        "faqs": [
            ("Plaint format Pakistan mein kya hota hai?", "Order VII CPC ke mutabiq: court ka naam, parties, suit ka title, numbered facts, cause of action, jurisdiction aur valuation, limitation, prayer, verification aur documents ki list."),
            ("Court fee kitni lagti hai?", "Suit ki qism aur valuation par depend karti hai. Mutaliqa court ke filing branch se current schedule confirm karein."),
            ("Kya plaint amend ho sakti hai?", "Aam taur par haan, court ki ijazat se (CPC ke mutabiq). Magar jitni jaldi ho utna behtar — trial ke baad amendment mushkil hota hai."),
            ("Plaint Urdu mein likh sakte hain?", "Aam practice English mein hai. Urdu translation saath rakh sakte hain, magar court ki requirement pehle confirm karein."),
        ],
        "related": [("Legal notice format", "drafts/legal-notice-format/index.html"),
                    ("Vakalatnama format", "drafts/vakalatnama-format/index.html"),
                    ("Case law hub", "case-law/index.html")],
    },
])
