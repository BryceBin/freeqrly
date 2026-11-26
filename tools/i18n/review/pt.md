# pt


## landing-app-store-qr-code

EN: App Store QR Code Generator: One Code Per Store | FreeQrly
→  Gerador de QR code App Store: um código por loja | FreeQrly

EN: Make a QR code for your App Store or Google Play link. A static code holds one URL, so iOS and Android are two codes — here is how to print the right one.
→  Crie um QR code para seu link da App Store ou do Google Play. Um código estático guarda uma URL: iOS e Android são dois códigos, e aqui você vê qual imprimir.

EN: Your app link, <span class="hl hl-honey">printed right</span>.
→  Seu link de app, <span class="hl hl-honey">impresso do jeito certo</span>.

EN: A static QR code stores one URL, so your App Store listing and your Play listing need one code each. Fill in a link, print it at a size that scans, and put the right code in front of the right phone.
→  Um QR code estático guarda uma URL, então sua página da App Store e sua página da Play precisam de um código cada. Cole um link, imprima num tamanho que escaneie e coloque o código certo na frente do telefone certo.

EN: <span class="sn">1</span><span><b>Copy one store link</b>App Store from App Store Connect, Play from the Play Console. One link per code — fill the App Store field for iOS, the Google Play field for Android.</span>
→  <span class="sn">1</span><span><b>Copie um link da loja</b>App Store no App Store Connect, Play no Play Console. Um link por código — preencha o campo App Store para iOS, o campo Google Play para Android.</span>

EN: <span class="sn">2</span><span><b>Paste it in</b>Your code appears instantly. Leave the other field empty unless you are making a second code.</span>
→  <span class="sn">2</span><span><b>Cole</b>Seu código aparece na hora. Deixe o outro campo vazio, a não ser que esteja criando um segundo código.</span>

EN: <span class="sn">3</span><span><b>Label it and print</b>“iPhone” or “Android” next to the code, at 2 cm or larger. Ads, packaging, receipts, launch slides.</span>
→  <span class="sn">3</span><span><b>Etiquete e imprima</b>“iPhone” ou “Android” ao lado do código, com 2 cm ou mais. Anúncios, embalagens, recibos, slides de lançamento.</span>

EN: One static code holds one link
→  Um código estático, um link

EN: This is the part most app-store QR pages skip, so here it is plainly: a QR code stores text, and that text is a URL. One code, one destination. There is no logic inside the pattern that can look at the phone and pick a store.
→  É a parte que quase toda página de QR code para loja de apps pula, então vai direto: um QR code guarda texto, e esse texto é uma URL. Um código, um destino. Não existe lógica dentro do padrão que consiga olhar o telefone e escolher uma loja.

EN: That matters because your iOS and Android listings are two different URLs. A single static code can only point at one of them. If you encode the App Store link, Android users land on a page for an app they can't install, and the reverse is just as bad.
→  Isso importa porque suas páginas de iOS e Android são duas URLs diferentes. Um único código estático só pode apontar para uma delas. Se você codificar o link da App Store, usuários de Android caem na página de um app que não podem instalar, e o contrário é igualmente ruim.

EN: You have three ways to cover both platforms. The table below compares them.
→  Você tem três caminhos para cobrir as duas plataformas. A tabela abaixo compara.

EN: Approach
→  Abordagem

EN: Printed codes
→  Códigos impressos

EN: Works if a link changes
→  Funciona se um link mudar

EN: Setup
→  Configuração

EN: Two codes, side by side
→  Dois códigos, lado a lado

EN: one App Store, one Play
→  um da App Store, um da Play

EN: no, reprint
→  não, reimprimir

EN: none
→  nenhuma

EN: One code to a router page
→  Um código para uma página de redirecionamento

EN: page reads the device, forwards to the right store
→  a página detecta o aparelho e encaminha para a loja certa

EN: yes, if the page is dynamic
→  sim, se a página for dinâmica

