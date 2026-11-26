# de


## landing-app-store-qr-code

EN: App Store QR Code Generator: One Code Per Store | FreeQrly
→  App-Store-QR-Code-Generator: ein Code pro Store | FreeQrly

EN: Make a QR code for your App Store or Google Play link. A static code holds one URL, so iOS and Android are two codes — here is how to print the right one.
→  QR-Code für App Store oder Google Play: Ein statischer Code enthält eine URL – für iOS und Android brauchst du zwei Codes. So druckst du den richtigen.

EN: Your app link, <span class="hl hl-honey">printed right</span>.
→  Dein App-Link, <span class="hl hl-honey">richtig gedruckt</span>.

EN: A static QR code stores one URL, so your App Store listing and your Play listing need one code each. Fill in a link, print it at a size that scans, and put the right code in front of the right phone.
→  Ein statischer QR-Code speichert eine URL – dein App-Store-Eintrag und dein Play-Eintrag brauchen also je einen eigenen Code. Füge einen Link ein, drucke ihn in einer Größe, die sich scannen lässt, und bring den richtigen Code vor das richtige Handy.

EN: <span class="sn">1</span><span><b>Copy one store link</b>App Store from App Store Connect, Play from the Play Console. One link per code — fill the App Store field for iOS, the Google Play field for Android.</span>
→  <span class="sn">1</span><span><b>Einen Store-Link kopieren</b>App Store aus App Store Connect, Play aus der Play Console. Ein Link pro Code — für iOS ins App-Store-Feld, für Android ins Google-Play-Feld.</span>

EN: <span class="sn">2</span><span><b>Paste it in</b>Your code appears instantly. Leave the other field empty unless you are making a second code.</span>
→  <span class="sn">2</span><span><b>Einfügen</b>Dein Code erscheint sofort. Lass das andere Feld leer, außer du erstellst einen zweiten Code.</span>

EN: <span class="sn">3</span><span><b>Label it and print</b>“iPhone” or “Android” next to the code, at 2 cm or larger. Ads, packaging, receipts, launch slides.</span>
→  <span class="sn">3</span><span><b>Beschriften und drucken</b>„iPhone“ oder „Android“ neben den Code, mindestens 2 cm groß. Werbung, Verpackungen, Bons, Launch-Slides.</span>

EN: One static code holds one link
→  Ein statischer Code, ein Link

EN: This is the part most app-store QR pages skip, so here it is plainly: a QR code stores text, and that text is a URL. One code, one destination. There is no logic inside the pattern that can look at the phone and pick a store.
→  Diesen Punkt lassen die meisten App-Store-QR-Seiten weg, deshalb hier ganz klar: Ein QR-Code speichert Text, und dieser Text ist eine URL. Ein Code, ein Ziel. Im Muster steckt keine Logik, die auf das Handy schaut und einen Store auswählt.

EN: That matters because your iOS and Android listings are two different URLs. A single static code can only point at one of them. If you encode the App Store link, Android users land on a page for an app they can't install, and the reverse is just as bad.
→  Das ist wichtig, weil deine iOS- und Android-Einträge zwei verschiedene URLs sind. Ein einzelner statischer Code kann nur auf eine davon zeigen. Kodierst du den App-Store-Link, landen Android-Nutzer auf einer Seite für eine App, die sie nicht installieren können – und umgekehrt ist es genauso schlimm.

EN: You have three ways to cover both platforms. The table below compares them.
→  Es gibt drei Wege, beide Plattformen abzudecken. Die Tabelle unten vergleicht sie.

EN: Approach
→  Ansatz

EN: Printed codes
→  Gedruckte Codes

EN: Works if a link changes
→  Funktioniert bei Linkänderung

EN: Setup
→  Einrichtung

EN: Two codes, side by side
→  Zwei Codes nebeneinander

EN: one App Store, one Play
→  einer für App Store, einer für Play

EN: no, reprint
→  nein, neu drucken

EN: none
→  keine

EN: One code to a router page
→  Ein Code zeigt auf eine Router-Seite

EN: page reads the device, forwards to the right store
→  Seite erkennt das Gerät und leitet an den richtigen Store weiter

EN: yes, if the page is dynamic
→  ja, wenn die Seite dynamisch ist

EN: a page you control
→  eine Seite, die du kontrollierst

