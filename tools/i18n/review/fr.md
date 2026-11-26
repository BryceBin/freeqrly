# fr


## landing-app-store-qr-code

EN: App Store QR Code Generator: One Code Per Store | FreeQrly
→  QR code App Store : un code par boutique | FreeQrly

EN: Make a QR code for your App Store or Google Play link. A static code holds one URL, so iOS and Android are two codes — here is how to print the right one.
→  Créez un QR code pour votre lien App Store ou Google Play. Un code statique ne contient qu’une URL : iOS et Android, c’est deux codes. Voici lequel imprimer.

EN: Your app link, <span class="hl hl-honey">printed right</span>.
→  Votre lien d’app, <span class="hl hl-honey">imprimé comme il faut</span>.

EN: A static QR code stores one URL, so your App Store listing and your Play listing need one code each. Fill in a link, print it at a size that scans, and put the right code in front of the right phone.
→  Un QR code statique ne stocke qu’une URL : votre fiche App Store et votre fiche Play ont donc besoin d’un code chacune. Collez un lien, imprimez-le à une taille qui se scanne et placez le bon code devant le bon téléphone.

EN: <span class="sn">1</span><span><b>Copy one store link</b>App Store from App Store Connect, Play from the Play Console. One link per code — fill the App Store field for iOS, the Google Play field for Android.</span>
→  <span class="sn">1</span><span><b>Copiez un lien de boutique</b>App Store depuis App Store Connect, Play depuis la Play Console. Un lien par code — remplissez le champ App Store pour iOS, le champ Google Play pour Android.</span>

EN: <span class="sn">2</span><span><b>Paste it in</b>Your code appears instantly. Leave the other field empty unless you are making a second code.</span>
→  <span class="sn">2</span><span><b>Collez-le</b>Votre code apparaît aussitôt. Laissez l’autre champ vide, sauf si vous créez un second code.</span>

EN: <span class="sn">3</span><span><b>Label it and print</b>“iPhone” or “Android” next to the code, at 2 cm or larger. Ads, packaging, receipts, launch slides.</span>
→  <span class="sn">3</span><span><b>Étiquetez et imprimez</b>« iPhone » ou « Android » à côté du code, sur au moins 2 cm. Pubs, emballages, tickets, visuels de lancement.</span>

EN: One static code holds one link
→  Un code statique, un lien

EN: This is the part most app-store QR pages skip, so here it is plainly: a QR code stores text, and that text is a URL. One code, one destination. There is no logic inside the pattern that can look at the phone and pick a store.
→  C’est le point que la plupart des pages de QR code pour l’App Store passent sous silence, alors disons-le clairement : un QR code stocke du texte, et ce texte est une URL. Un code, une destination. Il n’y a aucune logique dans le motif qui puisse regarder le téléphone et choisir une boutique.

EN: That matters because your iOS and Android listings are two different URLs. A single static code can only point at one of them. If you encode the App Store link, Android users land on a page for an app they can't install, and the reverse is just as bad.
→  Cela compte parce que vos fiches iOS et Android sont deux URL différentes. Un seul code statique ne peut pointer que vers l’une des deux. Si vous encodez le lien App Store, les utilisateurs Android atterrissent sur la page d’une app qu’ils ne peuvent pas installer, et l’inverse est tout aussi mauvais.

EN: You have three ways to cover both platforms. The table below compares them.
→  Trois approches permettent de couvrir les deux plateformes. Le tableau ci-dessous les compare.

EN: Approach
→  Approche

EN: Printed codes
→  Codes imprimés

EN: Works if a link changes
→  Fonctionne si un lien change

EN: Setup
→  Mise en place

EN: Two codes, side by side
→  Deux codes côte à côte

EN: one App Store, one Play
→  un App Store, un Play

EN: no, reprint
→  non, réimpression

EN: none
→  aucune

EN: One code to a router page
→  Un code vers une page de redirection

EN: page reads the device, forwards to the right store
→  la page détecte l’appareil et renvoie vers la bonne boutique

