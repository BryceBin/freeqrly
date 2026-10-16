#!/usr/bin/env python3
"""Generate /blog/ hub and /about/ page for FreeQrly.

STALE — DO NOT RUN without syncing: about/index.html and blog/index.html have
been hand-edited since (copy calibration 2026-10-16). Running this would
revert those edits. The generated files are the source of truth now."""
import os
SITE = os.path.dirname(os.path.abspath("/home/hatch/workspace/qr-site/")) + "/qr-site"

HEADER = '''<header class="top">
    <div class="brand"><a href="/" style="color:inherit;text-decoration:none">Free<em>Qrly</em></a></div>
    <nav class="tnav">
      <a href="/#studio">Studio</a><a href="/blog/">Field notes</a><a href="/about/">About</a>
    </nav>
    <div class="topbtns">
      <button class="tbtn" id="themeBtn" aria-label="theme">&#9681;</button>
    </div>
  </header>
  <div class="topline"></div>'''

THEME_JS = '''<script>
(function(){
  const root=document.documentElement;
  const set=d=>{d?root.setAttribute("data-theme","dark"):root.removeAttribute("data-theme");localStorage.setItem("freeqrly-theme",d?"dark":"light")};
  set(localStorage.getItem("freeqrly-theme")==="dark"||(!localStorage.getItem("freeqrly-theme")&&matchMedia("(prefers-color-scheme: dark)").matches));
  document.getElementById("themeBtn").onclick=()=>set(root.getAttribute("data-theme")!=="dark");
})();
</script>'''

FOOT = '''<footer>
    <div class="mascot m-foot" aria-hidden="true"><img loading="lazy" decoding="async" width="512" height="512" src="https://assets.freeqrly.com/mascots/v1/home-welcome.webp" alt="Qly the elephant waving hello"></div>
    <p class="fline">Made quietly, in your browser.</p>
    <p class="flinks"><a href="/google-form-qr-code/">Google Form QR codes</a><a href="/wifi-qr-code/">WiFi QR codes</a><a href="/vcard-qr-code/">vCard QR codes</a><a href="/batch-qr-code/">Batch QR codes</a></p>
    <p class="flinks"><a href="/business-card-qr-code/">Business card QR codes</a><a href="/google-review-qr-code/">Google review QR codes</a><a href="/qr-code-with-logo/">QR codes with logo</a><a href="/wedding-qr-code/">Wedding QR codes</a><a href="/instagram-qr-code/">Instagram QR codes</a></p>
    <p class="flinks"><a href="/scan/">QR scanner</a><a href="/blog/">Field notes</a><a href="/about/">About FreeQrly</a><a href="/developers/">API &amp; MCP for agents</a></p>
    <p class="fmeta">© 2026 FreeQrly</p>
  </footer>'''

HUB_CSS = '''<style>
.hub-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:34px 0}
.hub-card{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:24px;text-decoration:none;color:inherit;display:block;transition:transform .15s ease, box-shadow .15s ease}
.hub-card:hover{transform:translateY(-3px);box-shadow:0 14px 34px -18px rgba(120,90,40,.35)}
.hub-card .kicker{text-align:left;margin-bottom:8px}
.hub-card h2{font-size:21px;line-height:1.35;margin:0 0 8px;font-weight:600}
.hub-card p{font-size:14.5px;color:var(--soft);line-height:1.65;margin:0}
.hub-card .d{font-size:12px;color:var(--faint);margin-top:12px;letter-spacing:.08em}
@media(max-width:720px){.hub-grid{grid-template-columns:1fr}}
</style>'''

POSTS = [
 ("scan-qr-code-online", "Scan QR codes online", "No app, no upload — camera or image, decoded privately in your browser.", "2026-10-14"),
 ("scan-qr-code-from-image", "Scan a QR code from a picture", "iPhone, Android, and PC methods for decoding codes trapped in photos.", "2026-10-14"),
 ("qr-codes-for-events", "QR codes for events", "Check-in, add-to-calendar, photo sharing, and venue WiFi — the full playbook.", "2026-10-14"),
 ("wedding-rsvp-qr-code", "Wedding RSVP QR codes", "Link your RSVP form, print on invitations, stop chasing reply cards.", "2026-10-14"),
 ("how-to-scan-a-qr-code", "How to scan a QR code", "No app needed — your iPhone or Android camera already does it. The 3-second method, plus screenshots and safety.", "2026-10-14"),
 ("why-is-my-qr-code-not-working", "Why is my QR code not working?", "Seven real fixes in two minutes: size, contrast, damage, quiet zone, dead links, and the smudged lens.", "2026-10-14"),
 ("qr-code-print-size-guide", "QR code print size guide", "The 2x2 cm rule, the 1:10 distance ratio, and resolution settings for cards, flyers, and posters.", "2026-10-14"),
 ("qr-codes-for-restaurants", "QR codes for restaurants", "The three codes every restaurant needs: menu, Google reviews, and guest WiFi. Free setup guide.", "2026-10-14"),
 ("free-qr-codes-that-dont-expire", "Free QR codes that don't expire", "They exist — they're called static codes. How to spot the trial trap and make codes that last.", "2026-10-14"),
 ("do-qr-codes-expire", "Do QR codes expire?", "The honest answer: the pattern never expires, but the business model behind it might. Know the difference.", "2026-10-13"),
 ("static-vs-dynamic-qr-codes", "Static vs dynamic QR codes", "One is free forever, the other rents you your own code. Which one you actually need.", "2026-10-13"),
]