EN: a page you control
→  uma página que você controla

EN: Store smart banner
→  Banner inteligente da loja

EN: Apple and Google banners on your own site
→  Banners da Apple e do Google no seu próprio site

EN: 1 (to your site)
→  1 (para o seu site)

EN: a website
→  um site

EN: Two codes is the honest, zero-effort option. Router page is what most apps do once they have a marketing site. Smart banners only work if people land on your site first, which is a different job from a printed code.
→  Dois códigos são a opção honesta e sem esforço. A página de redirecionamento é o que a maioria dos apps faz quando já tem um site de marketing. Banners inteligentes só funcionam se as pessoas chegarem primeiro ao seu site, o que é um trabalho diferente de um código impresso.

EN: How to get your store links
→  Como conseguir seus links da loja

EN: Both stores give you a clean, permanent URL, and both are easy to find once you know where to look.
→  As duas lojas oferecem uma URL limpa e permanente, e as duas são fáceis de achar quando você sabe onde olhar.

EN: For iOS, open your app in App Store Connect, go to App Information, and copy the App Store URL. It looks like <code>apps.apple.com/app/id1234567890</code>. You can add a country segment — <code>apps.apple.com/gb/app/id…</code> — if you want the code to open a specific storefront, but the plain version redirects to the visitor's own region, which is usually what you want.
→  Para iOS, abra seu app no App Store Connect, vá em Informações do App e copie a URL da App Store. Ela se parece com <code>apps.apple.com/app/id1234567890</code>. Você pode adicionar um segmento de país — <code>apps.apple.com/gb/app/id…</code> — se quiser que o código abra uma loja específica, mas a versão simples redireciona para a região do visitante, o que normalmente é o que você quer.

EN: For Android, open the Play Console listing and copy the link from the browser bar. It looks like <code>play.google.com/store/apps/details?id=com.yourcompany.yourapp</code>. The <code>id</code> is your package name, and it never changes even when the app name does.
→  Para Android, abra a página no Play Console e copie o link da barra do navegador. Ele se parece com <code>play.google.com/store/apps/details?id=com.yourcompany.yourapp</code>. O <code>id</code> é o nome do seu pacote e nunca muda, mesmo quando o nome do app muda.

EN: Drop anything after the ID. Marketing tools often append tracking parameters like <code>?mt=8</code> or <code>&referrer=…</code>. They're harmless, but they make the QR pattern denser for no benefit, and a denser pattern is harder to print small.
→  Descarte tudo depois do ID. Ferramentas de marketing costumam acrescentar parâmetros de rastreamento como <code>?mt=8</code> ou <code>&referrer=…</code>. Eles são inofensivos, mas deixam o padrão do QR mais denso sem nenhum benefício, e um padrão mais denso é mais difícil de imprimir pequeno.

EN: Building a router page that works
→  Como montar uma página de redirecionamento que funcione

EN: If you go with one code, it needs somewhere to send people. A router page is a small page on your own domain that reads the user agent and forwards.
→  Se você ficar com um código só, ele precisa de um lugar para mandar as pessoas. Uma página de redirecionamento é uma página pequena no seu próprio domínio que lê o agente do usuário e encaminha.

EN: The logic is short: if the browser reports an iPhone or iPad, go to the App Store; if it reports Android, go to Play; otherwise show both buttons. Keep a fallback for desktop, because a meaningful share of scans come from people testing on a laptop.
→  A lógica é curta: se o navegador informar um iPhone ou iPad, vá para a App Store; se informar Android, vá para a Play; caso contrário, mostre os dois botões. Mantenha uma alternativa para desktop, porque boa parte dos escaneamentos vem de gente testando no notebook.

