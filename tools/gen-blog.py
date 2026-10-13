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
  title="Static vs Dynamic QR Codes: Which Should You Choose? — FreeQrly",
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

def faq_json(faq):
    return ",\n    ".join(
        '{\n      "@type": "Question",\n      "name": "%s",\n      "acceptedAnswer": {\n        "@type": "Answer",\n        "text": "%s"\n      }\n    }' % (q.replace('"', '\\"'), a.replace('"', '\\"'))
        for q, a in faq)

def build(p):
    url = f"https://freeqrly.com/blog/{p['slug']}/"
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
</head>
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
    <section class="faq" id="faq" style="margin-top:50px">
      <h2>Good to know</h2>
{faq_html}
    </section>
  </article>
  <footer>
    <div class="fin"><a href="/" style="color:inherit">FreeQrly</a> — made quietly, in your browser.</div>
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
    html = build(p)
    open(os.path.join(d, "index.html"), "w").write(html)
    print("wrote blog/" + p["slug"], len(html), "bytes")
