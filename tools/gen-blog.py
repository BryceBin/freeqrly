#!/usr/bin/env python3
"""Generate the 2 SEO blog posts for FreeQrly."""
import os

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."

HEADER = '''<div id="siteHeader"></div>
<script src="/assets/js/site-header.js?v=b3r-20261020"></script>
<script src="/assets/js/acct-menu.js?v=b3r-20261020"></script>
<script src="/assets/js/subpage-header.js?v=b3r-20261020"></script>'''

THEME_JS = ''

POSTS = [
 dict(
  slug="do-qr-codes-expire",
  title="Do QR Codes Expire? The Short Answer Is No — FreeQrly",
  desc="Do QR codes expire? Static QR codes never expire — the pattern holds your link forever. Learn what actually stops working (and why paid codes die).",
  h1="Do QR codes <span class='hl hl-mint'>expire</span>?",
  lede="Short answer: no — at least, not the kind you make here. The longer answer is worth knowing before you print a thousand of them.",
  date="October 13, 2026",
  mascot="privacy",
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
<li><strong>Print too small.</strong> As a rule of thumb, keep codes at least 2 × 2 cm with a quiet margin. Tiny codes on business cards are a common scan failure.</li>
<li><strong>Low contrast.</strong> Dark ink on a light background. That champagne-on-cream wedding code is beautiful and unreadable.</li>
<li><strong>Damage.</strong> Outdoor codes fade and scratch. Higher error correction (we default to M, and bump it automatically when you add a logo) lets a code survive <a href="http://www.iso.org/standard/83389.html">up to 30% damage</a> at the High level defined in ISO/IEC 18004.</li>
<li><strong>Link changes.</strong> Moving your site? The old code still points at the old URL. Keep a list of where each code lives.</li>
</ul>

<h2>The FreeQrly angle</h2>
<p>Every static code made here is free, and yours — no account, no redirect server, nothing to cancel. There is simply no mechanism by which it could expire. That's not a marketing claim; it's just how static codes work when nobody inserts themselves in the middle.</p>
""",
  faq=[
    ("Do free QR codes expire?",
     "No. A free static QR code lasts as long as the link it points to. Codes that 'expire' are dynamic codes tied to a paid subscription — the vendor switches them off when you stop paying."),
    ("Can a QR code stop working?",
     "Yes, but not from expiry. The usual causes: the destination page was deleted, the code was printed too small or with low contrast, or it got physically damaged."),
    ("How long do static QR codes last?",
     "Indefinitely. The pattern encodes your data directly with no server involved, so there's nothing to maintain or renew."),
  ],
  sources=[("http://www.iso.org/standard/83389.html", "ISO/IEC 18004:2024", "The QR Code symbology specification. Defines the four error-correction levels (L 7%, M 15%, Q 25%, H 30%) and the 4-module quiet zone.")],
 ),
 dict(
  slug="static-vs-dynamic-qr-codes",
  title="Static vs Dynamic QR Codes | FreeQrly",
  desc="Static vs dynamic QR codes explained honestly: when you need an editable, trackable dynamic code — and when static is the smarter, free choice.",
  h1="Static vs <span class='hl hl-blush'>dynamic</span> QR codes",
  lede="One of them is free forever. The other is a subscription. Here's how to tell which one you actually need.",
  date="October 13, 2026",
  mascot="faq",
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
<p>FreeQrly makes both. Static codes are free, unlimited, no account — and cover most everyday needs. Dynamic codes are free too: sign in (email, Google, or GitHub) and you get 8 editable codes with scan stats. <a href="/blog/how-to-create-a-dynamic-qr-code/">How to create one</a>, <a href="/blog/how-to-edit-a-qr-code-after-printing/">how to edit after printing</a>, and <a href="/blog/dynamic-qr-code-statistics/">what the stats tell you</a>.</p>
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
          '<ol>\n'
          '<li><b>Point your camera at the code</b> Open the built-in Camera app and point it '
          'at the QR code, keeping the whole square in frame.</li>\n'
          '<li><b>Tap the notification</b> A banner or link preview appears — tap it to open '
          'the destination.</li>\n'
          '<li><b>On iPhone, use the built-in shortcuts</b> Control Center QR scanner, or '
          'long-press the Camera icon. For a code inside a photo, long-press it in '
          'Photos.</li>\n'
          '<li><b>On Android, use Lens or Quick Settings</b> Google Lens in the camera or '
          'Google app, or the Scan QR code tile in Quick Settings. For a saved image, Google '
          'Photos + Lens.</li>\n'
          '<li><b>If nothing happens, fix the code, not the phone</b> Move closer, wipe the '
          'lens, and check the code itself: too small, low contrast, damaged, or printed on a '
          'curve.</li>\n'
          '<li><b>Check the preview before opening</b> Glance at the URL before tapping, '
          'especially on codes you find in public places.</li>\n'
          '</ol>\n'
          '<h2>On iPhone</h2>\n'
          '<p>Open the Camera app and point it at the code — hold steady for a second. A yellow '
          "notification appears; tap it. That's it. This works on any modern iPhone — "
          '<a href="https://support.apple.com/en-ca/102680">Apple\'s guide</a> covers the Camera '
          "app and Code Scanner.</p>\n"
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
          "characters, don't tap — <a "
          'href="https://consumer.ftc.gov/consumer-alerts/2023/12/scammers-hide-harmful-links-qr-codes-steal-your-information">stickers '
          'over real codes are a known scam the FTC has warned about</a>. Codes you generate '
          'yourself with <a href="/">FreeQrly</a> are static and contain exactly what you typed, '
          'nothing hidden.</p>\n',
  'date': '2026-10-14',
  'desc': 'How to scan a QR code on iPhone and Android — no app needed. Use the built-in camera, '
          "Control Center, or Google Lens, and fix it when it won't scan.",
  'faq': [('Do I need an app to scan QR codes?',
           'No. iPhones and virtually all Android phones scan QR codes with the built-in '
           'camera. Third-party scanner apps are unnecessary and often full of ads. '
           '<a href="https://support.apple.com/en-ca/102680">Apple\'s guide</a> covers the '
           'Camera app and Code Scanner on iPhone.'),
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
            ('On iPhone, use the built-in shortcuts',
             'Open Control Center and tap the QR scanner icon, or long-press the Camera icon. '
             'To scan a code inside a photo, open it in Photos and long-press the code.'),
            ('On Android, use Lens or Quick Settings',
             'Use Google Lens in the camera or Google app, or the Scan QR code tile in Quick '
             'Settings (Samsung). For a saved image, open it in Google Photos and tap the Lens '
             'button.'),
            ('If nothing happens, fix the code, not the phone',
             'Move closer, wipe the lens, and check the code itself: too small, low contrast, '
             'damaged, or printed on a curve. See the full troubleshooting checklist.'),
            ('Check the preview before opening',
             'Glance at the URL before tapping, especially on codes you find in public places '
             '— stickers over real codes are a known scam.')],
  'lede': 'No app required. Every modern iPhone and Android phone scans QR codes with the camera '
          "it already has. Here's how — plus what to do when nothing happens.",
  'mascot': 'scanner',
  'slug': 'how-to-scan-a-qr-code',
  'title': 'How to Scan a QR Code (iPhone & Android) | FreeQrly',
  'sources': [('https://support.apple.com/en-ca/102680', 'Apple Support: Scan a QR code with your iPhone or iPad', 'How to scan with the Camera app or Code Scanner.'),
              ('https://consumer.ftc.gov/consumer-alerts/2023/12/scammers-hide-harmful-links-qr-codes-steal-your-information', 'FTC: Scammers hide harmful links in QR codes', 'The FTC on QR codes covering real ones, spoofed sites, and checking the URL before opening.')]},
 {'body': '\n'
          "<h2>1. It's too small</h2>\n"
          "<p>The classic. A code squeezed into the corner of a business card at 1 cm wide won't "
          'scan reliably. Minimum for print, as a rule of thumb: <b>2x2 cm</b> (about 0.8 inches), and bigger is '
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
          'edges. Keep a clear border <a href="http://www.iso.org/standard/83389.html">at least '
          '4 modules wide</a> on all four sides, as specified in ISO/IEC 18004. Don\'t let '
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
           'Often yes, thanks to error correction — <a href="http://www.iso.org/standard/83389.html">up to 30% damage can be tolerated at the High setting</a>, as defined in ISO/IEC 18004. '
           'But heavy damage, fading, or missing finder patterns will kill it.'),
          ("My QR code scans but the link doesn't work — is the code broken?",
           'No, the code is doing its job. The destination is the problem: the page moved, the '
           'site is down, or a trial-based generator deactivated it.')],
  'h1': 'Why won’t this thing <span class="hl hl-blush">scan</span>?',
  'howto': [('Check the size',
             'As a rule of thumb, printed codes need to be at least 2x2 cm. On screen, make it '
             'at least 2 cm wide on your display.'),
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
  'mascot': 'error',
  'slug': 'why-is-my-qr-code-not-working',
  'title': 'QR Code Not Working? 7 Fixes That Help | FreeQrly',
  'sources': [('http://www.iso.org/standard/83389.html', 'ISO/IEC 18004:2024', 'The QR Code symbology specification. Defines the four error-correction levels (L 7%, M 15%, Q 25%, H 30%) and the 4-module quiet zone.')]},
 {'body': '\n'
          '<h2>The two rules that matter</h2>\n'
          '<p><b>Rule of thumb 1 — minimum size:</b> 2 x 2 cm (0.8 x 0.8 in). Below that, phone cameras '
          "can't resolve the modules reliably, especially codes holding a lot of data like "
          'vCards.</p>\n'
          "<p><b>Rule of thumb 2 — the 1:10 distance ratio:</b> the code's width should be at least "
          'one-tenth of the scanning distance. Scanning from 50 cm (a table card)? 5 cm code. From '
          '5 meters (a poster)? 50 cm code. Printers and signage folks use this ratio as a rule of thumb.</p>\n'
          '<h2>Cheat sheet by use case</h2>\n'
          '<p><b>Business cards:</b> 2x2 cm minimum — see the <a '
          'href="/business-card-qr-code/">business card generator</a>. Keep it clear of the card '
          'edge.<br> '
          "<b>Flyers &amp; menus:</b> 3x3 cm. People scan these at arm's length.<br> "
          '<b>Table tents:</b> 4–5 cm, so guests scan from their seats.<br> '
          '<b>Posters:</b> use the 1:10 ratio against expected viewing distance.<br> '
          '<b>Packaging:</b> 2x2 cm minimum, and avoid curved surfaces that distort the '
          'pattern.</p>\n'
          '<h2>Resolution: export big</h2>\n'
          '<p>Print needs 300 dpi. A 2 cm code at 300 dpi is only ~240 px — but always export '
          'larger and let the designer scale down: <b>PNG at 1024 or 2048 px</b>, or <b>SVG</b> '
          'which is infinitely scalable and the best choice for professional print. FreeQrly '
          'exports both, free.</p>\n'
          "<h2>Don't forget the quiet zone</h2>\n"
          '<p>Leave a blank margin around the code <a href="http://www.iso.org/standard/83389.html">at least 4 modules wide</a> on every side, as specified in ISO/IEC 18004. Crowding '
          'it with text or graphics is one of the top reasons codes fail — more in <a '
          'href="/blog/why-is-my-qr-code-not-working/">why your code won\'t scan</a>.</p>\n'
          '<h2>Logo in the middle? Go bigger</h2>\n'
          '<p>A <a href="/qr-code-with-logo/">logo in the center</a> eats into the pattern, so '
          "give it room: 3x3 cm minimum in print, and keep the logo under ~30% of the code's "
          'area as a rule of thumb.</p>\n',
  'date': '2026-10-14',
  'desc': 'How big should a QR code be in print? Minimum sizes for business cards, flyers, and '
          'posters — plus resolution and quiet-zone rules that keep codes scannable.',
  'faq': [('What is the minimum size for a printed QR code?',
           'As a rule of thumb, 2 x 2 cm (0.8 x 0.8 inches). Smaller codes fail on many phones, '
           'especially for data-heavy codes like vCards.'),
          ('How big should a QR code be on a poster?',
           'Use the 1:10 rule of thumb: the code width should be at least one-tenth of the '
           'expected scanning distance. A poster scanned from 5 meters needs a 50 cm code.'),
          ('PNG or SVG for print?',
           'SVG is best — it scales infinitely with no quality loss. If your printer needs raster, '
           'export PNG at 2048 px.')],
  'h1': 'How <span class="hl hl-mint">big</span> should a printed QR code be?',
  'lede': 'The short answer: at least 2x2 cm, at 300 dpi, with a clear margin. The longer answer — '
          'with the distance rule of thumb printers actually use — is below.',
  'mascot': 'batch',
  'slug': 'qr-code-print-size-guide',
  'title': 'QR Code Print Size Guide: How Big Should It Be? | FreeQrly',
  'sources': [('http://www.iso.org/standard/83389.html', 'ISO/IEC 18004:2024', 'The QR Code symbology specification. Defines the four error-correction levels (L 7%, M 15%, Q 25%, H 30%) and the 4-module quiet zone.')]},
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
          'guide with printable codes — no fees.',
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
  'mascot': 'faq',
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
          '<p>Many "free QR code generators" quietly create dynamic codes on a short trial. '
          'Your printed flyers work beautifully — until the trial ends and every code goes dead. '
          'Red flags: the site asks for your email before generating, mentions "scan analytics", '
          'or talks about "campaigns". A truly free static generator needs none of that.</p>\n'
          '<h2>The 30-second test</h2>\n'
          '<p>Before you trust a generator with your print run: generate a code <b>without '
          "creating an account</b>. If it works, it's static. Static codes from FreeQrly need no account, so there's nothing to expire. That's also why <a "
          'href="/blog/do-qr-codes-expire/">QR codes don\'t have to expire</a>.</p>\n'
          "<h2>What can still break (it's not the code)</h2>\n"
          '<p>A static code lasts forever, but its destination might not: if you delete the page '
          'it links to, the code "stops working". Link to stable URLs you control, and your codes '
          'will outlive most of your marketing materials.</p>\n'
          '<h2>Make yours</h2>\n'
          '<p>Pick any type in the <a href="/">free generator</a> — link, vCard, WiFi — download '
          'the PNG or SVG, and print it. No sign-up needed for a static code, no trial, no expiry date hiding in the fine '
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
  'mascot': 'privacy',
  'slug': 'free-qr-codes-that-dont-expire',
  'title': "Free QR Codes That Never Expire | FreeQrly"}]


POSTS += [{'body': '\n'
          '<h2>Why "no upload" matters</h2>\n'
          '<p>QR codes often contain sensitive things: WiFi passwords, event tickets, boarding '
          "passes, private links. Uploading that image to a stranger's server — just to read it — "
          "is a privacy trade most people don't realize they're making. FreeQrly's <a "
          'href="/scan/">QR scanner</a> decodes the image with JavaScript on your device (the '
          '<a href="https://github.com/cozmo/jsQR">open-source jsQR library</a>). The image never leaves the page.</p>\n'
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
           'It depends where the image goes. Many online scanners upload your image to their '
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
  'lede': "Many online QR scanners ask you to upload your image to their server. Ours doesn't — the "
          'code is decoded right in your browser. Camera or image upload, free forever.',
  'mascot': 'scanner',
  'slug': 'scan-qr-code-online',
  'title': 'Scan QR Codes Online — Free, No App, No Upload | FreeQrly',
  'sources': [('https://github.com/cozmo/jsQR', 'jsQR on GitHub', 'A pure JavaScript QR code reading library. Takes in raw images and locates, extracts and parses any QR code found within.')]},
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
  'mascot': 'scanner',
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
          'iPhone and Android. Print it on the invitation — one less step between the invite and the calendar may mean fewer no-shows.</p>\n'
          '<h2>3. The shared photo album</h2>\n'
          '<p>Every event has the same problem: the photos scatter across fifty phones. A code '
          'linking to a shared album (Google Photos, iCloud shared album) on table cards fixes it '
          '— guests upload their shots in one tap.</p>\n'
          '<h2>4. WiFi for the venue</h2>\n'
          '<p>Attendees will ask for WiFi. A <a href="/wifi-qr-code/">WiFi QR code</a> on signage '
          'connects them in one scan — no password spelling over loud music.</p>\n'
          '<h2>5. Feedback &amp; follow-up</h2>\n'
          '<p>A code linking to a 2-question feedback form on the exit signage or closing slide. '
          'Guests answer while the event is still fresh, instead of ignoring a follow-up email days later.</p>\n'
          '<h2>Printing tips</h2>\n'
          '<p>Event codes get scanned in chaotic lighting by hurried people: go bigger than you '
          'think (the <a href="/blog/qr-code-print-size-guide/">1:10 distance rule of thumb</a>), keep '
          'contrast high, and test on both iPhone and Android before printing a hundred table '
          "cards. Static codes never expire, so last year's signage template still works.</p>\n",
  'date': '2026-10-14',
  'desc': 'How to use QR codes for events: check-in, registration, tickets, photo sharing, and '
          'add-to-calendar codes. Free generator.',
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
  'mascot': 'wedding',
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
          'responses. Free generator.',
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
  'lede': 'Plenty of RSVPs arrive late because the reply card is sitting in a drawer. A QR code on '
          'the invitation — straight to your RSVP form — fixes the biggest wedding admin headache.',
  'mascot': 'wedding',
  'slug': 'wedding-rsvp-qr-code',
  'title': 'Wedding RSVP QR Codes: A Complete Guide | FreeQrly'}]


POSTS += [
 dict(
  slug="how-to-create-a-dynamic-qr-code",
  title="How to Create a Dynamic QR Code (Free & Editable) | FreeQrly",
  desc="Create a dynamic QR code for free: sign in, pick a type, style it, print it. Edit the destination later without reprinting. 8 free codes.",
  h1="How to create a <span class='hl hl-mint'>dynamic</span> QR code",
  lede="A dynamic QR code lets you change the destination after printing — and see how many people scanned. Here's how to make one, free, in about a minute.",
  date="October 16, 2026",
  datePublished="2026-10-16",
  mascot="faq",
  body="""
<p>Static codes are great — until the destination changes. The flyer is printed, the menu moved, the campaign URL wasn't final. A <strong>dynamic QR code</strong> fixes that: the printed pattern stays the same, but you can change where it points, any time, from your Dashboard. You also get scan counts, so you know whether anyone is actually scanning.</p>
<p>On FreeQrly, dynamic codes are free. Sign in (email, Google, or GitHub), and you get 8 of them. No trial, no card, no expiry games. Here's the whole process.</p>

<ol>
<li><b>Sign in — free.</b> Open the <a href="/login/">sign-in page</a> and create an account with email + password, Google, or GitHub. Static codes never need this; dynamic codes do, because the code has to belong to someone.</li>
<li><b>Switch to Dynamic.</b> In the <a href="/?mode=dynamic">studio</a>, flip the toggle from Static to Dynamic. Everything else — types, styling, download — works exactly the same.</li>
<li><b>Pick a type and fill it in.</b> Website, WiFi, contact, event — all 12 content types work as dynamic codes. (Batch stays static: one dynamic code per generation.)</li>
<li><b>Style it if you want.</b> Dots, colors, logo, frame — the preview updates live. The style is saved with the code, so the Dashboard and the download match.</li>
<li><b>Generate.</b> Hit Generate. You get a short link like <code>freeqrly.com/q/XXXXXXX</code> — that's what the QR pattern encodes. Print it, ship it, stick it on the wall.</li>
<li><b>Manage it later.</b> Your codes live in the <a href="/dashboard/">Dashboard</a>: edit, check stats, or delete one to free a slot.</li>
</ol>

<h2>What the QR code actually contains</h2>
<p>A dynamic code does not hold your link directly. It holds a short FreeQrly link, and our server redirects scanners to your destination. That's the mechanism that makes editing and counting possible — and it's why dynamic codes need an account while static ones don't. If a service ever tells you its "free" codes need an account, this is the mechanism at work; the difference here is that the account is free and the codes don't die.</p>

<h2>The limits, stated plainly</h2>
<ul>
<li><strong>8 codes, free.</strong> That's the free quota. Delete a code and the slot frees up.</li>
<li><strong>One at a time.</strong> Dynamic codes are generated one by one; batch generation stays static.</li>
<li><strong>Editing changes the destination, not the pattern.</strong> The printed code keeps working through every edit — which is the entire point.</li>
</ul>

<p>Not sure whether you need dynamic at all? <a href="/blog/static-vs-dynamic-qr-codes/">Static vs dynamic, explained honestly</a>. Already printed and need to fix a link? <a href="/blog/how-to-edit-a-qr-code-after-printing/">How to edit a QR code after printing</a>. Curious what the numbers look like? <a href="/blog/dynamic-qr-code-statistics/">What dynamic QR code statistics tell you</a>.</p>
""",
  howto=[
    ("Sign in — free",
     "Create a free account with email + password, Google, or GitHub. Static codes skip this; dynamic codes need an owner."),
    ("Switch to Dynamic",
     "In the studio, flip the Static/Dynamic toggle to Dynamic."),
    ("Pick a type and fill it in",
     "Website, WiFi, contact, event — all 12 content types work. Batch stays static."),
    ("Style it",
     "Dots, colors, logo, frame. The preview updates live and the style is saved with the code."),
    ("Generate",
     "Hit Generate. You get a short link like freeqrly.com/q/XXXXXXX — that's what the pattern encodes."),
    ("Manage it later",
     "Find your codes in the Dashboard: edit, check stats, or delete one to free a slot."),
  ],
  faq=[
    ("Is creating a dynamic QR code really free?",
     "Yes. Sign in free, create up to 8 dynamic codes, edit them, see stats. No trial period, no card, no subscription. Static codes remain free and unlimited with no account at all."),
    ("Do I need an account for a dynamic QR code?",
     "Yes — the code has to belong to someone so only you can edit it. Email + password, Google, or GitHub. Static codes never need an account."),
    ("How many dynamic QR codes can I have?",
     "8 on the free account. Delete a code to free its slot."),
    ("What does a dynamic QR code link to?",
     "A short FreeQrly link (freeqrly.com/q/XXXXXXX) that redirects to your destination. Scanners land on your page; the redirect is what makes editing and stats possible."),
  ],
  cta=dict(title="Make your first dynamic code",
           text="Free sign-in, 8 codes, editable after printing. Start in the studio.",
           href="/?mode=dynamic", btn="Create a dynamic code"),
 ),
 dict(
  slug="how-to-edit-a-qr-code-after-printing",
  title="How to Edit a QR Code After Printing | FreeQrly",
  desc="Printed the wrong link? Fix it without reprinting. Edit a dynamic QR code's destination, type, or style in the Dashboard — the printed code updates instantly.",
  h1="Edit a QR code <span class='hl hl-blush'>after printing</span>",
  lede="The flyers are already out — and the link is wrong. With a dynamic code, that's a two-minute fix, not a reprint.",
  date="October 16, 2026",
  datePublished="2026-10-16",
  mascot="error",
  body="""
<p>The flyers are already out — and the link is wrong. Or the menu moved. Or the campaign page wasn't final when the poster went to print. With a static code, that's a reprint. With a dynamic code, it's a two-minute fix.</p>
<p>The trick: a dynamic code's pattern never changes. It points at a short link on FreeQrly's server, and you control where that link sends people. Edit the destination, and every printed copy — already on walls, flyers, packaging — serves the new content instantly. No reprint, no stickers over the old code.</p>

<ol>
<li><b>Sign in.</b> Open the <a href="/login/">sign-in page</a> and log in to the account that owns the code.</li>
<li><b>Open the Dashboard.</b> Go to <a href="/dashboard/">your Dashboard</a>. Every dynamic code on your account is there as a card, with its QR thumbnail and scan count.</li>
<li><b>Open Edit.</b> On the code's card, click Edit. You'll see the same generator you used to create it — type, content, style, all of it.</li>
<li><b>Change what you need.</b> Destination, content, even the type: a Website code can become a WiFi code. Colors, logo, frame — all editable too.</li>
<li><b>Save.</b> Hit Save changes. Done. The printed code now serves the new content. Test it with your phone camera to be sure.</li>
</ol>

<h2>What you can change — and what you can't</h2>
<ul>
<li><strong>Destination and content:</strong> the link, the text, the WiFi password — anything the code carries.</li>
<li><strong>Type:</strong> switch a code from one content type to another. The pattern doesn't care; it only holds the short link.</li>
<li><strong>Style:</strong> colors, dots, logo, frame. The Dashboard thumbnail updates to match.</li>
<li><strong>What you can't change:</strong> the printed pattern itself — but you never need to, since the pattern only holds the short link. And you can't transfer a code to another account.</li>
</ul>

<h2>Two things worth knowing</h2>
<p><strong>Edits are instant and silent.</strong> There's no "republish" step and no delay — the next scan gets the new destination. If the old destination was a page you took down, fix the code first, then take the page down.</p>
<p><strong>Deleting is permanent.</strong> Delete a code and its printed copies stop working — there's no undo. Delete only when the code is truly retired; the slot frees up for a new code. (Still unsure whether dynamic is right for you? <a href="/blog/static-vs-dynamic-qr-codes/">Static vs dynamic, explained honestly</a>. Want the full creation walkthrough? <a href="/blog/how-to-create-a-dynamic-qr-code/">How to create a dynamic QR code</a>.)</p>
""",
  howto=[
    ("Sign in",
     "Log in to the account that owns the code."),
    ("Open the Dashboard",
     "Your codes are listed as cards with thumbnails and scan counts."),
    ("Open Edit",
     "On the code's card, click Edit — the full generator opens with your content prefilled."),
    ("Change what you need",
     "Destination, content, type, style — everything is editable."),
    ("Save",
     "Hit Save changes. The printed code serves the new content instantly — test it with your phone."),
  ],
  faq=[
    ("Do I need to reprint a QR code after editing it?",
     "No. The printed pattern holds a short link; editing changes where that link points. Every printed copy serves the new content immediately."),
    ("Can I change a dynamic QR code to a different type?",
     "Yes. In the Dashboard, open Edit and pick a new type — a Website code can become a WiFi code, for example. The printed pattern stays valid."),
    ("Does editing a QR code reset its scan statistics?",
     "No. Stats keep accumulating on the same code. Deleting a code removes it and its stats permanently."),
    ("What if I delete a dynamic QR code by mistake?",
     "There's no undo — printed copies stop working and the slot frees up. Only delete codes that are truly retired."),
  ],
  cta=dict(title="Fix a printed code",
           text="Sign in, open the Dashboard, edit, save. The printed code updates instantly.",
           href="/dashboard/", btn="Open the Dashboard"),
 ),
 dict(
  slug="dynamic-qr-code-statistics",
  title="Dynamic QR Code Statistics: What You Can Track | FreeQrly",
  desc="What dynamic QR code statistics tell you: total and unique scans, by day, country, city, device, and OS — and what FreeQrly never tracks.",
  h1="What dynamic QR <span class='hl hl-honey'>statistics</span> tell you",
  lede="A dynamic code reports home every time it's scanned. Here's what FreeQrly counts, how to read it, and what it never collects.",
  date="October 16, 2026",
  datePublished="2026-10-16",
  mascot="batch",
  body="""
<p>A static code is silent: it never reports home, so nobody — including you — knows how often it was scanned. A dynamic code reports every scan to your Dashboard. Here's what FreeQrly counts, how to read it, and what it deliberately never collects.</p>

<h2>The numbers on each card</h2>
<ul>
<li><strong>Total scans.</strong> Every scan of the code, all time.</li>
<li><strong>Today.</strong> Scans so far today.</li>
<li><strong>Unique scans.</strong> Distinct scanners, counted once per day. Two scans by the same person on the same day count as one unique scan.</li>
<li><strong>Last 7 days.</strong> A daily bar chart covering today and the previous six days — always seven bars, with zero-height bars for quiet days, so you can see gaps at a glance.</li>
</ul>

<h2>The breakdowns</h2>
<p>Open Stats on a code and you get four breakdowns, each with counts and percentages:</p>
<ul>
<li><strong>By country and by city.</strong> Where scans came from, from the scanner's approximate location.</li>
<li><strong>By device.</strong> Phone, tablet, or desktop.</li>
<li><strong>By OS.</strong> iOS, Android, and the rest.</li>
</ul>
<p>Use them the way a campaign would: a flyer in two neighborhoods shows which one pulls; a poster that gets desktop scans at noon is probably being scanned from a screenshot, not the wall.</p>

<h2>What FreeQrly never collects</h2>
<p>Stats are aggregates — there is no per-visitor record to look at. A "unique scan" is a one-way hash of the scanner's IP address, browser, and date: enough to count distinct scanners per day, impossible to reverse into a person. No names, no emails, no exact locations, no cross-code tracking of individuals. And static codes track nothing at all — they never touch a server, so there's nothing to count.</p>

<h2>Reading the numbers honestly</h2>
<ul>
<li><strong>Scans are not customers.</strong> A scan is a glance. Compare codes against each other, not against a fantasy benchmark.</li>
<li><strong>Zero is data.</strong> A code with no scans for a week is telling you the placement is wrong, not the code.</li>
<li><strong>Spikes need context.</strong> A burst of scans right after a post goes out is the post, not the poster. The 7-day chart makes this visible.</li>
</ul>

<p>Ready to try it? <a href="/blog/how-to-create-a-dynamic-qr-code/">Create your first dynamic code</a> — free sign-in, 8 codes — and check back after your first print run. Already printed and need a fix? <a href="/blog/how-to-edit-a-qr-code-after-printing/">How to edit a QR code after printing</a>.</p>
""",
  faq=[
    ("What counts as a unique scan?",
     "One scanner, once per day. FreeQrly counts distinct scanners using a one-way hash of IP address, browser, and date — the same person scanning twice in a day counts once."),
    ("Do static QR codes track scans?",
     "No. Static codes never touch a server — the destination lives in the pattern — so there's nothing to count. Only dynamic codes report scans."),
    ("Is visitor data private?",
     "Yes. Stats are aggregates only: counts by day, country, city, device, and OS. No names, emails, exact locations, or per-visitor records. Unique scans use a non-reversible hash."),
    ("Can I see who scanned my QR code?",
     "No — and that's by design. FreeQrly counts scans; it doesn't identify scanners."),
  ],
  cta=dict(title="Try it with your next print run",
           text="Create a free dynamic code and watch the stats come in.",
           href="/?mode=dynamic", btn="Create a dynamic code"),
 ),
]

REL_CSS = """<style>
.rel-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:10px}
.rel-card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 16px;text-decoration:none;color:inherit;display:block}
.rel-card:hover{border-color:var(--gold)}
.rel-card b{font-size:14px;font-weight:600;line-height:1.4}
@media(max-width:720px){.rel-grid{grid-template-columns:1fr}}
</style>"""
SOURCES_CSS = """<style>
.sources{margin-top:34px;padding:18px 20px;border:1px solid var(--line);border-radius:14px;background:var(--card)}
.sources h2{font-size:15px;margin:0 0 8px}
.sources ul{margin:0;padding-left:18px;font-size:13.5px;line-height:1.7;color:var(--soft)}
.sources a{color:inherit;text-decoration:underline}
</style>"""
POSTS += [
 dict(
  slug="qr-code-vs-barcode",
  title="QR Code vs Barcode: What's the Difference? | FreeQrly",
  desc="QR codes vs barcodes: what each holds, how much data fits, and when to use which. Barcodes for checkout, QR codes for everything else.",
  h1="QR code vs <span class='hl hl-mint'>barcode</span>",
  lede="Barcodes identify products at checkout. QR codes carry links, menus, WiFi passwords, contact cards. Same idea, very different jobs.",
  date="October 17, 2026",
  datePublished="2026-10-17",
  mascot="faq",
  body="""
