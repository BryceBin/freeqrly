// GET /api/auth/oauth/:provider — start OAuth (google|github|microsoft).
// Optional ?turnstileToken=... — verified server-side when TURNSTILE_SECRET_KEY is set
// (missing token proceeds; a token that fails verification redirects with error=turnstile).
// Unconfigured provider → redirect /login/?error=provider_unavailable.
// Sets HttpOnly fq_pkce (verifier, 10 min) + fq_oauth_state cookies, redirects to provider.
import { oauthProviderConfig, appUrl, genToken, sha256Base64Url, tempCookie,
  PKCE_COOKIE, OAUTH_STATE_COOKIE, verifyTurnstile, getClientIp, redirectTo } from '../../../_lib/auth.js';

export async function onRequestGet({ request, env, params }) {
  const url = new URL(request.url);
  const provider = (params.provider || '').toLowerCase();
  const login = (err) => redirectTo(new URL(`/login/?error=${err}`, url.origin).toString());
  const cfg = oauthProviderConfig(env, provider);
  if (!cfg || !cfg.clientId) return login('provider_unavailable');

  const ts = await verifyTurnstile(env, url.searchParams.get('turnstileToken') || '', getClientIp(request));
  if (!ts.ok) return login('turnstile');

  const verifier = genToken(64); // 86-char base64url, within PKCE 43–128
  const state = genToken(24);
  const redirectUri = `${appUrl(env)}/api/auth/callback/${provider}`;
  const authUrl = new URL(cfg.authorize);
  authUrl.searchParams.set('client_id', cfg.clientId);
  authUrl.searchParams.set('redirect_uri', redirectUri);
  authUrl.searchParams.set('response_type', 'code');
  authUrl.searchParams.set('scope', cfg.scope);
  authUrl.searchParams.set('state', state);
  if (provider === 'google') {
    authUrl.searchParams.set('access_type', 'offline');
    authUrl.searchParams.set('prompt', 'consent');
  }
  const headers = new Headers();
  if (cfg.pkce) {
    const challenge = await sha256Base64Url(verifier);
    authUrl.searchParams.set('code_challenge', challenge);
    authUrl.searchParams.set('code_challenge_method', 'S256');
    headers.append('Set-Cookie', tempCookie(PKCE_COOKIE, verifier, 600));
  }
  headers.append('Set-Cookie', tempCookie(OAUTH_STATE_COOKIE, state, 600));
  headers.set('Location', authUrl.toString());
  return new Response(null, { status: 302, headers });
}
