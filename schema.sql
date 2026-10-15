-- FreeQrly dynamic QR codes — D1 schema
-- Apply: wrangler d1 execute freeqrly --file=schema.sql
-- Or paste into Cloudflare Dashboard → D1 → freeqrly → Console

CREATE TABLE IF NOT EXISTS codes (
  code TEXT PRIMARY KEY,
  destination TEXT NOT NULL,
  edit_key_hash TEXT NOT NULL,
  created_at INTEGER NOT NULL,
  total_scans INTEGER DEFAULT 0
);

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