EN: yes, if the page is dynamic
→  oui, si la page est dynamique

EN: a page you control
→  une page que vous contrôlez

EN: Store smart banner
→  Bannière intelligente du store

EN: Apple and Google banners on your own site
→  Bannières Apple et Google sur votre propre site

EN: 1 (to your site)
→  1 (vers votre site)

EN: a website
→  un site web

EN: Two codes is the honest, zero-effort option. Router page is what most apps do once they have a marketing site. Smart banners only work if people land on your site first, which is a different job from a printed code.
→  Deux codes, c’est l’option honnête et sans effort. La page de redirection, c’est ce que font la plupart des apps une fois qu’elles ont un site marketing. Les bannières intelligentes ne marchent que si les gens arrivent d’abord sur votre site, ce qui n’est pas le même travail qu’un code imprimé.

EN: How to get your store links
→  Comment récupérer vos liens de store

EN: Both stores give you a clean, permanent URL, and both are easy to find once you know where to look.
→  Les deux stores vous donnent une URL propre et permanente, et les deux sont faciles à trouver quand on sait où regarder.

EN: For iOS, open your app in App Store Connect, go to App Information, and copy the App Store URL. It looks like <code>apps.apple.com/app/id1234567890</code>. You can add a country segment — <code>apps.apple.com/gb/app/id…</code> — if you want the code to open a specific storefront, but the plain version redirects to the visitor's own region, which is usually what you want.
→  Pour iOS, ouvrez votre app dans App Store Connect, allez dans Informations sur l’app et copiez l’URL App Store. Elle ressemble à <code>apps.apple.com/app/id1234567890</code>. Vous pouvez ajouter un segment de pays — <code>apps.apple.com/gb/app/id…</code> — si vous voulez que le code ouvre une vitrine précise, mais la version simple redirige vers la région du visiteur, ce qui est généralement ce que vous voulez.

EN: For Android, open the Play Console listing and copy the link from the browser bar. It looks like <code>play.google.com/store/apps/details?id=com.yourcompany.yourapp</code>. The <code>id</code> is your package name, and it never changes even when the app name does.
→  Pour Android, ouvrez la fiche dans la Play Console et copiez le lien depuis la barre d’adresse. Il ressemble à <code>play.google.com/store/apps/details?id=com.yourcompany.yourapp</code>. L’<code>id</code> est votre nom de package, et il ne change jamais, même quand le nom de l’app change.

EN: Drop anything after the ID. Marketing tools often append tracking parameters like <code>?mt=8</code> or <code>&referrer=…</code>. They're harmless, but they make the QR pattern denser for no benefit, and a denser pattern is harder to print small.
→  Supprimez tout ce qui suit l’ID. Les outils marketing ajoutent souvent des paramètres de suivi comme <code>?mt=8</code> ou <code>&referrer=…</code>. Ils sont inoffensifs, mais ils densifient le motif QR sans aucun bénéfice, et un motif plus dense est plus difficile à imprimer en petit.

EN: Building a router page that works
→  Créer une page de redirection qui fonctionne

EN: If you go with one code, it needs somewhere to send people. A router page is a small page on your own domain that reads the user agent and forwards.
→  Si vous optez pour un seul code, il lui faut une destination. Une page de redirection est une petite page sur votre propre domaine qui lit l’agent utilisateur et redirige.

EN: The logic is short: if the browser reports an iPhone or iPad, go to the App Store; if it reports Android, go to Play; otherwise show both buttons. Keep a fallback for desktop, because a meaningful share of scans come from people testing on a laptop.
→  La logique est courte : si le navigateur signale un iPhone ou un iPad, direction l’App Store ; s’il signale Android, direction Play ; sinon, affichez les deux boutons. Prévoyez un repli pour ordinateur, car une part non négligeable des scans vient de gens qui testent sur un ordinateur portable.