cards = "\n".join(
 f'''    <a class="hub-card" href="/blog/{s}/">
      <div class="kicker">Field notes</div>
      <h2>{t}</h2>
      <p>{d}</p>
      <div class="d">{dt}</div>
    </a>''' for s, t, d, dt in POSTS)

hub = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Field Notes — QR Code Guides &amp; Tips | FreeQrly</title>
<meta name="description" content="Practical QR code guides: how to scan, print sizes, troubleshooting, restaurant playbooks, and why free codes don't have to expire.">
<link rel="canonical" href="https://freeqrly.com/blog/">
<link rel="alternate" hreflang="en" href="https://freeqrly.com/blog/">
<link rel="alternate" hreflang="x-default" href="https://freeqrly.com/blog/">
<meta property="og:title" content="Field Notes — QR Code Guides & Tips | FreeQrly">
<meta property="og:description" content="Practical QR code guides from the FreeQrly studio.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://freeqrly.com/blog/">
<meta property="og:image" content="https://freeqrly.com/og.png">
<link rel="icon" type="image/png" href="/assets/img/favicon-elephant.png">
<link rel="stylesheet" href="/assets/css/main.css">
{HUB_CSS}
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"CollectionPage","name":"Field Notes — QR Code Guides & Tips","description":"Practical QR code guides from FreeQrly.","url":"https://freeqrly.com/blog/"}}
</script>
</head>
<body>
<div class="wrap">
{HEADER}
  <article class="article" style="max-width:880px">
    <div class="mascot m-blog" aria-hidden="true"><img decoding="async" width="512" height="512" src="https://assets.freeqrly.com/mascots/v1/faq.webp" alt="Qly thinking about your question"></div>
    <div class="kicker" style="text-align:center">Field notes</div>
    <h1 style="text-align:center;max-width:640px;margin:0 auto">Notes on <span class="hl hl-honey">QR codes</span></h1>
    <p class="lede">Short, practical guides from the studio — scanning, printing, troubleshooting, and getting the most out of a free code.</p>
    <div class="hub-grid">
{cards}
    </div>
    <p style="text-align:center;margin-top:10px"><a class="btn" href="/#studio" style="text-decoration:none">Make a QR code &rarr;</a></p>
  </article>
{FOOT}
</div>
{THEME_JS}
</body>
</html>'''
os.makedirs(f"{SITE}/blog", exist_ok=True)
open(f"{SITE}/blog/index.html", "w").write(hub)
print("wrote blog hub")

ABOUT_CSS = '''<style>
.facts{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:26px 0}
.fact{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px}
.fact b{display:block;font-size:15px;margin-bottom:4px}
.fact span{font-size:14px;color:var(--soft);line-height:1.6}
@media(max-width:720px){.facts{grid-template-columns:1fr}}
.qa{margin:22px 0}
.qa h3{font-size:17px;margin:18px 0 6px}
.qa p{font-size:15px;color:var(--soft);line-height:1.7;margin:0 0 4px}
</style>'''

about = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>About FreeQrly — Free QR Codes, No Sign-Up, No Expiry</title>
<meta name="description" content="FreeQrly is a free QR code generator that runs 100% in your browser. No sign-up, no tracking, no expiry. Learn what it is and how it works.">
<link rel="canonical" href="https://freeqrly.com/about/">
<link rel="alternate" hreflang="en" href="https://freeqrly.com/about/">
<link rel="alternate" hreflang="x-default" href="https://freeqrly.com/about/">
<meta property="og:title" content="About FreeQrly">
<meta property="og:description" content="A free QR code generator that runs 100% in your browser. No sign-up, no tracking, no expiry.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://freeqrly.com/about/">
<meta property="og:image" content="https://freeqrly.com/og.png">
<link rel="icon" type="image/png" href="/assets/img/favicon-elephant.png">
<link rel="stylesheet" href="/assets/css/main.css">
{ABOUT_CSS}
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization","name":"FreeQrly","url":"https://freeqrly.com/","logo":"https://freeqrly.com/assets/img/favicon-elephant.png","description":"FreeQrly is a free QR code generator that runs entirely in the browser. No sign-up, no tracking, no expiry — static QR codes with optional logos, in 10 languages.","foundingDate":"2026","sameAs":[]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebSite","name":"FreeQrly","url":"https://freeqrly.com/","inLanguage":["en","zh","es","hi","ar","pt","fr","ru","de","ja"]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
 {{"@type":"Question","name":"What is FreeQrly?","acceptedAnswer":{{"@type":"Answer","text":"FreeQrly is a free online QR code generator. It creates static QR codes for links, text, WiFi, vCards, SMS, calls, and locations — entirely in your browser, with no account and no fees."}}}},
 {{"@type":"Question","name":"Is FreeQrly really free?","acceptedAnswer":{{"@type":"Answer","text":"Yes. Every feature — including logo upload, batch generation, and high-resolution export — is free with no sign-up, no trial, and no watermarks."}}}},
 {{"@type":"Question","name":"Do FreeQrly QR codes expire?","acceptedAnswer":{{"@type":"Answer","text":"No. FreeQrly only generates static QR codes, which encode the destination directly in the pattern. They never expire and require no subscription."}}}},
 {{"@type":"Question","name":"Does FreeQrly track my QR codes or my data?","acceptedAnswer":{{"@type":"Answer","text":"No. Codes are generated locally in your browser using JavaScript; your content is never uploaded to a server, and there is no scan tracking."}}}},
 {{"@type":"Question","name":"What languages does FreeQrly support?","acceptedAnswer":{{"@type":"Answer","text":"Ten: English, Chinese, Spanish, Hindi, Arabic (with right-to-left layout), Portuguese, French, Russian, German, and Japanese."}}}}
]}}
</script>
</head>
<body>
<div class="wrap">
{HEADER}
  <article class="article">
    <div class="mascot m-blog" aria-hidden="true"><img decoding="async" width="512" height="512" src="https://assets.freeqrly.com/mascots/v1/privacy.webp" alt="Qly protecting your privacy with a shield"></div>
    <div class="kicker" style="text-align:center">About</div>
    <h1 style="text-align:center;max-width:640px;margin:0 auto">What is <span class="hl hl-mint">FreeQrly</span>?</h1>
    <p class="lede">FreeQrly is a free QR code generator with a simple idea: the tool should live in your browser, not on somebody's server. You type, it draws — nothing is uploaded, tracked, or billed.</p>
    <div class="facts">
      <div class="fact"><b>100% browser-based</b><span>Every code is drawn locally with JavaScript. Your links, contacts, and WiFi passwords never leave your device.</span></div>
      <div class="fact"><b>Static codes only</b><span>No trials, no subscriptions, no deactivated codes. What you print today scans in ten years.</span></div>
      <div class="fact"><b>Free, no sign-up</b><span>Logo upload, batch generation, 2048&nbsp;px PNG and SVG export — all free, no account, no watermark.</span></div>
      <div class="fact"><b>10 languages</b><span>English, Chinese, Spanish, Hindi, Arabic (RTL), Portuguese, French, Russian, German, Japanese.</span></div>
      <div class="fact"><b>Built for print</b><span>High-resolution export and vector SVG, quiet zones respected — made for business cards, menus, and posters.</span></div>
      <div class="fact"><b>Agent-friendly</b><span>A free <a href="/developers/">API and MCP server</a> so AI assistants can generate codes too.</span></div>
    </div>
    <div class="qa">
      <h2 style="text-align:center">Questions, answered</h2>
      <h3>Is FreeQrly really free?</h3>
      <p>Yes — every feature is free, with no sign-up and no watermarks. Static codes cost nothing to serve once generated in your browser, so there's nothing to charge for.</p>
      <h3>Do the QR codes expire?</h3>
      <p>No. FreeQrly generates static codes only; the destination lives inside the pattern itself. Details: <a href="/blog/do-qr-codes-expire/">do QR codes expire?</a></p>
      <h3>Can I use it for my business?</h3>
      <p>Yes — commercial use is free. Restaurants use it for <a href="/blog/qr-codes-for-restaurants/">menus and reviews</a>, shops for <a href="/google-review-qr-code/">review codes</a> and <a href="/wifi-qr-code/">WiFi codes</a>.</p>
      <h3>Who is behind FreeQrly?</h3>
      <p>An independent maker who got tired of "free" generators that hold your codes hostage behind a trial. The mascot is Qly, a small elephant who appears across the site.</p>
    </div>
    <p style="text-align:center;margin-top:26px"><a class="btn" href="/#studio" style="text-decoration:none">Try the generator &rarr;</a></p>
  </article>
{FOOT}
</div>
{THEME_JS}
</body>
</html>'''
os.makedirs(f"{SITE}/about", exist_ok=True)
open(f"{SITE}/about/index.html", "w").write(about)
print("wrote about")
