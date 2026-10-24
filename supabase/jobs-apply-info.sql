-- WakeelBano — what a lawyer needs before applying
-- Adds the two columns the alert email and the job cards show.
-- Run once in Supabase → SQL Editor → Run.

alter table public.jobs add column if not exists deadline     date;
alter table public.jobs add column if not exists how_to_apply text;

-- deadline: only a date the source actually states. Null means "not stated",
--           which the email shows as "confirm on the source page" rather than guessing.
-- how_to_apply: one short instruction, filled by scripts/jobs_apply_info.py.
--           Re-run that script after adding new postings:
--               python3 scripts/jobs_apply_info.py --apply

create index if not exists jobs_deadline_idx on public.jobs (deadline) where status = 'live';

select count(*) as jobs,
       count(how_to_apply) as with_apply_note,
       count(deadline) as with_last_date
from public.jobs;
