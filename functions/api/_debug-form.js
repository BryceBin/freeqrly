// TEMPORARY DEBUG — delete after diagnosing formData.
import { json } from '../_lib/dynamic.js';

export async function onRequestPost(context) {
  const { request } = context;
  const clone = request.clone();
  const raw = await clone.text().catch(() => '<unreadable>');
  try {
    const form = await request.formData();
    const out = [];
    for (const [k, v] of form.entries()) {
      out.push({ key: k, kind: typeof v, ctor: v?.constructor?.name || null, size: v?.size ?? null, name: v?.name ?? null, type: v?.type ?? null });
    }
    return json({ keys: out, ct: request.headers.get('content-type'), raw: raw.slice(0, 600) });
  } catch (e) {
    return json({ error: 'formData threw: ' + String(e?.message || e), raw: raw.slice(0, 600) }, 500);
  }
}