EN: Two things break these pages in practice. Apple's in-app browsers and some social apps strip the user agent down to something generic, so the detection guesses wrong. And a redirect that fires before the page renders can look like a broken link. Showing both buttons with the detected one highlighted is more forgiving than an instant forward.
→  Na prática, duas coisas quebram essas páginas. Os navegadores internos da Apple e alguns apps sociais reduzem o agente do usuário a algo genérico, e a detecção erra. E um redirecionamento que dispara antes de a página renderizar pode parecer um link quebrado. Mostrar os dois botões com o detectado em destaque funciona melhor do que encaminhar na hora.

EN: If you want the destination editable later, use a dynamic code pointing at the router page. Change the page and every printed code follows, no reprint.
→  Se você quiser poder editar o destino depois, use um código dinâmico apontando para a página de redirecionamento. Mude a página e todos os códigos impressos acompanham, sem reimprimir.

EN: App launch slide
→  Slide de lançamento

⚠️ 未翻译（与英文相同）
EN: 8 cm
→  8 cm

EN: scanned from a seat, 1–2 m away
→  escaneado do assento, a 1–2 m

EN: Packaging and inserts
→  Embalagens e encartes

EN: one code per platform, clearly labelled
→  um código por plataforma, bem identificado

EN: Receipt footer
→  Rodapé do recibo

EN: thermal printers blur thin lines; test first
→  impressoras térmicas borram linhas finas; teste antes

EN: Poster or ad
→  Pôster ou anúncio

EN: scanned from 2–3 m
→  escaneado a 2–3 m

EN: only if you print two codes with labels
→  só se você imprimir dois códigos com etiquetas

EN: When you print two codes, label them. A pair of identical-looking squares with no "iPhone" and "Android" text is worse than one code, because people scan the wrong one and land on a store they can't use.
→  Quando imprimir dois códigos, etiquete-os. Dois quadrados idênticos sem o texto “iPhone” e “Android” são piores que um código só, porque as pessoas escaneiam o errado e caem numa loja que não serve para elas.

EN: <span>Can one static code open both stores?</span>
→  <span>Um código estático pode abrir as duas lojas?</span>

EN: No. A static code stores a single URL, and your two store listings are two URLs. Encode the App Store link and Android visitors land on an app they cannot install. Print two labelled codes, or point one code at a page on your own domain that reads the phone and forwards to the right store.
→  Não. Um código estático guarda uma única URL, e suas duas páginas de loja são duas URLs. Se você codificar o link da App Store, visitantes de Android caem num app que não podem instalar. Imprima dois códigos etiquetados ou aponte um código para uma página do seu próprio domínio que detecte o telefone e encaminhe para a loja certa.

EN: <span>What if I fill in both fields?</span>
→  <span>E se eu preencher os dois campos?</span>

EN: Only the App Store link is encoded — the Play field is used when the App Store field is empty. To cover both platforms, make two codes, one per field.
→  Só o link da App Store é codificado — o campo Play é usado quando o campo App Store está vazio. Para cobrir as duas plataformas, crie dois códigos, um por campo.

EN: <span>What if I only have one platform?</span>
→  <span>E se eu só tiver uma plataforma?</span>

EN: Fill that field and print one code. Nothing else is needed.
→  Preencha esse campo e imprima um código. Não precisa de mais nada.

EN: <span>Can it detect the phone and route automatically?</span>
→  <span>Detecta o telefone e redireciona sozinho?</span>

EN: Not on its own — a printed pattern cannot run logic. Device detection needs a page in between: host a small router page, then point a dynamic code at it so you can change the destination later without reprinting.
→  Não sozinho — um padrão impresso não executa lógica. A detecção de aparelho precisa de uma página no meio: hospede uma pequena página de redirecionamento e aponte um código dinâmico para ela, assim você muda o destino depois sem reimprimir.

EN: <span>Does it track installs?</span>
→  <span>Conta as instalações?</span>

EN: No. Static codes carry only the link and never phone home. App Store Connect and the Play Console already report installs.
→  Não. Códigos estáticos carregam só o link e nunca enviam nada. O App Store Connect e o Play Console já informam as instalações.

