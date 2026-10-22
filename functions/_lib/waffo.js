// Waffo Pancake client (Merchant of Record for the Pro tier).
// API auth = RSA-SHA256 request signing (docs.waffo.ai/api-reference/authentication):
//   canonical = METHOD + "\n" + PATH + "\n" + TIMESTAMP(sec) + "\n" + SHA256_BASE64(body)
//   X-Signature = Base64(RSA-SHA256(canonical)) with the merchant private key.
// Webhook verification = RSA-SHA256 over `${t}.${rawBody}` with Waffo's fixed
// per-environment public keys (they ship inside the official SDK; public keys
// are not secrets). Secrets (merchant id + private keys) live ONLY in
// Cloudflare Pages env vars: WAFFO_MERCHANT_ID, WAFFO_PRIVATE_KEY_TEST,
// WAFFO_PRIVATE_KEY_PROD. WAFFO_ENV ("test" | "prod", wrangler.toml [vars])
// selects the key pair + product IDs (WAFFO_PRODUCT_PRO_MONTHLY_<ENV>, ...).

const API_BASE = 'https://api.waffo.ai';

export const WAFFO_WEBHOOK_PUBLIC_KEYS = {
  test: `-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxnmRY6yMMA3lVqmAU6ZG
b1sjL/+r/z6E+ZjkXaDAKiqOhk9rpazni0bNsGXwmftTPk9jy2wn+j6JHODD/WH/
SCnSfvKkLIjy4Hk7BuCgB174C0ydan7J+KgXLkOwgCAxxB68t2tezldwo74ZpXgn
F49opzMvQ9prEwIAWOE+kV9iK6gx/AckSMtHIHpUesoPDkldpmFHlB2qpf1vsFTZ
5kD6DmGl+2GIVK01aChy2lk8pLv0yUMu18v44sLkO5M44TkGPJD9qG09wrvVG2wp
OTVCn1n5pP8P+HRLcgzbUB3OlZVfdFurn6EZwtyL4ZD9kdkQ4EZE/9inKcp3c1h4
xwIDAQAB
-----END PUBLIC KEY-----`,
  prod: `-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAz+xApdTIb4ua+DgZKQ54
iBsD82ybyhGCLRETONW4Jgbb3A8DUM1LqBk6r/CmTOCHqLalTQHNigvP3R5zkDNX
iRJz6gA4MJ/+8K0+mnEE2RISQzN+Qu65TNd6svb+INm/kMaftY4uIXr6y6kchtTJ
dwnQhcKdAL2v7h7IFnkVelQsKxDdb2PqX8xX/qwd01iXvMcpCCaXovUwZsxH2QN5
ZKBTseJivbhUeyJCco4fdUyxOMHe2ybCVhyvim2uxAl1nkvL5L8RCWMCAV55LLo0
9OhmLahz/DYNu13YLVP6dvIT09ZFBYU6Owj1NxdinTynlJCFS9VYwBgmftosSE1U
dwIDAQAB
-----END PUBLIC KEY-----`,
};

export function waffoEnv(env) {
  return env.WAFFO_ENV === 'prod' ? 'prod' : 'test';
}

export function waffoConfigured(env) {
  const e = waffoEnv(env);
  return Boolean(
    env.WAFFO_MERCHANT_ID &&
    (e === 'prod' ? env.WAFFO_PRIVATE_KEY_PROD : env.WAFFO_PRIVATE_KEY_TEST) &&
    waffoProductId(env, 'monthly') &&
    waffoProductId(env, 'yearly')
  );
}

export function waffoProductId(env, period) {
  const e = waffoEnv(env).toUpperCase();
  return period === 'yearly'
    ? env[`WAFFO_PRODUCT_PRO_YEARLY_${e}`]
    : env[`WAFFO_PRODUCT_PRO_MONTHLY_${e}`];
}

