import QR from './_lib/qrcode.js';

const qrcode = QR && QR.default ? QR.default : QR;
const HEX = /^[0-9a-fA-F]{6}$/;

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization',
  'Access-Control-Max-Age': '86400',
};

const SERVER_INFO = {
  name: 'freeqrly-mcp',
  title: 'FreeQrly QR Generator',
  version: '1.0.0',
};

const TOOLS = [
  {
    name: 'generate_qr',
    description:
      'Generate a QR code and get a ready-to-download SVG URL. Free, no key required. ' +
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

function callTool(name, args, base) {
  if (name !== 'generate_qr') throw new Error('Unknown tool: ' + name);
  const data = (args.data || '').trim();
  if (!data) throw new Error('data is required');
  if (data.length > 2000) throw new Error('data too long (max 2000 chars)');
  // Validate it encodes, so agents get a clean error instead of a broken URL.
  const qr = qrcode(0, 'M');
  qr.addData(data);
  qr.make();
  const url = apiUrl(base, { ...args, data });
  return {
    content: [
      {
        type: 'text',
        text:
          `QR code ready: ${url}\n` +
          `Static code (${data.length} chars) — never expires, no sign-up, no tracking. ` +
          `Fetch the URL for the SVG, or open it in a browser to download.`,
      },
    ],
  };
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
export async function onRequestPost({ request }) {
  let body;
  try {
    body = await request.json();
  } catch {
    return jsonRpcError(null, -32700, 'Parse error');
  }
  const { id = null, method, params = {} } = body || {};
  const base = new URL(request.url).origin;

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
      return jsonRpc(id, { tools: TOOLS });
    }
    if (method === 'tools/call') {
      const result = callTool(params.name, params.arguments || {}, base);
      return jsonRpc(id, result);
    }
    return jsonRpcError(id, -32601, 'Method not found: ' + method);
  } catch (e) {
    return jsonRpcError(id, -32602, String((e && e.message) || e));
  }
}