EN: Store smart banner
→  Smart-Banner der App-Stores

EN: Apple and Google banners on your own site
→  Apple- und Google-Banner auf deiner eigenen Website

EN: 1 (to your site)
→  1 (auf deine Website)

EN: a website
→  eine Website

EN: Two codes is the honest, zero-effort option. Router page is what most apps do once they have a marketing site. Smart banners only work if people land on your site first, which is a different job from a printed code.
→  Zwei Codes sind die ehrliche Variante ohne Aufwand. Eine Router-Seite ist das, was die meisten Apps machen, sobald sie eine Marketing-Website haben. Smart-Banner funktionieren nur, wenn die Leute zuerst auf deiner Website landen – das ist eine andere Aufgabe als ein gedruckter Code.

EN: How to get your store links
→  So kommst du an deine Store-Links

EN: Both stores give you a clean, permanent URL, and both are easy to find once you know where to look.
→  Beide Stores geben dir eine saubere, dauerhafte URL, und beide sind leicht zu finden, wenn du weißt, wo du schauen musst.

EN: For iOS, open your app in App Store Connect, go to App Information, and copy the App Store URL. It looks like <code>apps.apple.com/app/id1234567890</code>. You can add a country segment — <code>apps.apple.com/gb/app/id…</code> — if you want the code to open a specific storefront, but the plain version redirects to the visitor's own region, which is usually what you want.
→  Öffne für iOS deine App in App Store Connect, geh zu „App-Informationen“ und kopiere die App-Store-URL. Sie sieht so aus: <code>apps.apple.com/app/id1234567890</code>. Du kannst ein Länderkürzel ergänzen — <code>apps.apple.com/gb/app/id…</code> —, wenn der Code einen bestimmten Store öffnen soll. Die einfache Version leitet aber in die Region des Besuchers weiter, und das willst du meistens.

EN: For Android, open the Play Console listing and copy the link from the browser bar. It looks like <code>play.google.com/store/apps/details?id=com.yourcompany.yourapp</code>. The <code>id</code> is your package name, and it never changes even when the app name does.
→  Öffne für Android den Eintrag in der Play Console und kopiere den Link aus der Adressleiste. Er sieht so aus: <code>play.google.com/store/apps/details?id=com.yourcompany.yourapp</code>. Die <code>id</code> ist dein Paketname, und der ändert sich nie, auch wenn sich der App-Name ändert.

EN: Drop anything after the ID. Marketing tools often append tracking parameters like <code>?mt=8</code> or <code>&referrer=…</code>. They're harmless, but they make the QR pattern denser for no benefit, and a denser pattern is harder to print small.
→  Lass alles nach der ID weg. Marketing-Tools hängen oft Tracking-Parameter an wie <code>?mt=8</code> oder <code>&referrer=…</code>. Die sind harmlos, machen das QR-Muster aber ohne Nutzen dichter, und ein dichteres Muster lässt sich schlechter klein drucken.

EN: Building a router page that works
→  Eine Router-Seite bauen, die funktioniert

EN: If you go with one code, it needs somewhere to send people. A router page is a small page on your own domain that reads the user agent and forwards.
→  Wenn du dich für einen Code entscheidest, braucht er ein Ziel. Eine Router-Seite ist eine kleine Seite auf deiner eigenen Domain, die den User-Agent liest und weiterleitet.

EN: The logic is short: if the browser reports an iPhone or iPad, go to the App Store; if it reports Android, go to Play; otherwise show both buttons. Keep a fallback for desktop, because a meaningful share of scans come from people testing on a laptop.
→  Die Logik ist kurz: Meldet der Browser ein iPhone oder iPad, geht es zum App Store; meldet er Android, zu Play; sonst zeigst du beide Buttons. Bau einen Fallback für den Desktop ein, denn ein nicht unerheblicher Teil der Scans kommt von Leuten, die am Laptop testen.

EN: Two things break these pages in practice. Apple's in-app browsers and some social apps strip the user agent down to something generic, so the detection guesses wrong. And a redirect that fires before the page renders can look like a broken link. Showing both buttons with the detected one highlighted is more forgiving than an instant forward.
→  In der Praxis scheitern diese Seiten an zwei Dingen. Apples In-App-Browser und einige Social-Apps reduzieren den User-Agent auf etwas Generisches, dann rät die Erkennung falsch. Und eine Weiterleitung, die losgeht, bevor die Seite gerendert ist, kann wie ein kaputter Link wirken. Beide Buttons zu zeigen und den erkannten hervorzuheben, ist fehlertoleranter als sofort weiterzuleiten.

