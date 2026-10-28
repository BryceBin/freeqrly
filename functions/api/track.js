/* Privacy-first analytics: receives front-end events and writes them to
   Cloudflare Analytics Engine. Aggregate counts only: no cookies, no user
   IDs, no raw IP storage, never input content. Field map (blobs appended
   after the original three, so old queries keep working):
   blob1 = type (qr type | page path | action name)
   blob2 = format (png|svg) | method (camera|upload)
   blob3 = UI language
   blob4 = referrer class (direct|google|baidu|bing|ai|other)
   blob5 = per-tab random session id (sessionStorage, discarded on tab close)
   blob6 = device class (mobile|desktop)
   blob7 = browser family (chrome|safari|firefox|edge|other)
   blob8 = country (Cloudflare request.cf.country, e.g. CN; empty if unknown)
   Never throws. */
const ALLOWED = new Set([
  "page_view",        // {type:pathname}
  "type_select",      // {type:qr type}
  "preset_click",     // {type:bf|xmas|none}
  "qr_download",      // {type, format:png|svg}
  "batch_generate",   // {count}
  "batch_zip",        // {count}
  "scan_decode",      // {method:camera|upload}
  "auth_click",       // {type:login|register|oauth_google|oauth_github}
  "code_create",      // {type:qr type}
  "dashboard_view",   // {}
  "dashboard_action", // {type:stats_view|code_edit|code_delete|token_create|token_revoke|checkout|cancel|code_download}
]);

const clean = (v, n) => String(v ?? "").slice(0, n);
const oneOf = (v, list, fb) => list.includes(v) ? v : fb;

export async function onRequest(context) {
  if (context.request.method !== "POST") {
    return new Response("method not allowed", { status: 405 });
  }
  try {
    const body = await context.request.json();
    const event = clean(body.event, 32);
    if (!ALLOWED.has(event)) return new Response("ok", { status: 200 });
    const sid = /^[0-9a-f]{16}$/.test(body.sid || "") ? body.sid : "";
    const cf = context.request.cf || {};
    const dp = {
      indexes: [event],
      blobs: [
        clean(body.type, 64),
        clean(body.format || body.method, 16),
        clean(body.lang, 8),
        oneOf(body.ref, ["direct", "google", "baidu", "bing", "ai", "other"], "other"),
        sid,
        oneOf(body.device, ["mobile", "desktop"], "other"),
        oneOf(body.browser, ["chrome", "safari", "firefox", "edge", "other"], "other"),
        clean(cf.country, 2),
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