<p>They look like cousins, but a barcode and a QR code solve different problems. A barcode is a row of vertical lines that encodes a short number — usually a product ID. A QR code is a square grid that encodes text, links, or whole contact cards. If you only remember one line: <strong>barcodes point at a database entry; QR codes carry the content itself.</strong></p>

<h2>The differences that matter</h2>
<table>
<tr><th></th><th>Barcode (1D)</th><th>QR code (2D)</th></tr>
<tr><td><strong>What it holds</strong></td><td>A short number (typically 8–13 digits)</td><td>Text, URLs, WiFi details, contacts — up to ~4,000 characters</td></tr>
<tr><td><strong>How it scans</strong></td><td>Laser scanners read it in one direction; needs to be aligned</td><td>Any phone camera, from any angle, in a fraction of a second</td></tr>
<tr><td><strong>Damage tolerance</strong></td><td>Low — a scratched line can kill it</td><td>High — error correction recovers up to 30% of a damaged code</td></tr>
<tr><td><strong>Needs a database?</strong></td><td>Yes — the number is useless without the lookup</td><td>No — the content lives inside the pattern</td></tr>
<tr><td><strong>Typical use</strong></td><td>Retail checkout, inventory, library books</td><td>Menus, tickets, payments, WiFi, marketing, contact cards</td></tr>
</table>

