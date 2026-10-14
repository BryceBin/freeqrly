/* Privacy-first analytics: receives front-end events and writes them to
   Cloudflare Analytics Engine. No cookies, no user IDs, no IP storage —
   just aggregate counts (event name + a few string props). Never throws. */
const ALLOWED = new Set([
  "qr_download",    // {type, format:png|svg}
  "batch_generate", // {count}
  "batch_zip",      // {count}
  "scan_decode",     // {method:camera|upload}
]);

const clean = (v, n) => String(v ?? "").slice(0, n);

export async function onRequest(context) {
  if (context.request.method !== "POST") {
    return new Response("method not allowed", { status: 405 });
  }
  try {
    const body = await context.request.json();
    const event = clean(body.event, 32);
    if (!ALLOWED.has(event)) return new Response("ok", { status: 200 });
    const dp = {
      indexes: [event],
      blobs: [
        clean(body.type, 16),                       // qr type: wifi, url, ...
        clean(body.format || body.method, 16),      // png|svg | camera|upload
        clean(body.lang, 8),                        // ui language
      ],
      doubles: [Math.min(Math.max(Number(body.count) || 1, 1), 100000)],
    };
    if (context.env.ANALYTICS) {
      context.env.ANALYTICS.writeDataPoint(dp);
    }
    return new Response("ok", {
      status: 200,
      headers: { "Content-Type": "text/plain" },
    });
  } catch (e) {
    return new Response("ok", { status: 200 });
  }
}
