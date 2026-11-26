# zh


## landing-app-store-qr-code

EN: App Store QR Code Generator: One Code Per Store | FreeQrly
→  App Store 二维码生成器：一码一店 | FreeQrly

EN: Make a QR code for your App Store or Google Play link. A static code holds one URL, so iOS and Android are two codes — here is how to print the right one.
→  为 App Store 或 Google Play 链接免费生成二维码。静态码只装一个 URL，iOS 和安卓各做一个码，扫码才落到对的商店。

EN: Your app link, <span class="hl hl-honey">printed right</span>.
→  你的 App 链接，<span class="hl hl-honey">印得刚刚好</span>。

EN: A static QR code stores one URL, so your App Store listing and your Play listing need one code each. Fill in a link, print it at a size that scans, and put the right code in front of the right phone.
→  一个静态二维码只装一个 URL，所以 App Store 上架页和 Play 上架页各需要一个码。填入链接，按扫得动的尺寸打印，再把对的码放到对的手机面前。

EN: <span class="sn">1</span><span><b>Copy one store link</b>App Store from App Store Connect, Play from the Play Console. One link per code — fill the App Store field for iOS, the Google Play field for Android.</span>
→  <span class="sn">1</span><span><b>复制一个商店链接</b>App Store 的从 App Store Connect 拿，Play 的从 Play Console 拿。一个码配一个链接——iOS 填 App Store 那一栏，安卓填 Google Play 那一栏。</span>

EN: <span class="sn">2</span><span><b>Paste it in</b>Your code appears instantly. Leave the other field empty unless you are making a second code.</span>
→  <span class="sn">2</span><span><b>粘贴进去</b>二维码立刻出现。除非你要做第二个码，否则另一栏留空。</span>

EN: <span class="sn">3</span><span><b>Label it and print</b>“iPhone” or “Android” next to the code, at 2 cm or larger. Ads, packaging, receipts, launch slides.</span>
→  <span class="sn">3</span><span><b>标注并打印</b>在码旁边写上“iPhone”或“安卓”，尺寸 2 厘米以上。广告、包装、小票、发布会幻灯片都能用。</span>

EN: One static code holds one link
→  一个静态码只装一个链接

EN: This is the part most app-store QR pages skip, so here it is plainly: a QR code stores text, and that text is a URL. One code, one destination. There is no logic inside the pattern that can look at the phone and pick a store.
→  这一点大多数应用商店的二维码页面都跳过，所以我们直说：二维码存的是文本，而这段文本是一个 URL。一个码，一个目的地。图案里没有逻辑，没法看手机型号再挑商店。

EN: That matters because your iOS and Android listings are two different URLs. A single static code can only point at one of them. If you encode the App Store link, Android users land on a page for an app they can't install, and the reverse is just as bad.
→  你的 iOS 和安卓上架页是两个不同的 URL。一个静态码只能指向其中一个。把 App Store 链接写进码里，安卓用户就会落到一个他们装不了的页面；反过来一样糟。

EN: You have three ways to cover both platforms. The table below compares them.
→  覆盖双平台有三种做法，下表做个对比。

EN: Approach
→  方案

EN: Printed codes
→  要印几个码

EN: Works if a link changes
→  链接变了还能用吗

EN: Setup
→  需要准备

EN: Two codes, side by side
→  两个码并排

EN: one App Store, one Play
→  一个 App Store，一个 Play

EN: no, reprint
→  不能，要重印

EN: none
→  无需

EN: One code to a router page
→  一个码指向路由页

EN: page reads the device, forwards to the right store
→  页面识别设备，跳转到对应商店

EN: yes, if the page is dynamic
→  可以，前提是页面是动态的

EN: a page you control
→  一个你自己控制的页面

EN: Store smart banner
→  商店的 Smart Banner

EN: Apple and Google banners on your own site
→  在你自己的网站上放 Apple 和 Google 的横幅

EN: 1 (to your site)
→  1 个（指向你的网站）

EN: a website
→  一个网站

