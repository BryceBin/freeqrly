# ru


## landing-app-store-qr-code

EN: App Store QR Code Generator: One Code Per Store | FreeQrly
→  Генератор QR-кодов App Store: один код на магазин | FreeQrly

EN: Make a QR code for your App Store or Google Play link. A static code holds one URL, so iOS and Android are two codes — here is how to print the right one.
→  Создайте QR-код для ссылки App Store или Google Play. Статический код хранит один URL, поэтому для iOS и Android нужны два кода — вот как напечатать нужный.

EN: Your app link, <span class="hl hl-honey">printed right</span>.
→  Ваша ссылка на приложение — <span class="hl hl-honey">напечатана как надо</span>.

EN: A static QR code stores one URL, so your App Store listing and your Play listing need one code each. Fill in a link, print it at a size that scans, and put the right code in front of the right phone.
→  Статический QR-код хранит один URL — значит, для страницы в App Store и для страницы в Play нужен свой код. Вставьте ссылку, напечатайте код достаточно крупным, чтобы он сканировался, и поставьте нужный код туда, где его увидит владелец нужного телефона.

EN: <span class="sn">1</span><span><b>Copy one store link</b>App Store from App Store Connect, Play from the Play Console. One link per code — fill the App Store field for iOS, the Google Play field for Android.</span>
→  <span class="sn">1</span><span><b>Скопируйте ссылку одного магазина</b>App Store — из App Store Connect, Play — из Play Console. Одна ссылка на код: для iOS заполните поле App Store, для Android — поле Google Play.</span>

EN: <span class="sn">2</span><span><b>Paste it in</b>Your code appears instantly. Leave the other field empty unless you are making a second code.</span>
→  <span class="sn">2</span><span><b>Вставьте её</b>Код появится сразу. Оставьте второе поле пустым, если не делаете второй код.</span>

EN: <span class="sn">3</span><span><b>Label it and print</b>“iPhone” or “Android” next to the code, at 2 cm or larger. Ads, packaging, receipts, launch slides.</span>
→  <span class="sn">3</span><span><b>Подпишите и напечатайте</b>«iPhone» или «Android» рядом с кодом, сам код — от 2 см. Реклама, упаковка, чеки, слайды запуска.</span>

EN: One static code holds one link
→  Один статический код — одна ссылка

EN: This is the part most app-store QR pages skip, so here it is plainly: a QR code stores text, and that text is a URL. One code, one destination. There is no logic inside the pattern that can look at the phone and pick a store.
→  Об этом большинство страниц про QR-коды для магазинов приложений умалчивают, поэтому скажем прямо: QR-код хранит текст, и этот текст — URL. Один код — один адрес. Внутри узора нет никакой логики, которая могла бы посмотреть на телефон и выбрать магазин.

EN: That matters because your iOS and Android listings are two different URLs. A single static code can only point at one of them. If you encode the App Store link, Android users land on a page for an app they can't install, and the reverse is just as bad.
→  Это важно, потому что страницы приложения в App Store и Google Play — два разных URL. Один статический код может указывать только на одну из них. Закодируете ссылку App Store — пользователи Android попадут на страницу приложения, которое не могут установить. В обратную сторону — та же история.

EN: You have three ways to cover both platforms. The table below compares them.
→  Охватить обе платформы можно тремя способами. Таблица ниже сравнивает их.

EN: Approach
→  Подход

EN: Printed codes
→  Сколько кодов печатать

EN: Works if a link changes
→  Работает при смене ссылки

EN: Setup
→  Что нужно

EN: Two codes, side by side
→  Два кода рядом

EN: one App Store, one Play
→  один App Store, один Play

EN: no, reprint
→  нет, перепечатывать

EN: none
→  ничего

EN: One code to a router page
→  Один код на страницу-маршрутизатор

EN: page reads the device, forwards to the right store
→  страница определяет устройство и отправляет в нужный магазин

EN: yes, if the page is dynamic
→  да, если страница динамическая

EN: a page you control
→  своя страница

EN: Store smart banner
→  Умный баннер магазина

EN: Apple and Google banners on your own site
→  баннеры Apple и Google на вашем сайте

EN: 1 (to your site)
→  1 (на ваш сайт)

EN: a website
→  сайт

EN: Two codes is the honest, zero-effort option. Router page is what most apps do once they have a marketing site. Smart banners only work if people land on your site first, which is a different job from a printed code.
→  Два кода — честный вариант без лишних усилий. Большинство приложений заводит страницу-маршрутизатор, когда появляется сайт для продвижения. Умные баннеры работают, только если человек сначала попал на ваш сайт, — а это уже другая задача, нежели печатный код.