EN: FreeQrly — app store qr code generator
→  FreeQrly — gerador de QR code da App Store

EN: Can one static code open both stores?
→  Um código estático pode abrir as duas lojas?

EN: What if I fill in both fields?
→  E se eu preencher os dois campos?

EN: What if I only have one platform?
→  E se eu só tiver uma plataforma?

EN: Can it detect the phone and route automatically?
→  Detecta o telefone e redireciona sozinho?

EN: Does it track installs?
→  Conta as instalações?

EN: Make your app store QR code
→  Crie seu QR code da App Store

EN: Copy one store link
→  Copie um link da loja

EN: App Store from App Store Connect, Play from the Play Console. One link per code — fill the App Store field for iOS, the Google Play field for Android.
→  App Store no App Store Connect, Play no Play Console. Um link por código — preencha o campo App Store para iOS, o campo Google Play para Android.

EN: Paste it in
→  Cole

EN: Your code appears instantly. Leave the other field empty unless you are making a second code.
→  Seu código aparece na hora. Deixe o outro campo vazio, a não ser que esteja criando um segundo código.

EN: Label it and print
→  Etiquete e imprima

EN: “iPhone” or “Android” next to the code, at 2 cm or larger. Ads, packaging, receipts, launch slides.
→  “iPhone” ou “Android” ao lado do código, com 2 cm ou mais. Anúncios, embalagens, recibos, slides de lançamento.


## about

EN: About FreeQrly — Free Static QR Codes, No Sign-Up, No Expiry
→  Sobre o FreeQrly — QR codes estáticos grátis, sem cadastro

EN: FreeQrly is a free QR code generator: static codes run 100% in your browser — no sign-up, no tracking, no expiry. Learn what it is and how it works.
→  FreeQrly é um gerador de QR code gratuito: códigos estáticos rodam 100% no navegador — sem cadastro, rastreamento ou expiração. Saiba o que é e como funciona.

EN: About FreeQrly
→  Sobre o FreeQrly

EN: A free QR code generator: static codes run 100% in your browser — no sign-up, no tracking, no expiry.
→  Um gerador de QR code gratuito: códigos estáticos rodam 100% no seu navegador — sem cadastro, sem rastreamento, sem expiração.

EN: Qly protecting your privacy with a shield
→  Qly protegendo sua privacidade com um escudo

EN: About
→  Sobre

EN: What is <span class="hl hl-mint">FreeQrly</span>?
→  O que é o <span class="hl hl-mint">FreeQrly</span>?

EN: FreeQrly is a free QR code generator with a simple idea: the tool should live in your browser, not on somebody's server. You type, it draws — nothing is uploaded, tracked, or billed.
→  O FreeQrly é um gerador de QR code gratuito com uma ideia simples: a ferramenta deve viver no seu navegador, não no servidor de outra pessoa. Você digita, ele desenha — nada é enviado, rastreado ou cobrado.

EN: <b>100% browser-based</b><span>Every code is drawn locally with JavaScript. Your links, contacts, and WiFi passwords never leave your device.</span>
→  <b>100% no navegador</b><span>Todo código é desenhado localmente com JavaScript. Seus links, contatos e senhas de WiFi nunca saem do seu dispositivo.</span>

EN: <b>Codes that never expire</b><span>Static codes live in the pattern itself; dynamic codes stay editable after printing. No trials, no deactivated codes — what you print today scans in ten years.</span>
→  <b>Códigos que nunca expiram</b><span>Códigos estáticos vivem no próprio padrão; códigos dinâmicos continuam editáveis depois de impressos. Sem períodos de teste, sem códigos desativados — o que você imprime hoje escaneia daqui a dez anos.</span>