EN: Two codes is the honest, zero-effort option. Router page is what most apps do once they have a marketing site. Smart banners only work if people land on your site first, which is a different job from a printed code.
→  两个码是最实在、也最省事的做法。路由页是大多数 App 有了营销站之后的常见方案。Smart Banner 只对先落到你网站的人才有效，那和印出来的码是两件事。

EN: How to get your store links
→  怎么拿到商店链接

EN: Both stores give you a clean, permanent URL, and both are easy to find once you know where to look.
→  两个商店都会给你一个干净、永久的 URL，知道去哪找就很容易。

EN: For iOS, open your app in App Store Connect, go to App Information, and copy the App Store URL. It looks like <code>apps.apple.com/app/id1234567890</code>. You can add a country segment — <code>apps.apple.com/gb/app/id…</code> — if you want the code to open a specific storefront, but the plain version redirects to the visitor's own region, which is usually what you want.
→  iOS：在 App Store Connect 打开你的 App，进“App 信息”，复制 App Store URL。它长这样 <code>apps.apple.com/app/id1234567890</code>。你可以加国家代码——<code>apps.apple.com/gb/app/id…</code>——让码打开指定地区的商店；但默认版本会按访客所在地区跳转，通常这才是你要的。

EN: For Android, open the Play Console listing and copy the link from the browser bar. It looks like <code>play.google.com/store/apps/details?id=com.yourcompany.yourapp</code>. The <code>id</code> is your package name, and it never changes even when the app name does.
→  安卓：在 Play Console 打开商品页，从地址栏复制链接。它长这样 <code>play.google.com/store/apps/details?id=com.yourcompany.yourapp</code>。<code>id</code> 是你的包名，即使 App 改名也不会变。

EN: Drop anything after the ID. Marketing tools often append tracking parameters like <code>?mt=8</code> or <code>&referrer=…</code>. They're harmless, but they make the QR pattern denser for no benefit, and a denser pattern is harder to print small.
→  ID 之后的东西都删掉。营销工具常会加跟踪参数，比如 <code>?mt=8</code> 或 <code>&referrer=…</code>。它们没有害处，但会让二维码图案变密，一点好处都没有——而图案越密，小尺寸越难印清楚。

EN: Building a router page that works
→  做一个能用的路由页

EN: If you go with one code, it needs somewhere to send people. A router page is a small page on your own domain that reads the user agent and forwards.
→  选一个码的话，它得有个去处。路由页是你自己域名下的一张小页面，读 User-Agent 然后跳转。

EN: The logic is short: if the browser reports an iPhone or iPad, go to the App Store; if it reports Android, go to Play; otherwise show both buttons. Keep a fallback for desktop, because a meaningful share of scans come from people testing on a laptop.
→  逻辑很简单：浏览器报 iPhone 或 iPad，去 App Store；报安卓，去 Play；其余情况两个按钮都显示。给桌面端留个兜底，因为相当一部分扫码来自在电脑上测试的人。

EN: Two things break these pages in practice. Apple's in-app browsers and some social apps strip the user agent down to something generic, so the detection guesses wrong. And a redirect that fires before the page renders can look like a broken link. Showing both buttons with the detected one highlighted is more forgiving than an instant forward.
→  实际使用中有两种东西会让这类页面失灵。Apple 的应用内浏览器和部分社交 App 会把 User-Agent 削成通用值，识别就猜错了。另外，在页面渲染完成前就触发的跳转，看起来像坏链接。两个按钮都显示、把识别到的那个高亮，比直接跳转更友好。

EN: If you want the destination editable later, use a dynamic code pointing at the router page. Change the page and every printed code follows, no reprint.
→  如果想让目标以后可改，就用动态码指向路由页。改页面，所有印出去的码跟着变，不用重印。

EN: App launch slide
→  发布会幻灯片

EN: 8 cm
→  8 厘米

EN: scanned from a seat, 1–2 m away
→  座位上扫，1–2 米

EN: Packaging and inserts
→  包装与内附卡片

EN: one code per platform, clearly labelled
→  每平台一个码，标注清楚

EN: Receipt footer
→  小票底部

EN: thermal printers blur thin lines; test first
→  热敏打印机会糊掉细线，先打样测试

