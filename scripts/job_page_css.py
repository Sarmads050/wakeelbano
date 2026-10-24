# -*- coding: utf-8 -*-
"""WakeelBano — the stylesheet for /jobs/<id>/ pages.

Kept in its own file so the design can change without touching the generator.
Everything is scoped under .job-page so it cannot leak into other page types.
"""
CSS = """
.job-page .hero{padding:30px 0 34px;margin-bottom:0}
.job-page .hero .org-line{font-size:17px;color:#E3EBF2;margin:6px 0 0;font-weight:600}
.job-page .hero .org-line span{color:#93A6B5;font-weight:400}
.job-page .hero .pills{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}
.job-page .pill{font-size:13px;font-weight:700;color:#0B2540;background:#E8EEF4;border:1px solid rgba(255,255,255,.18);
  padding:5px 11px;border-radius:99px}
.job-page .pill.gold{background:linear-gradient(180deg,#E7CE7A,#D2B14A);color:#2A1F00;border-color:transparent}
.job-page .pill.warn{background:#FDECEC;color:#9B1C1C;border-color:#F3C9C9}
.job-page .pill.ghost{background:rgba(255,255,255,.1);color:#DCE7EF}

.job-page main{padding-top:26px;padding-bottom:10px}
.job-page .jobgrid{display:grid;grid-template-columns:minmax(0,1fr) 322px;gap:30px;align-items:start}
.job-page .col-main{min-width:0}
.job-page .col-side{position:sticky;top:80px}

/* snapshot */
.job-page .snap{background:#fff;border:1px solid var(--line);border-radius:14px;padding:6px 18px;margin:0 0 22px}
.job-page .snap dl{display:grid;grid-template-columns:1fr 1fr;gap:0;margin:0}
.job-page .snap .cell{padding:12px 0;border-top:1px solid #F0EBE0}
.job-page .snap .cell:nth-child(-n+2){border-top:0}
.job-page .snap dt{font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;color:#7A8794;font-weight:800;margin:0 0 3px}
.job-page .snap dd{margin:0;font-size:15.5px;font-weight:700;color:var(--navy);line-height:1.4}

/* deadline banner */
.job-page .deadline{display:flex;gap:12px;align-items:flex-start;border-radius:12px;padding:14px 16px;margin:0 0 26px;
  background:#FFF8E6;border:1px solid #EBD9A4;color:#5F4A00;font-size:14.5px;line-height:1.55}
.job-page .deadline.urgent{background:#FDEFEF;border-color:#F0C9C9;color:#8C1C1C}
.job-page .deadline.none{background:#F4F7FA;border-color:#E1E8EE;color:#44525F}
.job-page .deadline b{display:block;font-size:15px;margin-bottom:2px}

/* sections */
.job-page h2{font-size:22px;margin:32px 0 12px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.job-page .lead{font-size:16.5px;color:#33424F;margin:0 0 18px;line-height:1.7}
.job-page ol.steps li{font-size:15px;line-height:1.6;color:#33424F}
.job-page ol.steps li b{color:var(--navy)}
.job-page .check{list-style:none;padding:0;margin:0 0 8px}
.job-page .check li{position:relative;padding:11px 15px 11px 44px;background:#fff;border:1px solid var(--line);
  border-radius:11px;margin:0 0 9px;font-size:15px;color:#33424F}
.job-page .check li:before{content:"";position:absolute;left:15px;top:15px;width:16px;height:16px;border-radius:5px;
  background:var(--gold-soft);border:1px solid #E0CD9A}
.job-page .check li b{color:var(--navy)}

/* apply card */
.job-page .applycard{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px;
  box-shadow:0 10px 30px rgba(11,27,43,.08)}
.job-page .applycard .pay{font-family:Georgia,serif;font-size:23px;font-weight:700;color:var(--navy);line-height:1.2}
.job-page .applycard .pay small{display:block;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:#7A8794;font-weight:800;margin-bottom:4px}
.job-page .applycard .rowline{display:flex;justify-content:space-between;gap:10px;font-size:14px;padding:9px 0;
  border-top:1px solid #F0EBE0;color:#44525F}
.job-page .applycard .rowline b{color:var(--navy);text-align:right}
.job-page .applycard .rowline:first-of-type{border-top:0}
.job-page .btn-apply{display:block;text-align:center;margin:16px 0 10px;padding:15px 18px;border-radius:11px;border:0;
  background:linear-gradient(180deg,#DDB845,#BE9A1F);color:#2A1F00;font-size:16.5px;font-weight:800;
  letter-spacing:.01em;box-shadow:0 6px 16px rgba(190,154,31,.28)}
.job-page .btn-apply:hover{filter:brightness(1.04)}
.job-page .applycard .note{font-size:12.5px;color:#7A8794;line-height:1.55;margin:0}
.job-page .applycard .verified{display:flex;align-items:center;gap:7px;font-size:12.5px;color:#1F7A5C;
  background:#EAF6F1;border:1px solid #CBE7DB;border-radius:9px;padding:8px 10px;margin:12px 0 0}
.job-page .btn-apply-bottom{display:none}

@media(max-width:900px){
  .job-page .jobgrid{grid-template-columns:1fr;gap:22px}
  .job-page .col-side{position:static;order:-1}
  .job-page .snap .cell{padding:10px 0}
  .job-page .btn-apply-bottom{display:block;margin:24px 0 0;text-align:center;padding:16px;border-radius:11px;
    background:linear-gradient(180deg,#DDB845,#BE9A1F);color:#2A1F00;font-size:16.5px;font-weight:800}
}
"""
