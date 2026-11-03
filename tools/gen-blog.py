#!/usr/bin/env python3
"""Generate the 2 SEO blog posts for FreeQrly."""
import os

SITE = os.path.dirname(os.path.abspath(__file__)) + "/.."

HEADER = '''<div id="siteHeader"></div>
<script src="/assets/js/site-header.js?v=b3y-20261102"></script>
<script src="/assets/js/acct-menu.js?v=b3y-20261102"></script>
<script src="/assets/js/subpage-header.js?v=b3y-20261102"></script>'''

THEME_JS = ''

POSTS = [
 dict(
  slug="do-qr-codes-expire",
  cta=dict(title="Try it yourself — free", text="Everything in this article works in the FreeQrly studio right now. Static codes, all 17 content types, PNG and SVG export.", href="/#studio", btn="Open the studio"),
  title="Do QR Codes Expire? No — But Paid Ones Can Die | FreeQrly",
  desc="Do QR codes expire? Static codes never expire — the pattern holds your link forever. What actually stops working is paid dynamic codes when the subscription ends.",
  h1="Do QR codes <span class='hl hl-mint'>expire</span>?",
  lede="Short answer: no — at least, not the kind you make here. The longer answer is worth knowing before you print a thousand of them.",
  date="October 13, 2026", updated="November 3, 2026", dateModified="2026-11-03",
  mascot="privacy",
  body="""<p>Short answer: no — at least, not the kind you make here. A static QR code cannot expire, because there is no clock inside those little squares. A static code is just your link, drawn as a pattern. As long as the link works, the code works — print it today, scan it in ten years. What actually stops working is something else wearing the same name: a paid dynamic code whose subscription has ended, a link that has been deleted, or a print damaged beyond reading. Each of those failures needs a different fix, and only one of them is a reason to buy anything.</p>
<p>The confusion is understandable, because the warning usually arrives next to a pricing page: “free QR codes expire!” What expires in that sentence is rarely the code. It is the free trial, the subscription, or the vendor's willingness to keep redirecting your scans for free.</p>

<h2>Then why do people say QR codes expire?</h2>
<p>Three different things get tangled together:</p>
<ul>
<li><strong>Dynamic codes die when you stop paying.</strong> Many “free” generators actually make <em>dynamic</em> codes: instead of your link, the pattern holds a short URL on <em>their</em> server, which redirects to your link. Stop paying, and they switch the redirect off. Your code is not expired — it has been taken hostage.</li>
<li><strong>Links rot; codes do not.</strong> If the page behind the code is deleted, scanning leads nowhere. That is the destination dying, not the code. A QR code pointing at a dead link is a perfectly healthy code with nothing to say.</li>
<li><strong>Trial accounts get deactivated.</strong> Some services tie your codes to an account, then nudge you toward a subscription. The code did not expire — the account did.</li>
</ul>
<p>There is a fourth case that looks like expiry but is not the pattern's fault: codes issued by someone else's system. A boarding pass, ticket, or one-time login code can stop working because the issuer invalidates the session, ticket, or booking behind it. The pattern is still readable; the system behind it has withdrawn permission. That is a property of tickets and logins, not of QR codes in general.</p>

<h2>A pattern with no clock in it</h2>
<p>The QR code was developed in 1994 by DENSO WAVE to overcome the limits of barcodes on factory lines: the barcodes then in use could hold only about 20 alphanumeric characters, while parts tracking needed far more. The QR code that replaced them could store up to about 7,000 characters and was released with open patents and specifications, so anyone could use it. The format was designed as a way to carry data, not as a service with an account or a renewal date. The current edition of its standard, ISO/IEC 18004:2024, specifies the symbology, encoding, and error-correction rules — and it contains no timer, no licence check, and no expiry date, because a printed pattern has nowhere to store one and no one to report to.</p>
<p>That is why the FreeQrly angle is a consequence of the design, not a marketing claim. Every static code made here is free, and yours — no account, no redirect server, nothing to cancel. There is simply no mechanism by which it could expire. Paper can fade, tear, or be thrown away, but it cannot be switched off remotely.</p>

<h2>Static vs. dynamic, in one paragraph</h2>
<p>A <strong>static</strong> code encodes the destination directly: <code>WIFI:T:WPA;S:MyCafe;P:secret;;</code> or <code>https://your-site.com/menu</code>. Nothing to maintain, nothing to bill. A <strong>dynamic</strong> code encodes a redirect on someone's server, which lets the owner change the destination later and count scans. Useful for marketing campaigns — and a subscription for as long as the code must keep working. The full comparison, with the cases where each wins, is in <a href="/blog/static-vs-dynamic-qr-codes/">static vs dynamic QR codes</a>.</p>

<blockquote>Rule of thumb: if the destination will never change — your WiFi, your business card, your restaurant menu — static is not the cheap option. It is the <em>correct</em> option.</blockquote>

<h2>What actually stops a code: a diagnostic table</h2>
<table>
<tr><th>What you see on scanning</th><th>What actually failed</th><th>Fix</th></tr>
<tr><td>Nothing happens, on every phone</td><td>Print: too small, low contrast, damaged, or no quiet zone</td><td>Reprint larger, darker, with a clear margin; test a proof first</td></tr>
<tr><td>Code scans, but the page is missing</td><td>Link rot: page deleted, site moved, domain lapsed</td><td>Restore the page, or repoint a dynamic code; a static code needs a reprint</td></tr>
<tr><td>Code scans to a vendor upgrade or ad page</td><td>Subscription or trial ended; vendor switched the redirect off</td><td>Renew with that vendor, or replace the code with a static one</td></tr>
<tr><td>Code scans, then stops after many scans</td><td>Scan cap on a free dynamic plan</td><td>Upgrade, or replace with a code that has unlimited scans</td></tr>
<tr><td>Code scans on one phone, not another</td><td>Marginal print quality or a damaged finder square</td><td>Reprint larger and cleaner; do not rely on one phone's success</td></tr>
</table>

<h2>Steps: find out which failure you have</h2>
<ol>
<li><strong>Open the destination directly.</strong> Type the link into a browser, without scanning. If the page itself is missing, the code is innocent: restore the page, or, for a dynamic code, repoint it. If the page loads, the problem is the code, print, or redirect.</li>
<li><strong>Scan a printed proof on two phones.</strong> One iPhone and one Android if you can. If neither reads it, suspect size, contrast, damage, or a cropped quiet zone. If only one reads it, the print is marginal — reprint larger rather than trusting the phone that worked.</li>
<li><strong>Read the scan preview, not just the result.</strong> Before tapping, look at the URL your phone shows. A short vendor domain where you expected your own means a dynamic redirect is in the middle. A vendor upgrade page means the redirect has been switched off. A strange domain means a sticker or spoof, not an expiry.</li>
<li><strong>Check the account and plan behind a dynamic code.</strong> Log in to the creating account and check whether the plan is active, the code is within its scan allowance, and the code has not been deleted. Deleting a dynamic code stops its printed copies at once, on any vendor, because the redirect is removed.</li>
<li><strong>Fix the right layer.</strong> Print problem: reprint. Dead page: restore the page. Dead redirect: renew, or replace the code with a static code pointing at a page you control.</li>
</ol>

<h2>What actually goes wrong with printed codes</h2>
<p>Since expiry is not a thing, watch for these instead:</p>
<ul>
<li><strong>Print too small.</strong> As a rule of thumb, keep codes at least 2 × 2 cm with a quiet margin. Tiny codes on business cards are a common scan failure. The full sizing guidance, including distance, is in the <a href="/blog/qr-code-print-size-guide/">QR code print size guide</a>.</li>
<li><strong>Low contrast.</strong> Dark ink on a light background. That champagne-on-cream wedding code is beautiful and unreadable.</li>
<li><strong>Damage.</strong> Outdoor codes fade and scratch. Higher error correction helps: FreeQrly defaults to level M and bumps it automatically when you add a logo. At the High level in ISO/IEC 18004, up to about 30% of codewords can be restored — codewords, not visible area, so “30% damage” misleads. A small scratch over a finder square, the large corner square the scanner uses to locate the code, can stop a scan even when most of the pattern looks intact.</li>
<li><strong>No quiet zone.</strong> The blank margin around the code, at least 4 modules wide on all four sides under ISO/IEC 18004, is part of the code. Text or design crowded into it makes scanners fail to find the edges at all.</li>
<li><strong>Link changes.</strong> Moving your site? The old code still points at the old URL. Keep a list of where each code lives — or use a <a href="/dynamic-qr-code/">dynamic code</a> and repoint it instead of reprinting. Full checklist: <a href="/blog/why-is-my-qr-code-not-working/">why your QR code is not working</a>.</li>
</ul>

<h2>Scenarios: which codes should outlive their maker</h2>
<h3>A business card</h3>
<p>A business card is printed once and handed out for years. A static code holding a contact card or personal page is the right call: no account to maintain, no redirect to keep paying for, and no one who can switch it off. If the job title changes, the card is reprinted anyway, so the code's frozen destination costs nothing.</p>
<h3>A wedding invitation</h3>
<p>Invitations go out months before the day, and guests keep them on fridges long after. A static code to an RSVP page you control will still work when the thank-you notes go out, provided the page stays up. A dynamic code also works, but only if someone still minds the account in a year's time — for a one-day event, permanence beats editability. See <a href="/blog/wedding-rsvp-qr-code/">wedding RSVP QR codes</a> and <a href="/blog/free-qr-codes-that-dont-expire/">free QR codes that don't expire</a>.</p>
<h3>A restaurant menu or a shop window</h3>
<p>Here the choice splits on one question: does the destination change? A menu page you update in place needs only a static code pointing at that page — update the page, not the code. A menu that moves platforms, or a window offer that changes monthly, earns a dynamic code, because reprinting a window sign every month is the expensive option. See <a href="/blog/qr-codes-for-restaurants/">QR codes for restaurants</a>.</p>
<h3>A campaign poster with a deadline</h3>
<p>A poster is the classic dynamic case: it must print before the landing page is final, and later it can point at a recap or waiting list. But it is also where the subscription trap bites hardest, because the poster may still be on walls months after the campaign budget is gone. Before printing a campaign code on any vendor, read what that vendor does when the plan ends, and consider pointing, statically, at a campaign page you own instead.</p>
<h3>Packaging sold for years</h3>
<p>Packaging is the longest-lived print of all, and the worst place for a subscription-dependent code. A static code to a product page you control survives staff changes and budget cycles, because nothing about it needs renewing. A dynamic code on packaging is justified only when the destination genuinely must change over the product's life, and when someone owns keeping that account alive for the product's whole shelf life.</p>

<h2>The honest comparison: what vendors actually say</h2>
<p>Every vendor describes its own expiry behaviour on its pricing or FAQ page, and those pages are the only fair source for a comparison. The figures below are each vendor's own statements, checked on 3 November 2026. Prices and limits change, so check the vendor's page before you print anything that has to last — and read the free tier, not the headline.</p>
<table>
<tr><th>Vendor, free plan, as stated by the vendor</th><th>Free dynamic codes</th><th>Free scan limit</th><th>What the vendor says happens when a plan ends</th></tr>
<tr><td>FreeQrly, free account</td><td>20, currently unlimited during the limited-time promotion</td><td>Unlimited scans</td><td>Static codes never expire and need no account; deleting a dynamic code stops its printed copies and frees the slot</td></tr>
<tr><td>QR TIGER, freemium plan</td><td>3</td><td>500 scans per code</td><td>Paid codes have unlimited scans while the subscription is valid; “If your plan expires, it will stop working”; static codes are stated to never expire</td></tr>
<tr><td>The QR Code Generator, free plan</td><td>2</td><td>The free allowance is the 2 codes</td><td>After a trial ends, 2 codes remain active but display ads; on its parent platform Uniqode, trial codes become inactive without a paid plan</td></tr>
</table>
<p>Three patterns in that table are worth learning to spot. First, a scan cap is a second expiry: a free code capped at 500 scans dies from popularity, not from age, at the worst possible moment — when the campaign is working. Second, a trial is a calendar: codes made during a trial may keep working, keep working with advertisements, or stop entirely, depending on the vendor, and the vendor's pricing or FAQ page, not the sales page, is where the distinction lives. Third, “unlimited scans” on a paid plan means unlimited while the subscription is valid — a fair deal for a live campaign, a poor deal for a permanent sign.</p>
<p>FreeQrly's own position: a static code has no account and no redirect, so there is nothing to expire or renew. A dynamic code is free on a free account with unlimited scans, editable after printing, and counted in the Dashboard. Deleting one stops it permanently, because the redirect is removed — so delete only codes with no printed copy left in circulation.</p>

<h2>A safety note the expiry debate usually skips</h2>
<p>A code that scans is not necessarily a code you should trust. In a consumer alert dated 6 December 2023, the US Federal Trade Commission warned that scammers place their own QR stickers over real codes on parking meters, and send QR codes in unexpected messages inventing urgent reasons to scan — a missed delivery, an account problem, a password that must be changed. A scammer's code can lead to a spoofed site or to malware. The FTC's advice is the best habit: inspect the URL preview before opening a code in an unexpected place, look for misspellings or a switched letter, and do not scan a code from an unexpected message urging immediate action — contact the company through a number or site you already know instead. For your own codes, check the preview after every edit.</p>

<h2>The FreeQrly angle, and the choice that follows</h2>
<p>Every static code made here is free, and yours — no account, no redirect server, nothing to cancel. There is simply no mechanism by which it could expire. That is just how static codes work when nobody inserts themselves in the middle. Dynamic codes are a different, honest trade: sign in free, get 20 codes (currently unlimited during the limited-time promotion), edit them after printing, and see their statistics, with unlimited scans — dependence on a redirect and an account, in exchange for editability and measurement.</p>
<p>So the question before printing is not “will this code expire?” but “what could stop this code, and who controls it?” If the answer is “nothing, because the destination is in the pattern and the page is mine,” print static and stop worrying. If the answer is “the destination will change, and I will be here to change it,” print dynamic, keep the account, and keep the list of where each code lives. If the answer is “a vendor's subscription, and I am not sure I will renew it,” do not print that code on anything meant to last — point a static code at a page you own instead. Start with a static code in the <a href="/">free generator</a>, or, when the destination must stay editable, with <a href="/blog/how-to-create-a-dynamic-qr-code/">how to create a dynamic QR code</a> and the <a href="/dynamic-qr-code/">dynamic QR code generator</a>. Already printed and need to fix a link? <a href="/blog/how-to-edit-a-qr-code-after-printing/">How to edit a QR code after printing</a> explains the two-minute fix — for dynamic codes, at least.</p>""",
  faq=[
  ('Do free QR codes expire?', 'No, if they are static. A free static QR code lasts as long as the link it points to. Codes that stop working are usually dynamic codes tied to a paid subscription — the vendor switches the redirect off when you stop paying — or codes pointing at a deleted page.'),
  ('Can a QR code stop working?', 'Yes, but not from expiry. The usual causes are: the destination page was deleted, the code was printed too small or with low contrast, it got physically damaged, its quiet zone was cropped, or a dynamic plan ended or hit a scan cap.'),
  ('How long do static QR codes last?', 'Indefinitely, as long as the destination still works. The pattern encodes your data directly with no server involved, so there is nothing to maintain or renew.'),
  ('What happens to paid dynamic codes when a subscription ends?', "It depends on the vendor, and the vendor's own FAQ page is the source to check. QR TIGER's FAQ says paid codes have unlimited scans while the subscription is valid and 'If your plan expires, it will stop working.' The QR Code Generator says that after a trial ends, 2 codes remain active but display ads, while on its parent platform Uniqode trial codes become inactive without a paid plan."),
  ('Can a scan limit stop a QR code?', "Yes, on vendors that cap free dynamic scans. QR TIGER's freemium plan, as stated on its own subscription page, gives 3 dynamic codes with a 500 scan limit each. A code that hits its cap stops serving its destination even though the pattern is undamaged. FreeQrly dynamic codes have unlimited scans."),
  ('Does damage kill a QR code?', 'Not always. Error correction can rebuild missing data: at the High level in ISO/IEC 18004, up to about 30% of codewords can be restored. That counts codewords, not visible area — a small scratch over a corner finder square can stop a scan even when most of the pattern looks intact.'),
  ('How do I tell a dead link from a dead subscription from a bad print?', "Open the destination directly in a browser; scan a printed proof on two phones; read the scan preview URL before tapping; and, for a dynamic code, check the creating account's plan and scan allowance. Each check points at a different layer, and each layer has a different fix."),
  ('Should a permanent sign or packaging use static or dynamic?', "Static, if the destination is fixed. A static code to a page you control needs no account and no renewal, so it survives staff changes and budget cycles. Use dynamic only when the destination genuinely must change and someone will keep the account alive for the code's whole life."),
],
  sources=[
  ('http://www.iso.org/standard/83389.html', 'ISO/IEC 18004:2024', 'Retained from the original post. The QR Code symbology specification, Edition 4, published August 2024. Defines the four error-correction levels (L 7%, M 15%, Q 25%, H 30% of codewords) and the 4-module quiet zone.'),
  ('https://www.denso-wave.com/en/adcd/info/detail__190808_01.html', 'DENSO WAVE: 25th Anniversary of the QR Code', 'Published 8 August 2019. Supports: QR Code developed in 1994; barcodes then in use could hold only about 20 alphanumeric characters; QR Code could store up to about 7,000 characters; released with open patents and specifications.'),
  ('https://www.qrcode-tiger.com/faq', 'QR TIGER FAQ', "Vendor's own FAQ page, accessed 2026-11-03 (no publication date shown on the page). Supports: 3 free dynamic codes with a 500 scan limit each; paid dynamic codes have unlimited scans while the subscription is valid; 'If your plan expires, it will stop working'; free static codes are unlimited and never expire."),
  ('https://www.qrcode-tiger.com/software-subscription', 'QR TIGER Subscription Plan Management', "Vendor's own subscription page, accessed 2026-11-03 (no publication date shown on the page). Supports: freemium plan with 3 dynamic codes at a 500 scan limit each; Regular US$7 with 12 dynamic codes; Advanced US$16 with 200; Premium US$37 with 600; Professional US$89 with 1,200."),
  ('https://www.the-qrcode-generator.com/pricing?lng=en&signup_source=custom-qr-code_explore_plans', 'The QR Code Generator (TQRCG) Pricing', "Vendor's own pricing page, accessed 2026-11-03 (no publication date shown on the page). Supports: Free plan with 2 dynamic codes and unlimited static codes; after a free trial ends, 2 dynamic codes remain active but display ads; on Uniqode, trial codes become inactive without a paid plan."),
  ('https://consumer.ftc.gov/consumer-alerts/2023/12/scammers-hide-harmful-links-qr-codes-steal-your-information', 'FTC: Scammers hide harmful links in QR codes to steal your information', 'Consumer alert dated 6 December 2023. Supports: scammers covering QR codes on parking meters with their own codes; QR codes sent in unexpected messages inventing urgent reasons to scan; advice to inspect the URL preview and look for misspellings or a switched letter.'),
],
 ),
 dict(
  slug="static-vs-dynamic-qr-codes",
  title="Static vs Dynamic QR Codes: Free Forever or a Subscription? | FreeQrly",
  desc="Static codes are free forever: no sign-up, no watermark, no expiry. Dynamic codes are editable and trackable — FreeQrly gives you 20 free (currently unlimited) with scan stats. Here is how to choose.",
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

<h2>Static vs dynamic at a glance</h2>
<table>
<tr><th></th><th>Static code</th><th>Dynamic code</th></tr>
<tr><td><strong>Where the destination lives</strong></td><td>In the pattern itself</td><td>On the vendor's server, behind a short link</td></tr>
<tr><td><strong>Edit after printing</strong></td><td>No — print a new code</td><td>Yes — change the destination any time</td></tr>
<tr><td><strong>Scan statistics</strong></td><td>None — scans are silent</td><td>Counts and more, from the vendor</td></tr>
<tr><td><strong>Account needed</strong></td><td>No</td><td>Yes — a free account at minimum</td></tr>
<tr><td><strong>Cost</strong></td><td>Free forever</td><td>Free up to a limit, then a subscription</td></tr>
<tr><td><strong>Expiry</strong></td><td>Never — as long as the link works</td><td>Lives as long as the account and plan do</td></tr>
<tr><td><strong>Privacy</strong></td><td>Scans touch nothing but the destination</td><td>Every scan pings the vendor's server</td></tr>
</table>

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
<p>FreeQrly makes both. Static codes are free, unlimited, no account — and cover most everyday needs. Dynamic codes are free too: sign in (email, Google, or GitHub) and you get 20 free dynamic codes (currently unlimited during the limited-time promotion) with scan stats. <a href="/blog/how-to-create-a-dynamic-qr-code/">How to create one</a>, <a href="/blog/how-to-edit-a-qr-code-after-printing/">how to edit after printing</a>, and <a href="/blog/dynamic-qr-code-statistics/">what the stats tell you</a>. <a href="/dynamic-qr-code/">Make your first dynamic code</a> — free to start.</p>
""",
  faq=[
    ("What is the difference between static and dynamic QR codes?",
     "A static QR code encodes the destination directly in the pattern — free forever, uneditable. A dynamic QR code encodes a redirect on the vendor's server, so the destination can be changed later and scans can be tracked — but it requires an ongoing subscription."),
    ("Do I need a dynamic QR code?",
     "Probably not. If your destination won't change — WiFi, business cards, fixed links — static is the right choice. You need dynamic only for editable destinations or scan analytics, typically in marketing campaigns."),
    ("Why do free QR code generators push dynamic codes?",
     "Because dynamic codes require their server, which justifies a subscription. Many 'free' generators create dynamic codes tied to a trial — the code stops working when the trial ends."),
  ],
  sources=[
    ("https://www.qrcode-generator.com/", "QR Code Generator", "Free tool and PRO plans"),
    ("https://www.qrcode-tiger.com/software-subscription", "QR Tiger pricing", "Free plan and paid plan limits"),
  ],
 ),
]


POSTS += [{'body': """<p><strong>The short answer: point your phone's camera at the code, wait for the preview, read it, and tap it.</strong> No app to install, no account to create, no photo to take. Every modern iPhone and Android phone reads QR codes with the camera it already has, and the whole job takes a few seconds once you know the rhythm: frame the whole code, hold still, read the preview, tap. This guide covers what each kind of code does, what your phone asks along the way, the safety habit that matters most, and a fault chain for the moment nothing happens.</p>

<p>Start by recognising what you are looking at. A QR code is the square pattern with three large corner squares; those corners are the reader's landmarks, and a pattern without them is not a QR code at all — it may be an ordinary barcode, a proprietary mark, or a decorative pattern, and no QR reader will read it. A genuine QR code can hold several kinds of content, and knowing which kind you have scanned changes what you should expect next. A link opens a page, a Wi-Fi code offers a network, a contact code offers a person to save, a text code shows words, an event code offers a calendar entry, and a payment or ticket code opens an app or checkout. Your phone's preview tells you which kind it is before anything happens.</p>

<h2>What a scan gives you, by code type</h2>
<table>
<tr><th>Code holds</th><th>After the preview, expect</th><th>Check before you confirm</th></tr>
<tr><td>A web link</td><td>A browser page</td><td>The domain matches the sign or sender</td></tr>
<tr><td>Wi-Fi details</td><td>A prompt to join a network</td><td>The network name matches the sign</td></tr>
<tr><td>Contact details</td><td>A prompt to save a contact</td><td>The name and organisation look right</td></tr>
<tr><td>Plain text</td><td>The text itself, with a copy option</td><td>Nothing to confirm — just read it</td></tr>
<tr><td>An event</td><td>A prompt to add it to your calendar</td><td>Date, time, and place match the invitation</td></tr>
<tr><td>A payment or ticket</td><td>An app, a checkout, or a validation screen</td><td>Merchant or event name, and the amount</td></tr>
</table>

<h2>The steps, from code to destination</h2>
<ol>
<li><strong>Frame the whole code.</strong> Open the built-in Camera app and hold the phone so the entire square, including the blank margin around it, sits inside the frame. You do not need to press the shutter button. If part of the code is cut off, pull back until all four corners are visible.</li>
<li><strong>Hold still and let the camera focus.</strong> Give the camera a second to settle; a moving phone produces a blurred pattern.</li>
<li><strong>Read the preview.</strong> A link, a network name, or an action appears on screen. Read it fully before you tap — the domain, not just the first words. This step is the safety habit, and it is covered in detail below.</li>
<li><strong>Tap to open, and answer the confirmation.</strong> Tapping opens the destination; read any confirmation the same way, as a second preview.</li>
<li><strong>If nothing appears, work the fault chain.</strong> Do not keep pointing and hoping. The ordered checks below separate a phone problem from a light problem from a code problem in about a minute.</li>
<li><strong>If the code is already on your own screen, read the image instead.</strong> Screenshot the code, or save the image, and read it from the image (Photos on iPhone, Google Photos with Lens on Android). The full version is <a href="/blog/scan-qr-code-from-image/">the guide to scanning a QR code from a picture</a>.</li>
</ol>

<h2>Before you tap: permissions and confirmations</h2>
<p>Scanning asks very little of you, and that is part of its appeal — but the few things it does ask deserve attention. A browser-based scanner may ask for camera permission the first time; allow it while using the page, and revoke it afterwards. It does not need your photos, contacts, or location, and any such request is a reason to stop.</p>
<p>After the preview, confirmations follow the code type. A Wi-Fi code asks you to join a network — check the name against the sign before you join, since a rogue network with a plausible name is a real trick, and joining the wrong network is worse than failing to join the right one. A contact code asks you to save a person, and an app code asks you to open an app — check both against what you expected. A download should make you pause: a file is a larger commitment than a page. And a login form reached from a public code deserves a second look before any password goes near it.</p>

<h2>Scenarios: the same rhythm, different stakes</h2>
<p><strong>Menus, posters, and timetables</strong> are the lowest-stakes scans, and the rhythm is at its simplest: frame, preview, tap. Failures here are usually physical: tilt for glare, step closer for size, add light for darkness. <strong>Tickets and check-ins</strong> are higher-stakes because they are time-sensitive and often single-use. Have the code ready before you reach the queue, and scan promptly if it refreshes.</p>

<h2>The safety habit, in full</h2>
<p>A QR code hides its destination by design. You cannot read a URL from looking at the pattern, which is exactly why a code is such an effective vehicle for a link you would never tap if you could see it. The defence is not to avoid codes — it is to read the preview, every time, and to treat the preview as a decision, not a formality. The United States Federal Trade Commission warned about this pattern in a consumer alert dated December 6, 2023: scammers cover genuine codes with their own stickers — on parking meters, for example — or send codes in unexpected messages, and a scanned code can lead to a spoofed site that looks real, where anything entered can be stolen, or to malware. The FTC's advice in that alert is the same habit this guide recommends: inspect the URL before opening it, look for misspellings or a switched letter in a familiar name, and do not scan a code in an unexpected message, especially one urging immediate action.</p>
<p>Turn that advice into three checks: the domain, letter for letter, matches the business or sign in front of you; the code shows no tampering, such as a sticker pasted over another code; and the context fits — you expected this code, in this place, for this purpose. Failing any one of those checks is enough to stop. A preview showing only a shortened link hides the final destination just as thoroughly as the code itself did; if you do not recognise the sender, that is a reason to stop, not to tap and find out.</p>

<h2>When nothing happens: the fault chain, in order</h2>
<p>Work through this chain in order. Each step takes seconds, and the order matters: it moves from the cheapest fixes to the most conclusive test, so you stop as soon as you find the fault instead of trying everything at random. The phone-specific versions of these steps — the exact toggles and shortcuts on iPhone, Pixel, and Samsung — are in <a href="/blog/how-to-scan-qr-code-on-phone/">the phone scanning guide</a>; this chain is the logic that sits underneath them.</p>
<ol>
<li><strong>Frame.</strong> Is the whole code, including its quiet margin, inside the frame? Pull back until all four corners are visible. A code cropped by the frame's edge is the most common cause of silence.</li>
<li><strong>Mode.</strong> Use the normal photo view, not portrait or video, or use your phone's dedicated scanner shortcut.</li>
<li><strong>Setting.</strong> A toggle switched off by an update looks exactly like a broken code; check your camera settings first.</li>
<li><strong>Focus and steadiness.</strong> Hold steady and move slowly closer or farther until the pattern sharpens.</li>
<li><strong>Light.</strong> Add light in a dark room, remove glare in a bright one, and tilt slightly for a code behind glass.</li>
<li><strong>Lens.</strong> Is the lens clean? Wipe it with a soft cloth. A smudged lens blurs every code equally, which is why a dirty lens is so often mistaken for a bad print.</li>
<li><strong>Code integrity.</strong> Are the corner squares intact, the contrast dark-on-light, and the code free of damage, fading, or a distorting curve?</li>
<li><strong>Size and distance.</strong> Is the code large enough for the distance? Per the <a href="/blog/qr-code-print-size-guide/">print size guide</a>, a code should be at least one-tenth as wide as the scanning distance and at least 2 × 2 cm in print; move closer if it is too small for its distance.</li>
<li><strong>Second phone test.</strong> If another phone reads it, the problem is your phone; if none does, it is the code.</li>
</ol>

<h2>Going deeper: blur, damage, and the quiet zone</h2>
<p>Three code-side failures deserve more than a line in a chain, because they are the ones people misdiagnose most often. <strong>Blur</strong> is the first. A code can be blurred at creation — a low-resolution export stretched to poster size — or at capture — a moving phone, a shaky hand, a code photographed in poor light. Capture blur is fixed by holding still, adding light, and retaking; creation blur is fixed only by a better original. The full treatment is in <a href="/blog/why-is-my-qr-code-blurry/">why your QR code is blurry</a>.</p>
<p><strong>Damage</strong> is the second. Under ISO/IEC 18004, four error-correction levels — L, M, Q, H — let a reader reconstruct a damaged pattern: roughly 7% of codewords at L, 15% at M, 25% at Q, and 30% at H. So a scuffed code often still reads, and a code with a central logo reads because the correction absorbs the missing middle. The limit is the corner squares: damage one badly and the reader cannot orient the pattern at all, however good the error correction is elsewhere. That is why a torn corner fails while a scuffed middle succeeds.</p>
<p><strong>The quiet zone</strong> is the third, and the most often designed away. The blank margin around a code, at least four modules wide on every side under the standard, is what lets the reader find the code's edges. A design that crowds the code with text, borders, or graphics up to its edge is not being stylish; it is removing the margin the reader needs to find the pattern. Crowding, pale colours on white, and a logo covering a corner square are the design choices that most often turn a working code into a decoration; see <a href="/blog/why-is-my-qr-code-not-working/">why your QR code won't scan</a>.</p>

<h2>The honest comparison: built-in scanning, browser scanners, and scanner apps</h2>
<p>Three kinds of scanner compete for the same job, and the honest ranking is short. The built-in camera is the best default: already installed, already updated with the phone, and it reads standard codes with the same preview as any other reader, without an account or an ad between you and a menu. A browser scanner is the best backup: it needs no install, it works on a phone or a computer, and — when it decodes in your browser rather than uploading your image — it is the right tool for a code in a saved image or on a computer screen. Scanner apps are the weakest default for everyday scanning: they add an install, a permission screen, and often ads or an account, in exchange for a capability your phone already has.</p>
<p>The exceptions are real but narrow. A phone old enough to lack a built-in reader needs an app or a browser scanner. A person who scans codes all day for work — inventory, tickets, asset tags — may want a history, bulk reading, or exports, and a dedicated tool can justify itself there. And a code in a saved image on a phone whose gallery tools do not offer a reader may need a browser decoder, which is a better answer than an app for a single code. For everyone else, the case against an app is concrete: many scanner apps show ads, and some ask for permissions far beyond the camera — contacts, location, or an account that ties your scanning history to an identity. A scanner that knows every menu, ticket, and poster you have ever pointed it at knows a great deal about your movements, and that knowledge is the product being sold when the app itself costs nothing. The built-in camera reads the code and moves on; it does not keep a diary of your scans.</p>

<h2>When the scan works but the destination does not</h2>
<p>Sometimes everything above goes right and the result still disappoints: a dead link, a moved page, a form that no longer exists, a ticket that has already been used. That is not a scanning failure; it is a destination failure, and the fix belongs to whoever issued the code. A static code holds its destination directly, so if the destination is gone, the code has nothing to say. If the destination moved, only the issuer can point the code somewhere new — which is exactly what a dynamic code is for: it stays editable after printing, with scan statistics, under a free account. If you are the scanner and the link is dead, do not keep rescanning; ask the sender for a fresh code.</p>

<h2>Testing your own codes before anyone else scans them</h2>
<p>If you print codes for other people — a menu, a poster, a ticket, a business card — test them the way your audience will scan them, not the way you made them. Scan the printed proof, not just the screen version, because print changes size, contrast, and sharpness. Scan it on two phones if you can, one iPhone and one Android, because a code that reads on one and not the other has a real problem hiding in its size, contrast, or quiet zone. Scan it in the light and from the distance where it will actually be used. Thirty seconds of testing per code saves a reprint, a queue of confused customers, and a poster that is decoration rather than a door.</p>

<h2>Make your first code and scan it yourself</h2>
<p>The fastest way to learn all of this is to make a code and scan it yourself. FreeQrly's generator covers 17 types — links, Wi-Fi, contact cards, events, and more — and a static code made there is free with no sign-up, no watermark, and no expiry, so a test code costs nothing and keeps working. Print it, place it where you would actually use it, and try it in worse light, from farther away, and on a second phone. If the destination behind your code may change — a menu that updates seasonally, a poster going to print before its landing page exists — a dynamic code is the right tool instead: it stays editable after printing and reports scan statistics, with a free account. Dynamic codes are free for 20 codes, currently with unlimited availability during the promotional period, and with unlimited scans. For a batch of codes, <a href="/batch-qr-code/">batch generation</a> makes one code per link. Start with one static test code, scan it on your own phone, and build from a result you have actually seen work.</p>""",
  'date': '2026-10-14', 'updated': "November 3, 2026", 'dateModified': "2026-11-03",
  'desc': 'How to scan a QR code on iPhone and Android — no app needed. Use the built-in camera, '
          "Control Center, or Google Lens, and fix it when it won't scan.",
  'faq': [
  ('Do I need an app to scan QR codes?', 'No. iPhones and virtually all Android phones scan QR codes with the built-in camera. Third-party scanner apps are unnecessary for standard codes, and are a reasonable answer only for a phone with no built-in reader or for work that needs a history or bulk reading.'),
  ('What happens after I scan a QR code?', "It depends on what the code holds: a link opens a web page, a Wi-Fi code offers to join a network, a contact code offers to save a person, a text code shows words, and an event code offers a calendar entry. Your phone's preview tells you which kind it is before anything opens."),
  ("How do I scan a QR code that is on my own phone's screen?", 'Screenshot the code or save the image, then read it from the image: on iPhone, open it in Photos and press and hold the code; on Android, open it in Google Photos and tap Lens. A camera cannot point at its own screen.'),
  ("Why won't my camera scan the QR code?", 'Work the fault chain in order: whole code in frame, normal photo view, scanning switched on, steady focus, good light without glare, clean lens, intact corner squares and contrast, and size for the distance. Finish with a second-phone test: if another phone reads it, the problem is your phone; if none does, it is the code.'),
  ('What is the difference between a QR code and a barcode?', "A QR code is the square pattern with three large corner squares, which are the reader's landmarks. A pattern without those corner squares is not a QR code, and no QR reader will read it."),
  ("My QR code scans, but the link doesn't work. Is the code broken?", 'No. The code did its job; the destination is the problem — the page moved, the site is down, or the form no longer exists. Contact the sender for a fresh code, or, if you issued it, use a code whose destination you control or a dynamic code that stays editable.'),
  ('Is it safe to scan a QR code I find in public?', 'Read the preview before you tap: the domain should match the sign in front of you, the code should show no tampering such as a sticker pasted over another code, and you should have expected this code in this place. Failing any one of those checks is enough to stop.'),
  ('How do I test a QR code I printed before other people scan it?', 'Scan the printed proof, not just the screen version, on two phones if you can — one iPhone and one Android — in the light and from the distance where it will actually be used. A code that reads in all of those conditions has its size, contrast, and quiet zone right.'),
],
  'h1': 'How to <span class="hl hl-mint">scan</span> a QR code',
  'howto': [
  ('Frame the whole code', 'Open the built-in Camera app and hold the phone so the entire square, including the blank margin around it, sits inside the frame. Do not press the shutter button.'),
  ('Hold still and let the camera focus', 'Give the camera a second to settle; a moving phone produces a blurred pattern.'),
  ('Read the preview', 'A link, a network name, or an action appears on screen. Read it fully before you tap — the domain, not just the first words.'),
  ('Tap to open, and answer the confirmation', 'Tapping opens the destination or triggers the action. Read any confirmation the same way, as a second preview.'),
  ('If nothing appears, work the fault chain', 'Check in order: whole code in frame, normal photo view, scanning switched on, steady focus, good light without glare, clean lens, intact corner squares and contrast, size for the distance — then a second-phone test.'),
  ('If the code is already on your own screen, read the image instead', 'Screenshot the code, or save the image, and read it from the image: on iPhone, open it in Photos and press and hold the code; on Android, open it in Google Photos and tap Lens.'),
],
  'lede': 'No app required. Every modern iPhone and Android phone scans QR codes with the camera '
          "it already has. Here's how — plus what to do when nothing happens.",
  'mascot': 'scanner',
  'slug': 'how-to-scan-a-qr-code',
  'cta': {'title': 'Try it yourself — free', 'text': 'Everything in this article works in the FreeQrly studio right now. Static codes, all 17 content types, PNG and SVG export.', 'href': '/#studio', 'btn': 'Open the studio'},
  'title': 'How to Scan a QR Code (iPhone & Android) | FreeQrly',
  'sources': [
  ('https://support.apple.com/en-ca/102680', 'Apple Support: Scan a QR code with your iPhone or iPad', 'RETAINED from the original post (original URL kept verbatim). The same guide, verified on the current en-us page published September 14, 2026, describes opening Camera or Code Scanner, holding the device so the code appears, and tapping the link.'),
  ('https://consumer.ftc.gov/consumer-alerts/2023/12/scammers-hide-harmful-links-qr-codes-steal-your-information', 'FTC: Scammers hide harmful links in QR codes to steal your information', 'RETAINED from the original post. Consumer alert dated December 6, 2023 (FTC listing; page verified by opening it 2026-11-03). Supports: scammers covering genuine codes with their own stickers, including on parking meters, and sending codes in unexpected messages; a scanned code can lead to a spoofed site or malware; inspect the URL before opening it and do not scan a code in an unexpected message urging immediate action.'),
  ('http://www.iso.org/standard/83389.html', 'ISO/IEC 18004:2024', 'ADDED. The QR Code symbology specification. Supports the body figures: four error-correction levels (L roughly 7%, M roughly 15%, Q roughly 25%, H roughly 30% of codewords) and the quiet zone of at least 4 modules on every side. Page accessed 2026-11-03; the ISO listing itself carries no public summary with the figures, which were corroborated against standard explainers during verification.'),
  ('https://support.google.com/pixelphone/answer/16561572?hl=en', 'Google Support: Scan QR codes with your Pixel phone', 'ADDED. Page accessed 2026-11-03; no publication date shown on the page. Supports the generic troubleshooting steps reflected in the fault chain (hold steady, good light without glare, clean lens, move closer while keeping the whole square in frame).'),
  ('https://www.samsung.com/uk/support/mobile-devices/how-to-scan-qr-code-on-your-galaxy-phone-or-tablet/', 'Samsung Support: How to scan QR codes on your Samsung phone', 'ADDED. Updated October 6, 2026 (shown on the page, verified by opening it 2026-11-03). Supports the phone-specific steps the general guide points to (Camera app, Quick Settings Scan QR code tile, Camera settings Scan QR codes toggle).'),
]},
 {'body': """<p>A QR code that will not scan is almost never a mystery. Run through these checks — in order — and you will find the culprit in about two minutes. Before you change anything, split the problem three ways: the phone, the printed or displayed code, and the destination. Scan with a second phone. If it reads the code, the first phone, its camera, or its lighting is the problem. If no phone reads it, the code itself — size, contrast, margin, damage, or logo — is the problem. If phones read it but the link goes nowhere, the code is doing its job and the destination is the problem. That three-way split saves most people a pointless reprint, because each branch has a different fix.</p>
<h2>The diagnostic table: check in this order</h2>
<table>
<tr><th>Order</th><th>Check</th><th>Quick test</th><th>Fix</th></tr>
<tr><td>1</td><td>Phone and camera</td><td>Wipe the lens; try a second phone</td><td>Clean lens, better light, steadier hold</td></tr>
<tr><td>2</td><td>Distance and angle</td><td>Move closer; fill half the viewfinder; shoot straight on</td><td>Print larger, or move the code closer</td></tr>
<tr><td>3</td><td>Size</td><td>Measure the code; compare with the distance rule</td><td>Reprint larger; see the <a href="/blog/qr-code-print-size-guide/">print size guide</a></td></tr>
<tr><td>4</td><td>Contrast</td><td>Check it in dim light: dark on light?</td><td>Black on white; drop busy backgrounds</td></tr>
<tr><td>5</td><td>Quiet zone</td><td>Clear blank margin on all four sides?</td><td>Restore a margin at least 4 modules wide</td></tr>
<tr><td>6</td><td>Damage and fading</td><td>Check the three corner squares and surface</td><td>Reprint; raise error correction for harsh use</td></tr>
<tr><td>7</td><td>Logo obstruction</td><td>How much of the grid does the logo hide?</td><td>Shrink the logo, raise error correction, print larger</td></tr>
<tr><td>8</td><td>Glare, curve, angle</td><td>Tilt the print; flatten the surface</td><td>Matte finish, flatter placement, larger code</td></tr>
<tr><td>9</td><td>Sharpness</td><td>Are module edges crisp or smeared?</td><td>Re-export larger or as SVG; see <a href="/blog/why-is-my-qr-code-blurry/">why your code looks blurry</a></td></tr>
<tr><td>10</td><td>Destination</td><td>Link preview shown? Link opens?</td><td>Fix the page, or redirect a dynamic code</td></tr>
</table>
<h2>The two standards that explain most failures</h2>
<p>Two ideas from ISO/IEC 18004, the QR code symbology specification, explain a surprising share of scan failures. The first is the quiet zone: a blank margin at least 4 modules wide on every side, where a module is one small square of the grid. Scanners use that border to find where the symbol begins and ends, so text, graphics, or a crop invading it can make a perfect code invisible to a camera. The second is error correction: extra data that lets a reader rebuild codewords that come back wrong or unreadable, at four levels — L approximately 7%, M approximately 15%, Q approximately 25%, H approximately 30%. Those percentages describe codewords, not visible area: a torn finder pattern can kill a code well inside its level, while scattered minor damage elsewhere may survive. Higher levels are not free either: more recovery data means a denser grid, so raising the level on an already-small code can make it harder to read. Raise it for a reason — a logo, rough handling, outdoor use — then re-check size and test-scan.</p>
<table>
<tr><th>Level</th><th>Approximate codeword recovery</th><th>Best for</th></tr>
<tr><td>L</td><td>7%</td><td>Clean, screen-only codes, no logo, no wear</td></tr>
<tr><td>M</td><td>15%</td><td>The usual default for ordinary print</td></tr>
<tr><td>Q</td><td>25%</td><td>Print that will be handled, scuffed, or weathered</td></tr>
<tr><td>H</td><td>30%</td><td>Codes with a central logo, or harsh conditions</td></tr>
</table>
<h2>Step 1: rule out the phone</h2>
<p>Wipe the lens. A smudged lens is behind an embarrassing number of supposedly broken codes, because a thin film of grease softens the whole image just enough to blur module edges. Then test on a second phone: if phone B reads it, the code was never the problem. The whole square must be in frame, with a little room around it — a code cropped by the viewfinder edge will not read. Hold still once the code fills about half the viewfinder, and move to better light in dim conditions. A code that shows a preview but goes nowhere when tapped has a destination problem (Step 9), not a scanning problem.</p>
<h2>Step 2: size and distance</h2>
<p>The classic failure is a code squeezed into a business card corner at 1 cm wide. As a rule of thumb, printed codes need at least 2 x 2 cm (about 0.8 inches), and bigger is always safer. Size and distance follow the 1:10 distance rule of thumb: code width at least one-tenth of scanning distance — 5 cm for a table card scanned from 50 cm, 50 cm for a poster scanned from 5 metres. Below that rule for its distance, no cleaning, re-angling, or re-exporting will reliably fix it — reprint larger, or move the code closer to where people stand. The full breakdown by use case is in the <a href="/blog/qr-code-print-size-guide/">print size guide</a>. Density tightens the rule: a short link gives a roomy grid, while a long link, full contact card, or long Wi-Fi password gives a denser grid with smaller modules, needing a larger print. A dynamic code shortens the printed pattern without shortening the final destination, because it encodes a short link you control and can redirect later, with scan stats showing performance.</p>
<h2>Step 3: contrast</h2>
<p>QR readers look for dark modules on a light background. Light grey on white, brand pastels, a dark code on dark, or a code over a busy photo will fail — especially in dim light. Judge it in the light where the code will actually be scanned: if you squint to tell modules from background, a phone camera will struggle too. The fix is black on white, which always works, with the quiet zone in the same light background colour. Inverted codes — light modules on dark — are a special case: some readers handle them and many do not, so do not rely on inversion for public codes. If brand colours matter, keep them in the surrounding design and a small central logo, not in the modules, and test the coloured version in dim light first.</p>
<h2>Step 4: the quiet zone</h2>
<p>The blank margin around the code is not decoration — scanners need it to find the edges. Keep a clear border at least 4 modules wide on all four sides, as specified in ISO/IEC 18004, and keep text, rules, decorative borders, and nearby images out of it. This failure is common in designed layouts, where a headline, a rule, or a photo edge creeps into the margin, and at a page edge, where a code too close to the trim loses its margin. Check all four sides: a margin generous on three sides and zero on the fourth still fails. The fix is layout, not re-export — give the code room, or place it on a plain light panel that guarantees the margin inside a busy layout.</p>
<h2>Step 5: damage, fading, and wear</h2>
<p>Creased flyers, sun-faded posters, scratched stickers, rain-spotted labels: error correction can survive some damage, but location matters more than size. Damage to the three large corner finder patterns is the most serious, because without them the reader cannot find or orient the grid — a torn finder pattern is often fatal even when the rest looks intact. Scattered scuffs across the data area are far more forgiving, because that is what error correction is built to rebuild. Fading is slower damage: as dark modules lighten towards the background, contrast falls until the reader can no longer separate modules, even though the pattern is still there. Judge a worn code corners first, then contrast, then surface. The fix for a damaged print is a reprint; for a code that will live a hard life — outdoors, on packaging, on a vehicle — be preventive: higher error correction, a larger print, lamination or a sheltered position.</p>
<h2>Step 6: logo obstruction</h2>
<p>A logo in the centre eats into the pattern, consuming part of the error-correction budget by design — which is why it can work, and why it can fail. Judge it by how much of the grid the logo covers and whether it touches a finder pattern: a small logo cleanly centred, clear of the three corners, is safe; a large logo, one spreading towards the corners, or one with busy detail mimicking modules is risky. As a rule of thumb, keep the logo under about 30% of the code area, print logo codes at 3 x 3 cm or larger, and use error correction Q or H. Test the logo version specifically: a plain code that scans tells you nothing about its logo sibling. If a logo code fails, shrink the logo first, then enlarge the print, then raise the level, testing after each change. See <a href="/blog/add-logo-to-qr-code/">how to add a logo to a QR code</a> and <a href="/qr-code-with-logo/">the logo code generator</a>.</p>
<h2>Step 7: glare, curve, and angle</h2>
<p>Glossy lamination under bright light, a code wrapped around a bottle, or a photo taken at a steep angle all distort what the camera sees. Glare washes modules out in patches; a curve stretches edge modules while compressing middle ones; a steep angle turns squares into trapezoids the reader must un-warp. Tilt the print slowly: if the unreadable patch moves with the reflection, it is glare. Flatten the surface if you can, and shoot straight on. Prefer a flat panel over a tight curve, matte over gloss where lights are strong, and a position people can face squarely. A bottle code that scans when turned to face the camera is a placement problem — move it to the flattest, most front-facing spot, and print it larger.</p>
<h2>Step 8: sharpness — when blur is the culprit</h2>
<p>If the code is the right size, high contrast, well margined, undamaged, and logo-free, yet still hesitates, look at the module edges: crisp or smeared? Low-resolution exports, JPEG compression, stretching, poor print, and copies of copies all soften edges, and soft edges fail first in dim light and at distance. The full diagnosis is in <a href="/blog/why-is-my-qr-code-blurry/">why your QR code looks blurry</a>. Short version: re-export at 1024 px for cards and flyers or 2048 px for posters, use SVG whenever the printer accepts it, never use JPEG for a code, keep proportions when resizing, and test-scan one real print at the real distance first. Softness and weak contrast compound, so fix both rather than hunting for a single culprit.</p>
<h2>Step 9: the destination is dead</h2>
<p>Sometimes the code scans fine — but the link is broken, the page moved, the site is down, or a trial-based generator deactivated the code. This is the expired-link trap: nothing useful happens after the tap, so it feels like a scanning failure. Watch the link preview: if a preview appears, the code decoded and the destination is the problem. Check whether the page opens when typed directly into a browser, and whether the link was shortened by a service that has since changed its terms. Static codes never expire on their own — the destination lives inside the pattern, so a static code fails only if the destination itself goes away. Dynamic codes point at a short link you control, so a moved page is fixable without reprinting: sign in, change the destination, and the printed code works again, with scan stats to confirm it. That editability is also the trap to avoid when choosing a generator: a code tied to an ended trial can stop working even though the pattern is perfect — see <a href="/blog/do-qr-codes-expire/">do QR codes expire?</a> before a large run. For codes already printed: static plus moved page means restore the page or reprint; dynamic means redirect it and test on two phones.</p>
<h2>Scenarios: the same checklist, different culprits</h2>
<h3>A flyer that scans in the office but not at the event</h3>
<p>Office light is kind; event light is not. The usual culprits are contrast that only just passes in bright light, a code slightly too small for the distance people stand at, and gloss under venue lights. Fix in order: test in the venue's light, enlarge the code, switch to matte, and return to black on white before reprinting.</p>
<h3>A business card that scans for you but not for clients</h3>
<p>Your phone knows the code; a stranger's phone meets it cold, in worse light, at a different angle. Check size first — below 2 cm as a rule of thumb fails on many phones — then the quiet zone, which card designs love to crowd, then the stock, which may absorb ink and soften edges.</p>
<h3>A code on screen — slides, video, or social images</h3>
<p>Screen codes fail on compression, size, and time. A code recompressed by a platform, shown small in a slide corner, or flashed briefly in a video gives the camera little to work with. Keep it large, flat to the camera, and on screen long enough to scan; for a code inside a photo, <a href="/blog/scan-qr-code-from-image/">scanning from an image</a> is the fallback.</p>
<h2>Honest comparison: reprint, redirect, or redesign?</h2>
<p>Not every failure deserves a reprint. If the destination moved and the code is dynamic, redirecting beats reprinting on cost, waste, and speed — the pattern stays valid and the fix takes minutes. If the code is static and the destination moved, redirecting is not an option: restore the destination or reprint, and choose dynamic next time if the destination may change again. If the pattern itself is at fault — too small, low contrast, crowded margin, heavy logo, soft print — no redirect will help, because the reader cannot decode the pattern; reprint with that parameter changed, one parameter at a time, so you learn which fix worked. Two trade-offs deserve a plain statement. First, higher error correction is not a cure-all: it buys tolerance for damage and logos, but it densifies the grid, so raising the level on an already-small code can make it worse. Second, a coloured or logo code that scans in your office is not proven: it is proven only when it scans first try, in the real light, at the real distance, on two different phones, on the real material.</p>
<h2>Test before you print — every time</h2>
<ol>
<li><strong>Scan on two phones</strong> — one iPhone, one Android if you can — before printing.</li>
<li><strong>Test at the real distance and in the real light</strong>, on the real material.</li>
<li><strong>Check the preview, then the destination</strong>: a preview means the code decoded; an opening page means the destination works.</li>
<li><strong>Change one thing at a time</strong> when a test fails, so you know which fix actually fixed it.</li>
</ol>
<p>Generate a test code in the <a href="/#studio">free generator</a> — 17 types, static codes free with no sign-up, no watermark, and no expiry, dynamic codes free after sign-in with editing and scan stats, and unlimited scans — and run it through the checklist above. If the failure is sharpness rather than size, contrast, or damage, see <a href="/blog/why-is-my-qr-code-blurry/">why your QR code looks blurry</a>; for sizing by use case, see the <a href="/blog/qr-code-print-size-guide/">print size guide</a>; and if the code scans but the destination must change after printing, see <a href="/blog/how-to-edit-a-qr-code-after-printing/">how to edit a QR code after printing</a>.</p>""",
  'date': 'October 14, 2026', 'updated': "November 3, 2026", 'dateModified': "2026-11-03",
  'datePublished': '2026-10-14',
  'desc': 'QR code not scanning? Seven real fixes: size, contrast, damage, quiet zone, and the '
          'expired-link trap — plus how to test before you print.',
  'faq': [
  ('Why does my QR code scan on one phone but not another?', 'Then the code itself is usually fine — it is the camera, lighting, or angle on the failing phone. Wipe the lens, move to better light, hold the code so it fills about half the viewfinder, and try again.'),
  ('Can a damaged QR code still work?', 'Often yes, thanks to error correction — at the High level, approximately 30% of codewords can be restored, as defined in ISO/IEC 18004. But damage to the three corner finder patterns or to the quiet zone is much harder to recover from, and heavy fading will kill a code even when its shape looks intact.'),
  ('My QR code scans but the link does not work — is the code broken?', 'No, the code is doing its job. The destination is the problem: the page moved, the site is down, or a trial-based generator deactivated it. If the code is dynamic, sign in and redirect it; if it is static, restore the page or reprint.'),
  ('How big should a printed QR code be?', 'As a rule of thumb, at least 2 x 2 cm, and at least one-tenth of the scanning distance: 5 cm for a table card scanned from 50 cm, 50 cm for a poster scanned from 5 metres. Denser codes holding long links or contact cards need to be larger at the same distance.'),
  ('Why does my logo code fail when the plain version scans?', 'The logo covers part of the grid and consumes error-correction budget. Keep the logo under about 30% of the code area as a rule of thumb, print logo codes at 3 x 3 cm or larger, use error correction Q or H, and test the logo version itself — a plain code that scans proves nothing about its logo sibling.'),
  ('How much blank space does a QR code need around it?', 'A quiet zone at least 4 modules wide on all four sides, as specified in ISO/IEC 18004. Keep text, rules, decorative borders, and nearby images out of it, and check all four sides — a margin generous on three sides and zero on the fourth still fails.'),
  ('Can I fix a printed QR code without reprinting?', 'Only if the problem is the destination and the code is dynamic: sign in, change the destination, and the printed pattern works again. If the pattern itself is at fault — too small, low contrast, crowded margin, heavy logo, or soft print — the fix is a reprint with that parameter changed.'),
],
  'h1': 'Why won’t this thing <span class="hl hl-blush">scan</span>?',
  'howto': [
  ('Rule out the phone', 'Wipe the lens and test on a second phone. If phone B reads it, the code was never the problem. Keep the whole square in frame and hold still once it fills about half the viewfinder.'),
  ('Check size and distance', 'As a rule of thumb, printed codes need at least 2 x 2 cm, and at least one-tenth of the scanning distance. Below that rule for its distance, reprint larger or move the code closer to where people stand.'),
  ('Check contrast', 'Dark modules on a light background. If you squint to tell modules from background in the real scanning light, return to black on white and do not rely on inverted codes for public use.'),
  ('Check the quiet zone', 'Keep a clear border at least 4 modules wide on all four sides, as specified in ISO/IEC 18004. Check all four sides — a margin generous on three sides and zero on the fourth still fails.'),
  ('Check damage, fading, and wear', 'Check the three corner finder patterns first, then contrast, then the surface. A torn finder pattern is often fatal; scattered scuffs are what error correction is built to rebuild.'),
  ('Check logo obstruction', 'Keep the logo under about 30% of the code area as a rule of thumb, print logo codes at 3 x 3 cm or larger, and use error correction Q or H. Test the logo version itself.'),
  ('Check glare, curve, and angle', 'Tilt the print to separate glare from blur, flatten the surface if you can, and shoot straight on. Prefer a flat panel over a tight curve and matte over gloss where lights are strong.'),
  ('Check sharpness', 'Look at the module edges: crisp or smeared? Re-export at 1024 px for cards and flyers or 2048 px for posters, use SVG whenever the printer accepts it, and never use JPEG for a code.'),
  ('Check the destination', 'If a link preview appears, the code decoded and the destination is the problem. Dynamic codes can be redirected without reprinting; static codes need the page restored or a reprint.'),
],
  'lede': "A QR code that won't scan is almost never a mystery. Run through these seven checks — "
          "in order — and you'll find the culprit in about two minutes.",
  'mascot': 'error',
  'slug': 'why-is-my-qr-code-not-working',
  'cta': {'title': 'Try it yourself — free', 'text': 'Everything in this article works in the FreeQrly studio right now. Static codes, all 17 content types, PNG and SVG export.', 'href': '/#studio', 'btn': 'Open the studio'},
  'title': 'QR Code Not Working? 7 Fixes That Help | FreeQrly',
  'sources': [
  ('http://www.iso.org/standard/83389.html', 'ISO/IEC 18004:2024', 'Retained from the original post. The QR Code symbology specification. ISO page shows Edition 4, published 2024-08 (page fetched 2026-11-03). Supports the four error-correction levels (L 7%, M 15%, Q 25%, H 30% of codewords) and the 4-module quiet zone, as defined in the standard.'),
  ('https://qrlynx.com/blog/iso-iec-18004-qr-code-standard-explained', 'ISO/IEC 18004:2024 Explained (QRLynx)', 'Reviewed July 2026 against ISO and DENSO WAVE. Supports the codeword reading of the error-correction percentages (7% / 15% / 25% / 30% of total codewords, not a guaranteed visible-area tolerance) and the four-module quiet zone specified by DENSO WAVE.'),
]},
 {'body': """<p>The short answer: at least 2 × 2 cm, at 300 dpi, with a clear margin. The longer answer — the one that keeps a poster scannable from across a room and a business card scannable from a handshake — is two rules of thumb plus a table. Rule one: never print a code smaller than 2 × 2 cm (0.8 × 0.8 in). Rule two: the code's width should be at least one-tenth of the scanning distance. A code scanned from 50 cm needs a 5 cm code; a poster scanned from 5 meters needs a 50 cm code. Everything below works those two rules out for every surface you are likely to print on, plus the format, margin, and proofing details that decide whether the size actually works.</p>

<h2>The two rules that matter</h2>

<p><strong>Rule of thumb 1 — minimum size:</strong> 2 × 2 cm (0.8 × 0.8 in). Below that, phone cameras cannot resolve the modules reliably, especially codes holding a lot of data like vCards. This is a practical minimum for close, hand-held scanning, not a guarantee: a dense code at 2 cm is far more fragile than a short-URL code at the same size, and older phones need more room than new ones.</p>

<p><strong>Rule of thumb 2 — the 1:10 distance ratio:</strong> the code's width should be at least one-tenth of the scanning distance. Scanning from 50 cm (a table card)? 5 cm code. From 5 meters (a poster)? 50 cm code. Printers and signage folks use this ratio as a rule of thumb — it is a planning guideline, not part of the QR standard itself — and the safe habit is to round up rather than down, because distance, lighting, and glare all eat into the margin of safety.</p>

<p>Those two rules interact. The 1:10 ratio can demand less than the 2 cm minimum — a code scanned from 15 cm would only need 1.5 cm by the ratio — and in that case the minimum wins: print 2 cm anyway.</p>

<h2>Cheat sheet by use case</h2>

<table>
<tr><th>Use case</th><th>Typical scanning distance</th><th>Minimum size</th><th>Notes</th></tr>
<tr><td>Business cards</td><td>20–25 cm, in the hand</td><td>2 × 2 cm</td><td>Keep it clear of the card edge. See the <a href="/business-card-qr-code/">business card generator</a>.</td></tr>
<tr><td>Flyers and menus</td><td>30–40 cm, arm's length</td><td>3 × 3 cm</td><td>People scan these at arm's length; go to 4 cm for dense codes.</td></tr>
<tr><td>Table tents</td><td>30–50 cm, from a seat</td><td>4–5 cm</td><td>Guests scan from their seats, often in dim light — size up.</td></tr>
<tr><td>Receipts and tickets</td><td>20–30 cm, in the hand</td><td>2–3 cm</td><td>Thermal printing blurs fine detail; use a short URL and test on the actual printer.</td></tr>
<tr><td>Packaging and labels</td><td>20–30 cm, in the hand</td><td>2 × 2 cm</td><td>Avoid curved surfaces that distort the pattern; use a flat panel.</td></tr>
<tr><td>Codes with a logo</td><td>As the plain version, or closer</td><td>3 × 3 cm</td><td>Keep the logo under about 30% of the code area. Full guide: <a href="/blog/add-logo-to-qr-code/">adding a logo to a QR code</a>.</td></tr>
<tr><td>Posters (A3/A2, on a wall)</td><td>1–1.5 m</td><td>10–15 cm</td><td>Size by the 1:10 ratio; check the viewing distance in the actual room.</td></tr>
<tr><td>Shop windows and noticeboards</td><td>2–3 m</td><td>20–30 cm</td><td>Watch for glass glare; test from outside.</td></tr>
<tr><td>Outdoor signage and banners</td><td>5 m and more</td><td>50 cm and more</td><td>Ask whether people will really scan from that far — a smaller sign closer to the walkway often works better.</td></tr>
<tr><td>Slides and screens</td><td>Arm's length to several meters</td><td>At least 200 × 200 px; scale with distance</td><td>For a projected slide, apply the 1:10 ratio to the projected width, not the file size.</td></tr>
</table>

<p>Two cautions apply to the whole table. First, the sizes are for the code itself; the quiet zone goes on top, so the total footprint is larger. Second, size up whenever the code holds a lot of data, carries a logo, or will be scanned in poor light.</p>

<h2>The distance rule, worked out</h2>

<p>To work out a size, divide the distance people will scan from by ten, then round up — and never below the 2 cm minimum. A few worked examples make the habit automatic:</p>

<table>
<tr><th>Scanning distance</th><th>Distance ÷ 10</th><th>Print at least</th></tr>
<tr><td>30 cm (a flyer in hand)</td><td>3 cm</td><td>3 cm</td></tr>
<tr><td>50 cm (a table card)</td><td>5 cm</td><td>5 cm</td></tr>
<tr><td>1 m (a wall poster)</td><td>10 cm</td><td>10 cm</td></tr>
<tr><td>2 m (a bus-stop poster)</td><td>20 cm</td><td>20 cm</td></tr>
<tr><td>5 m (a sign across a car park)</td><td>50 cm</td><td>50 cm</td></tr>
<tr><td>10 m (a billboard)</td><td>100 cm</td><td>1 m</td></tr>
</table>

<p>The distance to use is the distance people will actually stand at, not the distance you wish they would. A poster in a corridor is scanned from the corridor's width; a sign across a car park is scanned from where people walk, not from the far fence.</p>

<h2>Why data density changes the answer</h2>

<p>Not all QR codes have the same number of modules. The more data you put in, the more modules the code needs: the smallest code (Version 1) is 21 × 21 modules, and each version up adds four modules per side, to a maximum of 177 × 177. Printed at the same size, a denser code has smaller modules, and smaller modules are harder for a camera to separate — especially in poor light.</p>

<p>Error correction adds the same trade-off. Higher levels are more robust, which is useful for codes with a logo or on surfaces that may get scuffed, but they also add modules. As a rough example, a 40-character web address fits in a 29 × 29 code at level M, but needs 37 × 37 at level H; on a 2 cm code, that shrinks each module from about 0.69 mm to about 0.54 mm. The practical takeaway: keep the content short. Use a short, clean URL instead of a long tracking link, include only the vCard fields you actually need, and if a small printed item must hold a lot, make the code bigger. A dynamic code helps differently: its destination is editable after printing, so you can print a short redirect once and change where it points later, instead of encoding a long URL that forces a dense grid — and it carries scan statistics, so you can see whether the size you chose is actually getting scanned.</p>

<h2>Resolution: export big</h2>

<p>Print needs 300 dpi. A 2 cm code at 300 dpi is only about 240 px — but always export larger and let the designer scale down: <strong>PNG at 1024 or 2048 px</strong>, or <strong>SVG</strong>, which is infinitely scalable and the best choice for professional print. FreeQrly exports both, free. The pixel math is simple: divide a PNG's pixel width by 300 to get its maximum print width in inches, and multiply by 2.54 for centimeters. A 600 px image gives 2 inches, about 5 cm, at 300 dpi — fine for a table card, far too small for a poster. A 2048 px image gives about 17 cm at 300 dpi, which covers flyers, menus, and small posters, but not a shop window; for that, use SVG.</p>

<p>For very large formats viewed from a distance, printers commonly accept lower effective resolutions — around 150 dpi is a workable benchmark for large posters — because the eye cannot resolve fine detail from meters away. Two format rules do not bend with size. Avoid JPG for QR codes: its compression blurs the sharp module edges a scanner depends on. If you must enlarge a PNG, use nearest-neighbor scaling (sometimes called "hard edges" or "no smoothing") by a whole number such as 2×, 3×, or 4×, which keeps every module a crisp block instead of a soft blur. Better still, import the SVG and re-export at the required resolution rather than stretching a small PNG.</p>

<h2>Don't forget the quiet zone</h2>

<p>Leave a blank margin around the code <a href="http://www.iso.org/standard/83389.html">at least 4 modules wide</a> on every side, as specified in ISO/IEC 18004. Crowding it with text or graphics is one of the top reasons codes fail — more in <a href="/blog/why-is-my-qr-code-not-working/">why your code won't scan</a>. A module is one small square of the grid, so the physical margin depends on the code: count the squares across your code, work out how wide one module is, and leave four of those widths clear on every side. For a 2 cm code with 29 modules across, one module is about 0.7 mm, so you need about 2.8 mm of clear space all round — and that margin must be the same light color as the code's background, not a frame, a crop mark, or a fold.</p>

<p>The quiet zone is also where layout software quietly sabotages you. A design tool that crops an image to its visible pattern, a printer's bleed that trims the margin, or a frame drawn tight around the code can each eat the margin after you set it correctly. Check the margin on the final artwork, not just in the generator, and remember the margin is part of the footprint — a 2 cm code with its quiet zone needs more than 2 cm of clear space on the card.</p>

<h2>On screens: pixels instead of centimeters</h2>

<p>Print sizes do not translate directly to screens, because a screen's physical size varies. The working rule of thumb for screen display is not to go below about 200 × 200 pixels, with more being better — people usually hold their phones at arm's length when scanning, and a small on-screen code competes with glare and room light. For slides and projected displays, the distance rule takes over: estimate how far the furthest viewer sits, divide by ten, and make the projected code at least that wide. A code that looks generous on your laptop can be tiny on a hall wall,.</p>

<h2>Materials and surfaces: where good sizes go wrong</h2>

<p>Size is only one part of a reliable printed code, and the surface can undo a perfect size. Glossy laminates cause glare; a matte finish is usually safer for signs and menus, and a table code under a restaurant spotlight should be tested under that spotlight, not office lighting. Curved surfaces distort the grid — a code wrapped around a small bottle reads worse than the same code flat, so use a flat panel or print larger. Textured card and thermal receipt paper blur fine detail, which is why receipts need short URLs and a test on the actual printer. On dark stock, print the code on a white patch. Outdoors, print larger and use a higher error-correction level.</p>

<h2>Common print mistakes</h2>

<ul>
<li><strong>Printed too small.</strong> The code looks fine in the design file and fails in the hand, because each module is a fraction of a millimeter wide. Size up or shorten the content.</li>
<li><strong>Stretched or squashed.</strong> Dragging one corner without locking proportions distorts the finder patterns — the three large corner squares scanners use to locate the code.</li>
<li><strong>Upscaled from a small, blurry PNG.</strong> Normal smoothing turns crisp edges into grey blur. Use SVG, or nearest-neighbor scaling.</li>
<li><strong>Cropped quiet zone.</strong> Text, borders, or a tight crop running into the margin stops the scanner finding the code's edges.</li>
<li><strong>Low contrast.</strong> Brand colors that look elegant on screen can fail in print, where ink and paper shift the tones. Dark code on a light background, always — and check the printed proof.</li>
<li><strong>Logo too big for the print size.</strong> A logo code needs a 3 × 3 cm minimum in print, not 2 × 2 cm, and the logo should stay under about 30% of the code area. The <a href="/blog/add-logo-to-qr-code/">logo guide</a> covers the trade-off.</li>
<li><strong>Never proofed.</strong> The most expensive mistake, because it turns every item above from a fixable detail into a reprint.</li>
</ul>

<h2>Preflight checklist before you send the file</h2>

<ol>
<li><strong>Format:</strong> SVG for professional print and anything large; PNG at 1024 or 2048 px if the printer needs raster, never JPG.</li>
<li><strong>Size:</strong> the larger of the 2 cm minimum and distance ÷ 10, rounded up, checked against the real scanning distance.</li>
<li><strong>Density:</strong> short URL, only the needed fields, and a larger print if the grid looks dense.</li>
<li><strong>Quiet zone:</strong> at least four modules of clear, light margin on all four sides, confirmed on the final artwork.</li>
<li><strong>Contrast:</strong> dark modules on a light background, verified on the printed proof, not just the screen.</li>
<li><strong>Finish and surface:</strong> matte where glare is a risk, flat panels on curved objects, a white patch on dark stock.</li>
<li><strong>Proof:</strong> one copy at final size, on the final material, scanned with more than one phone in the lighting where it will be used, plus a check that the destination opens on mobile data.</li>
</ol>

<h2>The honest comparison: print versus screen, static versus dynamic</h2>

<p>Print and screen reward opposite habits. On screen, a code can be regenerated in seconds and tested instantly, so a small or experimental code costs nothing to fix. In print, every fix is a reprint, which is why print demands the conservative choices: SVG over PNG, the larger size, the full quiet zone, the proof scan. Treating a print file like a screen file — export small, crop tight, skip the proof — is how good designs become dead squares on a finished run.</p>

<p>The static-versus-dynamic choice matters in print for a different reason: what happens after the run. A static code encodes its destination directly, needs no sign-up, carries no watermark, and never expires — ideal for a fixed destination such as a homepage or a product manual. A dynamic code encodes a redirect, so its destination can be edited after printing and it carries scan statistics; that is the right choice when the destination may change, or when you need to know whether the size and placement you chose are working. What a dynamic code cannot do is rescue a badly sized print: editing the destination does not fix modules too small to read. Size the print correctly first.</p>

<p>One more comparison is worth making plainly, because it decides budgets: a bigger code is nearly free, and a reprint is not. Going from 2 cm to 3 cm on a business card costs nothing in print; reprinting a thousand cards costs the whole run. When the size decision is close, the larger size is almost always the cheaper choice — and a code with unlimited scans behind it stays useful however popular it becomes.</p>

<p>Make yours in the <a href="/qr-code-with-logo/">free generator</a> — any of the 17 types, PNG up to 2048 px or SVG, static codes with no sign-up and no expiry, or a free dynamic code you can edit after printing. If the code carries your logo, read the <a href="/blog/add-logo-to-qr-code/">logo guide</a> first: a logo code needs the bigger minimum this table already assumes.</p>""",
  'date': 'October 14, 2026', 'updated': "November 3, 2026", 'dateModified': "2026-11-03",
  'datePublished': '2026-10-14',
  'desc': 'How big should a QR code be in print? Minimum sizes for business cards, flyers, and '
          'posters — plus the 1:10 distance rule, resolution, and quiet-zone rules that keep codes scannable.',
  'faq': [
  ('What is the minimum size for a printed QR code?', 'As a rule of thumb, 2 × 2 cm (0.8 × 0.8 in). Smaller codes fail on many phones, especially for data-heavy codes like vCards.'),
  ('How big should a QR code be on a poster?', 'Use the 1:10 rule of thumb: the code width should be at least one-tenth of the expected scanning distance. A poster scanned from 5 meters needs a 50 cm code.'),
  ('PNG or SVG for print?', 'SVG is best — it scales infinitely with no quality loss. If your printer needs raster, export PNG at 2048 px. Never use JPG: its compression blurs the module edges a scanner depends on.'),
  ('How much margin does a QR code need?', 'A quiet zone at least 4 modules wide on every side, in the same light color as the code background, as specified in ISO/IEC 18004. For a 2 cm code with 29 modules across, that is about 2.8 mm all round.'),
  ('How do I work out the size for a scanning distance?', 'Divide the distance by ten and round up, never below the 2 cm minimum. A code scanned from 2 meters needs at least 20 cm; from 10 meters, at least 1 meter.'),
  ('Does a longer URL need a bigger print?', 'Yes. More data means more modules, and more modules at the same print size means smaller modules that are harder to read. Use a short, clean URL, or a dynamic code whose short redirect destination you can edit after printing.'),
  ('What size should a QR code be on a screen?', "As a rule of thumb, not below about 200 × 200 pixels. For slides and projected displays, apply the 1:10 ratio to the projected width and the furthest viewer's distance."),
  ('Why does my printed code fail when the screen version scans?', 'Common causes are a cropped quiet zone, glare on gloss laminate, ink spread on textured stock, a stretched grid, or a PNG upscaled with smoothing. Proof one copy at final size, on the final material, and scan it with more than one phone before the full run.'),
],
  'h1': 'How <span class="hl hl-mint">big</span> should a printed QR code be?',
  'lede': 'The short answer: at least 2x2 cm, at 300 dpi, with a clear margin. The longer answer — '
          'with the distance rule of thumb printers actually use — is below.',
  'mascot': 'batch',
  'slug': 'qr-code-print-size-guide',
  'cta': {'title': 'Try it yourself — free', 'text': 'Everything in this article works in the FreeQrly studio right now. Static codes, all 17 content types, PNG and SVG export.', 'href': '/#studio', 'btn': 'Open the studio'},
  'title': 'QR Code Print Size Guide: Business Cards to Posters | FreeQrly',
  'sources': [
  ('http://www.iso.org/standard/83389.html', 'ISO/IEC 18004:2024', 'The QR Code symbology specification, published 2024-08 (Edition 4). Supports the four error-correction levels (L 7%, M 15%, Q 25%, H 30%) and the 4-module quiet zone.'),
  ('https://www.qrcodebarn.com/blog/qr-code-size-guide.html', 'QRCodeBarn — QR Code Size Guide: How to Resize a QR Code Properly', 'Published 13 October 2026. Supports the 2 cm practical minimum, the distance ÷ 10 rule of thumb with worked examples, the 4-module quiet zone (2.8 mm on a 2 cm, 29-module code), 300 DPI raster guidance, the 600 px = about 5 cm at 300 DPI check, and the 29 × 29 to 37 × 37 level M/H example.'),
  ('https://www.adobe.com/uk/creativecloud/photography/discover/image-resolution.html', 'Adobe — What Does Resolution Mean? Image Resolution Guide', 'No publication date shown on the page; accessed 2026-11-03. Supports 300 DPI as the minimum for best print results and 150 DPI as workable for large prints viewed from a distance.'),
  ('https://pretty-qr.com/blog/qr-design-best-practices', 'Pretty QR — QR Code Design Rules: 10 Rules for Beautiful Codes That Still Scan', 'No publication date shown on the page; accessed 2026-11-03. Supports the 2 cm print minimum, scan distance ÷ 10, the 4-module quiet zone, and the 200 × 200 px minimum for screens.'),
  ('https://www.notraqr.com/qr-codes-technical.html', 'NoTraQR — QR Code Technical Guide: Error Correction, File Formats and Barcode Comparison', 'No publication date shown on the page; accessed 2026-11-03. Supports the error-correction table, the 2 cm / 3 cm rules of thumb, D/10 sizing, and testing on at least two devices (iOS and Android).'),
]},
 {'body': '\n'
          '<h2>1. The menu code</h2>\n'
          '<p>Link it to your online menu — your website, a <a href="/pdf-qr-code/">PDF</a>, or your Google Business menu. '
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
          '<h2>Setup checklist</h2>\n'
          '<ul>\n'
          '<li>Menu code: one per table, or a single framed code at the entrance.</li>\n'
          '<li>Review code: on the receipt, the table tent, and the takeout bag.</li>\n'
          '<li>WiFi code: one on each table.</li>\n'
          '<li>Laminate table codes, print at least 3x3 cm, and keep contrast high.</li>\n'
          '</ul>\n'
          '<h2>What it costs</h2>\n'
          '<p>Nothing. These are static codes — no subscriptions, no scan limits, no "pro plan" to '
          "unlock the menu link. Print them once and they work for years. That's the whole "
          'pitch.</p>\n',
  'date': 'October 14, 2026',
  'datePublished': '2026-10-14',
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
          'Red flags:</p>\n'
          '<ul>\n'
          '<li>The site asks for your email before generating.</li>\n'
          '<li>It mentions "scan analytics" or talks about "campaigns".</li>\n'
          '</ul>\n'
          '<p>A truly free static generator needs none of that.</p>\n'
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
  'date': 'October 14, 2026',
  'datePublished': '2026-10-14',
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
  'date': 'October 14, 2026',
  'datePublished': '2026-10-14',
  'desc': 'Scan a QR code online in seconds: use your camera or upload a photo or screenshot. '
          'Decoded in your browser, so nothing is ever uploaded. No app, no sign-up.',
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
             'Go to the <a href="/scan/">FreeQrly scanner</a> — no app to install, no account needed.'),
            ('Use your camera or upload',
             'Point your camera at the code, or upload a photo or screenshot that contains one.'),
            ('Get the result instantly',
             'The decoded text or link appears immediately. Links get an Open button; everything '
             'else gets Copy.')],
  'lede': "Many online QR scanners ask you to upload your image to their server. Ours doesn't — the "
          'code is decoded right in your browser. Camera or image upload, free forever.',
  'mascot': 'scanner',
  'slug': 'scan-qr-code-online',
  'title': 'Scan Any QR Code Online Free — No App, No Upload | FreeQrly',
  'sources': [('https://github.com/cozmo/jsQR', 'jsQR on GitHub', 'A pure JavaScript QR code reading library. Takes in raw images and locates, extracts and parses any QR code found within.')]},
 {'body': """<p><strong>The short answer: you do not need a second phone, and you do not need to point a camera at your own screen.</strong> A QR code that arrives as a photo, a screenshot, a message attachment, or a picture on a web page can be read from the image itself. On an iPhone, open the image in Photos and press and hold the code. On Android, open it in Google Photos and tap the Lens button. On a computer, upload the image to a decoder that reads it in your browser, such as <a href="/scan/">FreeQrly's scanner</a>. The rest of this guide is about choosing the right one of those paths for where your image actually lives, cleaning up a stubborn image before you give up on it, and keeping private images private while you do it.</p>

<p>The core distinction is simple. A live camera reads a pattern in front of it. An image reader reads a pattern already stored as pixels. The two jobs look similar, but they use different tools, and reaching for the live camera when the code is already a file is the most common reason people conclude a code "cannot be scanned" when it can. If the code is in your hand as a file, start with an image reader, not with a camera.</p>

<h2>Where the image lives decides the method</h2>
<table>
<tr><th>Where the code is</th><th>First method to try</th><th>What you need</th></tr>
<tr><td>A photo or screenshot on your iPhone</td><td>Photos, press and hold the code</td><td>Nothing to install</td></tr>
<tr><td>A photo or screenshot on your Android phone</td><td>Google Photos, Lens button</td><td>Google Photos and Lens, already on most Android phones</td></tr>
<tr><td>A photo on a Samsung Galaxy</td><td>Gallery with Bixby Vision, or the Quick Settings scanner's gallery icon</td><td>Nothing to install</td></tr>
<tr><td>An image on a computer, or a code on a web page</td><td>A browser decoder with image upload</td><td>The saved image file, or a screenshot of the page</td></tr>
<tr><td>An image someone sent you in a chat or email</td><td>Save it first, then use the method for your phone</td><td>The saved file, so you are not reading inside a chat bubble</td></tr>
<tr><td>A code inside a video</td><td>Pause on a sharp frame, screenshot it, then read the screenshot</td><td>A still frame where the code is in focus and fully visible</td></tr>
</table>

<h2>The basic steps, whichever device you use</h2>
<ol>
<li><strong>Get the image into a form a reader can open.</strong> Save an attachment, take a screenshot of a code shown on screen, or download the picture from the page. A reader needs a file or an open image, not a thumbnail in a chat list.</li>
<li><strong>Open the image full-screen.</strong> Readers work on what they can see. A code shrunk to a thumbnail in a message thread is a much smaller target than the same code opened full-screen, and opening it full-screen costs nothing.</li>
<li><strong>Use your phone's built-in image reader first.</strong> On iPhone, Photos; on Android, Google Photos with Lens; on Samsung, Gallery. These readers run on the device and need no upload, which matters for the privacy section below.</li>
<li><strong>Read the preview before you open anything.</strong> The same rule as live scanning applies, with one extra reason: an image forwarded to you has passed through someone else's hands, and the preview is your check that the code leads where the sender said it does.</li>
<li><strong>If the first reader finds nothing, clean the image and try again</strong> — crop, brighten, and retry — before you conclude the code is unreadable. The cleaning steps below rescue more images than any change of reader.</li>
</ol>

<h2>On iPhone: Photos, press and hold</h2>
<p>Open the photo or screenshot in the Photos app and press and hold the QR code itself. The phone detects the code in the image and offers the link or action, which you tap after reading the preview. That is the whole method, and it covers the most common cases: a screenshot a friend sent you, a photo of a poster you took yesterday, a boarding pass saved to your camera roll, a code inside an email that you screenshotted rather than saved. If pressing and holding does nothing, check two things before anything else: that you are pressing on the code itself rather than on empty space near it, and that the code is fully visible in the image rather than cut off at an edge. A code cropped by the screenshot's edge is the image equivalent of a code cropped by the camera's frame, and no reader can reconstruct the missing corner.</p>
<p>When the code is not a saved photo at all — it is showing in a message, an email, or a web page on the same phone — take a screenshot first, then open the screenshot in Photos and press and hold the code. This two-step dance feels clumsy the first time and becomes automatic quickly, and it is the answer to the question that confuses the most people: you cannot point your own camera at your own screen, so you capture the screen and read the capture instead. Live codes in front of you are covered in <a href="/blog/how-to-scan-qr-code-on-phone/">the phone scanning guide</a> and <a href="/blog/how-to-scan-a-qr-code/">the general scanning guide</a>.</p>

<h2>On Android: Google Photos and Lens</h2>
<p>Open the image in Google Photos and tap the Lens button. Lens analyses the image, finds the code, and shows the decoded link or action, which you tap after reading the preview. Lens reads pixels, not sources, so it works for a saved photo, a screenshot, or a downloaded image alike. If you do not see a Lens button, look for it in the image's options or share menu. You can also reach Lens from the Google app by tapping its Lens icon and choosing the image.</p>
<p>On a Samsung Galaxy, there is an additional built-in path. Open the image in the Samsung Gallery app and tap the Bixby Vision button; the phone reads the image and offers to open the link or copy it. Samsung's support guide, updated in October 2026, describes the same path through the Quick Settings scanner: open Quick Settings, tap Scan QR code, tap the gallery image icon at the bottom, choose the photo, and confirm. Either door leads to the same result, so use whichever you find first. If your phone is neither a Samsung nor a phone with Google Photos, the fallback is the same as on a computer: save the image and upload it to a browser decoder, which is covered next.</p>

<h2>On a computer: upload to a browser decoder</h2>
<p>A computer has no built-in image reader for QR codes in the way a phone does, so this is where a browser decoder earns its keep. Save the image — or take a screenshot of the code on the web page, in the document, or in the presentation — and upload it to a decoder. <a href="/scan/">FreeQrly's scanner</a> decodes the image in your browser, so the image never leaves the page; that detail matters most exactly when the screenshot contains something private, which is often, and the privacy section below explains why. The decoder returns the raw decoded content, with a link button for links and a copy button for everything else. Read the decoded link before you open it, just as you would read a phone's preview.</p>

<h2>Images other people send you</h2>
<p>A code sent to you in a chat, an email, or a social post deserves one extra habit: save it before you scan it. Reading inside a chat bubble means reading a small, possibly compressed version of the image, inside an app that may not offer a reader at all. Saving the image gives you the full file, opens it in Photos or Google Photos where the reader lives, and lets you crop and brighten it if the first attempt fails. It also gives you a moment to think: a code arriving from a sender you do not know, with an urgent story attached, is the image version of the unexpected message the safety guides warn about. Save it, read the preview, and only then decide.</p>

<h2>Cleaning up a stubborn image</h2>
<p>Most unreadable images are not unreadable codes; they are readable codes buried in a bad picture. Work through these fixes in order, and retest after each one, because the first fix that works saves you the rest.</p>
<ul>
<li><strong>Crop tight around the code.</strong> Cut away the chat window, the surrounding text, the table, and the background. Keep the quiet zone — the blank margin around the code — inside the crop.</li>
<li><strong>Straighten and flatten.</strong> A code photographed at an angle, on a curved surface, or in perspective is stretched in the image. If your photo app offers a straightening tool, use it lightly; otherwise retake the photo straight-on.</li>
<li><strong>Brighten, do not sharpen blindly.</strong> Raising brightness or contrast can rescue a code shot in dim light. Heavy sharpening can invent edges that are not there, so brighten first and sharpen only a little.</li>
<li><strong>Try the original file.</strong> If you have been working from a compressed chat copy, go back to the original photo, the original download, or a fresh screenshot. Editing cannot restore detail that compression removed.</li>
<li><strong>Try a different reader.</strong> If Photos finds nothing, try Lens; if Lens finds nothing, try a browser decoder; if a browser decoder finds nothing, try the other phone in the house. A code on the edge of readability sometimes passes one reader and not another. A code that no reader can read from the original file should be replaced by the sender.</li>
</ul>

<h2>Special cases: video stills, multiple codes, and tiny codes</h2>
<p><strong>A code inside a video</strong> is a screenshot problem in disguise: pause on a frame where the code is sharp, fully visible, and not in motion, screenshot that frame, and read the screenshot. <strong>Multiple codes in one image</strong> — a poster, a page of tickets — should be read one at a time: crop to a single code, read it, and repeat, since a reader shown several codes will typically pick one, and it may not be the one you wanted. <strong>A tiny code in a large image</strong> may simply be too few pixels to resolve; crop to it, and if the modules still blur together when you zoom in, the image does not contain enough detail — ask for a closer photo, a higher-resolution download, or a fresh code.</p>

<h2>Privacy: what your screenshot contains besides the code</h2>
<p>Screenshots and photos almost always contain more than the QR code. A screenshot of a chat contains the conversation around the code. A photo of a ticket contains the name, the booking reference, and the barcode next to the code. A screenshot of a payment page contains amounts and account details. Before you upload any such image to a decoder, look at what else is in the frame, and crop it out. Cropping is not just a readability fix; it is a privacy fix, and it costs the same few seconds either way.</p>
<p>The deeper question is where the image goes. Many online decoders upload your image to their server to read it, which means a stranger's server receives your screenshot — chat, ticket, and all — just to read one code. A decoder that reads the image in your browser, like <a href="/scan/">FreeQrly's scanner</a>, never sends the image anywhere; the reading happens on your device, in the page, and the image stays with you. Prefer a local decoder for any image you would not email to a stranger, and crop before you upload even then.</p>

<h2>The honest comparison: built-in readers, browser decoders, and scanner apps</h2>
<p>For a code in an image, three kinds of tool compete, and the honest ranking depends on the image, not on the tool's marketing. Built-in readers — Photos on iPhone, Lens on Android, Gallery on Samsung — are the best first choice for a saved image on your own phone: they are already installed, they run on the device, and they need no upload. Browser decoders are the best choice on a computer, and the best backup on a phone when the built-in reader fails, provided the decoder reads locally in the browser rather than uploading your image. Scanner apps are the weakest default for this job: they add an install, a permission screen, and often ads or an account, in exchange for a capability your phone already has.</p>
<p>One more honest note: no reader rescues a code whose detail is gone. A heavily compressed forward, a blurred video frame, a code cut off at the edge of a screenshot — these are missing-data problems, not reader problems, and switching readers five times will not restore what was never captured. The fix for missing data is a better original, and asking the sender for one is faster and more honest than trying every decoder on the internet. Readers are good at finding codes in images; they are not good at inventing codes that are not there.</p>

<h2>When the image reads but the destination fails</h2>
<p>Sometimes the image reads perfectly and the result still disappoints: a dead link, a moved page, a form that no longer exists, a ticket that has already been used. That is not a scanning failure; it is a destination failure, and the fix belongs to whoever issued the code. A static code holds its destination directly, so if the destination is gone, the code has nothing to say — and if the destination moved, only the issuer can point the code somewhere new, which is exactly what a dynamic code is for: it stays editable after printing, with scan statistics, under a free account. For codes that will not read at all, see <a href="/blog/why-is-my-qr-code-not-working/">why your QR code won't scan</a> and <a href="/blog/why-is-my-qr-code-blurry/">why your QR code is blurry</a>. If the link is dead, ask the sender for a fresh code rather than rescanning.</p>

<h2>Make a code worth sending as an image</h2>
<p>The other side of this guide is worth a paragraph, because the codes people struggle to read from images are often codes that were made badly in the first place. If you are the one sending a code as an image, send the original file, not a screenshot of a screenshot; keep the code large in the frame, with its quiet zone intact and dark modules on a light background; and test it by reading it back from the image yourself before you send it. FreeQrly's generator covers 17 types, and a static code made there is free with no sign-up, no watermark, and no expiry, so a test code costs nothing. If the code will be forwarded or reused, consider a dynamic code instead: it stays editable if the destination changes, reports scan statistics, and is free for 20 codes, currently with unlimited availability during the promotional period, and with unlimited scans. For many codes at once, <a href="/batch-qr-code/">batch generation</a> makes one code per link. Send a clean original, and the person on the other end will not need this guide's cleaning section at all.</p>""",
  'date': 'October 14, 2026', 'updated': "November 3, 2026", 'dateModified': "2026-11-03", 'sources': [
  ('https://www.samsung.com/uk/support/mobile-devices/how-to-scan-qr-code-on-your-galaxy-phone-or-tablet/', 'Samsung Support: How to scan QR codes on your Samsung phone', "ADDED (the original post had no sources field at all). Updated October 6, 2026 (shown on the page, verified by opening it 2026-11-03). Supports: Gallery with Bixby Vision for a saved picture, and the Quick Settings Scan QR code tile's gallery image icon for choosing a photo and extracting its link."),
],
  'datePublished': '2026-10-14',
  'desc': 'Your QR code is in a photo, not in front of your camera. Here is how to decode it on '
          'iPhone, Android, and PC — free, no app needed.',
  'faq': [
  ('How do I scan a QR code from a screenshot on iPhone?', 'Open the screenshot in the Photos app and press and hold the QR code itself. The phone detects the code in the image and offers the link or action; read the preview before you tap it.'),
  ('How do I scan a QR code from an image on Android?', 'Open the image in Google Photos and tap the Lens button. Lens reads the code inside the image and shows the decoded link or action. On a Samsung Galaxy you can also open the image in Gallery and tap the Bixby Vision button.'),
  ('How do I scan a QR code from an image on a computer?', "Save the image, or screenshot the code on the page, and upload it to a browser decoder. Prefer a decoder that reads the image in your browser, so the image is never sent to a server — FreeQrly's scanner works that way."),
  ('Someone sent me a QR code in a chat. How do I scan it?', 'Save the image first, then open the saved file in Photos or Google Photos and use the built-in image reader. Reading inside a chat bubble means reading a smaller, possibly compressed copy, and the chat app may offer no reader at all.'),
  ("Why can't the decoder read my picture?", 'Usually the code is cut off at an edge, too small in the frame, blurred, or shot at an angle. Crop tight around the code while keeping its quiet zone, brighten if it is dim, try the original file instead of a compressed forward, and try a different reader. If no reader can read the original file, ask the sender for a fresh code.'),
  ('What if one image contains several QR codes?', 'Crop to a single code and read it, then repeat for the next. A reader shown several codes at once will typically pick one, and it may not be the one you wanted.'),
  ('Is it safe to upload a screenshot to an online decoder?', 'Crop out everything except the code first — screenshots often contain chats, tickets, or payment details beside the code. Prefer a decoder that reads locally in your browser, so the image is never uploaded to a server.'),
],
  'h1': 'Scan a QR code <span class="hl hl-honey">from a picture</span>',
  'howto': [
  ('Get the image into a form a reader can open', 'Save an attachment, take a screenshot of a code shown on screen, or download the picture from the page.'),
  ('Open the image full-screen', 'Readers work on what they can see, so open the image full-screen rather than reading a thumbnail in a message thread.'),
  ("Use your phone's built-in image reader first", 'On iPhone, open the image in Photos and press and hold the code. On Android, open it in Google Photos and tap the Lens button. On Samsung, Gallery with Bixby Vision works too.'),
  ('Read the preview before you open anything', 'Check that the decoded link or action matches what the sender said the code leads to, especially for a forwarded image.'),
  ('If the first reader finds nothing, clean the image and try again', 'Crop tight around the code while keeping its quiet zone, brighten if it is dim, try the original file instead of a compressed forward, and try a different reader before concluding the code is unreadable.'),
],
  'lede': "The code is in a photo, not in front of your camera. Here's how to decode it on iPhone, "
          'Android, and desktop — no app required.',
  'mascot': 'scanner',
  'slug': 'scan-qr-code-from-image',
  'cta': {'title': 'Try it yourself — free', 'text': 'Everything in this article works in the FreeQrly studio right now. Static codes, all 17 content types, PNG and SVG export.', 'href': '/#studio', 'btn': 'Open the studio'},
  'title': 'How to Scan a QR Code from a Picture, Photo, or Screenshot | FreeQrly'},
 {'body': """<p>Check-in lines, ticket chaos, “where are the photos?” — a few well-placed QR codes solve the recurring event headaches. The trick is not the code itself; it is matching each code to one moment in the guest's journey, and choosing static or dynamic for each moment deliberately. A code on the invitation does a different job from a code on the exit sign, and printing the wrong kind in the wrong place is how events end up with a wall of codes nobody scans.</p>
<p>Start from the guest, not from the technology. A guest meets your event in roughly five moments: they hear about it, they commit, they arrive, they take part, and they leave. Each moment has one question — when is it, am I in, where do I go, what is happening, what did I think — and each question has a code that answers it in one scan.</p>
<h2>The event code map</h2>
<table>
<tr><th>Guest moment</th><th>The code</th><th>Where it goes</th><th>Static or dynamic</th></tr>
<tr><td>Before: hearing about it</td><td>Add-to-calendar code (event type)</td><td>Invitation, save-the-date, email</td><td>Static — the date, time, and venue rarely change, and a keepsake invitation should keep working</td></tr>
<tr><td>Before: committing</td><td>RSVP or registration form</td><td>Invitation details card, event page</td><td>Static if the form link is final; dynamic if the form might move</td></tr>
<tr><td>Before: tickets</td><td>Ticket validation page, one code per ticket</td><td>Ticket email, printed ticket</td><td>Dynamic when a ticket can be transferred or cancelled; static only for a simple, non-transferable ticket</td></tr>
<tr><td>Arrival: check-in</td><td>Check-in form or “I'm here” page</td><td>Confirmation email, entrance sign</td><td>Dynamic if the check-in page or the day's schedule might change</td></tr>
<tr><td>During: agenda and speakers</td><td>Agenda page, speaker bios</td><td>Program, session signs, slide footers</td><td>Dynamic — agendas change, speakers drop out, rooms move</td></tr>
<tr><td>During: connectivity</td><td>Venue WiFi</td><td>Entrance and table signage</td><td>Static — the network rarely changes on the day</td></tr>
<tr><td>During: photos</td><td>Shared photo album</td><td>Table cards, photo wall, closing slide</td><td>Dynamic if you might switch albums; static if the album is set</td></tr>
<tr><td>After: feedback</td><td>Short feedback form</td><td>Exit signage, closing slide, thank-you email</td><td>Dynamic if you reuse the sign for the next event</td></tr>
</table>
<p>The pattern in that table is the whole strategy: anything that might change after printing goes dynamic, and anything fixed goes static. A static code never expires — right for a keepsake invitation, wrong for an agenda that will be edited the morning of the event.</p>
<h2>Before the event: invitations, calendar, and RSVP</h2>
<p>The invitation is where most event codes fail, because organizers print a code that leads to a homepage and expect guests to find the RSVP form themselves. Link the code to the form, not to the site. Build your RSVP form first — a simple form tool works fine — then generate the code, print it on the invitation suite, and guests scan, tap, and respond. No stamps, no lost reply cards, no deciphering handwriting. After the responses roll in, the form tallies them automatically, meal choices included; export to a sheet, share it with the caterer, and the admin is done.</p>
<p>Pair the RSVP code with an add-to-calendar code, the most underused event code there is. One scan drops the event — title, start and end time, location — straight into the guest's calendar on both iPhone and Android. Print it on the invitation, and one less step sits between the invite and the calendar, which may mean fewer no-shows. A wedding invitation suite is the classic case: the RSVP code goes on the details card, the calendar code beside it, and the photo album code waits for the table cards. The same invitation trick works for holiday parties — see the <a href="/christmas-qr-code/">Christmas QR code generator</a>.</p>
<p>Word the invitation code the way you would word an instruction to a stranger. Print exactly what to do next to the code: “Scan to RSVP by June 1st.” Older guests may need the nudge, and the truly scan-averse still need a phone number on the invitation. Every code should sit beside a short printed alternative — a link or a phone number — so a guest with a dead battery, no signal, or no camera phone is not locked out.</p>
<h2>Tickets: one code per ticket, and what that really means</h2>
<p>For ticketed events, link each ticket to its own validation page rather than printing one shared code on every ticket. A shared code cannot tell one ticket from another, so it cannot catch a ticket scanned twice — and a screenshot of a shared code is a free ticket for anyone who receives it.</p>
<p>Batch generation turns a list of ticket links into a set of codes in one download. Name the files by ticket or guest and test-scan a sample before sending. At the door, the check-in team needs one thing above all: a fallback. Phones die, screens crack, and screenshots arrive too dim to read. Keep a printed guest list at the entrance, and train the door team to check a name when a code will not read.</p>
<h2>At the door: check-in without the clipboard queue</h2>
<p>Put a code on the confirmation email linking to a check-in form, or to a simple “I'm here” page. Guests scan at the door instead of spelling their names for a volunteer with a clipboard. For a small event, that form can be as simple as a name field and a submit button.</p>
<p>Three details make door check-in work. First, print the entrance code large and at chest height, where a guest holding a phone naturally points it — not on a table where people queue behind it, and not on a swinging door. Second, give the door team a second way in: a printed link and the guest list on paper. Third, decide before doors open what happens when a code has already been used. A ticket scanned twice is either a returning guest or a screenshot doing the rounds; the door team needs a rule, not a debate in front of a queue.</p>
<h2>During the event: agenda, speakers, WiFi, and the photo wall</h2>
<h3>Agenda and speaker bios</h3>
<p>A code on the program — or in the footer of each session slide — linking to the live agenda page saves you from reprinting the program every time a session moves rooms. This is the strongest case for dynamic codes at an event: the printed pattern stays the same while the destination changes from your Dashboard. Speaker bios work the same way.</p>
<h3>Venue WiFi</h3>
<p>Attendees will ask for WiFi. A <a href="/wifi-qr-code/">WiFi QR code</a> on signage connects them in one scan — no password spelling over loud music, no queue at the help desk. Put it where people first look for it: the entrance, the registration desk, and the tables, not only on a slide that disappears after thirty seconds. One honest trade-off: anyone who photographs the printed code can join the network, so treat a venue WiFi code like a guest key.</p>
<h3>The shared photo album</h3>
<p>Every event has the same problem: the photos scatter across fifty phones, and the organizer spends the next week begging for them. A code linking to a shared album on table cards fixes it — guests upload their shots in one tap, all night, into one place. Print it on the table cards, on a photo wall sign, and on the closing slide, where guests see it when they take a photo. Check the album's sharing settings before the event: anyone with the link can usually add to a shared album. If the album is meant for guests only, keep the code inside the room rather than on a public event page.</p>
<h2>After the event: feedback while it is still fresh</h2>
<p>A code linking to a short feedback form on the exit signage or the closing slide catches guests while the event is still fresh, instead of competing with a follow-up email days later that most guests will ignore. Keep the form to two questions: one rating and one open box for what to change. A ten-question survey at the exit gets abandoned; a two-question form gets answered on the walk to the car. The thank-you email the next day can carry the same code again, plus the photo album link, for guests who left too quickly.</p>
<p>After the event is also when the static-versus-dynamic choice pays off a second time. A dynamic code on a reusable sign can be repointed at the next event's feedback form, so the sign never needs reprinting. A static code on a keepsake keeps working for years as a memento. Decide which kind of afterlife each sign should have before you print it.</p>
<h2>Static or dynamic: the before-and-after difference</h2>
<p>The honest comparison is not “dynamic is better.” The two kinds fail differently, and an event is exactly where both failure modes show up:</p>
<table>
<tr><th></th><th>Static</th><th>Dynamic</th></tr>
<tr><td><strong>What it holds</strong></td><td>The destination itself, inside the pattern</td><td>A short link that redirects to the destination</td></tr>
<tr><td><strong>If the destination changes after printing</strong></td><td>The code breaks; reprint</td><td>Edit the destination in the Dashboard; every printed copy follows</td></tr>
<tr><td><strong>If you want to know what got scanned</strong></td><td>Nothing is recorded; static codes never report home</td><td>Scan statistics show totals, timing, and breakdowns — see <a href="/blog/dynamic-qr-code-statistics/">what dynamic QR code statistics tell you</a></td></tr>
<tr><td><strong>Needs an account</strong></td><td>No — free, no sign-up, no watermark, never expires</td><td>Yes — free sign-in, 20 codes on the free account, unlimited scans during the limited-time promotion</td></tr>
<tr><td><strong>Best event uses</strong></td><td>Invitations, calendar codes, WiFi, keepsakes</td><td>Agenda, check-in, feedback, reusable signage, anything that might move</td></tr>
<tr><td><strong>Failure mode</strong></td><td>Silent: a changed link means a dead code nobody reports</td><td>Dependent: the redirect service must stay up for the code to work</td></tr>
</table>
<p>A practical rule: use dynamic codes for everything the event team controls on the day — agenda, check-in, feedback — and static codes for everything the guest keeps — invitations, calendar entries, photo albums that should outlive the event. If anyone might need to change where a code points after it is printed, make it dynamic.</p>
<h2>Printing and testing: the unglamorous part that decides everything</h2>
<p>Event codes get scanned in chaotic lighting by hurried people. Print for that reality, not for a design mockup:</p>
<ul>
<li><strong>Go bigger than you think.</strong> The <a href="/blog/qr-code-print-size-guide/">1:10 distance rule of thumb</a> is a good starting point: a code scanned from a metre away needs to be roughly ten times larger than one scanned from ten centimetres. Size each one for its actual distance.</li>
<li><strong>Keep contrast high and the margin clear.</strong> Dark ink on a light background, with a clear quiet margin around the code. A code printed over a busy photo, or in brand colours with low contrast, is the most common reason an otherwise fine code fails at an event.</li>
<li><strong>Print for damage.</strong> Tickets get folded, table cards get spilled on, outdoor signs get rained on. The QR standard, ISO/IEC 18004:2024, defines four error-correction levels — L, M, Q, and H — recovering 7%, 15%, 25%, and 30% of the symbol's codewords respectively, so a code with a higher level keeps scanning after more of it is damaged. Use a higher level for anything guests will handle, and keep logos small and centred so they do not eat into that margin.</li>
<li><strong>Test on both iPhone and Android before printing a hundred of anything.</strong> The built-in camera on modern phones reads codes with no app needed — Apple's support page describes opening Camera or the Control Center scanner, holding the phone so the code appears in frame, and tapping the link that appears — but camera behaviour varies between models, and a code that scans on one phone in bright light may fail on another in a dim hall. Test the actual print, at the actual size, in lighting like the venue's.</li>
<li><strong>One code per sign, with a label.</strong> Two codes side by side make guests hesitate and cameras pick the wrong one. Label every code with what it does — “Scan for WiFi,” “Scan for photos” — because a bare code at an event is a code guests walk past.</li>
</ul>
<p>One more number worth knowing before you plan around phones: in Pew Research Center's 2026 survey of United States adults, 91% said they owned a smartphone, up from 35% in the Center's first such survey in 2011. That is a United States figure, from a survey of 5,511 adults conducted from January 30 to June 18, 2026 — not a global rate, and not a promise about your particular guest list. Its practical meaning is modest: for most audiences, planning around phone cameras is planning around the device nearly everyone already carries, while still keeping a printed alternative for the rest.</p>
<h2>What can go wrong — and the fix for each</h2>
<ul>
<li><strong>A code leads to a page that moved.</strong> Fix: dynamic codes for anything the team might move, and a final link check the morning of the event, from a phone, on the venue's network.</li>
<li><strong>Guests cannot connect because the WiFi code is on one slide.</strong> Fix: WiFi codes on permanent signage at the entrance and the tables, not only on a slide.</li>
<li><strong>The photo album fills with uploads from strangers.</strong> Fix: keep the album code inside the room, check the sharing settings before doors open, and change the album link after the event if the link escaped.</li>
<li><strong>A ticket screenshot does the rounds.</strong> Fix: one code per ticket, a rule for second scans at the door, and the paper guest list as backup.</li>
<li><strong>Older guests or guests without smartphones are stranded.</strong> Fix: a phone number on the invitation, a paper list at the door, and a printed agenda beside the code. The code is an additional route, never the only one.</li>
</ul>
<h2>Event code checklist</h2>
<ul>
<li>Check-in: a code on the confirmation email, scanned at the door.</li>
<li>Add-to-calendar: on the invitation, so guests keep the date.</li>
<li>RSVP: on the details card, linking to the form.</li>
<li>Tickets: one code per ticket, batch-generated, test-scanned before sending.</li>
<li>Agenda and speakers: on the program and slide footers, dynamic.</li>
<li>Photo album: on table cards, so shots land in one shared album.</li>
<li>Venue WiFi: on signage, so nobody spells the password over loud music.</li>
<li>Feedback: on exit signage and the closing slide, while the event is still fresh.</li>
</ul>
<p>Put together: one code per guest question, dynamic where things change, static where things should last, each code labelled, tested, and backed by a printed alternative. Make the codes in the <a href="/dynamic-qr-code/">dynamic QR code studio</a> for anything the event team might need to change, or as free static codes for the invitations and keepsakes — and if you are still deciding which kind you need, <a href="/blog/static-vs-dynamic-qr-codes/">static vs dynamic, explained honestly</a> lays out the trade-off without the sales pitch. Planning a wedding specifically? The <a href="/blog/wedding-rsvp-qr-code/">wedding RSVP guide</a> covers the invitation suite in detail.</p>""",
  'date': 'October 14, 2026', 'updated': "November 3, 2026", 'dateModified': "2026-11-03", 'sources': [
  ('https://support.apple.com/en-us/102680', 'Apple Support — Scan a QR code with your iPhone or iPad', 'Supports the test-scan method: open Camera or the Control Center Scan Code control, hold the phone so the code appears in frame, and tap the link that appears. Published September 14, 2026.'),
  ('http://www.iso.org/standard/83389.html', 'ISO/IEC 18004:2024 — QR code bar code symbology specification', "Supports the error-correction levels used in the printing section: L recovers 7%, M 15%, Q 25%, and H 30% of the symbol's codewords. 2024 edition of the standard."),
  ('https://www.pewresearch.org/internet/fact-sheet/mobile/', "Pew Research Center — Americans' Use of Mobile Devices in 2026", "Supports: 91% of United States adults said they owned a smartphone and 98% said they owned a cellphone of some kind, up from 35% smartphone ownership in the Center's first such survey in 2011. Based on a survey of 5,511 United States adults conducted January 30 to June 18, 2026, margin of error plus or minus 1.8 percentage points."),
],
  'datePublished': '2026-10-14',
  'desc': 'How to use QR codes for events: check-in, registration, tickets, photo sharing, and '
          'add-to-calendar codes. Free generator.',
  'faq': [
  ('How do I make a QR code for event check-in?', 'Link the code to your check-in form or registration page, print it for the entrance, and guests scan on arrival instead of queueing at a desk. Keep a printed guest list beside the scanner as a fallback for phones that die or screens that will not read.'),
  ('Can a QR code add an event to my calendar?', "Yes — calendar (VEVENT) QR codes open an 'add to calendar' prompt on iPhones and Androids. FreeQrly generates them free with its event type: title, start and end time, and location in one scan."),
  ('What QR codes do I need for an event?', 'At minimum: check-in/registration, a shared photo album, and venue WiFi. Add-to-calendar codes on invitations are the high-value extra. For conferences, add agenda and speaker codes; for ticketed events, add one code per ticket.'),
  ('Should event ticket codes be static or dynamic?', 'One code per ticket, and dynamic when a ticket can be transferred or cancelled or when the validation page might change — a dynamic code can be repointed without reprinting the ticket. A simple, non-transferable ticket with a final validation page can use a static code. Never print one shared code on every ticket: it cannot tell one ticket from another.'),
  ("What if a guest's ticket code will not scan at the door?", 'Check the name against the printed guest list instead of turning the guest away. Phones die, screens crack, and screenshots arrive too dim to read. Decide before doors open what the door team does when a code has already been used — a returning guest or a screenshot doing the rounds needs a rule, not a debate in front of a queue.'),
  ('Can I reuse event signage for the next event?', "Yes, if the codes on it are dynamic. A dynamic code on a reusable sign can be repointed at the next event's feedback form or agenda, so the sign never needs reprinting. Static codes are better for keepsakes — invitations and printed programs that should keep working for years."),
  ('How big should event QR codes be printed?', "Size each code for its actual scanning distance, using the 1:10 distance rule of thumb from the print size guide: a code scanned from a metre away needs to be roughly ten times larger than one scanned from ten centimetres. Keep contrast high, leave a clear quiet margin, and test the actual print on both iPhone and Android in lighting like the venue's before printing a full run."),
],
  'h1': 'QR codes for <span class="hl hl-blush">events</span>, done right',
  'lede': "Check-in lines, ticket chaos, 'where are the photos?' — a few well-placed QR codes "
          "solve the recurring event headaches. Here's the playbook.",
  'mascot': 'wedding',
  'slug': 'qr-codes-for-events',
  'cta': {'title': 'Try it yourself — free', 'text': 'Everything in this article works in the FreeQrly studio right now. Static codes, all 17 content types, PNG and SVG export.', 'href': '/#studio', 'btn': 'Open the studio'},
  'title': 'QR Codes for Events: Check-In, Tickets & More | FreeQrly'},
 {'body': '\n'
          '<h2>The setup</h2>\n'
          '<p>Build your RSVP form first (Google Forms is free and perfect for this — see the <a '
          'href="/google-form-qr-code/">Google Form QR generator</a>). Then generate the code, '
          'print it on the invitation suite, and guests scan → tap → done. No stamps, no lost '
          'reply cards, no deciphering handwriting.</p>\n'
          '<h2>Where to print it</h2>\n'
          '<ul>\n'
          '<li><b>Invitations:</b> on the details card, at least 2x2 cm.</li>\n'
          '<li><b>Save-the-dates:</b> link it to your wedding website.</li>\n'
          '<li><b>Table cards:</b> a second code linking to the <a href="/wedding-qr-code/">shared photo album</a> — guests upload their shots all night.</li>\n'
          '</ul>\n'
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
  'date': 'October 14, 2026',
  'datePublished': '2026-10-14',
  'desc': 'Wedding RSVP QR codes: link your RSVP form, print on invitations, track responses — '
          'no stamps, no lost reply cards. Free generator.',
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
  'title': 'Wedding RSVP QR Codes: No More Chasing Replies | FreeQrly'}]


