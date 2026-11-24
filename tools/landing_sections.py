# -*- coding: utf-8 -*-
"""落地页正文补充章节（由 tests/md2sections.py 从 drafts/*.md 生成）。

改文案请改 drafts/*.md 后重新生成，不要直接编辑本文件。
"""

SECTIONS = {
    "pdf-qr-code": [
        ('Where to put the PDF',
         """<p>A QR code holds a link, not a file. The code you print points at wherever your PDF already lives, so the first decision is where to host it. Three options cover almost every case.</p>
<div class="tblwrap"><table>
  <thead><tr><th>Where it lives</th><th>What the link looks like</th><th>Free tier</th><th>Breaks if you...</th></tr></thead>
  <tbody>
    <tr><td>Google Drive</td><td><code>drive.google.com/file/d/…/view</code></td><td>15 GB</td><td>move the file, delete it, or change who can see it</td></tr>
    <tr><td>Dropbox</td><td><code>dropbox.com/s/…/menu.pdf</code></td><td>2 GB</td><td>delete or rename the file</td></tr>
    <tr><td>Your own site</td><td><code>yoursite.com/menu.pdf</code></td><td>depends on host</td><td>remove the file</td></tr>
  </tbody>
</table></div>
<p>Whichever you pick, set sharing to "anyone with the link". A PDF shared with specific people asks every scanner to sign in, and most of them won't.</p>"""),
        ('Why a Drive link sometimes shows a warning',
         """<p>Two things trip people up, and neither is a problem with the code.</p>
<p>The first is file size. Google scans Drive downloads for viruses, and it skips that scan above 100 MB. Instead of a download you get a page that says Google couldn't scan the file, with a button to continue anyway. The PDF still opens, but it looks suspicious on a restaurant table. Keep menus and brochures under 100 MB and the warning never appears.</p>
<p>The second is permission. If the file is still private, the scanner lands on a Google sign-in page. Open the file's sharing settings and switch to "anyone with the link can view".</p>
<p>If neither fix is practical — a 300 MB portfolio, or a client who insists on a private folder — host the PDF on your own domain. You control the permissions, and there's no interstitial.</p>"""),
        ('How big to print it',
         """<p>A code that scans on your monitor can fail on a wall. The practical rule: the printed code should be roughly one tenth of the distance you expect people to scan from. Stand 3 metres away, print a 30 cm code.</p>
<div class="tblwrap"><table>
  <thead><tr><th>Where it goes</th><th>Typical scan distance</th><th>Smallest that works</th><th>Comfortable</th></tr></thead>
  <tbody>
    <tr><td>Counter card, table tent</td><td>30 cm</td><td>3 cm</td><td>4–5 cm</td></tr>
    <tr><td>A4 poster in a window</td><td>1–2 m</td><td>10 cm</td><td>15 cm</td></tr>
    <tr><td>Door sign, trade show panel</td><td>3 m</td><td>30 cm</td><td>40 cm</td></tr>
    <tr><td>Product packaging</td><td>15–25 cm</td><td>2 cm</td><td>3 cm</td></tr>
  </tbody>
</table></div>
<p>Leave a margin. The blank border around the pattern — the quiet zone — is part of how scanners find the code. Cropping it to save space is the most common reason a printed code stops working.</p>"""),
        ('When you update the PDF',
         """<p>The code points at a link. Whether you can change the PDF without reprinting depends entirely on whether the link stays the same.</p>
<p>If you replace the file in place, the link survives. In Drive, open the existing file and upload a new version rather than creating a new one; in Dropbox, overwrite the file at the same path. The URL doesn't move, so every printed code still works.</p>
<p>If you upload a new file, you get a new link. The old code now opens a deleted file or a 404. You'll need to print again — which is worth knowing before you order 500 table tents.</p>
<p>One more case: if the PDF lives on your own domain and you keep the filename, swapping the file behind it is invisible to scanners. That's the most forgiving setup, and the one we'd pick for anything printed in volume.</p>"""),
        ('Test it before you print',
         """<p>Scan the code off your screen with two different phones — one iPhone, one Android — before anything goes to a printer. Screen and paper fail in different ways: glare, ink spread, and the loss of the quiet zone only show up on the printed version.</p>
<p>Then scan the printed proof from the distance you expect. If it takes more than a second to lock on, the code is too small for that spot, not badly made.</p>"""),
    ],
    "tiktok-qr-code": [
        ('Which TikTok link to use',
         """<p>TikTok gives you three kinds of URL, and they behave differently once printed.</p>
<div class="tblwrap"><table>
  <thead><tr><th>Link type</th><th>Looks like</th><th>A scan opens</th><th>Survives a deleted video?</th></tr></thead>
  <tbody>
    <tr><td>Profile</td><td><code>tiktok.com/@yourhandle</code></td><td>your profile, follow button at top</td><td>yes</td></tr>
    <tr><td>Single video</td><td><code>tiktok.com/@yourhandle/video/7312…</code></td><td>that video, playing</td><td>no</td></tr>
    <tr><td>Hashtag</td><td><code>tiktok.com/tag/yourcampaign</code></td><td>every video on the tag</td><td>yes, but shows other people's posts</td></tr>
  </tbody>
</table></div>
<p>For a business card, shop window, or packaging insert, use the profile link. It keeps working as you post, and the follow button sits one tap from the landing screen.</p>
<p>Use a video link when the code has exactly one job: a launch poster, or a sticker on the product that points at the ad. The link pins one video ID. Delete that video and the code goes dead.</p>
<p>Hashtag links work, but they show everyone's posts on the tag, not just yours. Good for a campaign landing page, wrong for a business card.</p>"""),
        ('What happens when someone scans it',
         """<div class="tblwrap"><table>
  <thead><tr><th>Scanner</th><th>TikTok installed</th><th>TikTok not installed</th></tr></thead>
  <tbody>
    <tr><td>iPhone Camera app</td><td>link opens, prompt to switch to the app</td><td>mobile web profile loads</td></tr>
    <tr><td>Android camera</td><td>same, app handoff usually automatic</td><td>mobile web profile loads</td></tr>
    <tr><td>TikTok's own scanner</td><td>opens in app</td><td>prompts to install</td></tr>
  </tbody>
</table></div>
<p>The handoff is a prompt, not a guarantee. Some phones show a full-screen "Open in TikTok?" banner, others show a slim bar at the top, and a few open the mobile site with no prompt at all. People tap through most of the time, but some don't, and you should assume a slice of scans land on the web version.</p>
<p>Two consequences worth planning for. A scan is not a follow: the person still has to tap Follow after landing, so the code gets them to the door, not through it. And the mobile web version loads slower than the app, which matters if the code is on packaging where attention is already thin.</p>
<p>A private account shows scanners the profile shell and a request button. No QR code can get around that setting.</p>"""),
        ("TikTok's own QR code, and when to use it instead",
         """<p>The app has a QR code built in: open your profile, tap the share icon, choose QR code. Free, and it works — inside TikTok.</p>
<p>The catch is who can read it. That code is meant for TikTok's own scanner. Scan it with an iPhone Camera app or a stock Android camera and you often get nothing at all, or a nudge to install TikTok first. On a phone screen, where the person already has the app open, that's fine. On a printed sticker, a shop window, or a menu, the scanner is a stranger holding a default camera app.</p>
<p>The code you make here is a standard QR code. Any camera reads it, and the link inside behaves the same as a typed URL. That's the entire difference, and it's the reason a printed code is worth generating separately from the in-app one.</p>
<p>One thing to watch: your handle is part of the URL. Rename the account and both codes break. Generate a fresh one after a rename, and replace anything already printed.</p>"""),
        ('Where to put it',
         """<div class="tblwrap"><table>
  <thead><tr><th>Placement</th><th>Code size</th><th>Why</th></tr></thead>
  <tbody>
    <tr><td>Shipping insert, box sticker</td><td>2 cm</td><td>read at arm's length, often on a curved surface</td></tr>
    <tr><td>Merch swing tag</td><td>1.5–2 cm</td><td>smaller gets smudged by fabric texture</td></tr>
    <tr><td>Counter card</td><td>4–5 cm</td><td>scanned from about 30 cm</td></tr>
    <tr><td>Shop window</td><td>15 cm</td><td>scanned from 1–2 m, often through glass</td></tr>
    <tr><td>Event poster</td><td>20–30 cm</td><td>scanned from 2–3 m while walking</td></tr>
    <tr><td>Business card</td><td>1.5 cm</td><td>the practical floor for matte stock</td></tr>
  </tbody>
</table></div>
<p>Keep the quiet zone. The blank margin around the pattern is how cameras find the code in the first place, and cropping it to fit a design is the single most common reason a printed code fails.</p>
<p>Test the proof with a phone before the print run. A code that reads on screen can fail on a curved bottle or a glossy label, and you find out after the boxes arrive.</p>"""),
        ('What this code cannot do',
         """<div class="tblwrap"><table>
  <thead><tr><th>Limit</th><th>Why</th><th>Workaround</th></tr></thead>
  <tbody>
    <tr><td>No scan counting</td><td>static code, nothing phones home</td><td>TikTok profile analytics (free)</td></tr>
    <tr><td>No redirect after printing</td><td>the URL is baked into the pattern</td><td>make a new code, reprint</td></tr>
    <tr><td>No private-account bypass</td><td>TikTok enforces the setting</td><td>switch the account to public</td></tr>
    <tr><td>No deep link to a tab</td><td>only profile, video and hashtag URLs exist</td><td>link the profile</td></tr>
  </tbody>
</table></div>
<p>The first two are the ones people ask about. If you need to change the destination later without reprinting, that's a dynamic code, not this one.</p>"""),
    ],
    "app-store-qr-code": [
        ('One static code holds one link',
         """<p>This is the part most app-store QR pages skip, so here it is plainly: a QR code stores text, and that text is a URL. One code, one destination. There is no logic inside the pattern that can look at the phone and pick a store.</p>
<p>That matters because your iOS and Android listings are two different URLs. A single static code can only point at one of them. If you encode the App Store link, Android users land on a page for an app they can't install, and the reverse is just as bad.</p>
<p>You have three ways to cover both platforms. The table below compares them.</p>
<div class="tblwrap"><table>
  <thead><tr><th>Approach</th><th>How it works</th><th>Printed codes</th><th>Works if a link changes</th><th>Setup</th></tr></thead>
  <tbody>
    <tr><td>Two codes, side by side</td><td>one App Store, one Play</td><td>2</td><td>no, reprint</td><td>none</td></tr>
    <tr><td>One code to a router page</td><td>page reads the device, forwards to the right store</td><td>1</td><td>yes, if the page is dynamic</td><td>a page you control</td></tr>
    <tr><td>Store smart banner</td><td>Apple and Google banners on your own site</td><td>1 (to your site)</td><td>yes</td><td>a website</td></tr>
  </tbody>
</table></div>
<p>Two codes is the honest, zero-effort option. Router page is what most apps do once they have a marketing site. Smart banners only work if people land on your site first, which is a different job from a printed code.</p>"""),
        ('How to get your store links',
         """<p>Both stores give you a clean, permanent URL, and both are easy to find once you know where to look.</p>
<p>For iOS, open your app in App Store Connect, go to App Information, and copy the App Store URL. It looks like <code>apps.apple.com/app/id1234567890</code>. You can add a country segment — <code>apps.apple.com/gb/app/id…</code> — if you want the code to open a specific storefront, but the plain version redirects to the visitor's own region, which is usually what you want.</p>
<p>For Android, open the Play Console listing and copy the link from the browser bar. It looks like <code>play.google.com/store/apps/details?id=com.yourcompany.yourapp</code>. The <code>id</code> is your package name, and it never changes even when the app name does.</p>
<p>Drop anything after the ID. Marketing tools often append tracking parameters like <code>?mt=8</code> or <code>&amp;referrer=…</code>. They're harmless, but they make the QR pattern denser for no benefit, and a denser pattern is harder to print small.</p>"""),
        ('Building a router page that works',
         """<p>If you go with one code, it needs somewhere to send people. A router page is a small page on your own domain that reads the user agent and forwards.</p>
<p>The logic is short: if the browser reports an iPhone or iPad, go to the App Store; if it reports Android, go to Play; otherwise show both buttons. Keep a fallback for desktop, because a meaningful share of scans come from people testing on a laptop.</p>
<p>Two things break these pages in practice. Apple's in-app browsers and some social apps strip the user agent down to something generic, so the detection guesses wrong. And a redirect that fires before the page renders can look like a broken link. Showing both buttons with the detected one highlighted is more forgiving than an instant forward.</p>
<p>If you want the destination editable later, use a dynamic code pointing at the router page. Change the page and every printed code follows, no reprint.</p>"""),
        ('Where to print it',
         """<div class="tblwrap"><table>
  <thead><tr><th>Placement</th><th>Size</th><th>Note</th></tr></thead>
  <tbody>
    <tr><td>App launch slide</td><td>8 cm</td><td>scanned from a seat, 1–2 m away</td></tr>
    <tr><td>Packaging and inserts</td><td>2 cm</td><td>one code per platform, clearly labelled</td></tr>
    <tr><td>Receipt footer</td><td>1.5 cm</td><td>thermal printers blur thin lines; test first</td></tr>
    <tr><td>Poster or ad</td><td>15 cm</td><td>scanned from 2–3 m</td></tr>
    <tr><td>Business card</td><td>1.5 cm</td><td>only if you print two codes with labels</td></tr>
  </tbody>
</table></div>
<p>When you print two codes, label them. A pair of identical-looking squares with no "iPhone" and "Android" text is worse than one code, because people scan the wrong one and land on a store they can't use.</p>"""),
    ],
}
