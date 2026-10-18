// FreeQrly MCP server — Streamable HTTP (POST JSON-RPC), no key for static codes.
// POST /mcp
//   generate_qr (open): static QR -> /api/qr SVG URL. Free, no auth.
//   dynamic_qr_* (require `Authorization: Bearer <api_token>`):
//     create / list / update / delete / stats — the same dynamic codes as the
//     Dashboard UI, same per-user quota (free: 8). Create a token at
//     https://freeqrly.com/dashboard/ (API Tokens section).
import QR from './_lib/qrcode.js';
import { getApiTokenUser } from './_lib/auth.js';
import {
  VALID_TYPES,
  ApiError,
  createDynamicCode,
  updateDynamicCode,
  deleteDynamicCode,
  listDynamicCodes,
  getCodeStats,
} from './_lib/codes_api.js';

const qrcode = QR && QR.default ? QR.default : QR;
const HEX = /^[0-9a-fA-F]{6}$/;

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization',
  'Access-Control-Max-Age': '86400',
};

const AUTH_HINT = 'Authentication required: pass `Authorization: Bearer <api_token>`. ' +
  'Create a token at https://freeqrly.com/dashboard/ (API Tokens section).';

const SERVER_INFO = {
  name: 'freeqrly-mcp',
  title: 'FreeQrly QR Generator',
  version: '1.1.0',
};

const STATIC_TOOLS = [
  {
    name: 'generate_qr',
    description:
      'Generate a static QR code and get a ready-to-download SVG URL. Free, no key required. ' +
      'Encodes any text, URL, WiFi credentials (WIFI:T:WPA;S:MyNet;P:secret;;), ' +
      'vCard, or geo URI as a static QR code that never expires.',
    inputSchema: {
      type: 'object',
      properties: {
        data: { type: 'string', description: 'Text/URL to encode (max 2000 chars).', minLength: 1 },
        size: { type: 'integer', description: 'Output size in px (128-2048).', default: 1024 },
        color: { type: 'string', description: 'Module color, 6-digit hex.', default: '2F4A62' },
        bgcolor: { type: 'string', description: 'Background color, 6-digit hex.', default: 'ffffff' },
        ecc: { type: 'string', description: 'Error correction: L, M, Q, H.', default: 'M' },
      },
      required: ['data'],
    },
  },
];

const TYPE_ENUM = [...VALID_TYPES];

const DYNAMIC_TOOLS = [
  {
    name: 'dynamic_qr_create',
    description:
      'Create an EDITABLE dynamic QR code (' + AUTH_HINT + ') ' +
      'The printed QR never changes; its content can be edited later and scans are tracked. ' +
      'Free quota: 8 codes per account.',
    inputSchema: {
      type: 'object',
      properties: {
        type: { type: 'string', description: 'Content type.', enum: TYPE_ENUM, default: 'url' },
        payload: { type: 'string', description: 'URL, text, WiFi string, vCard, etc. (max 8000 chars).', minLength: 1 },
      },
      required: ['payload'],
    },
  },
  {
    name: 'dynamic_qr_list',
    description: 'List your dynamic QR codes with scan counts and quota usage. (' + AUTH_HINT + ')',
    inputSchema: { type: 'object', properties: {} },
  },
  {
    name: 'dynamic_qr_update',
    description: 'Edit a dynamic QR code\'s content — printed QRs serve the new content instantly. (' + AUTH_HINT + ')',
    inputSchema: {
      type: 'object',
      properties: {
        code: { type: 'string', description: 'The 7-char code.', minLength: 1 },
        type: { type: 'string', description: 'Content type.', enum: TYPE_ENUM },
        payload: { type: 'string', description: 'New content (max 8000 chars).', minLength: 1 },
      },
      required: ['code', 'type', 'payload'],
    },
  },
  {
    name: 'dynamic_qr_delete',
    description: 'Delete a dynamic QR code (frees one quota slot; printed QRs stop working). (' + AUTH_HINT + ')',
    inputSchema: {
      type: 'object',
      properties: {
        code: { type: 'string', description: 'The 7-char code.', minLength: 1 },
      },
      required: ['code'],
    },
  },
  {
    name: 'dynamic_qr_stats',
    description: 'Scan statistics for a dynamic QR code (by date, country, device). (' + AUTH_HINT + ')',
    inputSchema: {
      type: 'object',
      properties: {
        code: { type: 'string', description: 'The 7-char code.', minLength: 1 },
      },
      required: ['code'],
    },
  },
];

