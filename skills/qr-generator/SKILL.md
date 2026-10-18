---
name: qr-generator
description: "Generate QR codes via the FreeQrly API or MCP server: static QR codes (URL, WiFi, vCard, text, geo) as SVG. Free, no key, no sign-up. Use when the user asks to create a QR code, encode a link/WiFi/password/contact as QR, or needs a QR image in an agent workflow."
---

# FreeQrly QR Generator

FreeQrly (https://freeqrly.com) exposes QR generation for agents two ways.
Both are free, require no key, and produce **static** QR codes that never expire.

## Option A — MCP (preferred for MCP-capable agents)

Server: `https://freeqrly.com/mcp` (Streamable HTTP, no auth).

```json
{ "jsonrpc": "2.0", "id": 1, "method": "tools/call",
  "params": { "name": "generate_qr",
    "arguments": { "data": "https://example.com", "size": 1024 } } }
```

Tool `generate_qr` arguments:

| arg | type | default | notes |
|---|---|---|---|
| `data` | string, required | — | text to encode, max 2000 chars |
| `size` | integer | 1024 | 128–2048 px |
| `color` | string | `2F4A62` | 6-digit hex, no `#` |
| `bgcolor` | string | `ffffff` | 6-digit hex, no `#` |
| `ecc` | string | `M` | `L`, `M`, `Q`, `H` — use `Q`/`H` with logos or print |

Returns a ready-to-download SVG URL plus a one-line summary.

### Authenticated dynamic codes (MCP)

Pass `Authorization: Bearer <api_token>` (create one in the dashboard under
API Tokens — the user does this, never the agent). Five more tools appear:

| tool | arguments | notes |
|---|---|---|
| `dynamic_qr_create` | `type`, `payload` (required) | editable after printing; free quota 8/account |
| `dynamic_qr_list` | — | codes with scan counts + quota usage |
| `dynamic_qr_update` | `code`, `type`, `payload` (required) | printed QRs serve the new content instantly |
| `dynamic_qr_delete` | `code` (required) | frees one quota slot |
| `dynamic_qr_stats` | `code` (required) | scans by date, country, device |

`type` is one of `url text wifi vcard email sms phone geo event bitcoin coupon appstore`
(default `url`); `payload` max 8000 chars. Same validation and quota as the
dashboard UI. Without a token these tools return an auth error.

## Option B — plain HTTP API

```
GET https://freeqrly.com/api/qr?data=TEXT&size=1024&margin=4&color=2F4A62&bgcolor=ffffff&ecc=M
```

Returns `image/svg+xml` (CORS `*`). `data` is required; errors are JSON
with an `error` field and a 4xx status.

### Authenticated dynamic codes (HTTP)

Same Bearer token as above:

```
POST   /api/codes            {"type":"url","payload":"https://example.com"} → {"code","shortUrl"}
GET    /api/me/codes         list + {"quota":{"used","limit"}}
GET    /api/codes/{code}/stats
PATCH  /api/codes/{code}     {"type","payload"}
DELETE /api/codes/{code}
```

## Payload recipes

- Website: `https://example.com/menu`
- WiFi: `WIFI:T:WPA;S:CafeNet;P:s3cret;;` (T is WPA, WPA2, WEP, or nopass)
- Contact: `BEGIN:VCARD\nVERSION:3.0\nN:Ada Lovelace\nTEL:+15550100\nEMAIL:ada@example.com\nEND:VCARD`
- Location: `geo:37.7749,-122.4194`
- SMS: `sms:+15550100?body=Hello` · Call: `tel:+15550100` · Email: `mailto:hi@example.com`

## Guardrails

- Keep `data` under 2000 chars; longer payloads make denser, harder-to-scan codes.
- Dark modules on a light background scan best; avoid low contrast.
- For print, use `size` ≥ 1024 and `ecc` Q or H.
- The API is rate-limited per IP; cache results instead of re-requesting.
