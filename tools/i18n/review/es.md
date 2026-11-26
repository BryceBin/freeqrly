# es


## landing-app-store-qr-code

EN: App Store QR Code Generator: One Code Per Store | FreeQrly
→  Generador de QR App Store: un código por tienda | FreeQrly

EN: Make a QR code for your App Store or Google Play link. A static code holds one URL, so iOS and Android are two codes — here is how to print the right one.
→  Crea un QR para tu enlace de App Store o Google Play. Un código estático guarda una URL: iOS y Android son dos códigos, y aquí ves cómo imprimir el correcto.

EN: Your app link, <span class="hl hl-honey">printed right</span>.
→  Tu enlace de app, <span class="hl hl-honey">bien impreso</span>.

EN: A static QR code stores one URL, so your App Store listing and your Play listing need one code each. Fill in a link, print it at a size that scans, and put the right code in front of the right phone.
→  Un QR estático guarda una URL, así que tu ficha de App Store y tu ficha de Play necesitan un código cada una. Pega un enlace, imprímelo a un tamaño que se escanee y pon el código correcto delante del teléfono correcto.

EN: <span class="sn">1</span><span><b>Copy one store link</b>App Store from App Store Connect, Play from the Play Console. One link per code — fill the App Store field for iOS, the Google Play field for Android.</span>
→  <span class="sn">1</span><span><b>Copia un enlace de tienda</b>App Store desde App Store Connect, Play desde Play Console. Un enlace por código: rellena el campo de App Store para iOS y el de Google Play para Android.</span>

EN: <span class="sn">2</span><span><b>Paste it in</b>Your code appears instantly. Leave the other field empty unless you are making a second code.</span>
→  <span class="sn">2</span><span><b>Pégalo</b>Tu código aparece al instante. Deja el otro campo vacío salvo que estés creando un segundo código.</span>

EN: <span class="sn">3</span><span><b>Label it and print</b>“iPhone” or “Android” next to the code, at 2 cm or larger. Ads, packaging, receipts, launch slides.</span>
→  <span class="sn">3</span><span><b>Etiquétalo e imprime</b>“iPhone” o “Android” junto al código, a 2 cm o más. Anuncios, empaques, recibos, diapositivas de lanzamiento.</span>

EN: One static code holds one link
→  Un código estático, un enlace

EN: This is the part most app-store QR pages skip, so here it is plainly: a QR code stores text, and that text is a URL. One code, one destination. There is no logic inside the pattern that can look at the phone and pick a store.
→  Esto es lo que se saltan casi todas las páginas de QR para tiendas de apps, así que lo decimos claro: un código QR guarda texto, y ese texto es una URL. Un código, un destino. Dentro del patrón no hay lógica que mire el teléfono y elija una tienda.

EN: That matters because your iOS and Android listings are two different URLs. A single static code can only point at one of them. If you encode the App Store link, Android users land on a page for an app they can't install, and the reverse is just as bad.
→  Esto importa porque tus fichas de iOS y Android son dos URLs distintas. Un solo código estático solo puede apuntar a una de ellas. Si codificas el enlace de App Store, los usuarios de Android llegan a la página de una app que no pueden instalar, y al revés pasa exactamente lo mismo.

EN: You have three ways to cover both platforms. The table below compares them.
→  Tienes tres formas de cubrir las dos plataformas. La tabla de abajo las compara.

EN: Approach
→  Enfoque

EN: Printed codes
→  Códigos impresos

EN: Works if a link changes
→  Funciona si cambia un enlace

EN: Setup
→  Preparación

EN: Two codes, side by side
→  Dos códigos, uno al lado del otro

EN: one App Store, one Play
→  uno de App Store, uno de Play

EN: no, reprint
→  no, reimprimir

EN: none
→  ninguna

EN: One code to a router page
→  Un código que apunta a una página de redirección

EN: page reads the device, forwards to the right store
→  la página detecta el dispositivo y redirige a la tienda correcta