EN: How to get your store links
→  Где взять ссылки на магазины

EN: Both stores give you a clean, permanent URL, and both are easy to find once you know where to look.
→  Оба магазина выдают аккуратный постоянный URL, и найти его легко, если знать, где искать.

EN: For iOS, open your app in App Store Connect, go to App Information, and copy the App Store URL. It looks like <code>apps.apple.com/app/id1234567890</code>. You can add a country segment — <code>apps.apple.com/gb/app/id…</code> — if you want the code to open a specific storefront, but the plain version redirects to the visitor's own region, which is usually what you want.
→  Для iOS откройте приложение в App Store Connect, перейдите в раздел «Информация о приложении» и скопируйте URL App Store. Он выглядит так: <code>apps.apple.com/app/id1234567890</code>. Если нужно, чтобы код открывал конкретную витрину, добавьте сегмент страны — <code>apps.apple.com/gb/app/id…</code>. Но простая версия перенаправляет в регион посетителя, а обычно нужно именно это.

EN: For Android, open the Play Console listing and copy the link from the browser bar. It looks like <code>play.google.com/store/apps/details?id=com.yourcompany.yourapp</code>. The <code>id</code> is your package name, and it never changes even when the app name does.
→  Для Android откройте страницу приложения в Play Console и скопируйте ссылку из адресной строки. Она выглядит так: <code>play.google.com/store/apps/details?id=com.yourcompany.yourapp</code>. <code>id</code> — это имя пакета, оно не меняется, даже если меняется название приложения.

EN: Drop anything after the ID. Marketing tools often append tracking parameters like <code>?mt=8</code> or <code>&referrer=…</code>. They're harmless, but they make the QR pattern denser for no benefit, and a denser pattern is harder to print small.
→  Всё после ID можно отбросить. Маркетинговые инструменты часто добавляют параметры отслеживания вроде <code>?mt=8</code> или <code>&referrer=…</code>. Они безвредны, но делают узор QR-кода плотнее без всякой пользы, а плотный узор хуже печатается мелко.

EN: Building a router page that works
→  Как сделать рабочую страницу-маршрутизатор

EN: If you go with one code, it needs somewhere to send people. A router page is a small page on your own domain that reads the user agent and forwards.
→  Если вы выбрали один код, ему нужно куда-то отправлять людей. Страница-маршрутизатор — это небольшая страница на вашем домене, которая читает user agent и перенаправляет дальше.

EN: The logic is short: if the browser reports an iPhone or iPad, go to the App Store; if it reports Android, go to Play; otherwise show both buttons. Keep a fallback for desktop, because a meaningful share of scans come from people testing on a laptop.
→  Логика короткая: если браузер сообщает об iPhone или iPad — ведём в App Store; если об Android — в Play; в остальных случаях показываем обе кнопки. Обязательно оставьте запасной вариант для компьютеров: заметная доля сканирований приходится на тех, кто проверяет код с ноутбука.

EN: Two things break these pages in practice. Apple's in-app browsers and some social apps strip the user agent down to something generic, so the detection guesses wrong. And a redirect that fires before the page renders can look like a broken link. Showing both buttons with the detected one highlighted is more forgiving than an instant forward.
→  На практике такие страницы ломают две вещи. Встроенные браузеры Apple и некоторые соцсети урезают user agent до чего-то обобщённого, и определение ошибается. А перенаправление, которое срабатывает до отрисовки страницы, выглядит как битая ссылка. Показать обе кнопки, выделив определённую, — надёжнее, чем мгновенно перебрасывать.

EN: If you want the destination editable later, use a dynamic code pointing at the router page. Change the page and every printed code follows, no reprint.
→  Если адрес нужно будет менять, используйте динамический код, указывающий на страницу-маршрутизатор. Меняете страницу — и все напечатанные коды следуют за ней, перепечатывать не нужно.

EN: App launch slide
→  Слайд запуска приложения

EN: 8 cm
→  8 см

EN: scanned from a seat, 1–2 m away
→  сканируют сидя, с 1–2 м

EN: Packaging and inserts
→  Упаковка и вкладыши

EN: one code per platform, clearly labelled
→  по коду на платформу, с чёткими подписями

EN: Receipt footer
→  Низ чека

EN: thermal printers blur thin lines; test first
→  термопринтеры смазывают тонкие линии — сначала проверьте

