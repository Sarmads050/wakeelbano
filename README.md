# SANAD — Karachi ka Lawyer Ecosystem

Pakistan ke naye wakeelon ke liye ek career-first ecosystem: chamber/mentor matching, verified rehail
(rooms + chamber-share), kaam board, AI kit, aur growth school.

Ye repo do cheezon par mushtamil hai:

| File | Kya hai |
|---|---|
| `index.html` | Poora working prototype — single file, koi dependency nahi (inline CSS + JS, no CDN) |
| `research/pakistani-lawyers-deep-research.md` | Deep-research report: market size, lawyers ke 7 layers ke masail, competitor landscape, 8 revenue streams, 90-din launch plan, risks aur sources |

## Prototype kya kar sakta hai

- **Career Navigator** — 3 tracks (law student / fresh graduate / junior advocate), tickable steps + progress (localStorage)
- **Chamber Match** — practice area, court, zaban aur zaroorat ke hisaab se mentor/chamber matching
- **Rehail** — area, budget, type aur gender filters ke saath verified room / PG / chamber-share listings
- **Kaam Board** — drafting, research, remote aur content gigs (escrow model)
- **AI Kit** — 6 Pakistan-specific prompts (plaint, legal notice, bail, case-law memo, client message, social post) + guardrails
- **Growth School** — allowed vs risky marketing + 7-din content calendar
- **Pricing** — juniors hamesha free; paisa seniors / firms / universities se

## Kaise chalayein

Bas `index.html` browser mein kholein. Koi build step, server ya internet connection zaroori nahi.

```bash
open index.html          # macOS
xdg-open index.html      # Linux
start index.html         # Windows
```

Ya local server:

```bash
python3 -m http.server 8000
# phir http://localhost:8000
```

## GitHub Pages par live karna

1. Repo → **Settings** → **Pages**
2. Source: **Deploy from a branch** → Branch: `main` → Folder: `/ (root)`
3. Save. Link kuch minute mein ban jayega: `https://<username>.github.io/<repo>/`

## Update workflow

Is repo mein changes chat ke zariye hoti hain:

1. Aap chat mein change batayein ("Rehail mein Malir ke rooms add karo", "Pricing ka rupya badlo")
2. Change `index.html` / research file mein apply hota hai
3. Commit + push — GitHub Pages khud update ho jata hai (~1 minute)

Har commit ka message change ko describe karta hai, is liye history se pata chalta hai kab kya badla.

## Notes / Guardrails

- Sanad case referral par commission **nahi** leta — wo Bar Council rules ke khilaf hoga
- Koi "guaranteed client" ya "ranking" nahi bechi jati
- Har listing/profile verify hoti hai; demo data clearly marked hai
- AI outputs hamesha lawyer ki verification ke baad hi use hone chahiye

## Status

Prototype / demo. Backend, authentication aur real verification pipeline abhi nahi hai.