EN: yes, if the page is dynamic
→  sí, si la página es dinámica

EN: a page you control
→  una página que controlas

EN: Store smart banner
→  Banner inteligente de la app

EN: Apple and Google banners on your own site
→  Banners de Apple y Google en tu propio sitio

EN: 1 (to your site)
→  1 (a tu sitio)

EN: a website
→  un sitio web

EN: Two codes is the honest, zero-effort option. Router page is what most apps do once they have a marketing site. Smart banners only work if people land on your site first, which is a different job from a printed code.
→  Dos códigos son la opción honesta y sin esfuerzo. La página de redirección es lo que hacen casi todas las apps cuando ya tienen una web de marketing. Los banners inteligentes solo funcionan si la gente llega antes a tu sitio, que es un trabajo distinto del de un código impreso.

EN: How to get your store links
→  Cómo conseguir tus enlaces de tienda

EN: Both stores give you a clean, permanent URL, and both are easy to find once you know where to look.
→  Las dos tiendas te dan una URL limpia y permanente, y ambas son fáciles de encontrar cuando sabes dónde mirar.

EN: For iOS, open your app in App Store Connect, go to App Information, and copy the App Store URL. It looks like <code>apps.apple.com/app/id1234567890</code>. You can add a country segment — <code>apps.apple.com/gb/app/id…</code> — if you want the code to open a specific storefront, but the plain version redirects to the visitor's own region, which is usually what you want.
→  Para iOS, abre tu app en App Store Connect, ve a Información de la app y copia la URL de App Store. Se ve así: <code>apps.apple.com/app/id1234567890</code>. Puedes añadir un segmento de país — <code>apps.apple.com/gb/app/id…</code> — si quieres que el código abra una tienda concreta, pero la versión simple redirige a la región del visitante, que suele ser lo que buscas.

EN: For Android, open the Play Console listing and copy the link from the browser bar. It looks like <code>play.google.com/store/apps/details?id=com.yourcompany.yourapp</code>. The <code>id</code> is your package name, and it never changes even when the app name does.
→  Para Android, abre la ficha en Play Console y copia el enlace de la barra del navegador. Se ve así: <code>play.google.com/store/apps/details?id=com.yourcompany.yourapp</code>. El <code>id</code> es tu nombre de paquete y nunca cambia, ni siquiera cuando cambia el nombre de la app.

EN: Drop anything after the ID. Marketing tools often append tracking parameters like <code>?mt=8</code> or <code>&referrer=…</code>. They're harmless, but they make the QR pattern denser for no benefit, and a denser pattern is harder to print small.
→  Descarta todo lo que haya después del ID. Las herramientas de marketing suelen añadir parámetros de seguimiento como <code>?mt=8</code> o <code>&referrer=…</code>. Son inofensivos, pero hacen que el patrón QR sea más denso sin ninguna ventaja, y un patrón más denso cuesta más imprimir en pequeño.

EN: Building a router page that works
→  Cómo crear una página de redirección que funcione

EN: If you go with one code, it needs somewhere to send people. A router page is a small page on your own domain that reads the user agent and forwards.
→  Si te quedas con un solo código, este necesita un sitio al que enviar a la gente. Una página de redirección es una página pequeña en tu propio dominio que lee el agente de usuario y reenvía.

EN: The logic is short: if the browser reports an iPhone or iPad, go to the App Store; if it reports Android, go to Play; otherwise show both buttons. Keep a fallback for desktop, because a meaningful share of scans come from people testing on a laptop.
→  La lógica es corta: si el navegador informa de un iPhone o un iPad, ve a App Store; si informa de Android, ve a Play; si no, muestra los dos botones. Deja un plan B para escritorio, porque una parte nada desdeñable de los escaneos viene de gente que prueba en un portátil.