EN: Two things break these pages in practice. Apple's in-app browsers and some social apps strip the user agent down to something generic, so the detection guesses wrong. And a redirect that fires before the page renders can look like a broken link. Showing both buttons with the detected one highlighted is more forgiving than an instant forward.
→  Deux choses cassent ces pages en pratique. Les navigateurs intégrés d’Apple et certaines apps sociales réduisent l’agent utilisateur à quelque chose de générique, et la détection se trompe. Et une redirection déclenchée avant le rendu de la page peut ressembler à un lien cassé. Afficher les deux boutons en mettant en avant celui qui a été détecté est plus robuste qu’un renvoi immédiat.

EN: If you want the destination editable later, use a dynamic code pointing at the router page. Change the page and every printed code follows, no reprint.
→  Si vous voulez pouvoir modifier la destination plus tard, utilisez un code dynamique pointant vers la page de redirection. Changez la page et tous les codes imprimés suivent, sans réimpression.

EN: App launch slide
→  Slide de lancement

EN: 8 cm
→  8 cm

EN: scanned from a seat, 1–2 m away
→  scanné depuis son siège, à 1–2 m

EN: Packaging and inserts
→  Emballages et encarts

EN: one code per platform, clearly labelled
→  un code par plateforme, clairement étiqueté

EN: Receipt footer
→  Bas de ticket

EN: thermal printers blur thin lines; test first
→  les imprimantes thermiques brouillent les traits fins ; testez d’abord

EN: Poster or ad
→  Affiche ou pub

EN: scanned from 2–3 m
→  scanné à 2–3 m

EN: only if you print two codes with labels
→  uniquement si vous imprimez deux codes étiquetés

EN: When you print two codes, label them. A pair of identical-looking squares with no "iPhone" and "Android" text is worse than one code, because people scan the wrong one and land on a store they can't use.
→  Quand vous imprimez deux codes, étiquetez-les. Deux carrés identiques sans mention « iPhone » et « Android » sont pires qu’un seul code : les gens scannent le mauvais et atterrissent sur un store inutilisable pour eux.

EN: <span>Can one static code open both stores?</span>
→  <span>Un code statique peut-il ouvrir les deux boutiques ?</span>

EN: No. A static code stores a single URL, and your two store listings are two URLs. Encode the App Store link and Android visitors land on an app they cannot install. Print two labelled codes, or point one code at a page on your own domain that reads the phone and forwards to the right store.
→  Non. Un code statique stocke une seule URL, et vos deux fiches de boutique sont deux URL. Si vous encodez le lien App Store, les visiteurs Android atterrissent sur une app qu’ils ne peuvent pas installer. Imprimez deux codes étiquetés, ou faites pointer un code vers une page de votre domaine qui détecte le téléphone et redirige vers la bonne boutique.

EN: <span>What if I fill in both fields?</span>
→  <span>Et si je remplis les deux champs ?</span>

EN: Only the App Store link is encoded — the Play field is used when the App Store field is empty. To cover both platforms, make two codes, one per field.
→  Seul le lien App Store est encodé — le champ Play sert quand le champ App Store est vide. Pour couvrir les deux plateformes, créez deux codes, un par champ.

EN: <span>What if I only have one platform?</span>
→  <span>Et si je n'ai qu'une plateforme ?</span>

EN: Fill that field and print one code. Nothing else is needed.
→  Remplissez ce champ et imprimez un code. Rien d’autre n’est nécessaire.

EN: <span>Can it detect the phone and route automatically?</span>
→  <span>Détecte-t-il le téléphone et redirige-t-il automatiquement ?</span>

EN: Not on its own — a printed pattern cannot run logic. Device detection needs a page in between: host a small router page, then point a dynamic code at it so you can change the destination later without reprinting.
→  Pas tout seul — un motif imprimé ne peut pas exécuter de logique. La détection d’appareil demande une page intermédiaire : hébergez une petite page de redirection, puis faites pointer un code dynamique dessus pour pouvoir changer la destination plus tard sans réimprimer.

EN: <span>Does it track installs?</span>
→  <span>Compte-t-il les installations ?</span>