<h2>When a barcode is still the right call</h2>
<p>Retail checkout, warehouse inventory, and anything scanned by a dedicated laser scanner at close range. Barcodes are cheap to print, fast on laser hardware, and the whole retail world already speaks UPC/EAN. If your workflow is "scan a product, look up its record," a barcode is the tool.</p>

<h2>When a QR code wins</h2>
<p>Anything a <em>person</em> scans with a phone: menus, tickets, payment links, WiFi join codes, contact cards, product pages, feedback forms. QR codes hold far more, survive damage, and need no special hardware. They can also carry a product link — a QR code on packaging that opens the manual, the warranty page, or the reorder page is a barcode's job done better.</p>

<h2>Can a QR code replace a barcode on products?</h2>
<p>For consumer-facing uses, yes — and retail is moving that way with GS1 Digital Link, which puts a QR code on pack that carries the same product identity a barcode does, plus a link to web content. For checkout lanes with laser-only scanners, barcodes stay for now: laser scanners cannot read 2D codes. The practical rule: barcode where laser scanners rule, QR code everywhere a phone is involved.</p>

<p>Want the QR side? <a href="/#studio">Make a QR code</a> — free, no sign-up for static codes. Curious about the editable kind? <a href="/blog/static-vs-dynamic-qr-codes/">Static vs dynamic, explained honestly</a>.</p>