EN: Poster or ad
→  海报或广告

EN: scanned from 2–3 m
→  2–3 米外扫

EN: only if you print two codes with labels
→  仅在印两个带标注的码时使用

EN: When you print two codes, label them. A pair of identical-looking squares with no "iPhone" and "Android" text is worse than one code, because people scan the wrong one and land on a store they can't use.
→  印两个码的时候要标注清楚。两个长得一模一样、没有“iPhone”和“安卓”字样的方块，比一个码还糟——人们会扫错，然后落到一个用不了的商店。

EN: <span>Can one static code open both stores?</span>
→  <span>一个静态码能同时打开两个商店吗？</span>

EN: No. A static code stores a single URL, and your two store listings are two URLs. Encode the App Store link and Android visitors land on an app they cannot install. Print two labelled codes, or point one code at a page on your own domain that reads the phone and forwards to the right store.
→  不能。一个静态码只存一个 URL，而你的两个上架页就是两个 URL。写了 App Store 链接，安卓用户就会落到一个装不了的页面。要么印两个带标注的码，要么让一个码指向你自己域名下的一页，由它识别手机型号再转到对应的商店。

EN: <span>What if I fill in both fields?</span>
→  <span>两栏都填会怎样？</span>

EN: Only the App Store link is encoded — the Play field is used when the App Store field is empty. To cover both platforms, make two codes, one per field.
→  只会编码 App Store 链接——Play 那一栏只在 App Store 栏为空时才会用到。要覆盖两个平台，就做两个码，一栏一个。

EN: <span>What if I only have one platform?</span>
→  <span>只有一个平台怎么办？</span>

EN: Fill that field and print one code. Nothing else is needed.
→  填那一栏，印一个码就够了，别的都不用。

EN: <span>Can it detect the phone and route automatically?</span>
→  <span>能自动识别手机并跳转吗？</span>

EN: Not on its own — a printed pattern cannot run logic. Device detection needs a page in between: host a small router page, then point a dynamic code at it so you can change the destination later without reprinting.
→  单靠它不行——印在纸上的图案没法执行逻辑。要识别设备，中间得加一个页面：自己托管一个小的路由页，再用动态码指向它，这样以后改目标也不用重印。

EN: <span>Does it track installs?</span>
→  <span>能统计安装量吗？</span>

EN: No. Static codes carry only the link and never phone home. App Store Connect and the Play Console already report installs.
→  不会。静态码只带着链接，从不回传数据。安装量在 App Store Connect 和 Play Console 里本来就有。

EN: FreeQrly — app store qr code generator
→  FreeQrly —— 应用商店二维码生成器

EN: Can one static code open both stores?
→  一个静态码能同时打开两个商店吗？

EN: What if I fill in both fields?
→  两栏都填会怎样？

EN: What if I only have one platform?
→  只有一个平台怎么办？

EN: Can it detect the phone and route automatically?
→  能自动识别手机并跳转吗？

EN: Does it track installs?
→  能统计安装量吗？

EN: Make your app store QR code
→  生成你的应用商店二维码

EN: Copy one store link
→  复制一个商店链接

EN: App Store from App Store Connect, Play from the Play Console. One link per code — fill the App Store field for iOS, the Google Play field for Android.
→  App Store 的从 App Store Connect 拿，Play 的从 Play Console 拿。一个码配一个链接——iOS 填 App Store 那一栏，安卓填 Google Play 那一栏。

EN: Paste it in
→  粘贴进去

EN: Your code appears instantly. Leave the other field empty unless you are making a second code.
→  二维码立刻出现。除非你要做第二个码，否则另一栏留空。

EN: Label it and print
→  标注并打印

EN: “iPhone” or “Android” next to the code, at 2 cm or larger. Ads, packaging, receipts, launch slides.
→  在码旁边写上“iPhone”或“安卓”，尺寸 2 厘米以上。广告、包装、小票、发布会幻灯片都能用。


## about

EN: About FreeQrly — Free Static QR Codes, No Sign-Up, No Expiry
→  关于 FreeQrly — 免费静态二维码，免注册、不过期

