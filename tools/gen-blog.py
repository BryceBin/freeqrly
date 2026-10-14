#!/usr/bin/env python3
"""Generate the 2 SEO blog posts for FreeQrly."""
import os

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."

HEADER = '''<header class="top">
    <div class="brand"><a href="/" style="color:inherit;text-decoration:none">Free<em>Qrly</em></a></div>
    <nav class="tnav">
      <a href="/#studio">Studio</a><a href="/blog/">Field notes</a>
    </nav>
    <div class="topbtns">
      <button class="tbtn" id="langBtn" aria-label="language" style="display:none">EN</button>
      <button class="tbtn" id="themeBtn" aria-label="theme">◐</button>
    </div>
  </header>
  <div class="topline"></div>'''

# theme toggle only (no i18n on blog pages)
THEME_JS = '''<script>
(function(){
  const root=document.documentElement;
  const set=d=>{d?root.setAttribute("data-theme","dark"):root.removeAttribute("data-theme");localStorage.setItem("freeqrly-theme",d?"dark":"light")};
  set(localStorage.getItem("freeqrly-theme")==="dark"||(!localStorage.getItem("freeqrly-theme")&&matchMedia("(prefers-color-scheme: dark)").matches));
  document.getElementById("themeBtn").onclick=()=>set(root.getAttribute("data-theme")!=="dark");
})();
</script>'''

POSTS = [
 dict(
  slug="do-qr-codes-expire",
  title="Do QR Codes Expire? The Short Answer Is No — FreeQrly",
  desc="Do QR codes expire? Static QR codes never expire — the pattern holds your link forever. Learn what actually stops working (and why paid codes die).",
  h1="Do QR codes <span class='hl hl-mint'>expire</span>?",
  lede="Short answer: no — at least, not the kind you make here. The longer answer is worth knowing before you print a thousand of them.",
  date="October 13, 2026",
  mascot="sleep",
  body="""
<p>You've seen the warnings: "free QR codes expire!" Usually right next to a pricing page. So let's settle it plainly: a static QR code <strong>cannot expire</strong>. There is no clock inside those little squares. A static code is just your link, drawn as a pattern. As long as the link works, the code works — print it today, scan it in ten years.</p>

<h2>Then why do people say QR codes expire?</h2>
<p>Three different things get tangled together:</p>
<ul>
<li><strong>Dynamic codes die when you stop paying.</strong> Many "free" generators actually make <em>dynamic</em> codes: instead of your link, the pattern holds a short URL on <em>their</em> server, which redirects to your link. Stop paying, and they switch the redirect off. Your code isn't expired — it's been taken hostage.</li>
<li><strong>Links rot; codes don't.</strong> If the page behind the code is deleted, scanning leads nowhere. That's the destination dying, not the code. A QR code pointing at a dead link is a perfectly healthy code with nothing to say.</li>
<li><strong>Trial accounts get deactivated.</strong> Some services tie your codes to an account, then nudge you toward a subscription. The code didn't expire — the account did.</li>
</ul>

<h2>Static vs. dynamic, in one paragraph</h2>
<p>A <strong>static</strong> code encodes the destination directly: <code>WIFI:T:WPA;S:MyCafe;P:secret;;</code> or <code>https://your-site.com/menu</code>. Nothing to maintain, nothing to bill. A <strong>dynamic</strong> code encodes a redirect on someone's server, which lets the owner change the destination later and count scans. Useful for marketing campaigns — and a subscription forever.</p>

<blockquote>Rule of thumb: if the destination will never change — your WiFi, your business card, your restaurant menu — static is not the cheap option. It's the <em>correct</em> option.</blockquote>

<h2>What actually goes wrong with printed codes</h2>
<p>Since expiry isn't a thing, here's what to actually watch for:</p>
<ul>
<li><strong>Print too small.</strong> Keep codes at least 2 × 2 cm with a quiet margin. Tiny codes on business cards are the #1 scan failure.</li>
<li><strong>Low contrast.</strong> Dark ink on a light background. That champagne-on-cream wedding code is beautiful and unreadable.</li>
<li><strong>Damage.</strong> Outdoor codes fade and scratch. Higher error correction (we default to M, and bump it automatically when you add a logo) lets a code survive up to 30% damage.</li>
<li><strong>Link changes.</strong> Moving your site? The old code still points at the old URL. Keep a list of where each code lives.</li>
</ul>

<h2>The FreeQrly angle</h2>
<p>Every code made here is static, free, and yours — no account, no redirect server, nothing to cancel. There is simply no mechanism by which it could expire. That's not a marketing claim; it's just how static codes work when nobody inserts themselves in the middle.</p>
""",
  faq=[
    ("Do free QR codes expire?",
     "No. A free static QR code lasts as long as the link it points to. Codes that 'expire' are dynamic codes tied to a paid subscription — the vendor switches them off when you stop paying."),
    ("Can a QR code stop working?",
     "Yes, but not from expiry. The usual causes: the destination page was deleted, the code was printed too small or with low contrast, or it got physically damaged."),
    ("How long do static QR codes last?",
     "Indefinitely. The pattern encodes your data directly with no server involved, so there's nothing to maintain or renew."),
  ],
 ),
 dict(
  slug="static-vs-dynamic-qr-codes",
  title="Static vs Dynamic QR Codes | FreeQrly",
  desc="Static vs dynamic QR codes explained honestly: when you need an editable, trackable dynamic code — and when static is the smarter, free choice.",
  h1="Static vs <span class='hl hl-blush'>dynamic</span> QR codes",
  lede="One of them is free forever. The other is a subscription. Here's how to tell which one you actually need.",
  date="October 13, 2026",
  mascot="wave",
  body="""
<p>Every QR code generator wants to have the same conversation with you: <em>have you considered dynamic?</em> Before you answer, it helps to know what the two kinds actually are — and why the industry pushes one of them so hard.</p>

<h2>The difference, without the sales pitch</h2>
<p>A <strong>static QR code</strong> contains your destination directly. Scan it and your phone reads the WiFi password, the vCard, or the URL straight out of the pattern. No middleman, no server, no account.</p>
<p>A <strong>dynamic QR code</strong> contains a short link on the vendor's server. Scan it, your phone visits their server, and their server redirects you to the real destination. Because the destination lives on their server, the vendor can change it later — and count every scan.</p>
<p>That's the entire difference. Everything else is consequences.</p>

<h2>When dynamic actually makes sense</h2>
<ul>
<li><strong>You run campaigns.</strong> A poster goes to print next week but the landing page isn't final. Dynamic lets you point it somewhere now and fix it later.</li>
<li><strong>You need scan analytics.</strong> How many people scanned, from where, on what. Static codes are silent; dynamic codes report home.</li>
<li><strong>You A/B test destinations.</strong> Swap the link behind a printed code without reprinting.</li>
</ul>

<h2>When static wins</h2>
<ul>
<li><strong>The destination won't change.</strong> WiFi passwords, business cards, app download links, restaurant menus, museum labels. Most QR codes in the wild are like this.</li>
<li><strong>You don't want a subscription.</strong> Dynamic means paying forever — stop, and the codes die. Static is a one-time act.</li>
<li><strong>Privacy matters.</strong> Every dynamic scan pings the vendor's server. Static scans touch nothing but the destination.</li>
</ul>

<blockquote>Here's the uncomfortable bit: most generators push dynamic because it's recurring revenue, not because you need it. If someone's "free" code requires an account, you're looking at a dynamic code with a trial timer.</blockquote>

<h2>A quick decision guide</h2>
<ul>
<li>WiFi for guests? <strong>Static.</strong></li>
<li>Contact details on a business card? <strong>Static.</strong></li>
<li>Menu that changes seasonally? <strong>Static</strong> — point it at your menu page and update the page, not the code.</li>
<li>Billboard for a product launch with unfinalized URLs? <strong>Dynamic</strong> — this is what it's for.</li>
<li>Need to report scan counts to a client? <strong>Dynamic.</strong></li>
</ul>

<h2>Where FreeQrly stands</h2>
<p>We make static codes — free, unlimited, no account. It's the honest 90% of the job. Dynamic codes with editable links and analytics are on our roadmap for people running campaigns; until then, we'd rather tell you the truth than sell you the subscription.</p>
""",
  faq=[
    ("What is the difference between static and dynamic QR codes?",
     "A static QR code encodes the destination directly in the pattern — free forever, uneditable. A dynamic QR code encodes a redirect on the vendor's server, so the destination can be changed later and scans can be tracked — but it requires an ongoing subscription."),
    ("Do I need a dynamic QR code?",
     "Probably not. If your destination won't change — WiFi, business cards, fixed links — static is the right choice. You need dynamic only for editable destinations or scan analytics, typically in marketing campaigns."),
    ("Why do free QR code generators push dynamic codes?",
     "Because dynamic codes require their server, which justifies a subscription. Many 'free' generators create dynamic codes tied to a trial — the code stops working when the trial ends."),
  ],
 ),
]