EN: <b>Free to start</b><span>Static codes need no account at all. Dynamic codes — editable, with scan stats — need a free sign-in. No watermark either way.</span>
→  <b>Grátis para começar</b><span>Códigos estáticos não precisam de conta nenhuma. Códigos dinâmicos — editáveis, com estatísticas de escaneamento — precisam de um login gratuito. Sem marca d'água em nenhum dos casos.</span>

EN: <b>10 languages</b><span>English, Chinese, Spanish, Hindi, Arabic (RTL), Portuguese, French, Russian, German, Japanese.</span>
→  <b>10 idiomas</b><span>Inglês, chinês, espanhol, hindi, árabe (RTL), português, francês, russo, alemão, japonês.</span>

EN: <b>Built for print</b><span>High-resolution export and vector SVG, quiet zones respected — made for business cards, menus, and posters.</span>
→  <b>Feito para impressão</b><span>Exportação em alta resolução e SVG vetorial, zonas de silêncio respeitadas — feito para cartões de visita, cardápios e pôsteres.</span>

EN: <b>Agent-friendly</b><span>A free <a href="/developers/">API and MCP server</a> so AI assistants can generate codes too.</span>
→  <b>Amigável para agentes</b><span>Uma <a href="/developers/">API e servidor MCP</a> gratuitos para que assistentes de IA também possam gerar códigos.</span>

EN: Questions, answered
→  Perguntas, respondidas

EN: Almost everything is free. Static codes are completely free, with no watermarks — they are made entirely in your browser and need no account. Dynamic codes need a free sign-in so they can be edited later, and 20 are included free; if you need more, an optional Pro subscription (US$9/month or US$90/year) makes dynamic codes unlimited.
→  Quase tudo é gratuito. Os códigos estáticos são totalmente gratuitos, sem marcas d'água — são criados inteiramente no seu navegador e não precisam de conta. Os códigos dinâmicos precisam de um login gratuito para poderem ser editados depois, e 20 estão incluídos grátis; se precisar de mais, uma assinatura Pro opcional (US$ 9 por mês ou US$ 90 por ano) torna os códigos dinâmicos ilimitados.

EN: Do the QR codes expire?
→  Os QR codes expiram?

EN: No — neither kind. A static code's destination lives inside the pattern itself, and dynamic codes stay live and editable for as long as your account exists. Details: <a href="/blog/do-qr-codes-expire/">do QR codes expire?</a>
→  Não — nenhum dos dois. O destino de um código estático vive dentro do próprio padrão, e códigos dinâmicos continuam ativos e editáveis enquanto sua conta existir. Detalhes: <a href="/blog/do-qr-codes-expire/">os QR codes expiram?</a>

EN: Can I use it for my business?
→  Posso usar no meu negócio?

EN: Yes — commercial use is free. Restaurants use it for <a href="/blog/qr-codes-for-restaurants/">menus and reviews</a>, shops for <a href="/google-review-qr-code/">review codes</a> and <a href="/wifi-qr-code/">WiFi codes</a>.
→  Sim — o uso comercial é grátis. Restaurantes usam para <a href="/blog/qr-codes-for-restaurants/">cardápios e avaliações</a>, lojas para <a href="/google-review-qr-code/">códigos de avaliação</a> e <a href="/wifi-qr-code/">códigos de WiFi</a>.

EN: Who is behind FreeQrly?
→  Quem está por trás do FreeQrly?

EN: An independent maker who got tired of "free" generators that hold your codes hostage behind a trial. The mascot is Qly, a small elephant who appears across the site.
→  Um criador independente que cansou de geradores “grátis” que mantêm seus códigos reféns atrás de um teste. O mascote é o Qly, um elefantinho que aparece por todo o site.

EN: Try the generator →
→  Experimentar o gerador →

EN: FreeQrly is a free QR code generator that runs entirely in the browser. No sign-up, no tracking, no expiry — static QR codes with optional logos, in 10 languages.
→  O FreeQrly é um gerador de QR code gratuito que roda inteiramente no navegador. Sem cadastro, sem rastreamento, sem expiração — QR codes estáticos com logos opcionais, em 10 idiomas.