EN: If you want the destination editable later, use a dynamic code pointing at the router page. Change the page and every printed code follows, no reprint.
→  Wenn du das Ziel später ändern willst, nimm einen dynamischen Code, der auf die Router-Seite zeigt. Ändere die Seite, und alle gedruckten Codes ziehen mit – kein Neudruck.

EN: App launch slide
→  Launch-Slide

⚠️ 未翻译（与英文相同）
EN: 8 cm
→  8 cm

EN: scanned from a seat, 1–2 m away
→  vom Sitz aus 1–2 m gescannt

EN: Packaging and inserts
→  Verpackungen und Beileger

EN: one code per platform, clearly labelled
→  ein Code pro Plattform, klar beschriftet

EN: Receipt footer
→  Kassenbon-Fußzeile

EN: thermal printers blur thin lines; test first
→  Thermodrucker verwischen dünne Linien; vorher testen

EN: Poster or ad
→  Poster oder Anzeige

EN: scanned from 2–3 m
→  aus 2–3 m gescannt

EN: only if you print two codes with labels
→  nur wenn du zwei Codes mit Beschriftung druckst

EN: When you print two codes, label them. A pair of identical-looking squares with no "iPhone" and "Android" text is worse than one code, because people scan the wrong one and land on a store they can't use.
→  Wenn du zwei Codes druckst, beschrifte sie. Zwei gleich aussehende Quadrate ohne die Beschriftung „iPhone“ und „Android“ sind schlimmer als ein Code, weil die Leute den falschen scannen und in einem Store landen, der ihnen nichts bringt.

EN: <span>Can one static code open both stores?</span>
→  <span>Kann ein statischer Code beide Stores öffnen?</span>

EN: No. A static code stores a single URL, and your two store listings are two URLs. Encode the App Store link and Android visitors land on an app they cannot install. Print two labelled codes, or point one code at a page on your own domain that reads the phone and forwards to the right store.
→  Nein. Ein statischer Code speichert eine einzige URL, und deine beiden Store-Einträge sind zwei URLs. Kodierst du den App-Store-Link, landen Android-Besucher bei einer App, die sie nicht installieren können. Druck zwei beschriftete Codes – oder lass einen Code auf eine Seite deiner eigenen Domain zeigen, die das Handy erkennt und an den richtigen Store weiterleitet.

EN: <span>What if I fill in both fields?</span>
→  <span>Was, wenn ich beide Felder ausfülle?</span>

EN: Only the App Store link is encoded — the Play field is used when the App Store field is empty. To cover both platforms, make two codes, one per field.
→  Kodiert wird nur der App-Store-Link — das Play-Feld greift, wenn das App-Store-Feld leer ist. Um beide Plattformen abzudecken, erstellst du zwei Codes, einen pro Feld.

EN: <span>What if I only have one platform?</span>
→  <span>Was, wenn es nur eine Plattform gibt?</span>

EN: Fill that field and print one code. Nothing else is needed.
→  Füll das Feld aus und druck einen Code. Mehr brauchst du nicht.

EN: <span>Can it detect the phone and route automatically?</span>
→  <span>Erkennt er das Handy und leitet automatisch weiter?</span>

EN: Not on its own — a printed pattern cannot run logic. Device detection needs a page in between: host a small router page, then point a dynamic code at it so you can change the destination later without reprinting.
→  Nicht von allein — ein gedrucktes Muster kann keine Logik ausführen. Für die Geräteerkennung braucht es eine Seite dazwischen: Hoste eine kleine Router-Seite und lass einen dynamischen Code darauf zeigen, dann kannst du das Ziel später ändern, ohne neu zu drucken.

EN: <span>Does it track installs?</span>
→  <span>Zählt er Installationen?</span>

EN: No. Static codes carry only the link and never phone home. App Store Connect and the Play Console already report installs.
→  Nein. Statische Codes enthalten nur den Link und senden keine Daten. App Store Connect und die Play Console melden die Installationen ohnehin.

