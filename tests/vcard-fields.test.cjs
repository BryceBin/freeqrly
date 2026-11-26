// The generator's vCard form collects more than a name, phone and email.
// Those extra fields (company, title, website, address, note) go through the
// same builder, so check they are emitted, escaped, and folded correctly.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const vcard = require('../assets/js/vcard.js');

test('every optional field reaches the card', () => {
  const card = vcard.build({
    name: 'Jane Doe',
    phone: '+1 555 0100',
    email: 'jane@example.com',
    org: 'Acme Inc',
    title: 'Designer',
    url: 'https://example.com/a?b=1&c=2',
    address: '123 Main St, Springfield',
    note: 'Met at the conference',
  });
  assert.match(card, /\r\nORG:Acme Inc\r\n/);
  assert.match(card, /\r\nTITLE:Designer\r\n/);
  // A URL is a URI: it must NOT be text-escaped, or the query string breaks.
  assert.match(card, /\r\nURL:https:\/\/example\.com\/a\?b=1&c=2\r\n/);
  assert.match(card, /\r\nADR;TYPE=HOME:;;123 Main St\\, Springfield;;;;\r\n/);
  assert.match(card, /\r\nNOTE:Met at the conference\r\n/);
  assert.ok(card.endsWith('END:VCARD\r\n'));
});

test('a name with separators is escaped, not split into extra fields', () => {
  const card = vcard.build({ name: 'Doe; Jane, PhD', phone: '1' });
  assert.match(card, /\r\nFN:Doe\\; Jane\\, PhD\r\n/);
  assert.match(card, /\r\nN:;Doe\\; Jane\\, PhD;;;\r\n/);
  // N must still have exactly four component separators; the ones inside the
  // name are escaped and therefore not separators.
  const nLine = card.split('\r\n').find(l => l.startsWith('N:'));
  const separators = (nLine.match(/(?<!\\);|(?<=\\\\);|^;/g) || []).length;
  assert.equal((nLine.match(/(?<!\\);/g) || []).length, 4, nLine);
});

test('a long note folds at 75 octets instead of producing one giant line', () => {
  const note = 'x'.repeat(200);
  const card = vcard.build({ name: 'A', note });
  for (const line of card.split('\r\n')) {
    assert.ok(Buffer.byteLength(line, 'utf8') <= 75, `line too long: ${line.length}`);
  }
  assert.ok(card.replace(/\r\n /g, '').includes('NOTE:' + note));
});

test('empty optional fields are omitted rather than emitted blank', () => {
  const card = vcard.build({ name: 'A', org: '', title: '', url: '', address: '', note: '' });
  assert.ok(!card.includes('ORG:'));
  assert.ok(!card.includes('TITLE:'));
  assert.ok(!card.includes('URL:'));
  assert.ok(!card.includes('ADR'));
  assert.ok(!card.includes('NOTE:'));
});