EN: Two things break these pages in practice. Apple's in-app browsers and some social apps strip the user agent down to something generic, so the detection guesses wrong. And a redirect that fires before the page renders can look like a broken link. Showing both buttons with the detected one highlighted is more forgiving than an instant forward.
→  En la práctica, estas páginas fallan por dos cosas. Los navegadores integrados de Apple y algunas apps sociales reducen el agente de usuario a algo genérico, y la detección se equivoca. Y una redirección que se dispara antes de que la página se dibuje puede parecer un enlace roto. Mostrar los dos botones con el detectado resaltado funciona mejor que reenviar al instante.

EN: If you want the destination editable later, use a dynamic code pointing at the router page. Change the page and every printed code follows, no reprint.
→  Si quieres poder cambiar el destino más adelante, usa un código dinámico que apunte a la página de redirección. Cambia la página y todos los códigos impresos la siguen, sin reimprimir.

EN: App launch slide
→  Diapositiva de lanzamiento

⚠️ 未翻译（与英文相同）
EN: 8 cm
→  8 cm

EN: scanned from a seat, 1–2 m away
→  escaneado desde el asiento, a 1–2 m

EN: Packaging and inserts
→  Empaques y encartes

EN: one code per platform, clearly labelled
→  un código por plataforma, bien etiquetado

EN: Receipt footer
→  Pie de recibo

EN: thermal printers blur thin lines; test first
→  las impresoras térmicas emborronan las líneas finas; prueba antes

EN: Poster or ad
→  Póster o anuncio

EN: scanned from 2–3 m
→  escaneado a 2–3 m

EN: only if you print two codes with labels
→  solo si imprimes dos códigos con etiquetas

EN: When you print two codes, label them. A pair of identical-looking squares with no "iPhone" and "Android" text is worse than one code, because people scan the wrong one and land on a store they can't use.
→  Cuando imprimas dos códigos, etiquétalos. Un par de cuadrados idénticos sin el texto “iPhone” y “Android” es peor que un solo código, porque la gente escanea el equivocado y acaba en una tienda que no le sirve.

EN: <span>Can one static code open both stores?</span>
→  <span>¿Puede un código estático abrir las dos tiendas?</span>

EN: No. A static code stores a single URL, and your two store listings are two URLs. Encode the App Store link and Android visitors land on an app they cannot install. Print two labelled codes, or point one code at a page on your own domain that reads the phone and forwards to the right store.
→  No. Un código estático guarda una sola URL, y tus dos fichas de tienda son dos URLs. Si codificas el enlace de App Store, los visitantes de Android llegan a una app que no pueden instalar. Imprime dos códigos etiquetados o apunta un código a una página de tu propio dominio que detecte el teléfono y redirija a la tienda correcta.

EN: <span>What if I fill in both fields?</span>
→  <span>¿Y si relleno los dos campos?</span>

EN: Only the App Store link is encoded — the Play field is used when the App Store field is empty. To cover both platforms, make two codes, one per field.
→  Solo se codifica el enlace de App Store: el campo de Play se usa cuando el de App Store está vacío. Para cubrir las dos plataformas, crea dos códigos, uno por campo.

EN: <span>What if I only have one platform?</span>
→  <span>¿Y si solo tengo una plataforma?</span>

EN: Fill that field and print one code. Nothing else is needed.
→  Rellena ese campo e imprime un código. No hace falta nada más.

EN: <span>Can it detect the phone and route automatically?</span>
→  <span>¿Detecta el teléfono y redirige solo?</span>

EN: Not on its own — a printed pattern cannot run logic. Device detection needs a page in between: host a small router page, then point a dynamic code at it so you can change the destination later without reprinting.
→  No por sí solo: un patrón impreso no puede ejecutar lógica. La detección de dispositivo necesita una página en medio: aloja una pequeña página de redirección y apunta a ella un código dinámico, así podrás cambiar el destino después sin reimprimir.

EN: <span>Does it track installs?</span>
→  <span>¿Cuenta las instalaciones?</span>