<p>Need a barcode instead? <a href="/barcode-generator/">Make a barcode</a> — free, no sign-up.</p>
""",
  faq=[
    ("Can a QR code hold the same number as a barcode?",
     "Yes — a QR code can encode any barcode's number (UPC, EAN, Code 128) as plain text. But a phone scanning it will show the number, not look it up, unless the code points at a page that does the lookup."),
    ("Why do barcodes still exist if QR codes hold more?",
     "Legacy hardware. Millions of checkout lanes and warehouses run laser scanners that read only 1D barcodes. Until that hardware turns over, barcodes stay for checkout — QR codes take everything else."),
    ("Which is better for a product label?",
     "For checkout: a barcode (or both). For customers: a QR code linking to the manual, warranty, or reorder page. Many brands now print both on the same pack."),
    ("Do QR codes expire while barcodes don't?",
     "Neither expires on its own. A static QR code works as long as its destination exists — same as a barcode's number staying valid. Only dynamic codes can stop working, if the service behind them shuts down."),
  ],
  cta=dict(title="Make a QR code",
           text="Barcodes for checkout, QR codes for everything else. Make yours free.",
           href="/#studio", btn="Open the studio"),
 ),
 dict(
  slug="make-qr-code-in-canva-excel-word",
  title="How to Make a QR Code in Canva, Excel & Word | FreeQrly",
  desc="No built-in QR tool in Canva, Excel, or Word? Make the code in FreeQrly (free, no sign-up), download PNG, and drop it into your design or document.",
  h1="QR codes in <span class='hl hl-honey'>Canva, Excel & Word</span>",
  lede="None of these apps has a good built-in QR maker. The fast route: generate the code in FreeQrly, download a PNG, and drop it in. Two minutes, every time.",
  date="October 17, 2026",
  datePublished="2026-10-17",
  mascot="batch",
  body="""