POSTS += [{'body': '\n'
          '<h2>On iPhone</h2>\n'
          '<p>Open the Camera app and point it at the code — hold steady for a second. A yellow '
          "notification appears; tap it. That's it. This works on iOS 11 and later, so unless your "
          "phone is ancient, you're covered.</p>\n"
          '<p>Two shortcuts worth knowing: open <b>Control Center</b> and tap the QR scanner icon '
          "(add it via Settings → Control Center if it's missing), or long-press the Camera icon "
          'on the lock screen. If the code is in a photo or screenshot, open it in the Photos app '
          'and long-press the code — iOS detects it right in the image.</p>\n'
          '<h2>On Android</h2>\n'
          '<p>Most Android phones scan from the built-in camera too: point, wait for the prompt, '
          'tap. On Pixel and many others, <b>Google Lens</b> in the camera or Google app handles '
          'it. Samsung phones have a dedicated scanner in the Quick Settings panel — swipe down '
          'and look for "Scan QR code". And like iPhone, you can open a saved image in Google '
          'Photos and tap the Lens button.</p>\n'
          '<h2>When nothing happens</h2>\n'
          "<p>Nine times out of ten it's the code, not your phone: too small, low contrast, "
          "damaged, or printed on a curve. There's a full checklist in <a "
          'href="/blog/why-is-my-qr-code-not-working/">why your QR code won\'t scan</a>. Dirty '
          'camera lens is the classic overlooked one — wipe it and try again.</p>\n'
          '<h2>A 3-second safety habit</h2>\n'
          '<p>Your phone shows a preview of the link before opening it. Glance at it. If a code on '
          'a lamppost promises a parking meter but the URL looks like a random string of '
          "characters, don't tap — stickers over real codes are a known scam. Codes you generate "
          'yourself with <a href="/">FreeQrly</a> are static and contain exactly what you typed, '
          'nothing hidden.</p>\n',
  'date': '2026-10-14',
  'desc': 'How to scan a QR code on iPhone and Android — no app needed. Use the built-in camera, '
          "Control Center, or Google Lens, and fix it when it won't scan.",
  'faq': [('Do I need an app to scan QR codes?',
           'No. iPhones (iOS 11+) and virtually all Android phones scan QR codes with the built-in '
           'camera. Third-party scanner apps are unnecessary and often full of ads.'),
          ('How do I scan a QR code from a screenshot?',
           'On iPhone, open the screenshot in Photos and long-press the code. On Android, open it '
           'in Google Photos and tap the Lens button.'),
          ("Why won't my camera scan the QR code?",
           "Usually the code is too small, low contrast, damaged, or there's no quiet zone around "
           'it. Wipe your lens, move closer, and see the full fix list in our troubleshooting '
           'guide.')],
  'h1': 'How to <span class="hl hl-mint">scan</span> a QR code',
  'howto': [('Point your camera at the code',
             'Open the built-in Camera app and point it at the QR code, keeping the whole square '
             'in frame.'),
            ('Tap the notification',
             'A banner or link preview appears — tap it to open the destination.'),
            ('Check the preview first',
             'Glance at the URL before opening, especially on codes you find in public places.')],
  'lede': 'No app required. Every modern iPhone and Android phone scans QR codes with the camera '
          "it already has. Here's how — plus what to do when nothing happens.",
  'mascot': 'wave',
  'slug': 'how-to-scan-a-qr-code',
  'title': 'How to Scan a QR Code (iPhone & Android) | FreeQrly'},
 {'body': '\n'
          "<h2>1. It's too small</h2>\n"
          "<p>The classic. A code squeezed into the corner of a business card at 1 cm wide won't "
          'scan reliably. Minimum for print: <b>2x2 cm</b> (about 0.8 inches), and bigger is '
          "always safer. There's a full breakdown in the <a "
          'href="/blog/qr-code-print-size-guide/">print size guide</a>.</p>\n'
          '<h2>2. Low contrast killed it</h2>\n'
          '<p>QR readers look for dark modules on a light background. Light gray on white, brand '
          'pastels, or a code over a busy photo will fail — especially in dim light. When in '
          'doubt: black on white always works.</p>\n'
          "<h2>3. It's damaged or faded</h2>\n"
          '<p>Creased flyers, sun-faded posters, scratched stickers. Error correction can survive '
          'some damage (that\'s why <a href="/qr-code-with-logo/">adding a logo</a> works), but '
          "there's a limit. If a quarter of the code is gone, reprint.</p>\n"
          '<h2>4. No quiet zone</h2>\n'
          "<p>The blank margin around the code isn't decoration — scanners need it to find the "
          "edges. Keep a clear border at least as wide as one module on all four sides. Don't let "
          'text or design elements crowd it.</p>\n'
          '<h2>5. Glare, curve, or angle</h2>\n'
          '<p>Glossy lamination under bright light, a code wrapped around a bottle, or shot at a '
          'steep angle. Flatten it, kill the glare, shoot straight on.</p>\n'
          '<h2>6. The content is dead</h2>\n'
          '<p>The code scans fine — but the link is broken, the page moved, or the "free" '
          "generator's trial expired and took your code with it. This is the expired-link trap: <a "
          'href="/blog/do-qr-codes-expire/">do QR codes expire?</a> explains which ones do and how '
          'to avoid them.</p>\n'
          '<h2>7. Your camera</h2>\n'
          '<p>Wipe the lens. Seriously — a smudged lens is behind an embarrassing number of '
          '"broken" codes. Then test on a second phone: if phone B reads it, the code was never '
          'the problem.</p>\n'
          '<h2>Test before you print</h2>\n'
          '<p>Scan the code on two different phones (one iPhone, one Android if you can) before '
          'sending anything to print. Thirty seconds now saves a reprint later. Generate a test '
          'code in the <a href="/">free generator</a> and try it.</p>\n',
  'date': '2026-10-14',
  'desc': 'QR code not scanning? Seven real fixes: size, contrast, damage, quiet zone, and the '
          'expired-link trap — plus how to test before you print.',
  'faq': [('Why does my QR code scan on one phone but not another?',
           "Then the code itself is fine — it's the camera, lighting, or angle on the failing "
           'phone. Wipe the lens and try in better light.'),
          ('Can a damaged QR code still work?',
           'Often yes, thanks to error correction — up to 30% damage can be tolerated at the High '
           'setting. But heavy damage, fading, or missing finder patterns will kill it.'),
          ("My QR code scans but the link doesn't work — is the code broken?",
           'No, the code is doing its job. The destination is the problem: the page moved, the '
           'site is down, or a trial-based generator deactivated it.')],
  'h1': 'Why won\\u2019t this thing <span class="hl hl-blush">scan</span>?',
  'howto': [('Check the size',
             'Printed codes need to be at least 2x2 cm. On screen, make it at least 2 cm wide on '
             'your display.'),
            ('Check the contrast',
             'Dark code on a light background. Fancy low-contrast color pairs are the #1 design '
             'killer.'),
            ('Test on a second phone',
             "If one phone reads it and another doesn't, the code is fine — it's the camera or "
             'lighting.'),
            ('Re-export at higher resolution',
             'Blurry edges from a low-res export fail at print size. Export PNG at 1024 px or '
             'higher, or use SVG.')],
  'lede': "A QR code that won't scan is almost never a mystery. Run through these seven checks — "
          "in order — and you'll find the culprit in about two minutes.",
  'mascot': 'qr',
  'slug': 'why-is-my-qr-code-not-working',
  'title': 'QR Code Not Working? 7 Fixes That Help | FreeQrly'},
 {'body': '\n'
          '<h2>The two rules that matter</h2>\n'
          '<p><b>Rule 1 — minimum size:</b> 2 x 2 cm (0.8 x 0.8 in). Below that, phone cameras '
          "can't resolve the modules reliably, especially codes holding a lot of data like "
          'vCards.</p>\n'
          "<p><b>Rule 2 — the 1:10 distance ratio:</b> the code's width should be at least "
          'one-tenth of the scanning distance. Scanning from 50 cm (a table card)? 5 cm code. From '
          '5 meters (a poster)? 50 cm code. Printers and signage folks live by this ratio.</p>\n'
          '<h2>Cheat sheet by use case</h2>\n'
          '<p><b>Business cards:</b> 2x2 cm minimum — see the <a '
          'href="/business-card-qr-code/">business card generator</a>. Keep it clear of the card '
          'edge.<br>\n'
          "<b>Flyers &amp; menus:</b> 3x3 cm. People scan these at arm's length.<br>\n"
          '<b>Table tents:</b> 4–5 cm, so guests scan from their seats.<br>\n'
          '<b>Posters:</b> use the 1:10 ratio against expected viewing distance.<br>\n'
          '<b>Packaging:</b> 2x2 cm minimum, and avoid curved surfaces that distort the '
          'pattern.</p>\n'
          '<h2>Resolution: export big</h2>\n'
          '<p>Print needs 300 dpi. A 2 cm code at 300 dpi is only ~240 px — but always export '
          'larger and let the designer scale down: <b>PNG at 1024 or 2048 px</b>, or <b>SVG</b> '
          'which is infinitely scalable and the best choice for professional print. FreeQrly '
          'exports both, free.</p>\n'
          "<h2>Don't forget the quiet zone</h2>\n"
          '<p>Leave a blank margin around the code at least 4 modules wide on every side. Crowding '
          'it with text or graphics is one of the top reasons codes fail — more in <a '
          'href="/blog/why-is-my-qr-code-not-working/">why your code won\'t scan</a>.</p>\n'
          '<h2>Logo in the middle? Go bigger</h2>\n'
          '<p>A <a href="/qr-code-with-logo/">logo in the center</a> eats into the pattern, so '
          "give it room: 3x3 cm minimum in print, and keep the logo under ~30% of the code's "
          'area.</p>\n',
  'date': '2026-10-14',
  'desc': 'How big should a QR code be in print? Minimum sizes for business cards, flyers, and '
          'posters — plus resolution and quiet-zone rules that keep codes scannable.',
  'faq': [('What is the minimum size for a printed QR code?',
           '2 x 2 cm (0.8 x 0.8 inches). Smaller codes fail on many phones, especially for '
           'data-heavy codes like vCards.'),
          ('How big should a QR code be on a poster?',
           'Use the 1:10 rule: the code width should be at least one-tenth of the expected '
           'scanning distance. A poster scanned from 5 meters needs a 50 cm code.'),
          ('PNG or SVG for print?',
           'SVG is best — it scales infinitely with no quality loss. If your printer needs raster, '
           'export PNG at 2048 px.')],
  'h1': 'How <span class="hl hl-mint">big</span> should a printed QR code be?',
  'lede': 'The short answer: at least 2x2 cm, at 300 dpi, with a clear margin. The longer answer — '
          'with the distance rule printers actually use — is below.',
  'mascot': 'batch',
  'slug': 'qr-code-print-size-guide',
  'title': 'QR Code Print Size Guide: How Big Should It Be? | FreeQrly'},
 {'body': '\n'
          '<h2>1. The menu code</h2>\n'
          '<p>Link it to your online menu — your website, a PDF, or your Google Business menu. '
          'Print one per table or a single framed code at the entrance. Generate it with the <a '
          'href="/google-form-qr-code/">link generator</a> in seconds, export at 1024 px, and '
          "you're done. Pro tip: link to a page you control, not a screenshot — when the menu "
          'changes, you update the page, not the print.</p>\n'
          '<h2>2. The review code</h2>\n'
          '<p>This is the highest-ROI square centimeter in your restaurant. A code linking '
          'straight to your Google review form — on the receipt, the table tent, the takeout bag — '
          "turns happy meals into public reviews. There's a dedicated <a "
          'href="/google-review-qr-code/">Google review QR generator</a> that walks through '
          'finding your review link.</p>\n'
          '<h2>3. The WiFi code</h2>\n'
          '<p>Guests ask for the WiFi password fifty times a day. A <a href="/wifi-qr-code/">WiFi '
          'QR code</a> on each table connects them in one scan — no spelling out "capital K, '
          'underscore, 123" ever again. It never expires, so print it once.</p>\n'
          '<h2>Printing tips for restaurants</h2>\n'
          '<p>Laminate table codes (spills happen), use at least 3x3 cm so guests scan from their '
          'seats, and keep contrast high — dim dining rooms punish pastel codes. Full sizing '
          'rules: <a href="/blog/qr-code-print-size-guide/">print size guide</a>.</p>\n'
          '<h2>What it costs</h2>\n'
          '<p>Nothing. These are static codes — no subscriptions, no scan limits, no "pro plan" to '
          "unlock the menu link. Print them once and they work for years. That's the whole "
          'pitch.</p>\n',
  'date': '2026-10-14',
  'desc': 'How restaurants use QR codes: digital menus, Google reviews, and guest WiFi. Free setup '
          'guide with printable codes — no sign-up, no fees.',
  'faq': [('What QR codes does a restaurant need?',
           'Three: a menu link, a Google review link, and the WiFi credentials. That covers nearly '
           'every guest interaction.'),
          ('Should the menu QR link to a PDF or a webpage?',
           'A webpage you control. When prices change you update the page — the printed code stays '
           'the same. A PDF works but is harder to update.'),
          ('How do I get more Google reviews with a QR code?',
           'Link a code directly to your Google review form and place it where happy customers '
           'look: receipts, table tents, takeout bags.')],
  'h1': 'The restaurant <span class="hl hl-blush">playbook</span>',
  'lede': 'Three QR codes cover 90% of what a restaurant needs: the menu, the review link, and the '
          'WiFi password. All free, all printable today.',
  'mascot': 'party',
  'slug': 'qr-codes-for-restaurants',
  'title': 'QR Codes for Restaurants — Free Guide | FreeQrly'},
 {'body': '\n'
          '<h2>Static vs. dynamic: the only distinction that matters</h2>\n'
          '<p>A <b>static</b> code encodes your link directly in the pattern. Nothing to expire, '
          'nothing to renew — it works as long as the link works. A <b>dynamic</b> code encodes a '
          "redirect on the vendor's server, so they can charge you monthly to keep it alive. The "
          'full explainer: <a href="/blog/static-vs-dynamic-qr-codes/">static vs dynamic QR '
          'codes</a>.</p>\n'
          '<h2>The trial trap</h2>\n'
          '<p>Many "free QR code generators" quietly create dynamic codes on a 7- or 14-day trial. '
          'Your printed flyers work beautifully — until the trial ends and every code goes dead. '
          'Red flags: the site asks for your email before generating, mentions "scan analytics", '
          'or talks about "campaigns". A truly free static generator needs none of that.</p>\n'
          '<h2>The 30-second test</h2>\n'
          '<p>Before you trust a generator with your print run: generate a code <b>without '
          "creating an account</b>. If it works, it's static. FreeQrly only makes static codes — "
          "no accounts exist, so there's nothing to expire. That's also why <a "
          'href="/blog/do-qr-codes-expire/">QR codes don\'t have to expire</a>.</p>\n'
          "<h2>What can still break (it's not the code)</h2>\n"
          '<p>A static code lasts forever, but its destination might not: if you delete the page '
          'it links to, the code "stops working". Link to stable URLs you control, and your codes '
          'will outlive most of your marketing materials.</p>\n'
          '<h2>Make yours</h2>\n'
          '<p>Pick any type in the <a href="/">free generator</a> — link, vCard, WiFi — download '
          'the PNG or SVG, and print it. No sign-up, no trial, no expiry date hiding in the fine '
          'print.</p>\n',
  'date': '2026-10-14',
  'desc': "Free QR codes that don't expire do exist — they're called static codes. How to spot "
          'trial-trap generators and make codes that last forever.',
  'faq': [('Do free QR codes expire?',
           "Static ones don't — the destination is baked into the pattern. Dynamic ones from "
           'trial-based generators stop working when the subscription or trial ends.'),
          ('How can I tell if my QR code will expire?',
           "If the generator required an account or email, it's almost certainly dynamic and tied "
           'to a subscription. True static generators work with no sign-up.'),
          ("What's the catch with FreeQrly?",
           "There isn't one for static codes: they're generated entirely in your browser, so "
           "there's no server cost to pass on to you.")],
  'h1': 'Free codes that <span class="hl hl-mint">never</span> expire',
  'lede': "Yes, they exist — they're called static QR codes. Here's how to tell them apart from "
          'the trial-trap kind, and how to make yours in 30 seconds.',
  'mascot': 'sleep',
  'slug': 'free-qr-codes-that-dont-expire',
  'title': "Free QR Codes That Never Expire | FreeQrly"}]


