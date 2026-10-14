/* Catch-all: proper 404 for unknown paths.
   Pages serves static files and specific functions first; only truly
   unknown paths reach here (fixes soft-404s hurting SEO). */
export async function onRequest(context) {
  try {
    const asset = await context.env.ASSETS.fetch(
      new URL('/404.html', context.request.url)
    );
    return new Response(asset.body, {
      status: 404,
      headers: { 'Content-Type': 'text/html; charset=utf-8' },
    });
  } catch (e) {
    return new Response('Not found', { status: 404 });
  }
}
