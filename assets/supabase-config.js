/* WakeelBano — Supabase connection settings.
 *
 * Paste the two values from your Supabase project here:
 *   Supabase dashboard  →  Project Settings  →  API
 *     Project URL      →  SUPABASE_URL
 *     anon public key  →  SUPABASE_ANON_KEY
 *
 * The anon key is designed to be public (it is shipped in every browser app);
 * the database rules in supabase/schema.sql are what protect the data. Never put
 * the "service_role" key in this file.
 *
 * Leave both empty and the site runs in local demo mode.
 */
window.WB_CONFIG = {
  SUPABASE_URL: "",
  SUPABASE_ANON_KEY: ""
};
