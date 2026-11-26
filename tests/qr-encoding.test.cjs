// Guard for the UTF-8 patch in assets/lib/qr-code-styling.js.
//
// The bundled qrcode-generator defaults to `stringToBytesFuncs.default`,
// which does `e.push(255 & charCodeAt(i))` — it masks every character to a
// single byte. Any non-ASCII character is therefore silently truncated:
// "中文测试" was encoded as the four Latin-1 bytes 2D 87 4B D5, so Chinese,
// Japanese, Arabic, Hindi and Cyrillic input all produced codes that decode
// to garbage. The library ships a UTF-8 implementation; one assignment
// switches to it.
//
// Replacing the vendored file (a version bump, a re-download) would drop that
// line and reintroduce the bug with no visible error, so assert it here.
//
// Run: node --test tests/qr-encoding.test.cjs
const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const path = require('node:path');

const LIB = path.join(__dirname, '..', 'assets', 'lib', 'qr-code-styling.js');
const src = fs.readFileSync(LIB, 'utf8');

test('vendored QR library keeps the UTF-8 stringToBytes patch', () => {
  assert.match(
    src,
    /i\.stringToBytes\s*=\s*i\.stringToBytesFuncs\["UTF-8"\]/,
    'the UTF-8 assignment is missing — non-ASCII QR content would be truncated to Latin-1'
  );
});

test('the library still ships a UTF-8 implementation to switch to', () => {
  assert.ok(
    src.includes('stringToBytesFuncs["UTF-8"]'),
    'stringToBytesFuncs["UTF-8"] is no longer defined; re-check the patch against the new build'
  );
});

test('the Latin-1 default is still what the patch overrides', () => {
  assert.ok(
    src.includes('255&n') || src.includes('255 & n'),
    'the default stringToBytes no longer masks to 8 bits — the patch may be unnecessary, but verify before removing'
  );
});
