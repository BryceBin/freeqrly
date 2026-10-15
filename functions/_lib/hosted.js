// Hosted page renderer for non-URL dynamic QR types
// When a dynamic code's type is not 'url', scanning shows this page
// instead of redirecting. Clean, minimal, FreeQrly-branded.

const esc = s => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

function layout(title, body) {
  return `<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(title)} | FreeQrly</title>
<style>
*{box-sizing:border-box}body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;background:#FBF6EC;color:#22303F;padding:24px 16px}
.card{max-width:480px;margin:40px auto;background:#fff;border-radius:18px;padding:28px;box-shadow:0 14px 36px rgba(190,145,60,.16)}
h1{font-size:22px;margin:0 0 16px}.row{margin:10px 0}.lbl{font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:#8a7a5f;margin-bottom:4px}.val{font-size:16px;word-break:break-all;white-space:pre-wrap}
a.btn{display:inline-block;background:#2F4A62;color:#fff;text-decoration:none;padding:12px 20px;border-radius:10px;margin-top:16px;font-weight:600}
a.btn2{background:#F1EAD9;color:#22303F}.foot{text-align:center;margin-top:24px;font-size:12px;color:#8a7a5f}.foot a{color:#8a7a5f}
pre{white-space:pre-wrap;word-break:break-all;font-family:inherit;font-size:15px;margin:0}
</style></head><body><div class="card">${body}</div>
<div class="foot">Made with <a href="https://freeqrly.com/">FreeQrly</a> — free QR codes, no sign-up.</div></body></html>`;
}

export function renderHostedPage(type, payload) {
  const p = payload || '';
  switch (type) {
    case 'text':
      return layout('Text', `<h1>📝 Text</h1><pre>${esc(p)}</pre>`);
    case 'wifi': {
      // WIFI:T:WPA;S:SSID;P:pass;;
      const m = p.match(/S:([^;]*);P:([^;]*);/);
      const ssid = m ? m[1] : p;
      const pass = m ? m[2] : '';
      return layout('WiFi', `<h1>📶 WiFi Network</h1>
        <div class="row"><div class="lbl">Network</div><div class="val">${esc(ssid)}</div></div>
        ${pass ? `<div class="row"><div class="lbl">Password</div><div class="val">${esc(pass)}</div></div>` : ''}`);
    }
    case 'vcard': {
      // Parse basic vCard fields for display
      const get = (k) => { const m = p.match(new RegExp('^' + k + ':(.*)$', 'm')); return m ? m[1].trim() : ''; };
      const fn = get('FN'), org = get('ORG'), title = get('TITLE'), tel = get('TEL'), email = get('EMAIL'), url = get('URL');
      const dl = `data:text/vcard;charset=utf-8,${encodeURIComponent(p)}`;
      return layout('Contact', `<h1>👤 ${esc(fn || 'Contact')}</h1>
        ${org ? `<div class="row"><div class="lbl">Company</div><div class="val">${esc(org)}</div></div>` : ''}
        ${title ? `<div class="row"><div class="lbl">Title</div><div class="val">${esc(title)}</div></div>` : ''}
        ${tel ? `<div class="row"><div class="lbl">Phone</div><div class="val"><a href="tel:${esc(tel)}">${esc(tel)}</a></div></div>` : ''}
        ${email ? `<div class="row"><div class="lbl">Email</div><div class="val"><a href="mailto:${esc(email)}">${esc(email)}</a></div></div>` : ''}
        ${url ? `<div class="row"><div class="lbl">Website</div><div class="val"><a href="${esc(url)}">${esc(url)}</a></div></div>` : ''}
        <a class="btn" href="${dl}" download="contact.vcf">Download contact</a>`);
    }
    case 'email': {
      const m = p.match(/mailto:([^?]*)\?subject=([^&]*)&body=(.*)/);
      const to = m ? decodeURIComponent(m[1]) : p;
      const subj = m ? decodeURIComponent(m[2]) : '';
      return layout('Email', `<h1>✉️ Email</h1>
        <div class="row"><div class="lbl">To</div><div class="val">${esc(to)}</div></div>
        ${subj ? `<div class="row"><div class="lbl">Subject</div><div class="val">${esc(subj)}</div></div>` : ''}
        <a class="btn" href="${esc(p)}">Compose email</a>`);
    }
    case 'sms': {
      const m = p.match(/sms:([^?]*)\?body=(.*)/);
      const num = m ? m[1] : p;
      const msg = m ? decodeURIComponent(m[2]) : '';
      return layout('SMS', `<h1>💬 SMS</h1>
        <div class="row"><div class="lbl">To</div><div class="val">${esc(num)}</div></div>
        ${msg ? `<div class="row"><div class="lbl">Message</div><div class="val">${esc(msg)}</div></div>` : ''}
        <a class="btn" href="${esc(p)}">Send SMS</a>`);
    }
    case 'phone': {
      const num = p.replace(/^tel:/, '');
      return layout('Phone', `<h1>📞 Phone</h1>
        <div class="row"><div class="lbl">Number</div><div class="val">${esc(num)}</div></div>
        <a class="btn" href="${esc(p)}">Call now</a>`);
    }
    case 'geo': {
      const coords = p.replace(/^geo:/, '');
      return layout('Location', `<h1>📍 Location</h1>
        <div class="row"><div class="lbl">Coordinates</div><div class="val">${esc(coords)}</div></div>
        <a class="btn" href="https://maps.google.com/?q=${esc(coords)}" target="_blank" rel="noopener">Open in Maps</a>`);
    }
    case 'event': {
      const get = (k) => { const m = p.match(new RegExp('^' + k + ':(.*)$', 'm')); return m ? m[1].trim() : ''; };
      const summary = get('SUMMARY'), loc = get('LOCATION'), desc = get('DESCRIPTION');
      return layout('Event', `<h1>📅 ${esc(summary || 'Event')}</h1>
        ${loc ? `<div class="row"><div class="lbl">Location</div><div class="val">${esc(loc)}</div></div>` : ''}
        ${desc ? `<div class="row"><div class="lbl">Details</div><div class="val">${esc(desc)}</div></div>` : ''}
        <a class="btn" href="data:text/calendar;charset=utf-8,${encodeURIComponent(p)}" download="event.ics">Add to calendar</a>`);
    }
    case 'bitcoin': {
      const m = p.match(/bitcoin:([^?]*)\?amount=([^&]*)&label=([^&]*)&message=(.*)/);
      const addr = m ? m[1] : p.replace(/^bitcoin:/, '');
      const amt = m ? decodeURIComponent(m[2]) : '';
      return layout('Bitcoin', `<h1>₿ Bitcoin</h1>
        <div class="row"><div class="lbl">Address</div><div class="val">${esc(addr)}</div></div>
        ${amt ? `<div class="row"><div class="lbl">Amount</div><div class="val">${esc(amt)} BTC</div></div>` : ''}`);
    }
    case 'coupon': {
      const lines = p.split('\n');
      return layout('Coupon', `<h1>🎟️ Coupon</h1><pre>${esc(p)}</pre>`);
    }
    case 'appstore': {
      const [ios, android] = p.split('\n');
      return layout('App', `<h1>📱 Get the app</h1>
        ${ios ? `<a class="btn" href="${esc(ios)}" target="_blank" rel="noopener">Download on App Store</a><br>` : ''}
        ${android ? `<a class="btn btn2" href="${esc(android)}" target="_blank" rel="noopener">Get it on Google Play</a>` : ''}`);
    }
    default:
      return layout('QR Code', `<h1>QR Code</h1><pre>${esc(p)}</pre>`);
  }
}
