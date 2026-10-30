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

HEADER = '''<div id="siteHeader"></div>
<script src="../assets/js/site-header.js?v=b3q-20261019"></script>
<script src="../assets/js/acct-menu.js?v=b3q-20261019"></script>
<script>
(function(){
  var LANGS = ["en","zh","es","hi","ar","pt","fr","ru","de","ja"];
  var LANGN = {en:"English",zh:"中文",es:"Español",hi:"हिन्दी",ar:"العربية",pt:"Português",fr:"Français",ru:"Русский",de:"Deutsch",ja:"日本語"};
  function getLang(){
    var m = location.pathname.match(/^\/(zh|es|hi|ar|pt|fr|ru|de|ja)(\/.*)?$/);
    if(m) return m[1];
    try{
      var s = localStorage.getItem("freeqrly-lang");
      if(s && LANGS.indexOf(s) >= 0) return s;
    }catch(e){}
    return "en";
  }
  function getCachedUser(){
    try{
      var c = localStorage.getItem("freeqrly-user");
      if(!c) return null;
      var u = JSON.parse(c);
      return (u && u.email) ? u : null;
    }catch(e){ return null; }
  }
  var lang = getLang();
  if(window.initSiteHeader){
    window.initSiteHeader({
      nav: [
        {href: "#studio", text: "Studio"},
        {href: "#how", text: "How it works"},
        {href: "#faq", text: "FAQ"}
      ],
      t: function(k){
        var T = {
          en: {signin:"Sign in",acctDashboard:"Dashboard",acctExport:"Export my data",acctDelete:"Delete account",acctLogout:"Log out",acctSignedInWith:"Signed in with {method}",acctDeleteConfirm:"Delete your account? This cannot be undone.",acctDeleteFailed:"Couldn't delete the account. Please try again.",acctNetErr:"Network error. Please try again."},
          zh: {signin:"登录",acctDashboard:"Dashboard",acctExport:"导出我的数据",acctDelete:"删除账号",acctLogout:"退出登录",acctSignedInWith:"通过{method}登录",acctDeleteConfirm:"确定删除账号吗？此操作无法撤销。",acctDeleteFailed:"删除失败，请重试。",acctNetErr:"网络错误，请重试。"},
          es: {signin:"Iniciar sesión",acctDashboard:"Dashboard",acctExport:"Exportar mis datos",acctDelete:"Eliminar cuenta",acctLogout:"Cerrar sesión",acctSignedInWith:"Sesión con {method}",acctDeleteConfirm:"¿Eliminar tu cuenta? No se puede deshacer.",acctDeleteFailed:"No se pudo eliminar. Inténtalo de nuevo.",acctNetErr:"Error de red. Inténtalo de nuevo."},
          hi: {signin:"साइन इन",acctDashboard:"Dashboard",acctExport:"मेरा डेटा निर्यात करें",acctDelete:"खाता हटाएं",acctLogout:"लॉग आउट",acctSignedInWith:"{method} से लॉग इन",acctDeleteConfirm:"अपना खाता हटाएं? इसे पूर्ववत नहीं किया जा सकता।",acctDeleteFailed:"हटाया नहीं जा सका। पुनः प्रयास करें।",acctNetErr:"नेटवर्क त्रुटि। पुनः प्रयास करें।"},
          ar: {signin:"تسجيل الدخول",acctDashboard:"Dashboard",acctExport:"تصدير بياناتي",acctDelete:"حذف الحساب",acctLogout:"تسجيل الخروج",acctSignedInWith:"تم تسجيل الدخول عبر {method}",acctDeleteConfirm:"حذف حسابك؟ لا يمكن التراجع عن هذا.",acctDeleteFailed:"تعذر الحذف. حاول مجددًا.",acctNetErr:"خطأ في الشبكة. حاول مجددًا."},
          pt: {signin:"Entrar",acctDashboard:"Dashboard",acctExport:"Exportar meus dados",acctDelete:"Excluir conta",acctLogout:"Sair",acctSignedInWith:"Sessão com {method}",acctDeleteConfirm:"Excluir sua conta? Não pode ser desfeito.",acctDeleteFailed:"Não foi possível excluir. Tente novamente.",acctNetErr:"Erro de rede. Tente novamente."},
          fr: {signin:"Se connecter",acctDashboard:"Dashboard",acctExport:"Exporter mes données",acctDelete:"Supprimer le compte",acctLogout:"Se déconnecter",acctSignedInWith:"Connecté via {method}",acctDeleteConfirm:"Supprimer votre compte ? Irréversible.",acctDeleteFailed:"Suppression impossible. Réessayez.",acctNetErr:"Erreur réseau. Réessayez."},
          ru: {signin:"Войти",acctDashboard:"Dashboard",acctExport:"Экспортировать мои данные",acctDelete:"Удалить аккаунт",acctLogout:"Выйти",acctSignedInWith:"Вход через {method}",acctDeleteConfirm:"Удалить аккаунт? Это необратимо.",acctDeleteFailed:"Не удалось удалить. Попробуйте ещё раз.",acctNetErr:"Ошибка сети. Попробуйте ещё раз."},
          de: {signin:"Anmelden",acctDashboard:"Dashboard",acctExport:"Meine Daten exportieren",acctDelete:"Konto löschen",acctLogout:"Abmelden",acctSignedInWith:"Angemeldet mit {method}",acctDeleteConfirm:"Konto wirklich löschen? Kann nicht rückgängig gemacht werden.",acctDeleteFailed:"Löschen fehlgeschlagen. Bitte erneut versuchen.",acctNetErr:"Netzwerkfehler. Bitte erneut versuchen."},
          ja: {signin:"ログイン",acctDashboard:"Dashboard",acctExport:"データをエクスポート",acctDelete:"アカウントを削除",acctLogout:"ログアウト",acctSignedInWith:"{method}でログイン中",acctDeleteConfirm:"アカウントを削除しますか？元に戻せません。",acctDeleteFailed:"削除できませんでした。もう一度お試しください。",acctNetErr:"ネットワークエラー。もう一度お試しください。"}
        };
        var tb = T[lang] || T.en;
        return tb[k] || k;
      },
      lang: lang,
      langs: LANGS,
      langNames: LANGN,
      onLangChange: function(code){
        try{ localStorage.setItem("freeqrly-lang", code); }catch(e){}
        var m = location.pathname.match(/^\/(zh|es|hi|ar|pt|fr|ru|de|ja)(\/.*)?$/);
        var enPath = m ? (m[2] || "/") : location.pathname;
        location.href = (code === "en" ? enPath : "/" + code + enPath);
      },
      user: getCachedUser(),
      showDashboard: true
    });
  }
  // Revalidate auth in background; update if changed
  fetch("/api/auth/me", {credentials: "same-origin"}).then(function(r){
    return r.json().catch(function(){ return {}; });
  }).then(function(d){
    var me = d.user || null;
    var user = (me && me.email) ? {email: me.email, name: me.name, avatar: me.avatar || me.avatar_url || null, authMethod: me.authMethod} : null;
    try{
      if(user) localStorage.setItem("freeqrly-user", JSON.stringify(user));
      else localStorage.removeItem("freeqrly-user");
    }catch(e){}
    if(window.renderSiteHeader) window.renderSiteHeader({user: user});
  }).catch(function(){});
})();
</script>'''

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
dict(slug="black-friday-qr-code", dtype="coupon",
  title="Free Black Friday QR Code Generator | FreeQrly",
  desc="Free QR codes for your Black Friday sale: coupon codes customers scan instead of typing, sale pages you can repoint all weekend. Static codes need no sign-up and never expire.",
  kw="black friday qr code",
  h1='Black Friday deals, <span class="hl hl-blush">one scan away</span>.',
  lede="Put the sale on every surface \u2014 window posters, shelf tags, receipts, packaging. Turn the promo code into a scannable code, or link straight to the deal. When the offer changes mid-weekend, a dynamic code changes with it. The poster doesn\u2019t.",
  steps=[("Decide what the scan opens","A promo code, your sale page, a doorbuster list \u2014 one code, one job."),
         ("Make the code","Coupon codes are static: free, no sign-up, generated in your browser. For a sale page, sign in free and make it dynamic so you can repoint it later."),
         ("Print once, swap all weekend","Early access Thursday, doorbusters Friday, Cyber Monday leftovers on Monday \u2014 edit the destination, keep the poster.")],
  studio_h2="Make your Black Friday QR code",
  faq=[("Static or dynamic \u2014 which does a sale need?","Static for the coupon code itself: it carries the code as text and never expires. Dynamic for anything that changes \u2014 the sale page, hourly drops, stock that sells out. Dynamic codes are free with a sign-in, and currently unlimited for a limited time."),
       ("Can I change where a printed code points?","Yes \u2014 that\u2019s what dynamic means here. Edit the destination from your dashboard any time; the printed code never changes."),
       ("What happens to my codes after the sale?","Nothing expires. Repoint dynamic codes to your next campaign, and keep the posters for next year \u2014 same codes, new offers."),
       ("How big should a window poster code be?","Big enough to scan through glass from the sidewalk \u2014 10 cm (4 in) or more. Our blog\u2019s print size guide has the full distance table.")]),