EN: No. Static codes carry only the link and never phone home. App Store Connect and the Play Console already report installs.
→  No. Los códigos estáticos solo llevan el enlace y nunca envían nada. App Store Connect y Play Console ya informan de las instalaciones.

EN: FreeQrly — app store qr code generator
→  FreeQrly — generador de QR de App Store

EN: Can one static code open both stores?
→  ¿Puede un código estático abrir las dos tiendas?

EN: What if I fill in both fields?
→  ¿Y si relleno los dos campos?

EN: What if I only have one platform?
→  ¿Y si solo tengo una plataforma?

EN: Can it detect the phone and route automatically?
→  ¿Detecta el teléfono y redirige solo?

EN: Does it track installs?
→  ¿Cuenta las instalaciones?

EN: Make your app store QR code
→  Crea tu QR de App Store

EN: Copy one store link
→  Copia un enlace de tienda

EN: App Store from App Store Connect, Play from the Play Console. One link per code — fill the App Store field for iOS, the Google Play field for Android.
→  App Store desde App Store Connect, Play desde Play Console. Un enlace por código: rellena el campo de App Store para iOS y el de Google Play para Android.

EN: Paste it in
→  Pégalo

EN: Your code appears instantly. Leave the other field empty unless you are making a second code.
→  Tu código aparece al instante. Deja el otro campo vacío salvo que estés creando un segundo código.

EN: Label it and print
→  Etiquétalo e imprime

EN: “iPhone” or “Android” next to the code, at 2 cm or larger. Ads, packaging, receipts, launch slides.
→  “iPhone” o “Android” junto al código, a 2 cm o más. Anuncios, empaques, recibos, diapositivas de lanzamiento.


## about

EN: About FreeQrly — Free Static QR Codes, No Sign-Up, No Expiry
→  Acerca de FreeQrly — QR gratis, sin registro ni caducidad

EN: FreeQrly is a free QR code generator: static codes run 100% in your browser — no sign-up, no tracking, no expiry. Learn what it is and how it works.
→  FreeQrly es un generador gratuito de QR: los estáticos funcionan 100% en tu navegador, sin registro, sin rastreo ni caducidad. Descubre qué es y cómo funciona.

EN: About FreeQrly
→  Acerca de FreeQrly

EN: A free QR code generator: static codes run 100% in your browser — no sign-up, no tracking, no expiry.
→  Un generador gratuito de códigos QR: los estáticos funcionan 100% en tu navegador, sin registro, sin rastreo y sin caducidad.

EN: Qly protecting your privacy with a shield
→  Qly protegiendo tu privacidad con un escudo

EN: About
→  Acerca de

EN: What is <span class="hl hl-mint">FreeQrly</span>?
→  ¿Qué es <span class="hl hl-mint">FreeQrly</span>?

EN: FreeQrly is a free QR code generator with a simple idea: the tool should live in your browser, not on somebody's server. You type, it draws — nothing is uploaded, tracked, or billed.
→  FreeQrly es un generador gratuito de códigos QR con una idea simple: la herramienta debe vivir en tu navegador, no en el servidor de nadie. Tú escribes y él dibuja: nada se sube, se rastrea ni se cobra.

EN: <b>100% browser-based</b><span>Every code is drawn locally with JavaScript. Your links, contacts, and WiFi passwords never leave your device.</span>
→  <b>100% en el navegador</b><span>Cada código se dibuja localmente con JavaScript. Tus enlaces, contactos y contraseñas de WiFi nunca salen de tu dispositivo.</span>

EN: <b>Codes that never expire</b><span>Static codes live in the pattern itself; dynamic codes stay editable after printing. No trials, no deactivated codes — what you print today scans in ten years.</span>
→  <b>Códigos que nunca caducan</b><span>Los códigos estáticos viven en el propio patrón; los dinámicos se pueden seguir editando después de imprimir. Sin periodos de prueba ni códigos desactivados: lo que imprimes hoy se escanea dentro de diez años.</span>