EN: FreeQrly — app store qr code generator
→  FreeQrly — App-Store-QR-Code-Generator

EN: Can one static code open both stores?
→  Kann ein statischer Code beide Stores öffnen?

EN: What if I fill in both fields?
→  Was, wenn ich beide Felder ausfülle?

EN: What if I only have one platform?
→  Was, wenn es nur eine Plattform gibt?

EN: Can it detect the phone and route automatically?
→  Erkennt er das Handy und leitet automatisch weiter?

EN: Does it track installs?
→  Zählt er Installationen?

EN: Make your app store QR code
→  Erstelle deinen App-Store-QR-Code

EN: Copy one store link
→  Einen Store-Link kopieren

EN: App Store from App Store Connect, Play from the Play Console. One link per code — fill the App Store field for iOS, the Google Play field for Android.
→  App Store aus App Store Connect, Play aus der Play Console. Ein Link pro Code — für iOS ins App-Store-Feld, für Android ins Google-Play-Feld.

EN: Paste it in
→  Einfügen

EN: Your code appears instantly. Leave the other field empty unless you are making a second code.
→  Dein Code erscheint sofort. Lass das andere Feld leer, außer du erstellst einen zweiten Code.

EN: Label it and print
→  Beschriften und drucken

EN: “iPhone” or “Android” next to the code, at 2 cm or larger. Ads, packaging, receipts, launch slides.
→  „iPhone“ oder „Android“ neben den Code, mindestens 2 cm groß. Werbung, Verpackungen, Bons, Launch-Slides.


## about

EN: About FreeQrly — Free Static QR Codes, No Sign-Up, No Expiry
→  Über FreeQrly — Kostenlose QR-Codes ohne Anmeldung

EN: FreeQrly is a free QR code generator: static codes run 100% in your browser — no sign-up, no tracking, no expiry. Learn what it is and how it works.
→  FreeQrly ist ein kostenloser QR-Code-Generator: Statische Codes laufen zu 100 % in deinem Browser — ohne Anmeldung, ohne Tracking, ohne Ablauf. Erfahre mehr.

EN: About FreeQrly
→  Über FreeQrly

EN: A free QR code generator: static codes run 100% in your browser — no sign-up, no tracking, no expiry.
→  Ein kostenloser QR-Code-Generator: Statische Codes laufen zu 100 % in deinem Browser — ohne Anmeldung, ohne Tracking, ohne Ablauf.

EN: Qly protecting your privacy with a shield
→  Qly schützt deine Privatsphäre mit einem Schild

EN: About
→  Über uns

EN: What is <span class="hl hl-mint">FreeQrly</span>?
→  Was ist <span class="hl hl-mint">FreeQrly</span>?

EN: FreeQrly is a free QR code generator with a simple idea: the tool should live in your browser, not on somebody's server. You type, it draws — nothing is uploaded, tracked, or billed.
→  FreeQrly ist ein kostenloser QR-Code-Generator mit einer einfachen Idee: Das Tool gehört in deinen Browser, nicht auf dem Server von irgendwem. Du tippst, es zeichnet — nichts wird hochgeladen, getrackt oder abgerechnet.

EN: <b>100% browser-based</b><span>Every code is drawn locally with JavaScript. Your links, contacts, and WiFi passwords never leave your device.</span>
→  <b>100 % im Browser</b><span>Jeder Code wird lokal mit JavaScript gezeichnet. Deine Links, Kontakte und WLAN-Passwörter verlassen nie dein Gerät.</span>

EN: <b>Codes that never expire</b><span>Static codes live in the pattern itself; dynamic codes stay editable after printing. No trials, no deactivated codes — what you print today scans in ten years.</span>
→  <b>Codes, die nie ablaufen</b><span>Statische Codes stecken im Muster selbst; dynamische Codes bleiben nach dem Drucken änderbar. Keine Testphasen, keine deaktivierten Codes — was du heute druckst, scannt in zehn Jahren noch.</span>

EN: <b>Free to start</b><span>Static codes need no account at all. Dynamic codes — editable, with scan stats — need a free sign-in. No watermark either way.</span>
→  <b>Kostenlos starten</b><span>Statische Codes brauchen gar kein Konto. Dynamische Codes — änderbar, mit Scan-Statistiken — brauchen eine kostenlose Anmeldung. Wasserzeichen gibt es in beiden Fällen nicht.</span>

