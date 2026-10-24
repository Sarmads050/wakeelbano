/* WakeelBano data layer.
 *
 * Works in two modes with one API:
 *   cloud  - Supabase configured in assets/supabase-config.js (real, shared data)
 *   local  - no config: everything is stored in this browser (demo / offline)
 *
 * Every page calls WB.* and never touches Supabase directly, so switching modes
 * needs no other change.
 */
(function (global) {
  var cfg = global.WB_CONFIG || {};
  var client = null;
  var mode = "local";

  function init() {
    if (global.supabase && cfg.SUPABASE_URL && cfg.SUPABASE_ANON_KEY &&
        cfg.SUPABASE_URL.indexOf("YOUR-") === -1) {
      try {
        client = global.supabase.createClient(cfg.SUPABASE_URL, cfg.SUPABASE_ANON_KEY);
        mode = "cloud";
      } catch (e) { mode = "local"; }
    }
    return mode;
  }

  /* ------------------------------------------------ local helpers */
  function lsGet(k, d) {
    try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; }
  }
  function lsSet(k, v) {
    try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {}
  }
  function deviceKey() {
    var k = lsGet("wb.device", null);
    if (!k) {
      k = "d_" + Math.random().toString(36).slice(2) + Date.now().toString(36);
      lsSet("wb.device", k);
    }
    return k;
  }

  /* ------------------------------------------------ reads */
  function mapJob(r) {
    return {
      id: r.id, t: r.title, org: r.org, city: r.city, area: r.area, type: r.job_type || "",
      exp: r.experience || "Not stated", pay: r.pay || "Not stated",
      desc: r.description || "", tags: r.tags || [], src: r.source || "WakeelBano",
      url: r.source_url || "", posted: (r.posted_at || "").slice(0, 10)
    };
  }
  function mapTask(r) {
    return {
      id: r.id, t: r.title, cat: r.category || "", city: r.city || "", pay: r.pay || "",
      days: r.turnaround || "", by: r.posted_for || "", desc: r.description || ""
    };
  }
  function mapLawyer(r) {
    var stars = Number(r.avg_stars || 0);
    var count = Number(r.review_count || 0);
    return {
      id: r.id, n: r.name, city: r.city, area: r.area, chamber: r.chamber || "",
      since: r.enrolled, cases: r.cases || 0, skills: r.skills || [], rate: r.rate || "",
      rating: Number(r.seed_rating || 0), reviews: Number(r.seed_reviews || 0),
      liveRating: stars, liveReviews: count, verified: !!r.verified, bio: r.bio || ""
    };
  }

  async function listJobs() {
    if (mode === "cloud") {
      var res = await client.from("jobs").select("*")
        .eq("status", "live").order("posted_at", { ascending: false });
      if (!res.error && res.data) return res.data.map(mapJob);
    }
    return lsGet("wb.postedJobs", []);
  }

  async function listTasks() {
    if (mode === "cloud") {
      var res = await client.from("tasks").select("*").eq("status", "open");
      if (!res.error && res.data) return res.data.map(mapTask);
    }
    return lsGet("wb.postedTasks", []);
  }

  async function listLawyers() {
    if (mode === "cloud") {
      var res = await client.from("lawyers").select("*").eq("status", "live");
      var ratings = await client.from("lawyer_ratings").select("*");
      if (!res.error && res.data) {
        var byId = {};
        (ratings.data || []).forEach(function (x) { byId[x.lawyer_id] = x; });
        return res.data.map(function (r) {
          var combined = Object.assign({}, r, byId[r.id] || {});
          return mapLawyer(combined);
        });
      }
    }
    return [];
  }

  async function listProfile() {
    var key = deviceKey();
    if (mode === "cloud") {
      var res = await client.from("profiles").select("*").eq("device_key", key).maybeSingle();
      if (!res.error && res.data) {
        var p = res.data;
        return { name: p.name, city: p.city, area: p.area, chamber: p.chamber || "",
                 cases: p.cases || "", skills: (p.skills || []).join(", "),
                 rate: p.rate || "", bio: p.bio || "" };
      }
      return null;
    }
    return lsGet("wb.profile", null);
  }

  async function listMyRatings() {
    return lsGet("wb.ratings", {});
  }

  /* ------------------------------------------------ writes */
  async function saveProfile(p) {
    if (mode === "cloud") {
      var row = {
        device_key: deviceKey(), name: p.name, city: p.city, area: p.area,
        chamber: p.chamber || null, cases: parseInt(p.cases, 10) || 0,
        skills: (p.skills || "").split(",").map(function (s) { return s.trim(); }).filter(Boolean),
        rate: p.rate || null, bio: p.bio || null, updated_at: new Date().toISOString()
      };
      var res = await client.from("profiles").upsert(row, { onConflict: "device_key" });
      if (res.error) throw res.error;
      return { mode: "cloud" };
    }
    lsSet("wb.profile", p);
    return { mode: "local" };
  }

  async function apply(a) {
    if (mode === "cloud") {
      var res = await client.from("applications").insert({
        job_id: a.jobId || null, job_title: a.title, org: a.org || null,
        name: a.name, phone: a.phone, note: a.note || null, device_key: deviceKey()
      });
      if (res.error) throw res.error;
      return { mode: "cloud" };
    }
    var all = lsGet("wb.applications", []);
    all.push({ role: a.title, org: a.org, name: a.name, phone: a.phone,
               why: a.note, at: new Date().toISOString() });
    lsSet("wb.applications", all);
    return { mode: "local" };
  }

  async function postJob(j) {
    if (mode === "cloud") {
      var id = "u" + Date.now();
      var res = await client.from("jobs").insert({
        id: id, title: j.t, org: j.org, city: j.city, area: j.area,
        job_type: j.type, experience: j.exp, pay: j.pay, description: j.desc,
        contact: j.contact || null, tags: [], source: "Posted on WakeelBano",
        source_url: null, status: "live", posted_by: deviceKey()
      });
      if (res.error) throw res.error;
      return { mode: "cloud", id: id };
    }
    var list = lsGet("wb.postedJobs", []);
    var jid = "u" + Date.now();
    list.unshift(Object.assign({ id: jid, posted: new Date().toISOString().slice(0, 10),
                                 tags: [], src: "Posted on WakeelBano", url: "" }, j));
    lsSet("wb.postedJobs", list);
    return { mode: "local", id: jid };
  }

  async function rate(r) {
    if (mode === "cloud") {
      var res = await client.from("ratings").insert({
        lawyer_id: r.lawyerId, job_id: r.jobId || ("manual-" + Date.now()),
        stars: r.stars, review: r.review || null, rater_name: r.rater || null,
        device_key: deviceKey()
      });
      if (res.error) throw res.error;   /* the unique(lawyer_id, job_id) rule blocks double rating */
      return { mode: "cloud" };
    }
    var all = lsGet("wb.ratings", {});
    (all[r.lawyerId] = all[r.lawyerId] || []).push(
      { stars: r.stars, text: r.review || "", at: new Date().toISOString() });
    lsSet("wb.ratings", all);
    return { mode: "local" };
  }

  global.WB = {
    init: init,
    get mode() { return mode; },
    deviceKey: deviceKey,
    listJobs: listJobs,
    listTasks: listTasks,
    listLawyers: listLawyers,
    listProfile: listProfile,
    listMyRatings: listMyRatings,
    saveProfile: saveProfile,
    apply: apply,
    postJob: postJob,
    rate: rate
  };
})(window);