EN: FreeQrly is a free QR code generator: static codes run 100% in your browser — no sign-up, no tracking, no expiry. Learn what it is and how it works.
→  FreeQrly 是免费二维码生成器：静态码在你的浏览器里运行，免注册、不追踪、不过期、无水印。了解它怎么工作、哪些功能免费。

EN: About FreeQrly
→  关于 FreeQrly

EN: A free QR code generator: static codes run 100% in your browser — no sign-up, no tracking, no expiry.
→  免费二维码生成器：静态码 100% 在你的浏览器里运行——免注册、不追踪、不过期。

EN: Qly protecting your privacy with a shield
→  Qly 举着盾牌保护你的隐私

EN: About
→  关于

EN: What is <span class="hl hl-mint">FreeQrly</span>?
→  <span class="hl hl-mint">FreeQrly</span> 是什么？

EN: FreeQrly is a free QR code generator with a simple idea: the tool should live in your browser, not on somebody's server. You type, it draws — nothing is uploaded, tracked, or billed.
→  FreeQrly 是免费二维码生成器，想法很简单：工具应该住在你的浏览器里，而不是别人的服务器上。你输入，它画出来——不上传、不追踪、不收费。

EN: <b>100% browser-based</b><span>Every code is drawn locally with JavaScript. Your links, contacts, and WiFi passwords never leave your device.</span>
→  <b>100% 浏览器端生成</b><span>每个码都用 JavaScript 在本地绘制。你的链接、联系方式和 WiFi 密码永远不会离开你的设备。</span>

EN: <b>Codes that never expire</b><span>Static codes live in the pattern itself; dynamic codes stay editable after printing. No trials, no deactivated codes — what you print today scans in ten years.</span>
→  <b>永不过期的码</b><span>静态码的内容就写在图案里；动态码印完之后依然可以改。没有试用期，没有被停用的码——今天印的，十年后照样能扫。</span>

EN: <b>Free to start</b><span>Static codes need no account at all. Dynamic codes — editable, with scan stats — need a free sign-in. No watermark either way.</span>
→  <b>免费开始</b><span>静态码完全不需要账号。动态码可以修改、带扫码统计，需要免费登录。两种都没有水印。</span>

EN: <b>10 languages</b><span>English, Chinese, Spanish, Hindi, Arabic (RTL), Portuguese, French, Russian, German, Japanese.</span>
→  <b>10 种语言</b><span>英语、中文、西班牙语、印地语、阿拉伯语（RTL）、葡萄牙语、法语、俄语、德语、日语。</span>

EN: <b>Built for print</b><span>High-resolution export and vector SVG, quiet zones respected — made for business cards, menus, and posters.</span>
→  <b>打印友好</b><span>高分辨率导出和矢量 SVG，留足静区——为名片、菜单和海报而做。</span>

EN: <b>Agent-friendly</b><span>A free <a href="/developers/">API and MCP server</a> so AI assistants can generate codes too.</span>
→  <b>智能体友好</b><span>免费的 <a href="/developers/">API 和 MCP 服务器</a>，AI 助手也能生成二维码。</span>

EN: Questions, answered
→  问题，都有答案

EN: Almost everything is free. Static codes are completely free, with no watermarks — they are made entirely in your browser and need no account. Dynamic codes need a free sign-in so they can be edited later, and 20 are included free; if you need more, an optional Pro subscription (US$9/month or US$90/year) makes dynamic codes unlimited.
→  几乎全部免费。静态码完全免费、没有水印——它们完全在你的浏览器里生成，不需要账号。动态码需要免费登录，以便之后编辑，免费包含 20 个；如果需要更多，可选的 Pro 订阅（每月 9 美元或每年 90 美元）可让动态码不限量。

EN: Do the QR codes expire?
→  二维码会过期吗？

EN: No — neither kind. A static code's destination lives inside the pattern itself, and dynamic codes stay live and editable for as long as your account exists. Details: <a href="/blog/do-qr-codes-expire/">do QR codes expire?</a>
→  不会——两种都不会。静态码的目标链接就写在图案里，动态码只要你的账号还在，就一直有效、随时可改。详情：<a href="/blog/do-qr-codes-expire/">二维码会过期吗？</a>