function b64ToBytes(b64) {
  const bin = atob(b64.replace(/\s+/g, ''));
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

function bytesToB64(bytes) {
  let bin = '';
  for (const b of bytes) bin += String.fromCharCode(b);
  return btoa(bin);
}

// WebCrypto only imports RSA private keys as PKCS#8. Waffo's download may be
// PKCS#1 ("BEGIN RSA PRIVATE KEY") — wrap it in the standard PKCS#8 envelope
// (version + rsaEncryption AlgorithmIdentifier + OCTET STRING) when needed.
function pemToPkcs8(pem) {
  const body = pem.replace(/-----BEGIN [^-]+-----/, '').replace(/-----END [^-]+-----/, '').replace(/\s+/g, '');
  const der = b64ToBytes(body);
  if (/BEGIN PRIVATE KEY-----/.test(pem) && !/RSA PRIVATE KEY/.test(pem)) return der;
  // Bare base64 without PEM armor (Waffo's dashboard copy format): detect the
  // structure from the DER itself. After SEQ header + version INTEGER, a
  // PKCS#8 PrivateKeyInfo has a SEQUENCE (AlgorithmIdentifier) next, while a
  // PKCS#1 RSAPrivateKey has an INTEGER (modulus) next.
  let i = 1;
  if (der[i] & 0x80) i += der[i] & 0x7f;
  i += 1; // first length byte / long-form length position
  if (der[i] === 0x02) { // version INTEGER
    const vlen = der[i + 1];
    if (der[i + 2 + vlen] === 0x30) return der; // already PKCS#8
  }
  // PKCS#1 → PKCS#8 wrap
  const algId = [0x30, 0x0d, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x01, 0x01, 0x05, 0x00];
  const version = [0x02, 0x01, 0x00];
  const octetHeader = der.length < 256
    ? [0x04, 0x82, (der.length >> 8) & 0xff, der.length & 0xff]
    : [0x04, 0x82, (der.length >> 8) & 0xff, der.length & 0xff];
  const inner = [...version, ...algId, ...octetHeader, ...der];
  const seqHeader = inner.length < 256
    ? [0x30, 0x81, inner.length]
    : [0x30, 0x82, (inner.length >> 8) & 0xff, inner.length & 0xff];
  return new Uint8Array([...seqHeader, ...inner]);
}

const keyCache = new Map();

async function importPrivateKey(pem) {
  const cacheKey = pem.slice(-32);
  if (keyCache.has(cacheKey)) return keyCache.get(cacheKey);
  const key = await crypto.subtle.importKey(
    'pkcs8', pemToPkcs8(pem),
    { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' },
    false, ['sign']
  );
  keyCache.set(cacheKey, key);
  return key;
}

async function importPublicKey(pem) {
  const body = pem.replace(/-----BEGIN [^-]+-----/, '').replace(/-----END [^-]+-----/, '').replace(/\s+/g, '');
  return crypto.subtle.importKey(
    'spki', b64ToBytes(body),
    { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' },
    false, ['verify']
  );
}

async function sha256B64(text) {
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
  return bytesToB64(new Uint8Array(digest));
}

// Signed API call. Returns the parsed JSON body; throws on HTTP errors with
// Waffo's error message attached.
export async function waffoApi(env, method, path, bodyObj) {
  const e = waffoEnv(env);
  const pem = e === 'prod' ? env.WAFFO_PRIVATE_KEY_PROD : env.WAFFO_PRIVATE_KEY_TEST;
  if (!env.WAFFO_MERCHANT_ID || !pem) throw new Error('waffo_not_configured');
  const bodyStr = bodyObj === undefined ? '' : JSON.stringify(bodyObj);
  const timestamp = Math.floor(Date.now() / 1000).toString();
  const canonical = `${method}\n${path}\n${timestamp}\n${await sha256B64(bodyStr)}`;
  const key = await importPrivateKey(pem);
  const sig = await crypto.subtle.sign('RSASSA-PKCS1-v1_5', key, new TextEncoder().encode(canonical));
  const res = await fetch(`${API_BASE}${path}`, {
    method,
    headers: {
      'Content-Type': 'application/json',
      'X-Merchant-Id': env.WAFFO_MERCHANT_ID,
      'X-Timestamp': timestamp,
      'X-Signature': bytesToB64(new Uint8Array(sig)),
    },
    body: bodyStr || undefined,
  });
  const data = await res.json().catch(() => null);
  if (!res.ok) {
    const msg = data && data.errors && data.errors[0] ? data.errors[0].message : `HTTP ${res.status}`;
    throw new Error(`waffo_api_error: ${msg}`);
  }
  return data;
}

export async function createCheckoutSession(env, { period, buyerEmail, userId, successUrl }) {
  const productId = waffoProductId(env, period);
  if (!productId) throw new Error('waffo_not_configured');
  const res = await waffoApi(env, 'POST', '/v1/actions/checkout/create-session', {
    productId,
    productType: 'subscription',
    currency: 'USD',
    buyerEmail,
    successUrl,
    metadata: { userId, period },
    orderMerchantExternalId: userId,
  });
  return res.data; // { sessionId, checkoutUrl, expiresAt }
}

export async function cancelSubscription(env, orderId) {
  return waffoApi(env, 'POST', '/v1/actions/subscription-order/cancel-order', { orderId });
}

// Verify an incoming webhook. `mode` comes from the payload itself; the
// matching platform key must verify. Returns the parsed event or null.
export async function verifyWebhook(rawBody, signatureHeader, publicKeys = WAFFO_WEBHOOK_PUBLIC_KEYS) {
  if (!signatureHeader) return null;
  let t = '', v1 = '';
  for (const pair of signatureHeader.split(',')) {
    const eq = pair.indexOf('=');
    if (eq === -1) continue;
    const k = pair.slice(0, eq).trim(), v = pair.slice(eq + 1).trim();
    if (k === 't') t = v; else if (k === 'v1') v1 = v;
  }
  if (!t || !v1) return null;
  const ts = Number(t);
  if (!Number.isFinite(ts)) return null;
  const ageMs = Date.now() - ts;
  if (ageMs > 45 * 60 * 1000 || ageMs < -60 * 1000) return null; // replay window (SDK defaults)
  let evt;
  try { evt = JSON.parse(rawBody); } catch { return null; }
  const keyPem = publicKeys[evt.mode === 'test' ? 'test' : 'prod'];
  if (!keyPem) return null;
  try {
    const key = await importPublicKey(keyPem);
    const ok = await crypto.subtle.verify(
      'RSASSA-PKCS1-v1_5', key,
      b64ToBytes(v1),
      new TextEncoder().encode(`${t}.${rawBody}`)
    );
    return ok ? evt : null;
  } catch {
    return null;
  }
}
