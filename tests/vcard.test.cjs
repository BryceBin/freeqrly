const test=require('node:test');
const assert=require('node:assert/strict');
const vcard=require('../assets/js/vcard.js');

test('contact cards include the required names and CRLF delimiters',()=>{
  const card=vcard.build({name:'Jane Doe',phone:'+1 555 0100',email:'jane@example.com'});
  assert.match(card,/\r\nFN:Jane Doe\r\n/);
  assert.match(card,/\r\nN:;Jane Doe;;;\r\n/);
  assert.match(card,/TEL;TYPE=CELL:\+1 555 0100/);
  assert.ok(card.endsWith('END:VCARD\r\n'));
  assert.ok(!/(?<!\r)\n/.test(card));
});

test('the exact old QR payload from the reported screenshot can be exported as a valid card',()=>{
  const old='BEGIN:VCARD\nVERSION:3.0\nN:Jane Doe\nTEL:+1 555 0100\nEMAIL:jane@example.com\nEND:VCARD';
  const card=vcard.normalize(old);
  assert.match(card,/FN:Jane Doe\r\n/);
  assert.match(card,/N:Jane Doe;;;;\r\n/);
  assert.match(card,/TEL:\+1 555 0100\r\n/);
  assert.match(card,/EMAIL:jane@example.com\r\n/);
  assert.ok(vcard.isVCard(card));
  assert.equal(vcard.normalize(card),card);
});

test('Unicode names and punctuation survive escaping and UTF-8 line folding',()=>{
  const name='于悦;测试,\\团队\n'+ '象'.repeat(80);
  const card=vcard.build({name,phone:'123'});
  for(const line of card.split('\r\n')) assert.ok(Buffer.byteLength(line,'utf8')<=75);
  const unfolded=card.replace(/\r\n /g,'');
  assert.ok(unfolded.includes('FN:于悦\\;测试\\,\\\\团队\\n'+'象'.repeat(80)));
  assert.ok(!unfolded.includes('\nTEL:'));
});

test('valid vCard 4.0 data remains intact and ordinary text is not a contact',()=>{
  const card='BEGIN:VCARD\r\nVERSION:4.0\r\nFN:Jane Doe\r\nEMAIL:jane@example.com\r\nEND:VCARD\r\n';
  assert.equal(vcard.normalize(card),card);
  assert.equal(vcard.isVCard('https://example.com'),false);
  assert.equal(vcard.isVCard('BEGIN:VCARD\nnot finished'),false);
  assert.throws(()=>vcard.normalize('plain text'));
});