dict(slug="christmas-qr-code", dtype="event",
  title="Free Christmas QR Code Generator | FreeQrly",
  desc="Free QR codes for Christmas: cards that play a video greeting, gift tags with a surprise inside, party invitations that add themselves to calendars. No sign-up for static codes.",
  kw="christmas qr code",
  h1='Hide a little Christmas <span class="hl hl-mint">inside a code</span>.',
  lede="Tape a code inside a card and it plays your video greeting. Stick one on a gift tag. Or send party invitations that land straight in your guests\u2019 calendars \u2014 date, time and place, no typing. Free, and made in your browser.",
  steps=[("Pick your moment","A video greeting, a photo album, a playlist \u2014 or the party itself, as a calendar event."),
         ("Paste the link, or set the date","Links become static codes instantly, no sign-up. For invitations, the studio below starts on Event: title, start, end, place."),
         ("Print it where the surprise lands","Inside the card, on the gift tag, on the invitation envelope. The 1024 px export stays crisp at card size.")],
  studio_h2="Make your Christmas QR code",
  faq=[("How do I put a video inside a Christmas card?","Upload the video somewhere with a shareable link \u2014 an unlisted YouTube video is perfect \u2014 make a QR code from the link, and print it inside the card. One scan and it plays."),
       ("Can a code add the party to my guests\u2019 calendars?","Yes. The Event type (the studio below starts on it) carries the title, time and place; one scan adds the party to their calendar app."),
       ("Will the code still work next Christmas?","Yes \u2014 static codes never expire. The same printed code works next year too, as long as the page or video behind it is still online."),
       ("I need a different code on every gift tag. Help?","Use Batch mode in the generator: one link per line, one code per tag, all downloaded as a ZIP.")]),
]
PAGES += [
dict(slug="dynamic-qr-code", dtype="url", mode="dynamic",
  title="Free Dynamic QR Code Generator | FreeQrly",
  desc="Create a free dynamic QR code you can edit after printing. Change the destination anytime, see scan counts \u2014 free sign-in, no expiry, no watermark.",
  kw="dynamic qr code",
  h1='A QR code you can <span class="hl hl-blush">change after printing</span>.',
  lede="Print it once, point it anywhere, forever. A dynamic code keeps the same printed pattern while you change where it goes \u2014 and shows you how often it gets scanned. Free with a sign-in.",
  steps=[("Make a code here","Paste your link in the studio below \u2014 your code appears instantly, free, no sign-up for the static version."),
         ("Sign in free to make it dynamic","From your dashboard, create a dynamic code for the same destination. It looks the same on paper \u2014 the difference is on our side."),
         ("Edit and track from your dashboard","Change the destination anytime, check scan counts, and repoint old posters to your next campaign. The printed code never changes.")],
  studio_h2="Try the studio \u2014 then make it dynamic",
  faq=[("What is a dynamic QR code?","A code whose destination lives on the server side instead of inside the pattern. The printed code stays the same, but you can change where it points after printing \u2014 and see how many times it was scanned."),
       ("How is it different from a static code?","A static code carries its content inside the pattern: free, no sign-up, made in your browser, and it can never change. A dynamic code needs a free sign-in, but you can edit its destination and track scans. Both never expire."),
       ("How many dynamic codes are free?","20 on the free plan \u2014 and right now, during the limited-time offer, unlimited for everyone. Pro is unlimited, always."),
       ("Do dynamic codes expire?","No. Dynamic codes never expire. If you stop using one, repoint it to your next campaign instead of reprinting \u2014 the poster keeps working.")]),
dict(slug="ticket-qr-code", dtype="url",
  title="Free Ticket QR Code Generator | FreeQrly",
  desc="Create free QR codes for tickets: link to your ticket or check-in page, print one code per ticket with Batch mode, no sign-up for static codes, never expires.",
  kw="qr code ticket",
  h1='One scan at the door, <span class="hl hl-mint">no ticket queue</span>.',
  lede="Put a QR code on every ticket, poster, and confirmation email. Guests scan at the entrance and land straight on your ticket or check-in page \u2014 concerts, conferences, workshops, school events.",
  steps=[("Link to your ticket page","Your ticketing page, check-in form, or event details \u2014 one code, one destination."),
         ("Make the code","Paste the link in the studio below. Print-ready PNG or SVG, free, no watermark, no sign-up for static codes."),
         ("One code per ticket, with Batch","Need a different code on every ticket? Batch mode takes one link per line and downloads every code as a ZIP.")],
  studio_h2="Make your ticket QR code",
  faq=[("What should a ticket QR code link to?","Your ticket page, a check-in form, or the event details page. The code simply opens that page on the guest\u2019s phone \u2014 keep the page itself as the source of truth for entry."),
       ("Can I make a different code for every ticket?","Yes \u2014 Batch mode generates one code per link: paste one ticket link per line, download them all as a ZIP, and print each on its own ticket."),
       ("Do ticket QR codes expire?","No. Static codes never expire. If the event moves, point the page behind the code at the new details \u2014 or, with a dynamic code, repoint the code itself without reprinting."),
       ("How big should I print it on a ticket?","At least 2 \u00d7 2 cm with a clear quiet margin, at 1024 px export or higher. At a busy entrance, bigger is safer \u2014 a code that scans first try keeps the line moving.")]),
]