EN: Can I use it for my business?
→  能商用吗？

EN: Yes — commercial use is free. Restaurants use it for <a href="/blog/qr-codes-for-restaurants/">menus and reviews</a>, shops for <a href="/google-review-qr-code/">review codes</a> and <a href="/wifi-qr-code/">WiFi codes</a>.
→  能——商用免费。餐厅用它做<a href="/blog/qr-codes-for-restaurants/">菜单和评价</a>，商店用它做<a href="/google-review-qr-code/">评价码</a>和 <a href="/wifi-qr-code/">WiFi 码</a>。

EN: Who is behind FreeQrly?
→  FreeQrly 背后是谁？

EN: An independent maker who got tired of "free" generators that hold your codes hostage behind a trial. The mascot is Qly, a small elephant who appears across the site.
→  一个独立开发者，受够了那些把二维码扣在试用期后面的“免费”生成器。吉祥物是 Qly，一头小象，出现在全站各处。

EN: Try the generator →
→  试试生成器 →

EN: FreeQrly is a free QR code generator that runs entirely in the browser. No sign-up, no tracking, no expiry — static QR codes with optional logos, in 10 languages.
→  FreeQrly 是免费二维码生成器，完全在浏览器里运行。免注册、不追踪、不过期——支持可选 Logo 的静态二维码，覆盖 10 种语言。

EN: What is FreeQrly?
→  FreeQrly 是什么？

EN: FreeQrly is a free online QR code generator. It creates static QR codes for links, text, WiFi, vCards, SMS, calls, and locations — entirely in your browser, with no account and no fees.
→  FreeQrly 是免费在线二维码生成器，可为链接、文本、WiFi、vCard、短信、电话和位置生成静态二维码——完全在你的浏览器里完成，不需要账号，也不收费。

EN: Yes — almost everything. Static codes are free with no trial and no watermarks, including logo upload, batch generation, and high-resolution export. Static codes need no account; dynamic codes need a free sign-in and include 20 free, with an optional Pro subscription for unlimited dynamic codes.
→  是的——几乎所有功能都免费。静态码免费、无试用、无水印，包括 Logo 上传、批量生成和高分辨率导出。静态码不需要账号；动态码需要免费登录，包含 20 个免费额度，并有可选的 Pro 订阅提供不限量动态码。

EN: Do FreeQrly QR codes expire?
→  FreeQrly 的二维码会过期吗？

EN: No. Static codes encode the destination directly in the pattern, and dynamic codes stay live and editable — neither kind expires or requires a subscription.
→  不会。静态码把目标链接直接编进图案里，动态码一直有效、随时可改——两种都不会过期，也不需要订阅。

EN: Does FreeQrly track my QR codes or my data?
→  FreeQrly 会追踪我的二维码或数据吗？

EN: Static codes are generated locally in your browser; their content is never uploaded and they have no scan tracking. Dynamic codes count scans — that is what they are for — and their destinations can be changed anytime.
→  静态码在你的浏览器本地生成，内容从不上传，也没有扫码追踪。动态码会统计扫码次数——本来就是干这个的——目标链接随时可以修改。

EN: What languages does FreeQrly support?
→  FreeQrly 支持哪些语言？

EN: Ten: English, Chinese, Spanish, Hindi, Arabic (with right-to-left layout), Portuguese, French, Russian, German, and Japanese.
→  十种：英语、中文、西班牙语、印地语、阿拉伯语（从右到左排版）、葡萄牙语、法语、俄语、德语和日语。


## landing-ticket-qr-code

EN: Free Ticket QR Code Generator | FreeQrly
→  免费门票二维码生成器 | FreeQrly

EN: Create free QR codes for tickets: link to your ticket or check-in page, print one code per ticket with Batch mode, no sign-up for static codes, never expires.
→  免费做门票二维码：链接到购票页或签到页，批量模式一票一码，静态码免注册、永不过期，演唱会、会议、校园活动都能用。

EN: One scan at the door, <span class="hl hl-mint">no ticket queue</span>.
→  门口扫一下，<span class="hl hl-mint">不用排队验票</span>。

