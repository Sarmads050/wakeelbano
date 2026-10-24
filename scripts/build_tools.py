# -*- coding: utf-8 -*-
"""WakeelBano — /tools/ : the three things a junior needs every court day.

    1. Cause-list tracker      keeps your own matters and next dates
    2. Court-day calculator    working days, court holidays, next date
    3. Filing cost worksheet   court fee, process fee, copies — added up

Everything runs in the browser. Nothing is sent anywhere, which is why a lawyer
can put a client's case title in it without worrying.

    python3 scripts/build_tools.py
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import build_pages as BP  # noqa: E402

CSS = """
.tools .hero{padding:30px 0 32px;margin-bottom:0}
.tools h2{font-size:22px;margin:34px 0 6px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.tools .sub{color:var(--muted);font-size:14.5px;margin:0 0 18px}
.toolcard{background:#fff;border:1px solid var(--line);border-radius:15px;padding:20px;margin:0 0 18px;
  box-shadow:0 8px 24px rgba(11,27,43,.05)}
.tgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.tgrid .full{grid-column:1/-1}
.tools label{display:block;font-size:11.5px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;
  color:#4A5763;margin:0 0 5px}
.tools input,.tools select,.tools textarea{width:100%;font-family:inherit;font-size:16px;padding:11px 12px;
  border:1px solid var(--line);border-radius:10px;background:#fff;color:var(--ink)}
.tools input:focus,.tools select:focus,.tools textarea:focus{outline:2px solid rgba(201,162,39,.45);outline-offset:1px}
.tools .btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;border:0;cursor:pointer;
  font-family:inherit;font-size:14.5px;font-weight:800;padding:13px 20px;border-radius:11px;min-height:48px}
.tools .btn-gold{background:linear-gradient(180deg,#DDB845,#BE9A1F);color:#2A1F00}
.tools .btn-line{background:#fff;border:1px solid var(--line);color:var(--navy)}
.tools .btn-sm{min-height:38px;padding:8px 13px;font-size:13px;border-radius:9px}
.tools .row{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end;margin-top:12px}
.tools .result{background:#F4F8F5;border:1px solid #CBE7DB;border-radius:12px;padding:14px 16px;margin-top:14px;font-size:15px}
.tools .result b{color:var(--navy)}
.tools .result .big{font-family:Georgia,serif;font-size:26px;color:var(--navy);display:block;margin:2px 0 4px}
.tools table.cases{width:100%;border-collapse:collapse;font-size:14px;margin-top:14px}
.tools table.cases th{background:#F3F0E9;text-align:left;padding:9px 10px;font-size:11px;letter-spacing:.05em;
  text-transform:uppercase;color:#4A5763;border-bottom:1px solid var(--line)}
.tools table.cases td{padding:10px;border-bottom:1px solid #F0EBE0;vertical-align:top}
.tools .badge{display:inline-block;font-size:11.5px;font-weight:800;border-radius:99px;padding:3px 9px;
  background:#EEF3F7;color:#3E4C59;border:1px solid #DDE6EE;white-space:nowrap}
.tools .badge.today{background:#FDECEC;border-color:#F3C9C9;color:#9B1C1C}
.tools .badge.week{background:#FFF7E2;border-color:#EBD9A4;color:#7A5E00}
.tools .badge.done{background:#EAF6F1;border-color:#CBE7DB;color:#1F7A5C}
.tools .hint{font-size:12.5px;color:#7A8794;line-height:1.55}
.tools .warn{background:var(--gold-soft);border:1px solid #EBD9A4;border-radius:11px;padding:12px 14px;
  font-size:13.5px;color:#5F4A00;margin:14px 0 0}
.tools .links a{display:inline-block;margin:0 14px 8px 0;font-size:14px;font-weight:700}
.tools .costline{display:flex;justify-content:space-between;gap:12px;padding:9px 0;border-bottom:1px dashed var(--line);font-size:14.5px}
.tools .costline b{white-space:nowrap}
.tools .costline.total{border-bottom:0;border-top:2px solid var(--navy);margin-top:6px;padding-top:11px;font-size:17px}
@media(max-width:820px){
  .tgrid{grid-template-columns:1fr 1fr}
  .tools input,.tools select,.tools textarea{font-size:16px}
  .tools table.cases{display:block;overflow-x:auto;white-space:nowrap}
  .tools .row .btn{width:100%}
  .tools h2{font-size:20px}
}
@media(max-width:520px){.tgrid{grid-template-columns:1fr}}
"""

BODY = """
<div class="tools">
<section class="hero"><div class="wrap">
  <div class="kicker">Free tools · no sign-up</div>
  <h1>Court tools</h1>
  <p>Three things a junior needs every court day: your own cause list, the next working date, and
     what filing actually costs. Everything runs inside your browser — nothing you type is sent
     to a server.</p>
</div></section>

<main class="wrap">

<!-- ============ 1. CAUSE-LIST TRACKER ============ -->
<h2 id="tracker">1. Cause-list tracker</h2>
<p class="sub">Your matters, your dates. Saved on this device only, so client names stay with you.</p>

<div class="toolcard">
  <div class="tgrid">
    <div><label>Case title</label><input id="cTitle" placeholder="ABC v XYZ"></div>
    <div><label>Court</label>
      <select id="cCourt">
        <option>City Courts, Karachi</option>
        <option>Sindh High Court</option>
        <option>Supreme Court</option>
        <option>Family Court</option>
        <option>District Court</option>
        <option>Special court / tribunal</option>
      </select>
    </div>
    <div><label>Case number</label><input id="cNo" placeholder="Suit 123/2026"></div>
    <div><label>Next date</label><input id="cDate" type="date"></div>
    <div class="full"><label>Note (optional)</label><input id="cNote" placeholder="Written statement due, bring original documents"></div>
  </div>
  <div class="row">
    <button class="btn btn-gold" onclick="addCase()">Add matter</button>
    <button class="btn btn-line" onclick="exportCases()">Export CSV</button>
    <button class="btn btn-line" onclick="window.print()">Print list</button>
  </div>
  <div id="caseWrap"></div>
  <p class="hint" style="margin-top:12px">Always check the official list the evening before. A date
     sent on WhatsApp is unconfirmed until you have seen it on the court list.</p>
  <p class="links" style="margin-top:6px">
    <a href="https://www.shc.gov.pk/" target="_blank" rel="noopener">Sindh High Court →</a>
    <a href="https://www.supremecourt.gov.pk/" target="_blank" rel="noopener">Supreme Court →</a>
  </p>
</div>

<!-- ============ 2. COURT-DAY CALCULATOR ============ -->
<h2 id="dates">2. Court-day calculator</h2>
<p class="sub">Count working days between two dates, or find the date N working days from today —
   skipping weekends and the holidays below.</p>

<div class="toolcard">
  <div class="tgrid">
    <div><label>From</label><input id="dFrom" type="date"></div>
    <div><label>Add working days</label><input id="dAdd" type="number" value="7" min="1" max="180"></div>
    <div><label>Saturday is</label>
      <select id="dSat"><option value="0">A holiday</option><option value="1">A working day</option></select>
    </div>
    <div><label>Or count between</label><input id="dTo" type="date"></div>
  </div>
  <div class="row">
    <button class="btn btn-gold" onclick="calcDates()">Calculate</button>
    <button class="btn btn-line" onclick="resetDates()">Reset</button>
  </div>
  <div id="dateResult"></div>

  <details style="margin-top:16px">
    <summary style="cursor:pointer;font-weight:700;font-size:14.5px">Holidays used in the count (2026)</summary>
    <table class="cases" id="holTable"></table>
    <p class="hint">Islamic dates depend on moon sighting and are announced by the government a day or
       two before. This list is a planning aid — confirm with your court office and the official
       notification before telling a client a date.</p>
  </details>
</div>

<!-- ============ 3. FILING COST ============ -->
<h2 id="fees">3. Filing cost worksheet</h2>
<p class="sub">Adds up what a fresh civil suit usually costs to file. Court fee is an estimate —
   the stamp vendor or the court office gives you the exact figure.</p>

<div class="toolcard">
  <div class="tgrid">
    <div><label>Suit value (Rs)</label><input id="fValue" type="number" value="500000" min="0" step="1000" oninput="estimateFee()"></div>
    <div><label>Court fee (Rs)</label><input id="fFee" type="number" min="0" step="100" oninput="calcCost()"></div>
    <div><label>Summons × process fee</label>
      <div style="display:flex;gap:8px">
        <input id="fSummons" type="number" value="2" min="0" oninput="calcCost()" style="max-width:80px">
        <input id="fPerSummon" type="number" value="500" min="0" step="100" oninput="calcCost()">
      </div>
    </div>
    <div><label>Copies: pages × rate</label>
      <div style="display:flex;gap:8px">
        <input id="fPages" type="number" value="40" min="0" oninput="calcCost()" style="max-width:80px">
        <input id="fPerPage" type="number" value="30" min="0" step="5" oninput="calcCost()" style="max-width:110px">
      </div>
    </div>
    <div><label>Vakalatnama / stamp paper (Rs)</label><input id="fVakalat" type="number" value="500" min="0" step="50" oninput="calcCost()"></div>
    <div><label>Other (affidavit, courier, misc.)</label><input id="fOther" type="number" value="1000" min="0" step="100" oninput="calcCost()"></div>
  </div>
  <div id="costResult" class="result" style="margin-top:16px"></div>
  <p class="warn"><b>Read this before you rely on the court fee.</b> The Court Fees Act 1870,
     Schedule I, Article 1 sets an ad valorem fee on the value of the subject matter, and the
     percentage and the ceiling have both been amended over the years. Treat the number above as a
     planning estimate only: the stamp vendor and the court office decide the exact fee, and a wrong
     fee comes back as a scrutiny objection.</p>
  <p class="links" style="margin-top:10px">
    <a href="https://www.shc.gov.pk/" target="_blank" rel="noopener">Sindh High Court →</a>
    <a href="../drafts/plaint-format/index.html">Plaint format →</a>
    <a href="../drafts/vakalatnama-format/index.html">Vakalatnama format →</a>
  </p>
</div>

</main>
</div>
"""

JS = """
/* ---------------- cause-list tracker ---------------- */
const CKEY = 'wb.cases';
function loadCases(){ try { return JSON.parse(localStorage.getItem(CKEY) || '[]'); } catch(e) { return []; } }
function saveCases(list){ try { localStorage.setItem(CKEY, JSON.stringify(list)); } catch(e) {} }

function dayDiff(d){
  if(!d) return null;
  const t = new Date(d + 'T00:00:00');
  if(isNaN(t)) return null;
  const n = new Date(); n.setHours(0,0,0,0);
  return Math.round((t - n)/86400000);
}
function pretty(d){
  const t = new Date(d + 'T00:00:00');
  if(isNaN(t)) return d || '';
  return t.toLocaleDateString('en-GB', {weekday:'short', day:'numeric', month:'short', year:'numeric'});
}
function esc(s){ return String(s==null?'':s).replace(/[&<>"']/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }

function addCase(){
  const title = document.getElementById('cTitle').value.trim();
  const date = document.getElementById('cDate').value;
  if(!title || !date){ alert('Case title and next date are both required.'); return; }
  const list = loadCases();
  list.push({
    id: Date.now(), title, court: document.getElementById('cCourt').value,
    no: document.getElementById('cNo').value.trim(),
    date, note: document.getElementById('cNote').value.trim(), done: false
  });
  saveCases(list);
  document.getElementById('cTitle').value = '';
  document.getElementById('cNo').value = '';
  document.getElementById('cNote').value = '';
  document.getElementById('cDate').value = '';
  renderCases();
}

function toggleCase(id){
  const list = loadCases().map(c => c.id === id ? Object.assign({}, c, {done: !c.done}) : c);
  saveCases(list); renderCases();
}
function removeCase(id){
  if(!confirm('Remove this matter from your list?')) return;
  saveCases(loadCases().filter(c => c.id !== id)); renderCases();
}

function renderCases(){
  const wrap = document.getElementById('caseWrap');
  const list = loadCases().sort((a,b) => String(a.date).localeCompare(String(b.date)));
  if(!list.length){
    wrap.innerHTML = '<p class="hint" style="margin-top:14px">Nothing saved yet. Add your first matter above — it stays in this browser.</p>';
    return;
  }
  const rows = list.map(c => {
    const d = dayDiff(c.date);
    let badge = '';
    if(c.done) badge = '<span class="badge done">done</span>';
    else if(d === null) badge = '';
    else if(d < 0) badge = '<span class="badge">' + Math.abs(d) + ' days ago</span>';
    else if(d === 0) badge = '<span class="badge today">today</span>';
    else if(d === 1) badge = '<span class="badge today">tomorrow</span>';
    else if(d <= 7) badge = '<span class="badge week">in ' + d + ' days</span>';
    else badge = '<span class="badge">in ' + d + ' days</span>';
    return `<tr>
      <td><b>${esc(c.title)}</b>${c.no ? '<br><span class="hint">' + esc(c.no) + '</span>' : ''}</td>
      <td>${esc(c.court)}</td>
      <td>${esc(pretty(c.date))}<br>${badge}</td>
      <td>${esc(c.note || '')}</td>
      <td style="white-space:nowrap">
        <button class="btn btn-line btn-sm" onclick="toggleCase(${c.id})">${c.done ? 'Reopen' : 'Done'}</button>
        <button class="btn btn-line btn-sm" onclick="removeCase(${c.id})">Remove</button>
      </td>
    </tr>`;
  }).join('');
  wrap.innerHTML = `<table class="cases">
    <thead><tr><th>Matter</th><th>Court</th><th>Next date</th><th>Note</th><th></th></tr></thead>
    <tbody>${rows}</tbody></table>`;
}

function exportCases(){
  const list = loadCases();
  if(!list.length){ alert('Nothing to export yet.'); return; }
  const rows = [['Case title','Court','Case number','Next date','Note','Done']]
    .concat(list.map(c => [c.title, c.court, c.no, c.date, c.note, c.done ? 'yes' : 'no']));
  const csv = rows.map(r => r.map(v => '"' + String(v == null ? '' : v).replace(/"/g,'""') + '"').join(',')).join('\\n');
  const a = document.createElement('a');
  a.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv);
  a.download = 'wakeelbano-cause-list.csv';
  a.click();
}

/* ---------------- court-day calculator ---------------- */
// Pakistan public holidays 2026. Islamic dates are subject to moon sighting.
const HOLIDAYS_2026 = [
  ['2026-02-05', 'Kashmir Solidarity Day'],
  ['2026-03-20', 'Eid-ul-Fitr (expected, confirm)'],
  ['2026-03-21', 'Eid-ul-Fitr (expected, confirm)'],
  ['2026-03-22', 'Eid-ul-Fitr (expected, confirm)'],
  ['2026-03-23', 'Pakistan Day'],
  ['2026-05-01', 'Labour Day'],
  ['2026-05-27', 'Eid-ul-Adha (expected, confirm)'],
  ['2026-05-28', 'Eid-ul-Adha (expected, confirm)'],
  ['2026-05-29', 'Eid-ul-Adha (expected, confirm)'],
  ['2026-06-24', 'Ashura (expected, confirm)'],
  ['2026-06-25', 'Ashura (expected, confirm)'],
  ['2026-08-14', 'Independence Day'],
  ['2026-08-25', 'Eid Milad-un-Nabi (expected, confirm)'],
  ['2026-11-09', 'Iqbal Day'],
  ['2026-12-25', 'Quaid-e-Azam Day']
];
const HOL = {}; HOLIDAYS_2026.forEach(h => HOL[h[0]] = h[1]);

function isHoliday(d, satWork){
  const key = d.toISOString().slice(0,10);
  const day = d.getDay();               // 0 Sun, 6 Sat
  if(day === 0) return 'Sunday';
  if(day === 6 && !satWork) return 'Saturday';
  return HOL[key] || null;
}
function resetDates(){
  const t = new Date();
  document.getElementById('dFrom').value = t.toISOString().slice(0,10);
  document.getElementById('dTo').value = '';
}
function calcDates(){
  const fromEl = document.getElementById('dFrom').value;
  if(!fromEl){ alert('Pick a start date first.'); return; }
  const satWork = document.getElementById('dSat').value === '1';
  const add = parseInt(document.getElementById('dAdd').value || '0', 10);
  const toEl = document.getElementById('dTo').value;

  let out = '';

  if(add > 0){
    let d = new Date(fromEl + 'T00:00:00');
    let counted = 0, skipped = [];
    while(counted < add){
      d.setDate(d.getDate() + 1);
      const why = isHoliday(d, satWork);
      if(why) skipped.push(d.toISOString().slice(0,10) + ' (' + why + ')');
      else counted++;
    }
    out += `<span class="big">${pretty(d.toISOString().slice(0,10))}</span>
      <b>${add} working day${add===1?'':'s'} after ${pretty(fromEl)}</b>
      ${skipped.length ? '<div class="hint" style="margin-top:8px">Skipped: ' + skipped.slice(0,8).join(', ') + (skipped.length > 8 ? ' …' : '') + '</div>' : ''}`;
  }

  if(toEl){
    let d = new Date(fromEl + 'T00:00:00');
    const end = new Date(toEl + 'T00:00:00');
    let working = 0, holidays = 0;
    if(end >= d){
      while(d < end){
        d.setDate(d.getDate() + 1);
        if(isHoliday(d, satWork)) holidays++; else working++;
      }
      out += `${out ? '<hr style="border:0;border-top:1px solid #CBE7DB;margin:12px 0">' : ''}
        <b>${working} working days</b> between ${pretty(fromEl)} and ${pretty(toEl)}
        <div class="hint" style="margin-top:6px">${holidays} weekend/holiday days fall in that range${satWork ? ' (Saturday counted as working)' : ' (Saturday counted as a holiday)'}.</div>`;
    } else {
      out += '<div class="hint">The end date is before the start date.</div>';
    }
  }

  document.getElementById('dateResult').innerHTML = out
    ? '<div class="result">' + out + '</div>'
    : '<div class="result">Add a number of working days, or pick a second date to count between.</div>';
}

/* ---------------- filing cost ---------------- */
const FEE_RATE = 0.085;      // Court Fees Act 1870, Sch. I, Art. 1 — ad valorem, amended over time
const FEE_CAP  = 34000;      // commonly cited ceiling; confirm the current figure at the court office

function money(n){ return 'Rs ' + Math.round(n).toLocaleString('en-PK'); }

function estimateFee(){
  const v = parseFloat(document.getElementById('fValue').value || '0');
  const raw = v * FEE_RATE;
  const fee = Math.min(raw, FEE_CAP);
  document.getElementById('fFee').value = Math.round(fee);
  calcCost();
}

function calcCost(){
  const num = id => parseFloat(document.getElementById(id).value || '0') || 0;
  const fee = num('fFee');
  const processFee = num('fSummons') * num('fPerSummon');
  const copies = num('fPages') * num('fPerPage');
  const vakalat = num('fVakalat');
  const other = num('fOther');
  const total = fee + processFee + copies + vakalat + other;
  const value = num('fValue');

  document.getElementById('costResult').innerHTML = `
    <div class="costline"><span>Court fee on ${money(value)}</span><b>${money(fee)}</b></div>
    <div class="costline"><span>Process fee (${num('fSummons')} × ${money(num('fPerSummon'))})</span><b>${money(processFee)}</b></div>
    <div class="costline"><span>Copies (${num('fPages')} pages)</span><b>${money(copies)}</b></div>
    <div class="costline"><span>Vakalatnama and stamp paper</span><b>${money(vakalat)}</b></div>
    <div class="costline"><span>Other (affidavit, courier, misc.)</span><b>${money(other)}</b></div>
    <div class="costline total"><span>Estimated total to file</span><b>${money(total)}</b></div>`;
}

function renderHolidays(){
  const t = document.getElementById('holTable');
  if(!t) return;
  t.innerHTML = '<thead><tr><th>Date</th><th>Holiday</th></tr></thead><tbody>' +
    HOLIDAYS_2026.map(h => `<tr><td>${pretty(h[0])}</td><td>${h[1]}</td></tr>`).join('') + '</tbody>';
}

/* ---------------- boot ---------------- */
(function(){
  const t = new Date();
  const f = document.getElementById('dFrom');
  if(f) f.value = t.toISOString().slice(0,10);
  renderCases();
  renderHolidays();
  estimateFee();
})();
"""


def build():
    title = "Court tools for Pakistani lawyers — cause list, working days and filing costs | WakeelBano"
    desc = ("Free court tools: a cause-list tracker for your own matters, a working-day calculator that "
            "skips weekends and court holidays, and a filing cost worksheet. No sign-up, nothing leaves "
            "your browser.")[:158]

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebApplication",
                "name": "WakeelBano Court Tools",
                "applicationCategory": "BusinessApplication",
                "operatingSystem": "Any",
                "url": BP.BASE + "tools/",
                "description": desc,
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "PKR"},
                "featureList": ["Cause-list tracker", "Working-day and court holiday calculator",
                                "Filing cost worksheet"],
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": BP.BASE},
                    {"@type": "ListItem", "position": 2, "name": "Court tools",
                     "item": BP.BASE + "tools/"},
                ],
            },
        ],
    }

    body = BP.crumbs("../", "Court tools", []) + BODY + f"<script>{JS}</script>"
    html = BP.page(title, desc, "tools/", body, "tools/", schema, extra_css=CSS)

    out = os.path.join(ROOT, "tools")
    os.makedirs(out, exist_ok=True)
    io.open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)
    print("tools/index.html written")


if __name__ == "__main__":
    build()
