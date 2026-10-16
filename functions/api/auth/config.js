// GET /api/auth/config — which login providers are configured. No auth required.
// { providers: { google, github } }
// Email + password is always available (no env dependency); email sending
// (verification / password reset) still needs RESEND_API_KEY server-side.
import { json } from '../../_lib/dynamic.js';

export async function onRequestGet({ env }) {
  return json({
    // Sitekey is public (embedded in page HTML); secret stays server-side.
    turnstileSitekey: '0x4AAAAAAFYIGXSuCanTvOxZ',
    providers: {
      google: !!env.GOOGLE_CLIENT_ID,
      github: !!env.GITHUB_CLIENT_ID,
    },
  });
}