EN: <b>10 languages</b><span>English, Chinese, Spanish, Hindi, Arabic (RTL), Portuguese, French, Russian, German, Japanese.</span>
→  <b>10 Sprachen</b><span>Englisch, Chinesisch, Spanisch, Hindi, Arabisch (RTL), Portugiesisch, Französisch, Russisch, Deutsch, Japanisch.</span>

EN: <b>Built for print</b><span>High-resolution export and vector SVG, quiet zones respected — made for business cards, menus, and posters.</span>
→  <b>Gemacht für den Druck</b><span>Hochauflösender Export und Vektor-SVG, Ruhezonen eingehalten — gemacht für Visitenkarten, Menüs und Poster.</span>

EN: <b>Agent-friendly</b><span>A free <a href="/developers/">API and MCP server</a> so AI assistants can generate codes too.</span>
→  <b>Agent-freundlich</b><span>Eine kostenlose <a href="/developers/">API und ein MCP-Server</a>, damit auch KI-Assistenten Codes erzeugen können.</span>

EN: Questions, answered
→  Fragen, beantwortet

EN: Almost everything is free. Static codes are completely free, with no watermarks — they are made entirely in your browser and need no account. Dynamic codes need a free sign-in so they can be edited later, and 20 are included free; if you need more, an optional Pro subscription (US$9/month or US$90/year) makes dynamic codes unlimited.
→  Fast alles ist kostenlos. Statische Codes sind völlig kostenlos, ohne Wasserzeichen — sie werden komplett in deinem Browser erstellt und brauchen kein Konto. Dynamische Codes brauchen eine kostenlose Anmeldung, damit sie später bearbeitet werden können, und 20 sind kostenlos enthalten; wenn du mehr brauchst, macht ein optionales Pro-Abo (9 US$ pro Monat oder 90 US$ pro Jahr) dynamische Codes unbegrenzt.

EN: Do the QR codes expire?
→  Laufen die QR-Codes ab?

EN: No — neither kind. A static code's destination lives inside the pattern itself, and dynamic codes stay live and editable for as long as your account exists. Details: <a href="/blog/do-qr-codes-expire/">do QR codes expire?</a>
→  Nein — keiner von beiden. Das Ziel eines statischen Codes steckt im Muster selbst, und dynamische Codes bleiben aktiv und änderbar, solange es dein Konto gibt. Details: <a href="/blog/do-qr-codes-expire/">Laufen QR-Codes ab?</a>

EN: Can I use it for my business?
→  Kann ich es für mein Geschäft nutzen?

EN: Yes — commercial use is free. Restaurants use it for <a href="/blog/qr-codes-for-restaurants/">menus and reviews</a>, shops for <a href="/google-review-qr-code/">review codes</a> and <a href="/wifi-qr-code/">WiFi codes</a>.
→  Ja — kommerzielle Nutzung ist kostenlos. Restaurants nutzen es für <a href="/blog/qr-codes-for-restaurants/">Menüs und Bewertungen</a>, Läden für <a href="/google-review-qr-code/">Bewertungs-Codes</a> und <a href="/wifi-qr-code/">WLAN-Codes</a>.

EN: Who is behind FreeQrly?
→  Wer steckt hinter FreeQrly?

EN: An independent maker who got tired of "free" generators that hold your codes hostage behind a trial. The mascot is Qly, a small elephant who appears across the site.
→  Ein unabhängiger Macher, der genug hatte von „kostenlosen“ Generatoren, die deine Codes hinter einer Testphase als Geisel halten. Das Maskottchen ist Qly, ein kleiner Elefant, der überall auf der Seite auftaucht.

EN: Try the generator →
→  Generator ausprobieren →

EN: FreeQrly is a free QR code generator that runs entirely in the browser. No sign-up, no tracking, no expiry — static QR codes with optional logos, in 10 languages.
→  FreeQrly ist ein kostenloser QR-Code-Generator, der vollständig im Browser läuft. Ohne Anmeldung, ohne Tracking, ohne Ablauf — statische QR-Codes mit optionalen Logos, in 10 Sprachen.

EN: What is FreeQrly?
→  Was ist FreeQrly?