EN: Poster or ad
→  Плакат или реклама

EN: scanned from 2–3 m
→  сканируют с 2–3 м

EN: only if you print two codes with labels
→  только если печатаете два кода с подписями

EN: When you print two codes, label them. A pair of identical-looking squares with no "iPhone" and "Android" text is worse than one code, because people scan the wrong one and land on a store they can't use.
→  Печатаете два кода — подпишите их. Пара одинаковых на вид квадратиков без надписей «iPhone» и «Android» хуже одного кода: люди сканируют не тот и попадают в магазин, которым не могут воспользоваться.

EN: <span>Can one static code open both stores?</span>
→  <span>Может ли один статический код открывать оба магазина?</span>

EN: No. A static code stores a single URL, and your two store listings are two URLs. Encode the App Store link and Android visitors land on an app they cannot install. Print two labelled codes, or point one code at a page on your own domain that reads the phone and forwards to the right store.
→  Нет. Статический код хранит один URL, а ваши страницы в двух магазинах — это два URL. Закодируйте ссылку App Store — и посетители с Android попадут на приложение, которое не могут установить. Печатайте два кода с подписями или направьте один код на страницу на вашем домене, которая определяет телефон и перенаправляет в нужный магазин.

EN: <span>What if I fill in both fields?</span>
→  <span>А если заполнить оба поля?</span>

EN: Only the App Store link is encoded — the Play field is used when the App Store field is empty. To cover both platforms, make two codes, one per field.
→  Кодируется только ссылка App Store: поле Play используется, когда поле App Store пустое. Чтобы охватить обе платформы, сделайте два кода — по одному на каждое поле.

EN: <span>What if I only have one platform?</span>
→  <span>А если платформа одна?</span>

EN: Fill that field and print one code. Nothing else is needed.
→  Заполните это поле и напечатайте один код. Больше ничего не нужно.

EN: <span>Can it detect the phone and route automatically?</span>
→  <span>Сам ли он определяет телефон и направляет в нужный магазин?</span>

EN: Not on its own — a printed pattern cannot run logic. Device detection needs a page in between: host a small router page, then point a dynamic code at it so you can change the destination later without reprinting.
→  Сам по себе — нет: напечатанный узор не умеет выполнять логику. Для определения устройства нужна страница-посредник: разместите небольшую страницу-маршрутизатор и направьте на неё динамический код, чтобы потом менять адрес без перепечатки.

EN: <span>Does it track installs?</span>
→  <span>Он считает установки?</span>

EN: No. Static codes carry only the link and never phone home. App Store Connect and the Play Console already report installs.
→  Нет. Статический код содержит только ссылку и ничего никуда не отправляет. App Store Connect и Play Console и так считают установки.

EN: FreeQrly — app store qr code generator
→  FreeQrly — генератор QR-кодов App Store

EN: Can one static code open both stores?
→  Может ли один статический код открывать оба магазина?

EN: What if I fill in both fields?
→  А если заполнить оба поля?

EN: What if I only have one platform?
→  А если платформа одна?

EN: Can it detect the phone and route automatically?
→  Сам ли он определяет телефон и направляет в нужный магазин?

EN: Does it track installs?
→  Он считает установки?

EN: Make your app store QR code
→  Создайте свой QR-код App Store

EN: Copy one store link
→  Скопируйте ссылку одного магазина

EN: App Store from App Store Connect, Play from the Play Console. One link per code — fill the App Store field for iOS, the Google Play field for Android.
→  App Store — из App Store Connect, Play — из Play Console. Одна ссылка на код: для iOS заполните поле App Store, для Android — поле Google Play.

EN: Paste it in
→  Вставьте её

EN: Your code appears instantly. Leave the other field empty unless you are making a second code.
→  Код появится сразу. Оставьте второе поле пустым, если не делаете второй код.

EN: Label it and print
→  Подпишите и напечатайте

EN: “iPhone” or “Android” next to the code, at 2 cm or larger. Ads, packaging, receipts, launch slides.
→  «iPhone» или «Android» рядом с кодом, сам код — от 2 см. Реклама, упаковка, чеки, слайды запуска.


## about

EN: About FreeQrly — Free Static QR Codes, No Sign-Up, No Expiry
→  О FreeQrly — бесплатные статические QR-коды без регистрации

EN: FreeQrly is a free QR code generator: static codes run 100% in your browser — no sign-up, no tracking, no expiry. Learn what it is and how it works.
→  FreeQrly — бесплатный генератор QR-кодов: статические коды работают на 100% в браузере — без регистрации, слежки и срока действия. Что это и как работает.

