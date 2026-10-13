#!/usr/bin/env python3
"""Generate the 4 SEO landing pages for FreeQrly. Reuses the studio markup from index.html."""
import re, os, json

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."
idx = open(os.path.join(SITE, "index.html")).read()

# Extract the studio <main> block from index.html
m = re.search(r'<main class="studio" id="studio">.*?</main>', idx, re.S)
assert m, "studio block not found"
STUDIO = m.group(0)

PAGES = [
 dict(
  slug="google-form-qr-code", dtype="url",
  title="Free QR Code Generator for Google Forms — No Sign-Up | FreeQrly",
  desc="Turn any Google Form link into a QR code in seconds. Free, no sign-up, no watermark. Paste your form URL and download a printable PNG or SVG.",
  kw="qr code generator for google form",
  h1="QR codes for Google Forms, without the fine print.",
  lede="Paste your form's responder link below and get a crisp, printable QR code — no account, no watermark, no expiry. Put it on a poster and watch the responses roll in.",
  steps=[
    ("Copy your form link", "In Google Forms, click <b>Send</b> and copy the responder link (the short one works best)."),
    ("Paste it above", "Drop the link into the Website field — your code appears instantly in the preview."),
    ("Download and print", "Grab a high-resolution PNG or SVG. It scans straight to your form, forever."),
  ],
  studio_h2="Make your Google Form QR code",
  faq=[
    ("Do respondents need to sign in to open my form?",
     "No. The QR code simply opens your form's link — access follows your form's own sharing settings, not the code."),
    ("Will this QR code expire?",
     "Never. It is a static code: the link lives inside the pattern itself, so it works as long as your form does. No renewals, no vendor to disappear."),
    ("Is it really free? Any watermark?",
     "Completely free, no watermark, no account. Some tools in the search results add watermarks or paywalls — this one doesn't."),
    ("Can I track how many people scanned it?",
     "Static codes don't phone home, which is exactly why they're private. For response counts, use your form's Responses tab — it already tracks everything."),
  ],
 ),
 dict(
  slug="wifi-qr-code", dtype="wifi",
  title="Free WiFi QR Code Generator — Share WiFi Without the Password | FreeQrly",
  desc="Create a free WiFi QR code so guests join your network with one scan. No app needed, no sign-up. Your password never leaves your browser.",
  kw="wifi qr code generator",
  h1="Share your WiFi without spelling the password.",
  lede="Type your network name and password once, print the code, stick it on the fridge. Guests scan and they're online — no more shouting the password across the room.",
  steps=[
    ("Enter your network details", "Network name, password, and security type (WPA2 on most home routers)."),
    ("Print the code", "Download a high-resolution PNG — it stays readable even on a small card."),
    ("Guests scan to join", "iPhone camera (iOS 11+) and Android (10+) connect straight from the scan. No app needed."),
  ],
  studio_h2="Make your WiFi QR code",
  faq=[
    ("Is my WiFi password safe here?",
     "Yes. The code is drawn entirely in your browser — your password is never uploaded or stored anywhere. For extra peace of mind, load the page, disconnect from the internet, then type."),
    ("Which phones can scan a WiFi QR code?",
     "iPhones on iOS 11+ join straight from the Camera app; most Android phones on Android 10+ do the same from the camera or WiFi settings. No extra app needed."),
    ("Does it work with WPA3 or hidden networks?",
     "Choose the security type that matches your router (WPA, WPA2, WEP, or open). Enter a hidden network's name exactly and it connects the same way."),
    ("Can I use this for my café or Airbnb?",
     "Absolutely — that's the classic use. Print it once and it works for every guest, forever, at no cost."),
  ],
 ),
 dict(
  slug="vcard-qr-code", dtype="vcard",
  title="Free vCard QR Code Generator — Contact QR Codes | FreeQrly",
  desc="Turn your contact details into a scannable vCard QR code. Free, no sign-up. One scan saves you straight to their phone.",
  kw="vcard qr code generator",
  h1="Your contact card, one scan away.",
  lede="Name, number, email — encoded into a vCard QR code. Print it on your business card and new contacts save you with a single scan instead of typing.",
  steps=[
    ("Fill in your details", "Name, phone, and email — exactly as you want them saved."),
    ("Style it your way", "Add your logo, pick colors. Higher error correction keeps it scannable with a logo in the middle."),
    ("Print it on everything", "Business cards, email signatures, conference badges. Download PNG or SVG."),
  ],
  studio_h2="Make your vCard QR code",
  faq=[
    ("What information goes into the code?",
     "A standard vCard 3.0 contact: full name, phone number, and email. Phones recognize the format and offer to save it as a new contact."),
    ("Does it work on iPhone and Android?",
     "Yes — both open vCard QR codes natively in the camera app and prompt to create a contact. No extra app needed."),
    ("How big should I print it on a business card?",
     "At least 2 × 2 cm (about 0.8 in) with a quiet margin around it. Export at 1024 px or higher so the print stays sharp."),
    ("Will my details ever expire or change?",
     "The code is static — it carries your details inside the pattern, so it works indefinitely. If your number changes, just generate a fresh one."),
  ],
 ),
 dict(
  slug="batch-qr-code", dtype="batch",
  title="Free Batch QR Code Generator — Bulk QR Codes as ZIP | FreeQrly",
  desc="Generate dozens of QR codes at once and download them as a ZIP. Free, no sign-up, no limits games. One link per line — done.",
  kw="batch qr code generator",
  h1="Dozens of QR codes. One download.",
  lede="Paste your links — one per line — hit generate, and download every code as a tidy ZIP. The batch feature other tools put behind a paywall, free here.",
  steps=[
    ("Paste your links", "One URL per line in the batch box below. Up to 50 at a time."),
    ("Hit Generate all", "Every link becomes its own QR code, previewed in a grid."),
    ("Download the ZIP", "One click packs them all as print-ready PNGs, named qr-1, qr-2, and so on."),
  ],
  studio_h2="Generate your batch",
  faq=[
    ("How many QR codes can I make at once?",
     "Up to 50 per batch. Need more? Run another batch — there's no daily cap or account to hit."),
    ("Is batch generation really free?",
     "Yes. Many generators charge a subscription for bulk export; here it's the same free tool, no watermark, no sign-up."),
    ("What format do the downloads come in?",
     "A single ZIP containing high-resolution PNGs (1024 px), each named qr-1.png, qr-2.png, and so on — ready for print."),
    ("Can I add my logo to batch codes?",
     "Upload your logo once and it applies across the batch, with error correction raised automatically so every code stays scannable."),
  ],
 ),
]