EN: <b>Free to start</b><span>Static codes need no account at all. Dynamic codes — editable, with scan stats — need a free sign-in. No watermark either way.</span>
→  <b>Gratis para empezar</b><span>Los códigos estáticos no necesitan cuenta. Los dinámicos — editables y con estadísticas de escaneos — necesitan un inicio de sesión gratuito. En ningún caso hay marca de agua.</span>

EN: <b>10 languages</b><span>English, Chinese, Spanish, Hindi, Arabic (RTL), Portuguese, French, Russian, German, Japanese.</span>
→  <b>10 idiomas</b><span>Inglés, chino, español, hindi, árabe (RTL), portugués, francés, ruso, alemán, japonés.</span>

EN: <b>Built for print</b><span>High-resolution export and vector SVG, quiet zones respected — made for business cards, menus, and posters.</span>
→  <b>Hecho para imprimir</b><span>Exportación en alta resolución y SVG vectorial, con zonas de silencio respetadas: hecho para tarjetas de visita, menús y carteles.</span>

EN: <b>Agent-friendly</b><span>A free <a href="/developers/">API and MCP server</a> so AI assistants can generate codes too.</span>
→  <b>Amigable con agentes</b><span>Una <a href="/developers/">API y servidor MCP</a> gratuitos para que los asistentes de IA también generen códigos.</span>

EN: Questions, answered
→  Preguntas, respondidas

EN: Almost everything is free. Static codes are completely free, with no watermarks — they are made entirely in your browser and need no account. Dynamic codes need a free sign-in so they can be edited later, and 20 are included free; if you need more, an optional Pro subscription (US$9/month or US$90/year) makes dynamic codes unlimited.
→  Casi todo es gratis. Los códigos estáticos son completamente gratuitos, sin marcas de agua — se crean enteramente en tu navegador y no necesitan cuenta. Los códigos dinámicos necesitan un inicio de sesión gratuito para poder editarlos después, e incluyen 20 gratis; si necesitas más, una suscripción opcional a Pro (9 US$ al mes o 90 US$ al año) hace los códigos dinámicos ilimitados.

EN: Do the QR codes expire?
→  ¿Caducan los códigos QR?

EN: No — neither kind. A static code's destination lives inside the pattern itself, and dynamic codes stay live and editable for as long as your account exists. Details: <a href="/blog/do-qr-codes-expire/">do QR codes expire?</a>
→  No, ninguno de los dos. El destino de un código estático vive dentro del propio patrón, y los códigos dinámicos siguen activos y editables mientras exista tu cuenta. Detalles: <a href="/blog/do-qr-codes-expire/">¿caducan los códigos QR?</a>

EN: Can I use it for my business?
→  ¿Puedo usarlo para mi negocio?

EN: Yes — commercial use is free. Restaurants use it for <a href="/blog/qr-codes-for-restaurants/">menus and reviews</a>, shops for <a href="/google-review-qr-code/">review codes</a> and <a href="/wifi-qr-code/">WiFi codes</a>.
→  Sí: el uso comercial es gratis. Los restaurantes lo usan para <a href="/blog/qr-codes-for-restaurants/">menús y reseñas</a>, las tiendas para <a href="/google-review-qr-code/">códigos de reseña</a> y <a href="/wifi-qr-code/">códigos WiFi</a>.

EN: Who is behind FreeQrly?
→  ¿Quién está detrás de FreeQrly?

EN: An independent maker who got tired of "free" generators that hold your codes hostage behind a trial. The mascot is Qly, a small elephant who appears across the site.
→  Un creador independiente que se cansó de los generadores “gratis” que retienen tus códigos detrás de una prueba. La mascota es Qly, un elefantito que aparece por todo el sitio.

EN: Try the generator →
→  Prueba el generador →

EN: FreeQrly is a free QR code generator that runs entirely in the browser. No sign-up, no tracking, no expiry — static QR codes with optional logos, in 10 languages.
→  FreeQrly es un generador gratuito de códigos QR que funciona por completo en el navegador. Sin registro, sin rastreo, sin caducidad: códigos QR estáticos con logos opcionales, en 10 idiomas.