EN: What is FreeQrly?
→  O que é o FreeQrly?

EN: FreeQrly is a free online QR code generator. It creates static QR codes for links, text, WiFi, vCards, SMS, calls, and locations — entirely in your browser, with no account and no fees.
→  O FreeQrly é um gerador de QR code online e gratuito. Ele cria QR codes estáticos para links, textos, WiFi, vCards, SMS, chamadas e locais — inteiramente no seu navegador, sem conta e sem taxas.

EN: Yes — almost everything. Static codes are free with no trial and no watermarks, including logo upload, batch generation, and high-resolution export. Static codes need no account; dynamic codes need a free sign-in and include 20 free, with an optional Pro subscription for unlimited dynamic codes.
→  Sim — quase tudo. Os códigos estáticos são gratuitos, sem teste e sem marcas d'água, incluindo upload de logo, geração em lote e exportação em alta resolução. Os códigos estáticos não precisam de conta; os dinâmicos precisam de um login gratuito e incluem 20 grátis, com uma assinatura Pro opcional para códigos dinâmicos ilimitados.

EN: Do FreeQrly QR codes expire?
→  Os QR codes do FreeQrly expiram?

EN: No. Static codes encode the destination directly in the pattern, and dynamic codes stay live and editable — neither kind expires or requires a subscription.
→  Não. Códigos estáticos codificam o destino diretamente no padrão, e códigos dinâmicos continuam ativos e editáveis — nenhum dos dois expira ou exige assinatura.

EN: Does FreeQrly track my QR codes or my data?
→  O FreeQrly rastreia meus QR codes ou meus dados?

EN: Static codes are generated locally in your browser; their content is never uploaded and they have no scan tracking. Dynamic codes count scans — that is what they are for — and their destinations can be changed anytime.
→  Códigos estáticos são gerados localmente no seu navegador; o conteúdo nunca é enviado e não há contagem de escaneamentos. Códigos dinâmicos contam escaneamentos — é para isso que servem — e o destino pode ser alterado a qualquer momento.

EN: What languages does FreeQrly support?
→  Quais idiomas o FreeQrly suporta?

EN: Ten: English, Chinese, Spanish, Hindi, Arabic (with right-to-left layout), Portuguese, French, Russian, German, and Japanese.
→  Dez: inglês, chinês, espanhol, hindi, árabe (com layout da direita para a esquerda), português, francês, russo, alemão e japonês.


## landing-ticket-qr-code

EN: Free Ticket QR Code Generator | FreeQrly
→  Gerador de QR code grátis para ingressos | FreeQrly

EN: Create free QR codes for tickets: link to your ticket or check-in page, print one code per ticket with Batch mode, no sign-up for static codes, never expires.
→  QR codes grátis para ingressos: um código por ingresso com o modo lote, sem cadastro para códigos estáticos — eles nunca expiram.

EN: One scan at the door, <span class="hl hl-mint">no ticket queue</span>.
→  Um escaneamento na porta, <span class="hl hl-mint">sem fila na entrada</span>.

EN: Put a QR code on every ticket, poster, and confirmation email. Guests scan at the entrance and land straight on your ticket or check-in page — concerts, conferences, workshops, school events.
→  Coloque um QR code em cada ingresso, pôster e e-mail de confirmação. O convidado escaneia na entrada e cai direto na sua página de ingresso ou de check-in — shows, conferências, workshops, eventos escolares.

EN: <span class="sn">1</span><span><b>Link to your ticket page</b>Your ticketing page, check-in form, or event details — one code, one destination.</span>
→  <span class="sn">1</span><span><b>Vincule à sua página de ingresso</b>Sua página de venda de ingressos, formulário de check-in ou detalhes do evento — um código, um destino.</span>