HEADER = '''<header class="top">
    <div class="brand"><a href="/" style="color:inherit;text-decoration:none">Free<em>Qrly</em></a></div>
    <nav class="tnav">
      <a href="#studio">Studio</a><a href="#how">How it works</a><a href="#faq">FAQ</a>
    </nav>
    <div class="topbtns">
      <button class="tbtn" id="langBtn" aria-label="language">中文</button>
      <button class="tbtn" id="themeBtn" aria-label="theme">◐</button>
    </div>
  </header>
  <div class="topline"></div>'''

STUDIO_H2_RE = re.compile(r'<div class="shead"><div class="over" data-i18n="sOver">.*?</div><h2 data-i18n="sTitle">.*?</h2></div>', re.S)

EXTRA_CSS = '''
.lp-hero{grid-template-columns:1fr 1fr;align-items:start}
.steps{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:12px}
.steps li{display:flex;gap:14px;align-items:flex-start;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:15px 17px;font-size:14.5px;line-height:1.6;color:var(--soft)}
.steps .sn{flex-shrink:0;width:26px;height:26px;border-radius:50%;border:1px solid var(--gold);color:var(--gold);font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:1px}
.steps b{color:var(--ink);font-weight:600;display:block;margin-bottom:2px}
@media(max-width:960px){.lp-hero{grid-template-columns:1fr}}
'''

def faq_json(faq):
    return ",\n    ".join(
        '{\n      "@type": "Question",\n      "name": "%s",\n      "acceptedAnswer": {\n        "@type": "Answer",\n        "text": "%s"\n      }\n    }' % (q.replace('"', '\\"'), a.replace('"', '\\"'))
        for q, a in faq)

def build(p):
    url = f"https://freeqrly.com/{p['slug']}/"
    studio = STUDIO_H2_RE.sub(
        '<div class="shead"><div class="over">The studio</div><h2>%s</h2></div>' % p["studio_h2"], STUDIO)
    # studio assets live one level up
    studio = studio.replace('id="batchPanel"', 'id="batchPanel"')  # noop, keep ids
    steps_html = "\n".join(
        '      <li><span class="sn">%d</span><span><b>%s</b>%s</span></li>' % (i+1, t, d)
        for i, (t, d) in enumerate(p["steps"]))
    faq_html = "\n".join(
        '    <details><summary><span>%s</span></summary><p>%s</p></details>' % (q, a)
        for q, a in p["faq"])
    other = [x for x in PAGES if x["slug"] != p["slug"]]
    foot_links = ' · '.join('<a href="/%s/">%s</a>' % (x["slug"], x["kw"]) for x in other)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta name="theme-color" content="#e9eef4">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://freeqrly.com/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232F4A62'/%3E%3Crect x='7' y='7' width='8' height='8' fill='white'/%3E%3Crect x='17' y='7' width='8' height='8' fill='white'/%3E%3Crect x='7' y='17' width='8' height='8' fill='white'/%3E%3Crect x='19' y='19' width='4' height='4' fill='white'/%3E%3C/svg%3E">
<link rel="stylesheet" href="../assets/css/main.css">
<style>{EXTRA_CSS}</style>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebApplication","name":"FreeQrly — {p["kw"]}","applicationCategory":"UtilitiesApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0"}},"url":"{url}","description":"{p["desc"]}"}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {faq_json(p["faq"])}
  ]
}}
</script>
</head>
<body data-lp="{p["slug"]}" data-type="{p["dtype"]}">
<div class="wrap">
{HEADER}
  <section class="hero lp-hero">
    <div>
      <div class="kicker">Free · No sign-up · No watermark</div>
      <h1>{p["h1"]}</h1>
      <p class="lede">{p["lede"]}</p>
    </div>
    <ol class="steps" id="how">
{steps_html}
    </ol>
  </section>
{studio}

  <section class="faq" id="faq">
    <h2>Good to know</h2>
{faq_html}
  </section>

  <footer>
    <div class="fin"><a href="/" style="color:inherit">FreeQrly</a> — made quietly, in your browser.</div>
    <div class="rule"></div>
    <div class="lplinks">{foot_links}</div>
    <div class="tiny">FreeQrly · MMXXVI</div>
  </footer>
</div>
<script src="../assets/lib/qr-code-styling.js"></script>
<script src="../assets/lib/jszip.min.js"></script>
<script src="../assets/js/app.js"></script>
</body>
</html>
'''

for p in PAGES:
    d = os.path.join(SITE, p["slug"])
    os.makedirs(d, exist_ok=True)
    html = build(p)
    open(os.path.join(d, "index.html"), "w").write(html)
    print("wrote", p["slug"], len(html), "bytes")
