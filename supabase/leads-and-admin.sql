-- WakeelBano — leads + admin access
-- Run once in Supabase → SQL Editor → Run.

create extension if not exists "pgcrypto";

-- ---------------------------------------------------------------- leads
-- The "Join free" form on the home page writes here.
create table if not exists public.leads (
  id           uuid primary key default gen_random_uuid(),
  name         text not null,
  phone        text not null,
  stage        text,
  need         text,
  city         text,
  source       text default 'home-join',
  status       text not null default 'new',   -- new | contacted | joined | dropped
  device_key   text,
  created_at   timestamptz not null default now()
);

create index if not exists leads_created_idx on public.leads (created_at desc);

alter table public.leads enable row level security;

-- anyone may submit the form
drop policy if exists leads_insert on public.leads;
create policy leads_insert on public.leads for insert with check (true);

-- only a signed-in admin may read or delete
drop policy if exists leads_read on public.leads;
drop policy if exists leads_update on public.leads;
drop policy if exists leads_delete on public.leads;
create policy leads_read   on public.leads for select to authenticated using (true);
create policy leads_update on public.leads for update to authenticated using (true) with check (true);
create policy leads_delete on public.leads for delete to authenticated using (true);

-- ---------------------------------------------------------------- applications
-- Same rule for job applications: submit freely, read only when signed in.
drop policy if exists applications_read on public.applications;
drop policy if exists applications_delete on public.applications;
create policy applications_read   on public.applications for select to authenticated using (true);
create policy applications_delete on public.applications for delete to authenticated using (true);

-- ---------------------------------------------------------------- jobs moderation
-- Admins can close or remove user-posted jobs.
drop policy if exists jobs_update on public.jobs;
drop policy if exists jobs_delete on public.jobs;
create policy jobs_update on public.jobs for update to authenticated using (true) with check (true);
create policy jobs_delete on public.jobs for delete to authenticated using (true);

-- ---------------------------------------------------------------- profiles
drop policy if exists profiles_admin_read on public.profiles;
create policy profiles_admin_read on public.profiles for select to authenticated using (true);

grant select, insert, update, delete on public.leads to anon, authenticated;
grant select, delete on public.applications to authenticated;
grant update, delete on public.jobs to authenticated;

select 'leads table ready' as result,
       (select count(*) from public.leads) as existing_leads;