EN: No. Static codes carry only the link and never phone home. App Store Connect and the Play Console already report installs.
→  Non. Les codes statiques ne contiennent que le lien et ne renvoient jamais rien. App Store Connect et la Play Console indiquent déjà les installations.

EN: FreeQrly — app store qr code generator
→  FreeQrly — générateur de QR code App Store

EN: Can one static code open both stores?
→  Un code statique peut-il ouvrir les deux boutiques ?

EN: What if I fill in both fields?
→  Et si je remplis les deux champs ?

EN: What if I only have one platform?
→  Et si je n'ai qu'une plateforme ?

EN: Can it detect the phone and route automatically?
→  Détecte-t-il le téléphone et redirige-t-il automatiquement ?

EN: Does it track installs?
→  Compte-t-il les installations ?

EN: Make your app store QR code
→  Créez votre QR code App Store

EN: Copy one store link
→  Copiez un lien de boutique

EN: App Store from App Store Connect, Play from the Play Console. One link per code — fill the App Store field for iOS, the Google Play field for Android.
→  App Store depuis App Store Connect, Play depuis la Play Console. Un lien par code — remplissez le champ App Store pour iOS, le champ Google Play pour Android.

EN: Paste it in
→  Collez-le

EN: Your code appears instantly. Leave the other field empty unless you are making a second code.
→  Votre code apparaît aussitôt. Laissez l’autre champ vide, sauf si vous créez un second code.

EN: Label it and print
→  Étiquetez et imprimez

EN: “iPhone” or “Android” next to the code, at 2 cm or larger. Ads, packaging, receipts, launch slides.
→  « iPhone » ou « Android » à côté du code, sur au moins 2 cm. Pubs, emballages, tickets, visuels de lancement.


## about

EN: About FreeQrly — Free Static QR Codes, No Sign-Up, No Expiry
→  À propos de FreeQrly — QR codes gratuits, sans inscription

EN: FreeQrly is a free QR code generator: static codes run 100% in your browser — no sign-up, no tracking, no expiry. Learn what it is and how it works.
→  FreeQrly est un générateur de QR code gratuit : les codes statiques fonctionnent à 100 % dans votre navigateur, sans inscription, sans suivi, sans expiration.

EN: About FreeQrly
→  À propos de FreeQrly

EN: A free QR code generator: static codes run 100% in your browser — no sign-up, no tracking, no expiry.
→  Un générateur de QR code gratuit : les codes statiques fonctionnent à 100 % dans votre navigateur — sans inscription, sans suivi, sans expiration.

EN: Qly protecting your privacy with a shield
→  Qly protégeant votre vie privée avec un bouclier

EN: About
→  À propos

EN: What is <span class="hl hl-mint">FreeQrly</span>?
→  Qu’est-ce que <span class="hl hl-mint">FreeQrly</span> ?

EN: FreeQrly is a free QR code generator with a simple idea: the tool should live in your browser, not on somebody's server. You type, it draws — nothing is uploaded, tracked, or billed.
→  FreeQrly est un générateur de QR code gratuit avec une idée simple : l’outil doit vivre dans votre navigateur, pas sur le serveur de quelqu’un d’autre. Vous tapez, il dessine — rien n’est téléversé, suivi ni facturé.

EN: <b>100% browser-based</b><span>Every code is drawn locally with JavaScript. Your links, contacts, and WiFi passwords never leave your device.</span>
→  <b>100 % dans le navigateur</b><span>Chaque code est dessiné localement avec JavaScript. Vos liens, contacts et mots de passe WiFi ne quittent jamais votre appareil.</span>

EN: <b>Codes that never expire</b><span>Static codes live in the pattern itself; dynamic codes stay editable after printing. No trials, no deactivated codes — what you print today scans in ten years.</span>
→  <b>Des codes qui n’expirent jamais</b><span>Les codes statiques vivent dans le motif lui-même ; les codes dynamiques restent modifiables après impression. Pas d’essai, pas de code désactivé — ce que vous imprimez aujourd’hui se scannera dans dix ans.</span>