EN: <span class="sn">2</span><span><b>Make the code</b>Paste the link in the studio below. Print-ready PNG or SVG, free, no watermark, no sign-up for static codes.</span>
→  <span class="sn">2</span><span><b>Crie o código</b>Cole o link no estúdio abaixo. PNG ou SVG pronto para impressão, grátis, sem marca-d'água, sem cadastro para códigos estáticos.</span>

EN: <span class="sn">3</span><span><b>One code per ticket, with Batch</b>Need a different code on every ticket? Batch mode takes one link per line and downloads every code as a ZIP.</span>
→  <span class="sn">3</span><span><b>Um código por ingresso, com o modo lote</b>Precisa de um código diferente em cada ingresso? O modo lote recebe um link por linha e baixa todos os códigos em ZIP.</span>

EN: <span>What should a ticket QR code link to?</span>
→  <span>Para onde deve apontar o QR code do ingresso?</span>

EN: Your ticket page, a check-in form, or the event details page. The code simply opens that page on the guest’s phone — keep the page itself as the source of truth for entry.
→  Sua página de ingresso, um formulário de check-in ou a página de detalhes do evento. O código apenas abre essa página no celular do convidado — mantenha a própria página como fonte oficial para a entrada.

EN: <span>Can I make a different code for every ticket?</span>
→  <span>Posso criar um código diferente para cada ingresso?</span>

EN: Yes — Batch mode generates one code per link: paste one ticket link per line, download them all as a ZIP, and print each on its own ticket.
→  Sim — o modo lote gera um código por link: cole um link de ingresso por linha, baixe todos em ZIP e imprima cada um no seu ingresso.

EN: <span>Do ticket QR codes expire?</span>
→  <span>QR codes de ingresso expiram?</span>

EN: No. Static codes never expire. If the event moves, point the page behind the code at the new details — or, with a dynamic code, repoint the code itself without reprinting.
→  Não. Códigos estáticos nunca expiram. Se o evento mudar de lugar, aponte a página por trás do código para os novos detalhes — ou, com um QR code dinâmico, redirecione o próprio código sem reimprimir.

EN: <span>How big should I print it on a ticket?</span>
→  <span>De que tamanho devo imprimir no ingresso?</span>

EN: At least 2 × 2 cm with a clear quiet margin, at 1024 px export or higher. At a busy entrance, bigger is safer — a code that scans first try keeps the line moving.
→  Pelo menos 2 × 2 cm, com margem de silêncio limpa, em exportação de 1024 px ou mais. Em uma entrada movimentada, maior é mais seguro — um código que lê de primeira mantém a fila andando.

EN: FreeQrly — qr code ticket
→  FreeQrly — qr code ingresso

EN: What should a ticket QR code link to?
→  Para onde deve apontar o QR code do ingresso?

EN: Can I make a different code for every ticket?
→  Posso criar um código diferente para cada ingresso?

EN: Do ticket QR codes expire?
→  QR codes de ingresso expiram?

EN: How big should I print it on a ticket?
→  De que tamanho devo imprimir no ingresso?

EN: Make your ticket QR code
→  Crie seu QR code do ingresso

EN: Link to your ticket page
→  Vincule à sua página de ingresso

EN: Your ticketing page, check-in form, or event details — one code, one destination.
→  Sua página de venda de ingressos, formulário de check-in ou detalhes do evento — um código, um destino.

EN: Paste the link in the studio below. Print-ready PNG or SVG, free, no watermark, no sign-up for static codes.
→  Cole o link no estúdio abaixo. PNG ou SVG pronto para impressão, grátis, sem marca-d'água, sem cadastro para códigos estáticos.

EN: One code per ticket, with Batch
→  Um código por ingresso, com o modo lote

EN: Need a different code on every ticket? Batch mode takes one link per line and downloads every code as a ZIP.
→  Precisa de um código diferente em cada ingresso? O modo lote recebe um link por linha e baixa todos os códigos em ZIP.
