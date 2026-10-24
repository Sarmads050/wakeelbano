-- WakeelBano — Supabase schema
-- Run this once in Supabase → SQL Editor → New query → paste → Run.
--
-- Tables: jobs, tasks, lawyers, profiles, applications, ratings
-- Security model (pilot): public can READ jobs, tasks and lawyers.
-- Anyone with the anon key can INSERT applications and ratings, and insert/update
-- a profile that carries its own random device_key. The device_key is generated in
-- the browser and never shown, which keeps the app usable without asking a junior
-- lawyer to create an account. Hardening path is at the bottom of this file.

create extension if not exists "pgcrypto";

-- ---------------------------------------------------------------- jobs
create table if not exists public.jobs (
  id           text primary key,
  title        text not null,
  org          text not null,
  city         text not null,
  area         text not null,
  job_type     text,
  experience   text,
  pay          text,
  description  text,
  contact      text,
  tags         text[] default '{}',
  source       text,
  source_url   text,
  posted_at    date default current_date,
  status       text not null default 'live',   -- live | closed | pending
  posted_by    text,                           -- device_key of the recruiter, if user-posted
  created_at   timestamptz not null default now()
);

-- ---------------------------------------------------------------- tasks
create table if not exists public.tasks (
  id           text primary key,
  title        text not null,
  category     text,
  city         text,
  pay          text,
  turnaround   text,
  posted_for   text,
  description  text,
  status       text not null default 'open',   -- open | assigned | done
  created_at   timestamptz not null default now()
);

-- ---------------------------------------------------------------- lawyers
create table if not exists public.lawyers (
  id           text primary key,
  name         text not null,
  city         text not null,
  area         text not null,
  chamber      text,
  enrolled     int,
  cases        int default 0,
  skills       text[] default '{}',
  rate         text,
  bio          text,
  verified     boolean default false,
  seed_rating  numeric(2,1) default 0,          -- rating from completed work before launch
  seed_reviews int default 0,
  status       text not null default 'live',
  created_at   timestamptz not null default now()
);

-- ---------------------------------------------------------------- profiles
-- A lawyer's own profile, created from the site. Keyed by a random device_key
-- stored in the browser, so no signup is needed during the pilot.
create table if not exists public.profiles (
  id           uuid primary key default gen_random_uuid(),
  device_key   text not null unique,
  name         text not null,
  city         text not null,
  area         text not null,
  chamber      text,
  cases        int default 0,
  skills       text[] default '{}',
  rate         text,
  bio          text,
  public       boolean not null default true,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now()
);

-- ---------------------------------------------------------------- applications
create table if not exists public.applications (
  id           uuid primary key default gen_random_uuid(),
  job_id       text,
  job_title    text not null,
  org          text,
  name         text not null,
  phone        text not null,
  note         text,
  device_key   text,
  status       text not null default 'sent',    -- sent | shortlisted | hired | rejected
  created_at   timestamptz not null default now()
);

-- ---------------------------------------------------------------- ratings
-- One rating per completed job: the unique constraint is what makes ratings real.
create table if not exists public.ratings (
  id           uuid primary key default gen_random_uuid(),
  lawyer_id    text,          -- id from public.lawyers, or a profiles.id
  job_id       text,
  stars        int not null check (stars between 1 and 5),
  review       text,
  rater_name   text,
  device_key   text,
  created_at   timestamptz not null default now(),
  unique (lawyer_id, job_id)
);

-- ---------------------------------------------------------------- aggregates
create or replace view public.lawyer_ratings as
select lawyer_id,
       round(avg(stars)::numeric, 2) as avg_stars,
       count(*)                      as review_count
from public.ratings
group by lawyer_id;

-- ---------------------------------------------------------------- RLS
alter table public.jobs         enable row level security;
alter table public.tasks        enable row level security;
alter table public.lawyers      enable row level security;
alter table public.profiles     enable row level security;
alter table public.applications enable row level security;
alter table public.ratings      enable row level security;

-- read: public listings
drop policy if exists jobs_read   on public.jobs;
drop policy if exists tasks_read  on public.tasks;
drop policy if exists lawyers_read on public.lawyers;
drop policy if exists profiles_read on public.profiles;
drop policy if exists ratings_read on public.ratings;
create policy jobs_read    on public.jobs    for select using (status = 'live');
create policy tasks_read   on public.tasks   for select using (status = 'open');
create policy lawyers_read on public.lawyers for select using (status = 'live');
create policy profiles_read on public.profiles for select using (public = true);
create policy ratings_read  on public.ratings  for select using (true);

-- write: recruiting actions are open during the pilot
drop policy if exists jobs_insert on public.jobs;
drop policy if exists applications_insert on public.applications;
drop policy if exists profiles_insert on public.profiles;
drop policy if exists profiles_update on public.profiles;
drop policy if exists ratings_insert on public.ratings;
create policy jobs_insert on public.jobs for insert with check (status = 'live');
create policy applications_insert on public.applications for insert with check (true);
create policy profiles_insert on public.profiles for insert with check (true);
create policy profiles_update on public.profiles for update using (true) with check (true);
create policy ratings_insert on public.ratings for insert with check (stars between 1 and 5);

-- Helpful indexes
create index if not exists jobs_city_idx      on public.jobs (city);
create index if not exists jobs_area_idx      on public.jobs (area);
create index if not exists jobs_posted_idx    on public.jobs (posted_at desc);
create index if not exists lawyers_city_idx   on public.lawyers (city);
create index if not exists applications_job_idx on public.applications (job_id);
create index if not exists ratings_lawyer_idx on public.ratings (lawyer_id);

-- ---------------------------------------------------------------- API grants
-- These make the tables reachable by the public key regardless of the
-- "Automatically expose new tables" toggle. RLS above still decides which rows
-- are visible, so grants without policies would expose nothing.
grant usage on schema public to anon, authenticated;
grant select on public.jobs, public.tasks, public.lawyers, public.profiles,
                public.ratings, public.lawyer_ratings to anon, authenticated;
grant insert on public.jobs, public.applications, public.ratings, public.profiles
                to anon, authenticated;
grant update on public.profiles to anon, authenticated;

-- ---------------------------------------------------------------- hardening (later)
-- 1. Turn on Supabase Authentication → Providers → Anonymous sign-ins.
-- 2. Add an owner column: alter table public.profiles add column owner uuid default auth.uid();
-- 3. Replace the open update policy with:
--      create policy profiles_update on public.profiles
--        for update using (owner = auth.uid()) with check (owner = auth.uid());
-- 4. Same pattern for applications and ratings (applicant_id = auth.uid()).
-- 5. Turn job posting into an authenticated, moderated action: status = 'pending'
--    on insert, and only you approve it to 'live' from the Supabase table editor.
