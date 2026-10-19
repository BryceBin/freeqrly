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
  slug="google-form-qr-code", dtype="google-form",
  title="Free Google Form QR Code Generator | FreeQrly",
  desc="Turn any Google Form link into a QR code in seconds. Free, no sign-up for static codes, no watermark. Paste your form URL and download a printable PNG or SVG.",
  kw="qr code generator for google form",
  h1="QR codes for Google Forms, without the fine print.",
  lede="Paste your form's responder link and get a crisp, printable QR code — no account needed for static codes, no watermark, no expiry. Put it on a poster and watch the responses roll in.",
  steps=[
    ("Copy your form link", "In Google Forms, click <b>Send</b> and copy the responder link (the short one works best)."),
    ("Paste your link", "Drop the link into the Website field — your code appears instantly in the preview."),
    ("Download and print", "Grab a high-resolution PNG or SVG. It scans straight to your form, forever."),
  ],
  studio_h2="Make your Google Form QR code",
  faq=[
    ("Do respondents need to sign in to open my form?",
     "No. The QR code simply opens your form's link — access follows your form's own sharing settings, not the code."),
    ("Will this QR code expire?",
     "Never. It is a static code: the link lives inside the pattern itself, so it works as long as your form does. No renewals, no vendor to disappear."),
    ("Is it really free? Any watermark?",
     "Completely free, no watermark, no account needed for static codes. Some tools in the search results add watermarks or paywalls — this one doesn't."),
    ("Can I track how many people scanned it?",
     "Static codes don't phone home, which is exactly why they're private. For response counts, use your form's Responses tab — it already tracks everything."),
  ],
 ),
 dict(
  slug="wifi-qr-code", dtype="wifi",
  title="Free WiFi QR Code Generator | FreeQrly",
  desc="Create a free WiFi QR code so guests join your network with one scan. No app needed, no sign-up for static codes. For a static code, your password never leaves your browser.",
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
     "For a static code, yes. The code is drawn entirely in your browser — your password is never uploaded or stored anywhere. For extra peace of mind, load the page, disconnect from the internet, then type."),
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
  desc="Turn your contact details into a scannable vCard QR code. Free, no sign-up for static codes. One scan saves you straight to their phone.",
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
  title="Free Batch QR Code Generator | FreeQrly",
  desc="Generate dozens of QR codes at once and download them as a ZIP. Free, no sign-up for static codes, no limits games. One link per line — done.",
  kw="batch qr code generator",
  h1="Dozens of QR codes. One download.",
  lede="Paste your links — one per line — hit generate, and download every code as a tidy ZIP. The batch feature other tools put behind a paywall, free here.",
  steps=[
    ("Paste your links", "One URL per line in the batch box. Up to 50 at a time."),
    ("Hit Generate all", "Every link becomes its own QR code, previewed in a grid."),
    ("Download the ZIP", "One click packs them all as print-ready PNGs, named qr-1, qr-2, and so on."),
  ],
  studio_h2="Generate your batch",
  faq=[
    ("How many QR codes can I make at once?",
     "Up to 50 per batch. Need more? Run another batch — there's no daily cap or account to hit."),
    ("Is batch generation really free?",
     "Yes. Many generators charge a subscription for bulk export; here it's the same free tool, no watermark, no sign-up for static codes."),
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
      <span id="authArea"><a class="tbtn authLink" href="/login/" data-i18n="signin">Sign in</a></span>
      <select class="tbtn langsel" id="langBtn" aria-label="Language" data-i18n-aria="ariaLanguage"></select>
      <button class="tbtn" id="themeBtn" aria-label="theme">◐</button>
    </div>
  </header>
  <div class="topline"></div>'''

STUDIO_H2_RE = re.compile(r'<div class="shead"><div class="over" data-i18n="sOver">.*?</div><h2 data-i18n="sTitle">.*?</h2></div>', re.S)

PAGES += [
dict(slug="business-card-qr-code", dtype="vcard",
  title="Free Business Card QR Code Generator | FreeQrly",
  desc="Put a scannable vCard QR code on your business card. Free, no sign-up for static codes \u2014 one scan saves your contact straight to their phone.",
  kw="qr code for business cards",
  h1='Your business card, <span class="hl hl-mint">but it introduces itself</span>.',
  lede="Encode your details as a vCard QR code. Print it on your card and new contacts save you with one scan \u2014 no typing, no lost cards.",
  steps=[("Fill in your details","Name, phone, email, company \u2014 the card builds itself as a vCard."),
         ("Style it with your logo","Upload your logo; error correction adjusts so it still scans."),
         ("Print it on your card","2x2 cm minimum, 1024 px export. High contrast, always.")],
  studio_h2="Make your business card QR code",
  faq=[("vCard or a plain link \u2014 which is better?","vCard saves the contact directly to the phone with one tap. A link sends them to a page first. For business cards, vCard wins."),
       ("How big should the QR code be on a card?","At least 2x2 cm (0.8x0.8 in). Export at 1024 px or higher so edges stay crisp in print."),
       ("Will it scan on iPhone and Android?","Yes \u2014 both read vCard codes natively with the built-in camera. No app needed."),
       ("Does it expire or need an account?","No. It is a static code: your details live inside the pattern. Print it today, it scans in ten years.")]),
dict(slug="google-review-qr-code", dtype="review",
  title="Free Google Review QR Code Generator | FreeQrly",
  desc="Turn your Google review link into a printable QR code. Free, no sign-up for static codes. Put it on the counter and watch the reviews come in.",
  kw="qr code for google review",
  h1='More five-star reviews, <span class="hl hl-blush">one scan away</span>.',
  lede="Paste your Google review link and get a printable QR code. Counter, receipt, takeout bag, table tent \u2014 make leaving a review effortless.",
  steps=[("Copy your review link","In your Google Business Profile, open Share review form and copy the link."),
         ("Paste your link","The generator pre-fills the link tab \u2014 your code appears instantly."),
         ("Print it where customers see it","Counter cards, receipts, packaging. 1024 px export for crisp print.")],
  studio_h2="Make your Google review QR code",
  faq=[("Where do I find my Google review link?","In Google Business Profile: open your listing, click Ask for reviews or Share review form, and copy the short link."),
       ("Do reviewers need to be signed in?","They need a Google account to post, but scanning works for everyone \u2014 the code just opens your review form."),
       ("Can I track how many scans it gets?","FreeQrly codes are static and private \u2014 no tracking by design. For counts, put a URL shortener with stats in front of the link."),
       ("Does the code expire?","No. Static codes never expire and need no account, so your counter card works forever.")]),
dict(slug="qr-code-with-logo", dtype="url",
  title="QR Code Generator with Logo \u2014 Free | FreeQrly",
  desc="Add your logo to the center of any QR code. Free, no sign-up for static codes, no watermark. Error correction adjusts automatically so it always scans.",
  kw="qr code with logo",
  h1='Your logo, <span class="hl hl-honey">right in the middle</span>.',
  lede="Upload your logo and it lands dead center, with error correction cranked up automatically so the code still scans perfectly. Free, no watermark, no account needed for static codes.",
  steps=[("Make your code","Any type \u2014 link, vCard, WiFi. The logo step works with all of them."),
         ("Upload your logo","Square PNG with transparency works best. Keep it under ~30% of the code area as a rule of thumb."),
         ("Download print-ready","PNG up to 2048 px or infinitely scalable SVG \u2014 crisp on cards and banners alike.")],
  studio_h2="Make your logo QR code",
  faq=[("Will the code still scan with a logo on it?","Yes. Uploading a logo automatically raises error correction to High, which reserves <a href=\"http://www.iso.org/standard/83389.html\">up to 30% of the pattern for recovery</a> under ISO/IEC 18004 \u2014 that is where your logo sits."),
       ("What logo file works best?","A square PNG with a transparent background. Avoid fine text inside the logo \u2014 bold shapes read better at small sizes."),
       ("What size should I print it?","At least 2x2 cm, at 1024 px export or higher. Bigger is safer when a logo covers the center."),
       ("Is there a watermark or a fee?","No. Logo upload is free and unlimited, and for static codes your files never leave your browser.")]),
dict(slug="wedding-qr-code", dtype="url",
  title="Free Wedding QR Code Generator | FreeQrly",
  desc="QR codes for weddings: RSVP forms, photo sharing, menus, seating charts. Free, no sign-up for static codes \u2014 one scan for your guests.",
  kw="qr code wedding",
  h1='One scan, <span class="hl hl-honey">zero wedding-day questions</span>.',
  lede="RSVP form, photo album, menu, seating chart \u2014 turn every wedding link into a pretty QR code for invitations and table cards. Free forever, styled to match your theme.",
  steps=[("Pick what guests need","RSVP link, shared photo album, menu, seating chart \u2014 one code per link."),
         ("Style it to match","Your wedding colors, your logo or monogram in the center."),
         ("Print for invites & tables","SVG for the stationer, PNG for table cards. They never expire.")],
  studio_h2="Make your wedding QR code",
  faq=[("What do couples usually link to?","RSVP forms, shared photo albums (guests upload their shots), digital menus, seating charts, and the gift registry."),
       ("Can I match my wedding colors?","Yes \u2014 set any ink and paper color. Just keep strong contrast between the code and background so phones read it in dim venues."),
       ("How big for table cards?","At least 3x3 cm so guests can scan from across the table without standing up."),
       ("Will they still work on the day?","Yes \u2014 static codes never expire. Make them months ahead; they will scan on the day and for years after as a keepsake.")]),
dict(slug="instagram-qr-code", dtype="url",
  title="Free Instagram QR Code Generator | FreeQrly",
  desc="Turn your Instagram profile or post into a scannable QR code. Free, no sign-up for static codes. Print it for packaging, flyers, and shop windows.",
  kw="qr code for instagram",
  h1='Your profile, <span class="hl hl-blush">off the screen</span>.',
  lede="Paste your Instagram URL and get a scannable code for packaging, flyers, receipts, and the shop window. New followers, minus the username spelling.",
  steps=[("Copy your profile link","From your profile: instagram.com/yourname \u2014 or any post or Reel URL."),
         ("Paste your link","Your code appears instantly in the link tab."),
         ("Print it where people look","Packaging inserts, counter cards, flyers. Export 1024 px for print.")],
  studio_h2="Make your Instagram QR code",
  faq=[("Profile link or a specific post?","Profile link for general follows. Linking a Reel or post works too \u2014 handy for campaigns and packaging inserts."),
       ("Does it open in the Instagram app?","On most phones, tapping the scanned link offers to open it in the app if installed; otherwise it opens in the browser."),
       ("Can I add my logo or brand colors?","Yes \u2014 upload your logo and set your brand colors. Keep contrast high so it scans in any light."),
       ("Does it expire if I change my username?","The code encodes the exact URL, so if your handle changes, make a fresh code. The code itself never expires.")]),
]

PAGES += [
dict(slug="real-estate-qr-code", dtype="url",
  title="Free Real Estate QR Code Generator | FreeQrly",
  desc="QR codes for real estate: listings, virtual tours, flyers, and yard signs. Free, no sign-up for static codes \u2014 one scan takes buyers to the listing.",
  kw="qr code for real estate",
  h1='Every listing, <span class="hl hl-mint">one scan away</span>.',
  lede="Link listings, virtual tours, and open-house details to scannable codes. Print them for yard signs, brochures, and window displays \u2014 free forever, no account needed for static codes.",
  steps=[("Copy your listing URL","Your MLS page, Zillow/Redfin link, or virtual tour \u2014 any URL works."),
         ("Paste your link","Your code appears instantly in the link tab."),
         ("Print for signs & flyers","SVG for the sign printer, PNG for flyers. Yard signs need 10+ cm \u2014 see the 1:10 rule of thumb.")],
  studio_h2="Make your real estate QR code",
  faq=[("What do agents usually link to?","Listing pages, virtual tours, open-house schedules, mortgage calculators, and the agent\u2019s contact card."),
       ("How big for a yard sign?","Use the 1:10 rule of thumb: code width at least one-tenth of the viewing distance. A sign read from 5 meters needs a 50 cm code \u2014 SVG export keeps it sharp at any size."),
       ("Can I add my photo or brokerage logo?","Yes \u2014 upload your logo or headshot in the center. Error correction adjusts automatically so it still scans."),
       ("What if the listing sells?","Point the code at your agent profile or listings page instead of a single property, so the sign keeps working after the sale. The code itself never expires.")]),
]
PAGES += [
dict(slug="pdf-qr-code", dtype="url",
  title="Free PDF QR Code Generator | FreeQrly",
  desc="Turn any PDF link into a scannable QR code. Free, no sign-up for static codes. Upload your PDF to Drive or Dropbox, paste the link, done.",
  kw="pdf qr code generator",
  h1='Your PDF, <span class="hl hl-honey">one scan away</span>.',
  lede="Menus, brochures, price lists, resumes \u2014 put your PDF behind a QR code. Host the file anywhere, paste the link, print the code. Scanners open the PDF straight away.",
  steps=[("Host your PDF","Upload it to Google Drive, Dropbox, or your own site, and copy the share link (anyone-with-link)."),
         ("Paste the link","Drop the link into the Website field \u2014 your code appears instantly."),
         ("Print it anywhere","Flyers, menus, posters, packaging. PNG or SVG, never expires.")],
  studio_h2="Make your PDF QR code",
  faq=[("Can I upload a PDF directly here?","FreeQrly does not host files \u2014 your PDF lives on Drive, Dropbox, or your site, and the QR code simply opens its link. That also means you can swap the file later without reprinting, as long as the link stays the same."),
       ("Will the QR code still work if I update the PDF?","Yes, if you replace the file at the same link (same Drive file, same URL). The code encodes the link, not the file itself."),
       ("What if the PDF is large?","Size does not matter for the code \u2014 it only encodes the link. Keep the PDF itself reasonable so it opens fast on phones."),
       ("Does it expire?","No. Static codes never expire and need no account.")]),
dict(slug="multi-link-qr-code", dtype="url",
  title="Free Multi-Link QR Code Generator | FreeQrly",
  desc="One QR code for all your links. Free, no sign-up for static codes. Point it at your Linktree, Beacons, or any link-in-bio page.",
  kw="multi link qr code",
  h1='All your links, <span class="hl hl-blush">one code</span>.',
  lede="One QR code that opens your whole link page \u2014 Instagram, shop, YouTube, booking, everything in one place. Point it at your Linktree, Beacons, or any link-in-bio page.",
  steps=[("Build your link page","Linktree, Beacons, or a simple page on your own site with all your links."),
         ("Paste its link","Drop the page URL into the Website field."),
         ("Print it everywhere","Packaging, cards, posters, receipts. One code, every link.")],
  studio_h2="Make your multi-link QR code",
  faq=[("What is a multi-link QR code?","A QR code that opens a page full of links instead of a single destination \u2014 the classic link-in-bio pattern. One code on your packaging can lead to your shop, your Instagram, and your YouTube at once."),
       ("Can I change the links later?","Yes \u2014 edit your link page (Linktree, Beacons, or your own page) and the same QR code shows the new links. The code encodes the page URL, not the links themselves."),
       ("Linktree or my own page \u2014 which is better?","Linktree and Beacons are fastest to set up. Your own page gives you full control over design and no third-party branding. Both work the same way with a QR code."),
       ("Does it expire?","No. Static codes never expire and need no account.")]),
dict(slug="menu-qr-code", dtype="menu",
  title="Free Menu QR Code Generator | FreeQrly",
  desc="Turn your restaurant menu into a scannable QR code. Free, no sign-up for static codes. Link a PDF menu or an online menu page.",
  kw="menu qr code generator",
  h1='Your menu, <span class="hl hl-mint">on every table</span>.',
  lede="A QR code on each table that opens your menu \u2014 PDF or online page. No app, no reprinting menus when a dish changes. Update the menu file, the same code keeps working.",
  steps=[("Put your menu online","A PDF on Drive or Dropbox, or a page on your site \u2014 copy the link."),
         ("Paste the link","Your code appears instantly in the Website field."),
         ("Print for every table","Table tents, window stickers, receipts. 1024 px export for crisp print.")],
  studio_h2="Make your menu QR code",
  faq=[("PDF menu or a web page \u2014 which is better?","A web page loads faster and is easier to edit; a PDF preserves your exact layout. Both work \u2014 pick whichever you already have."),
       ("Can I update the menu without reprinting?","Yes, if you replace the file at the same link. Guests scanning the same code see the new menu."),
       ("Do diners need an app?","No. Any phone camera opens the menu straight from the scan."),
       ("What size for table tents?","At least 3 x 3 cm so guests can scan from their seats. Bigger is safer in dim dining rooms.")]),
dict(slug="payment-qr-code", dtype="url",
  title="Free Payment QR Code Generator | FreeQrly",
  desc="Turn a PayPal, Venmo, or payment link into a scannable QR code. Free, no sign-up for static codes. Get paid with one scan.",
  kw="payment qr code generator",
  h1='Get paid, <span class="hl hl-honey">one scan</span>.',
  lede="Paste your PayPal, Venmo, Cash App, or checkout link and get a QR code customers scan to pay. Print it on invoices, market stalls, and tip jars.",
  steps=[("Copy your payment link","PayPal.me, Venmo profile, Cash App $cashtag link, or any checkout URL."),
         ("Paste the link","Your code appears instantly in the Website field."),
         ("Print it where you sell","Invoices, market stalls, tip jars, packaging.")],
  studio_h2="Make your payment QR code",
  faq=[("Which payment services work?","Any service that gives you a payment link: PayPal.me, Venmo, Cash App, Stripe Payment Links, and most checkout pages. The QR code just opens your link."),
       ("Is it safe to print a payment link?","The code only opens your public payment link \u2014 the same link you would send in a message. Never encode private account details; use the service's official share link."),
       ("Can I preset the amount?","Yes, if your payment link supports it (PayPal.me lets you add an amount). The code opens whatever the link contains."),
       ("Does it expire?","No. Static codes never expire and need no account.")]),
dict(slug="youtube-qr-code", dtype="url",
  title="Free YouTube QR Code Generator | FreeQrly",
  desc="Turn any YouTube video or channel into a scannable QR code. Free, no sign-up for static codes. Print it for packaging, posters, and merch.",
  kw="youtube qr code generator",
  h1='Your video, <span class="hl hl-blush">one scan from playing</span>.',
  lede="Paste any YouTube video or channel URL and get a QR code that opens it straight in the app. Posters, packaging, merch, business cards \u2014 viewers scan and watch.",
  steps=[("Copy the YouTube link","Video, channel, Short, or playlist \u2014 any YouTube URL."),
         ("Paste the link","Your code appears instantly in the Website field."),
         ("Print it where viewers look","Posters, merch, packaging, handouts. 1024 px export for print.")],
  studio_h2="Make your YouTube QR code",
  faq=[("Video, channel, or playlist?","All three work \u2014 the code opens whatever YouTube URL you paste. A channel link grows your subscribers; a video link plays one video."),
       ("Does it open in the YouTube app?","On most phones, yes \u2014 tapping the scanned link offers the app if installed, otherwise it opens in the browser."),
       ("Can I add my logo?","Yes \u2014 upload your logo and set your brand colors. Keep contrast high so it scans in any light."),
       ("Does it expire if I rename the channel?","The code encodes the exact URL. Channel URLs with custom handles change if the handle changes \u2014 use the channel ID URL for permanence, or make a fresh code.")]),
dict(slug="whatsapp-qr-code", dtype="url",
  title="Free WhatsApp QR Code Generator | FreeQrly",
  desc="Turn your WhatsApp number or chat link into a scannable QR code. Free, no sign-up for static codes. Customers scan and message you.",
  kw="whatsapp qr code generator",
  h1='Chat with you, <span class="hl hl-mint">one scan</span>.',
  lede="Paste your WhatsApp chat link (wa.me) and get a QR code that opens a chat with you. Shop windows, business cards, packaging \u2014 customers scan and start talking.",
  steps=[("Copy your wa.me link","wa.me/ followed by your full international number, e.g. wa.me/15551234567."),
         ("Paste the link","Your code appears instantly in the Website field."),
         ("Print it where customers look","Shop window, cards, receipts, packaging.")],
  studio_h2="Make your WhatsApp QR code",
  faq=[("How do I get my WhatsApp link?","Use wa.me/ plus your number in international format, no plus sign, no spaces \u2014 e.g. wa.me/15551234567. You can also add ?text=Hello to prefill a message."),
       ("Can I prefill a message?","Yes \u2014 append ?text=Your%20message to the wa.me link. When someone scans, the chat opens with your text ready to send."),
       ("Do I need WhatsApp Business?","No. A personal number works the same way. WhatsApp Business adds catalogs and auto-replies, but the QR code works with either."),
       ("Does it expire?","No. Static codes never expire and need no account.")]),
]

PAGES += [
dict(slug="tiktok-qr-code", dtype="url",
  title="Free TikTok QR Code Generator | FreeQrly",
  desc="Turn your TikTok profile or video into a scannable QR code. Free, no sign-up for static codes. Print it for packaging, posters, and merch.",
  kw="tiktok qr code generator",
  h1='Your TikTok, <span class="hl hl-blush">one scan to follow</span>.',
  lede="Paste your TikTok profile or video link and get a QR code that opens it straight in the app. Packaging, posters, merch, business cards — new followers without the username spelling.",
  steps=[("Copy your TikTok link","Profile, video, or hashtag — any TikTok URL. From the app: Share → Copy link."),
         ("Paste the link","Your code appears instantly in the Website field."),
         ("Print it where fans look","Packaging, posters, merch, flyers. 1024 px export for print.")],
  studio_h2="Make your TikTok QR code",
  faq=[("Profile link or a specific video?","Profile link for general follows. A video link plays one video — handy for campaigns, packaging inserts, and posters for a launch."),
       ("Does it open in the TikTok app?","On most phones, yes — tapping the scanned link offers the app if installed, otherwise it opens in the browser."),
       ("Can I add my logo or brand colors?","Yes — upload your logo and set your brand colors. Keep contrast high so it scans in any light."),
       ("Does it expire if I change my username?","The code encodes the exact URL, so if your handle changes, make a fresh code. The code itself never expires.")]),
dict(slug="spotify-qr-code", dtype="url",
  title="Free Spotify QR Code Generator | FreeQrly",
  desc="Turn any Spotify song, playlist, or artist page into a scannable QR code. Free, no sign-up for static codes. Share music offline.",
  kw="spotify qr code generator",
  h1='Your sound, <span class="hl hl-mint">one scan to play</span>.',
  lede="Paste any Spotify link — song, album, playlist, artist, podcast — and get a QR code that opens it in the app. Flyers, posters, merch, café tables: listeners scan and press play.",
  steps=[("Copy the Spotify link","In the app: Share → Copy link. Works for songs, playlists, artists, and podcasts."),
         ("Paste the link","Your code appears instantly in the Website field."),
         ("Print it where listeners are","Posters, merch, menus, flyers. 1024 px export for print.")],
  studio_h2="Make your Spotify QR code",
  faq=[("Song, playlist, or artist — which link?","All three work. A song link plays one track; a playlist link opens the list; an artist link opens the profile. Pick the one your audience should land on."),
       ("Does it open in the Spotify app?","On most phones, yes — tapping the scanned link offers the app if installed, otherwise it opens in the browser. Free accounts can open it too."),
       ("Is this the same as a Spotify Code?","No. Spotify Codes are the scannable barcodes inside the Spotify app. A QR code works everywhere — posters, print, packaging — with any phone camera, no Spotify app needed to scan."),
       ("Does it expire?","No. Static codes never expire and need no account.")]),
dict(slug="facebook-qr-code", dtype="url",
  title="Free Facebook QR Code Generator | FreeQrly",
  desc="Turn your Facebook page, group, or post into a scannable QR code. Free, no sign-up for static codes. Print it for your shop and flyers.",
  kw="facebook qr code generator",
  h1='Your page, <span class="hl hl-honey">one scan to like</span>.',
  lede="Paste your Facebook page, group, event, or post URL and get a scannable code. Shop windows, flyers, receipts, packaging — new followers without the page-name spelling.",
  steps=[("Copy your Facebook link","Page, group, event, or post — any Facebook URL. From the app: Share → Copy link."),
         ("Paste the link","Your code appears instantly in the Website field."),
         ("Print it where customers look","Shop window, counter cards, flyers, packaging. 1024 px export for print.")],
  studio_h2="Make your Facebook QR code",
  faq=[("Page, group, or event?","All work — the code opens whatever Facebook URL you paste. A page link grows followers; an event link fills seats."),
       ("Does it open in the Facebook app?","On most phones, yes — tapping the scanned link offers the app if installed, otherwise it opens in the browser."),
       ("Can I add my logo or brand colors?","Yes — upload your logo and set your brand colors. Keep contrast high so it scans in any light."),
       ("Does it expire?","No. Static codes never expire and need no account.")]),
dict(slug="google-maps-qr-code", dtype="url",
  title="Free Google Maps QR Code Generator | FreeQrly",
  desc="Turn any Google Maps location into a scannable QR code. Free, no sign-up for static codes. Customers scan and navigate straight to you.",
  kw="google maps qr code generator",
  h1='Directions, <span class="hl hl-mint">one scan</span>.',
  lede="Paste any Google Maps link — your business, an event venue, a meeting point — and get a QR code that opens directions. Invitations, flyers, shop windows: guests scan and navigate straight to you.",
  steps=[("Copy the Maps link","Search the place in Google Maps → Share → Copy link. Any place, business, or dropped pin works."),
         ("Paste the link","Your code appears instantly in the Website field."),
         ("Print it where people decide","Invitations, flyers, shop window, receipts. 1024 px export for print.")],
  studio_h2="Make your Google Maps QR code",
  faq=[("Business listing or a dropped pin?","Both work. A business listing shows reviews and hours; a dropped pin is better for a field, a trailhead, or a venue without a listing."),
       ("Does it open navigation automatically?","The code opens the place in Google Maps (or the browser). One tap on Directions starts navigation — guests pick their mode and go."),
       ("Can I add my logo?","Yes — upload your logo and set your brand colors. Keep contrast high so it scans outdoors in bright light."),
       ("Does it expire if the business moves?","The code encodes the exact Maps URL. If the listing changes, make a fresh code. The code itself never expires.")]),
dict(slug="bitcoin-qr-code", dtype="bitcoin",
  title="Free Bitcoin QR Code Generator | FreeQrly",
  desc="Create a Bitcoin payment QR code with wallet address, amount, and label. Free, no sign-up, generated entirely in your browser \u2014 your address never leaves your device.",
  kw="bitcoin qr code generator",
  h1='Get paid in Bitcoin, <span class="hl hl-mint">one scan away</span>.',
  lede="Type your wallet address, add an amount and a label, and get a printable QR code. Wallets scan it and pre-fill the payment \u2014 no typing long addresses by hand.",
  steps=[("Enter your wallet address","Copy it from your wallet app \u2014 double-check the first and last characters."),
         ("Add amount and label (optional)","Set the BTC amount so the payer can't get it wrong; add a label like \u201cCoffee\u201d for your records."),
         ("Print or share","Download a high-resolution PNG for your counter, invoice, or website. It works forever.")],
  studio_h2="Make your Bitcoin QR code",
  faq=[("Is my wallet address safe here?","Yes. The code is generated entirely in your browser \u2014 your address is never uploaded or stored anywhere. For extra safety, verify the code decodes to your address before sharing it."),
       ("Do I have to set an amount?","No. Leave it blank and the payer enters the amount in their wallet. Setting it is handy for fixed prices."),
       ("Which wallets can scan it?","Any wallet that supports BIP-21 payment URIs \u2014 that's virtually all of them. The code opens the wallet with your address pre-filled."),
       ("Can someone change where the money goes?","Only if they make their own code. Always generate the code yourself and verify it decodes to your address \u2014 never trust a payment code someone else made for you.")]),
dict(slug="coupon-qr-code", dtype="coupon",
  title="Free Coupon QR Code Generator | FreeQrly",
  desc="Turn a promo code into a scannable QR code. Free, no sign-up. Print it on flyers, receipts, packaging, and table tents.",
  kw="coupon qr code generator",
  h1='Your promo code, <span class="hl hl-blush">ready to scan</span>.',
  lede="Type your coupon code and a short description, and get a QR code customers can scan at checkout. Flyers, receipts, packaging \u2014 anywhere a typed code gets mistyped.",
  steps=[("Enter your coupon code","The exact code customers type at checkout, e.g. SAVE20."),
         ("Add a description","What they get \u2014 \u201c20% off\u201d beats a bare code."),
         ("Print where shoppers see it","Flyers, shelf tags, receipts, takeout bags. 1024 px export for crisp print.")],
  studio_h2="Make your coupon QR code",
  faq=[("What does the scanner see?","Your description plus the code, as plain text \u2014 e.g. \u201c20% off\u201d on one line and \u201cCode: SAVE20\u201d on the next. Staff type it in as usual."),
       ("Can it apply the discount automatically?","No \u2014 this is a static code carrying the promo text, not a deep link into your store. Pair it with a short URL to the sale page if you want one scan to do both."),
       ("One code per coupon or one for all?","One code per coupon. Each code is static and free, so make as many as you have promotions."),
       ("Does it expire?","The code itself never expires. When the promotion ends, stop printing it \u2014 the code can't enforce dates.")]),
dict(slug="app-store-qr-code", dtype="appstore",
  title="Free App Store QR Code Generator | FreeQrly",
  desc="One QR code for your iOS App Store and Google Play links. Free, no sign-up. Print it on ads, packaging, posters, and receipts.",
  kw="app store qr code generator",
  h1='Get your app installed, <span class="hl hl-honey">one scan away</span>.',
  lede="Paste your App Store and Google Play links and get a single QR code. One scan opens the right store \u2014 no more \u201ciPhone or Android?\u201d on your poster.",
  steps=[("Copy both store links","Your App Store and Google Play URLs \u2014 one of them is enough to start."),
         ("Paste them in","iOS link first, Android second. Your code appears instantly."),
         ("Print it everywhere","Ads, packaging, posters, receipts, app launch slides. SVG scales to billboard size.")],
  studio_h2="Make your app store QR code",
  faq=[("How does one code open two stores?","The code opens your iOS link by default; Android users get your Play link. Set both so every scanner lands in the right store."),
       ("What if I only have one platform?","Just fill that one. The code opens whichever link you provided."),
       ("Can it detect the phone and route automatically?","This is a static code with your links \u2014 it opens the iOS link first. For automatic device detection you'd need a smart link service in front; the code still works as the front door."),
       ("Does it track installs?","No \u2014 static codes are private by design and phone nothing home. Your App Store Connect and Play Console already count installs.")]),
dict(slug="mp3-qr-code", dtype="mp3",
  title="Free MP3 QR Code Generator | FreeQrly",
  desc="Link any audio \u2014 a song, a podcast episode, a voice note \u2014 to a QR code. Free, no sign-up for static codes.",
  kw="mp3 qr code generator",
  h1='Your sound, <span class="hl hl-blush">one scan away</span>.',
  lede="Paste the link to your audio file and get a QR code that plays it. Album inserts, podcast flyers, museum labels, greeting cards \u2014 anywhere listening starts with a scan.",
  steps=[("Put your audio online","An MP3 on your site, Drive, Dropbox, or SoundCloud \u2014 copy the direct link."),
         ("Paste the link","Your code appears instantly in the Audio field."),
         ("Print where ears are","Album art, flyers, exhibits, invitations. 1024 px export for print.")],
  studio_h2="Make your MP3 QR code",
  faq=[("What audio can I link?","Anything with a URL: MP3 files, podcast episodes, SoundCloud tracks, voice notes on Drive. If a browser can play it, the code can open it."),
       ("Does the code contain the audio itself?","No \u2014 it holds the link. Keep the file online at the same address and the code plays it forever."),
       ("Can I link Spotify or Apple Music?","Yes \u2014 paste the share link. Note listeners may need that app installed; a direct MP3 link plays everywhere."),
       ("Will it play automatically on scan?","Phones open the link in the browser or audio app; autoplay depends on the listener's settings. Most tap play once.")]),
]

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

def strip_tags(s):
    return re.sub(r'<[^>]+>', '', s)

def howto_json(p):
    # HowTo steps mirror the page's own "how" steps — no invented steps.
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": p["studio_h2"],
        "description": strip_tags(p["lede"]),
        "step": [
            {"@type": "HowToStep", "name": t, "text": strip_tags(d)}
            for t, d in p["steps"]
        ],
    }, ensure_ascii=False)

def build(p):
    url = f"https://freeqrly.com/{p['slug']}/"
    studio = STUDIO_H2_RE.sub(
        '<div class="shead"><div class="over">The studio</div><h2>%s</h2></div>' % p["studio_h2"], STUDIO)
    studio = studio.replace('<main class="studio" id="studio">',
        '<main class="studio" id="studio">\n    <div class="mascot m-peek" aria-hidden="true"><img loading="lazy" decoding="async" width="512" height="512" src="https://assets.freeqrly.com/mascots/v1/studio-qr.webp" alt="Qly presenting a QR code" data-studio-mascot data-mascot-default="studio-qr"></div>', 1)
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
<link rel="alternate" hreflang="zh" href="https://freeqrly.com/zh/{p['slug']}/">
<link rel="alternate" hreflang="es" href="https://freeqrly.com/es/{p['slug']}/">
<link rel="alternate" hreflang="hi" href="https://freeqrly.com/hi/{p['slug']}/">
<link rel="alternate" hreflang="ar" href="https://freeqrly.com/ar/{p['slug']}/">
<link rel="alternate" hreflang="pt" href="https://freeqrly.com/pt/{p['slug']}/">
<link rel="alternate" hreflang="fr" href="https://freeqrly.com/fr/{p['slug']}/">
<link rel="alternate" hreflang="ru" href="https://freeqrly.com/ru/{p['slug']}/">
<link rel="alternate" hreflang="de" href="https://freeqrly.com/de/{p['slug']}/">
<link rel="alternate" hreflang="ja" href="https://freeqrly.com/ja/{p['slug']}/">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta name="theme-color" content="#e9eef4">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:type" content="website">
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
<link rel="icon" type="image/png" href="../assets/img/favicon-qly.png">
<link rel="apple-touch-icon" href="../assets/img/favicon-qly.png">
<link rel="stylesheet" href="../assets/css/main.css">
<style>{EXTRA_CSS}</style>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebApplication","name":"FreeQrly — {p["kw"]}","applicationCategory":"UtilitiesApplication","operatingSystem":"Any","speakable":{{"@type":"SpeakableSpecification","cssSelector":["h1",".lede"]}},"offers":{{"@type":"Offer","price":"0"}},"url":"{url}","description":"{p["desc"]}"}}
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
<script type="application/ld+json">
{howto_json(p)}
</script>
</head>
<body data-lp="{p["slug"]}" data-type="{p["dtype"]}">
<div class="wrap">
{HEADER}
  <section class="hero lp-hero">
    <div>
      <div class="kicker">Free · Static codes need no sign-up · No watermark</div>
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
    <div class="fin"><a href="/" style="color:inherit">FreeQrly</a> — made quietly, static codes in your browser.</div>
    <div class="rule"></div>
    <div class="lplinks">{foot_links}</div>
    <div class="lplinks"><a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a> · <a href="mailto:hello@freeqrly.com">hello@freeqrly.com</a></div>
    <div class="tiny">© 2026 FreeQrly</div>
  </footer>
</div>
<script src="../assets/lib/qr-code-styling.js"></script>
<script src="../assets/lib/jszip.min.js"></script>
<script src="/assets/js/vcard.js?v=b3f-20261015"></script>
<script src="../assets/js/app.js?v=b3f-20261015"></script>
</body>
</html>
'''

for p in PAGES:
    d = os.path.join(SITE, p["slug"])
    os.makedirs(d, exist_ok=True)
    html = build(p)
    open(os.path.join(d, "index.html"), "w").write(html)
    print("wrote", p["slug"], len(html), "bytes")