EN: FreeQrly is a free online QR code generator. It creates static QR codes for links, text, WiFi, vCards, SMS, calls, and locations — entirely in your browser, with no account and no fees.
→  FreeQrly ist ein kostenloser Online-QR-Code-Generator. Er erstellt statische QR-Codes für Links, Texte, WLAN, vCards, SMS, Anrufe und Orte — vollständig in deinem Browser, ohne Konto und ohne Gebühren.

EN: Yes — almost everything. Static codes are free with no trial and no watermarks, including logo upload, batch generation, and high-resolution export. Static codes need no account; dynamic codes need a free sign-in and include 20 free, with an optional Pro subscription for unlimited dynamic codes.
→  Ja — fast alles. Statische Codes sind kostenlos, ohne Testphase und ohne Wasserzeichen, einschließlich Logo-Upload, Batch-Generierung und Export in hoher Auflösung. Statische Codes brauchen kein Konto; dynamische Codes brauchen eine kostenlose Anmeldung und enthalten 20 kostenlose Codes, mit einem optionalen Pro-Abo für unbegrenzt dynamische Codes.

EN: Do FreeQrly QR codes expire?
→  Laufen FreeQrly-QR-Codes ab?

EN: No. Static codes encode the destination directly in the pattern, and dynamic codes stay live and editable — neither kind expires or requires a subscription.
→  Nein. Statische Codes kodieren das Ziel direkt im Muster, und dynamische Codes bleiben aktiv und änderbar — keiner von beiden läuft ab oder braucht ein Abo.

EN: Does FreeQrly track my QR codes or my data?
→  Trackt FreeQrly meine QR-Codes oder meine Daten?

EN: Static codes are generated locally in your browser; their content is never uploaded and they have no scan tracking. Dynamic codes count scans — that is what they are for — and their destinations can be changed anytime.
→  Statische Codes werden lokal in deinem Browser erzeugt; ihre Inhalte werden nie hochgeladen, und sie zählen keine Scans. Dynamische Codes zählen Scans — dafür sind sie da — und ihr Ziel lässt sich jederzeit ändern.

EN: What languages does FreeQrly support?
→  Welche Sprachen unterstützt FreeQrly?

EN: Ten: English, Chinese, Spanish, Hindi, Arabic (with right-to-left layout), Portuguese, French, Russian, German, and Japanese.
→  Zehn: Englisch, Chinesisch, Spanisch, Hindi, Arabisch (mit Rechts-nach-links-Layout), Portugiesisch, Französisch, Russisch, Deutsch und Japanisch.


## landing-ticket-qr-code

EN: Free Ticket QR Code Generator | FreeQrly
→  Kostenloser Ticket-QR-Code-Generator | FreeQrly

EN: Create free QR codes for tickets: link to your ticket or check-in page, print one code per ticket with Batch mode, no sign-up for static codes, never expires.
→  Kostenlose QR-Codes für Tickets: ein Code pro Ticket per Stapelmodus, ohne Anmeldung für statische Codes, laufen nie ab.

EN: One scan at the door, <span class="hl hl-mint">no ticket queue</span>.
→  Ein Scan am Eingang, <span class="hl hl-mint">keine Warteschlange</span>.

EN: Put a QR code on every ticket, poster, and confirmation email. Guests scan at the entrance and land straight on your ticket or check-in page — concerts, conferences, workshops, school events.
→  Setze einen QR-Code auf jedes Ticket, Plakat und jede Bestätigungs-E-Mail. Gäste scannen am Eingang und landen direkt auf deiner Ticket- oder Check-in-Seite – Konzerte, Konferenzen, Workshops, Schulveranstaltungen.

EN: <span class="sn">1</span><span><b>Link to your ticket page</b>Your ticketing page, check-in form, or event details — one code, one destination.</span>
→  <span class="sn">1</span><span><b>Zu deiner Ticket-Seite verlinken</b>Deine Ticketing-Seite, dein Check-in-Formular oder die Veranstaltungsdetails – ein Code, ein Ziel.</span>

EN: <span class="sn">2</span><span><b>Make the code</b>Paste the link in the studio below. Print-ready PNG or SVG, free, no watermark, no sign-up for static codes.</span>
→  <span class="sn">2</span><span><b>Den Code erstellen</b>Link unten im Studio einfügen. Druckfertiges PNG oder SVG, kostenlos, kein Wasserzeichen, keine Anmeldung für statische Codes.</span>

