# WakeelBano database — setup in 10 minutes

The site runs today in **demo mode** (data stays in the visitor's browser). These steps make
jobs, profiles, applications and ratings **real and shared**. Everything here uses Supabase's
free tier — no card needed.

---

## 1. Create the project

1. Go to **[supabase.com](https://supabase.com)** → *Start your project* → sign in with GitHub
   (`Sarmads050`).
2. *New project*: name `wakeelbano`, region **Southeast Asia (Singapore)** — closest to Pakistan,
   database password: generate one and save it somewhere safe.
3. Wait ~2 minutes for the project to finish provisioning.

## 2. Create the tables

1. In the left sidebar open **SQL Editor** → *New query*.
2. Open `supabase/schema.sql` from this repo, copy **everything**, paste it, press **Run**.
   You should see *Success. No rows returned*.
3. New query again → paste **all of `supabase/seed.sql`** → **Run**.
   It inserts the 18 job openings, 6 tasks and 8 lawyer profiles, and finishes with a count row
   (`jobs 18 | tasks 6 | lawyers 8`).

## 3. Copy the two keys

Sidebar → **Project Settings** → **API**:

| What Supabase calls it | Where it goes |
|---|---|
| **Project URL** (`https://xxxx.supabase.co`) | `SUPABASE_URL` |
| **anon / public** key (long `eyJ…`) | `SUPABASE_ANON_KEY` |

Open `assets/supabase-config.js` in this repo and paste them:

```js
window.WB_CONFIG = {
  SUPABASE_URL: "https://xxxx.supabase.co",
  SUPABASE_ANON_KEY: "eyJhbGciOi..."
};
```

> The anon key is meant to be public — it ships inside every browser app. The table rules in
> `schema.sql` are what protect the data. **Never** paste the `service_role` key here.

Then rebuild, commit and push:

```bash
python3 scripts/build_jobs.py && python3 scripts/validate.py
bash scripts/push.sh "Connect the live Supabase database"
```

Within a minute the banner at the top of `/jobs/` changes from *Demo mode* to
**Live database connected**, and everything written by one visitor is visible to the next.

## 4. Test it (2 minutes)

1. Open `https://sarmads050.github.io/wakeelbano/jobs/` — the green banner should appear.
2. Post a test job in the **Post a job** tab.
3. In another browser or on your phone, open the same page — the job should be in the list.
4. Rate a lawyer, then check Supabase → **Table Editor** → `ratings`: the row is there.
5. Delete your test job in the Table Editor when finished.

## 5. Where to look when something is wrong

| Symptom | Cause | Fix |
|---|---|---|
| Banner still says *Demo mode* | keys empty or the file was not deployed | re-check `assets/supabase-config.js`, hard-refresh (Ctrl+Shift+R) |
| Page loads but lists are empty | `schema.sql` not run, or RLS blocked the read | run the schema again, then check **Table Editor** has rows |
| "Could not save…" on apply/profile | policies missing | run the `create policy` block at the end of `schema.sql` |
| "already been rated for that job" | working as designed | one rating per job — that is what makes ratings trustworthy |

## 6. Keeping it current

- **Job list:** edit `scripts/jobs_data.py`, then
  `python3 scripts/build_jobs.py && python3 scripts/gen_supabase.py` and run the new
  `supabase/seed.sql` in the SQL Editor. Delete expired rows in **Table Editor → jobs**.
- **Moderating posts:** user-posted jobs carry `posted_by` = the poster's device key and
  `source = 'Posted on WakeelBano'`. Filter on that column to review them.
- **Hardening before serious traffic:** follow the "hardening" block at the bottom of
  `schema.sql` — anonymous sign-in, an `owner` column, and owner-scoped update policies.
- **Backups:** free tier keeps daily backups for 7 days. Export CSV from the Table Editor
  monthly for your own copy.