EN: About FreeQrly
→  О FreeQrly

EN: A free QR code generator: static codes run 100% in your browser — no sign-up, no tracking, no expiry.
→  Бесплатный генератор QR-кодов: статические коды работают на 100% в вашем браузере — без регистрации, слежки и срока действия.

EN: Qly protecting your privacy with a shield
→  Qly защищает вашу приватность щитом

EN: About
→  О проекте

EN: What is <span class="hl hl-mint">FreeQrly</span>?
→  Что такое <span class="hl hl-mint">FreeQrly</span>?

EN: FreeQrly is a free QR code generator with a simple idea: the tool should live in your browser, not on somebody's server. You type, it draws — nothing is uploaded, tracked, or billed.
→  FreeQrly — бесплатный генератор QR-кодов с простой идеей: инструмент должен жить в вашем браузере, а не на чьём-то сервере. Вы вводите — он рисует: ничего не загружается, не отслеживается и не оплачивается.

EN: <b>100% browser-based</b><span>Every code is drawn locally with JavaScript. Your links, contacts, and WiFi passwords never leave your device.</span>
→  <b>100% в браузере</b><span>Каждый код рисуется локально на JavaScript. Ваши ссылки, контакты и пароли от WiFi никогда не покидают устройство.</span>

EN: <b>Codes that never expire</b><span>Static codes live in the pattern itself; dynamic codes stay editable after printing. No trials, no deactivated codes — what you print today scans in ten years.</span>
→  <b>Коды, которые не истекают</b><span>Статические коды живут в самом узоре, динамические остаются редактируемыми после печати. Никаких пробных периодов и деактивированных кодов: напечатанное сегодня отсканируется и через десять лет.</span>

EN: <b>Free to start</b><span>Static codes need no account at all. Dynamic codes — editable, with scan stats — need a free sign-in. No watermark either way.</span>
→  <b>Начать бесплатно</b><span>Статическим кодам аккаунт не нужен вовсе. Динамическим — редактируемым, со статистикой сканирований — нужен бесплатный вход. Водяных знаков нет в обоих случаях.</span>

EN: <b>10 languages</b><span>English, Chinese, Spanish, Hindi, Arabic (RTL), Portuguese, French, Russian, German, Japanese.</span>
→  <b>10 языков</b><span>Английский, китайский, испанский, хинди, арабский (справа налево), португальский, французский, русский, немецкий, японский.</span>

EN: <b>Built for print</b><span>High-resolution export and vector SVG, quiet zones respected — made for business cards, menus, and posters.</span>
→  <b>Сделано для печати</b><span>Экспорт в высоком разрешении и векторный SVG, с соблюдением тихих зон — для визиток, меню и постеров.</span>

EN: <b>Agent-friendly</b><span>A free <a href="/developers/">API and MCP server</a> so AI assistants can generate codes too.</span>
→  <b>Удобно для агентов</b><span>Бесплатные <a href="/developers/">API и MCP-сервер</a>, чтобы коды могли генерировать и ИИ-ассистенты.</span>

EN: Questions, answered
→  Вопросы и ответы

EN: Almost everything is free. Static codes are completely free, with no watermarks — they are made entirely in your browser and need no account. Dynamic codes need a free sign-in so they can be edited later, and 20 are included free; if you need more, an optional Pro subscription (US$9/month or US$90/year) makes dynamic codes unlimited.
→  Почти всё бесплатно. Статические коды полностью бесплатны, без водяных знаков — они создаются целиком в вашем браузере и не требуют аккаунта. Для динамических кодов нужен бесплатный вход, чтобы их можно было редактировать позже, и 20 включены бесплатно; если нужно больше, необязательная подписка Pro (9 долларов США в месяц или 90 в год) делает динамические коды безлимитными.

EN: Do the QR codes expire?
→  Истекают ли QR-коды?

EN: No — neither kind. A static code's destination lives inside the pattern itself, and dynamic codes stay live and editable for as long as your account exists. Details: <a href="/blog/do-qr-codes-expire/">do QR codes expire?</a>
→  Нет — ни те, ни другие. Адрес статического кода живёт внутри самого узора, а динамические коды остаются рабочими и редактируемыми, пока существует ваш аккаунт. Подробнее: <a href="/blog/do-qr-codes-expire/">истекают ли QR-коды?</a>

EN: Can I use it for my business?
→  Можно ли использовать для бизнеса?

