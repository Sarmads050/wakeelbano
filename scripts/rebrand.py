import io, re, sys

p = 'index.html'
s = io.open(p, encoding='utf-8').read()

SEO_HEAD = '''<title>WakeelSaathi — Pakistan ke Wakeelon ka Ecosystem | Karachi</title>
<meta name="description" content="WakeelSaathi Pakistan ke wakeelon ka pehla saathi hai: career roadmap, verified chamber aur mentor matching, rehail (rooms + chamber-share), kaam board, case law aur draft library, AI kit aur growth school. Karachi se shuru.">
<meta name="keywords" content="lawyer in karachi, wakeel, advocate pakistan, chamber match, pupillage pakistan, case law pakistan, legal drafting, lawyer jobs in karachi, lawyer room for rent karachi">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="https://wakeelsaathi.com/">
<meta name="theme-color" content="#0B1B2B">
<meta name="geo.region" content="PK-SD">
<meta name="geo.placename" content="Karachi">
<meta property="og:type" content="website">
<meta property="og:site_name" content="WakeelSaathi">
<meta property="og:title" content="WakeelSaathi — Pakistan ke Wakeelon ka Ecosystem">
<meta property="og:description" content="Sanad milti hai, raasta hum dete hain. Career roadmap, chamber match, rehail, kaam board, case law library — ek jagah.">
<meta property="og:url" content="https://wakeelsaathi.com/">
<meta property="og:locale" content="en_PK">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="WakeelSaathi — Pakistan ke Wakeelon ka Ecosystem">
<meta name="twitter:description" content="Sanad milti hai, raasta hum dete hain. Karachi se shuru hone wala lawyer ecosystem.">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://wakeelsaathi.com/#org",
      "name": "WakeelSaathi",
      "url": "https://wakeelsaathi.com/",
      "description": "Pakistan ke wakeelon ka ecosystem: career guidance, chamber matching, verified rehail, kaam board aur legal resources.",
      "areaServed": {"@type": "City", "name": "Karachi"},
      "address": {"@type": "PostalAddress", "addressLocality": "Karachi", "addressRegion": "Sindh", "addressCountry": "PK"}
    },
    {
      "@type": "WebSite",
      "@id": "https://wakeelsaathi.com/#website",
      "url": "https://wakeelsaathi.com/",
      "name": "WakeelSaathi",
      "publisher": {"@id": "https://wakeelsaathi.com/#org"},
      "inLanguage": "en-PK"
    },
    {
      "@type": "LegalService",
      "name": "WakeelSaathi",
      "description": "Lawyer ecosystem aur career platform. Legal advice nahi deta.",
      "areaServed": {"@type": "City", "name": "Karachi"},
      "priceRange": "Free to Rs 60,000",
      "url": "https://wakeelsaathi.com/"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {"@type": "Question", "name": "Pakistan mein naye wakeel ko pehla chamber kaise milta hai?", "acceptedAnswer": {"@type": "Answer", "text": "WakeelSaathi par verified chambers ki list hai jahan practice area, court aur terms (paid ya unpaid pupillage) clearly likhe hote hain. Aap request bhej sakte hain, reference ki zaroorat nahi."}},
        {"@type": "Question", "name": "Kya WakeelSaathi legal advice deta hai?", "acceptedAnswer": {"@type": "Answer", "text": "Nahi. WakeelSaathi ek technology platform hai jo wakeelon ko career resources, listings aur tools deta hai. Ye koi legal advice ya case referral service nahi hai."}},
        {"@type": "Question", "name": "Karachi mein wakeel ke liye room ya chamber share kahan milega?", "acceptedAnswer": {"@type": "Answer", "text": "Rehail section mein Punjab Colony, Garden, Saddar, Malir aur Gulshan ke verified rooms, PG aur chamber-share listings maujood hain, budget aur area filter ke saath."}},
        {"@type": "Question", "name": "Kya junior wakeel ke liye WakeelSaathi free hai?", "acceptedAnswer": {"@type": "Answer", "text": "Haan. Students, fresh graduates aur junior advocates ke liye platform hamesha free hai. Paisa seniors, chambers, firms aur universities se aata hai."}}
      ]
    }
  ]
}
</script>'''

old_title = "<title>Sanad — Karachi's Lawyer Ecosystem</title>"
if old_title in s:
    s = s.replace(old_title, SEO_HEAD)
else:
    print('WARN: title not found')

reps = [
    ('<span><b>SANAD</b><small>Lawyer Ecosystem</small></span>',
     '<span><b>WakeelSaathi</b><small>Wakeel ka pehla saathi</small></span>'),
    ('<b style="font-size:19px">SANAD</b>', '<b style="font-size:19px">WakeelSaathi</b>'),
    ('SANAD — Karachi ka lawyer ecosystem', 'WakeelSaathi — Karachi ka lawyer ecosystem'),
    ('Sanad — Karachi pilot. Demo prototype.', 'WakeelSaathi — Karachi pilot. Demo prototype.'),
    ('Sanad koi legal advice nahi deta', 'WakeelSaathi koi legal advice nahi deta'),
    ('Sanad kisi client ki case referral par commission nahi leta', 'WakeelSaathi kisi client ki case referral par commission nahi leta'),
    ('Sanad Verified', 'WakeelSaathi Verified'),
    ('Sanad Free', 'WakeelSaathi Free'),
    ('Sanad dashboard', 'WakeelSaathi dashboard'),
    ('Sanad mein shamil hon', 'WakeelSaathi mein shamil hon'),
    ('Junior lawyer ke liye Sanad hamesha muft rahega.', 'Junior lawyer ke liye WakeelSaathi hamesha muft rahega.'),
    ('Sanad Chamber Match yahan kaam aata hai.', 'WakeelSaathi Chamber Match yahan kaam aata hai.'),
    ('Sanad profile link daalein.', 'WakeelSaathi profile link daalein.'),
    ('Sanad 10–15% platform fee leta hai', 'WakeelSaathi 10–15% platform fee leta hai'),
    ('Sanad kabhi deposit apne paas nahi rakhta', 'WakeelSaathi kabhi deposit apne paas nahi rakhta'),
    ('Sanad ka model simple hai', 'WakeelSaathi ka model simple hai'),
    ('Sanad ke rules', 'WakeelSaathi ke rules'),
    ("sanad.progress", "ws.progress"),
    ("sanad.leads", "ws.leads"),
]
for a, b in reps:
    if a not in s:
        print('WARN missing:', a[:50])
    s = s.replace(a, b)

# nav: add Case Law + Drafts
nav_old = '      <a href="#kaam" data-v="kaam">Kaam</a>'
nav_new = ('      <a href="#kaam" data-v="kaam">Kaam</a>\n'
           '      <a href="case-law/index.html" class="ext">Case Law</a>\n'
           '      <a href="drafts/index.html" class="ext">Drafts</a>')
if nav_old in s:
    s = s.replace(nav_old, nav_new)
else:
    print('WARN nav not found')

s = s.replace('  nav.main a.active{background:rgba(201,162,39,.16);color:var(--gold2)}',
'''  nav.main a.active{background:rgba(201,162,39,.16);color:var(--gold2)}
  nav.main a.ext{color:#E7CE7A}
  nav.main a.ext:hover{background:rgba(201,162,39,.16);color:#fff}''')

io.open(p, 'w', encoding='utf-8').write(s)
print('rebrand done; remaining Sanad mentions:', s.count('Sanad'))