PAGES += [
dict(slug="freeqrly-vs-qr-tiger", dtype="url",
  title="FreeQrly vs QR Tiger: Free Dynamic Codes, Scan Limits, and Price | FreeQrly",
  desc="FreeQrly vs QR Tiger on the free plan: 20 dynamic codes (currently unlimited) with unlimited scans, versus 3 codes capped at 500 scans each. Static codes are free on both. Pro costs $9/month; QR Tiger Regular starts at $7/month.",
  kw="freeqrly vs qr tiger",
  h1='FreeQrly vs QR Tiger: <span class="hl hl-mint">where the free plan ends</span>.',
  lede="If you only need static codes, both tools are free forever. The difference starts with dynamic codes: FreeQrly \u2014 freeqrly.com gives you 20 free dynamic codes (currently unlimited during the limited-time offer) with unlimited scans, while QR Tiger's free plan gives you 3 dynamic codes capped at 500 scans each. Pick by how many editable codes you print, and how many scans they will get.",
  steps=[("Decide static or dynamic","Static fits anything that never changes: a homepage, a WiFi login, a business card. Dynamic fits anything you may repoint or measure: a sale page, a menu, a campaign poster."),
         ("Make the code","Use the studio below. Static codes are free with no sign-up. For a dynamic code, sign in free and create it from your dashboard."),
         ("Print once, edit later","A dynamic code keeps its printed pattern while you change the destination and check scan counts. A static code never changes and never expires.")],
  studio_h2="Make your free QR code",
  faq=[("Do I need an account for static codes on either tool?","No. FreeQrly static codes need no sign-up, and QR Tiger's free plan includes unlimited static codes. The account question only matters for dynamic codes, and both need a free account there."),
       ("What happens when a QR Tiger free dynamic code reaches 500 scans?","QR Tiger lists a 500 scan limit on each free dynamic code. FreeQrly gives unlimited scans on free dynamic codes, so a poster that takes off does not hit a ceiling at 500."),
       ("Which paid plan is cheaper?","QR Tiger's Regular plan starts at $7 per month, below FreeQrly Pro at $9 per month (or $90 per year). The trade is allowance: Regular includes 12 dynamic codes, while FreeQrly Pro is unlimited. If you need more than 12 editable codes, the cheaper sticker price stops being cheaper per code."),
       ("Can I edit a printed code on both free plans?","Yes. QR Tiger's free dynamic codes can be edited and tracked, and FreeQrly's free dynamic codes can be edited after printing with scan statistics. The difference is quantity and the scan limit, not the ability itself.")],
  compare='''
  <h2>FreeQrly vs QR Tiger at a glance</h2>
  <p>FreeQrly \u2014 freeqrly.com, compared with QR Tiger (qrcode-tiger.com). Figures below are from each product's own pricing and plan pages, checked October 30, 2026.</p>
  <table>
    <thead><tr><th>Feature</th><th>FreeQrly</th><th>QR Tiger</th></tr></thead>
    <tbody>
      <tr><td><b>Static codes</b></td><td>Free, unlimited, no sign-up, no watermark, never expire</td><td>Free, unlimited, never expire (free plan account required)</td></tr>
      <tr><td><b>Free dynamic codes</b></td><td>20 with a free account (currently unlimited during the limited-time offer)</td><td>3</td></tr>
      <tr><td><b>Scan cap on free dynamic codes</b></td><td>Unlimited</td><td>500 scans each</td></tr>
      <tr><td><b>Edit after printing (free)</b></td><td>Yes</td><td>Yes</td></tr>
      <tr><td><b>Scan statistics (free)</b></td><td>Yes</td><td>Yes, basic tracking</td></tr>
      <tr><td><b>Batch creation (free)</b></td><td>Yes, up to 50 per batch</td><td>No \u2014 bulk creation is an Advanced plan ($16/month) feature</td></tr>
      <tr><td><b>Barcode generator</b></td><td>Yes, included</td><td>Not listed on the plan pages we checked</td></tr>
      <tr><td><b>QR API</b></td><td>Yes (see <a href="/developers/">Developers</a>)</td><td>Regular ($7) and up: 500 requests per month</td></tr>
      <tr><td><b>Paid plan entry</b></td><td>Pro $9/month or $90/year, unlimited dynamic codes</td><td>Regular $7/month, 12 dynamic codes</td></tr>
    </tbody>
  </table>
  <p class="csrc">Sources: <a href="/pricing/">FreeQrly pricing</a>; <a href="https://www.qrcode-tiger.com/software-subscription">QR Tiger subscription plan page</a>.</p>
  <h2>Who should pick which?</h2>
  <p><b>Pick FreeQrly if</b> you print more than 3 editable codes, or any code that might pass 500 scans; if you want batch creation, a barcode generator, or a QR API without paying; or if you want free static codes with no account at all. If you ever cancel Pro, your codes keep working.</p>
  <p><b>Pick QR Tiger if</b> you need its campaign extras \u2014 saved design templates, retargeting, password protection, expiry controls, geofencing, and white-label domains on Premium \u2014 or its enterprise seats and integrations (Canva, Monday.com, Zapier, HubSpot on higher tiers). For raw editable-code count, FreeQrly Pro is unlimited, so Tiger's edge is features and team tooling, not volume.</p>
  <p class="updated">Comparison checked October 30, 2026. Prices and limits change \u2014 check the pricing pages linked above before you decide.</p>
'''),
dict(slug="freeqrly-vs-qr-code-monkey", dtype="url",
  title="FreeQrly vs QR Code Monkey: Free Static Codes, Plus Dynamic | FreeQrly",
  desc="QR Code Monkey makes free static codes with logos and vector downloads. FreeQrly matches that and adds free dynamic codes you can edit, scan statistics, batch mode, a barcode generator, and a QR API.",
  kw="freeqrly vs qr code monkey",
  h1='FreeQrly vs QR Code Monkey: <span class="hl hl-honey">same free static codes, plus dynamic</span>.',
  lede="For a one-off static code, both tools are free forever. QR Code Monkey stops there: its free tool makes static codes only, with no editing and no scan statistics. FreeQrly \u2014 freeqrly.com keeps static codes free with no sign-up and no watermark, and adds free dynamic codes with editing and statistics, batch mode, a barcode generator, and a QR API.",
  steps=[("Decide static or dynamic","Static fits anything that never changes: a homepage, a business card, a poster. Dynamic fits anything you may repoint or measure: a sale page, a menu, a campaign."),
         ("Make the code","Use the studio below. Static codes are free with no sign-up. For a dynamic code, sign in free and create it from your dashboard."),
         ("Print once, edit later","A dynamic code keeps its printed pattern while you change the destination and check scan counts. A static code never changes and never expires.")],
  studio_h2="Make your free QR code",
  faq=[("Is QR Code Monkey really free?","Yes, for static codes: 100% free, including commercial use, with no expiry. The catch is only that the codes are static \u2014 you cannot edit them or track scans."),
       ("Can I edit a Monkey code after printing?","No. Monkey's own pages say the only limitation of its static codes is that you cannot change the content once printed. For editing and statistics, Monkey points you to its PRO upsell. FreeQrly's free dynamic codes are editable after printing with scan statistics."),
       ("Which has better design and download options?","Monkey's are genuinely good: logo upload, colors, shapes, templates, and PNG, SVG, PDF, and EPS downloads, with up to 30% error correction for a centered logo. FreeQrly offers logo upload, colors, and PNG and SVG downloads. If print-vector depth is your whole job, Monkey wins that row; if you also need editable codes, FreeQrly covers both."),
       ("Do I need an account on either for static codes?","No. Monkey's generator works without an account, and FreeQrly static codes need no sign-up. You only sign in when you want dynamic codes, statistics, or a dashboard.")],
  compare='''
  <h2>FreeQrly vs QR Code Monkey at a glance</h2>
  <p>FreeQrly \u2014 freeqrly.com, compared with QR Code Monkey at qrcode-monkey.com. Figures below are from each product's own pages, checked October 30, 2026.</p>
  <table>
    <thead><tr><th>Feature</th><th>FreeQrly</th><th>QR Code Monkey</th></tr></thead>
    <tbody>
      <tr><td><b>Static codes</b></td><td>Free, unlimited, no sign-up, no watermark, never expire</td><td>Free, never expire, free for commercial use</td></tr>
      <tr><td><b>Edit after printing</b></td><td>Yes, free dynamic codes</td><td>No \u2014 static only; editing lives in the PRO upsell</td></tr>
      <tr><td><b>Scan statistics</b></td><td>Yes, free dynamic codes</td><td>No \u2014 statistics live in the PRO upsell</td></tr>
      <tr><td><b>Batch creation</b></td><td>Yes, up to 50 per batch, free</td><td>No \u2014 bulk generation is a Premium feature</td></tr>
      <tr><td><b>Barcode generator</b></td><td>Yes, included</td><td>Not listed on the free tool's pages we checked</td></tr>
      <tr><td><b>Vector downloads</b></td><td>PNG and SVG</td><td>PNG, SVG, PDF, and EPS \u2014 Monkey's strongest row</td></tr>
      <tr><td><b>Logo and design</b></td><td>Logo upload, colors, dot styles</td><td>Logo upload, colors, gradients, shapes, templates</td></tr>
      <tr><td><b>Where static codes are made</b></td><td>In your browser; nothing leaves your device</td><td>On Monkey's site; generated image files are cached 24 hours</td></tr>
      <tr><td><b>Paid option</b></td><td>Pro $9/month or $90/year, unlimited dynamic codes</td><td>PRO platform for dynamic codes and statistics (see our <a href="/freeqrly-vs-qr-code-generator/">QR Code Generator comparison</a>)</td></tr>
    </tbody>
  </table>
  <p class="csrc">Sources: <a href="/pricing/">FreeQrly pricing</a>; <a href="https://www.qrcode-monkey.com/">QR Code Monkey homepage</a>.</p>
  <h2>Who should pick which?</h2>
  <p><b>Pick FreeQrly if</b> you want anything beyond a fixed code: editing after printing, scan counts, batch runs, barcodes, or an API \u2014 while keeping static codes free with no account.</p>
  <p><b>Pick QR Code Monkey if</b> you only ever need fixed codes and you care most about print design depth: EPS and PDF vectors, templates, gradients, and a 30% logo area. For that one job, it is the best free tool we checked \u2014 FreeQrly does not beat it on vector formats.</p>
  <p class="updated">Comparison checked October 30, 2026. Prices and limits change \u2014 check the pages linked above before you decide.</p>
'''),
]