EN: Put a QR code on every ticket, poster, and confirmation email. Guests scan at the entrance and land straight on your ticket or check-in page — concerts, conferences, workshops, school events.
→  把二维码印在每张门票、海报和确认邮件上。观众到门口一扫，直接进入购票页或签到页——演唱会、会议、工作坊、校园活动都适用。

EN: <span class="sn">1</span><span><b>Link to your ticket page</b>Your ticketing page, check-in form, or event details — one code, one destination.</span>
→  <span class="sn">1</span><span><b>链接到门票页面</b>购票页、签到表单或活动详情页——一个码，一个去处。</span>

EN: <span class="sn">2</span><span><b>Make the code</b>Paste the link in the studio below. Print-ready PNG or SVG, free, no watermark, no sign-up for static codes.</span>
→  <span class="sn">2</span><span><b>生成二维码</b>把链接粘贴到下方工作室。可直接印刷的 PNG 或 SVG，免费、无水印，静态码免注册。</span>

EN: <span class="sn">3</span><span><b>One code per ticket, with Batch</b>Need a different code on every ticket? Batch mode takes one link per line and downloads every code as a ZIP.</span>
→  <span class="sn">3</span><span><b>批量模式，一票一码</b>每张票都要不同的码？批量模式每行一个链接，全部生成后打包成 ZIP 下载。</span>

EN: <span>What should a ticket QR code link to?</span>
→  <span>门票二维码应该链接到哪里？</span>

EN: Your ticket page, a check-in form, or the event details page. The code simply opens that page on the guest’s phone — keep the page itself as the source of truth for entry.
→  购票页、签到表单或活动详情页都可以。二维码只负责在观众手机上打开这个页面，入场规则以页面本身为准。

EN: <span>Can I make a different code for every ticket?</span>
→  <span>能给每张票生成不同的二维码吗？</span>

EN: Yes — Batch mode generates one code per link: paste one ticket link per line, download them all as a ZIP, and print each on its own ticket.
→  可以。批量模式每个链接生成一个码：每行粘贴一个门票链接，全部下载成 ZIP，再分别印到各张门票上。

EN: <span>Do ticket QR codes expire?</span>
→  <span>门票二维码会过期吗？</span>

EN: No. Static codes never expire. If the event moves, point the page behind the code at the new details — or, with a dynamic code, repoint the code itself without reprinting.
→  不会。静态码永不过期。活动改期时，把码指向的页面改成新信息即可；如果用动态码，还能直接改指向，不必重印。

EN: <span>How big should I print it on a ticket?</span>
→  <span>印在门票上要多大？</span>

EN: At least 2 × 2 cm with a clear quiet margin, at 1024 px export or higher. At a busy entrance, bigger is safer — a code that scans first try keeps the line moving.
→  至少 2 × 2 厘米，并留足静区，导出建议 1024 像素以上。入口人多时越大越稳妥——一次就能扫出来的码，才不会堵住队伍。

EN: FreeQrly — qr code ticket
→  FreeQrly — 门票二维码

EN: What should a ticket QR code link to?
→  门票二维码应该链接到哪里？

EN: Can I make a different code for every ticket?
→  能给每张票生成不同的二维码吗？

EN: Do ticket QR codes expire?
→  门票二维码会过期吗？

EN: How big should I print it on a ticket?
→  印在门票上要多大？

EN: Make your ticket QR code
→  生成你的门票二维码

EN: Link to your ticket page
→  链接到门票页面

EN: Your ticketing page, check-in form, or event details — one code, one destination.
→  购票页、签到表单或活动详情——一个码，一个去处。

EN: Paste the link in the studio below. Print-ready PNG or SVG, free, no watermark, no sign-up for static codes.
→  把链接粘贴到下方工作室。可直接印刷的 PNG 或 SVG，免费、无水印，静态码免注册。

EN: One code per ticket, with Batch
→  批量模式，一票一码

EN: Need a different code on every ticket? Batch mode takes one link per line and downloads every code as a ZIP.
→  每张票都要不同的码？批量模式每行一个链接，全部打包成 ZIP 下载。