EN: <b>Free to start</b><span>Static codes need no account at all. Dynamic codes — editable, with scan stats — need a free sign-in. No watermark either way.</span>
→  <b>Gratuit pour commencer</b><span>Les codes statiques ne demandent aucun compte. Les codes dynamiques — modifiables, avec des statistiques de scans — demandent une connexion gratuite. Pas de filigrane dans un cas comme dans l’autre.</span>

EN: <b>10 languages</b><span>English, Chinese, Spanish, Hindi, Arabic (RTL), Portuguese, French, Russian, German, Japanese.</span>
→  <b>10 langues</b><span>Anglais, chinois, espagnol, hindi, arabe (RTL), portugais, français, russe, allemand, japonais.</span>

EN: <b>Built for print</b><span>High-resolution export and vector SVG, quiet zones respected — made for business cards, menus, and posters.</span>
→  <b>Pensé pour l’impression</b><span>Export haute résolution et SVG vectoriel, zones de silence respectées — fait pour les cartes de visite, les menus et les affiches.</span>

EN: <b>Agent-friendly</b><span>A free <a href="/developers/">API and MCP server</a> so AI assistants can generate codes too.</span>
→  <b>Pensé pour les agents</b><span>Une <a href="/developers/">API et un serveur MCP gratuits</a> pour que les assistants IA puissent aussi générer des codes.</span>

EN: Questions, answered
→  Questions, réponses

EN: Almost everything is free. Static codes are completely free, with no watermarks — they are made entirely in your browser and need no account. Dynamic codes need a free sign-in so they can be edited later, and 20 are included free; if you need more, an optional Pro subscription (US$9/month or US$90/year) makes dynamic codes unlimited.
→  Presque tout est gratuit. Les codes statiques sont entièrement gratuits, sans filigrane — ils sont créés entièrement dans votre navigateur et ne nécessitent aucun compte. Les codes dynamiques nécessitent une connexion gratuite pour pouvoir être modifiés ultérieurement, et 20 sont inclus gratuitement ; si vous en avez besoin de plus, un abonnement Pro facultatif (9 $ US par mois ou 90 $ US par an) rend les codes dynamiques illimités.

EN: Do the QR codes expire?
→  Les QR codes expirent-ils ?

EN: No — neither kind. A static code's destination lives inside the pattern itself, and dynamic codes stay live and editable for as long as your account exists. Details: <a href="/blog/do-qr-codes-expire/">do QR codes expire?</a>
→  Non — ni l’un ni l’autre. La destination d’un code statique vit dans le motif lui-même, et les codes dynamiques restent actifs et modifiables tant que votre compte existe. Détails : <a href="/blog/do-qr-codes-expire/">les QR codes expirent-ils ?</a>

EN: Can I use it for my business?
→  Puis-je l’utiliser pour mon entreprise ?

EN: Yes — commercial use is free. Restaurants use it for <a href="/blog/qr-codes-for-restaurants/">menus and reviews</a>, shops for <a href="/google-review-qr-code/">review codes</a> and <a href="/wifi-qr-code/">WiFi codes</a>.
→  Oui — l’usage commercial est gratuit. Les restaurants l’utilisent pour <a href="/blog/qr-codes-for-restaurants/">les menus et les avis</a>, les boutiques pour <a href="/google-review-qr-code/">les codes d’avis</a> et <a href="/wifi-qr-code/">les codes WiFi</a>.

EN: Who is behind FreeQrly?
→  Qui est derrière FreeQrly ?

EN: An independent maker who got tired of "free" generators that hold your codes hostage behind a trial. The mascot is Qly, a small elephant who appears across the site.
→  Un créateur indépendant fatigué des générateurs « gratuits » qui retiennent vos codes en otage derrière un essai. La mascotte est Qly, un petit éléphant qui apparaît partout sur le site.

EN: Try the generator →
→  Essayer le générateur →

EN: FreeQrly is a free QR code generator that runs entirely in the browser. No sign-up, no tracking, no expiry — static QR codes with optional logos, in 10 languages.
→  FreeQrly est un générateur de QR code gratuit qui fonctionne entièrement dans le navigateur. Sans inscription, sans suivi, sans expiration — des QR codes statiques avec logos optionnels, en 10 langues.

