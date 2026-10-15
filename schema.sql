-- FreeQrly — D1 schema (database `freeqrly`)
-- This file mirrors the LIVE database. Apply new statements with:
--   wrangler d1 execute freeqrly --remote --command "<SQL>"
-- (CREATE TABLE / INDEX statements below are all IF NOT EXISTS, so re-running is safe.)

-- Dynamic QR codes. user_id is NULL for anonymous codes; set when a signed-in
-- user creates a code or claims an anonymous one via /api/me/claims.
CREATE TABLE IF NOT EXISTS codes (
  code TEXT PRIMARY KEY,
  destination TEXT NOT NULL,
  edit_key_hash TEXT NOT NULL,
  created_at INTEGER NOT NULL,
  total_scans INTEGER DEFAULT 0,
  type TEXT DEFAULT 'url',
  payload TEXT,
  user_id TEXT
);
CREATE INDEX IF NOT EXISTS idx_codes_user ON codes(user_id);

CREATE TABLE IF NOT EXISTS daily_stats (
  code TEXT NOT NULL,
  date TEXT NOT NULL,
  country TEXT NOT NULL DEFAULT 'XX',
  city TEXT NOT NULL DEFAULT '',
  device TEXT NOT NULL DEFAULT 'desktop',
  os TEXT NOT NULL DEFAULT 'Other',
  count INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (code, date, country, city, device, os)
);

-- Unique scans: one row per (code, date, IP+UA hash). Fingerprint is SHA-256, not reversible.
CREATE TABLE IF NOT EXISTS scan_fingerprints (
  code TEXT NOT NULL,
  date TEXT NOT NULL,
  fingerprint TEXT NOT NULL,
  PRIMARY KEY (code, date, fingerprint)
);

CREATE TABLE IF NOT EXISTS create_limits (
  ip TEXT NOT NULL,
  hour TEXT NOT NULL,
  count INTEGER DEFAULT 0,
  PRIMARY KEY (ip, hour)
);

-- Tier 2 account system -------------------------------------------------------
CREATE TABLE IF NOT EXISTS users (
  id TEXT PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  email_verified INTEGER NOT NULL DEFAULT 1,
  name TEXT,
  avatar_url TEXT,
  auth_provider TEXT NOT NULL DEFAULT 'email',
  plan TEXT NOT NULL DEFAULT 'free',
  code_limit INTEGER NOT NULL DEFAULT 3,
  created_at INTEGER NOT NULL,
  last_login_at INTEGER
);

-- Sessions store only the SHA-256 hash of the opaque fq_session cookie token.
CREATE TABLE IF NOT EXISTS sessions (
  token_hash TEXT PRIMARY KEY,
  user_id TEXT NOT NULL REFERENCES users(id),
  created_at INTEGER NOT NULL,
  expires_at INTEGER NOT NULL,
  user_agent TEXT,
  ip TEXT
);

-- One-time email tokens (magic links). Only SHA-256 hashes are stored.
CREATE TABLE IF NOT EXISTS email_tokens (
  token_hash TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  purpose TEXT NOT NULL,
  expires_at INTEGER NOT NULL,
  used INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS abuse_reports (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL,
  reason TEXT,
  reporter_email TEXT,
  created_at INTEGER NOT NULL
);

-- Generic per-hour counters (magic-link per-email/per-IP, OAuth per-IP, abuse reports).
-- Same counting pattern as create_limits, keyed by purpose (e.g. 'magic:email:<sha256>').
CREATE TABLE IF NOT EXISTS rate_limits (
  key TEXT NOT NULL,
  hour TEXT NOT NULL,
  count INTEGER DEFAULT 0,
  PRIMARY KEY (key, hour)
);
