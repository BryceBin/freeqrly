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
  country TEXT NOT NULL,
  device TEXT NOT NULL,
  count INTEGER DEFAULT 0,
  PRIMARY KEY (code, date, country, device)
);

CREATE TABLE IF NOT EXISTS create_limits (
  ip TEXT NOT NULL,
  hour TEXT NOT NULL,
  count INTEGER DEFAULT 0,
  PRIMARY KEY (ip, hour)
);