EN: What is FreeQrly?
→  Qu’est-ce que FreeQrly ?

EN: FreeQrly is a free online QR code generator. It creates static QR codes for links, text, WiFi, vCards, SMS, calls, and locations — entirely in your browser, with no account and no fees.
→  FreeQrly est un générateur de QR code en ligne gratuit. Il crée des QR codes statiques pour liens, texte, WiFi, vCards, SMS, appels et lieux — entièrement dans votre navigateur, sans compte et sans frais.

EN: Yes — almost everything. Static codes are free with no trial and no watermarks, including logo upload, batch generation, and high-resolution export. Static codes need no account; dynamic codes need a free sign-in and include 20 free, with an optional Pro subscription for unlimited dynamic codes.
→  Oui — presque tout. Les codes statiques sont gratuits, sans essai et sans filigrane, y compris l'ajout de logo, la génération par lots et l'export haute résolution. Les codes statiques ne nécessitent aucun compte ; les codes dynamiques nécessitent une connexion gratuite et incluent 20 codes gratuits, avec un abonnement Pro facultatif pour des codes dynamiques illimités.

EN: Do FreeQrly QR codes expire?
→  Les QR codes FreeQrly expirent-ils ?

EN: No. Static codes encode the destination directly in the pattern, and dynamic codes stay live and editable — neither kind expires or requires a subscription.
→  Non. Les codes statiques encodent la destination directement dans le motif, et les codes dynamiques restent actifs et modifiables — ni les uns ni les autres n’expirent ni ne nécessitent d’abonnement.

EN: Does FreeQrly track my QR codes or my data?
→  FreeQrly suit-il mes QR codes ou mes données ?

EN: Static codes are generated locally in your browser; their content is never uploaded and they have no scan tracking. Dynamic codes count scans — that is what they are for — and their destinations can be changed anytime.
→  Les codes statiques sont générés localement dans votre navigateur ; leur contenu n’est jamais téléversé et ils ne comptent pas les scans. Les codes dynamiques comptent les scans — c’est leur rôle — et leur destination peut être changée à tout moment.

EN: What languages does FreeQrly support?
→  Quelles langues FreeQrly prend-il en charge ?

EN: Ten: English, Chinese, Spanish, Hindi, Arabic (with right-to-left layout), Portuguese, French, Russian, German, and Japanese.
→  Dix : anglais, chinois, espagnol, hindi, arabe (avec mise en page de droite à gauche), portugais, français, russe, allemand et japonais.


## landing-ticket-qr-code

EN: Free Ticket QR Code Generator | FreeQrly
→  Générateur de QR code pour billets, gratuit | FreeQrly

EN: Create free QR codes for tickets: link to your ticket or check-in page, print one code per ticket with Batch mode, no sign-up for static codes, never expires.
→  QR codes gratuits pour vos billets : un code par billet avec le mode lot, sans inscription pour les codes statiques et sans expiration.

EN: One scan at the door, <span class="hl hl-mint">no ticket queue</span>.
→  Un scan à l'entrée, <span class="hl hl-mint">pas de file d'attente</span>.

EN: Put a QR code on every ticket, poster, and confirmation email. Guests scan at the entrance and land straight on your ticket or check-in page — concerts, conferences, workshops, school events.
→  Mettez un QR code sur chaque billet, affiche et e-mail de confirmation. Les invités scannent à l'entrée et arrivent directement sur votre page de billet ou d'enregistrement — concerts, conférences, ateliers, événements scolaires.

EN: <span class="sn">1</span><span><b>Link to your ticket page</b>Your ticketing page, check-in form, or event details — one code, one destination.</span>
→  <span class="sn">1</span><span><b>Pointez vers votre page de billet</b>Votre page de billetterie, formulaire d'enregistrement ou détails de l'événement — un code, une destination.</span>

