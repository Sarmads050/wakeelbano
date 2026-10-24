-- WakeelBano — job alert subscriptions
-- Run once in Supabase → SQL Editor → Run.

create extension if not exists "pgcrypto";

create table if not exists public.subscribers (
  id           uuid primary key default gen_random_uuid(),
  email        text,
  whatsapp     text,
  city         text default 'All cities',
  area         text default 'All areas',
  keyword      text,
  level        text,                                  -- student | fresh | junior | senior
  status       text not null default 'active',        -- active | paused | bounced
  opt_in       boolean not null default true,
  device_key   text,
  last_sent_at timestamptz,
  created_at   timestamptz not null default now(),
  constraint contact_required check (email is not null or whatsapp is not null)
);

-- one subscription per email / per number
create unique index if not exists subscribers_email_idx on public.subscribers (lower(email)) where email is not null;
create unique index if not exists subscribers_wa_idx on public.subscribers (whatsapp) where whatsapp is not null;
create index if not exists subscribers_created_idx on public.subscribers (created_at desc);

alter table public.subscribers enable row level security;

-- anyone can subscribe
drop policy if exists subscribers_insert on public.subscribers;
create policy subscribers_insert on public.subscribers for insert with check (true);

-- only a signed-in admin can read, change or delete
drop policy if exists subscribers_read on public.subscribers;
drop policy if exists subscribers_update on public.subscribers;
drop policy if exists subscribers_delete on public.subscribers;
create policy subscribers_read   on public.subscribers for select to authenticated using (true);
create policy subscribers_update on public.subscribers for update to authenticated using (true) with check (true);
create policy subscribers_delete on public.subscribers for delete to authenticated using (true);

-- a subscriber may unsubscribe themselves by updating their own row through the
-- unsubscribe link (matched on device_key) — handled by the app, not by an open policy.

grant insert on public.subscribers to anon;
grant select, insert, update, delete on public.subscribers to authenticated;

select 'subscribers ready' as result, (select count(*) from public.subscribers) as existing;