<p>Canva has a QR app buried in its marketplace. Excel has none. Word has none. Google Docs and Sheets have none either. Every one of them, though, lets you insert an image — and a QR code is just an image. So the reliable workflow is the same everywhere: <strong>make the code in a real generator, download a PNG, insert it.</strong></p>

<h2>The workflow (works in all four)</h2>
<ol>
<li><b>Make the code.</b> In the <a href="/#studio">FreeQrly studio</a>, pick the type (Website for a link, WiFi for a network, vCard for a contact), fill it in, style it if you want.</li>
<li><b>Download PNG.</b> Use the PNG download at 1024 px or higher. PNG keeps the edges crisp in print and on screen; SVG is better if your app accepts it (Word and Docs do not, Canva does).</li>
<li><b>Insert it.</b> Canva: Uploads → Upload files. Excel: Insert → Pictures. Word: Insert → Pictures. Google Docs/Sheets: Insert → Image → Upload from computer.</li>
<li><b>Test it.</b> Point your phone camera at the screen (or a test print). If it scans on the first try, ship it.</li>
</ol>

<h2>Canva</h2>
<p>Canva's own QR app works, but it locks the style and the code lives inside Canva. A FreeQrly PNG gives you full control — logo, colors, frame — and the same file works in your flyer, your Instagram post, and your PDF export. Upload once, reuse everywhere. Size it to at least 2 × 2 cm on the final design so phones read it at arm's length.</p>

<h2>Excel</h2>
<p>Excel has no QR function. The IMAGE function (newer Excel) can display a QR code from a URL, but it needs the image hosted somewhere and breaks in older versions and in print. A pasted PNG is the dependable route: it prints, it survives file sharing, and it works in every Excel version. Place it in a cell corner or floating over the sheet — either way, keep the quiet margin around it clear.</p>

<h2>Word</h2>
<p>Word has no QR tool either. Insert → Pictures, then set text wrapping to Square or Tight so the paragraph flows around it. For letterheads and invoices, pin the code to a fixed spot (a header, a footer, or a text box) so it lands in the same place on every page. For print, export the document as PDF — the code stays sharp.</p>

<h2>Google Docs & Sheets</h2>
<p>Same pattern: Insert → Image → Upload from computer. In Docs, use "Wrap text" so the code sits beside the paragraph. In Sheets, float it over a corner cell range. One extra tip: Docs compresses large images on export, so start from a 1024 px PNG and keep the code at a reasonable size — a tiny code on a big page is the most common reason scans fail.</p>

<h2>Three mistakes that break scans</h2>
<ul>
<li><strong>Too small.</strong> Under 2 × 2 cm on print, or under ~150 px on screen, phones struggle. When in doubt, go bigger.</li>
<li><strong>Low contrast.</strong> Fancy colors look great and fail quietly. Dark code on a light background, always. See the <a href="/blog/qr-code-print-size-guide/">print size guide</a> for the distance rule.</li>
<li><strong>Stretching.</strong> Dragging a corner distorts the grid. Resize proportionally (hold Shift in most apps) so the squares stay square.</li>
</ul>
""",
  howto=[
    ("Make the code",
     "In the FreeQrly studio, pick the type, fill it in, style it if you want."),
    ("Download PNG",
     "PNG at 1024 px or higher. SVG if your app accepts it; Word and Docs do not."),
    ("Insert it",
     "Canva: Uploads. Excel/Word: Insert → Pictures. Docs/Sheets: Insert → Image."),
    ("Test it",
     "Scan with your phone camera. If it reads on the first try, ship it."),
  ],
  faq=[
    ("Does Canva have a built-in QR code generator?",
     "Canva has a QR app in its marketplace, but it locks the style and keeps the code inside Canva. A FreeQrly PNG gives you full control and works everywhere."),
    ("Can Excel generate QR codes natively?",
     "No. Excel has no QR function. Paste a PNG — it prints, survives file sharing, and works in every version."),
    ("PNG or SVG for Word and Docs?",
     "PNG. Word and Google Docs handle PNG images natively; SVG support is inconsistent. Export at 1024 px or higher for print."),
    ("Will the code stay sharp when I export to PDF?",
     "Yes, if you start from a 1024 px PNG and don't shrink it tiny. Test-scan the exported PDF before sending it out."),
  ],
  cta=dict(title="Make your QR code",
           text="Free, no sign-up for static codes. PNG and SVG export.",
           href="/#studio", btn="Open the studio"),
 ),
]

POSTS += [
 dict(
  slug="best-free-qr-code-generators",
  title="Best Free QR Code Generators in 2026 | FreeQrly",
  desc="5 free QR code generators compared: FreeQrly, QRCode Monkey, QR Tiger, QR Code Generator, ME-QR. Free tiers, watermarks, limits, and who each fits.",
  h1="The best free QR code generators, <span class='hl hl-mint'>compared honestly</span>",
  lede="Every generator calls itself free. The difference is what free actually includes — static codes, editable codes, watermarks, batch, and what happens when you hit the limit.",
  date="October 17, 2026",
  datePublished="2026-10-17",
  mascot="faq",
  body="""