PAGES += [
dict(slug="freeqrly-vs-qr-code-generator", dtype="url",
  title="FreeQrly vs QR Code Generator (Bitly): Free Static, Paid Dynamic | FreeQrly",
  desc="QR Code Generator by Bitly gives you free static codes that never expire, but editing and scan tracking need the paid PRO version. FreeQrly includes 20 free dynamic codes (currently unlimited) with editing and statistics.",
  kw="freeqrly vs qr code generator",
  h1='FreeQrly vs QR Code Generator: <span class="hl hl-blush">free static on both, dynamic is the split</span>.',
  lede="Both tools give you free static codes that never expire. The split is what happens after printing: QR Code Generator keeps editing and scan tracking in its paid PRO version, after a 14-day trial. FreeQrly \u2014 freeqrly.com gives you 20 free dynamic codes (currently unlimited during the limited-time offer) with editing and statistics included.",
  steps=[("Decide static or dynamic","Static fits anything that never changes: a homepage, a business card, a poster. Dynamic fits anything you may repoint or measure: a sale page, a menu, a campaign."),
         ("Make the code","Use the studio below. Static codes are free with no sign-up. For a dynamic code, sign in free and create it from your dashboard."),
         ("Print once, edit later","A dynamic code keeps its printed pattern while you change the destination and check scan counts. A static code never changes and never expires.")],
  studio_h2="Make your free QR code",
  faq=[("Are static codes really free on both?","Yes. QR Code Generator's own FAQ says all of its static codes are free and yours forever, and FreeQrly static codes are free with no sign-up. Neither expires."),
       ("What does the 14-day trial mean?","After signing up, QR Code Generator lets you try all features free for 14 days. Editing and tracking live in the PRO version, so when the trial ends you need a paid plan to keep them. FreeQrly's free dynamic codes have no trial clock."),
       ("Do I need an account to download PNG or SVG?","On QR Code Generator, yes: high-resolution JPG is the free download, and PNG, SVG, or EPS downloads require account signup. On FreeQrly, static PNG and SVG downloads need no sign-up."),
       ("Which paid plan is cheaper?","Close: QR Code Generator PRO starts at $9.99 per month billed annually for 2 dynamic codes, while FreeQrly Pro is $9 per month or $90 per year for unlimited dynamic codes. At the entry tier you pay about the same and get far more editable codes at FreeQrly; QR Code Generator's higher tiers add team seats, bulk creation, and API allowances that FreeQrly's single Pro tier does not itemize.")],
  compare='''
  <h2>FreeQrly vs QR Code Generator at a glance</h2>
  <p>FreeQrly \u2014 freeqrly.com, compared with QR Code Generator at qr-code-generator.com, part of Bitly. This is not The QR Code Generator at the-qrcode-generator.com, a different product. Figures below are from each product's own pages, checked October 30, 2026.</p>
  <table>
    <thead><tr><th>Feature</th><th>FreeQrly</th><th>QR Code Generator</th></tr></thead>
    <tbody>
      <tr><td><b>Static codes</b></td><td>Free, unlimited, no sign-up, never expire</td><td>Free, never expire (URL, vCard, text, email, SMS, Twitter, WiFi, Bitcoin)</td></tr>
      <tr><td><b>Sign-up for PNG/SVG download</b></td><td>No</td><td>Yes, signup required</td></tr>
      <tr><td><b>Edit after printing (free)</b></td><td>Yes, free dynamic codes</td><td>No \u2014 PRO version only</td></tr>
      <tr><td><b>Scan statistics (free)</b></td><td>Yes, free dynamic codes</td><td>No \u2014 PRO version only</td></tr>
      <tr><td><b>Free dynamic codes</b></td><td>20 (currently unlimited during the offer)</td><td>None free \u2014 14-day trial, then paid</td></tr>
      <tr><td><b>Paid entry</b></td><td>Pro $9/month or $90/year, unlimited dynamic codes</td><td>Starter $9.99/month billed annually, 2 dynamic codes, 10,000 scans/month</td></tr>
      <tr><td><b>Batch creation</b></td><td>Yes, up to 50 per batch, free</td><td>Paid tiers: 100 on Advanced, 500 on Professional</td></tr>
      <tr><td><b>QR API</b></td><td>Yes (see <a href="/developers/">Developers</a>)</td><td>Yes, plan-limited: 3,000 requests on Advanced, 10,000 on Professional</td></tr>
      <tr><td><b>Barcode generator</b></td><td>Yes, included</td><td>Not listed on the pages we checked</td></tr>
      <tr><td><b>Content types</b></td><td>17, including Batch</td><td>22 (their homepage count)</td></tr>
    </tbody>
  </table>
  <p class="csrc">Sources: <a href="/pricing/">FreeQrly pricing</a>; <a href="https://www.qr-code-generator.com/">QR Code Generator homepage</a>; <a href="https://www.qr-code-generator.com/blog/qr-code-generator-vs-qr-code-dynamic/">QR Code Generator PRO plans and pricing</a>.</p>
  <h2>Who should pick which?</h2>
  <p><b>Pick FreeQrly if</b> you want editable codes and statistics without a trial clock or a per-code allowance, plus batch runs, barcodes, and an API at no extra tier.</p>
  <p><b>Pick QR Code Generator if</b> you run campaigns inside Bitly's ecosystem, need team seats and white-labeling at the top tier, or want its 22 code types and hosted pages. Its paid tiers are the more corporate setup; FreeQrly is the simpler free-first one.</p>
  <p class="updated">Comparison checked October 30, 2026. Prices and limits change \u2014 check the pages linked above before you decide.</p>
'''),
dict(slug="qr-tiger-alternative", dtype="url",
  title="Best Free QR Tiger Alternative | FreeQrly",
  desc="Looking for a free QR Tiger alternative? FreeQrly gives you 20 free dynamic codes (currently unlimited) with unlimited scans, free static codes with no sign-up, batch mode, and a QR API.",
  kw="qr tiger alternative",
  h1='The free QR Tiger alternative, <span class="hl hl-mint">with unlimited scans</span>.',
  lede="If you are leaving QR Tiger because 3 free dynamic codes at 500 scans each run out too fast, FreeQrly \u2014 freeqrly.com is the straight swap: 20 free dynamic codes (currently unlimited during the limited-time offer) with unlimited scans, the same edit-after-printing and scan statistics, and free static codes with no sign-up.",
  steps=[("Bring your links","List the destinations behind your current codes \u2014 sale pages, menus, listings, profiles. One link per code."),
         ("Make the new codes","Use the studio below. Static codes are free with no sign-up; dynamic codes are free with a sign-in."),
         ("Reprint once for dynamic codes","Static codes you already printed keep working, because the destination lives inside the pattern. Dynamic codes live on the maker's server, so remake those at FreeQrly and reprint once.")],
  studio_h2="Make your free QR code",
  faq=[("Why do people look for a QR Tiger alternative?","Usually the free plan's limits: 3 dynamic codes, 500 scans each. A poster that takes off hits the ceiling, and the next step is a paid plan from $7 a month."),
       ("Do my printed QR Tiger codes stop working if I switch?","Static codes you already printed keep working wherever they were made, because the destination lives inside the pattern. Dynamic codes live on the maker's server, so those you remake at FreeQrly and reprint once."),
       ("How many free dynamic codes do I get?","20 with a free account, and currently unlimited for everyone during the limited-time offer. Codes you already made keep working when the offer ends."),
       ("What does FreeQrly Pro cost?","$9 per month or $90 per year for unlimited dynamic codes \u2014 against QR Tiger Regular at $7 per month for 12. If you need more than 12 editable codes, Pro is the cheaper per-code deal.")],
  compare='''
  <h2>FreeQrly vs QR Tiger at a glance</h2>
  <p>FreeQrly \u2014 freeqrly.com, compared with QR Tiger (qrcode-tiger.com). Figures below are from each product's own pricing and plan pages, checked October 30, 2026.</p>
  <table>
    <thead><tr><th>Feature</th><th>FreeQrly</th><th>QR Tiger</th></tr></thead>
    <tbody>
      <tr><td><b>Static codes</b></td><td>Free, unlimited, no sign-up, no watermark, never expire</td><td>Free, unlimited, never expire (free plan account required)</td></tr>
      <tr><td><b>Free dynamic codes</b></td><td>20 with a free account (currently unlimited during the limited-time offer)</td><td>3</td></tr>
      <tr><td><b>Scan cap on free dynamic codes</b></td><td>Unlimited</td><td>500 scans each</td></tr>
      <tr><td><b>Edit after printing (free)</b></td><td>Yes</td><td>Yes</td></tr>
      <tr><td><b>Scan statistics (free)</b></td><td>Yes</td><td>Yes, basic tracking</td></tr>
      <tr><td><b>Batch creation (free)</b></td><td>Yes, up to 50 per batch</td><td>No \u2014 bulk creation is an Advanced plan ($16/month) feature</td></tr>
      <tr><td><b>Barcode generator</b></td><td>Yes, included</td><td>Not listed on the plan pages we checked</td></tr>
      <tr><td><b>QR API</b></td><td>Yes (see <a href="/developers/">Developers</a>)</td><td>Regular ($7) and up: 500 requests per month</td></tr>
      <tr><td><b>Paid plan entry</b></td><td>Pro $9/month or $90/year, unlimited dynamic codes</td><td>Regular $7/month, 12 dynamic codes</td></tr>
    </tbody>
  </table>
  <p class="csrc">Sources: <a href="/pricing/">FreeQrly pricing</a>; <a href="https://www.qrcode-tiger.com/software-subscription">QR Tiger subscription plan page</a>.</p>
  <h2>Switch to FreeQrly if, stay with QR Tiger if</h2>
  <p><b>Switch to FreeQrly if</b> your codes keep hitting the 3-code or 500-scan ceiling, if you want batch creation, a barcode generator, or a QR API without paying, or if you want free static codes with no account at all. If you ever cancel Pro, your codes keep working.</p>
  <p><b>Stay with QR Tiger if</b> you need its campaign extras \u2014 saved design templates, retargeting, password protection, expiry controls, geofencing, and white-label domains on Premium \u2014 or its enterprise seats and integrations. For raw editable-code count, FreeQrly Pro is unlimited, so Tiger's edge is features and team tooling, not volume.</p>
  <p class="updated">Comparison checked October 30, 2026. Prices and limits change \u2014 check the pricing pages linked above before you decide.</p>
'''),
dict(slug="qr-code-monkey-alternative", dtype="url",
  title="Best QR Code Monkey Alternative with Dynamic Codes | FreeQrly",
  desc="QR Code Monkey is great for free static codes but has no editable codes or scan statistics. FreeQrly is the alternative that keeps static codes free and adds dynamic codes, statistics, batch mode, and a QR API.",
  kw="qr code monkey alternative",
  h1='The QR Code Monkey alternative, <span class="hl hl-honey">with dynamic codes</span>.',
  lede="Stay for the free static codes, switch for everything after printing. QR Code Monkey's free tool makes static codes only \u2014 no editing, no statistics. FreeQrly \u2014 freeqrly.com keeps static codes free with no sign-up and no watermark, and adds 20 free dynamic codes (currently unlimited) with editing and statistics, batch mode, a barcode generator, and a QR API.",
  steps=[("Bring your links","List what your current codes open \u2014 homepages, menus, profiles, posters. One link per code."),
         ("Make the new codes","Use the studio below. Static codes are free with no sign-up; dynamic codes are free with a sign-in."),
         ("Reprint only what must change","Static codes you already printed keep working, because the destination lives inside the pattern. Only remake the ones you need to edit or measure \u2014 as dynamic codes.")],
  studio_h2="Make your free QR code",
  faq=[("Why switch from QR Code Monkey at all?","Monkey's free tool is excellent for fixed codes. The switch is for everything after printing: editing a destination, seeing scan counts, making codes in batches, or generating barcodes \u2014 none of which the free tool does."),
       ("Do my printed Monkey codes stop working if I switch?","No. Static codes you already printed keep working forever, wherever they were made, because the destination lives inside the pattern. You only remake the codes you want to edit or measure."),
       ("Do I need an account?","Not for static codes \u2014 FreeQrly static codes need no sign-up, same as Monkey's generator. You sign in free only when you want dynamic codes, statistics, or a dashboard."),
       ("What does FreeQrly Pro cost?","$9 per month or $90 per year for unlimited dynamic codes. The free plan already covers 20 dynamic codes (currently unlimited during the offer), so most switchers never pay.")],
  compare='''
  <h2>FreeQrly vs QR Code Monkey at a glance</h2>
  <p>FreeQrly \u2014 freeqrly.com, compared with QR Code Monkey at qrcode-monkey.com. Figures below are from each product's own pages, checked October 30, 2026.</p>
  <table>
    <thead><tr><th>Feature</th><th>FreeQrly</th><th>QR Code Monkey</th></tr></thead>
    <tbody>
      <tr><td><b>Static codes</b></td><td>Free, unlimited, no sign-up, no watermark, never expire</td><td>Free, never expire, free for commercial use</td></tr>
      <tr><td><b>Edit after printing</b></td><td>Yes, free dynamic codes</td><td>No \u2014 static only; editing lives in the PRO upsell</td></tr>
      <tr><td><b>Scan statistics</b></td><td>Yes, free dynamic codes</td><td>No \u2014 statistics live in the PRO upsell</td></tr>
      <tr><td><b>Batch creation</b></td><td>Yes, up to 50 per batch, free</td><td>No \u2014 bulk generation is a Premium feature</td></tr>
      <tr><td><b>Barcode generator</b></td><td>Yes, included</td><td>Not listed on the free tool's pages we checked</td></tr>
      <tr><td><b>Vector downloads</b></td><td>PNG and SVG</td><td>PNG, SVG, PDF, and EPS \u2014 Monkey's strongest row</td></tr>
      <tr><td><b>Logo and design</b></td><td>Logo upload, colors, dot styles</td><td>Logo upload, colors, gradients, shapes, templates</td></tr>
      <tr><td><b>Where static codes are made</b></td><td>In your browser; nothing leaves your device</td><td>On Monkey's site; generated image files are cached 24 hours</td></tr>
      <tr><td><b>Paid option</b></td><td>Pro $9/month or $90/year, unlimited dynamic codes</td><td>PRO platform for dynamic codes and statistics (see our <a href="/freeqrly-vs-qr-code-generator/">QR Code Generator comparison</a>)</td></tr>
    </tbody>
  </table>
  <p class="csrc">Sources: <a href="/pricing/">FreeQrly pricing</a>; <a href="https://www.qrcode-monkey.com/">QR Code Monkey homepage</a>.</p>
  <h2>Switch to FreeQrly if, stay with QR Code Monkey if</h2>
  <p><b>Switch to FreeQrly if</b> you want anything beyond a fixed code: editing after printing, scan counts, batch runs, barcodes, or an API \u2014 while keeping static codes free with no account.</p>
  <p><b>Stay with QR Code Monkey if</b> you only ever need fixed codes and you care most about print design depth: EPS and PDF vectors, templates, gradients, and a 30% logo area. For that one job, it is the best free tool we checked \u2014 FreeQrly does not beat it on vector formats.</p>
  <p class="updated">Comparison checked October 30, 2026. Prices and limits change \u2014 check the pages linked above before you decide.</p>
'''),
]

