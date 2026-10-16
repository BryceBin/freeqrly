// POST /api/logos — upload a custom logo for dynamic QR codes.
// LOGIN REQUIRED. Body: multipart form with a `file` field (image, max 2MB).
// The file is stored in R2 (bucket `freeqrly-logos`, binding LOGOS) under an
// unguessable key: u_<userId>_<32 hex>.<ext>
// Returns: { key, url } — url is /api/logos/<key>, served by functions/api/logos/[key].js.
// The key goes into the code's style.logoKey (see _lib/style.js).
import { json } from '../_lib/dynamic.js';
import { getSessionUser } from '../_lib/auth.js';

const ALLOWED = {
  'image/png': 'png',
  'image/jpeg': 'jpg',
  'image/webp': 'webp',
  'image/gif': 'gif',
  'image/svg+xml': 'svg',
};
const MAX_BYTES = 2 * 1024 * 1024;

function hex(bytes) {
  return [...bytes].map((b) => b.toString(16).padStart(2, '0')).join('');
}

export async function onRequestPost(context) {
  const { request, env } = context;
  if (!env.LOGOS) return json({ error: 'Logo storage not configured' }, 503);
  let sess = null;
  try { sess = await getSessionUser(env, request); } catch { sess = null; }
  if (!sess) return json({ error: 'unauthorized' }, 401);

  let file = null;
  try {
    const form = await request.formData();
    file = form.get('file');
  } catch { return json({ error: 'Invalid upload' }, 400); }
  if (!file || typeof file === 'string' || !file.size) return json({ error: 'No file uploaded' }, 400);
  if (file.size > MAX_BYTES) return json({ error: 'File too large (max 2MB)' }, 400);
  const ext = ALLOWED[file.type];
  if (!ext) return json({ error: 'Only PNG, JPEG, WebP, GIF or SVG images' }, 400);

  const rand = hex(crypto.getRandomValues(new Uint8Array(16)));
  const key = `u_${sess.user.id}_${rand}.${ext}`;
  try {
    await env.LOGOS.put(key, await file.arrayBuffer(), {
      httpMetadata: { contentType: file.type },
    });
  } catch {
    return json({ error: 'Upload failed' }, 500);
  }
  return json({ key, url: `/api/logos/${encodeURIComponent(key)}` });
}