EN: What is FreeQrly?
→  ¿Qué es FreeQrly?

EN: FreeQrly is a free online QR code generator. It creates static QR codes for links, text, WiFi, vCards, SMS, calls, and locations — entirely in your browser, with no account and no fees.
→  FreeQrly es un generador gratuito de códigos QR en línea. Crea códigos QR estáticos para enlaces, texto, WiFi, vCards, SMS, llamadas y ubicaciones, todo dentro de tu navegador, sin cuenta y sin costos.

EN: Yes — almost everything. Static codes are free with no trial and no watermarks, including logo upload, batch generation, and high-resolution export. Static codes need no account; dynamic codes need a free sign-in and include 20 free, with an optional Pro subscription for unlimited dynamic codes.
→  Sí — casi todo. Los códigos estáticos son gratis, sin prueba y sin marcas de agua, incluyendo subida de logo, generación por lotes y exportación en alta resolución. Los códigos estáticos no necesitan cuenta; los dinámicos necesitan un inicio de sesión gratuito e incluyen 20 gratis, con una suscripción Pro opcional para códigos dinámicos ilimitados.

EN: Do FreeQrly QR codes expire?
→  ¿Caducan los códigos QR de FreeQrly?

EN: No. Static codes encode the destination directly in the pattern, and dynamic codes stay live and editable — neither kind expires or requires a subscription.
→  No. Los códigos estáticos codifican el destino directamente en el patrón, y los dinámicos siguen activos y editables: ninguno de los dos caduca ni requiere suscripción.

EN: Does FreeQrly track my QR codes or my data?
→  ¿FreeQrly rastrea mis códigos QR o mis datos?

EN: Static codes are generated locally in your browser; their content is never uploaded and they have no scan tracking. Dynamic codes count scans — that is what they are for — and their destinations can be changed anytime.
→  Los códigos estáticos se generan localmente en tu navegador; su contenido nunca se sube y no cuentan los escaneos. Los códigos dinámicos sí cuentan escaneos — para eso están — y su destino se puede cambiar en cualquier momento.

EN: What languages does FreeQrly support?
→  ¿Qué idiomas admite FreeQrly?

EN: Ten: English, Chinese, Spanish, Hindi, Arabic (with right-to-left layout), Portuguese, French, Russian, German, and Japanese.
→  Diez: inglés, chino, español, hindi, árabe (con diseño de derecha a izquierda), portugués, francés, ruso, alemán y japonés.


## landing-ticket-qr-code

EN: Free Ticket QR Code Generator | FreeQrly
→  Generador gratuito de códigos QR para entradas | FreeQrly

EN: Create free QR codes for tickets: link to your ticket or check-in page, print one code per ticket with Batch mode, no sign-up for static codes, never expires.
→  Códigos QR gratis para entradas: un código por entrada con el modo lote, sin registro para los estáticos y sin caducidad.

EN: One scan at the door, <span class="hl hl-mint">no ticket queue</span>.
→  Un escaneo en la puerta, <span class="hl hl-mint">sin colas</span>.

EN: Put a QR code on every ticket, poster, and confirmation email. Guests scan at the entrance and land straight on your ticket or check-in page — concerts, conferences, workshops, school events.
→  Pon un código QR en cada entrada, cartel y correo de confirmación. Tus invitados escanean en la entrada y llegan directamente a tu página de entradas o de registro: conciertos, conferencias, talleres, eventos escolares.

EN: <span class="sn">1</span><span><b>Link to your ticket page</b>Your ticketing page, check-in form, or event details — one code, one destination.</span>
→  <span class="sn">1</span><span><b>Enlaza a tu página de entradas</b>Tu página de venta de entradas, formulario de registro o detalles del evento: un código, un destino.</span>

