// Per-code QR style (colors, dots, frame, logo) stored as JSON in codes.style.
// Shared by create (POST /api/codes) and edit (PATCH /api/codes/:code).
// Shape:
//   { fg, bg, transparent, dots, ecc, frame, frameText, logoPreset, logoKey }
// logoPreset: one of the 6 built-in brand presets (by name).
// logoKey: R2 object key for a user-uploaded logo (u_<userId>_<rand>.<ext>).
// Only ONE logo source is kept: a valid logoKey wins over logoPreset.

export const LOGO_PRESETS = new Set(['apple', 'x', 'facebook', 'instagram', 'google', 'microsoft']);
export const DOT_STYLES = new Set(['square', 'dots', 'rounded', 'extra-rounded']);
export const ECC_LEVELS = new Set(['L', 'M', 'Q', 'H']);
export const FRAME_STYLES = new Set(['none', 'rounded', 'cta']);

const HEX = /^#[0-9A-Fa-f]{6}$/;
const LOGO_KEY_RE = /^u_[A-Za-z0-9_-]+_[0-9a-f]{32}\.(png|jpg|jpeg|webp|gif|svg)$/;

function cleanStr(v, max) {
  if (typeof v !== 'string') return '';
  return v.replace(/[\u0000-\u001F\u007F]/g, '').slice(0, max);
}

// Returns a sanitized style object, or null when the input is absent.
// Throws Error('invalid_style') on a present-but-malformed style.
export function sanitizeStyle(input, userId) {
  if (input === undefined || input === null) return null;
  if (typeof input !== 'object' || Array.isArray(input)) throw new Error('invalid_style');
  const raw = JSON.stringify(input);
  if (raw.length > 4096) throw new Error('invalid_style');

  const style = {
    fg: HEX.test(input.fg || '') ? input.fg : '#22303F',
    bg: HEX.test(input.bg || '') ? input.bg : '#FFFFFF',
    transparent: input.transparent === true,
    dots: DOT_STYLES.has(input.dots) ? input.dots : 'square',
    ecc: ECC_LEVELS.has(input.ecc) ? input.ecc : 'M',
    frame: FRAME_STYLES.has(input.frame) ? input.frame : 'none',
    frameText: cleanStr(input.frameText, 100),
    logoPreset: LOGO_PRESETS.has(input.logoPreset) ? input.logoPreset : null,
    logoKey: null,
  };
  if (typeof input.logoKey === 'string' && LOGO_KEY_RE.test(input.logoKey)) {
    // A logo key is only usable by the user it was uploaded for (key prefix).
    if (userId && input.logoKey.startsWith(`u_${userId}_`)) {
      style.logoKey = input.logoKey;
      style.logoPreset = null; // uploaded logo wins over preset
    } else if (!userId) {
      style.logoKey = input.logoKey;
      style.logoPreset = null;
    }
    // Otherwise: someone else's logo key — silently dropped.
  }
  return style;
}

export function parseStyle(stored) {
  if (!stored) return null;
  try {
    const v = JSON.parse(stored);
    if (v && typeof v === 'object') return v;
  } catch { /* corrupted style -> default */ }
  return null;
}