<p>"Free" in QR generators means at least three different things: free static codes (the code itself, forever), a few free dynamic codes (editable, with stats), and a free trial that ends. The right pick depends on which one you actually need. Here is how the five best-known free options compare — including this site, with its limits stated plainly.</p>

<h2>The comparison</h2>
<table>
<tr><th></th><th>FreeQrly</th><th>QRCode Monkey</th><th>QR Tiger</th><th>QR Code Generator</th><th>ME-QR</th></tr>
<tr><td><strong>Free static codes</strong></td><td>Unlimited, no sign-up</td><td>Free, with logo / SVG / PDF / EPS</td><td>Free tool</td><td>Free tool</td><td>Free tool</td></tr>
<tr><td><strong>Free dynamic codes</strong></td><td>8 free, with scan stats</td><td>Paid (via Bitly)</td><td>3 free</td><td>Paid plans</td><td>Free dynamic codes</td></tr>
<tr><td><strong>Batch generation</strong></td><td>50 per batch, static</td><td>Not stated</td><td>Up to 3,000 per batch</td><td>Not stated</td><td>500–2,000 per batch</td></tr>
<tr><td><strong>Type range</strong></td><td>12 types + batch</td><td>Core types</td><td>20–24 solutions</td><td>~37 types</td><td>52 types</td></tr>
<tr><td><strong>Best for</strong></td><td>Free dynamic codes + privacy</td><td>Simple free static codes</td><td>Bulk + enterprise features</td><td>Longest track record (since 2009)</td><td>Widest type range</td></tr>
</table>
<p><small>Limits and prices change — check each site before you commit. Figures from public pages and comparisons, October 2026.</small></p>

<h2>What "free" actually means</h2>
<p>A <strong>static</strong> code carries its content inside the pattern. It costs the provider nothing to serve, so genuinely free static codes — no watermark, no expiry — are the norm, and you should never pay for one. A <strong>dynamic</strong> code points at a short link on the provider's server, which is what makes editing and stats possible — and what costs them money. That is why dynamic codes are where the free tiers end. If a tool's "free" plan gives you dynamic codes, read the number: 3, 8, or unlimited changes everything. <a href="/blog/static-vs-dynamic-qr-codes/">Static vs dynamic, explained honestly</a>.</p>

<h2>The 5 questions to ask before you pick</h2>
<ol>
<li><b>Watermark?</b> Some free tiers stamp their logo on your code. If your code goes on packaging, that matters.</li>
<li><b>Expiry?</b> Static codes should never expire. If a "free" code stops working, it was dynamic on a trial.</li>
<li><b>Edit after printing?</b> Only dynamic codes allow it. If your link might change, you need dynamic — <a href="/blog/how-to-edit-a-qr-code-after-printing/">here is how editing works</a>.</li>
<li><b>Stats?</b> Only dynamic codes count scans. Static codes are private by design — nobody, including the provider, sees them.</li>
<li><b>Privacy?</b> Static codes made in your browser never leave your device. Dynamic codes live on a server by definition. Pick the model that matches the data.</li>
</ol>

<h2>The verdict</h2>
<ul>
<li><strong>Need free dynamic codes with stats?</strong> FreeQrly: 8 free, editable after printing, scan stats included.</li>
<li><strong>Need bulk or enterprise features?</strong> QR Tiger: up to 3,000 codes per batch, CRM integrations, white-label.</li>
<li><strong>Just want a quick free static code?</strong> QRCode Monkey is the classic — simple, free, no fuss.</li>
<li><strong>Want the widest type range?</strong> ME-QR lists 52 types.</li>
<li><strong>Want the longest-running brand?</strong> QR Code Generator (Egoditor, since 2009, now part of Bitly).</li>
</ul>

<p>Whatever you pick, test it: generate one code, print it at the size you will actually use, and scan it with your phone. A generator is only as good as its codes on paper. <a href="/#studio">Make a QR code</a> — free, no sign-up for static codes.</p>
""",
  faq=[
    ("Is FreeQrly really free?",
     "Yes. Static codes are free and unlimited with no account. Dynamic codes are free too: sign in and you get 8 editable codes with scan stats. No trial, no card, no expiry games."),
    ("Which QR code generator is best for beginners?",
     "Any of the five above will make a working code. Pick by what you need next: free dynamic editing (FreeQrly), bulk (QR Tiger), widest type range (ME-QR), or the simplest possible static code (QRCode Monkey)."),
    ("Do free QR codes expire?",
     "Static codes never expire — the content lives inside the pattern. Dynamic codes can stop working if the provider shuts down or the free tier ends, which is why the provider's longevity matters for dynamic codes."),
    ("Can I edit a free QR code after printing?",
     "Only if it is dynamic. Static codes are frozen at print time; dynamic codes point at a short link you control, so you can change the destination without reprinting."),
  ],
  cta=dict(title="Compare for yourself",
           text="Make a code in the studio — free, no sign-up for static codes.",
           href="/#studio", btn="Open the studio"),
 ),
 dict(
  slug="why-is-my-qr-code-blurry",
  title="Why Is My QR Code Blurry? Fixes That Work | FreeQrly",
  desc="Blurry QR code won't scan? The 5 usual causes: low-res export, wrong size, JPEG compression, stretching, and bad print. How to fix each.",
  h1="Why is my QR code <span class='hl hl-blush'>blurry</span>?",
  lede="A blurry QR code is almost always a resolution problem: too few pixels stretched across too much space. The fix is to export bigger — or as SVG.",
  date="October 17, 2026",
  datePublished="2026-10-17",
  mascot="error",
  body="""
<p>A QR code looks sharp on screen and turns to mush on paper. The cause is nearly always the same: the image did not have enough pixels for the size it was printed at. A QR code is a grid of tiny squares — when there are not enough pixels, the edges smear, phones cannot find the grid, and scans fail.</p>

<h2>The 5 usual causes</h2>
<ol>
<li><b>Low-resolution export.</b> A 512 px PNG looks fine at 2 cm wide. Blown up to a 20 cm poster, each module becomes a smudge. The bigger the print, the more pixels you need.</li>
<li><b>JPEG compression.</b> JPEG smears sharp edges — exactly what a QR code is made of. A code saved as a low-quality JPEG can fail even at small sizes. PNG or SVG only.</li>
<li><b>Stretching.</b> Dragging a corner of the image distorts the grid: squares become rectangles, and scanners give up. Always resize proportionally.</li>
<li><b>Bad print.</b> Low-DPI printers, ink bleed on rough or absorbent paper, and glossy glare all soften edges. Matte paper and a laser printer beat an inkjet on a napkin.</li>
<li><b>Copy of a copy.</b> Screenshotting a code from a message, then screenshotting that screenshot, loses resolution each time. Always go back to the original export.</li>
</ol>

<h2>How to fix it</h2>
<ul>
<li><strong>Export bigger.</strong> PNG at 1024 px for cards and flyers, 2048 px for posters. Rule of thumb: the print size in cm, times ~100, is the pixels you want.</li>
<li><strong>Use SVG for print.</strong> SVG is vector — infinitely scalable with zero blur. Use it whenever the printer or designer accepts it.</li>
<li><strong>Keep proportions.</strong> Hold Shift (or the lock icon) when resizing so the squares stay square.</li>
<li><strong>Test at final size.</strong> Print one copy at the real size, step back to the real viewing distance, and scan it with your phone. If it reads first try, the batch is safe.</li>
</ul>