POSTS += [{'body': '\n'
          '<h2>Why "no upload" matters</h2>\n'
          '<p>QR codes often contain sensitive things: WiFi passwords, event tickets, boarding '
          "passes, private links. Uploading that image to a stranger's server — just to read it — "
          "is a privacy trade most people don't realize they're making. FreeQrly's <a "
          'href="/scan/">QR scanner</a> decodes the image with JavaScript on your device (the '
          'open-source jsQR library). The image never leaves the page.</p>\n'
          '<h2>Two ways to scan</h2>\n'
          '<p><b>Camera:</b> hit "Start camera", point at the code, done. Uses your rear camera on '
          "phones. Your browser will ask for camera permission once — that's between you and your "
          'browser; we never see the feed.</p>\n'
          '<p><b>Upload:</b> got a screenshot, a saved flyer, or a photo with a code in it? Upload '
          "the image and it's decoded instantly. This even works <b>offline</b> — load the page "
          'once, disconnect, and upload scanning still works.</p>\n'
          '<h2>What you get back</h2>\n'
          '<p>The raw decoded content, plus smart actions: links get an "Open link" button (check '
          'the URL first — the <a href="/blog/how-to-scan-a-qr-code/">scanning guide</a> has a '
          '3-second safety habit), everything else gets a Copy button.</p>\n'
          "<h2>When it can't read your code</h2>\n"
          '<p>Blurry photos, tiny codes, heavy glare — the usual suspects. The full fix list is in '
          '<a href="/blog/why-is-my-qr-code-not-working/">why your QR code won\'t scan</a>. And if '
          'you need to <a href="/">make your own QR code</a> instead, that\'s the main studio — '
          'also free, also private.</p>\n',
  'date': '2026-10-14',
  'desc': 'Scan QR codes online for free: use your camera or upload an image. Decoded in your '
          'browser — nothing is ever uploaded. No app, no sign-up.',
  'faq': [('Is it safe to scan QR codes online?',
           'It depends where the image goes. Most online scanners upload your image to their '
           'server. FreeQrly decodes it locally in your browser, so nothing is transmitted '
           'anywhere.'),
          ('Do I need to download an app to scan QR codes?',
           'No. The scanner runs in any modern browser on phone or desktop — camera mode on '
           'mobile, image upload everywhere.'),
          ('Can I scan a QR code from a screenshot?',
           "Yes — upload the screenshot and it's decoded instantly, even offline after the page "
           'has loaded.')],
  'h1': 'Scan QR codes <span class="hl hl-mint">online</span>, privately',
  'howto': [('Open the scanner',
             'Go to the FreeQrly scanner — no app to install, no account needed.'),
            ('Use your camera or upload',
             'Point your camera at the code, or upload a photo or screenshot that contains one.'),
            ('Get the result instantly',
             'The decoded text or link appears immediately. Links get an Open button; everything '
             'else gets Copy.')],
  'lede': "Most online QR scanners make you upload your image to their server. Ours doesn't — the "
          'code is decoded right in your browser. Camera or image upload, free forever.',
  'mascot': 'qr',
  'slug': 'scan-qr-code-online',
  'title': 'Scan QR Codes Online — Free, No App, No Upload | FreeQrly'},
 {'body': '\n'
          '<h2>On iPhone</h2>\n'
          '<p>Open the photo in the Photos app and <b>long-press the QR code</b> — iOS detects it '
          'right in the image and offers to open the link. No extra tools needed.</p>\n'
          '<h2>On Android</h2>\n'
          '<p>Open the image in Google Photos and tap the <b>Lens</b> button. Most gallery apps on '
          'Samsung and Pixel phones do the same from the share menu.</p>\n'
          '<h2>On PC / Mac</h2>\n'
          "<p>Phones can't help you here — this is where an online decoder earns its keep. Take a "
          'screenshot (or save the image), then upload it to <a href="/scan/">FreeQrly\'s '
          "scanner</a>. It's decoded in your browser, so the image is never uploaded anywhere — "
          'nice when the screenshot contains something private.</p>\n'
          '<h2>Tips for stubborn images</h2>\n'
          '<p>Crop tight around the code before uploading — decoders work faster and more reliably '
          'on a clean crop. If the photo is blurry or shot at an angle, no decoder can save it; '
          'retake it straight-on. More in <a href="/blog/why-is-my-qr-code-not-working/">why your '
          "QR code won't scan</a>.</p>\n"
          '<h2>Privacy note</h2>\n'
          '<p>Screenshots often contain more than the QR code — chats, tickets, personal photos. '
          'Think twice before uploading them to a random decoder site. A <a href="/scan/">local '
          'decoder</a> never sees anything but your own browser tab.</p>\n',
  'date': '2026-10-14',
  'desc': 'How to scan a QR code from a picture, photo, or screenshot — on iPhone, Android, and '
          'PC. Free online decoder, no app needed.',
  'faq': [('How do I scan a QR code from a screenshot on iPhone?',
           'Open the screenshot in Photos and long-press the code — iOS reads it directly from the '
           'image.'),
          ('How do I scan a QR code from an image on PC?',
           'Upload the image to a free online QR decoder. Prefer one that decodes locally in the '
           'browser so your image is never uploaded.'),
          ("Why can't the decoder read my picture?",
           'Usually blur, a steep angle, or the code is too small in the frame. Crop tightly '
           'around the code and try again in good light.')],
  'h1': 'Scan a QR code <span class="hl hl-honey">from a picture</span>',
  'howto': [('Save or open the picture',
             'Screenshot it, save it, or just open the photo that contains the QR code.'),
            ('Upload it to a decoder',
             'Use a free online decoder that reads the image — preferably one that works locally, '
             'so the picture is never uploaded.'),
            ('Read the result',
             'The decoded link or text appears instantly. Check the URL before opening, as '
             'always.')],
  'lede': "The code is in a photo, not in front of your camera. Here's how to decode it on iPhone, "
          'Android, and desktop — no app required.',
  'mascot': 'wave',
  'slug': 'scan-qr-code-from-image',
  'title': 'How to Scan a QR Code from a Picture | FreeQrly'},
 {'body': '\n'
          '<h2>1. Check-in &amp; registration</h2>\n'
          '<p>Put a code on the confirmation email linking to a check-in form (or a simple "I\'m '
          'here" page). Guests scan at the door instead of spelling their names for a volunteer '
          'with a clipboard. For ticketed events, link each ticket to its validation page.</p>\n'
          '<h2>2. Add-to-calendar codes</h2>\n'
          "<p>The most underused event code: one that drops the event straight into the guest's "
          'calendar. FreeQrly\'s <a href="/?type=event">event QR type</a> builds it in seconds — '
          'title, start/end time, location — and scanning it offers "add to calendar" on both '
          'iPhone and Android. Print it on the invitation and watch no-show rates drop.</p>\n'
          '<h2>3. The shared photo album</h2>\n'
          '<p>Every event has the same problem: the photos scatter across fifty phones. A code '
          'linking to a shared album (Google Photos, iCloud shared album) on table cards fixes it '
          '— guests upload their shots in one tap. Autocomplete shows "event qr code for photos" '
          'is exactly what organizers search for.</p>\n'
          '<h2>4. WiFi for the venue</h2>\n'
          '<p>Attendees will ask for WiFi. A <a href="/wifi-qr-code/">WiFi QR code</a> on signage '
          'connects them in one scan — no password spelling over loud music.</p>\n'
          '<h2>5. Feedback &amp; follow-up</h2>\n'
          '<p>A code linking to a 2-question feedback form on the exit signage or closing slide. '
          'Response rates beat emailed surveys by a mile.</p>\n'
          '<h2>Printing tips</h2>\n'
          '<p>Event codes get scanned in chaotic lighting by hurried people: go bigger than you '
          'think (the <a href="/blog/qr-code-print-size-guide/">1:10 distance rule</a>), keep '
          'contrast high, and test on both iPhone and Android before printing a hundred table '
          "cards. Static codes never expire, so last year's signage template still works.</p>\n",
  'date': '2026-10-14',
  'desc': 'How to use QR codes for events: check-in, registration, tickets, photo sharing, and '
          'add-to-calendar codes. Free generator, no sign-up.',
  'faq': [('How do I make a QR code for event check-in?',
           'Link the code to your check-in form or registration page, print it for the entrance, '
           'and guests scan on arrival instead of queueing at a desk.'),
          ('Can a QR code add an event to my calendar?',
           "Yes — calendar (VEVENT) QR codes open an 'add to calendar' prompt on iPhones and "
           'Androids. FreeQrly generates them free with its event type.'),
          ('What QR codes do I need for an event?',
           'At minimum: check-in/registration, a shared photo album, and venue WiFi. '
           'Add-to-calendar codes on invitations are the high-ROI extra.')],
  'h1': 'QR codes for <span class="hl hl-blush">events</span>, done right',
  'lede': "Check-in lines, ticket chaos, 'where are the photos?' — a few well-placed QR codes "
          "solve the recurring event headaches. Here's the playbook.",
  'mascot': 'party',
  'slug': 'qr-codes-for-events',
  'title': 'QR Codes for Events: Check-In, Tickets & More | FreeQrly'},
 {'body': '\n'
          '<h2>The setup</h2>\n'
          '<p>Build your RSVP form first (Google Forms is free and perfect for this — see the <a '
          'href="/google-form-qr-code/">Google Form QR generator</a>). Then generate the code, '
          'print it on the invitation suite, and guests scan → tap → done. No stamps, no lost '
          'reply cards, no deciphering handwriting.</p>\n'
          '<h2>Where to print it</h2>\n'
          '<p><b>Invitations:</b> on the details card, at least 2x2 cm. <b>Save-the-dates:</b> '
          'link it to your wedding website. <b>Table cards:</b> a second code linking to the <a '
          'href="/wedding-qr-code/">shared photo album</a> — guests upload their shots all '
          'night.</p>\n'
          '<h2>The add-to-calendar trick</h2>\n'
          '<p>Pair the RSVP code with an <a href="/?type=event">event QR code</a> on the '
          'invitation. One scan drops your wedding — date, time, venue — into their calendar. '
          'Fewer "wait, when was it again?" texts.</p>\n'
          '<h2>RSVP wording that works</h2>\n'
          '<p>Next to the code, print exactly what to do: <i>"Scan to RSVP by June 1st."</i> Older '
          'guests may need the nudge — and keep a phone number on the invitation for the truly '
          'scan-averse.</p>\n'
          '<h2>After the RSVPs roll in</h2>\n'
          '<p>Google Forms tallies responses automatically — meal choices included. Export to a '
          'sheet, share with the caterer, done. The whole pipeline costs nothing: free form, <a '
          'href="/">free QR code</a>, zero postage.</p>\n',
  'date': '2026-10-14',
  'desc': 'How to use QR codes for wedding RSVPs: link your RSVP form, print on invitations, track '
          'responses. Free generator — no sign-up.',
  'faq': [('How do I create a QR code for my wedding RSVP?',
           'Make your RSVP form (Google Forms works great), paste its link into a free QR '
           'generator, and print the code on your invitations at 2x2 cm or larger.'),
          ('Should the RSVP QR code link to a form or a website?',
           'A form — one tap to respond. Link your wedding website separately for details like '
           'travel and registry.'),
          ('Do wedding QR codes expire?',
           "Static ones don't. Generate them months ahead; they'll scan on the day and for years "
           'after as a keepsake.')],
  'h1': 'Wedding <span class="hl hl-honey">RSVP</span> codes, minus the chase',
  'lede': 'Half your RSVPs are late because the reply card is sitting in a drawer. A QR code on '
          'the invitation — straight to your RSVP form — fixes the biggest wedding admin headache.',
  'mascot': 'wave',
  'slug': 'wedding-rsvp-qr-code',
  'title': 'Wedding RSVP QR Codes: A Complete Guide | FreeQrly'}]