POSTS += [
 dict(
  slug="how-to-create-a-dynamic-qr-code",
  title="How to Create a Dynamic QR Code Free (Editable After Printing) | FreeQrly",
  desc="Create a dynamic QR code free: sign in, pick a type, style it, print it. Edit the destination later without reprinting — 20 free codes, currently unlimited.",
  h1="How to create a <span class='hl hl-mint'>dynamic</span> QR code",
  lede="A dynamic QR code lets you change the destination after printing — and see how many people scanned. Here's how to make one, free, in about a minute.",
  date="October 16, 2026", updated="November 3, 2026", dateModified="2026-11-03", sources=[
  ('http://www.iso.org/standard/83389.html', 'ISO/IEC 18004:2024', 'The QR Code symbology specification, Edition 4, published August 2024. Defines the error-correction levels, including High at about 30% of codewords, and the quiet zone of at least 4 modules on all four sides.'),
  ('https://www.qrcode-tiger.com/faq', 'QR TIGER FAQ', "Vendor's own FAQ page, accessed 2026-11-03 (no publication date shown on the page). Supports: 3 free dynamic codes with a 500 scan limit each; paid dynamic codes have unlimited scans while the subscription is valid; 'If your plan expires, it will stop working'; free static codes are unlimited and never expire."),
  ('https://www.qrcode-tiger.com/software-subscription', 'QR TIGER Subscription Plan Management', "Vendor's own subscription page, accessed 2026-11-03 (no publication date shown on the page). Supports: freemium plan with 3 dynamic codes at a 500 scan limit each; Regular US$7 with 12 dynamic codes; Advanced US$16 with 200; Premium US$37 with 600; Professional US$89 with 1,200."),
  ('https://www.the-qrcode-generator.com/pricing?lng=en&signup_source=custom-qr-code_explore_plans', 'The QR Code Generator (TQRCG) Pricing', "Vendor's own pricing page, accessed 2026-11-03 (no publication date shown on the page). Supports: Free plan with 2 dynamic codes and unlimited static codes; after a free trial ends, 2 dynamic codes remain active but display ads; on Uniqode, trial codes become inactive without a paid plan; Flex plan at US$10/month billed yearly."),
],
  datePublished="2026-10-16",
  mascot="faq",
  body="""<p>Yes — you can create a dynamic QR code free, in about a minute, and change where it points after you have printed it. Choose dynamic when the destination is not final yet, when you want to count scans, or when one printed code must serve a new page next month. Choose static when the destination will never change: a fixed link, a WiFi password, or a business card needs no account and no redirect. This guide covers the FreeQrly process, the redirect mechanism in plain language, and the free limits up front.</p>
<p>On FreeQrly, dynamic codes are free. Sign in with email and password, Google, or GitHub, and you get 20 dynamic codes on the free account, currently unlimited during the limited-time promotion. There is no trial period and no card required to start, and scans are unlimited. You can edit a code after printing, see its scan statistics, generate codes in bulk in static form, and use the API.</p>

<h2>Dynamic or static? Decide before you print</h2>
<p>The decision cannot be reversed for a code that is already printed. A static code holds the destination inside the pattern, so it can never be repointed. A dynamic code holds a short link that redirects to the destination, so the destination can be changed later. A printed static code with a wrong link needs a reprint; a printed dynamic code needs only an edit in the Dashboard.</p>
<table>
<tr><th>Your situation</th><th>Choose</th><th>Why</th></tr>
<tr><td>Link, WiFi password, or contact details will not change</td><td>Static</td><td>No account, no redirect, nothing to maintain</td></tr>
<tr><td>Landing page is not final, but the poster must go to print</td><td>Dynamic</td><td>Print now, repoint later</td></tr>
<tr><td>You need to report how many people scanned</td><td>Dynamic</td><td>Only dynamic codes report scans</td></tr>
<tr><td>Seasonal menu, event, or campaign changes often</td><td>Dynamic</td><td>One print run serves every season</td></tr>
</table>
<p>If you are still unsure, <a href="/blog/static-vs-dynamic-qr-codes/">static vs dynamic, explained honestly</a> gives more examples. In short: dynamic buys flexibility and measurement at the price of dependence on a redirect service and an account; static buys independence at the price of a destination frozen at print time.</p>

<h2>How a dynamic code actually works</h2>
<p>A dynamic code does not hold your link directly. It holds a short FreeQrly link, in the form <code>freeqrly.com/q/XXXXXXX</code>, and the pattern encodes that short link. When someone scans the code, their phone opens the short link, FreeQrly's server looks up the destination you currently have set, and the scanner is redirected there. The scanner ends up on your page; the short link is only the junction in the middle.</p>
<p>That junction explains every feature and limit:</p>
<ul>
<li><strong>Editing works because the pattern never changes.</strong> The pattern holds only the short link. Editing changes the record behind it, so every printed copy serves the new destination at the next scan.</li>
<li><strong>Counting works because every scan passes through the junction.</strong> The server sees the scan on its way to the destination and adds it to the statistics. A static code never touches a server, so there is nothing to count.</li>
<li><strong>An account is required because the junction must belong to someone.</strong> Only the creating account may change where its short link points. Without an owner, anyone could repoint anyone else's printed code.</li>
<li><strong>Deleting is permanent because the junction is removed.</strong> Delete a code and its short link stops redirecting, so printed copies stop working. There is no undo, and the freed slot can be used for a new code.</li>
</ul>
<p>Scanners do not see any of this — they point, tap the preview, and land on your page. One thing they can notice is a redirect that shows an advertisement or a vendor-branded page first, so when comparing generators, scan a sample code and watch what appears before your destination loads.</p>

<h2>Step by step: create a dynamic QR code</h2>
<ol>
<li><strong>Sign in — free.</strong> Open the <a href="/login/">sign-in page</a> and create an account with email and password, Google, or GitHub. Static codes never need this; dynamic codes do, because the code must belong to someone who alone may edit it.</li>
<li><strong>Switch to Dynamic.</strong> In the <a href="/?mode=dynamic">studio</a>, flip the toggle from Static to Dynamic. Types, styling, and download all work exactly the same.</li>
<li><strong>Pick a type and fill it in.</strong> Website, WiFi, contact, event — all 17 content types work as dynamic codes. (<a href="/batch-qr-code/">Batch</a> stays static: one dynamic code per generation, because each needs its own short link and Dashboard record.)</li>
<li><strong>Style it if you want.</strong> Dots, colors, logo, frame — the preview updates live, and the style is saved with the code, so the Dashboard thumbnail and the download match. Keep contrast strong and never cover the three large finder squares in the corners.</li>
<li><strong>Generate.</strong> Hit Generate. You get a short link like <code>freeqrly.com/q/XXXXXXX</code> — that is what the pattern encodes. Name the download file for where the code will live, for example <code>cafe-window-menu.png</code>.</li>
<li><strong>Manage it later.</strong> Your codes live in the <a href="/dashboard/">Dashboard</a>: edit, check stats, or delete one to free a slot. Test the printed code with your phone camera before a full print run, and again after any edit.</li>
</ol>

<h2>Choosing the type</h2>
<p>The type decides what the scanner sees and does. A Website code opens a page. A WiFi code offers to join a network. A contact code offers to save a person. An event code offers to save a date. The right type removes a step, and that is usually worth more than a cleverer design. A restaurant should use a Website code pointing at its menu page, not a text code containing the menu: the page can be updated, the text code cannot. A guest WiFi code should be a WiFi code, because the phone can join from the scan itself — see <a href="/blog/share-wifi-with-qr-code/">how to share WiFi with a QR code</a>.</p>
<p>Point at a page you control, not a file hosted somewhere you do not control: a deleted file leaves a working code pointing at nothing. And note that long text makes a denser pattern, which needs a larger print size to scan at the same distance; see the <a href="/blog/qr-code-print-size-guide/">QR code print size guide</a>.</p>

<h2>Styling without breaking the scan</h2>
<p>Dynamic codes support the same styling as static codes: dot shapes, colors, a logo in the centre, and a frame with text. Three rules keep a styled code scannable. First, keep contrast high and the background light; scanners read dark modules against light ones. Second, keep the logo modest and centred, and never cover a finder square. Error correction rebuilds modules hidden behind a small central logo — at the High level in ISO/IEC 18004, up to about 30% of codewords can be restored — but that budget covers all damage combined, including print wear and dirt, not the logo alone. Third, keep the quiet zone: the blank margin around the code, at least 4 modules wide on all four sides under ISO/IEC 18004, is part of the code, not decoration. More on logos is in <a href="/blog/add-logo-to-qr-code/">how to add a logo to a QR code</a>.</p>
<p>For print, test a real printed proof, not just the screen preview: one copy at the intended size, on the intended material, scanned on two different phones — one iPhone and one Android if you can — in the lighting where it will actually be used. Glossy lamination under bright light and a code wrapped around a bottle fail in ways a screen preview never shows. If the proof scans slowly, print larger; size is the cheapest fix available.</p>

<h2>Reading the statistics honestly</h2>
<p>Every dynamic code reports to your Dashboard: total scans, scans today, unique scans, and a seven-day chart, with breakdowns by country, city, device, and operating system. The full guide is in <a href="/blog/dynamic-qr-code-statistics/">what dynamic QR code statistics tell you</a>. Three habits matter most. Compare codes against each other, not against an imagined benchmark: a shop-window code and a delivery-box code live in different worlds. Treat zero as data: a code with no scans for a week usually means the placement is wrong, the call to action is missing, or the code is too small. And give a spike context: a burst of scans right after a post goes out is the post, not the poster.</p>
<p>FreeQrly's stats are aggregates only — counts by day, country, city, device, and operating system — with no per-visitor record and no way to identify an individual scanner. A unique scan is counted with a one-way hash, not a name or an address.</p>

<h2>Scenarios where dynamic earns its keep</h2>
<h3>A restaurant menu that changes with the season</h3>
<p>Print one code on the table tents and point it at the menu page. When the season changes, update the page or repoint the code — the tents stay. See <a href="/blog/qr-codes-for-restaurants/">QR codes for restaurants</a>.</p>
<h3>An event poster printed before the details are final</h3>
<p>Posters go to print weeks before a venue, ticket link, or schedule is locked. A dynamic code lets the poster ship pointing at a holding page, then move to the ticket page when sales open, and to a recap page after the event. See <a href="/blog/qr-codes-for-events/">QR codes for events</a>.</p>
<h3>A product or package that outlives its first campaign</h3>
<p>Packaging is printed in bulk and sold over months or years. A dynamic code on the pack can start at a launch offer, move to a manual or warranty page, and later to a successor product — without a reprint. Keep a list of where each code lives: a code you cannot find in the Dashboard is a code you cannot fix.</p>
<h3>One code per placement, or the numbers lie</h3>
<p>Give each placement its own code. Sharing one code across a flyer, a business card, and a market stall merges their statistics into one number that explains nothing. A code by the till that opens a review page works the same way; see <a href="/blog/get-google-reviews-with-qr-code/">how to get Google reviews with a QR code</a>.</p>

<h2>The honest comparison: what dynamic costs elsewhere</h2>
<p>Dynamic codes are not free everywhere in the same way. What hurts after printing is how many free codes you get, whether scans are capped, and what happens when a plan ends. The figures below are each vendor's own statements on its own pricing or FAQ page, checked on 3 November 2026. Prices and limits change, so check the vendor's page before you print anything that has to last.</p>
<table>
<tr><th>Vendor, free plan, as stated by the vendor</th><th>Free dynamic codes</th><th>Free scan limit</th><th>What the vendor says happens when a plan ends</th></tr>
<tr><td>FreeQrly, free account</td><td>20, currently unlimited during the limited-time promotion</td><td>Unlimited scans</td><td>No trial period, no card to start; deleting a code stops its printed copies and frees the slot</td></tr>
<tr><td>QR TIGER, freemium plan</td><td>3</td><td>500 scans per code</td><td>Paid codes have unlimited scans while the subscription is valid; “If your plan expires, it will stop working”</td></tr>
<tr><td>The QR Code Generator, free plan</td><td>2</td><td>The free allowance is the 2 codes</td><td>After a trial ends, 2 codes remain active but display ads; on parent platform Uniqode, trial codes become inactive without a paid plan</td></tr>
</table>
<p>This is not a verdict on any vendor — a paid plan with more codes, a custom domain, or team seats can be the right buy for a large campaign — but it shows why the free tier needs reading, not skimming. A scan-capped free tier is a code that can die from popularity. A trial-tied free tier is a code with a calendar attached. The fair question for any generator, including FreeQrly, is: what exactly happens to a printed code if I never pay, if I stop paying, and if I delete the code? The answer should be one sentence each, on the pricing page.</p>
<p>One dependence deserves plain statement. A dynamic code depends on the vendor's redirect service for as long as it circulates — true here too. If that service were gone, dynamic codes would stop redirecting, while static codes, which hold the destination in the pattern, would keep working. That is why static is right for anything that must work for decades with no one maintaining it, such as a permanent sign. Dynamic is for living material that someone still looks after; static is for material that must look after itself.</p>

<h2>Mistakes that waste a print run</h2>
<ul>
<li><strong>Printing static when the link was not final.</strong> If the destination might change, the code should have been dynamic before printing; a printed static code cannot be rescued by an edit.</li>
<li><strong>Sharing one dynamic code across placements.</strong> One code, one placement, one statistics record — otherwise the numbers cannot say which placement worked.</li>
<li><strong>Deleting a code to “tidy up”.</strong> Deleting is permanent and printed copies stop at once. Repoint a retiring code to a closing page first, and delete only when no printed copy remains in circulation.</li>
<li><strong>Skipping the printed proof.</strong> A screen preview proves the design; only a printed proof at the real size, material, and light proves the scan. See <a href="/blog/why-is-my-qr-code-not-working/">why your QR code is not working</a>.</li>
<li><strong>Forgetting the call to action.</strong> A bare code asks scanners to guess. A frame saying what they get — menu, tickets, WiFi, discount — turns a decoration into a doorway.</li>
</ul>

<h2>Bulk, API, and the limits, stated plainly</h2>
<p>Dynamic codes are generated one at a time, because each needs its own short link and Dashboard record. If you need many codes at once — one per product, per table, per parcel — <a href="/batch-qr-code/">batch generation</a> stays static; see <a href="/blog/bulk-qr-codes/">bulk QR codes</a>. For programs that generate codes from another system, FreeQrly also offers an API for dynamic codes. The free limits, in one place:</p>
<ul>
<li><strong>20 codes, free (currently unlimited during the limited-time promotion).</strong> Delete a code and the slot frees up.</li>
<li><strong>Unlimited scans.</strong> A popular code does not stop because it was scanned too often.</li>
<li><strong>One at a time.</strong> Dynamic codes are generated one by one; batch generation stays static.</li>
<li><strong>Editing changes the destination, not the pattern.</strong> The printed code keeps working through every edit.</li>
<li><strong>Deleting is permanent.</strong> Printed copies stop working, with no undo, so delete only retired codes.</li>
</ul>
<p>Not sure whether you need dynamic at all? <a href="/blog/static-vs-dynamic-qr-codes/">Static vs dynamic, explained honestly</a>. Already printed and need to fix a link? <a href="/blog/how-to-edit-a-qr-code-after-printing/">How to edit a QR code after printing</a>. Curious what the numbers look like? <a href="/blog/dynamic-qr-code-statistics/">What dynamic QR code statistics tell you</a>. Ready to make one? Open the <a href="/dynamic-qr-code/">dynamic QR code generator</a>, sign in free, switch to Dynamic, and print a code you can still fix next month.</p>""",
  howto=[
  ('Sign in — free', 'Open the sign-in page and create an account with email and password, Google, or GitHub. Static codes never need this; dynamic codes do, because the code must belong to someone who alone may edit it.'),
  ('Switch to Dynamic', 'In the studio, flip the toggle from Static to Dynamic. Types, styling, and download all work exactly the same.'),
  ('Pick a type and fill it in', 'Website, WiFi, contact, event — all 17 content types work as dynamic codes. Batch stays static: one dynamic code per generation, because each needs its own short link and Dashboard record.'),
  ('Style it', 'Dots, colors, logo, frame — the preview updates live, and the style is saved with the code, so the Dashboard thumbnail and the download match. Keep contrast strong and never cover the three large finder squares in the corners.'),
  ('Generate', 'Hit Generate. You get a short link like freeqrly.com/q/XXXXXXX — that is what the QR pattern encodes. Name the download file for where the code will live.'),
  ('Manage it later', 'Your codes live in the Dashboard: edit, check stats, or delete one to free a slot. Test the printed code with your phone camera before a full print run, and again after any edit.'),
],
  faq=[
  ('Is creating a dynamic QR code really free?', 'Yes. Sign in free and create up to 20 dynamic codes, currently unlimited during the limited-time promotion, with unlimited scans. There is no trial period and no card required to start. Static codes remain free and unlimited with no account at all.'),
  ('Do I need an account for a dynamic QR code?', 'Yes — the code has to belong to someone so only you can edit it. Sign in with email and password, Google, or GitHub. Static codes never need an account.'),
  ('How many dynamic QR codes can I have?', '20 on the free account, currently unlimited during the limited-time promotion. Delete a code to free its slot — but deleting is permanent, and printed copies of a deleted code stop working.'),
  ('What does a dynamic QR code link to?', 'A short FreeQrly link (freeqrly.com/q/XXXXXXX) that redirects to your destination. Scanners land on your page; the redirect is what makes editing and scan statistics possible.'),
  ('Can I edit a dynamic QR code after printing?', 'Yes. Editing changes the destination behind the short link, not the printed pattern, so every printed copy serves the new destination at the next scan. Test the code again after any edit.'),
  ('When should I choose static instead of dynamic?', 'When the destination will never change — a fixed link, a WiFi password, a business card. Static codes hold the destination in the pattern itself, need no account, and keep working with no redirect service to maintain.'),
  ('Can I create dynamic codes in bulk?', 'No — dynamic codes are generated one at a time, because each needs its own short link and Dashboard record. Batch generation stays static.'),
  ('What happens to my scans if a code gets popular?', "Nothing bad on FreeQrly: scans are unlimited, so a popular code does not stop working because it was scanned too often. On some other vendors' free plans, a scan cap can stop a code — check the vendor's pricing or FAQ page before printing."),
],
  cta=dict(title="Make your first dynamic code",
           text="Free sign-in, 20 codes (currently unlimited), editable after printing. Start in the studio.",
           href="/?mode=dynamic", btn="Create a dynamic code"),
 ),
 dict(
  slug="how-to-edit-a-qr-code-after-printing",
  title="How to Edit a QR Code After Printing (Without Reprinting) | FreeQrly",
  desc="Printed the wrong link? Fix it free, without reprinting. Edit a dynamic QR code's destination, type, or style in the Dashboard — the printed code updates instantly.",
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
  title="Dynamic QR Code Statistics: What Scans Actually Tell You | FreeQrly",
  desc="Dynamic QR code statistics: total and unique scans, by day, country, city, device, and OS — free with your codes. And what FreeQrly never tracks.",
  h1="What dynamic QR <span class='hl hl-honey'>statistics</span> tell you",
  lede="A dynamic code reports home every time it's scanned. Here's what FreeQrly counts, how to read it, and what it never collects.",
  date="October 16, 2026", updated="November 3, 2026", dateModified="2026-11-03", sources=[
  ('http://www.iso.org/standard/83389.html', 'ISO/IEC 18004:2024 — QR code bar code symbology specification', "Supports the error-correction table: L recovers 7%, M 15%, Q 25%, and H 30% of the symbol's codewords. 2024 edition of the standard."),
  ('https://www.pewresearch.org/internet/fact-sheet/mobile/', "Pew Research Center — Americans' Use of Mobile Devices in 2026", "Supports: 91% of United States adults said they owned a smartphone and 98% said they owned a cellphone of some kind, up from 35% smartphone ownership in the Center's first such survey in 2011. Based on a survey of 5,511 United States adults conducted January 30 to June 18, 2026, margin of error plus or minus 1.8 percentage points."),
],
  datePublished="2026-10-16",
  mascot="batch",
  body="""<p>A static code is silent: it never reports home, so nobody — including you — knows how often it was scanned. A dynamic code reports every scan to your Dashboard. Here is what FreeQrly counts, how to read it, what it deliberately never collects, and how to use your own numbers to make decisions — plus the only outside numbers this post cites, each with its original source, so you can check them yourself.</p>
<p>The short answer first: scan statistics answer three questions, and only three. Which placement got attention? When did it get it? And on what kind of device and from roughly where? Everything else — whether a scan became a customer, whether the poster was good — is an interpretation you add on top, and most misreadings come from treating an interpretation as if it were a measurement.</p>
<h2>What FreeQrly counts</h2>
<p>Open a dynamic code in your Dashboard and you see the same set of numbers for every code. The definitions matter, because two of the most common misreadings come from confusing “total” with “unique” and “today” with “all time.”</p>
<table>
<tr><th>Number</th><th>What it means</th><th>How to read it</th></tr>
<tr><td><strong>Total scans</strong></td><td>Every scan of the code, all time</td><td>The lifetime footprint of that code. Compare totals only between codes that have been out for the same length of time.</td></tr>
<tr><td><strong>Today</strong></td><td>Scans so far today</td><td>A live pulse, not a verdict. A quiet morning says nothing about the evening.</td></tr>
<tr><td><strong>Unique scans</strong></td><td>Distinct scanners, counted once per day. Two scans by the same person on the same day count as one unique scan.</td><td>The closest thing to “how many people.” If total is far above unique, a small group is scanning repeatedly — or one code is being passed around.</td></tr>
<tr><td><strong>Last 7 days</strong></td><td>A daily bar chart covering today and the previous six days — always seven bars, with zero-height bars for quiet days</td><td>Shape matters more than height. Gaps, evening clusters, and weekday-only patterns are visible at a glance.</td></tr>
<tr><td><strong>By country</strong></td><td>Where scans came from, from the scanner's approximate location</td><td>Useful for spotting a code that travelled — a new country usually means someone shared it online.</td></tr>
<tr><td><strong>By city</strong></td><td>The same approximate location, at city level</td><td>Useful for comparing two neighbourhoods or two venues. Approximate means approximate: treat a city as a region, not an address.</td></tr>
<tr><td><strong>By device</strong></td><td>Phone, tablet, or desktop</td><td>A poster that gets desktop scans at noon is probably being scanned from a screenshot, not from the wall.</td></tr>
<tr><td><strong>By OS</strong></td><td>iOS, Android, and the rest</td><td>A sanity check on your audience and your testing: if nearly all scans are on one OS, test the destination on that OS first.</td></tr>
</table>
<p>Each breakdown comes with counts and percentages. Percentages are shares of that code's scans, not shares of anything larger — a code with mostly iOS scans does not mean most of your customers use iPhones. It means most of the people who scanned that code did so on an iPhone.</p>
<h2>Two outside numbers, with their sources attached</h2>
<p>This post deliberately cites very few outside numbers, and the reason is worth stating plainly: a QR statistic borrowed from a roundup usually arrives without the three facts that make a number usable — what was measured, over whom, and when. The two numbers below arrive with all three, from their original publishers.</p>
<h3>The QR standard itself: how much damage a code can survive</h3>
<p>Scan statistics are only half of a print decision; the other half is whether the code survives handling. The QR standard, ISO/IEC 18004:2024, defines four error-correction levels, each stating how much of the symbol's codewords can be recovered if damaged:</p>
<table>
<tr><th>Level</th><th>Recoverable codewords</th><th>Typical use</th></tr>
<tr><td>L</td><td>7%</td><td>Clean digital display</td></tr>
<tr><td>M</td><td>15%</td><td>Everyday indoor print</td></tr>
<tr><td>Q</td><td>25%</td><td>Print that gets handled or lives outdoors</td></tr>
<tr><td>H</td><td>30%</td><td>Codes carrying a centre logo, or rough handling</td></tr>
</table>
<p>Source: ISO/IEC 18004:2024, the QR code bar code symbology specification, via the ISO standard page (<a href="http://www.iso.org/standard/83389.html">iso.org/standard/83389.html</a>). Read the percentages carefully: they describe codewords, not printed surface area. A code at level H does not survive every possible 30% hole in the print, and a higher level buys resilience by spending more of the code on redundancy. For statistics, the practical point: a code printed at a low level on a handled surface will under-report its true audience — people tried to scan, the code failed, and no scan was recorded.</p>
<h3>Who carries a camera phone: Pew's United States survey</h3>
<p>When you read a device breakdown, it helps to know the ceiling: how many people in the audience could scan at all. Pew Research Center's 2026 mobile fact sheet reports that 91% of United States adults said they owned a smartphone, and 98% said they owned a cellphone of some kind, up from 35% smartphone ownership in the Center's first such survey in 2011. Source: Pew Research Center, “Americans' Use of Mobile Devices in 2026” (<a href="https://www.pewresearch.org/internet/fact-sheet/mobile/">pewresearch.org/internet/fact-sheet/mobile/</a>), based on a survey of 5,511 United States adults conducted January 30 to June 18, 2026, with an overall margin of error of plus or minus 1.8 percentage points.</p>
<p>Three cautions travel with that number, and they apply to any outside figure you meet. First, population: this is United States adults, not the world, and not your event's guest list. Second, measure: self-reported ownership, not scanning behaviour. Third, date: a 2026 survey describes 2026. A number used outside its population, its measure, or its date stops being evidence and becomes decoration.</p>
<h2>How to read your own numbers: five questions</h2>
<p>Your Dashboard numbers need no outside benchmark to be useful. Run every reading through these five questions before acting on it:</p>
<ol>
<li><strong>Compared with what?</strong> A code's total means little alone. Compare codes that ran in the same period, in similar placements, for the same offer. A flyer code and a poster code from the same week can be compared; a flyer code from last spring and a poster code from this week cannot, because the season, the offer, and the audience all changed between them.</li>
<li><strong>Over what period?</strong> The 7-day chart exists to stop single-day readings. A code that looks dead on a Monday may be an evening code, a weekend code, or a commuter-route code. Read the shape of the week before judging the height of a day.</li>
<li><strong>Total or unique?</strong> If total runs far ahead of unique, the same people are coming back — which is good for a menu or a timetable, and a warning sign for a one-time offer. If unique runs close to total, each scan is a different person, and the code is reaching broadly rather than deeply.</li>
<li><strong>What else happened that day?</strong> Spikes need context. A burst of scans right after a post goes out is the post, not the poster. A burst on a day you changed the destination is the new destination, not the old placement. Note external events — a post, a mention, a price change — beside the chart, or the chart will mislead you with perfect confidence.</li>
<li><strong>What did the scan lead to?</strong> A scan is a glance, not a conversion. Pair scan statistics with whatever the destination itself measures — form submissions, orders, sign-ups — and judge the code by the destination's outcome, not by the scan count alone.</li>
</ol>
<h2>Reading a real week: patterns, not just totals</h2>
<p>The same breakdowns, read as behaviour rather than numbers:</p>
<ul>
<li><strong>Evening-only scans.</strong> A code that wakes up after work hours is probably on a commuter route or an evening venue — evening visitors, not office visitors.</li>
<li><strong>A sudden new city.</strong> Scans spreading to a city you never printed in usually mean someone shared the code in a chat or a post — the code travelled without you. Check where the code is pointing: a shared code sends strangers to your destination, so the destination should make sense to a stranger.</li>
<li><strong>Weekday-only scans.</strong> A code that goes quiet on weekends is probably on an office poster or a weekday venue, not a weekend one.</li>
<li><strong>Desktop-heavy scans.</strong> A poster that gets desktop scans is probably being scanned from a screenshot or a forwarded image, not from the wall. The wall version may be fine; the screenshot version is doing the work, and the destination should be checked on a desktop screen as well as on a phone.</li>
<li><strong>Zero is data.</strong> A code with no scans for a week is telling you the placement is wrong, not the code. Codes do not fail silently very often — a printed code either scans or it does not, and a quick test with your own phone settles that in seconds. If it scans and nobody scans it, the problem is position, size, contrast, or the absence of a reason to scan, in that order.</li>
</ul>
<h2>A worked example, with the arithmetic shown</h2>
<p>Illustrative example — the numbers below are hypothetical, used only to show the arithmetic, not measurements from any real campaign. Suppose two codes point at the same page for the same two weeks. Code A, on a counter sign, records 120 total scans and 90 unique scans. Code B, on a window poster, records 60 total scans and 55 unique scans. Three readings follow, each with a different action:</p>
<ul>
<li><strong>Reach:</strong> Code A reached more distinct people (90 against 55), so the counter sign is the broader placement.</li>
<li><strong>Repeat use:</strong> Code A's total runs 30 scans ahead of its unique count, while Code B's runs only 5 ahead, so counter visitors scan repeatedly while poster visitors mostly scan once. That fits a counter sign seen by regulars and a poster seen by passers-by — and it suggests the counter code's destination should reward a second visit, while the poster code's destination should make its case in one visit.</li>
<li><strong>Next test:</strong> Swap nothing yet. Move Code B's poster to the counter for a week and Code A's sign to the window, then compare again. If the pattern follows the placement, the placement was the cause. If the pattern follows the code, the destination or the design was the cause. One swap beats a month of debate about which sign is better.</li>
</ul>
<p>The discipline in that example is the point, not the numbers: same period, same destination, one change at a time, and a decision rule written before the test runs.</p>
<h2>Set up a comparison you can trust</h2>
<ol>
<li><strong>Give each placement its own dynamic code.</strong> One code per placement — counter, window, flyer, receipt — all pointing at the same destination. Shared codes cannot tell placements apart, and a comparison built on a shared code is guesswork with a chart.</li>
<li><strong>Keep the destination identical.</strong> If two codes point at different pages, you are testing pages, not placements. Test one variable at a time.</li>
<li><strong>Run them for the same period.</strong> Start and end together, through the same weekdays and weekends. A code that ran over a holiday weekend is not comparable with one that ran over an ordinary week.</li>
<li><strong>Note what else happened.</strong> Keep a one-line log beside the chart: post published, price changed, venue closed. Spikes without notes become mysteries.</li>
<li><strong>Decide the action before you look.</strong> Write down what you will do if A outpulls B — move B, reprint B, retire B — before opening the statistics.</li>
<li><strong>Act on the result, then re-measure.</strong> Move the weak code, change the destination of the strong one, or retire the silent one — and watch the next 7-day chart for the change. A statistic that never changes a decision was entertainment, not measurement.</li>
</ol>
<h2>What FreeQrly never collects</h2>
<p>Stats are aggregates — there is no per-visitor record to look at. A “unique scan” is a one-way hash of the scanner's IP address, browser, and date: enough to count distinct scanners per day, impossible to reverse into a person. No names, no emails, no exact locations, no cross-code tracking of individuals. And static codes track nothing at all — they never touch a server, so there is nothing to count.</p>
<p>That limit shapes what you should ask of the statistics. You can ask which placement won, when it won, and on what devices. You cannot ask who scanned: a scan carries no identity, and any identity attached to it came from somewhere else. If your decision genuinely needs to know who responded, put a form behind the code and let people identify themselves there, voluntarily.</p>
<h2>What scan statistics cannot tell you</h2>
<ul>
<li><strong>Scans are not customers.</strong> A scan is a glance. Someone can scan out of curiosity, by accident, or to show a friend, and none of those are a sale. Judge the destination's outcome, not the scan count.</li>
<li><strong>Scans are not satisfaction.</strong> A heavily scanned code on a complaint form is not a success story. Read the destination's content alongside the counts.</li>
<li><strong>Averages hide the shape.</strong> Two codes with the same weekly total can have opposite patterns — one steady, one spiky — and the steady one is usually the healthier placement. Always read the 7-day chart, not just the total.</li>
<li><strong>Silence is ambiguous.</strong> Zero scans can mean a bad placement, a damaged print, a changed destination, or a code printed where nobody looks. Test the print with your own phone before concluding anything about the audience.</li>
<li><strong>Outside benchmarks mislead more than they help.</strong> A figure quoted without its population, measure, and date cannot be compared with your codes, because you do not know what it counted. Vendor-published figures deserve an extra check: read them as the vendor's own account of its own users, and look for the methodology page that states who was surveyed and how. A figure whose original page states its method can be used, with its scope attached; a figure carried secondhand, stripped of its method, should be left out of your decision entirely. That is why this post leans on your own Dashboard and on two standards-grade sources rather than on a roundup of borrowed percentages.</li>
</ul>
<h2>A weekly routine that takes ten minutes</h2>
<ul>
<li>Open each live code and read the 7-day chart shape first, totals second.</li>
<li>Compare placements that ran side by side, same period, same destination.</li>
<li>Move, repoint, or retire the weakest placement — one change, not five.</li>
<li>Check the destination on the device most scanners used that week.</li>
<li>Note any external event beside the chart, so next week's spike has an explanation ready.</li>
</ul>
<p>Do that weekly for a month and the statistics become a habit that moves signs and retires dead placements.</p>
<p>Ready to try it? <a href="/blog/how-to-create-a-dynamic-qr-code/">Create your first dynamic code</a> — free sign-in, 20 codes on the free account with unlimited scans during the limited-time promotion — and check back after your first print run. Already printed and need a fix? <a href="/blog/how-to-edit-a-qr-code-after-printing/">How to edit a QR code after printing</a> shows how to change the destination without reprinting.</p>""",
  faq=[
  ('What counts as a unique scan?', 'One scanner, once per day. FreeQrly counts distinct scanners using a one-way hash of IP address, browser, and date — the same person scanning twice in a day counts once.'),
  ('Do static QR codes track scans?', 'No. Static codes never touch a server — the destination lives in the pattern — so there is nothing to count. Only dynamic codes report scans.'),
  ('Is visitor data private?', 'Yes. Stats are aggregates only: counts by day, country, city, device, and OS. No names, emails, exact locations, or per-visitor records. Unique scans use a non-reversible hash.'),
  ('Can I see who scanned my QR code?', 'No — and that is by design. FreeQrly counts scans; it does not identify scanners. A scan carries no identity, so if a decision needs to know who responded, put a form behind the code and let people identify themselves there voluntarily.'),
  ('Why does one code show many more total scans than unique scans?', 'Because the same people are scanning repeatedly. A total far ahead of the unique count fits a code seen by regulars, such as a counter sign or a menu; a total close to the unique count fits a code seen mostly by passers-by. Compare the two numbers together — total alone hides repeat use.'),
  ('My code shows zero scans — is it broken?', 'Not necessarily. First test the print with your own phone: if it scans, the problem is placement, size, contrast, or the absence of a reason to scan, in that order. Zero scans for a week is data about the placement, not proof the code failed. If it does not scan, check damage, contrast, and size before concluding anything about the audience.'),
  ('How do I compare two placements fairly?', 'Give each placement its own dynamic code pointing at the same destination, run them for the same period through the same weekdays and weekends, and decide the action before you look — what you will do if one outpulls the other. Note anything else that happened that week, such as a post going out, beside the chart.'),
  ('Why does this post cite so few outside statistics?', "Because an outside figure is only usable with its measure, its population, and its date attached. This post cites two figures that arrive with all three from their original publishers — the ISO QR error-correction levels and Pew's United States smartphone survey — and leans on your own Dashboard for the rest. A figure carried secondhand, stripped of its method, is left out of decisions here."),
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
  title="QR Code vs Barcode: Which One Do You Actually Need? | FreeQrly",
  desc="QR code vs barcode: what each one holds, how much data fits, and when to use which. Barcodes for checkout, QR codes for links, menus, and WiFi.",
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
  title="How to Make a QR Code in Canva, Excel, or Word (Free) | FreeQrly",
  desc="Canva, Excel, and Word have no built-in QR tool. Make the code in FreeQrly (free, no sign-up), download PNG, and drop it into your design or document.",
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
<tr><td><strong>Free dynamic codes</strong></td><td>20 free, with scan stats</td><td>Paid (via Bitly)</td><td>3 free</td><td>Paid plans</td><td>Free dynamic codes</td></tr>
<tr><td><strong>Batch generation</strong></td><td>50 per batch, static</td><td>Not stated</td><td>Up to 3,000 per batch</td><td>Not stated</td><td>Supports bulk generation</td></tr>
<tr><td><strong>Type range</strong></td><td>17 types</td><td>Core types</td><td>20–24 solutions</td><td>~37 types</td><td>50+ types</td></tr>
<tr><td><strong>Best for</strong></td><td>Free dynamic codes + privacy</td><td>Simple free static codes</td><td>Bulk + enterprise features</td><td>Longest track record (since 2009)</td><td>Widest type range</td></tr>
</table>
<p><small>Limits and prices change — check each site before you commit. Figures from public pages and comparisons, October 2026.</small></p>
<p>Want the full head-to-head? <a href="/freeqrly-vs-qr-tiger/">FreeQrly vs QR Tiger</a>, <a href="/freeqrly-vs-qr-code-monkey/">FreeQrly vs QRCode Monkey</a>, and <a href="/freeqrly-vs-qr-code-generator/">FreeQrly vs QR Code Generator</a> put each free plan under the microscope.</p>

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
<li><strong>Need free dynamic codes with stats?</strong> FreeQrly: 20 free, editable after printing, scan stats included.</li>
<li><strong>Need bulk or enterprise features?</strong> QR Tiger: up to 3,000 codes per batch, CRM integrations, white-label. (<a href="/blog/qr-tiger-alternative/">QR Tiger alternative</a>.)</li>
<li><strong>Just want a quick free static code?</strong> QRCode Monkey is the classic — simple, free, no fuss. (<a href="/blog/qr-code-monkey-alternative/">QRCode Monkey alternative</a>.)</li>
<li><strong>Want the widest type range?</strong> ME-QR lists 50+ types.</li>
<li><strong>Want the longest-running brand?</strong> QR Code Generator (Egoditor, since 2009, now part of Bitly).</li>
</ul>

<p>Whatever you pick, test it: generate one code, print it at the size you will actually use, and scan it with your phone. A generator is only as good as its codes on paper. <a href="/#studio">Make a QR code</a> — free, no sign-up for static codes.</p>
""",
  faq=[
    ("Is FreeQrly really free?",
     "Yes. Static codes are free and unlimited with no account. Dynamic codes are free too: sign in and you get 20 free dynamic codes (currently unlimited during the limited-time promotion) with scan stats. No trial, no card, no expiry games."),
    ("Which QR code generator is best for beginners?",
     "Any of the five above will make a working code. Pick by what you need next: free dynamic editing (FreeQrly), bulk (QR Tiger), widest type range (ME-QR), or the simplest possible static code (QRCode Monkey)."),
    ("Do free QR codes expire?",
     "Static codes never expire — the content lives inside the pattern. Dynamic codes can stop working if the provider shuts down or the free tier ends, which is why the provider's longevity matters for dynamic codes."),
    ("Can I edit a free QR code after printing?",
     "Only if it is dynamic. Static codes are frozen at print time; dynamic codes point at a short link you control, so you can change the destination without reprinting."),
  ],
  sources=[
    ("https://www.qrcode-tiger.com/software-subscription", "QR Tiger pricing", "Free plan and paid plan limits"),
    ("https://www.qrcode-monkey.com/", "QRCode Monkey", "Free static codes and PRO features"),
    ("https://www.qrcode-generator.com/", "QR Code Generator", "Free tool and PRO plans"),
    ("https://me-qr.com/faq", "ME-QR FAQ", "Free dynamic codes and unlimited scans"),
  ],
  cta=dict(title="Compare for yourself",
           text="Make a code in the studio — free, no sign-up for static codes.",
           href="/#studio", btn="Open the studio"),
 ),
 dict(
  slug="why-is-my-qr-code-blurry",
  title="Why Is My QR Code Blurry? 5 Fixes That Work | FreeQrly",
  desc="Blurry QR code won't scan? 5 usual causes — low-res export, wrong size, JPEG compression, stretching, bad print — and how to fix each one.",
  h1="Why is my QR code <span class='hl hl-blush'>blurry</span>?",
  lede="A blurry QR code is almost always a resolution problem: too few pixels stretched across too much space. The fix is to export bigger — or as SVG.",
  date="October 17, 2026", updated="November 3, 2026", dateModified="2026-11-03", sources=[
  ('http://www.iso.org/standard/83389.html', 'ISO/IEC 18004:2024', 'The QR Code symbology specification. ISO page shows Edition 4, published 2024-08 (page fetched 2026-11-03). Supports the four error-correction levels (L 7%, M 15%, Q 25%, H 30% of codewords) and the 4-module quiet zone, as defined in the standard.'),
  ('https://www.4over4.com/guide/understanding-image-resolution-dpi-in-print-vs-web-part2', '4OVER4: Export Settings for Print vs Web, Sizes and DPI', 'Supports 300 DPI as the professional print standard for close-viewed items (business cards, postcards, brochures, flyers) and lower effective resolution for large-format items viewed from a distance. No explicit publication date on the page; accessed 2026-11-03.'),
  ('https://dev.to/bitran/image-formats-explained-jpg-vs-png-vs-webp-vs-avif-2hm7', 'Image Formats Explained: JPG vs PNG vs WebP vs AVIF', 'Supports JPEG as lossy compression that smears crisp edges and degrades further on re-saving, versus PNG as lossless compression that preserves every pixel exactly. No explicit publication date on the page; accessed 2026-11-03.'),
  ('https://qrlynx.com/blog/iso-iec-18004-qr-code-standard-explained', 'ISO/IEC 18004:2024 Explained (QRLynx)', 'Reviewed July 2026 against ISO and DENSO WAVE. Supports the codeword reading of the error-correction percentages (7% / 15% / 25% / 30% of total codewords, not a guaranteed visible-area tolerance) and the four-module quiet zone specified by DENSO WAVE.'),
],
  datePublished="2026-10-17",
  mascot="error",
  body="""<p>A blurry QR code is almost always a resolution problem: too few pixels stretched across too much space. The fix is to export bigger — or as SVG. If the code looked sharp on screen and turned to mush on paper, the image did not have enough pixels for the size it was printed at. A QR code is a grid of tiny squares called modules; when there are not enough pixels, their edges smear into each other, phones cannot find the grid, and scans fail. Start with the export, not a new design: regenerate at higher resolution or as a vector file, reprint one copy at the real size, and scan it at the real viewing distance before printing the batch.</p>
<p>That answer covers most cases, but blur has more than one cause, each with a different fix: a small export, JPEG compression, stretching, printer or paper, or a copy of a copy. The sections below separate those causes, give you a numbers table for the printer, walk through the fix in order, and cover codes that look sharp yet still will not scan — those belong to <a href="/blog/why-is-my-qr-code-not-working/">why your QR code will not scan</a>.</p>
<h2>What blur actually does to a code</h2>
<p>A phone camera does not read a QR code the way a person reads a picture. It looks for the three large square finder patterns in the corners, works out the grid from them, and then decides, module by module, whether each small square is dark or light. Blur attacks exactly that decision: when neighbouring modules bleed into each other, the camera sees grey where it needs black or white, and it starts guessing. A little guessing is survivable, because QR codes carry built-in error correction — extra data that lets a reader rebuild codewords that come back wrong or unreadable. That protection is measured in codewords, not visible area: the four levels in ISO/IEC 18004 restore approximately 7% of codewords at level L, 15% at M, 25% at Q, and 30% at H. A smudge over a finder pattern, or blur spread across the whole symbol, can defeat a reader long before any neat percentage suggests it should survive. Treat error correction as a safety net, never as permission to print a soft code.</p>
<p>Density makes blur worse. A short link produces a roomy grid with large modules; a long link, a full contact card, or a Wi-Fi code with a long password produces a denser grid with smaller modules, and smaller modules blur sooner. That is why the same export can look fine for a short URL and fail for a data-heavy code at the same print size. If a code is both dense and printed small, shorten the destination where you can, print larger, or both. A dynamic code helps differently: the printed pattern encodes a short link you can redirect later, so the grid stays roomy even if the final destination is long. For a destination that will never change, a static code is simpler: free, no account, no watermark, and it does not expire.</p>
<h2>The numbers: print size, pixels, and format</h2>
<p>Printers talk about resolution in dots or pixels per inch. For close-viewed print, 300 pixels per inch at the final print size is the widely used professional baseline for sharp output. The table below turns that baseline into pixel counts: print width in inches multiplied by 300. A 2 cm code is about 0.8 inches wide, so it needs roughly 240 pixels at 300 pixels per inch — and that is the bare minimum, not a comfortable margin. Always export larger than the minimum and let the designer scale down, because scaling down preserves sharpness while scaling up only enlarges the blur.</p>
<table>
<tr><th>Print width</th><th>Pixels at 300 per inch (minimum)</th><th>Export to send</th></tr>
<tr><td>2 cm (business card)</td><td>~240 px</td><td>PNG at 1024 px, or SVG</td></tr>
<tr><td>3 cm (flyer, menu)</td><td>~350 px</td><td>PNG at 1024 px, or SVG</td></tr>
<tr><td>5 cm (table tent, label)</td><td>~590 px</td><td>PNG at 1024 px, or SVG</td></tr>
<tr><td>10 cm (poster detail)</td><td>~1,180 px</td><td>PNG at 2048 px, or SVG</td></tr>
<tr><td>20 cm (poster)</td><td>~2,360 px</td><td>SVG; PNG at 2048 px only as a fallback</td></tr>
<tr><td>50 cm (large poster, signage)</td><td>~5,900 px</td><td>SVG</td></tr>
</table>
<p>Two rules of thumb sit behind that table. First, the print size in centimetres, multiplied by roughly 100, gives a quick pixel target — a 5 cm code wants around 500 pixels at minimum, a 10 cm code around 1,000. Second, the 1:10 distance rule of thumb from the <a href="/blog/qr-code-print-size-guide/">print size guide</a>: the code width should be at least one-tenth of the scanning distance, so a code scanned from 50 cm should be at least 5 cm wide, and a poster scanned from 5 metres needs a 50 cm code. A poster code viewed from metres away can tolerate a lower effective resolution than a card held in the hand, but it still needs enough pixels for its size — and only a vector file gives you that without a ceiling.</p>
<table>
<tr><th>Format</th><th>How it behaves</th><th>Use it for</th></tr>
<tr><td>SVG</td><td>Vector: no pixels, scales without limit, edges stay exact</td><td>Professional print, large posters, designer layouts</td></tr>
<tr><td>PNG</td><td>Lossless raster: every pixel preserved, no compression smear</td><td>Office printing, slides, apps that do not accept SVG</td></tr>
<tr><td>JPEG</td><td>Lossy: discards detail and smears sharp edges</td><td>Photographs only — never for a QR code</td></tr>
<tr><td>Screenshot or chat image</td><td>Re-compressed and often downscaled by the sending app</td><td>Nothing in print — go back to the original export</td></tr>
</table>
<h2>The 5 usual causes, in detail</h2>
<h3>1. Low-resolution export</h3>
<p>This is the most common cause, and the most forgiving to fix. A 512 px PNG looks fine at 2 cm wide; blown up to a 20 cm poster, each module becomes a smudge, because the same 512 pixels now cover ten times the area. The screen hides the problem — a display shows the code small, so the pixels look tight — while paper shows it at true size. The fix is at the source: re-export at 1024 px for cards and flyers, 2048 px for posters, or SVG whenever the printer accepts it. Enlarging the small file in an editor does not add detail; it only makes the existing blur bigger. If the original export is gone, regenerate from the same destination rather than stretching the file you have.</p>
<h3>2. JPEG compression</h3>
<p>JPEG is built for photographs, and it works by discarding detail the eye is least likely to notice in a photo. That trade is poor for a QR code, which is nothing but sharp edges and flat areas — exactly the features JPEG smears. A code saved as a low-quality JPEG can fail even at small sizes, and the damage worsens every time the file is re-saved as JPEG. PNG uses lossless compression, preserving every pixel exactly, and SVG has no pixels to lose. The rule is simple: PNG or SVG only. If a designer, chat app, or social platform hands you back a JPEG version, treat it as a preview, not print artwork, and replace it with the original PNG or SVG before printing.</p>
<h3>3. Stretching</h3>
<p>Dragging one corner distorts the grid: squares become rectangles, module spacing changes unevenly, and scanners give up. This happens most often in slide decks, word processors, and page-layout tools, where an image is dragged to fill a gap. Always resize proportionally — hold Shift, or use the lock icon, so width and height change together and the squares stay square. A code stretched and then stretched back is not automatically square again, because rounding in the layout tool can leave it slightly off. When in doubt, delete the placed image and place a fresh export at the intended size.</p>
<h3>4. Bad print: printer, ink, and paper</h3>
<p>Low-resolution printers, ink bleed on rough or absorbent paper, and glossy glare all soften edges. An inkjet on uncoated, absorbent stock lets ink spread into the fibres, so thin white gaps between modules fill in and the code looks bold and muddy. A laser printer on smooth or coated stock holds edges far better, which is why matte paper and a laser printer beat an inkjet on a napkin. Glossy lamination is different: the paper can stay sharp yet throw reflections back at the camera — tilt the print under the light to tell glare apart from blur. For fabric, embroidery, engraving, or very rough surfaces, expect edges to soften regardless, and compensate with a larger code, higher error correction, and a physical test first.</p>
<h3>5. Copy of a copy</h3>
<p>Screenshotting a code from a message, then screenshotting that screenshot, loses resolution each time. Messaging apps also recompress and downscale images, so a code forwarded through chat can arrive far smaller and softer than the original export. Photographing a printed code to reuse it adds perspective distortion, uneven light, and lens softness on top of the original print. Always go back to the original export, or regenerate from the same destination. If the destination is a dynamic code, generate a fresh code for the same short link — no old file needed.</p>
<h2>How to fix it, step by step</h2>
<ol>
<li><strong>Find the original file.</strong> If you only have a JPEG, a screenshot, or a forwarded chat image, stop and regenerate — no edit restores detail compression already threw away.</li>
<li><strong>Export at the right size.</strong> PNG at 1024 px for cards and flyers, 2048 px for posters, SVG whenever the printer or designer accepts it. Above about 20 cm, SVG is the only format that keeps edges exact without an enormous file.</li>
<li><strong>Use PNG or SVG, never JPEG.</strong> PNG for screens and office printing, SVG for professional print. If a tool insists on JPEG, use its highest quality setting for a screen preview only, never as the print master.</li>
<li><strong>Keep proportions when resizing.</strong> Hold Shift or the lock icon so the squares stay square. Place the image at the final size, rather than placing it small and stretching it later.</li>
<li><strong>Keep the code dark on light, with a clear margin.</strong> Blur and low contrast compound each other: a grey code on a pale background that is also soft fails sooner than either fault alone. Keep a blank margin at least 4 modules wide on every side, as specified in ISO/IEC 18004, and keep text, logos, and decorative borders out of it.</li>
<li><strong>Match paper and printer to the job.</strong> Smooth or coated stock and a laser printer for small codes; matte finish where glare is a risk; larger size and higher error correction for rough or textured surfaces.</li>
<li><strong>Test-scan the real print.</strong> Print one copy at final size, step back to the real viewing distance, and scan it in the real lighting. A first-try scan means the batch is safe. If it hesitates, fix the export or the size now — a run of soft codes cannot be rescued afterwards.</li>
</ol>
<h2>Scenarios: where blur bites hardest</h2>
<h3>Flyers, menus, and table tents</h3>
<p>These are scanned at arm's length, often in dim rooms, so they need both sharpness and size: at least 3 cm on a flyer or menu, 4–5 cm on a table tent as a rule of thumb. Menus add lamination risk: gloss under overhead lights can glare, while matte laminate keeps the code readable and wipes clean. For a menu that changes, link to a page you control rather than a screenshot, so the print never goes stale — and a dynamic code lets you change that destination after printing, with scan stats to show which tables actually scan.</p>
<h3>Posters and signage</h3>
<p>Posters fail differently: the export is usually the problem, not the printer. A 512 px file that looked fine on screen becomes visibly soft at 20 cm or 50 cm, and no printer can invent the missing pixels. Use SVG, apply the 1:10 distance rule of thumb, and proof the code panel at full size before the run. Outdoors, allow for fading too: a code that starts sharp but fades in sun drifts towards failure over weeks, so a higher error-correction level and a sheltered position matter more than a marginally sharper first print.</p>
<h3>Packaging and labels</h3>
<p>Small labels combine small size, dense data, and curved or textured surfaces. Keep the code at 2 cm or larger as a rule of thumb, avoid wrapping it around a tight curve where edge modules stretch, and test on the actual container — a code that scans flat can fail on a bottle. If the material is rough or printing coarse, print larger and simpler: a short link keeps the grid roomy, including a short link behind a dynamic code.</p>
<h2>Honest comparison: what fixes blur, and what does not</h2>
<p>Not every sharpening trick works, and some popular advice wastes a print run. Upscaling a small file — in an editor, with an enlarger tool, or by exporting the same small image larger — does not add detail; it interpolates between the pixels you already have, so edges stay soft, only bigger. A sharpening filter can make edges look crisper to the eye while adding halos that confuse a camera, so a filtered code can scan worse. Converting a JPEG to PNG does not undo JPEG damage either: the format changes, but the smeared pixels stay smeared. The only reliable repair is a fresh export from the original data at higher resolution, or as SVG.</p>
<p>Format choice has its own trade-offs. SVG is the best choice for print, but some office tools, older apps, and social platforms do not accept it — in those cases a high-resolution PNG is the right fallback, not a reason to fall back to JPEG. PDF can be a good carrier for print because it can hold the vector code, but only if the code inside the PDF is actually vector; a PDF with a small JPEG pasted inside it is just a JPEG with a fancier wrapper, so check what is inside before trusting the file extension.</p>
<p>Finally, sharpness is necessary but not sufficient. A perfectly sharp code can still fail if it is too small for its distance, if contrast is weak, if the quiet zone is crowded, if a logo covers too much of the centre, or if the destination itself is dead. Those are diagnosis questions, covered in order in <a href="/blog/why-is-my-qr-code-not-working/">the full troubleshooting guide</a>. If your reprint is sharp and still will not scan, work through that guide before reprinting again — a second reprint only helps if it changes the thing that is actually wrong.</p>
<p>Make the next code sharp from the start: generate it in the <a href="/#studio">free generator</a>, choose from 17 types, and export PNG up to 2048 px or infinitely scalable SVG — free for static codes, with no sign-up, no watermark, and no expiry. For sizing by use case, see the <a href="/blog/qr-code-print-size-guide/">print size guide</a>, and for a logo code, see <a href="/blog/add-logo-to-qr-code/">how to add a logo to a QR code</a>.</p>""",
  howto=[
  ('Find the original file', 'If you only have a JPEG, a screenshot, or a forwarded chat image, stop and regenerate — no edit restores detail compression already threw away.'),
  ('Export at the right size', 'PNG at 1024 px for cards and flyers, 2048 px for posters, SVG whenever the printer or designer accepts it. Above about 20 cm, SVG is the only format that keeps edges exact without an enormous file.'),
  ('Use PNG or SVG, never JPEG', 'PNG for screens and office printing, SVG for professional print. If a tool insists on JPEG, use its highest quality setting for a screen preview only, never as the print master.'),
  ('Keep proportions when resizing', 'Hold Shift or the lock icon so the squares stay square. Place the image at the final size, rather than placing it small and stretching it later.'),
  ('Keep the code dark on light, with a clear margin', 'Blur and low contrast compound each other. Keep a blank margin at least 4 modules wide on every side, as specified in ISO/IEC 18004, and keep text, logos, and decorative borders out of it.'),
  ('Match paper and printer to the job', 'Smooth or coated stock and a laser printer for small codes; matte finish where glare is a risk; larger size and higher error correction for rough or textured surfaces.'),
  ('Test-scan the real print', 'Print one copy at final size, step back to the real viewing distance, and scan it in the real lighting. A first-try scan means the batch is safe. If it hesitates, fix the export or the size now.'),
],
  faq=[
  ('Why does my QR code look blurry but still scan?', "Phones are forgiving — error correction rebuilds codewords that come back wrong or unreadable. But a code that scans in a bright office may fail in dim light or at arm's length. Sharp is safe; barely scanning is not."),
  ('What resolution do I need for a poster?', 'SVG is the best choice, because it scales without limit. If the printer needs a raster file, use PNG at 2048 px; a poster at 20 cm needs roughly 2,360 px at 300 pixels per inch, so a 512 px export will look soft at that size.'),
  ('PNG or SVG for print?', 'SVG whenever the printer or designer accepts it — it scales infinitely with zero blur. PNG at 1024 px for cards and flyers, or 2048 px for posters, is the fallback for office printing and apps that do not take SVG.'),
  ('Can I fix a blurry printed code without reprinting?', 'No. The blur is baked into the printed image. Reprint from a higher-resolution export (or SVG). Editing a dynamic code will not help — the pattern on paper is what it is, even though a dynamic code lets you change the destination behind a fresh print.'),
  ('Why does the same export look fine on screen but soft in print?', 'A screen shows the code small, so its pixels look tight. Paper shows the code at its true size, so the same pixel count spread over centimetres reveals the blur. Check the export against the print size before sending it to print.'),
  ('Will upscaling or a sharpening filter fix a blurry code?', 'No. Upscaling interpolates between the pixels you already have, so edges stay soft, only bigger. A sharpening filter can add halos that confuse a camera, and converting a JPEG to PNG does not undo JPEG damage. The only reliable repair is a fresh export from the original data at higher resolution, or as SVG.'),
],
  cta=dict(title="Make a sharp code",
           text="Export PNG up to 2048 px or infinitely scalable SVG. Free, no sign-up for static codes.",
           href="/#studio", btn="Open the studio"),
 ),
 dict(
  slug="how-to-scan-qr-code-on-phone",
  title="How to Scan a QR Code on Your Phone: iPhone & Android, No App Needed | FreeQrly",
  desc="No app needed: point your camera at the code. iPhone Camera and Control Center, Android camera and Google Lens — plus fixes for when it won't scan.",
  h1="How to scan a QR code <span class='hl hl-mint'>on your phone</span>",
  lede="No app to install — your phone already knows how. Here's where the scanner lives on iPhone and Android, and what to do when it won't read.",
  date="October 19, 2026", updated="November 3, 2026", dateModified="2026-11-03",
  datePublished="2026-10-19",
  mascot="scanner",
  body="""<p><strong>The short answer: open your phone's Camera app, point it at the code, and tap the link that appears.</strong> You do not need to download a scanner app, create an account, or press the shutter button. On a modern iPhone or Android phone, QR reading is built into the camera and into a few system shortcuts around it. The skill is knowing which shortcut fits each situation: the Camera app for a menu on the table, a dedicated scanner view for a ticket queue in dim light, and a saved-image method when the code is already on your own screen.</p>

<p>One habit covers all of them: read the preview before you tap. Your phone shows the link, the Wi-Fi network name, or the action the code wants to take before anything opens. That preview is your one chance to spot a code that does not belong where it sits. If the preview does not match the sign in front of you, stop before you tap.</p>

<h2>Which scanner to use, at a glance</h2>
<table>
<tr><th>Situation</th><th>Reach for this first</th><th>Why it fits</th></tr>
<tr><td>A code on paper, a poster, a menu, or a screen in front of you</td><td>The Camera app</td><td>Ready at once, works in the normal photo view</td></tr>
<tr><td>A queue, a gate, or a dark room with repeated scans</td><td>The dedicated scanner shortcut</td><td>Opens straight to scanning, flashlight at hand</td></tr>
<tr><td>Nothing happens in the Camera app</td><td>The Quick Settings scanner tile</td><td>Bypasses camera modes and goes straight to reading</td></tr>
<tr><td>A code already on your own screen or in a photo</td><td>The saved-image method for your phone</td><td>A camera cannot point at its own screen</td></tr>
<tr><td>A code that is small, damaged, or partly in shadow</td><td>Google Lens, or a second phone</td><td>A different reader sometimes succeeds where the first failed</td></tr>
</table>

<h2>On iPhone: Camera, Scan Code, and the lock screen</h2>
<p><strong>Method 1 — the Camera app.</strong> Open Camera, hold the phone so the whole code appears in the frame, and wait a moment. You do not need to take a picture. A link or action appears; tap it to open the destination. Apple describes exactly this flow — open Camera or Code Scanner, hold the device so the code appears, then tap the link — in its support guide for scanning a QR code with an iPhone or iPad. Keep the whole square in view, including the three large corner squares. If part of the code is cut off by the edge of the frame, the reader has to guess, and guessing is where failures start. Hold the phone steady and roughly parallel to the surface.</p>
<p><strong>Method 2 — the Scan Code control in Control Center.</strong> Open Control Center and tap the Scan Code button to open a dedicated scanner view. If you do not see it, touch and hold the background of Control Center, tap the Add a Control button, and choose Scan Code from the gallery. Set it up once and forget it until you need it: in a ticket line or a dim restaurant, one swipe and one tap puts you in a scanner with nothing else in the way, and the scanner view includes a flashlight. The Camera app is better when you might also want a photo; the Scan Code control is better when scanning is the whole job. Both use the same built-in reading, so the difference is speed, not capability. You can also open Camera from the lock screen, which matters at a gate or checkout where a scan is a one-handed, time-pressured job — though the preview rule still applies, even in a hurry.</p>

<h2>On Pixel: Camera suggestions and Quick Settings</h2>
<p><strong>Method 1 — the Camera app.</strong> Open the Camera app and point it at the code, making sure the entire code shows on screen. You do not need to take a picture; the camera recognises the code and shows a bubble or link, which you tap to open. Google's Pixel guide adds one setting worth checking if nothing appears: in the Camera app, open Settings, then More settings, and make sure Camera scan suggestions is turned on. That single toggle is the most common reason a Pixel camera stays silent in front of a perfectly good code, and it is worth checking before you conclude the code is at fault.</p>
<p><strong>Method 2 — the Quick Settings scanner.</strong> Swipe down from the top of the screen to open Quick Settings and tap Scan QR code. If you do not see the tile, swipe left for more buttons or tap the pencil icon to add it. A dedicated scanner opens; point it at the code. This is the fastest fallback when the Camera app is being stubborn. Google's troubleshooting advice is short: hold steady, use good light without glare, wipe a smudged lens, and move closer while keeping the whole square in frame. One more mode detail: on cameras built on Google's camera software, a code is read in the normal photo view, not in portrait or video mode, so switch back to the normal view first if you opened the camera to film something.</p>

<h2>On Samsung Galaxy: Camera, Quick Settings, and Gallery</h2>
<p>Samsung's support guide, updated in October 2026, lists several doors into the same scanner; in practice, start with the Camera app, keep Quick Settings as the fast backup, and use Gallery for a saved picture.</p>
<p><strong>Method 1 — the Camera app.</strong> Open Camera, point it at the code, and wait for the pop-up message; tap the pop-up to go to the code's information. You do not need to take a picture. If nothing appears, open Camera settings with the gear icon and make sure the Scan QR codes toggle is on. As with Pixel, this toggle is the first thing to check when a Samsung camera ignores a code, and Samsung's guide names it explicitly as the fix for a camera that will not scan.</p>
<p><strong>Method 2 — the Quick Settings panel.</strong> Swipe down from the top of the screen to open Quick Settings and tap Scan QR code; the Camera app launches into scanning. This scanner view gives quick access to the flashlight, which is genuinely useful in a dark venue: a code under a dim bar light is often a lighting problem, not a code problem. If the tile is missing, add it to the panel so it is there the next time you are standing in a queue. <strong>Method 3 — Gallery.</strong> If you have already photographed a code, open it in the Samsung Gallery app, select the image, and tap the Bixby Vision button; the phone reads the image and offers to open the link or copy it. The Quick Settings scanner offers a similar path: open it, tap the gallery image icon, choose the photo, and confirm. See <a href="/blog/scan-qr-code-from-image/">the guide to scanning a QR code from a picture</a> for these paths in full.</p>

<h2>Other Android phones: the same pattern, different labels</h2>
<p>Android has no single scanner, because each phone maker arranges the same pieces differently. The pattern, however, is consistent: a Camera app that reads codes in its normal photo view, a Scan QR code tile in Quick Settings, and Google Lens as the universal backup. If your phone is not a Pixel or a Samsung, work through the pattern in that order. First, open the Camera app and point it at a code in the normal photo view. If nothing appears, look in the camera's settings for a scanning toggle — the name varies by maker, so look for wording about QR codes, scanning, or suggestions — and switch it on. If there is no such toggle, or it is already on and nothing happens, swipe down for Quick Settings and look for the Scan QR code tile. If that is missing too, open Google Lens from the Google app or from inside the camera and point it at the code. Lens also reads saved images in Google Photos.</p>
<p><strong>A note on older phones.</strong> A phone old enough to lack any built-in reader is the one case where a separate scanner app is a reasonable answer. Pick one from the official app store with a clear, narrow permission request — camera access, and nothing else it does not need — and be wary of any scanner that asks for contacts, location, or an account before it will read a single code. Alternatively, skip the install entirely and use <a href="/scan/">the free scanner in your browser</a>, which reads a code from your camera or from an uploaded image with no install at all, and leaves nothing behind on the phone when you are done.</p>

<h2>Scenarios: matching the method to the moment</h2>
<p><strong>At a restaurant table,</strong> use the Camera app; the code is close and you want the menu in one tap, tilting the phone if a glossy laminated card glares under a downlight. <strong>At a gate or ticket check,</strong> use the dedicated scanner shortcut and have it open before you reach the front of the queue, since ticket codes are often time-sensitive. <strong>On a poster or shop window,</strong> step back until the whole code fits comfortably in the frame, and remember the sizing rule from the <a href="/blog/qr-code-print-size-guide/">print size guide</a>: as a rule of thumb, a code should be at least one-tenth as wide as the distance you scan it from. A code you cannot fit in the frame from where you stand is a code printed too small for its spot, and no phone setting fixes that. <strong>On a TV, laptop, or another phone's screen,</strong> point your camera at the other screen the same way you would point it at paper, but watch for glare on the glass and for the screen's own shimmer; tilt slightly for glare, hold steady for shimmer, and scan a login or pairing code promptly, since a refreshed code replaces the old one.</p>

<h2>When nothing happens: the phone-side checklist</h2>
<ol>
<li><strong>Whole code in frame?</strong> Pull back until all four corners and the quiet margin around the code are visible.</li>
<li><strong>Right camera mode?</strong> Use the normal photo view, not portrait or video; use the dedicated scanner shortcut if your camera offers one.</li>
<li><strong>Scanning switched on?</strong> Check the toggle: Camera scan suggestions on Pixel, Scan QR codes in Samsung's camera settings, the Scan Code control on iPhone.</li>
<li><strong>Lens clean?</strong> Wipe it with a soft cloth; a smudged lens blurs every code equally.</li>
<li><strong>Light helping or hurting?</strong> Add light in a dark room, remove glare in a bright one, keep your shadow off the code.</li>
<li><strong>Code itself readable?</strong> Check the three corner squares, the contrast, and any damage, fading, or curve that distorts the grid.</li>
<li><strong>Second phone test:</strong> if another phone reads the code and yours does not, the problem is your phone's settings, lens, or light — not the code.</li>
</ol>
<p>If the code reads but the destination fails — a dead link, a moved page, a form that no longer exists — that is a different failure with a different owner. The code did its job; the page behind it did not. The full chain of code-side failures is covered in <a href="/blog/why-is-my-qr-code-not-working/">why your QR code won't scan</a>, and blurry print in particular in <a href="/blog/why-is-my-qr-code-blurry/">why your QR code is blurry</a>. If none of the seven steps above helps, the next step is a different reader or a different phone, not more fiddling with your own.</p>

<h2>The honest comparison: built-in scanning versus scanner apps</h2>
<p>Scanner apps exist, and for a phone with no built-in reader they are a genuine solution. For everyone else, they are a worse version of something the phone already does. The built-in camera reads standard codes, shows the same preview, and opens the same destinations, without an account, without a subscription screen, and without a feed of ads between you and a menu. A scanner app adds a middleman to a transaction that does not need one, and that middleman is usually paid for with attention, data, or both. The case for an app is narrow but real: an older phone with no built-in reader needs one, or a browser scanner, and a person who scans codes all day for work may want a history or bulk reading. The case against an app, for everyday scanning, is just as concrete: many scanner apps show ads, and some ask for permissions far beyond the camera — contacts, location, or an account that ties your scanning history to an identity. The built-in camera, by contrast, reads the code and moves on; it does not keep a diary of your scans.</p>

<h2>Safety: the preview is the whole defence</h2>
<p>A QR code hides its destination by design. You cannot read a URL from looking at the pattern, which is exactly why a code is such an effective vehicle for a link you would never tap if you could see it. The defence is not to avoid codes — it is to read the preview, every time, and to treat the preview as a decision, not a formality. The United States Federal Trade Commission warned about this pattern in a consumer alert dated December 6, 2023: scammers cover genuine codes with their own stickers — on parking meters, for example — or send codes in unexpected messages, and a scanned code can lead to a spoofed site that looks real, where anything entered can be stolen, or to malware. The FTC's advice in that alert is the same habit this guide recommends: inspect the URL before opening it, look for misspellings or a switched letter in a familiar name, and do not scan a code in an unexpected message, especially one urging immediate action. Read the preview, check for tampering such as a sticker pasted over another code, and check the context: did you expect this code, in this place, for this purpose? Failing any one of those checks is enough to stop.</p>

<h2>Make a code and test it on your own phone</h2>
<p>The fastest way to learn all of this is to make a code and scan it yourself. FreeQrly's generator covers 17 types — links, Wi-Fi, contact cards, events, and more — and a static code made there is free with no sign-up, no watermark, and no expiry, so a test code costs nothing and keeps working. Print it, place it where you would use it, and scan it with the Camera app, then with the dedicated scanner shortcut, then from a saved photo. If it reads in all three, your size, contrast, and quiet zone are right. If the destination behind your code may change, a dynamic code is the right tool instead: it stays editable after printing and reports scan statistics, with a free account. Dynamic codes are free for 20 codes, currently with unlimited availability during the promotional period, and with unlimited scans. For a batch of codes, <a href="/batch-qr-code/">batch generation</a> makes one code per link and downloads them together. Start with one static test code, scan it on your own phone, and build from a result you have actually seen work.</p>""",
  faq=[
  ('How do I scan a QR code on my iPhone?', 'Open the Camera app, hold the phone so the whole code is in frame, and tap the link that appears. Alternatively, open Control Center and tap the Scan Code button for a dedicated scanner view; if the button is missing, add it from the Control Center gallery.'),
  ('How do I scan a QR code on a Pixel phone?', "Open the Camera app and point it at the code, making sure the whole square shows on screen. If nothing appears, check that Camera scan suggestions is turned on in the Camera app's Settings, then More settings. The Quick Settings Scan QR code tile is the fastest fallback."),
  ('How do I scan a QR code on a Samsung Galaxy phone?', 'Open the Camera app and point it at the code, then tap the pop-up. If nothing appears, open Camera settings and make sure the Scan QR codes toggle is on. You can also swipe down for Quick Settings and tap Scan QR code, or read a saved picture in the Gallery app with Bixby Vision.'),
  ('Do I need to download a QR scanner app?', 'No, not for standard codes on a modern phone. The built-in camera reads them with the same preview as any app. A separate scanner is a reasonable answer only for a phone with no built-in reader, or for work that genuinely needs a scan history or bulk reading.'),
  ("Why won't my phone scan the QR code?", 'Work the phone-side checklist in order: whole code in frame, normal photo view rather than portrait or video, scanning switched on, clean lens, good light without glare, intact corner squares and contrast, and finally a second-phone test. If another phone reads it, the problem is your phone; if none does, it is the code.'),
  ("Can I scan a QR code that is on my own phone's screen?", 'Not with the camera, since a camera cannot point at its own screen. Screenshot the code or save the image, then read it from the image — see the guide to scanning a QR code from a picture.'),
  ('Is it safe to scan a QR code in a public place?', 'Read the preview before you tap, and check that the domain matches the sign in front of you, that the code shows no sign of tampering such as a sticker pasted over another code, and that you expected this code in this place. Failing any one of those checks is enough to stop.'),
],
  sources=[
  ('http://www.iso.org/standard/83389.html', 'ISO/IEC 18004:2024', 'RETAINED from the original post. The QR Code symbology specification; the original description states it defines the four error-correction levels (L 7%, M 15%, Q 25%, H 30%). The body uses only those four percentages, plus the 4-module quiet zone from the same standard. Page accessed 2026-11-03; the ISO listing itself carries no public summary with the figures, which were corroborated against standard explainers during verification.'),
  ('https://support.apple.com/en-us/102680', 'Apple Support: Scan a QR code with your iPhone or iPad', 'ADDED. Published September 14, 2026 (shown on the page, verified by opening it 2026-11-03). Supports: open Camera or Code Scanner, hold the device so the code appears, tap the link; adding the Scan Code control by touching and holding the Control Center background and tapping Add a Control.'),
  ('https://support.google.com/pixelphone/answer/16561572?hl=en', 'Google Support: Scan QR codes with your Pixel phone', 'ADDED. Page accessed 2026-11-03; no publication date shown on the page. Supports: Camera scan suggestions toggle (Settings, then More settings), the Quick Settings Scan QR code tile, and the troubleshooting list (hold steady, good light without glare, clean lens, move closer while keeping the whole square in frame).'),
  ('https://www.samsung.com/uk/support/mobile-devices/how-to-scan-qr-code-on-your-galaxy-phone-or-tablet/', 'Samsung Support: How to scan QR codes on your Samsung phone', "ADDED. Updated October 6, 2026 (shown on the page, verified by opening it 2026-11-03). Supports: Camera app scanning, the Quick Settings Scan QR code tile, the Camera settings Scan QR codes toggle, Gallery with Bixby Vision, and the Quick Settings scanner's gallery image icon for saved pictures."),
  ('https://consumer.ftc.gov/consumer-alerts/2023/12/scammers-hide-harmful-links-qr-codes-steal-your-information', 'FTC: Scammers hide harmful links in QR codes to steal your information', 'ADDED. Consumer alert dated December 6, 2023 (FTC listing; page verified by opening it 2026-11-03). Supports: scammers covering genuine codes with their own stickers, including on parking meters, and sending codes in unexpected messages; a scanned code can lead to a spoofed site or malware; inspect the URL before opening it and do not scan a code in an unexpected message urging immediate action.'),
  ('https://support.google.com/camerafromgoogle/answer/12033278?hl=en', 'Google Support: Scan QR codes on Camera from Google', 'ADDED. Page accessed 2026-11-03 via search result; no publication date shown. Supports only the single mode note used in the body: a QR code cannot be scanned in portrait and video mode on Camera from Google.'),
],
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
  date="October 19, 2026", updated="November 3, 2026", dateModified="2026-11-03", sources=[
  ('https://support.google.com/business/answer/16816815?hl=en', 'Google Business Profile Help — Create a Google link or QR code to request reviews', 'Supports the steps (Business Profile, Read reviews, Get more reviews, Copy), the note that review QR codes can only be generated on a computer browser, sharing via email, WhatsApp, or Facebook, and the note that offering incentives for reviews is fake engagement and strictly prohibited. Page shows no publication date; accessed 2026-11-03.'),
  ('https://support.google.com/business/answer/7400114?hl=en&visit_id=639259422779627628-1285679715&rd=1', 'Google Business Profile Help — Prohibited & restricted content', 'Supports: reviews must reflect a genuine experience and be genuine and unbiased; reviews paid for directly or in kind are fake engagement; merchants may not offer incentives (payment, discounts, free goods/services) for posting, revising, or removing a review; merchants may not discourage or prohibit negative reviews or selectively solicit positive reviews; merchants should not require or pressure users to review on the premises or request specific content (including staff quotas); incentivized or biased reviews are removed from Maps; soliciting genuine content without incentives or influence is allowed. Page crawled 2026-10-16, no publication date shown; accessed 2026-11-03.'),
  ('https://support.google.com/business/answer/3474122?hl=en-GB', 'Google Business Profile Help — Tips to get more reviews', 'Supports the note that offering incentives (free or discounted goods or services) for posting, changing, or removing reviews is fake engagement and strictly prohibited, and the reply guidance: keep replies professional, polite, short, and specific, and move complex complaints to a private channel. Page shows no publication date; accessed 2026-11-03.'),
  ('https://Business.FTC.gov/system/files/ftc_gov/pdf/2025-Fake-Review-Warning-Template.pdf', 'FTC — Consumer Review Rule warning letter template', 'Supports: the Trade Regulation Rule on the Use of Consumer Reviews and Testimonials (16 CFR Part 465) became fully effective October 21, 2024; it prohibits providing compensation or other incentives expressly or implicitly conditioned on a review expressing a particular sentiment, and authorizes the FTC to seek civil penalties for knowing violations. Document dated December 22, 2025.'),
  ('https://support.apple.com/en-us/102680', 'Apple Support — Scan a QR code with your iPhone or iPad', 'Supports the test-scan method described in the body: open Camera or the Control Center Scan Code control, hold the phone so the code appears in frame, and tap the link that appears. Published September 14, 2026.'),
],
  datePublished="2026-10-19",
  mascot="success",
  body="""<p>Google reviews decide who gets picked — and the businesses with the most reviews did not get them by luck. They asked, at the right moment, with zero friction. A QR code pointing straight at your Google review form turns “please leave us a review” into a single scan. Get the link Google itself issues, turn it into a code, put it where a satisfied customer is already standing, and ask once, plainly. Everything else in this guide is detail around that sequence.</p>
<p>The reason a code works where a follow-up email often does not is timing. A request that arrives days later competes with everything else in an inbox. A code on the table, the receipt, or the card handed over at the end of a visit meets the customer while the experience is still fresh. The code does not persuade anyone. It removes the steps between “I would review this place” and the review form: no searching for the business name, no picking the right listing among lookalikes, no hunting for the review button.</p>
<h2>Where each placement earns its scan</h2>
<p>Placement is the whole game, and different placements catch customers at different moments. Use this table to pick placements for your business rather than printing the same sign everywhere.</p>
<table>
<tr><th>Placement</th><th>Customer moment</th><th>What to print beside the code</th><th>Static or dynamic</th></tr>
<tr><td><strong>Table tent (restaurants and cafés)</strong></td><td>During the meal, satisfaction still building</td><td>“Enjoyed your meal? Scan to review us on Google.”</td><td>Static, unless you run several sites</td></tr>
<tr><td><strong>Receipt</strong></td><td>At payment, the visit just concluded</td><td>“Tell us how we did — scan to review us on Google.”</td><td>Static for a single site; dynamic if you want to compare receipt scans with counter scans</td></tr>
<tr><td><strong>Checkout counter</strong></td><td>At purchase, satisfaction peaks</td><td>“Love it? Scan to review us on Google.”</td><td>Static</td></tr>
<tr><td><strong>Business card handed over at the end of a visit</strong></td><td>Services: plumber, tutor, clinic, salon</td><td>“Thanks for having us — scan to review us on Google.”</td><td>Static, or dynamic if the card design is reprinted rarely and the link might change</td></tr>
<tr><td><strong>Invoice sticker</strong></td><td>After the work, when the bill is in hand</td><td>“Happy with the job? Scan to review us on Google.”</td><td>Static</td></tr>
<tr><td><strong>Delivery and takeaway packaging</strong></td><td>At home, with the food in front of them</td><td>“Enjoying it? Scan to review us on Google.”</td><td>Static</td></tr>
<tr><td><strong>Email signature</strong></td><td>Every routine email, with no extra ask</td><td>A short link line: “Review us on Google”</td><td>A link, not a code — signatures travel by email, so a clickable link beats a printed code</td></tr>
</table>
<p>Two notes on that table. A business card code is easy to print too small: a code crammed into a corner gets ignored, while a 5 cm code on a table tent gets scanned. And an email signature is the one placement where the code itself is the wrong tool — the reader is already on a screen, so give them the review link as text they can tap. The link goes where people read, the code goes where people stand.</p>
<h2>Step 1 — get your Google review link</h2>
<p>You need the direct link to your review form, not just your business listing. Google issues this link from your Business Profile, and its current help page gives these steps:</p>
<ol>
<li>On a computer, go to your <a href="https://support.google.com/business/answer/16816815?hl=en">Business Profile</a> while signed in to the Google account that manages it.</li>
<li>Select <strong>Read reviews</strong>, then <strong>Get more reviews</strong>.</li>
<li>Select <strong>Copy</strong> to copy the review link. The link looks like <code>g.page/r/…/review</code> — a short link that opens your review form directly.</li>
</ol>
<p>Two details matter here. First, the same panel also holds a QR code you can save by right-clicking it and choosing “Save image as” — but Google notes that review QR codes can only be generated on a computer browser, not on a mobile device, so do this step at a desk. Second, Google's own code is plain: no branding, no frame, no instruction line. For a counter sign or table tent, generating a styled code from the same link — logo, frame, and a line telling people what happens when they scan — is usually worth the extra minute. The destination is identical either way.</p>
<p>Test the link before anything goes to print. Open it in a private browser window and confirm it lands on your business's review form, not on a general listing or a similarly named business. A printed code with the wrong destination teaches customers that your codes lead nowhere useful.</p>
<h2>Step 2 — turn it into a QR code</h2>
<p>Paste the link into a <a href="/google-review-qr-code/">Google review QR code generator</a> — it takes seconds, it is free, and a static code never expires. Print it at a decent size, keep dark ink on a light background, and leave a clear quiet margin around the code. The <a href="/blog/qr-code-print-size-guide/">print size guide</a> covers sizing in detail; the short version is that a code people have to lean in to read is a code people will not scan.</p>
<p>Now choose between static and dynamic, because the choice is harder to reverse once hundreds of cards are printed:</p>
<ul>
<li><strong>Static is the default for most shops.</strong> The review link lives inside the pattern itself, the code needs no account, and it keeps working as long as your Business Profile exists. One static code, printed well and placed well, is all most single-site businesses need.</li>
<li><strong>Dynamic earns its keep in two situations.</strong> First, when the destination might change: if Google ever changes your review link, or you move the request to a different page, a dynamic code lets you change the destination from your Dashboard without reprinting. Second, when you want to compare placements: give the counter, the receipt, and the delivery bag each their own dynamic code, and the scan statistics show which placement actually gets scanned. Dynamic codes are free to start with a sign-in, editable after printing, and come with scan statistics, with 20 codes on the free account and unlimited scans during the limited-time promotion. The trade-off is honest: a dynamic code points at a short link on a server, so it depends on that service staying up, while a static code depends on nothing but the printed pattern and the destination.</li>
</ul>
<p>If you run several locations, do not share one code across them. Each location has its own Business Profile and its own review link, so make one code per location, label the files by location name, and check each one before printing.</p>
<h2>Step 3 — put it where the moment happens</h2>
<p>The code has to be in front of a satisfied customer <em>before</em> they leave. Work through your own customer journey and mark every point where someone is happy, unhurried, and holding their phone — those are your placements, and everywhere else is decoration.</p>
<h3>Restaurants and cafés</h3>
<p>Table tents and the receipt are the two placements that matter. The table tent catches people mid-meal, when they are relaxed and the phone is already on the table. The receipt catches them at the end, when the whole visit is fresh. A code on the front door, by contrast, is scanned by people arriving — the one moment when they have nothing to review yet. Match the wording to the moment: “Enjoyed your meal? One scan.”</p>
<h3>Retail and salons</h3>
<p>The checkout counter is the natural spot — satisfaction peaks at purchase, and the customer is already standing there with their phone in hand while the card payment goes through. Put the code at eye level, not flat on the counter where bags cover it, and not behind the till where only staff can see it. A small standing sign next to the card reader outperforms a poster on the far wall.</p>
<h3>Services: plumbers, tutors, clinics, salons</h3>
<p>For work done at a customer's home or in an appointment, the handover moment is everything. A card handed over at the end of the visit — or a sticker on the invoice — travels home and sits on the kitchen counter as a reminder. The spoken ask matters as much as the card: “If you were happy with the work, this card takes you straight to our Google reviews.” Without that sentence, the card is just another piece of paper.</p>
<h3>Delivery and takeaway</h3>
<p>A sticker on the bag or box puts the code in front of the customer at the exact moment they open the food. The food is the reminder, and the code is already in their hands. Keep the wording to one line: a delivery bag has limited space and a short attention window.</p>
<h3>Email signatures and follow-up messages</h3>
<p>For businesses that already email customers — invoices, booking confirmations, thank-you notes — the signature is a quiet, permanent placement. Add the review link as a short text line rather than a code image, since the reader is already on a screen. The same applies to a follow-up message after the visit: one short message, one link, sent the same day while the visit is still fresh.</p>
<h2>What to write next to it</h2>
<p>A bare code gets fewer scans than a code with a reason. Keep it short and specific:</p>
<ul>
<li>“Love your visit? Scan to review us on Google.”</li>
<li>“Enjoyed your meal? One scan to review us.”</li>
<li>“Happy with the job? This code takes you to our Google reviews.”</li>
</ul>
<p>Asking for <em>Google</em> reviews by name matters — customers default to whichever platform is easiest. Wording that hints at a star rating (“Leave us five stars”) crosses from asking into steering, and Google's policy treats steering as a violation, as the compliance section below explains.</p>
<h2>The compliance rules, verified against Google's own pages</h2>
<p>This section only states policy points that appear on Google's official support pages, because review policy is exactly the kind of topic where secondhand summaries drift. Google's <a href="https://support.google.com/business/answer/7400114?hl=en&amp;visit_id=639259422779627628-1285679715&amp;rd=1">prohibited and restricted content</a> page and its <a href="https://support.google.com/business/answer/3474122?hl=en-GB">tips for getting more reviews</a> page agree on the following:</p>
<ul>
<li><strong>Reviews must reflect a genuine experience, and be genuine and unbiased.</strong> That is the foundation everything else hangs from. A review from someone who never visited, or a review written at the business's dictation, fails this test no matter how it was obtained.</li>
<li><strong>Never offer incentives for a review.</strong> Google does not allow merchants to offer payment, discounts, free goods, or free services in exchange for posting a review, revising a review, or removing a negative review. Incentivized or biased reviews are removed from Maps. This covers the obvious cases — a discount for a review, a free dessert for a review — and the less obvious ones, like an entry into a prize draw for reviewers or a benefit offered to take a negative review down.</li>
<li><strong>Do not discourage negative reviews, and do not ask only the customers you expect to be happy.</strong> Google's policy lists both as rating manipulation: discouraging or prohibiting negative reviews, and selectively soliciting positive reviews. The compliant version is simple and also better business: ask every customer, the same way, at the same point in the journey. A review profile built only from hand-picked happy customers is both a policy risk and a credibility problem — readers can tell.</li>
<li><strong>Do not require or pressure people to review while they are on the premises, and do not script the content.</strong> Google's policy says merchants should not require or pressure users to leave ratings or write reviews while on the premises, and should not request that specific content be included — including staff quotas or reviews mentioning a particular staff member. The practical line: one visible code plus one spoken, voluntary ask is compliant; standing over a customer until they post is not.</li>
<li><strong>Asking itself is allowed.</strong> Google expressly allows merchants to solicit or encourage content that does represent a genuine experience, provided no incentive is offered and no attempt is made to influence the rating or the contents. The QR code is simply the lowest-friction form of that allowed ask.</li>
</ul>
<p>Beyond Google's own rules, United States businesses should know that the Federal Trade Commission's Consumer Reviews rule, in effect since October 21, 2024, prohibits providing compensation or other incentives conditioned on a review expressing a particular sentiment, and authorizes civil penalties for knowing violations. Note the difference in scope: the FTC rule targets incentives tied to a sentiment, while Google's wording bars incentives for posting a review at all.</p>
<p>Compliance is not just about avoiding removal. A business that answers its reviews gets more of them, because reviewers can see they are read. Google's tips page advises keeping replies professional, polite, short, and specific rather than sending the same thank-you to everyone, and moving a complex complaint to a private channel rather than arguing in public. Reply to the negative reviews too, calmly and without sharing the reviewer's private information.</p>
<h2>The honest comparison: what a review code cannot do</h2>
<p>A review code is a friction remover, not a reputation machine, and it is worth stating its limits plainly before you print a hundred cards:</p>
<ul>
<li><strong>It cannot create satisfaction.</strong> A code in front of an unhappy customer produces, at best, nothing, and at worst an honest negative review. Fix the experience first.</li>
<li><strong>It cannot replace asking.</strong> The code is passive. In every placement above, it works best paired with one spoken sentence at the right moment, and then silence.</li>
<li><strong>It cannot target only happy customers.</strong> Any system that filters — a code shown only after a good outcome, a request sent only to customers who smiled — breaks Google's rule against selective solicitation. Ask everyone and reply to all of it.</li>
<li><strong>It cannot fix a broken link by itself.</strong> A static code holds the link it was printed with. If your review link changes, a static code keeps pointing at the old destination. That is the one case where a dynamic code pays for itself: change the destination once in the Dashboard and every printed copy follows.</li>
</ul>
<h2>A few honest tips</h2>
<ul>
<li><strong>Ask, don't beg.</strong> One visible code plus a spoken “we'd love a review” outperforms five signs.</li>
<li><strong>Start with one placement, not five.</strong> Put the code where your happiest moment already happens and run it for a few weeks before printing it everywhere.</li>
<li><strong>Reply to reviews.</strong> A business that answers reviews gets more of them; reviewers can see you read them. Keep replies short, specific, and human.</li>
<li><strong>Track what works.</strong> If you want to know which placement drives scans, use a dynamic code for one location and compare.</li>
</ul>
<p>Ready to make yours? Copy your review link from your Business Profile, paste it into the <a href="/google-review-qr-code/">Google review QR code generator</a>, and print it for the place your happiest customers already stand. Static codes are free, need no sign-up, and never expire. If the destination might change or you want to compare placements, make it dynamic instead — free with a sign-in, editable after printing, with scan statistics and unlimited scans.</p>""",
  faq=[
  ('How do I create a QR code for Google reviews?', 'Copy your Google review link from your Business Profile (Read reviews, then Get more reviews, then Copy), paste it into a free QR code generator, and print the code. Static codes are free and never expire. Note that Google generates its own review QR code only on a computer browser, not on a mobile device.'),
  ('Where should I put my Google review QR code?', 'Wherever a satisfied customer stands before leaving: restaurant tables and receipts, retail checkout counters, service invoices, or delivery packaging. For email, use the review link as a clickable text line in your signature instead of a code image, since the reader is already on a screen.'),
  ('Do Google review QR codes expire?', 'A static QR code never expires — it holds your review link directly. As long as your Google Business Profile exists, the code keeps working. A dynamic code keeps working too, as long as the service behind its short link stays up and you do not delete the code.'),
  ('Should I offer a discount for a Google review?', 'No. Google prohibits offering payment, discounts, free goods, or free services in exchange for posting, revising, or removing a review, and incentivized or biased reviews are removed from Maps. In the United States, the FTC Consumer Reviews rule also prohibits incentives conditioned on a review expressing a particular sentiment. Ask at the right moment instead — that is what the QR code is for.'),
  ('Should I use a static or a dynamic code for Google reviews?', 'Static for most single-site businesses: free, no sign-up, never expires. Dynamic when the destination might change or when you want to compare placements — give the counter, the receipt, and the delivery bag each their own dynamic code and compare their scan statistics. Dynamic codes are free with a sign-in, editable after printing, and come with scan statistics.'),
  ('Can I ask customers for a review while they are still in my shop?', "Yes, with one spoken, voluntary ask — but do not require or pressure anyone to review while on the premises, and do not hand them wording to copy. Google's policy bars requiring or pressuring users to leave ratings or reviews on the premises and bars requesting specific content, including staff review quotas."),
  ('What if my Google review link changes after I printed cards?', 'A static code keeps pointing at the old link, so you would need to reprint. A dynamic code can be repointed in the Dashboard without reprinting: change the destination once and every printed copy follows. If you print static codes, keep a note of which link each batch carries and re-test the link after any change to your Business Profile.'),
],
  cta=dict(title="Make your review QR code",
           text="Paste your Google review link, get a printable code in seconds. Free, no sign-up for static codes.",
           href="/google-review-qr-code/", btn="Create review code"),
 ),
]

POSTS += [
 dict(
  slug="share-wifi-with-qr-code",
  title="How to Share WiFi with a QR Code | FreeQrly",
  desc="Share your WiFi password with a QR code: guests scan and join, no spelling, no typing. Free and private — for a static code, the password never leaves your browser.",
  h1="Share your WiFi with <span class='hl hl-mint'>a QR code</span>",
  lede="Guests ask for the password. You point at the fridge. One scan and they're online — no spelling, no typos, no reading it off the router sticker.",
  date="October 28, 2026",
  datePublished="2026-10-28",
  mascot="wifi",
  body="""
<p>Every host knows the ritual: a guest arrives, asks for the WiFi password, and you recite a string of capitals, numbers, and symbols while they mistype it twice. A WiFi QR code ends it. You print one code, stick it where guests look, and their phone joins the network the moment they scan — no typing at all.</p>

<h2>What a WiFi QR code holds</h2>
<p>Three things: the network name (SSID), the password, and the security type — usually WPA or WPA2 on a home router, WEP on very old hardware, or nothing at all for an open network. A phone that scans the code reads all three and joins directly, instead of opening settings and typing.</p>

<h2>Make one in three steps</h2>
<ol>
<li><b>Find your network details.</b> The name and password are usually on a sticker on the router. If you changed them, use the ones you set — the code has to match the router exactly, including capitals.</li>
<li><b>Generate the code.</b> In the <a href="/wifi-qr-code/">WiFi QR code generator</a>, pick the WiFi type, enter the network name, password, and security type. The code appears instantly.</li>
<li><b>Print it and put it where guests look.</b> Fridge door at home, counter card in a café, the welcome book in an Airbnb, the reception desk in an office. At least 2 × 2 cm on print so phones read it at arm's length.</li>
</ol>

<h2>Which phones join from a scan?</h2>
<p>iPhones on iOS 11 and later join straight from the Camera app — point, tap the notification, done. Most Android phones on Android 10 and later do the same from the camera or from WiFi settings. No extra app needed on either side, and guests never see the password itself.</p>

<h2>The honest security note</h2>
<p>A static WiFi code is convenient because the password lives inside the pattern — which also means anyone who photographs the code can join your network. For a home, a café, or a rental, that is exactly the trade you want: guests are supposed to be online. Two rules keep it sane:</p>
<ul>
<li><strong>Generate it privately.</strong> A static code is drawn entirely in your browser — your password is never uploaded or stored anywhere. For extra peace of mind, load the page, disconnect from the internet, then type.</li>
<li><strong>If the code leaks somewhere it shouldn't, change the password and reprint.</strong> A static code can't be edited after printing, but making a new one is free and takes a minute.</li>
</ul>

<h2>Hidden networks and tricky routers</h2>
<p>Hidden networks work the same way — enter the exact network name and the phone connects without ever seeing it in a list. For WPA3 routers, pick the WPA2/WPA option if WPA3 isn't listed; most WPA3 routers accept WPA2 clients. And if a guest's phone refuses to join, check the password's capitals first — that is the cause almost every time.</p>

<p>Want the code itself? <a href="/wifi-qr-code/">Make your WiFi QR code</a> — free, no sign-up for static codes, and it never expires.</p>
""",
  howto=[
    ("Find your network details",
     "Network name and password from the router sticker, or the ones you set yourself. Capitals must match exactly."),
    ("Generate the code",
     "In the WiFi QR code generator, pick the WiFi type and enter the name, password, and security type."),
    ("Print it at least 2 × 2 cm",
     "PNG at 1024 px or higher. Stick it where guests look: fridge, counter, welcome book."),
    ("Test-scan before guests arrive",
     "Point your own phone at the print. If it joins on the first try, you're done."),
  ],
  faq=[
    ("Is my WiFi password safe in a QR code?",
     "For a static code, yes — it is drawn entirely in your browser and never uploaded or stored. Anyone who photographs the printed code can join, so treat it like a guest key: fine for homes, cafés, and rentals, and reprint if it leaks."),
    ("Which phones can scan a WiFi QR code?",
     "iPhones on iOS 11+ join straight from the Camera app; most Android phones on Android 10+ do the same from the camera or WiFi settings. No extra app needed."),
    ("Does it work with WPA3 or hidden networks?",
     "Choose the security type that matches your router (WPA, WPA2, WEP, or open). Enter a hidden network's name exactly and it connects the same way."),
    ("What if I change my WiFi password later?",
     "A static code can't be edited, so print a fresh one — it's free and takes a minute. That's also why the code is best for networks whose password rarely changes."),
  ],
  cta=dict(title="Make your WiFi QR code",
           text="Guests scan and they're online. Free, no sign-up for static codes.",
           href="/wifi-qr-code/", btn="Open the studio"),
 ),
 dict(
  slug="bulk-qr-codes",
  title="Bulk QR Codes: Generate Dozens at Once, Free | FreeQrly",
  desc="Generate QR codes in bulk: paste up to 50 links, get 50 print-ready codes, download them as one ZIP. Free, no sign-up for static codes, no watermark.",
  h1="Dozens of codes, <span class='hl hl-honey'>one download</span>",
  lede="Fifty product pages, fifty codes, one afternoon you don't have to spend making them one by one. Paste the links, download a ZIP, done.",
  date="October 28, 2026",
  datePublished="2026-10-28",
  mascot="batch",
  body="""
<p>Making one QR code takes seconds. Making fifty, one at a time, takes an afternoon — and the fiftieth always has a typo. Bulk generation exists for exactly this job: you paste a list of links, every link becomes its own code, and you download the whole set in one ZIP.</p>

<h2>How it works</h2>
<ol>
<li><b>Paste your links, one per line.</b> Up to 50 at a time in the <a href="/batch-qr-code/">batch QR code generator</a>.</li>
<li><b>Hit Generate all.</b> Every link becomes its own QR code, previewed in a grid.</li>
<li><b>Download the ZIP.</b> One click packs them all as print-ready PNGs at 1024 px, named qr-1.png, qr-2.png, and so on. Need more than 50? Run another batch — there's no daily cap and no account to hit.</li>
</ol>

<h2>Where bulk codes earn their keep</h2>
<ul>
<li><strong>Product packaging and labels.</strong> One code per product page, manual, or reorder link — printed straight onto the pack.</li>
<li><strong>Events.</strong> One code per ticket or per check-in point, generated in a single pass instead of a long evening of clicking.</li>
<li><strong>Real estate and retail.</strong> One code per listing or per shelf item, each opening its own page.</li>
<li><strong>Menus and locations.</strong> One code per branch or per table, all from the same list.</li>
</ul>

<h2>Three habits that save reprints</h2>
<p><strong>Check the list before you generate.</strong> A wrong link becomes a wrong code, fifty times over if it's repeated. Skim the list once — especially the first and last lines, where paste errors hide.</p>
<p><strong>Test-scan the first and last codes.</strong> If those two read on the first try, the middle ones will too — they're rendered the same way. Test on a print, not just on screen, if they're going to paper.</p>
<p><strong>Keep the print size honest.</strong> A code on a label still needs at least 2 × 2 cm and dark ink on a light background, with its quiet margin clear. Batch output is print-ready, but a tiny label undoes that.</p>

<h2>What bulk codes are — and aren't</h2>
<p>Batch codes are static: the link lives inside each pattern, so they never expire and need no sign-up. That also means a batch code can't be edited after printing — if a link changes, regenerate that one code (or the batch) and reprint. Want a logo on every code? Upload it once and it applies across the batch, with error correction raised automatically so every code stays scannable.</p>

<p>Ready? <a href="/batch-qr-code/">Generate your batch</a> — free, no watermark, no account for static codes.</p>
""",
  howto=[
    ("Paste your links, one per line",
     "Up to 50 at a time in the batch QR code generator. Skim the list once for paste errors."),
    ("Hit Generate all",
     "Every link becomes its own QR code, previewed in a grid."),
    ("Download the ZIP",
     "One click packs print-ready 1024 px PNGs, named qr-1.png, qr-2.png, and so on."),
    ("Test-scan first and last",
     "If those two read on the first try, the rest will too. Test on print if they're going to paper."),
  ],
  faq=[
    ("How many QR codes can I make at once?",
     "Up to 50 per batch. Need more? Run another batch — there's no daily cap or account to hit."),
    ("Is batch generation really free?",
     "Yes. Many generators charge a subscription for bulk export; here it's the same free tool, no watermark, no sign-up for static codes."),
    ("What format do the downloads come in?",
     "A single ZIP containing high-resolution PNGs (1024 px), each named qr-1.png, qr-2.png, and so on — ready for print."),
    ("Can I add my logo to batch codes?",
     "Upload your logo once and it applies across the batch, with error correction raised automatically so every code stays scannable."),
    ("Can I edit a batch code after printing?",
     "Batch codes are static, so no — if a link changes, regenerate that code and reprint. For editable codes, use a dynamic code instead."),
  ],
  cta=dict(title="Generate your batch",
           text="Paste up to 50 links, download one ZIP of print-ready codes. Free.",
           href="/batch-qr-code/", btn="Open batch mode"),
 ),
 dict(
  slug="add-logo-to-qr-code",
  title="How to Add a Logo to a QR Code (and Keep It Scannable) | FreeQrly",
  desc="Put your logo in the center of a QR code: upload a square PNG, keep it under ~30% of the code, let error correction do its job. Free, no watermark, still scans.",
  h1="Your logo, <span class='hl hl-blush'>in the middle</span> — still scannable",
  lede="A logo makes a code yours. It also covers up part of the pattern. Here's how to have both: logo dead center, code still scanning on the first try.",
  date="October 28, 2026", updated="November 3, 2026", dateModified="2026-11-03",
  datePublished="2026-10-28",
  mascot="logo-customize",
  body="""<p>A logo in the middle of a QR code works when three things are true: the logo stays small, the code's error correction is set high, and nothing important is covered. In practice that means a square logo with a transparent background, centered, kept under about 30% of the code area as a ceiling — and smaller if you want a safety margin — printed dark on light, with a clear margin around the whole code. Do that, test the printed piece on two phones, and the code reads on the first try while still looking unmistakably like your brand.</p>

<p>That short version hides one honest tension, and this guide does not dodge it: 30% is a ceiling, not a target. The highest error-correction level can rebuild about 30% of the data, so a logo approaching that limit leaves almost nothing in reserve for a scuffed print, a dim room, or an older phone. Many design guides therefore advise keeping a centered logo around 20–25% of the code area, so wear and tear still has room to be absorbed. If your logo must be large, the rest of this guide shows what to trade away — shorter content, a bigger print, or a simpler mark — instead of hoping the ceiling will save you.</p>

<h2>Why a logo can work at all: error correction</h2>

<p>A QR code is not just a picture of your link. It is a grid of dark and light squares, called modules, plus redundant data woven through the grid so a reader can rebuild missing pieces. That redundancy is set by the error-correction level, defined in the QR code standard, ISO/IEC 18004:</p>

<table>
<tr><th>Level</th><th>Recovers about</th><th>Use it for</th></tr>
<tr><td>L (Low)</td><td>7%</td><td>Clean, screen-only codes with no logo</td></tr>
<tr><td>M (Medium)</td><td>15%</td><td>Plain printed codes; a good default</td></tr>
<tr><td>Q (Quartile)</td><td>25%</td><td>Print exposed to wear, dirt, or scuffing</td></tr>
<tr><td>H (High)</td><td>30%</td><td>Any code with a logo, or a rough surface</td></tr>
</table>

<p>When you add a logo, the covered middle counts as damage, and the reader reconstructs it from the redundant data spread across the rest of the code. That is why the error-correction level matters more than the logo file itself: on level L or M, a logo eats most of your safety margin before the code ever reaches a printer, while on level H the same logo sits inside a much larger budget. FreeQrly raises error correction automatically when a logo is added, so you do not set the level by hand — but you still have to respect what it buys you. A higher level also adds modules, making the same content denser: a short address that fits in a 29 × 29 grid at level M needs 37 × 37 at level H, so each module gets smaller at the same print size. Keep the destination short, and print logo codes a little larger than plain ones.</p>

<h2>Logo size: the ceiling, the safer zone, and the area-versus-width trap</h2>

<p>Logo-size advice is easy to misread, because guides quote it two different ways. A logo spanning 30% of the code's <em>width</em> covers only about 9% of its <em>area</em>, while a logo covering 30% of the <em>area</em> spans about 55% of the width. When this guide says "under about 30% of the code area," it means area — the share of the whole square the logo hides — and that is the ceiling the FreeQrly generator uses. Treat anything near that ceiling as a code with no reserve left.</p>

<table>
<tr><th>Logo share of code area</th><th>What it means in practice</th></tr>
<tr><td>Up to about 20%</td><td>Comfortable. Room left for print variation, glare, and wear.</td></tr>
<tr><td>About 20–25%</td><td>The range most design guides recommend as a practical maximum for branded codes.</td></tr>
<tr><td>Approaching 30%</td><td>The ceiling. It can scan in clean conditions, but a scuff or dim light can finish it.</td></tr>
<tr><td>Over 30%</td><td>Past what error correction can rebuild. Shrink the logo or shorten the content.</td></tr>
</table>

<p>Two other placement rules are absolute, not matters of taste. First, the logo goes dead center. The center holds no positioning data, making it the safest place to cover, and centering keeps the mark away from the three large finder patterns in the corners — the squares a camera looks for first to find, orient, and straighten the code. Covering even one finder pattern can stop a scan entirely, no matter the error-correction level. Second, the logo must never touch the quiet zone, the blank margin around the code, which the standard sets at a minimum of four modules wide on every side. A logo edge bleeding into that margin can keep the camera from finding the code's edges at all.</p>

<p>If the logo must be big — a wide wordmark, a detailed crest — you have three honest levers. Shorten the destination, because less data means a roomier pattern with larger modules. Print the code bigger, because larger modules forgive more damage; the <a href="/blog/qr-code-print-size-guide/">print size guide</a> works through the sizes for cards, flyers, and posters. Or simplify the mark: use the compact symbol rather than the full lockup, and save the full version for the packaging around the code.</p>

<h2>Preparing the logo file</h2>

<p>The file you upload decides how clean the result looks at small sizes. A square PNG with a transparent background sits cleanest in the middle: no white box fighting the pattern, no wasted corners. A rectangular logo stretched into a square distorts the mark; crop a balanced, square version of your symbol instead of forcing the whole horizontal lockup into the center.</p>

<ul>
<li><strong>Simplify before you upload.</strong> Fine lettering and tiny details vanish when a mark is reduced to the center of a code. If your logo has a tagline, drop it from the code version.</li>
<li><strong>Give the logo a white pad.</strong> A small light backing around the mark separates it from the surrounding modules so the camera does not read logo edges as code data.</li>
<li><strong>Use the dark version of your mark.</strong> A pale logo on a light code confuses cameras. If your brand mark is light, place it on a contrasting white panel.</li>
</ul>

<h2>Color and contrast: the rules that matter more than the logo</h2>

<p>A logo code fails on color far more often than on logo size. The rule never changes: dark modules on a light background, with strong contrast. Brand colors are welcome, but only if the dark side stays clearly dark and the light side stays clearly light. Practitioner guides commonly use a contrast ratio of 4.5:1 or higher as a starting point, and the plainer the pairing, the wider the range of phones and lighting it survives.</p>

<ul>
<li><strong>Gradients are a risk.</strong> The light end of a gradient often loses contrast, and phones expose colors differently. Check that its lightest part still reads as clearly light, and test the printed piece, not just the screen preview.</li>
<li><strong>Inverted codes are a gamble.</strong> Light modules on a dark background are permitted by the standard and most current phone cameras read them, but some older scanner apps do not. Unless you can test on the devices your audience actually uses, keep the modules dark.</li>
<li><strong>Never recolor the finder patterns into invisibility.</strong> You can style the three corner squares — rounded corners and dotted eyes usually scan fine — but filling in the light ring between the outer and inner square, or coloring the eyes lighter than the rest of the code, breaks what the camera searches for first.</li>
<li><strong>Busy backgrounds are a second fight.</strong> A logo code on a photo forces the camera to separate background, logo, and pattern at once. Give the code a clean, light patch to sit on, with its quiet margin clear.</li>
</ul>

<h2>Shape, frames, and borders</h2>

<p>Rounded modules and dot-style patterns are fine, because the grid itself stays regular. What breaks scanning is distortion of the grid: stretching a code so the squares stop being square, warping it to follow a design, or wrapping it around a tight curve such as a small bottle. Scale evenly, keep the code square, and if a curved surface is unavoidable, print larger and test on the actual object.</p>

<p>Frames and borders belong outside the quiet zone, never inside it. A rounded frame, a brand-colored border, or a "Scan me" caption can all work, provided they sit beyond the four-module margin and do not touch the pattern. The same applies to folds and seams on packaging: if a fold runs through the code or its margin, move the code to a flat panel.</p>

<h2>Step by step</h2>

<ol>
<li><strong>Make the code.</strong> Any type works with a logo: a link, a vCard, a WiFi network, and every other type FreeQrly offers. Shorter destinations make roomier patterns.</li>
<li><strong>Upload a square PNG.</strong> Transparency works best. Keep the logo under about 30% of the code area as a ceiling, and nearer 20–25% for a safety margin.</li>
<li><strong>Let error correction adjust.</strong> It rises automatically when a logo is added, so the covered middle does not stop the scan. Check that the finder patterns and quiet zone are untouched before you export.</li>
<li><strong>Test-scan before printing.</strong> Two phones, one iPhone and one Android, on the print itself — not just the screen. If both read on the first try, ship it. If either hesitates, shrink the logo a notch, raise the contrast, or print larger, and test again.</li>
</ol>

<p>For print, download PNG up to 2048 px, or SVG for a banner or trade-show wall. The <a href="/blog/qr-code-print-size-guide/">print size guide</a> covers the full sizing table, including why logo codes need a 3 × 3 cm minimum in print rather than the 2 × 2 cm plain codes can use.</p>

<h2>How to test a logo code properly</h2>

<p>Testing on your own new phone, in good light, on a screen, proves almost nothing. A printed logo code meets worse conditions: ink spread, laminate glare, dim rooms, and older cameras. A useful test method is deliberately unkind:</p>

<ul>
<li><strong>Test the printed piece, at final size, on the final material.</strong> A code that scans on screen can fail on gloss laminate or textured card, where glare and ink spread change the contrast.</li>
<li><strong>Test two phones at minimum — one iPhone, one Android — and an older phone if you can borrow one.</strong> New flagships forgive a lot; the phone your customer owns may not.</li>
<li><strong>Test from the real distance and angle, in the real lighting.</strong> A table card is scanned from a seat, under restaurant lighting; a poster from meters away, possibly through glass.</li>
<li><strong>Test the destination, not just the decode.</strong> The code should open the right page and load quickly on mobile data.</li>
<li><strong>Treat hesitation as failure.</strong> If a scan takes several seconds or needs multiple attempts, the code is marginal. Shrink the logo, raise the contrast, or print larger — then test again.</li>
</ul>

<p>If a code still refuses to scan, the cause is usually one of the four original mistakes: a logo past the ceiling, low contrast, a crowded background, or a stretched grid. The <a href="/blog/why-is-my-qr-code-not-working/">troubleshooting guide</a> walks through them, and the <a href="/blog/why-is-my-qr-code-blurry/">blurry-code guide</a> covers resolution.</p>

<h2>Where logo codes earn their keep</h2>

<p>A logo code is worth the extra care wherever the code itself is part of the brand surface, not just a utility. On packaging, putting the mark inside the code makes the whole pack read as one design. On a business card, a logo code turns a forgettable square into a recognizable one, and the card is scanned at close range, where a logo code is most forgiving. At events, a logo code on a badge or poster is recognizable from across a room, which matters when ten exhibitors all have plain black squares. On menus, the logo reassures guests the code belongs to the restaurant.</p>

<p>Batch use is where consistency pays off. A product line with twenty variants should carry the same mark, the same colors, and the same quiet zone on every code — applied once across the batch rather than rebuilt per item. If the destination behind those codes ever needs to change, a dynamic code keeps the printed piece valid: its destination is editable after printing, and it carries scan statistics. Static codes, by contrast, need no sign-up, carry no watermark, and never expire — the right choice when the destination is fixed, such as a homepage or a product manual.</p>

<h2>The honest comparison: logo code versus plain code</h2>

<p>A plain code is more forgiving than a logo code in every dimension: it tolerates smaller print, lower contrast, denser data, and rougher surfaces, because no part of its pattern is deliberately hidden. A logo code trades some of that forgiveness for recognition. That trade is worth making when the code is a brand surface and the print is controlled — packaging, cards, posters, menus. It is a bad trade in four situations:</p>

<ul>
<li><strong>Tiny print.</strong> On a 2 cm code, a logo leaves very little pattern, and each module is already small. Either print larger or drop the logo.</li>
<li><strong>Dense data.</strong> A long URL or a full vCard already makes a dense grid. Adding a logo on top is two squeezes at once — shorten the content first.</li>
<li><strong>Harsh environments.</strong> Outdoor signage and workshop labels need their full error-correction budget for survival, not for decoration.</li>
<li><strong>Uncontrolled reproduction.</strong> If a code will be photocopied, faxed, shrunk by a partner, or reprinted by someone else at a size you did not choose, a plain code survives the journey better.</li>
</ul>

<p>There is also a brand-consistency argument against over-designing: one simplified mark, one color pairing, one quiet-zone rule, reused across the whole run, reads as a system. A different logo treatment on every code reads as noise, and noise is exactly what a scanner struggles with.</p>

<h2>Brand consistency across a whole run</h2>

<p>Decide the system once, then repeat it: the same simplified square mark, the same dark-on-light pairing even when the surrounding packaging changes color, the same quiet zone and minimum print size, on every surface. When a code appears on both a card and a poster, the poster version is not a stretched card version; it is the same code generated at the poster's size, with the same logo share. Generate many codes as a batch with the logo applied across all of them, then proof-scan one from each surface type before committing to the run. FreeQrly's batch mode and API cover that workflow, with unlimited scans on every code.</p>

<p>Try it: <a href="/qr-code-with-logo/">make a QR code with your logo</a> — free, no sign-up for static codes, no watermark. Start with the mark at about a fifth of the code, print a proof, scan it on two phones, and only then decide whether the logo earns more room. For sizing, the <a href="/blog/qr-code-print-size-guide/">print size guide</a> has the full table, from business cards to billboards.</p>""",
  howto=[
    ("Make the code",
     "Any type works with a logo: a link, a vCard, a WiFi network."),
    ("Upload a square PNG",
     "Transparency works best. Keep the logo under ~30% of the code area."),
    ("Let error correction adjust",
     "It rises automatically when a logo is added, so the code still scans."),
    ("Test-scan before printing",
     "Two phones, iPhone and Android, on the print itself. If both read first try, ship it."),
  ],
  faq=[
  ('Will my logo break the QR code?', 'Not if it stays under about 30% of the code area, which is the ceiling the generator uses, and nearer 20–25% if you want a safety margin. Error correction is raised automatically when a logo is added, so the covered middle does not stop the scan.'),
  ('What logo file works best?', 'A square PNG with a transparent background. Rectangular logos and white-boxed logos waste space and fight the pattern. Simplify the mark first: fine lettering and taglines vanish at code-center size.'),
  ('Can I use a logo with any QR code type?', 'Yes — link, vCard, WiFi, and every other type. The same logo can also be applied across a whole batch.'),
  ('PNG or SVG for print?', 'PNG up to 2048 px for most print jobs, or SVG when you need it infinitely scalable, like a banner.'),
  ('Why must the logo stay in the center?', 'The center holds no positioning data, so it is the safest place to cover, and centering keeps the mark away from the three finder patterns in the corners. Covering even one finder pattern can stop a scan entirely.'),
  ('How big should a logo code be in print?', 'At least 3 × 3 cm, rather than the 2 × 2 cm a plain code can use, and larger if the code holds a lot of data or will be scanned in poor light. The print size guide has the full table.'),
  ('How should I test a logo code before printing?', 'Scan the printed piece, at final size and on the final material, with at least two phones — one iPhone, one Android — from the real distance and in the real lighting. Treat hesitation as failure: shrink the logo, raise the contrast, or print larger, and test again.'),
  ('When should I skip the logo?', 'On tiny print, on very dense codes, on surfaces that will be scuffed or weathered, or when the code will be reproduced at a size you did not choose. In those cases a plain code is more forgiving.'),
],
  sources=[
  ('http://www.iso.org/standard/83389.html', 'ISO/IEC 18004:2024', 'The QR Code symbology specification, published 2024-08 (Edition 4). Supports the four error-correction levels (L 7%, M 15%, Q 25%, H 30%) and the 4-module quiet zone.'),
  ('https://pretty-qr.com/blog/qr-design-best-practices', 'Pretty QR — QR Code Design Rules: 10 Rules for Beautiful Codes That Still Scan', 'No publication date shown on the page; accessed 2026-11-03. Supports the 20–25% logo-area guidance, the 4.5:1 contrast starting point, intact finder patterns, and testing on real phones.'),
  ('https://www.qrcodebarn.com/blog/qr-code-size-guide.html', 'QRCodeBarn — QR Code Size Guide: How to Resize a QR Code Properly', 'Published 13 October 2026. Supports the 2 cm practical minimum, the distance ÷ 10 rule of thumb, the 4-module quiet zone, and the 29 × 29 (level M) to 37 × 37 (level H) example for a 40-character address.'),
  ('https://www.notraqr.com/qr-codes-technical.html', 'NoTraQR — QR Code Technical Guide: Error Correction, File Formats and Barcode Comparison', 'No publication date shown on the page; accessed 2026-11-03. Supports the error-correction table (L 7%, M 15%, Q 25%, H 30%), level H for logo overlays, and the 2 cm / 3 cm rules of thumb.'),
],
  cta=dict(title="Make your logo QR code",
           text="Upload your logo, keep it centered, keep it scannable. Free.",
           href="/qr-code-with-logo/", btn="Open the studio"),
 ),
]


POSTS += [
 dict(
  slug="qr-code-troubleshooting-guide",
  title="QR Code Troubleshooting Guide: Find and Fix Any Scan Failure | FreeQrly",
  desc="QR code won't scan? One hub for all eleven causes \u2014 size, blur, contrast, quiet zone, logo, damage, dead links, light, and camera \u2014 with the fix for each.",
  h1="QR code <span class='hl hl-mint'>troubleshooting</span>, start to finish",
  lede="Won't scan, scans sometimes, or scans to nowhere? Find your failure in the table, follow its fix, and test again \u2014 most codes are fixed without reprinting.",
  date="November 3, 2026",
  datePublished="2026-11-03",
  mascot="error",
  cta=dict(title="Try it yourself — free", text="Everything in this article works in the FreeQrly studio right now. Static codes, all 17 content types, PNG and SVG export.", href="/#studio", btn="Open the studio"),
  body="""<p>A QR code that will not scan is rarely a mystery. Most failures come down to one of eleven causes, and they split into three questions: is the pattern unreadable, is the phone struggling, or did the code scan fine and the destination let you down? Answer those first, and you will not reprint a sound code — or fix a pattern when the link is dead.</p>

<h2>Check these three first</h2>
<ol>
<li><strong>Try a second phone.</strong> If another phone reads the code, the pattern is fine. Skip to the phone checks below.</li>
<li><strong>Look at the code, not the screen.</strong> Is it small, pale, crowded by nearby text, covered by a logo, scratched, or faded? Any one of those can make a pattern unreadable. Also try a fresh copy of the original file: if the fresh copy scans, the original print failed, not the data.</li>
<li><strong>Read what the scan returns.</strong> If the phone recognises the code but the page never loads or lands somewhere unexpected, the pattern did its job. The destination is the problem: a deleted page, a mistyped link, or a switched-off dynamic code.</li>
</ol>
<p>One distinction matters throughout: a code that <em>never</em> scans has a pattern or camera problem, while a code that scans <em>sometimes</em> — in bright light but not dim light, up close but not at arm's length — is a borderline code. Borderline codes pass at your desk and fail in a customer's hands: treat a sometimes-code as broken.</p>

<h2>The cause table: every common failure at a glance</h2>
<table>
<tr><th>Cause</th><th>Symptom</th><th>Quick test</th><th>Fix</th><th>Deep dive</th></tr>
<tr><td><strong>Too small</strong></td><td>Only scans from very close</td><td>Scans closer up? Size is the fault</td><td>Print larger</td><td><a href="/blog/qr-code-print-size-guide/">Size guide</a></td></tr>
<tr><td><strong>Blurry / low resolution</strong></td><td>Soft edges, smudged squares</td><td>Soft in the file? Bad export</td><td>Re-export as PNG or SVG</td><td><a href="/blog/why-is-my-qr-code-blurry/">Blur fixes</a></td></tr>
<tr><td><strong>Low contrast</strong></td><td>Scans in bright light, fails in dim light</td><td>Would it read in black and white?</td><td>Dark code on a light background</td><td><a href="/blog/why-is-my-qr-code-not-working/">Diagnosis</a></td></tr>
<tr><td><strong>Quiet zone crowded</strong></td><td>Scans cropped, fails in design</td><td>Cover nearby text: scans now?</td><td>Restore a clear margin, 4 modules wide</td><td><a href="/blog/why-is-my-qr-code-not-working/">Diagnosis</a></td></tr>
<tr><td><strong>Logo too big</strong></td><td>Scanned before the logo, fails after</td><td>Regenerate without the logo</td><td>Smaller logo, higher error correction</td><td><a href="/blog/add-logo-to-qr-code/">Logo codes</a></td></tr>
<tr><td><strong>Damage or dirt</strong></td><td>Worked when new, fails after handling</td><td>Compare with a fresh print</td><td>Clean, protect, or reprint</td><td><a href="/blog/why-is-my-qr-code-not-working/">Diagnosis</a></td></tr>
<tr><td><strong>Dead link</strong></td><td>Scans, but page missing or wrong</td><td>Open the link on a computer</td><td>Restore or repoint the destination</td><td><a href="/blog/do-qr-codes-expire/">Do codes expire?</a></td></tr>
<tr><td><strong>Light and glare</strong></td><td>Scans at one angle, fails at another</td><td>Tilt away from the light</td><td>Move the light, use matte finish</td><td><a href="/blog/why-is-my-qr-code-not-working/">Diagnosis</a></td></tr>
<tr><td><strong>Camera permission / focus</strong></td><td>Fails on one phone only</td><td>Second-phone test, plus a lens wipe</td><td>Allow access, clean lens, hold steady</td><td><a href="/blog/how-to-scan-a-qr-code/">How to scan</a></td></tr>
<tr><td><strong>Dynamic code switched off</strong></td><td>Scans to an error page</td><td>Check the code in its Dashboard</td><td>Reactivate or replace it</td><td><a href="/blog/do-qr-codes-expire/">Do codes expire?</a></td></tr>
<tr><td><strong>Code on its own screen</strong></td><td>Camera cannot face its own display</td><td>Expected, not a fault</td><td>Decode the image file instead</td><td><a href="/blog/scan-qr-code-from-image/">From an image</a></td></tr>
</table>

<h2>The pattern itself: six ways a code becomes unreadable</h2>

<h3>1. Too small for the scanning distance</h3>
<p>Small codes fail because cameras cannot resolve the individual modules — the little squares — when they are tiny in the frame. As a rule of thumb, keep printed codes at least 2 × 2 cm, and scale up with distance: the code's width should be at least one-tenth of the expected scanning distance. A table card scanned from 50 cm needs a code around 5 cm wide; a poster scanned from 5 metres needs one around 50 cm wide. Dense codes holding long links need more room than short links. The full sizing tables are in the <a href="/blog/qr-code-print-size-guide/">print size guide</a>.</p>

<h3>2. Blurry or low resolution</h3>
<p>Blur means too few pixels stretched across too much space, so module edges smear together. The usual culprits are a low-resolution export, a JPEG save that softens sharp edges, a screenshot of a screenshot, or a file stretched out of proportion so squares become rectangles. Fix it at the source file: re-export as high-resolution PNG, or as SVG, which scales without blur, resizing only proportionally. An already-blurry print cannot be sharpened back — reprint from the clean file. The five causes and their fixes are in <a href="/blog/why-is-my-qr-code-blurry/">why your QR code is blurry</a>.</p>

<h3>3. Low contrast</h3>
<p>Scanners look for dark modules on a light background. Light grey on white, pastel brand colours, a code over a photograph, or dark modules on a dark background all remove the difference the camera needs. This is the most common design-driven failure, and the most avoidable: black on white always works, and any colour pair should still read in black and white. Watch out for inverted codes and codes over busy images, where the background competes with the pattern. If a code scans in bright light but not in a dim room, contrast is the first suspect.</p>

<h3>4. Quiet zone crowded or cropped</h3>
<p>The blank margin around a code is not decoration. Scanners use it to find the edges of the pattern, and the standard specifies a quiet zone at least 4 modules wide — four of the code's own little squares — on all four sides, as defined in ISO/IEC 18004. Text or patterns crowding into that margin confuse detection, so the phone never reads the data. This failure is easy to miss because the code itself looks perfect. Test it by covering everything around the code: if it scans clean, restore the margin and keep it empty.</p>

<h3>5. A logo covering too much of the pattern</h3>
<p>A centre logo works only because error correction rebuilds the covered data. ISO/IEC 18004 defines four error-correction levels — L, M, Q, and H — with approximate codeword recovery of 7%, 15%, 25%, and 30% respectively. Those percentages describe recovery of codewords, not a guaranteed share of visible area you may cover. As a rule of thumb, keep the logo small — the print size guide suggests under about 30% of the code's area — use the highest error-correction level, print larger than for a plain code, and never cover the three large corner squares, which the scanner needs to orient the pattern. Test-scan on two phones first. See <a href="/blog/add-logo-to-qr-code/">how to add a logo to a QR code</a> and the <a href="/qr-code-with-logo/">logo code generator</a>.</p>

<h3>6. Damage, dirt, and fading</h3>
<p>Creases, scratches, spills, fading, and worn stickers all eat into the pattern, and error correction can only rebuild so much. Damage to the corner squares is especially fatal: without them, the scanner cannot locate the code at all. For real-world codes — menus, labels, outdoor signs — prevention beats repair: laminate the surface, choose a higher error-correction level, print a spare, and inspect the oldest copies first. If the pattern itself is worn away, reprint from the original file rather than patching the damaged copy.</p>

<h2>The destination: when the code scans but nothing good happens</h2>
<p>A scan that returns an error page, a missing page, or a landing page you did not expect is a successful scan of a broken destination. Open the link on a computer and read it character by character: a moved or deleted page, a mistyped address, a site that is down, or a short link whose owner changed its destination are the usual causes.</p>
<p>One structural version decides whether a fix is even possible. A static code holds the destination directly in its pattern, so it works as long as the link works — and if the link dies, only the page behind it can be restored or the code reprinted. A dynamic code holds a short redirect instead, so its owner can change the destination without reprinting — but the code then depends on that account and service staying active. If that account lapses or the service switches the redirect off, the printed code stops leading anywhere useful, even though the pattern is flawless. That is the mechanism behind most "my code expired" stories, explained in <a href="/blog/do-qr-codes-expire/">do QR codes expire?</a>. Check first whether the destination can be restored or repointed before reprinting.</p>

<h2>The phone and the moment: permission, focus, light, and screens</h2>
<ul>
<li><strong>Camera permission.</strong> A scanner never granted camera access cannot see anything at all. Allow camera access, then try again. FreeQrly's scanner decodes in your browser on your own device — see the <a href="/scan/">scanner page</a> — but the browser still needs permission to open the camera.</li>
<li><strong>A dirty lens.</strong> Wipe the lens with a soft cloth. A smeared lens blurs exactly the fine detail a QR code is made of.</li>
<li><strong>Focus and distance.</strong> Hold the phone steady, keep the whole code and its quiet zone in frame, and move slowly until focus locks. Very close is not always better: most cameras cannot focus a few centimetres away.</li>
<li><strong>Light and glare.</strong> Glossy lamination, a screen, or a spotlight can reflect light back into the camera and wash out the modules. Tilt the code or phone, move out of direct light, or switch to matte finish. Glare that moves when you tilt is glare, not damage.</li>
<li><strong>Curved or angled surfaces.</strong> A code wrapped around a bottle or shot at a steep angle is distorted, and scanners tolerate only so much of that. Flatten what you can and shoot as straight-on as possible.</li>
<li><strong>A code on the phone's own screen.</strong> You cannot point a phone's camera at its own display. For a code in a photo, screenshot, or message on the same phone, decode the image file instead: on iPhone, long-press the code in Photos; on Android, use Lens in Photos; on a computer, upload it to a decoder such as FreeQrly's <a href="/scan/">scanner</a>. The full steps are in <a href="/blog/scan-qr-code-from-image/">how to scan a QR code from an image</a>, and the phone-by-phone camera steps are in <a href="/blog/how-to-scan-qr-code-on-phone/">how to scan a QR code on your phone</a>.</li>
</ul>
<p>Apple's own guide confirms the baseline: on iPhone, open the Camera app or the Code Scanner in Control Center, hold the phone so the code appears in frame, and tap the link that appears. If that path does nothing on a code other phones read, suspect permission, focus, and light — not a missing scanner app. The general steps for both iPhone and Android are in <a href="/blog/how-to-scan-a-qr-code/">how to scan a QR code</a>.</p>

<h2>By scene: print, screen, and outdoors</h2>
<h3>Printed codes: flyers, cards, menus, packaging</h3>
<p>Print failures are usually size, resolution, contrast, or wear — in that order. Test at final size, not on screen: print one copy, step back to the real viewing distance, and scan it with two phones. Check the quiet zone in the finished layout, not just the preview, because layout tools crop margins. Laminate handled codes and keep the original export.</p>
<h3>Codes on screens: slides, TV, video calls, websites</h3>
<p>Screen codes fail on glare, refresh flicker, and size relative to the viewer's distance. Make the code large on the slide, hold it on screen for several seconds rather than flashing it past, and avoid placing it over a moving background. For phone-to-phone display, raise brightness and tilt away from overhead lights.</p>
<h3>Outdoor codes: posters, signs, vehicles, shop windows</h3>
<p>Outdoor codes face every failure at once: distance, sunlight, glare, weather, and fading. Size up generously on the one-tenth rule, print high-contrast on matte stock, weatherproof it, and test at real passers-by distance and angle. Shop-window codes need a special check: scan from outside the glass, in daylight, because reflections invisible from inside can wash the code out.</p>

<h2>An honest comparison: free codes, paid codes, and "expired" codes</h2>
<p>A static code from any honest generator has the same property: the destination is baked into the pattern, so there is nothing to expire, nothing to renew, and no account that can lapse and take the code with it. FreeQrly's static codes are free, need no registration, carry no watermark, and never expire. Paying for a static code buys you nothing about its lifespan: a subscription for a code that never needed a server is not keeping it alive.</p>
<p>A dynamic code is a different product, and the honest trade is this: you gain editing after printing and scan statistics, and you accept a dependency on an account and a service. FreeQrly's dynamic codes are free to start — sign in, and you get 20 free dynamic codes, currently unlimited during the limited-time promotion — with editing, statistics, and unlimited scans. The dependency is real even at zero price: delete the account and the codes go with it, so a dynamic code should never be the only copy of a destination that must outlive its owner. For anything that must last with no maintenance — a WiFi password, a business card, a plaque — static is structurally safer.</p>
<p>The same logic applies to paid dynamic codes elsewhere: when one stops working, the pattern is almost never the problem — the subscription, account, or redirect is. Before reprinting, check the vendor's Dashboard, the account status, and the destination the redirect points to. For a print run that cannot be reprinted cheaply, ask first: if I stop paying, does the printed code keep working? The answer tells you whether you are buying a code or renting one.</p>

<h2>Remake, reprint, or fix the destination?</h2>
<ul>
<li><strong>Fix the destination</strong> when the code scans but the page is wrong or missing, and you control the page or redirect. No reprint needed.</li>
<li><strong>Reprint from the original file</strong> when the fresh copy scans but the installed copy does not: the print, surface, or placement failed.</li>
<li><strong>Remake the code</strong> when the fresh copy also fails, the data is wrong, or the design — size, contrast, logo, margin — is at fault. Generate a clean code, test it on two phones, and only then print.</li>
<li><strong>Switch code type</strong> for recurring structural failures: a changing destination belongs in a dynamic code; one that must never depend on an account belongs in a static one.</li>
</ul>
<p>If a code still fails on two phones from a fresh, large, black-on-white print with a clear margin, suspect the data itself — an over-long link, or a mistyped address. Shorten the link and regenerate.</p>

<h2>Make a clean replacement</h2>
<p>When the verdict is "remake it," start from a clean export rather than patching the old file. Generate the replacement in the <a href="/">free generator</a> — all 17 content types are available as static codes with no registration, and dynamic codes with editing and statistics are free after sign-in. If the code needs a logo, use the <a href="/qr-code-with-logo/">logo generator</a> and keep the logo small with a high error-correction level; if you need many codes at once, <a href="/batch-qr-code/">batch generation</a> makes one per link. Before printing, test it with the <a href="/scan/">scanner</a> and on a second phone. The deep dives linked above — the <a href="/blog/why-is-my-qr-code-not-working/">step-by-step diagnosis</a>, the <a href="/blog/why-is-my-qr-code-blurry/">blur fixes</a>, and the <a href="/blog/qr-code-print-size-guide/">print size guide</a> — each take one cause further.</p>""",
  faq=[
  ('Why does my QR code scan on one phone but not another?', 'Then the code and the link are both fine — the failing phone is the problem. Wipe its lens, allow camera access, hold steady with the whole code in frame, and try in better light. If it still fails on that phone alone, use the built-in camera path rather than a third-party scanner app.'),
  ('My QR code scans sometimes but not always — is it fine?', "No. A sometimes-code is a borderline code: it passes at your desk and fails in a customer's hands. Treat it as broken and fix the underlying cause — usually size, contrast, glare, or a crowded quiet zone — rather than hoping for good light."),
  ('How big should a printed QR code be?', 'As a rule of thumb, at least 2 x 2 cm, and at least one-tenth of the expected scanning distance: a table card scanned from 50 cm needs a code around 5 cm wide, and a poster scanned from 5 metres needs one around 50 cm wide. Dense codes holding long links need more room than short links.'),
  ('How much of a QR code can a logo cover?', "Keep it small. Use the highest error-correction level, print larger than for a plain code, and never cover the three large corner squares, which the scanner needs to orient the pattern. As a rule of thumb, the print size guide suggests under about 30% of the code's area — and always test-scan the finished code on two phones before printing."),
  ('My code scans but the page is gone — is the code broken?', 'No. The pattern decoded perfectly; the destination failed. A page that was moved or deleted, a mistyped address, or a dynamic code whose account or redirect was switched off all look like this. If you control the page or the dynamic redirect, restore or repoint it — no reprint is needed. A static code cannot be repointed; only the page behind it can be restored.'),
  ('Do I need a scanner app to test my code?', "No. On iPhone, use the Camera app or the Code Scanner in Control Center; on Android, use the built-in camera or Lens. For a code that is already on the phone's own screen — in a photo or screenshot — decode the image file instead of pointing the camera at its own display."),
],
  sources=[
  ('http://www.iso.org/standard/83389.html', 'ISO/IEC 18004:2024', 'Edition 4, published 2024-08; standard identity, edition, and publication date verified on the ISO page 2026-11-03, whose abstract confirms the standard specifies error-correction rules. Supports the error-correction levels L 7%, M 15%, Q 25%, H 30% (approximate codeword recovery) and the quiet zone of at least 4 modules on all sides, as defined in that standard.'),
  ('https://support.apple.com/en-us/102680', 'Apple Support: Scan a QR code with your iPhone or iPad', 'Published September 14, 2026, as shown on the page and verified 2026-11-03. Supports the built-in scanning steps cited in the post: open the Camera app or the Code Scanner in Control Center, hold the phone so the code appears in frame, and tap the link that appears. No numerical claim is taken from this page.'),
  ('https://freeqrly.com/blog/qr-code-print-size-guide/', 'FreeQrly: QR Code Print Size Guide', "Site-internal source, not an external standard. Supports the figures the hub page explicitly labels as rules of thumb: minimum print size 2 x 2 cm, the 1:10 distance rule (code width at least one-tenth of scanning distance), and a logo under about 30% of the code's area."),
],
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
    # Updated mechanism: shown only when a post actually carries an
    # 'updated' (long display) + 'dateModified' (ISO) pair. Never rendered
    # otherwise — no fabricated updated dates.
    meta_line = f'{p["date"]} · 4 min read'
    if p.get("updated"):
        meta_line = f'{p["date"]} · Last updated: {p["updated"]} · 4 min read'
    datemod_b = f',"dateModified":"{p["dateModified"]}"' if p.get("dateModified") else ""
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
<link rel="stylesheet" href="../../assets/css/main.css?v=b3y-20261102">
<link rel="stylesheet" href="/assets/css/site-header.css?v=b3y-20261102">
<link rel="stylesheet" href="/assets/css/acct-menu.css?v=b3y-20261102">
{REL_CSS}{SOURCES_CSS if p.get("sources") else ""}
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{p["title"]}","description":"{p["desc"]}","speakable":{{"@type":"SpeakableSpecification","cssSelector":["h1",".lede"]}},"datePublished":"{p.get('datePublished','2026-10-13')}"{datemod_b},"author":{{"@type":"Organization","name":"FreeQrly"}},"publisher":{{"@type":"Organization","name":"FreeQrly"}}}}
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
    <p class="meta" style="text-align:center">{meta_line}</p>
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
      <div class="fcol"><h4>Product</h4><a href="/">QR Generator</a><a href="/batch-qr-code/">Batch QR Codes</a><a href="/qr-code-with-logo/">QR Code with Logo</a><a href="/scan/">QR Scanner</a><a href="/barcode-generator/">Barcode Generator</a><a href="/pricing/">Pricing</a></div>
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