EN: <span class="sn">3</span><span><b>One code per ticket, with Batch</b>Need a different code on every ticket? Batch mode takes one link per line and downloads every code as a ZIP.</span>
→  <span class="sn">3</span><span><b>Ein Code pro Ticket, mit Stapelmodus</b>Brauchst du für jedes Ticket einen anderen Code? Der Stapelmodus nimmt einen Link pro Zeile und lädt jeden Code als ZIP herunter.</span>

EN: <span>What should a ticket QR code link to?</span>
→  <span>Worauf sollte ein Ticket-QR-Code verlinken?</span>

EN: Your ticket page, a check-in form, or the event details page. The code simply opens that page on the guest’s phone — keep the page itself as the source of truth for entry.
→  Deine Ticket-Seite, ein Check-in-Formular oder die Seite mit den Veranstaltungsdetails. Der Code öffnet diese Seite einfach auf dem Smartphone des Gastes – die Seite selbst bleibt die maßgebliche Quelle für den Einlass.

EN: <span>Can I make a different code for every ticket?</span>
→  <span>Kann ich für jedes Ticket einen anderen Code erstellen?</span>

EN: Yes — Batch mode generates one code per link: paste one ticket link per line, download them all as a ZIP, and print each on its own ticket.
→  Ja – der Stapelmodus erzeugt einen Code pro Link: einen Ticket-Link pro Zeile einfügen, alle als ZIP herunterladen und jeden auf sein eigenes Ticket drucken.

EN: <span>Do ticket QR codes expire?</span>
→  <span>Laufen Ticket-QR-Codes ab?</span>

EN: No. Static codes never expire. If the event moves, point the page behind the code at the new details — or, with a dynamic code, repoint the code itself without reprinting.
→  Nein. Statische Codes laufen nie ab. Wenn die Veranstaltung verlegt wird, richte die Seite hinter dem Code auf die neuen Details aus – oder lenke mit einem dynamischen Code den Code selbst um, ohne neu zu drucken.

EN: <span>How big should I print it on a ticket?</span>
→  <span>Wie groß sollte ich ihn auf einem Ticket drucken?</span>

EN: At least 2 × 2 cm with a clear quiet margin, at 1024 px export or higher. At a busy entrance, bigger is safer — a code that scans first try keeps the line moving.
→  Mindestens 2 × 2 cm mit einer klar abgegrenzten Ruhezone, bei einem Export von 1024 px oder mehr. An einem belebten Eingang ist größer sicherer – ein Code, der beim ersten Versuch scannt, hält die Schlange in Bewegung.

EN: FreeQrly — qr code ticket
→  FreeQrly — QR-Code-Ticket

EN: What should a ticket QR code link to?
→  Worauf sollte ein Ticket-QR-Code verlinken?

EN: Can I make a different code for every ticket?
→  Kann ich für jedes Ticket einen anderen Code erstellen?

EN: Do ticket QR codes expire?
→  Laufen Ticket-QR-Codes ab?

EN: How big should I print it on a ticket?
→  Wie groß sollte ich ihn auf einem Ticket drucken?

EN: Make your ticket QR code
→  Erstelle deinen Ticket-QR-Code

EN: Link to your ticket page
→  Zu deiner Ticket-Seite verlinken

EN: Your ticketing page, check-in form, or event details — one code, one destination.
→  Deine Ticketing-Seite, dein Check-in-Formular oder die Veranstaltungsdetails – ein Code, ein Ziel.

EN: Paste the link in the studio below. Print-ready PNG or SVG, free, no watermark, no sign-up for static codes.
→  Link unten im Studio einfügen. Druckfertiges PNG oder SVG, kostenlos, kein Wasserzeichen, keine Anmeldung für statische Codes.

EN: One code per ticket, with Batch
→  Ein Code pro Ticket, mit Batch

EN: Need a different code on every ticket? Batch mode takes one link per line and downloads every code as a ZIP.
→  Brauchst du für jedes Ticket einen anderen Code? Der Stapelmodus nimmt einen Link pro Zeile und lädt jeden Code als ZIP herunter.
