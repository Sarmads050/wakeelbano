-- Removes the connectivity-check rows created while connecting the live database.
-- Paste into Supabase → SQL Editor → Run.
delete from public.jobs         where id = 'probe1' or title like 'SETUP TEST%' or posted_by = 'setup_probe';
delete from public.applications where device_key = 'setup_probe' or job_title like 'SETUP TEST%';
delete from public.ratings      where device_key = 'setup_probe' or lawyer_id = 'setup_probe';
delete from public.profiles     where device_key = 'setup_probe';

select 'jobs' as table_name, count(*) from public.jobs
union all select 'tasks', count(*) from public.tasks
union all select 'lawyers', count(*) from public.lawyers
union all select 'applications', count(*) from public.applications
union all select 'ratings', count(*) from public.ratings;