function apiUrl(base, args) {
  const u = new URL('/api/qr', base);
  const eccRaw = String(args.ecc || 'M').toUpperCase();
  const p = {
    data: args.data,
    size: String(Math.min(2048, Math.max(128, parseInt(args.size) || 1024))),
    color: ((args.color || '2F4A62').replace(/^#/, '') || '2F4A62'),
    bgcolor: ((args.bgcolor || 'ffffff').replace(/^#/, '') || 'ffffff'),
    ecc: (['L', 'M', 'Q', 'H'].includes(eccRaw) ? eccRaw : 'M'),
  };
  if (!HEX.test(p.color)) p.color = '2F4A62';
  if (!HEX.test(p.bgcolor)) p.bgcolor = 'ffffff';
  for (const [k, v] of Object.entries(p)) u.searchParams.set(k, v);
  return u.toString();
}

function textResult(text) {
  return { content: [{ type: 'text', text }] };
}

function callStaticTool(name, args, base) {
  if (name !== 'generate_qr') throw new Error('Unknown tool: ' + name);
  const data = (args.data || '').trim();
  if (!data) throw new Error('data is required');
  if (data.length > 2000) throw new Error('data too long (max 2000 chars)');
  // Validate it encodes, so agents get a clean error instead of a broken URL.
  const qr = qrcode(0, 'M');
  qr.addData(data);
  qr.make();
  const url = apiUrl(base, { ...args, data });
  return textResult(
    `QR code ready: ${url}\n` +
    `Static code (${data.length} chars) — never expires, no sign-up, no tracking. ` +
    `Fetch the URL for the SVG, or open it in a browser to download.`
  );
}

async function callDynamicTool(env, user, name, args, base, ip) {
  const a = args || {};
  switch (name) {
    case 'dynamic_qr_create': {
      const r = await createDynamicCode(env, user,
        { type: a.type, payload: a.payload, style: a.style },
        { origin: base, ip });
      return textResult(
        `Dynamic QR created: ${r.shortUrl}\n` +
        `Code: ${r.code} (${r.type}). Editable after printing; scans are tracked in your dashboard.`
      );
    }
    case 'dynamic_qr_list': {
      const r = await listDynamicCodes(env, user);
      const lines = r.codes.map((c) =>
        `- ${c.code} [${c.type}] ${c.destination} — ${c.totalScans} scans`).join('\n');
      return textResult(
        `Dynamic codes (${r.quota.used}/${r.quota.limit} used):\n${lines || '(none yet)'}\n` +
        `Manage them at https://freeqrly.com/dashboard/`
      );
    }
    case 'dynamic_qr_update': {
      const r = await updateDynamicCode(env, user, a.code, { type: a.type, payload: a.payload, style: a.style });
      return textResult(`Updated ${r.code}: now serves [${r.type}] ${r.payload}`);
    }
    case 'dynamic_qr_delete': {
      await deleteDynamicCode(env, user, a.code);
      return textResult(`Deleted ${a.code}. One quota slot freed.`);
    }
    case 'dynamic_qr_stats': {
      const s = await getCodeStats(env, user, a.code);
      const top = (arr, k) => (arr || []).slice(0, 5).map((x) => `${x[k]}: ${x.scans}`).join(', ');
      return textResult(
        `Stats for ${s.code} [${s.type}]: ${s.totalScans} total scans (${s.uniqueScans} unique).\n` +
        `By country: ${top(s.byCountry, 'country') || '—'}\n` +
        `By device: ${top(s.byDevice, 'device') || '—'}`
      );
    }
    default:
      throw new Error('Unknown tool: ' + name);
  }
}

function jsonRpc(id, result) {
  return new Response(JSON.stringify({ jsonrpc: '2.0', id, result }), {
    headers: { 'Content-Type': 'application/json', ...CORS },
  });
}

function jsonRpcError(id, code, message) {
  return new Response(JSON.stringify({ jsonrpc: '2.0', id, error: { code, message } }), {
    headers: { 'Content-Type': 'application/json', ...CORS },
  });
}

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: CORS });
}

export async function onRequestGet() {
  return new Response('FreeQrly MCP — POST JSON-RPC here. See https://freeqrly.com/developers/', {
    status: 405,
    headers: { ...CORS, Allow: 'POST, OPTIONS' },
  });
}

// POST /mcp — Streamable HTTP (single response per request).
export async function onRequestPost({ request, env }) {
  let body;
  try {
    body = await request.json();
  } catch {
    return jsonRpcError(null, -32700, 'Parse error');
  }
  const { id = null, method, params = {} } = body || {};
  const base = new URL(request.url).origin;

  // Dynamic tools need a Bearer API token; static generate_qr stays open.
  let authed = null;
  try { authed = await getApiTokenUser(env, request); } catch { authed = null; }

  try {
    if (method === 'initialize') {
      return jsonRpc(id, {
        protocolVersion: '2024-11-05',
        capabilities: { tools: { listChanged: false } },
        serverInfo: SERVER_INFO,
      });
    }
    if (method === 'notifications/initialized') {
      return new Response(null, { status: 202, headers: CORS });
    }
    if (method === 'tools/list') {
      return jsonRpc(id, { tools: authed ? [...STATIC_TOOLS, ...DYNAMIC_TOOLS] : STATIC_TOOLS });
    }
    if (method === 'tools/call') {
      const toolName = params.name;
      if (toolName === 'generate_qr') {
        return jsonRpc(id, callStaticTool(toolName, params.arguments || {}, base));
      }
      if (toolName && toolName.startsWith('dynamic_qr_')) {
        if (!authed) return jsonRpcError(id, -32001, AUTH_HINT);
        try {
          const result = await callDynamicTool(env, authed.user, toolName, params.arguments || {}, base,
            request.headers.get('CF-Connecting-IP') || 'unknown');
          return jsonRpc(id, result);
        } catch (e) {
          if (e instanceof ApiError) {
            const msg = e.body && e.body.error ? e.body.error : 'request failed';
            const hint = e.body && e.body.hint ? ` (${e.body.hint})` : '';
            return jsonRpcError(id, -32002, msg + hint);
          }
          throw e;
        }
      }
      return jsonRpcError(id, -32601, 'Method not found: ' + toolName);
    }
    return jsonRpcError(id, -32601, 'Method not found: ' + method);
  } catch (e) {
    return jsonRpcError(id, -32602, String((e && e.message) || e));
  }
}