EN: <span class="sn">2</span><span><b>Make the code</b>Paste the link in the studio below. Print-ready PNG or SVG, free, no watermark, no sign-up for static codes.</span>
→  <span class="sn">2</span><span><b>Créez le code</b>Collez le lien dans le studio ci-dessous. PNG ou SVG prêt à imprimer, gratuit, sans filigrane, sans inscription pour les codes statiques.</span>

EN: <span class="sn">3</span><span><b>One code per ticket, with Batch</b>Need a different code on every ticket? Batch mode takes one link per line and downloads every code as a ZIP.</span>
→  <span class="sn">3</span><span><b>Un code par billet, avec le mode lot</b>Besoin d'un code différent sur chaque billet ? Le mode lot prend un lien par ligne et télécharge tous les codes en ZIP.</span>

EN: <span>What should a ticket QR code link to?</span>
→  <span>Vers quoi un QR code de billet doit-il mener ?</span>

EN: Your ticket page, a check-in form, or the event details page. The code simply opens that page on the guest’s phone — keep the page itself as the source of truth for entry.
→  Votre page de billet, un formulaire d'enregistrement ou la page des détails de l'événement. Le code ouvre simplement cette page sur le téléphone de l'invité — gardez la page elle-même comme référence pour l'entrée.

EN: <span>Can I make a different code for every ticket?</span>
→  <span>Puis-je créer un code différent pour chaque billet ?</span>

EN: Yes — Batch mode generates one code per link: paste one ticket link per line, download them all as a ZIP, and print each on its own ticket.
→  Oui — le mode lot génère un code par lien : collez un lien de billet par ligne, téléchargez-les tous en ZIP, et imprimez chacun sur son propre billet.

EN: <span>Do ticket QR codes expire?</span>
→  <span>Les QR codes de billet expirent-ils ?</span>

EN: No. Static codes never expire. If the event moves, point the page behind the code at the new details — or, with a dynamic code, repoint the code itself without reprinting.
→  Non. Les codes statiques n'expirent jamais. Si l'événement change de lieu, pointez la page derrière le code vers les nouveaux détails — ou, avec un QR code dynamique, redirigez le code lui-même sans réimprimer.

EN: <span>How big should I print it on a ticket?</span>
→  <span>Quelle taille d'impression sur un billet ?</span>

EN: At least 2 × 2 cm with a clear quiet margin, at 1024 px export or higher. At a busy entrance, bigger is safer — a code that scans first try keeps the line moving.
→  Au moins 2 × 2 cm avec une marge de silence nette, en export 1024 px ou plus. À une entrée très fréquentée, plus grand c'est plus sûr — un code qui scanne du premier coup fait avancer la file.

EN: FreeQrly — qr code ticket
→  FreeQrly — QR code pour billet

EN: What should a ticket QR code link to?
→  Vers quoi un QR code de billet doit-il mener ?

EN: Can I make a different code for every ticket?
→  Puis-je créer un code différent pour chaque billet ?

EN: Do ticket QR codes expire?
→  Les QR codes de billet expirent-ils ?

EN: How big should I print it on a ticket?
→  Quelle taille d'impression sur un billet ?

EN: Make your ticket QR code
→  Créez votre QR code de billet

EN: Link to your ticket page
→  Pointez vers votre page de billet

EN: Your ticketing page, check-in form, or event details — one code, one destination.
→  Votre page de billetterie, formulaire d'enregistrement ou détails de l'événement — un code, une destination.

EN: Paste the link in the studio below. Print-ready PNG or SVG, free, no watermark, no sign-up for static codes.
→  Collez le lien dans le studio ci-dessous. PNG ou SVG prêt à imprimer, gratuit, sans filigrane, sans inscription pour les codes statiques.

EN: One code per ticket, with Batch
→  Un code par billet, avec le mode lot

EN: Need a different code on every ticket? Batch mode takes one link per line and downloads every code as a ZIP.
→  Besoin d'un code différent sur chaque billet ? Le mode lot prend un lien par ligne et télécharge tous les codes en ZIP.