<p>Still not scanning after a sharp reprint? The problem is something else — size, contrast, or damage. <a href="/blog/why-is-my-qr-code-not-working/">The full troubleshooting guide</a> covers those. For the size-vs-distance rule, see the <a href="/blog/qr-code-print-size-guide/">print size guide</a>.</p>
""",
  howto=[
    ("Export at the right size",
     "PNG at 1024 px for cards and flyers, 2048 px for posters. SVG whenever the printer accepts it."),
    ("Use PNG or SVG, never JPEG",
     "JPEG smears the sharp edges a QR code is made of. PNG for screens and office printing, SVG for professional print."),
    ("Keep proportions when resizing",
     "Hold Shift or the lock icon so the squares stay square. Never drag one corner freehand."),
    ("Test-scan the real print",
     "Print one copy at final size, step back to the real viewing distance, scan with your phone. First-try scan means the batch is safe."),
  ],
  faq=[
    ("Why does my QR code look blurry but still scan?",
     "Phones are forgiving — error correction recovers a surprising amount of blur. But a code that scans in your bright office may fail in dim light or at arm's length. Sharp is safe; barely-scanning is not."),
    ("What resolution do I need for a poster?",
     "2048 px PNG minimum, or SVG. A poster viewed from 2 meters needs far more pixels than a business card viewed from 30 cm — see the print size guide for the distance rule."),
    ("PNG or SVG for print?",
     "SVG whenever the printer or designer accepts it — it scales infinitely with zero blur. PNG at 1024–2048 px is the fallback for office printing and apps that don't take SVG."),
    ("Can I fix a blurry printed code without reprinting?",
     "No. The blur is baked into the printed image. Reprint from a higher-resolution export (or SVG). Editing a dynamic code won't help — the pattern on paper is what it is."),
  ],
  cta=dict(title="Make a sharp code",
           text="Export PNG up to 2048 px or infinitely scalable SVG. Free, no sign-up for static codes.",
           href="/#studio", btn="Open the studio"),
 ),
 dict(
  slug="how-to-scan-qr-code-on-phone",
  title="How to Scan a QR Code on Your Phone (iPhone & Android) | FreeQrly",
  desc="How to scan a QR code on your phone: iPhone Camera and Control Center, Android camera and Google Lens. No extra app needed, plus fixes when it won't scan.",
  h1="How to scan a QR code <span class='hl hl-mint'>on your phone</span>",
  lede="No app to install — your phone already knows how. Here's where the scanner lives on iPhone and Android, and what to do when it won't read.",
  date="October 19, 2026",
  datePublished="2026-10-19",
  mascot="scanner",
  body="""
<p>Almost every "how do I scan this" question has the same answer: <strong>open your camera and point it at the code</strong>. Modern phones read QR codes natively — the scanner is built into the camera app, not a separate download. The exact spot differs slightly between iPhone and Android.</p>

<h2>On iPhone</h2>
<p><strong>Method 1 — the Camera app.</strong> Open Camera, point it at the code, and hold still for a second. A yellow notification banner appears at the top — tap it to open the link. That's it; there is nothing to enable first.</p>
<p><strong>Method 2 — Control Center.</strong> Swipe down from the top-right corner, tap the QR code icon (a small code symbol). If you don't see it, go to Settings → Control Center and add "Code Scanner." This opens a dedicated scanner view, handy in low light.</p>

<h2>On Android</h2>
<p><strong>Method 1 — the Camera app.</strong> On most Android phones (Samsung, Pixel, and others), open the camera and point it at the code. A link popup appears — tap it. If nothing happens, check the camera settings for a "Scan QR codes" toggle and switch it on.</p>
<p><strong>Method 2 — Google Lens.</strong> Open the Google app or Google Lens, point at the code, and tap the shutter button. Lens reads the code and shows the link. Some phones also have a QR tile in Quick Settings (swipe down twice from the top).</p>

<h2>When it won't scan</h2>
<p>Nine times out of ten it's one of these:</p>
<ul>
<li><strong>Too far or too close.</strong> Fill about half the viewfinder with the code, then hold still.</li>
<li><strong>Glare or shadow.</strong> Tilt the phone slightly so reflections move off the code.</li>
<li><strong>Dirty or damaged print.</strong> A smudged code may still scan — QR codes tolerate <a href="http://www.iso.org/standard/83389.html">up to 30% damage</a> at the highest error-correction level — but a torn finder pattern (the three big squares) is fatal.</li>
<li><strong>It's not a QR code.</strong> Some "codes" on packaging are barcodes or proprietary marks. A QR code always has three square positioning marks in the corners.</li>
</ul>

<h2>Do you need a scanner app?</h2>
<p>No — and that's the honest answer even though scanner apps exist. The built-in camera handles standard QR codes, and third-party scanner apps mostly add ads and tracking. The one exception: if your phone is old enough to lack a built-in reader, any reputable scanner app will do the job.</p>

<p>Want to test right now? Point your camera at any code on <a href="/scan/">our free scanner page</a> — or upload a photo of a code and decode it in your browser, nothing uploaded.</p>
""",
  faq=[
    ("How do I scan a QR code on my iPhone?",
     "Open the Camera app and point it at the code — a notification banner appears at the top. Tap it. Alternatively, add the Code Scanner to Control Center (Settings → Control Center) for a dedicated scanner."),
    ("How do I scan a QR code on Android?",
     "Open your camera app and point it at the code; a link popup appears. If that doesn't work, enable 'Scan QR codes' in camera settings, or use Google Lens."),
    ("Do I need to download a QR scanner app?",
     "No. iPhones and most Android phones read QR codes with the built-in camera. Scanner apps are unnecessary for standard codes."),
    ("Why won't my phone scan the QR code?",
     "Usually distance, glare, or a damaged print. Hold the phone so the code fills half the viewfinder, avoid reflections, and check the three corner squares aren't torn."),
  ],
  sources=[("http://www.iso.org/standard/83389.html", "ISO/IEC 18004:2024", "The QR Code symbology specification. Defines the four error-correction levels (L 7%, M 15%, Q 25%, H 30%).")],
  cta=dict(title="Try a scan right now",
           text="Point your phone at any QR code — or decode one from a photo, free, in your browser.",
           href="/scan/", btn="Open the scanner"),
 ),
 dict(
  slug="get-google-reviews-with-qr-code",
  title="How to Get More Google Reviews with a QR Code | FreeQrly",
  desc="More Google reviews with a QR code: find your review link, generate a free review QR code, and place it where customers actually scan — receipt, table, checkout.",
  h1="Get more Google reviews with <span class='hl hl-blush'>a QR code</span>",
  lede="The best time to ask for a review is the moment a happy customer is standing in front of you. A QR code makes that moment one scan long.",
  date="October 19, 2026",
  datePublished="2026-10-19",
  mascot="success",
  body="""
<p>Google reviews decide who gets picked — and the businesses with the most reviews didn't get them by luck. They asked, at the right moment, with zero friction. A QR code pointing straight at your Google review form turns "please leave us a review" into a single scan.</p>