EXTRA_CSS = '''
.lp-hero{grid-template-columns:1fr 1fr;align-items:start;margin-bottom:72px}
.steps{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:12px}
.steps li{display:flex;gap:14px;align-items:flex-start;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:15px 17px;font-size:14.5px;line-height:1.6;color:var(--soft)}
.steps .sn{flex-shrink:0;width:26px;height:26px;border-radius:50%;border:1px solid var(--gold);color:var(--gold);font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:1px}
.steps b{color:var(--ink);font-weight:600;display:block;margin-bottom:2px}
@media(max-width:960px){.lp-hero{grid-template-columns:1fr}}
.compare{max-width:860px;margin:0 auto 72px;padding:0 8px}
.compare h2{font-size:28px;line-height:1.25;margin:40px 0 12px}
.compare p{font-size:15.5px;line-height:1.7;color:var(--soft);margin:0 0 14px}
.compare table{width:100%;border-collapse:collapse;margin:16px 0 20px;font-size:14.5px;line-height:1.55}
.compare th,.compare td{border:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top}
.compare th{background:var(--card);color:var(--ink);font-weight:700}
.compare td:first-child{white-space:nowrap}
.compare .csrc,.compare .updated{font-size:13.5px;color:var(--soft)}
@media(max-width:640px){.compare td:first-child{white-space:normal}.compare table{font-size:13.5px}}
.lp-hero .glance{font-size:15px;line-height:1.7;color:var(--soft);margin:16px 0 0}
.lp-hero .glance b{color:var(--ink);font-weight:700}
.lp-hero .updated{font-size:13.5px;color:var(--soft);margin:6px 0 0}
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
        '<main class="studio" id="studio">\n    <div class="mascot m-peek" aria-hidden="true"><img loading="lazy" decoding="async" width="512" height="512" src="/assets/img/mascots/studio-qr.webp" alt="Qly presenting a QR code" data-studio-mascot data-mascot-default="studio-qr"></div>', 1)
    # studio assets live one level up
    studio = studio.replace('id="batchPanel"', 'id="batchPanel"')  # noop, keep ids
    steps_html = "\n".join(
        '      <li><span class="sn">%d</span><span><b>%s</b>%s</span></li>' % (i+1, t, d)
        for i, (t, d) in enumerate(p["steps"]))
    faq_html = "\n".join(
        '    <details><summary><span>%s</span></summary><p>%s</p></details>' % (q, a)
        for q, a in p["faq"])
    mode_attr = f' data-mode="{p["mode"]}"' if p.get("mode") else ""
    other = [x for x in PAGES if x["slug"] != p["slug"]]
    foot_links = ' · '.join('<a href="/%s/">%s</a>' % (x["slug"], x["kw"]) for x in other)
    # en_only pages ship English-only for now (no localized copies yet, so
    # they must NOT claim localized hreflang URLs that would 404). When
    # translations land, drop en_only and register the slug in
    # localize_pages.py LANDING + _LOCALIZABLE and extract-i18n.py LANDING.
    if p.get("en_only"):
        hl = f'<link rel="alternate" hreflang="en" href="{url}">\n<link rel="alternate" hreflang="x-default" href="{url}">'
        locale_alts = ""
    else:
        hl = "\n".join(
            [f'<link rel="alternate" hreflang="en" href="{url}">']
            + [f'<link rel="alternate" hreflang="{lg}" href="https://freeqrly.com/{lg}/{p["slug"]}/">' for lg in ("zh", "es", "hi", "ar", "pt", "fr", "ru", "de", "ja")]
            + [f'<link rel="alternate" hreflang="x-default" href="{url}">'])
        locale_alts = "\n".join(
            f'<meta property="og:locale:alternate" content="{lc}">' for lc in ("zh_CN", "es_ES", "hi_IN", "ar_AR", "pt_BR", "fr_FR", "ru_RU", "de_DE", "ja_JP"))
    compare_html = f'\n  <section class="compare" id="compare">\n{p["compare"]}\n  </section>\n' if p.get("compare") else ""
    # Non-comparison pages only: comparison pages already carry these
    # figures in their tables and their own checked dates.
    glance_html = "" if p.get("compare") else '\n      <p class="glance"><b>At a glance:</b> 20 free dynamic codes (currently unlimited during the limited-time promotion) · up to 50 codes per batch · 17 code types · Pro $9/mo or $90/yr · unlimited scans</p>\n      <p class="updated">Last updated: October 30, 2026</p>'
    datemod = '' if p.get("compare") else ',"dateModified":"2026-10-30"'
    return f'''<!DOCTYPE html>
