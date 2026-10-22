-- FreeQrly — D1 schema (database `freeqrly`)
-- This file mirrors the LIVE database. Apply new statements with:
--   wrangler d1 execute freeqrly --remote --command "<SQL>"
-- (CREATE TABLE / INDEX statements below are all IF NOT EXISTS, so re-running is safe.)
--
-- Migrations applied to LIVE (2026-10-16, auth changes):
--   ALTER TABLE users ADD COLUMN password_hash TEXT;
--   CREATE TABLE login_lockouts (see below).
-- Migrations applied to LIVE (2026-10-16, ATT removal):
--   ALTER TABLE codes DROP COLUMN edit_key_hash (no EditKey / claim flow);
--   UPDATE users SET code_limit = 8 (free quota 3 -> 8).
-- Migrations applied to LIVE (2026-10-18, API tokens):
--   CREATE TABLE api_tokens (see below).

-- Dynamic QR codes. user_id is NULL for anonymous codes created before
-- login was required; those keep redirecting but cannot be edited.
-- All codes created now are session-owned (user_id set).
CREATE TABLE IF NOT EXISTS codes (
  code TEXT PRIMARY KEY,
  destination TEXT NOT NULL,
  created_at INTEGER NOT NULL,
  total_scans INTEGER DEFAULT 0,
  type TEXT DEFAULT 'url',
  payload TEXT,
  user_id TEXT,
  -- Saved QR style (JSON): { fg, bg, transparent, dots, ecc, frame, frameText, logoPreset, logoKey }.
  -- NULL for codes created before style saving; those render with defaults.
  style TEXT
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
  code_limit INTEGER NOT NULL DEFAULT 20,
  created_at INTEGER NOT NULL,
  last_login_at INTEGER,
  -- PBKDF2-SHA256 hash for email+password accounts: pbkdf2$100000$<salt_b64>$<hash_b64>.
  -- NULL for OAuth / magic-link-only accounts. Never returned by any API.
  password_hash TEXT
);

-- Sessions store only the SHA-256 hash of the opaque fq_session cookie token.
-- auth_method records HOW this session signed in ('password' | 'email' |
-- 'google' | 'github') so the UI can show the real sign-in channel.
-- NULL = session predates the column; callers fall back to users.auth_provider.
CREATE TABLE IF NOT EXISTS sessions (
  token_hash TEXT PRIMARY KEY,
  user_id TEXT NOT NULL REFERENCES users(id),
  created_at INTEGER NOT NULL,
  expires_at INTEGER NOT NULL,
  user_agent TEXT,
  ip TEXT,
  auth_method TEXT
);

-- One-time email tokens (email verification, password reset).
-- Only SHA-256 hashes are stored. Single-use (used=1 after consume).
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

-- Login lockout: 5 failed password attempts per IP+email → 15 min lockout.
-- key = SHA-256 hex of "<ip>|<lowercase email>". failures resets to 1 once a
-- lockout expires; a successful login deletes the row.
CREATE TABLE IF NOT EXISTS login_lockouts (
  key TEXT PRIMARY KEY,
  failures INTEGER NOT NULL DEFAULT 0,
  locked_until INTEGER NOT NULL DEFAULT 0,
  updated_at INTEGER NOT NULL
);

-- API tokens for programmatic access (REST + MCP). Only the SHA-256 hash is
-- stored; the raw token (fqly_<43 base64url chars>) is shown once at creation.
-- Token management (create/list/revoke) requires a login session; a token
-- grants the same dynamic-code powers as the Dashboard UI (quota enforced).
CREATE TABLE IF NOT EXISTS api_tokens (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL REFERENCES users(id),
  name TEXT NOT NULL,
  token_hash TEXT NOT NULL UNIQUE,
  prefix TEXT NOT NULL,
  created_at INTEGER NOT NULL,
  last_used_at INTEGER,
  revoked_at INTEGER
);
CREATE INDEX IF NOT EXISTS idx_api_tokens_user ON api_tokens(user_id);

-- Paid tier (2026-10-22, Waffo Pancake as MoR). One row per Waffo subscription
-- order. users.plan mirrors the live state ('pro' while a subscription here is
-- active / canceling / past_due); quota resolution lives in _lib/billing.js.
CREATE TABLE IF NOT EXISTS subscriptions (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL REFERENCES users(id),
  provider TEXT NOT NULL DEFAULT 'waffo',
  waffo_order_id TEXT UNIQUE,
  buyer_email TEXT,
  period TEXT,
  status TEXT NOT NULL DEFAULT 'active',
  current_period_end TEXT,
  created_at INTEGER NOT NULL,
  updated_at INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_subscriptions_user ON subscriptions(user_id);

-- Waffo webhook idempotency: event_key = "<eventType>:<eventId>".
CREATE TABLE IF NOT EXISTS webhook_events (
  event_key TEXT PRIMARY KEY,
  received_at INTEGER NOT NULL
);