EN: Yes — commercial use is free. Restaurants use it for <a href="/blog/qr-codes-for-restaurants/">menus and reviews</a>, shops for <a href="/google-review-qr-code/">review codes</a> and <a href="/wifi-qr-code/">WiFi codes</a>.
→  Да — коммерческое использование бесплатно. Рестораны используют его для <a href="/blog/qr-codes-for-restaurants/">меню и отзывов</a>, магазины — для <a href="/google-review-qr-code/">кодов отзывов</a> и <a href="/wifi-qr-code/">WiFi-кодов</a>.

EN: Who is behind FreeQrly?
→  Кто стоит за FreeQrly?

EN: An independent maker who got tired of "free" generators that hold your codes hostage behind a trial. The mascot is Qly, a small elephant who appears across the site.
→  Независимый разработчик, которому надоело, что «бесплатные» генераторы держат ваши коды в заложниках пробного периода. Талисман — Qly, маленький слон, который появляется по всему сайту.

EN: Try the generator →
→  Попробовать генератор →

EN: FreeQrly is a free QR code generator that runs entirely in the browser. No sign-up, no tracking, no expiry — static QR codes with optional logos, in 10 languages.
→  FreeQrly — бесплатный генератор QR-кодов, который работает полностью в браузере. Без регистрации, слежки и срока действия — статические QR-коды с опциональными логотипами, на 10 языках.

EN: What is FreeQrly?
→  Что такое FreeQrly?

EN: FreeQrly is a free online QR code generator. It creates static QR codes for links, text, WiFi, vCards, SMS, calls, and locations — entirely in your browser, with no account and no fees.
→  FreeQrly — бесплатный онлайн-генератор QR-кодов. Он создаёт статические QR-коды для ссылок, текста, WiFi, vCard, SMS, звонков и мест — полностью в вашем браузере, без аккаунта и без оплаты.

EN: Yes — almost everything. Static codes are free with no trial and no watermarks, including logo upload, batch generation, and high-resolution export. Static codes need no account; dynamic codes need a free sign-in and include 20 free, with an optional Pro subscription for unlimited dynamic codes.
→  Да — почти всё. Статические коды бесплатны, без пробного периода и водяных знаков, включая загрузку логотипа, пакетную генерацию и экспорт в высоком разрешении. Статическим кодам аккаунт не нужен; динамическим нужен бесплатный вход, и включают 20 кодов бесплатно, а необязательная подписка Pro даёт безлимитные динамические коды.

EN: Do FreeQrly QR codes expire?
→  Истекают ли QR-коды FreeQrly?

EN: No. Static codes encode the destination directly in the pattern, and dynamic codes stay live and editable — neither kind expires or requires a subscription.
→  Нет. Статические коды кодируют адрес прямо в узоре, а динамические остаются рабочими и редактируемыми — ни те, ни другие не истекают и не требуют подписки.

EN: Does FreeQrly track my QR codes or my data?
→  Отслеживает ли FreeQrly мои QR-коды или мои данные?

EN: Static codes are generated locally in your browser; their content is never uploaded and they have no scan tracking. Dynamic codes count scans — that is what they are for — and their destinations can be changed anytime.
→  Статические коды генерируются локально в вашем браузере: их содержимое никуда не загружается, и сканирования не отслеживаются. Динамические коды считают сканы — для этого они и нужны, — а их адреса можно менять в любой момент.

EN: What languages does FreeQrly support?
→  Какие языки поддерживает FreeQrly?

EN: Ten: English, Chinese, Spanish, Hindi, Arabic (with right-to-left layout), Portuguese, French, Russian, German, and Japanese.
→  Десять: английский, китайский, испанский, хинди, арабский (с письмом справа налево), португальский, французский, русский, немецкий и японский.


## landing-ticket-qr-code

EN: Free Ticket QR Code Generator | FreeQrly
→  Бесплатный генератор QR-кодов для билетов | FreeQrly

EN: Create free QR codes for tickets: link to your ticket or check-in page, print one code per ticket with Batch mode, no sign-up for static codes, never expires.
→  Бесплатные QR-коды для билетов: по коду на каждый билет в пакетном режиме, без регистрации для статических кодов, без срока действия.

EN: One scan at the door, <span class="hl hl-mint">no ticket queue</span>.
→  Одно сканирование у входа — <span class="hl hl-mint">и никакой очереди за билетами</span>.

