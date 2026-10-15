// GET /api/auth/config — which login providers are configured. No auth required.
// { providers: { email, google, github, microsoft } }
import { json } from '../../_lib/dynamic.js';

export async function onRequestGet({ env }) {
  return json({
    providers: {
      email: !!env.RESEND_API_KEY,
      google: !!env.GOOGLE_CLIENT_ID,
      github: !!env.GITHUB_CLIENT_ID,
      microsoft: !!env.MICROSOFT_CLIENT_ID,
    },
  });
}