EN: <span class="sn">2</span><span><b>Make the code</b>Paste the link in the studio below. Print-ready PNG or SVG, free, no watermark, no sign-up for static codes.</span>
→  <span class="sn">2</span><span><b>Crea el código</b>Pega el enlace en el estudio de abajo. PNG listo para imprimir o SVG, gratis, sin marca de agua, sin registro para códigos estáticos.</span>

EN: <span class="sn">3</span><span><b>One code per ticket, with Batch</b>Need a different code on every ticket? Batch mode takes one link per line and downloads every code as a ZIP.</span>
→  <span class="sn">3</span><span><b>Un código por entrada, con el modo lote</b>¿Necesitas un código distinto en cada entrada? El modo lote toma un enlace por línea y descarga todos los códigos en un ZIP.</span>

EN: <span>What should a ticket QR code link to?</span>
→  <span>¿A qué debe enlazar un código QR de entradas?</span>

EN: Your ticket page, a check-in form, or the event details page. The code simply opens that page on the guest’s phone — keep the page itself as the source of truth for entry.
→  A tu página de entradas, un formulario de registro o la página de detalles del evento. El código simplemente abre esa página en el teléfono del invitado: mantén la página misma como la referencia para el acceso.

EN: <span>Can I make a different code for every ticket?</span>
→  <span>¿Puedo crear un código distinto para cada entrada?</span>

EN: Yes — Batch mode generates one code per link: paste one ticket link per line, download them all as a ZIP, and print each on its own ticket.
→  Sí: el modo lote genera un código por enlace: pega un enlace de entrada por línea, descarga todos en un ZIP e imprime cada uno en su propia entrada.

EN: <span>Do ticket QR codes expire?</span>
→  <span>¿Los códigos QR de entradas caducan?</span>

EN: No. Static codes never expire. If the event moves, point the page behind the code at the new details — or, with a dynamic code, repoint the code itself without reprinting.
→  No. Los códigos estáticos nunca caducan. Si el evento cambia de lugar, apunta la página detrás del código a los nuevos detalles o, con un código dinámico, redirige el código mismo sin reimprimir.

EN: <span>How big should I print it on a ticket?</span>
→  <span>¿A qué tamaño debo imprimirlo en una entrada?</span>

EN: At least 2 × 2 cm with a clear quiet margin, at 1024 px export or higher. At a busy entrance, bigger is safer — a code that scans first try keeps the line moving.
→  Al menos 2 × 2 cm con una zona de silencio despejada, con exportación a 1024 px o más. En una entrada concurrida, más grande es más seguro: un código que escanea a la primera mantiene la cola en movimiento.

EN: FreeQrly — qr code ticket
→  FreeQrly — código QR para entradas

EN: What should a ticket QR code link to?
→  ¿A qué debe enlazar un código QR de entradas?

EN: Can I make a different code for every ticket?
→  ¿Puedo crear un código distinto para cada entrada?

EN: Do ticket QR codes expire?
→  ¿Los códigos QR de entradas caducan?

EN: How big should I print it on a ticket?
→  ¿A qué tamaño debo imprimirlo en una entrada?

EN: Make your ticket QR code
→  Crea tu código QR para entradas

EN: Link to your ticket page
→  Enlaza a tu página de entradas

EN: Your ticketing page, check-in form, or event details — one code, one destination.
→  Tu página de venta de entradas, formulario de registro o detalles del evento: un código, un destino.

EN: Paste the link in the studio below. Print-ready PNG or SVG, free, no watermark, no sign-up for static codes.
→  Pega el enlace en el estudio de abajo. PNG listo para imprimir o SVG, gratis, sin marca de agua, sin registro para códigos estáticos.

EN: One code per ticket, with Batch
→  Un código por entrada, con el modo lote

EN: Need a different code on every ticket? Batch mode takes one link per line and downloads every code as a ZIP.
→  ¿Necesitas un código distinto en cada entrada? El modo lote toma un enlace por línea y descarga todos los códigos en un ZIP.