EN: Put a QR code on every ticket, poster, and confirmation email. Guests scan at the entrance and land straight on your ticket or check-in page — concerts, conferences, workshops, school events.
→  Разместите QR-код на каждом билете, плакате и письме с подтверждением. Гости сканируют его на входе и сразу попадают на страницу билета или регистрации — концерты, конференции, мастер-классы, школьные мероприятия.

EN: <span class="sn">1</span><span><b>Link to your ticket page</b>Your ticketing page, check-in form, or event details — one code, one destination.</span>
→  <span class="sn">1</span><span><b>Ссылка на страницу билета</b>Ваша страница продажи билетов, форма регистрации или детали мероприятия — один код — один адрес назначения.</span>

EN: <span class="sn">2</span><span><b>Make the code</b>Paste the link in the studio below. Print-ready PNG or SVG, free, no watermark, no sign-up for static codes.</span>
→  <span class="sn">2</span><span><b>Создайте код</b>Вставьте ссылку в студию ниже. PNG или SVG, готовые к печати, бесплатно, без водяных знаков, без регистрации для статических кодов.</span>

EN: <span class="sn">3</span><span><b>One code per ticket, with Batch</b>Need a different code on every ticket? Batch mode takes one link per line and downloads every code as a ZIP.</span>
→  <span class="sn">3</span><span><b>Один код на билет — в пакетном режиме</b>Нужен свой код на каждом билете? Пакетный режим принимает по одной ссылке на строку и скачивает все коды одним ZIP-архивом.</span>

EN: <span>What should a ticket QR code link to?</span>
→  <span>На что должен ссылаться QR-код билета?</span>

EN: Your ticket page, a check-in form, or the event details page. The code simply opens that page on the guest’s phone — keep the page itself as the source of truth for entry.
→  Страница билета, форма регистрации или страница с деталями мероприятия. Код просто открывает эту страницу на телефоне гостя — а точкой входа пусть остаётся сама страница.

EN: <span>Can I make a different code for every ticket?</span>
→  <span>Можно ли сделать отдельный код для каждого билета?</span>

EN: Yes — Batch mode generates one code per link: paste one ticket link per line, download them all as a ZIP, and print each on its own ticket.
→  Да — пакетный режим генерирует по одному коду на ссылку: вставьте по одной ссылке на билет на строку, скачайте все одним ZIP-архивом и напечатайте каждый на своём билете.

EN: <span>Do ticket QR codes expire?</span>
→  <span>Истекают ли QR-коды билетов?</span>

EN: No. Static codes never expire. If the event moves, point the page behind the code at the new details — or, with a dynamic code, repoint the code itself without reprinting.
→  Нет. Статические коды никогда не истекают. Если мероприятие переезжает, направьте страницу, на которую ведёт код, на новые детали — или, с динамическим кодом, перенаправьте сам код без перепечатки.

EN: <span>How big should I print it on a ticket?</span>
→  <span>Какого размера печатать код на билете?</span>

EN: At least 2 × 2 cm with a clear quiet margin, at 1024 px export or higher. At a busy entrance, bigger is safer — a code that scans first try keeps the line moving.
→  Не меньше 2 × 2 см, с чистой тихой зоной, при экспорте от 1024 px. На оживлённом входе чем крупнее, тем надёжнее: код, считывающийся с первой попытки, не даёт очереди расти.

EN: FreeQrly — qr code ticket
→  FreeQrly — QR-код для билета

EN: What should a ticket QR code link to?
→  На что должен ссылаться QR-код билета?

EN: Can I make a different code for every ticket?
→  Можно ли сделать отдельный код для каждого билета?

EN: Do ticket QR codes expire?
→  Истекают ли QR-коды билетов?

EN: How big should I print it on a ticket?
→  Какого размера печатать код на билете?

EN: Make your ticket QR code
→  Создайте QR-код для билета

EN: Link to your ticket page
→  Ссылка на страницу билета

EN: Your ticketing page, check-in form, or event details — one code, one destination.
→  Ваша страница продажи билетов, форма регистрации или детали мероприятия — один код — один адрес назначения.

EN: Paste the link in the studio below. Print-ready PNG or SVG, free, no watermark, no sign-up for static codes.
→  Вставьте ссылку в студию ниже. PNG или SVG, готовые к печати, бесплатно, без водяных знаков, без регистрации для статических кодов.

EN: One code per ticket, with Batch
→  Один код на билет — в пакетном режиме

EN: Need a different code on every ticket? Batch mode takes one link per line and downloads every code as a ZIP.
→  Нужен свой код на каждом билете? Пакетный режим принимает по одной ссылке на строку и скачивает все коды одним ZIP-архивом.