<html lang="en" data-lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{url}">
{hl}
<meta name="theme-color" content="#e9eef4">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://freeqrly.com/og.png">
<meta property="og:locale" content="en_US">
{locale_alts}
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="../assets/img/favicon-scanner.png">
<link rel="apple-touch-icon" href="../assets/img/favicon-scanner.png">
<link rel="stylesheet" href="../assets/css/main.css?v=b3r-20261020">
<link rel="stylesheet" href="../assets/css/site-header.css?v=b3q-20261019">
<link rel="stylesheet" href="../assets/css/acct-menu.css?v=b3q-20261019">
<style>{EXTRA_CSS}</style>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebApplication","name":"FreeQrly — {p["kw"]}","applicationCategory":"UtilitiesApplication","operatingSystem":"Any","speakable":{{"@type":"SpeakableSpecification","cssSelector":["h1",".lede"]}},"offers":{{"@type":"Offer","price":"0"}},"url":"{url}","description":"{p["desc"]}"{datemod}}}
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
<body data-lp="{p["slug"]}" data-type="{p["dtype"]}"{mode_attr}>
<div class="wrap">
{HEADER}
  <section class="hero lp-hero">
    <div>
      <div class="kicker">Free · Static codes need no sign-up · No watermark</div>
      <h1>{p["h1"]}</h1>
      <p class="lede">{p["lede"]}</p>{glance_html}
    </div>
    <ol class="steps" id="how">
{steps_html}
    </ol>
  </section>
{studio}
{compare_html}
  <section class="faq" id="faq">
    <h2>Good to know</h2>
{faq_html}
  </section>

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
      <div class="fcol"><h4>Product</h4><a href="/">QR Generator</a><a href="/batch-qr-code/">Batch QR Codes</a><a href="/qr-code-with-logo/">QR Code with Logo</a><a href="/dynamic-qr-code/">Dynamic QR Codes</a><a href="/ticket-qr-code/">Ticket QR Codes</a><a href="/scan/">QR Scanner</a><a href="/barcode-generator/">Barcode Generator</a><a href="/pricing/">Pricing</a></div>
      <div class="fcol"><h4>Resources</h4><a href="/blog/">Blog</a><a href="/developers/">Developers · API &amp; MCP</a><a href="/blog/qr-code-print-size-guide/">Print Size Guide</a><a href="/#faq">FAQ</a></div>
      <div class="fcol"><h4>Company</h4><a href="/about/">About</a><a href="mailto:hello@freeqrly.com">Contact</a></div>
      <div class="fcol"><h4>Legal</h4><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Service</a></div>
    </div>
    <div class="fbottom"><span>© 2026 FreeQrly</span><a href="mailto:hello@freeqrly.com">hello@freeqrly.com</a></div>
  </footer>
</div>
<script src="../assets/lib/qr-code-styling.js"></script>
<script src="../assets/lib/jszip.min.js"></script>
<script src="/assets/js/vcard.js?v=b3r-20261020"></script>
<script src="../assets/js/app.js?v=b3r-20261020"></script>
</body>
</html>
'''

for p in PAGES:
    d = os.path.join(SITE, p["slug"])
    os.makedirs(d, exist_ok=True)
    html = build(p)
    open(os.path.join(d, "index.html"), "w").write(html)
    print("wrote", p["slug"], len(html), "bytes")