REL_CSS = """<style>
.rel-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:10px}
.rel-card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 16px;text-decoration:none;color:inherit;display:block}
.rel-card:hover{border-color:var(--gold)}
.rel-card b{font-size:14px;font-weight:600;line-height:1.4}
@media(max-width:720px){.rel-grid{grid-template-columns:1fr}}
</style>"""
def faq_json(faq):
    return ",\n    ".join(
        '{\n      "@type": "Question",\n      "name": "%s",\n      "acceptedAnswer": {\n        "@type": "Answer",\n        "text": "%s"\n      }\n    }' % (q.replace('"', '\\"'), a.replace('"', '\\"'))
        for q, a in faq)

def build(p, all_posts=None):
    url = f"https://freeqrly.com/blog/{p['slug']}/"
    rel_html = ""
    if all_posts:
        others = [q for q in all_posts if q["slug"] != p["slug"]]
        # pick 3: rotate by index for variety
        idx = all_posts.index(p)
        picks = [others[(idx + i) % len(others)] for i in (1, 3, 5)]
        rel_html = "\n".join(
            '        <a class="rel-card" href="/blog/%s/"><b>%s</b></a>' % (q["slug"], q["title"].split("|")[0].strip())
            for q in picks)
    howto_json = ""
    if p.get("howto"):
        steps_json = ",\n    ".join(
            '{\n      "@type": "HowToStep",\n      "name": "%s",\n      "text": "%s"\n    }' % (s[0].replace('"', '\\"'), s[1].replace('"', '\\"'))
            for s in p["howto"])
        howto_json = '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"HowTo","name":"' + p["title"].replace('"','\\"') + '","description":"' + p["desc"].replace('"','\\"') + '","step":[\n    ' + steps_json + '\n  ]}\n</script>\n'

    faq_html = "\n".join(
        '    <details><summary><span>%s</span></summary><p>%s</p></details>' % (q, a)
        for q, a in p["faq"])
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
<meta name="theme-color" content="#FAF5EA">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://freeqrly.com/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="../../assets/img/favicon-elephant.png">
<link rel="apple-touch-icon" href="../../assets/img/favicon-elephant.png">
<link rel="stylesheet" href="../../assets/css/main.css">
{REL_CSS}
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{p["title"]}","description":"{p["desc"]}","datePublished":"2026-10-13","author":{{"@type":"Organization","name":"FreeQrly"}},"publisher":{{"@type":"Organization","name":"FreeQrly"}}}}
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
{howto_json}</head>
<body>
<div class="wrap">
{HEADER}
  <article class="article">
    <div class="mascot mascot-blog" aria-hidden="true"><img src="../../assets/img/elephant-{p["mascot"]}.png" alt="FreeQrly elephant mascot"></div>
    <div class="kicker" style="text-align:center">Field notes</div>
    <h1 style="text-align:center;max-width:640px;margin:0 auto">{p["h1"]}</h1>
    <p class="lede" style="text-align:center;margin-left:auto;margin-right:auto">{p["lede"]}</p>
    <p class="meta" style="text-align:center">{p["date"]} · 4 min read</p>
    <div class="prose" style="margin-top:40px">
{p["body"]}
    </div>
    <div class="cta-card">
      <div class="mascot" aria-hidden="true"><img src="../../assets/img/elephant-qr.png" alt="FreeQrly elephant mascot showing a QR code"></div>
      <div>
        <h3>Try it yourself — free, no sign-up</h3>
        <p>Everything in this article works in the FreeQrly studio right now. Static codes, eight content types, PNG and SVG export.</p>
        <a class="btn" href="/#studio">Open the studio</a>
      </div>
    </div>
    <div class="related">
      <div class="fl" style="margin-top:34px">Keep reading</div>
      <div class="rel-grid">
{rel_html}
      </div>
    </div>
    <section class="faq" id="faq" style="margin-top:50px">
      <h2>Good to know</h2>
{faq_html}
    </section>
  </article>
  <footer>
    <div class="fin"><a href="/" style="color:inherit">FreeQrly</a> — made quietly, in your browser.</div>
    <p class="flinks"><a href="/scan/">QR scanner</a><a href="/blog/">All field notes</a><a href="/about/">About</a></p>
    <div class="rule"></div>
    <div class="tiny">FreeQrly · MMXXVI</div>
  </footer>
</div>
{THEME_JS}
</body>
</html>
'''

for p in POSTS:
    d = os.path.join(SITE, "blog", p["slug"])
    os.makedirs(d, exist_ok=True)
    html = build(p, POSTS)
    open(os.path.join(d, "index.html"), "w").write(html)
    print("wrote blog/" + p["slug"], len(html), "bytes")