<h2>Step 1 — get your Google review link</h2>
<p>You need the direct link to your review form, not just your business listing:</p>
<ol>
<li>Go to your <a href="https://www.google.com/business/">Google Business Profile</a> and sign in.</li>
<li>Open the "Reviews" section and look for "Get more reviews" — Google gives you a short shareable link (it looks like <code>https://g.page/your-business/review</code>).</li>
<li>Copy it. That's the link your QR code will hold.</li>
</ol>

<h2>Step 2 — turn it into a QR code</h2>
<p>Paste the link into a <a href="/google-review-qr-code/">Google review QR code generator</a> — it takes seconds, it's free, and the static code never expires. Print it at a decent size: business-card codes get ignored, but a 5 cm code on a table tent gets scanned. Keep dark ink on a light background with a clear quiet margin around the code.</p>

<h2>Step 3 — put it where the moment happens</h2>
<p>Placement is the whole game. The code has to be in front of a happy customer <em>before</em> they leave:</p>
<ul>
<li><strong>Restaurants & cafés:</strong> table tents and the receipt. "Enjoyed your meal? One scan." beats a follow-up email nobody opens.</li>
<li><strong>Retail & salons:</strong> the checkout counter, right where they pay — satisfaction peaks at purchase.</li>
<li><strong>Services (plumbers, tutors, clinics):</strong> a card handed over at the end of the visit, or a sticker on the invoice.</li>
<li><strong>Delivery & takeaway:</strong> a sticker on the bag or box. The food is the reminder.</li>
</ul>

<h2>What to write next to it</h2>
<p>A bare code gets fewer scans than a code with a reason. Keep it short and specific: "Love your visit? Scan to review us on Google — 30 seconds." Asking for <em>Google</em> reviews by name matters — customers default to whichever platform is easiest, and you want them on the one future customers check.</p>

<h2>A few honest tips</h2>
<ul>
<li><strong>Ask, don't beg.</strong> One visible code plus a spoken "we'd love a review" outperforms five signs.</li>
<li><strong>Never pay for reviews or offer rewards for them</strong> — it violates Google's policies and the reviews get removed anyway.</li>
<li><strong>Reply to reviews.</strong> A business that answers reviews gets more of them; reviewers can see you read them.</li>
<li><strong>Track what works.</strong> If you want to know which placement drives scans, use a dynamic code for one location and compare — but for most shops, one static code that never expires is all you need.</li>
</ul>
""",
  faq=[
    ("How do I create a QR code for Google reviews?",
     "Copy your Google review link from your Google Business Profile (Reviews → Get more reviews), paste it into a free QR code generator, and print the code. Static codes are free and never expire."),
    ("Where should I put my Google review QR code?",
     "Wherever a satisfied customer stands before leaving: restaurant tables and receipts, retail checkout counters, service invoices, or delivery packaging."),
    ("Do Google review QR codes expire?",
     "A static QR code never expires — it holds your review link directly. As long as your Google Business Profile exists, the code keeps working."),
    ("Should I offer a discount for a Google review?",
     "No. Google prohibits incentivized reviews and removes them. Ask at the right moment instead — that's what the QR code is for."),
  ],
  cta=dict(title="Make your review QR code",
           text="Paste your Google review link, get a printable code in seconds. Free, no sign-up for static codes.",
           href="/google-review-qr-code/", btn="Create review code"),
 ),
]

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

    sources_html = ""
    if p.get("sources"):
        items = "\n".join(
            '      <li><a href="%s">%s</a> - %s</li>' % (u, label, note)
            for u, label, note in p["sources"])
        sources_html = ('\n    <section class="sources">\n      <h2>Sources</h2>\n      <ul>\n'
                        + items + '\n      </ul>\n    </section>\n')
    faq_html = "\n".join(
        '    <details><summary><span>%s</span></summary><p>%s</p></details>' % (q, a)
        for q, a in p["faq"])
    cta = p.get('cta') or {'title': 'Try it yourself — free', 'text': 'Everything in this article works in the FreeQrly studio right now. Static codes, thirteen content types, PNG and SVG export.', 'href': '/#studio', 'btn': 'Open the studio'}
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="zh" href="https://freeqrly.com/zh/blog/{p['slug']}/">
<link rel="alternate" hreflang="es" href="https://freeqrly.com/es/blog/{p['slug']}/">
<link rel="alternate" hreflang="hi" href="https://freeqrly.com/hi/blog/{p['slug']}/">
<link rel="alternate" hreflang="ar" href="https://freeqrly.com/ar/blog/{p['slug']}/">
<link rel="alternate" hreflang="pt" href="https://freeqrly.com/pt/blog/{p['slug']}/">
<link rel="alternate" hreflang="fr" href="https://freeqrly.com/fr/blog/{p['slug']}/">
<link rel="alternate" hreflang="ru" href="https://freeqrly.com/ru/blog/{p['slug']}/">
<link rel="alternate" hreflang="de" href="https://freeqrly.com/de/blog/{p['slug']}/">
<link rel="alternate" hreflang="ja" href="https://freeqrly.com/ja/blog/{p['slug']}/">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta name="theme-color" content="#FAF5EA">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://freeqrly.com/og.png">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="zh_CN">
<meta property="og:locale:alternate" content="es_ES">
<meta property="og:locale:alternate" content="hi_IN">
<meta property="og:locale:alternate" content="ar_AR">
<meta property="og:locale:alternate" content="pt_BR">
<meta property="og:locale:alternate" content="fr_FR">
<meta property="og:locale:alternate" content="ru_RU">
<meta property="og:locale:alternate" content="de_DE">
<meta property="og:locale:alternate" content="ja_JP">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="../../assets/img/favicon-scanner.png">
<link rel="apple-touch-icon" href="../../assets/img/favicon-scanner.png">
<link rel="stylesheet" href="../../assets/css/main.css?v=b3r-20261020">
<link rel="stylesheet" href="/assets/css/site-header.css?v=b3r-20261020">
<link rel="stylesheet" href="/assets/css/acct-menu.css?v=b3r-20261020">
{REL_CSS}{SOURCES_CSS if p.get("sources") else ""}
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{p["title"]}","description":"{p["desc"]}","speakable":{{"@type":"SpeakableSpecification","cssSelector":["h1",".lede"]}},"datePublished":"{p.get('datePublished','2026-10-13')}","author":{{"@type":"Organization","name":"FreeQrly"}},"publisher":{{"@type":"Organization","name":"FreeQrly"}}}}
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
    <div class="mascot m-blog" aria-hidden="true"><img decoding="async" width="512" height="512" src="/assets/img/mascots/{p["mascot"]}.webp" alt="Qly the FreeQrly elephant mascot"></div>
    <div class="kicker" style="text-align:center">Field notes</div>
    <h1 style="text-align:center;max-width:640px;margin:0 auto">{p["h1"]}</h1>
    <p class="lede" style="text-align:center;margin-left:auto;margin-right:auto">{p["lede"]}</p>
    <p class="meta" style="text-align:center">{p["date"]} · 4 min read</p>
    <div class="prose" style="margin-top:40px">
{p["body"]}
    </div>
{sources_html}    <div class="cta-card">
      <div class="mascot" aria-hidden="true"><img loading="lazy" decoding="async" width="512" height="512" src="/assets/img/mascots/studio-qr.webp" alt="Qly presenting a QR code"></div>
      <div>
        <h3>{cta['title']}</h3>
        <p>{cta['text']}</p>
        <a class="btn" href="{cta['href']}">{cta['btn']}</a>
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
    <div class="fcta">
      <img loading="lazy" decoding="async" width="160" height="160" src="/assets/img/mascots/scanner.webp" alt="">
      <div class="fctaText">
        <h3>Unlimited dynamic codes — limited-time offer.</h3>
        <p>Sign in free and create as many as you need. Every code stays editable after printing and never expires.</p>
      </div>
      <a class="fctaBtn" href="/login/">Start free</a>
    </div>
    <div class="fmain">
      <div class="fbrand">
        <a class="fbrandName" href="/" style="text-decoration:none">Free<em>Qrly</em></a>
        <p class="ftag">Beautiful QR codes, made in your browser. Static codes never expire.</p>
        <div class="fmade">Made quietly — static codes in your browser.</div>
      </div>
      <div class="fcol"><h4>Product</h4><a href="/">QR Generator</a><a href="/batch-qr-code/">Batch QR Codes</a><a href="/qr-code-with-logo/">QR Code with Logo</a><a href="/scan/">QR Scanner</a><a href="/barcode-generator/">Barcode Generator</a></div>
      <div class="fcol"><h4>Resources</h4><a href="/blog/">Blog</a><a href="/developers/">Developers · API &amp; MCP</a><a href="/blog/qr-code-print-size-guide/">Print Size Guide</a><a href="/#faq">FAQ</a></div>
      <div class="fcol"><h4>Company</h4><a href="/about/">About</a><a href="mailto:hello@freeqrly.com">Contact</a></div>
      <div class="fcol"><h4>Legal</h4><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Service</a></div>
    </div>
    <div class="fbottom"><span>© 2026 FreeQrly</span><a href="mailto:hello@freeqrly.com">hello@freeqrly.com</a></div>
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
