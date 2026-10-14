/* FreeQrly v1.0 — app logic */
(function(){
"use strict";
const $ = id => document.getElementById(id);

const I18N = {
en:{
  title:"Free QR Code Generator — No Sign-Up, No Expiry | FreeQrly",
  metaDesc:"FreeQrly is a free QR code generator that runs entirely in your browser — even with your logo. No sign-up, no tracking, no expiry. Export PNG & SVG.",
  navStudio:"Studio",navWhy:"Principles",navFaq:"FAQ",
  kicker:"Free · No sign-up · Private by design",
  h1a:"Quiet codes for",h1b:"loud",h1c:"places.",
  lede:"Make beautiful QR codes right in your browser — no sign-up, no tracking, no expiry. Free, simple, and yours to keep.",
  hc1:"Content types",hc2:"Export",hc3:"Your data",hc3v:"Stays with you",hc4:"Price",hc4v:"Free, forever",
  sOver:"The studio",sTitle:"Create your QR code",
  appearance:"Style",ink:"Ink",paper:"Paper",background:"Background",dots:"Dot style",ecc:"Error correction",
  dSquare:"Square",dRound:"Round",dSoft:"Soft",dPebble:"Pebble",
  eL:"Low",eM:"Medium",eQ:"High",eH:"Max",
  eccHint:"Higher levels survive logos and wear.",dotsSub:"QR dot shape",eccSub:"Higher survives wear",colors:"Colors",colorsSub:"Tap or customize",transparentSub:"No white base",
  size:"Export size",logo:"Add your logo",logoSub:"Brand or your own",
  privnote:"Everything is generated locally in your browser.",
  live:"Live preview — updates as you type",
  bLabel:"One link per line",bGo:"Generate all",bZip:"Download ZIP",bEmpty:"Enter at least one link above first",
  p1n:"No. 1",p1t:"Your data goes nowhere",p1p:"Every code is drawn on your own device — no uploads, no tracking, no accounts. Load the page, pull the plug, everything still works.",
  p2n:"No. 2",p2t:"Made to last",p2p:"A static code carries its destination inside the pattern. Print it today and it'll scan in ten years. No renewals, no platforms to disappear.",
  p3n:"No. 3",p3t:"Free means free",p3p:"No watermark, no sign-up wall, no expiry. No Pro tier, no hidden fees — good tools should just be free.",
  faqT:"Good to know",
  q1:"Do free QR codes expire?",a1:"Never. The destination is encoded directly in the pattern, so a code works as long as the destination does. Paid dynamic codes run through a vendor's servers and can die when you stop paying — one more reason static feels safer.",
  q2:"Is my WiFi password safe here?",a2:"Yes. Your password never leaves your browser — nothing is sent anywhere. Extra careful? Load the page, disconnect, then type.",
  q3:"Static or dynamic — which should I choose?",a3:"If the destination won't change, go static: WiFi, business cards, fixed links. Dynamic codes (editable links + scan stats) suit marketing campaigns — they're on our roadmap.",
  q4:"Can I use these commercially?",a4:"Absolutely. Every code you make here is yours — packaging, menus, business cards, no attribution needed.",
  q5:"Is FreeQrly really free?",a5:"Yes — everything on this page is free, with no watermark and no account. We don't sell subscriptions; this is a tool, not a funnel.",
  q6:"Do I need an account?",a6:"No. There is nothing to sign up for — open the page and make your code.",
  q7:"Can I add my logo to the QR code?",a7:"Yes — upload any square logo and it goes in the center, with error correction raised automatically so it keeps scanning. For print, use Q or H.",
  fin:"Made quietly, in your browser.",
  dl:"Download",navScan:"Scanner",history:"Recent",histClear:"Clear",transparent:"Transparent background",types:{url:["Website","link, page, video"],text:["Text","any words"],wifi:["WiFi","join instantly"],vcard:["Contact","vCard"],email:["Email","prefilled"],sms:["SMS","prefilled text"],phone:["Call","tap to dial"],geo:["Place","map pin"],"event":["Event","add to calendar"],"batch":["Batch","many at once"]},
  fields:{url:[["url","Destination","https://example.com"]],text:[["text","Message","textarea","Hello, world!"]],
    wifi:[["ssid","Network name","MyWiFi"],["pass","Password","","WiFi password"],["enc","Security","select:WPA,WPA2,WEP,nopass"]],
    vcard:[["name","Full name","Jane Doe"],["phone","Phone","+1 555 0100"],["email","Email","jane@example.com"]],
    email:[["to","To","hi@example.com"],["subject","Subject","Hello"],["body","Body","textarea","Email body…"]],
    sms:[["phone","Phone","+1 555 0100"],["body","Message","","Type your message…"]],
    phone:[["phone","Phone","+1 555 0100"]],geo:[["lat","Latitude","37.7749"],["lng","Longitude","-122.4194"]],"event":[["etitle","Title","","e.g. Birthday party"],["estart","Starts","datetime-local"],["eend","Ends","datetime-local"],["eloc","Location","","e.g. Central Park"],["edesc","Details","textarea","Event details…"]]}
},
zh:{
  title:"FreeQrly — 免费二维码生成器，隐私优先",
  metaDesc:"直接在浏览器里生成精美二维码。永久免费、免注册、不上传任何数据。支持 PNG / SVG 导出。",
  navStudio:"工作台",navWhy:"理念",navFaq:"常见问题",
  kicker:"免费 · 免注册 · 隐私优先",
  h1a:"把内容变成",h1b:"好看",h1c:"的二维码。",
  lede:"在浏览器里直接做二维码——免注册、无追踪、永不过期。免费、简单、一直都在。",
  hc1:"内容类型",hc2:"导出",hc3:"你的数据",hc3v:"从不离开你",hc4:"价格",hc4v:"永久免费",
  sOver:"工作台",sTitle:"做一张二维码",
  appearance:"外观样式",ink:"墨色",paper:"纸色",background:"背景",dots:"码点形状",ecc:"容错等级",
  dSquare:"方形",dRound:"圆形",dSoft:"柔和",dPebble:"鹅卵石",
  eL:"Bajo",eM:"Medio",eQ:"Alto",eH:"Máximo",
  eccHint:"容错越高，越耐磨损、越适合加 Logo。",dotsSub:"二维码点的样式",eccSub:"越高越耐磨损",colors:"颜色",colorsSub:"点选或自定义",transparentSub:"去掉白色底",
  size:"导出尺寸",logo:"添加 Logo",logoSub:"品牌或自定义",
  privnote:"所有生成都在你的浏览器里完成。",
  live:"实时预览，输入即变",
  bLabel:"每行一个链接",bGo:"全部生成",bZip:"下载 ZIP",bEmpty:"请先在上面输入至少一个链接",featsK:"不止于生成",featsT:"二维码之外，还有更多",featsS:"生成只是开始。FreeQrly 里还有这些。",f1t:"内置扫码器",f1d:"用摄像头对准，或上传图片——二维码在你的浏览器里直接解码，绝不上传到服务器。离线也能用。",f1l:"打开扫码器 →",f2t:"10 种二维码类型",f2d:"网址、文本、WiFi、电子名片、邮件、短信、电话、地点、日历事件。每种类型自动生成正确格式，不用记语法。",f2l:"都试试 →",f3t:"批量生成",f3d:"一次粘贴 50 个链接，一键得到 50 个可打印的二维码。逐个下载，或打包成 ZIP。",f3l:"批量模式 →",f4t:"日历事件码",f4d:"扫一下，活动标题、时间、地点直接进手机日历。为请柬而生。",f4l:"生成事件码 →",f5t:"Logo 与美化",f5d:"把 logo 放中间，容错等级自动提高，保证扫得出。圆点、墨色、纸色随便搭，还能透明底。",f5l:"带 logo 的码 →",f6t:"私密历史记录",f6d:"每次下载只记在这台设备上——最近 12 条，一键恢复。随时清空，我们永远看不到。",casesK:"真实场景",casesT:"为真实时刻而造",casesS:"选你的场景，方法都准备好了。",c1t:"名片",c1d:"扫一下，联系方式直接进对方手机。",c2t:"婚礼",c2d:"RSVP、照片共享、日历提醒。纸的流程，无纸的体验。",c3t:"房产",c3d:"房源立牌扫码看，一键预约看房。",c4t:"活动",c4d:"签到、验票、共享相册，一码搞定。",c5t:"WiFi 分享",c5d:"客人扫码上网。再也不用念密码。",c6t:"谷歌评价",c6d:"把满意的客人变成柜台前的五星好评。",
  p1n:"其一",p1t:"你的数据，哪儿也不去",p1p:"二维码在你的设备上直接绘制，不上传、不追踪、不用注册。页面加载后断网，也一切如常。",
  p2n:"其二",p2t:"一次生成，永久有效",p2p:"静态码把网址直接写进图案里。今天印出来，十年后照样能扫。不用续费，不怕平台倒闭。",
  p3n:"其三",p3t:"免费，就只是免费",p3p:"无水印、无注册墙、永不过期。没有 Pro 版，没有隐藏收费——好用的东西就该免费。",
  faqT:"你可能想问",
  q1:"免费的二维码会过期吗？",a1:"不会。网址直接编码在图案里，只要网址本身有效，码就一直有效。付费动态码走服务商的服务器，停付就可能失效——这也是静态码更让人放心的原因。",
  q2:"在这里输入 WiFi 密码安全吗？",a2:"安全。密码从头到尾都在你的浏览器里，不会发送到任何地方。实在不放心，页面加载完成后断网再输入。",
  q3:"静态码和动态码怎么选？",a3:"地址不变就用静态码：WiFi、名片、固定链接。动态码（可修改地址、看扫码统计）适合做营销活动，我们的路线图上有它。",
  q4:"可以商用吗？",a4:"当然。这里生成的所有二维码都属于你，印在包装、菜单、名片上都不需要署名。",
  q5:"FreeQrly 真的免费吗？",a5:"真的。这一页的所有功能都免费，无水印、不用注册。我们不卖订阅，这就是一个趁手的工具。",
  q6:"需要注册账号吗？",a6:"不需要。这里没有什么可注册的——打开页面，直接做码。",
  q7:"二维码中间能加我的 Logo 吗？",a7:"可以。上传一张方形 Logo，它会放在正中央，容错等级会自动提高以保证可扫。用来印刷的话，建议选 Q 或 H 容错。",
  fin:"在你的浏览器里，静静生成。",
  dl:"下载",navScan:"扫码",history:"最近",histClear:"清除",transparent:"透明背景",types:{url:["网址","链接、页面、视频"],text:["文本","任意文字"],wifi:["WiFi","一键联网"],vcard:["名片","vCard"],email:["邮箱","预填内容"],sms:["短信","预填内容"],phone:["电话","点击拨号"],geo:["位置","地图标记"],"event":["活动","添加到日历"],"batch":["批量","一次多个"]},
  fields:{url:[["url","目标地址","https://example.com"]],text:[["text","内容","textarea","你好，世界！"]],
    wifi:[["ssid","网络名称","MyWiFi"],["pass","密码","","WiFi 密码"],["enc","加密方式","select:WPA,WPA2,WEP,nopass"]],
    vcard:[["name","姓名","王小明"],["phone","电话","+86 138 0000 0000"],["email","邮箱","hi@example.com"]],
    email:[["to","收件人","hi@example.com"],["subject","主题","你好"],["body","正文","textarea","邮件正文…"]],
    sms:[["phone","电话","+86 138 0000 0000"],["body","内容","","输入短信内容…"]],
    phone:[["phone","电话","+86 138 0000 0000"]],geo:[["lat","纬度","39.9042"],["lng","经度","116.4074"]],"event":[["etitle","标题","","例如：生日派对"],["estart","开始","datetime-local"],["eend","结束","datetime-local"],["eloc","地点","","例如：中央公园"],["edesc","详情","textarea","活动详情…"]]}},
es:{title:"FreeQrly — Generador de códigos QR gratis | Sin registro",metaDesc:"Crea códigos QR gratis en tu navegador, incluso con tu logo. Sin registro, sin rastreo, sin caducidad. Exporta en PNG y SVG.",navStudio:"Estudio",navWhy:"Principios",navFaq:"Preguntas",kicker:"Gratis · Sin registro · Privado por diseño",h1a:"Códigos",h1b:"silenciosos",h1c:"para lugares ruidosos.",lede:"Crea códigos QR bonitos en tu navegador — sin registro, sin rastreo, sin caducidad. Gratis, simple y tuyos para siempre.",hc1:"Tipos de contenido",hc2:"Exportar",hc3:"Tus datos",hc3v:"Se quedan contigo",hc4:"Precio",hc4v:"Gratis, para siempre",sOver:"El estudio",sTitle:"Crea tu código QR",appearance:"Apariencia",ink:"Tinta",paper:"Papel",background:"Fondo",dots:"Estilo de puntos",ecc:"Corrección de errores",dSquare:"Cuadrado",dRound:"Redondo",dSoft:"Suave",dPebble:"Guijarro",eL:"Bajo",eM:"Medio",eQ:"Alto",eH:"Máximo",eccHint:"Más nivel, más resistencia a logos y desgaste.",dotsSub:"Forma de los puntos",eccSub:"Más alto, más resistente",colors:"Colores",colorsSub:"Toca o personaliza",transparentSub:"Sin fondo blanco",size:"Tamaño de exportación",logo:"Añade tu logo",logoSub:"Marca o propio",privnote:"Todo se genera localmente en tu navegador.",live:"Vista previa en vivo — cambia al escribir",bLabel:"Un enlace por línea",bGo:"Generar todos",bZip:"Descargar ZIP",bEmpty:"Escribe al menos un enlace arriba",featsK:"Más allá del código",featsT:"Todo lo que rodea al QR",featsS:"Generar es solo el principio. Esto también vive en FreeQrly.",f1t:"Escáner integrado",f1d:"Apunta tu cámara o sube una imagen — los códigos se decodifican en tu navegador y nunca se suben a ningún servidor. Funciona sin conexión.",f1l:"Abrir el escáner →",f2t:"10 tipos de código",f2d:"Web, texto, WiFi, tarjetas de contacto, correo, SMS, llamadas, ubicaciones, eventos de calendario. Cada tipo genera el formato correcto — sin memorizar sintaxis.",f2l:"Probarlos todos →",f3t:"Generación en lote",f3d:"Pega hasta 50 enlaces y obtén 50 códigos listos para imprimir en un clic. Descárgalos uno por uno o todo en un ZIP.",f3l:"Modo lote →",f4t:"Códigos de evento",f4d:"Un escaneo y tu evento — título, hora, lugar — entra directo al calendario del invitado. Hecho para invitaciones.",f4l:"Crear código de evento →",f5t:"Logo y estilo",f5d:"Pon tu logo en el centro y la corrección de errores sube sola para que siga escaneándose. Cambia puntos, tinta y papel — o usa fondo transparente.",f5l:"Códigos con logo →",f6t:"Historial privado",f6d:"Cada descarga se recuerda solo en este dispositivo — tus doce más recientes, un clic para recuperar. Bórralo cuando quieras.",casesK:"En acción",casesT:"Hecho para momentos reales",casesS:"Elige tu escenario — la configuración ya está resuelta.",c1t:"Tarjetas de visita",c1d:"Tus datos de contacto en un escaneo — directo a su teléfono.",c2t:"Bodas",c2d:"RSVP, fotos compartidas, añadir al calendario. El papeleo, sin papel.",c3t:"Inmobiliaria",c3d:"Anuncios en el cartel. Reserva una visita en un escaneo.",c4t:"Eventos",c4d:"Registro, validación de entradas, álbumes compartidos.",c5t:"Compartir WiFi",c5d:"Invitados conectados en un escaneo. Nunca más deletrees una contraseña.",c6t:"Reseñas de Google",c6d:"Convierte clientes felices en cinco estrellas, en el mostrador.",p1n:"N.º 1",p1t:"Tus datos no salen de aquí",p1p:"Cada código se dibuja en tu dispositivo — sin subidas, sin rastreo, sin cuentas. Carga la página, desconéctate, todo sigue funcionando.",p2n:"N.º 2",p2t:"Hechos para durar",p2p:"Un código estático lleva su destino dentro del patrón. Imprímelo hoy y se escaneará en diez años. Sin renovaciones ni plataformas que desaparezcan.",p3n:"N.º 3",p3t:"Gratis significa gratis",p3p:"Sin marca de agua, sin muro de registro, sin caducidad. Sin plan Pro ni cargos ocultos — las buenas herramientas deberían ser gratis.",faqT:"Conviene saber",q1:"¿Caduca un código QR gratuito?",a1:"Nunca. El destino va codificado en el patrón, así que funciona mientras el destino exista. Los códigos dinámicos de pago pasan por servidores del proveedor y pueden morir si dejas de pagar — otra razón para preferir lo estático.",q2:"¿Mi contraseña WiFi está segura aquí?",a2:"Sí. Tu contraseña nunca sale de tu navegador — nada se envía a ningún lado. ¿Precavido? Carga la página, desconéctate y escribe.",q3:"¿Estático o dinámico?",a3:"Si el destino no cambiará, usa estático: WiFi, tarjetas, enlaces fijos. Los dinámicos (enlaces editables y estadísticas) sirven para campañas — están en nuestra hoja de ruta.",q4:"¿Puedo usarlos comercialmente?",a4:"Por supuesto. Todo lo que crees aquí es tuyo — empaques, menús, tarjetas, sin atribución.",q5:"¿FreeQrly es realmente gratis?",a5:"Sí — todo en esta página es gratis, sin marca de agua ni cuenta. No vendemos suscripciones; esto es una herramienta, no un embudo.",q6:"¿Necesito una cuenta?",a6:"No. No hay nada que registrar — abre la página y crea tu código.",q7:"¿Puedo poner mi logo en el código?",a7:"Sí — sube un logo cuadrado y lo colocamos en el centro, subiendo automáticamente la corrección de errores para que siga escaneándose. Para imprenta, usa Q o H.",fin:"Hecho en silencio, en tu navegador.",dl:"Descargar",navScan:"Escáner",history:"Recientes",histClear:"Borrar",transparent:"Fondo transparente",types:{"url": ["Sitio web", "enlace, página, video"], "text": ["Texto", "cualquier palabra"], "wifi": ["WiFi", "conexión instantánea"], "vcard": ["Contacto", "vCard"], "email": ["Correo", "prellenado"], "sms": ["SMS", "texto prellenado"], "phone": ["Llamada", "tocar para llamar"], "geo": ["Lugar", "pin de mapa"],"event":["Evento","añadir al calendario"],"batch":["Lote", "muchos a la vez"]},fields:{"url": [["url", "Destino", "https://example.com"]], "text": [["text", "Mensaje", "textarea", "¡Hola, mundo!"]], "wifi": [["ssid", "Nombre de red", "MiWiFi"], ["pass", "Contraseña", "", "Contraseña WiFi"], ["enc", "Seguridad", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "Nombre completo", "María García"], ["phone", "Teléfono", "+34 600 000 000"], ["email", "Correo", "maria@example.com"]], "email": [["to", "Para", "hola@example.com"], ["subject", "Asunto", "Hola"], ["body", "Cuerpo", "textarea", "Cuerpo del correo…"]], "sms": [["phone", "Teléfono", "+34 600 000 000"], ["body", "Mensaje", "", "Escribe tu mensaje…"]], "phone": [["phone", "Teléfono", "+34 600 000 000"]], "geo": [["lat", "Latitud", "40.4168"], ["lng", "Longitud", "-3.7038"]],"event":[["etitle","Título","","p. ej. Cumpleaños"],["estart","Inicio","datetime-local"],["eend","Fin","datetime-local"],["eloc","Ubicación","","p. ej. Parque Central"],["edesc","Detalles","textarea","Detalles del evento…"]]}},
pt:{title:"FreeQrly — Gerador de QR Code grátis | Sem cadastro",metaDesc:"Crie QR codes grátis no seu navegador, até com seu logo. Sem cadastro, sem rastreamento, sem expiração. Exporte em PNG e SVG.",navStudio:"Estúdio",navWhy:"Princípios",navFaq:"Perguntas",kicker:"Grátis · Sem cadastro · Privado por design",h1a:"Códigos",h1b:"discretos",h1c:"para lugares barulhentos.",lede:"Crie QR codes bonitos no seu navegador — sem cadastro, sem rastreamento, sem expiração. Grátis, simples e seus para sempre.",hc1:"Tipos de conteúdo",hc2:"Exportar",hc3:"Seus dados",hc3v:"Ficam com você",hc4:"Preço",hc4v:"Grátis, para sempre",sOver:"O estúdio",sTitle:"Crie seu QR code",appearance:"Aparência",ink:"Tinta",paper:"Papel",background:"Fundo",dots:"Estilo dos pontos",ecc:"Correção de erros",dSquare:"Quadrado",dRound:"Redondo",dSoft:"Suave",dPebble:"Seixo",eL:"Baixo",eM:"Médio",eQ:"Alto",eH:"Máximo",eccHint:"Quanto maior, mais resiste a logos e desgaste.",dotsSub:"Formato dos pontos",eccSub:"Mais alto, mais resistente",colors:"Cores",colorsSub:"Toque ou personalize",transparentSub:"Sem fundo branco",size:"Tamanho de exportação",logo:"Adicione seu logo",logoSub:"Marca ou própria",privnote:"Tudo é gerado localmente no seu navegador.",live:"Prévia ao vivo — muda ao digitar",bLabel:"Um link por linha",bGo:"Gerar todos",bZip:"Baixar ZIP",bEmpty:"Digite pelo menos um link acima",featsK:"Além do código",featsT:"Tudo ao redor do QR",featsS:"Gerar é só o começo. Isto também vive dentro do FreeQrly.",f1t:"Scanner integrado",f1d:"Aponte a câmera ou suba uma imagem — os códigos são decodificados no seu navegador e nunca enviados a nenhum servidor. Funciona offline.",f1l:"Abrir o scanner →",f2t:"10 tipos de código",f2d:"Site, texto, WiFi, cartões de contato, e-mail, SMS, chamadas, locais, eventos de calendário. Cada tipo gera o formato correto — sem decorar sintaxe.",f2l:"Testar todos →",f3t:"Geração em lote",f3d:"Cole até 50 links e receba 50 códigos prontos para impressão em um clique. Baixe um por um ou tudo em ZIP.",f3l:"Modo lote →",f4t:"Códigos de evento",f4d:"Um scan e seu evento — título, hora, local — entra direto no calendário do convidado. Feito para convites.",f4l:"Criar código de evento →",f5t:"Logo e estilo",f5d:"Coloque seu logo no centro e a correção de erros sobe sozinha para continuar escaneável. Mude pontos, tinta e papel — ou use fundo transparente.",f5l:"Códigos com logo →",f6t:"Histórico privado",f6d:"Cada download é lembrado só neste dispositivo — seus doze mais recentes, um clique para recuperar. Limpe quando quiser.",casesK:"No mundo real",casesT:"Feito para momentos reais",casesS:"Escolha seu cenário — a configuração já está pronta.",c1t:"Cartões de visita",c1d:"Seus contatos em um scan — direto para o telefone deles.",c2t:"Casamentos",c2d:"RSVP, fotos compartilhadas, adicionar ao calendário. A papelada, sem papel.",c3t:"Imobiliária",c3d:"Anúncios na placa. Agende uma visita em um scan.",c4t:"Eventos",c4d:"Check-in, validação de ingressos, álbuns compartilhados.",c5t:"Compartilhar WiFi",c5d:"Convidados online em um scan. Nunca mais soletre uma senha.",c6t:"Avaliações no Google",c6d:"Transforme clientes felizes em cinco estrelas, no balcão.",p1n:"N.º 1",p1t:"Seus dados não saem daqui",p1p:"Cada código é desenhado no seu dispositivo — sem uploads, sem rastreamento, sem contas. Carregue a página, desconecte-se, tudo continua funcionando.",p2n:"N.º 2",p2t:"Feitos para durar",p2p:"Um código estático carrega o destino dentro do padrão. Imprima hoje e ele será escaneado em dez anos. Sem renovações nem plataformas que desaparecem.",p3n:"N.º 3",p3t:"Grátis significa grátis",p3p:"Sem marca d'água, sem muro de cadastro, sem expiração. Sem plano Pro nem taxas ocultas — boas ferramentas deveriam ser grátis.",faqT:"Bom saber",q1:"Um QR code grátis expira?",a1:"Nunca. O destino vai codificado no padrão, então funciona enquanto o destino existir. Códigos dinâmicos pagos passam pelos servidores do fornecedor e podem morrer se você parar de pagar — mais um motivo para preferir o estático.",q2:"Minha senha do WiFi está segura aqui?",a2:"Sim. Sua senha nunca sai do seu navegador — nada é enviado a lugar algum. Precavido? Carregue a página, desconecte-se e digite.",q3:"Estático ou dinâmico?",a3:"Se o destino não vai mudar, use estático: WiFi, cartões, links fixos. Os dinâmicos (links editáveis e estatísticas) servem para campanhas — estão no nosso roteiro.",q4:"Posso usar comercialmente?",a4:"Claro. Tudo que você criar aqui é seu — embalagens, cardápios, cartões, sem atribuição.",q5:"O FreeQrly é realmente grátis?",a5:"Sim — tudo nesta página é grátis, sem marca d'água nem conta. Não vendemos assinaturas; isto é uma ferramenta, não um funil.",q6:"Preciso de uma conta?",a6:"Não. Não há nada para cadastrar — abra a página e crie seu código.",q7:"Posso colocar meu logo no código?",a7:"Sim — envie um logo quadrado e o colocamos no centro, aumentando automaticamente a correção de erros para continuar escaneável. Para impressão, use Q ou H.",fin:"Feito em silêncio, no seu navegador.",dl:"Baixar",navScan:"Scanner",history:"Recentes",histClear:"Limpar",transparent:"Fundo transparente",types:{"url": ["Site", "link, página, vídeo"], "text": ["Texto", "qualquer palavra"], "wifi": ["WiFi", "conexão instantânea"], "vcard": ["Contato", "vCard"], "email": ["E-mail", "pré-preenchido"], "sms": ["SMS", "texto pré-preenchido"], "phone": ["Ligação", "tocar para ligar"], "geo": ["Lugar", "pino no mapa"],"event":["Evento","adicionar ao calendário"],"batch":["Lote", "vários de uma vez"]},fields:{"url": [["url", "Destino", "https://example.com"]], "text": [["text", "Mensagem", "textarea", "Olá, mundo!"]], "wifi": [["ssid", "Nome da rede", "MinhaWiFi"], ["pass", "Senha", "", "Senha do WiFi"], ["enc", "Segurança", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "Nome completo", "Maria Silva"], ["phone", "Telefone", "+55 11 90000 0000"], ["email", "E-mail", "maria@example.com"]], "email": [["to", "Para", "ola@example.com"], ["subject", "Assunto", "Olá"], ["body", "Corpo", "textarea", "Corpo do e-mail…"]], "sms": [["phone", "Telefone", "+55 11 90000 0000"], ["body", "Mensagem", "", "Digite sua mensagem…"]], "phone": [["phone", "Telefone", "+55 11 90000 0000"]], "geo": [["lat", "Latitude", "-23.5558"], ["lng", "Longitude", "-46.6396"]],"event":[["etitle","Título","","ex.: Festa de aniversário"],["estart","Início","datetime-local"],["eend","Fim","datetime-local"],["eloc","Local","","ex.: Parque Central"],["edesc","Detalhes","textarea","Detalhes do evento…"]]}},
fr:{title:"FreeQrly — Générateur de QR code gratuit | Sans inscription",metaDesc:"Créez des QR codes gratuits dans votre navigateur, même avec votre logo. Sans inscription, sans suivi, sans expiration. Export PNG et SVG.",navStudio:"Studio",navWhy:"Principes",navFaq:"Questions",kicker:"Gratuit · Sans inscription · Privé par design",h1a:"Des codes",h1b:"discrets",h1c:"pour lieux bruyants.",lede:"Créez de beaux QR codes dans votre navigateur — sans inscription, sans suivi, sans expiration. Gratuit, simple, et à vous pour toujours.",hc1:"Types de contenu",hc2:"Exporter",hc3:"Vos données",hc3v:"Restent avec vous",hc4:"Prix",hc4v:"Gratuit, pour toujours",sOver:"Le studio",sTitle:"Créez votre QR code",appearance:"Apparence",ink:"Encre",paper:"Papier",background:"Fond",dots:"Style des points",ecc:"Correction d'erreur",dSquare:"Carré",dRound:"Rond",dSoft:"Doux",dPebble:"Galet",eL:"Faible",eM:"Moyen",eQ:"Élevé",eH:"Maximal",eccHint:"Plus le niveau est haut, plus il résiste aux logos et à l'usure.",dotsSub:"Forme des points",eccSub:"Plus résistant",colors:"Couleurs",colorsSub:"Touchez ou personnalisez",transparentSub:"Sans fond blanc",size:"Taille d'export",logo:"Ajoutez votre logo",logoSub:"Marque ou perso",privnote:"Tout est généré localement dans votre navigateur.",live:"Aperçu en direct — change à la frappe",bLabel:"Un lien par ligne",bGo:"Tout générer",bZip:"Télécharger ZIP",bEmpty:"Saisissez au moins un lien ci-dessus",featsK:"Au-delà du code",featsT:"Tout autour du QR",featsS:"Générer n'est que le début. Ceci vit aussi dans FreeQrly.",f1t:"Scanner intégré",f1d:"Pointez votre caméra ou envoyez une image — les codes sont décodés dans votre navigateur et ne sont jamais téléversés. Fonctionne même hors ligne.",f1l:"Ouvrir le scanner →",f2t:"10 types de codes",f2d:"Site web, texte, WiFi, cartes de visite, e-mail, SMS, appels, lieux, événements. Chaque type génère le bon format — aucune syntaxe à retenir.",f2l:"Tous les essayer →",f3t:"Génération en lot",f3d:"Collez jusqu'à 50 liens et obtenez 50 codes prêts à imprimer en un clic. Téléchargez un par un ou tout en ZIP.",f3l:"Mode lot →",f4t:"Codes d'événement",f4d:"Un scan et votre événement — titre, heure, lieu — entre dans le calendrier de l'invité. Pensé pour les invitations.",f4l:"Créer un code d'événement →",f5t:"Logo et style",f5d:"Placez votre logo au centre et la correction d'erreur augmente seule pour rester scannable. Changez points, encre et papier — ou passez au transparent.",f5l:"Codes avec logo →",f6t:"Historique privé",f6d:"Chaque téléchargement est mémorisé sur cet appareil uniquement — vos douze plus récents, un clic pour retrouver. Effacez à tout moment.",casesK:"Sur le terrain",casesT:"Pensé pour les vrais moments",casesS:"Choisissez votre scénario — la configuration est déjà prête.",c1t:"Cartes de visite",c1d:"Vos coordonnées en un scan — directement dans leur téléphone.",c2t:"Mariages",c2d:"RSVP, photos partagées, ajout au calendrier. La paperasse, sans papier.",c3t:"Immobilier",c3d:"Les annonces sur le panneau. Réservez une visite en un scan.",c4t:"Événements",c4d:"Enregistrement, validation des billets, albums partagés.",c5t:"Partage WiFi",c5d:"Invités connectés en un scan. Fini d'épeler les mots de passe.",c6t:"Avis Google",c6d:"Transformez vos clients satisfaits en cinq étoiles, au comptoir.",p1n:"N° 1",p1t:"Vos données ne bougent pas d'ici",p1p:"Chaque code est dessiné sur votre appareil — aucun envoi, aucun suivi, aucun compte. Chargez la page, déconnectez-vous, tout continue de marcher.",p2n:"N° 2",p2t:"Faits pour durer",p2p:"Un code statique porte sa destination dans le motif. Imprimez-le aujourd'hui, il se scannera dans dix ans. Ni renouvellement, ni plateforme qui disparaît.",p3n:"N° 3",p3t:"Gratuit veut dire gratuit",p3p:"Sans filigrane, sans mur d'inscription, sans expiration. Ni offre Pro, ni frais cachés — les bons outils devraient être gratuits.",faqT:"Bon à savoir",q1:"Un QR code gratuit expire-t-il ?",a1:"Jamais. La destination est encodée dans le motif, donc il marche tant que la destination existe. Les codes dynamiques payants passent par les serveurs du fournisseur et peuvent mourir si vous arrêtez de payer — une raison de plus de préférer le statique.",q2:"Mon mot de passe WiFi est-il en sécurité ici ?",a2:"Oui. Votre mot de passe ne quitte jamais votre navigateur — rien n'est envoyé nulle part. Prudent ? Chargez la page, déconnectez-vous, puis tapez.",q3:"Statique ou dynamique ?",a3:"Si la destination ne changera pas, prenez statique : WiFi, cartes de visite, liens fixes. Les dynamiques (liens modifiables + stats) servent aux campagnes — c'est sur notre feuille de route.",q4:"Puis-je les utiliser commercialement ?",a4:"Bien sûr. Tout ce que vous créez ici vous appartient — emballages, menus, cartes, sans attribution.",q5:"FreeQrly est-il vraiment gratuit ?",a5:"Oui — tout sur cette page est gratuit, sans filigrane ni compte. Nous ne vendons pas d'abonnements ; c'est un outil, pas un entonnoir.",q6:"Faut-il un compte ?",a6:"Non. Il n'y a rien à quoi s'inscrire — ouvrez la page et créez votre code.",q7:"Puis-je ajouter mon logo au QR code ?",a7:"Oui — envoyez un logo carré, nous le plaçons au centre en augmentant automatiquement la correction d'erreur pour qu'il reste scannable. Pour l'impression, utilisez Q ou H.",fin:"Fait en silence, dans votre navigateur.",dl:"Télécharger",navScan:"Scanner",history:"Récents",histClear:"Effacer",transparent:"Fond transparent",types:{"url": ["Site web", "lien, page, vidéo"], "text": ["Texte", "n'importe quels mots"], "wifi": ["WiFi", "connexion instantanée"], "vcard": ["Contact", "vCard"], "email": ["E-mail", "pré-rempli"], "sms": ["SMS", "texte pré-rempli"], "phone": ["Appel", "toucher pour appeler"], "geo": ["Lieu", "épingle carte"],"event":["Événement","ajouter au calendrier"],"batch":["Lot", "plusieurs à la fois"]},fields:{"url": [["url", "Destination", "https://example.com"]], "text": [["text", "Message", "textarea", "Bonjour, le monde !"]], "wifi": [["ssid", "Nom du réseau", "MonWiFi"], ["pass", "Mot de passe", "", "Mot de passe WiFi"], ["enc", "Sécurité", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "Nom complet", "Marie Dupont"], ["phone", "Téléphone", "+33 6 00 00 00 00"], ["email", "E-mail", "marie@example.com"]], "email": [["to", "À", "bonjour@example.com"], ["subject", "Objet", "Bonjour"], ["body", "Corps", "textarea", "Corps de l'e-mail…"]], "sms": [["phone", "Téléphone", "+33 6 00 00 00 00"], ["body", "Message", "", "Écrivez votre message…"]], "phone": [["phone", "Téléphone", "+33 6 00 00 00 00"]], "geo": [["lat", "Latitude", "48.8566"], ["lng", "Longitude", "2.3522"]],"event":[["etitle","Titre","","ex. : Anniversaire"],["estart","Début","datetime-local"],["eend","Fin","datetime-local"],["eloc","Lieu","","ex. : Parc Central"],["edesc","Détails","textarea","Détails de l'événement…"]]}},
de:{title:"FreeQrly — Kostenloser QR-Code-Generator | Ohne Anmeldung",metaDesc:"QR-Codes kostenlos im Browser erstellen – sogar mit deinem Logo. Ohne Anmeldung, ohne Tracking, ohne Ablauf. Export als PNG & SVG.",navStudio:"Studio",navWhy:"Prinzipien",navFaq:"Fragen",kicker:"Kostenlos · Ohne Anmeldung · Privat per Design",h1a:"Leise Codes für",h1b:"laute",h1c:"Orte.",lede:"Erstelle schöne QR-Codes direkt im Browser — ohne Anmeldung, ohne Tracking, ohne Ablauf. Kostenlos, einfach und für immer deine.",hc1:"Inhaltstypen",hc2:"Export",hc3:"Deine Daten",hc3v:"Bleiben bei dir",hc4:"Preis",hc4v:"Für immer gratis",sOver:"Das Studio",sTitle:"Erstelle deinen QR-Code",appearance:"Darstellung",ink:"Tinte",paper:"Papier",background:"Hintergrund",dots:"Punktstil",ecc:"Fehlerkorrektur",dSquare:"Eckig",dRound:"Rund",dSoft:"Weich",dPebble:"Kiesel",eL:"Niedrig",eM:"Mittel",eQ:"Hoch",eH:"Maximal",eccHint:"Höher = robuster gegen Logos und Verschleiß.",dotsSub:"Punktform",eccSub:"Höher = robuster",colors:"Farben",colorsSub:"Tippen oder anpassen",transparentSub:"Ohne weißen Hintergrund",size:"Exportgröße",logo:"Logo hinzufügen",logoSub:"Marke oder eigen",privnote:"Alles wird lokal in Ihrem Browser erzeugt.",live:"Live-Vorschau — ändert sich beim Tippen",bLabel:"Ein Link pro Zeile",bGo:"Alle erzeugen",bZip:"ZIP laden",bEmpty:"Gib oben mindestens einen Link ein",featsK:"Mehr als Code",featsT:"Alles rund um den QR",featsS:"Generieren ist nur der Anfang. Das steckt auch in FreeQrly.",f1t:"Scanner eingebaut",f1d:"Kamera draufhalten oder Bild hochladen — Codes werden direkt in deinem Browser entschlüsselt und nirgends hochgeladen. Funktioniert sogar offline.",f1l:"Scanner öffnen →",f2t:"10 Code-Typen",f2d:"Website, Text, WLAN, Visitenkarten, E-Mail, SMS, Anrufe, Orte, Kalenderevents. Jeder Typ baut automatisch das richtige Format — keine Syntax pauken.",f2l:"Alle ausprobieren →",f3t:"Stapelverarbeitung",f3d:"Bis zu 50 Links einfügen, 50 druckfertige Codes mit einem Klick. Einzeln laden oder alles als ZIP.",f3l:"Stapelmodus →",f4t:"Kalender-Event-Codes",f4d:"Ein Scan und deine Veranstaltung — Titel, Zeit, Ort — landet direkt im Kalender des Gastes. Gemacht für Einladungen.",f4l:"Event-Code erstellen →",f5t:"Logo & Styling",f5d:"Logo in die Mitte setzen — die Fehlerkorrektur steigt automatisch, damit es scanbar bleibt. Punkte, Tinte, Papier anpassen — oder transparent.",f5l:"Codes mit Logo →",f6t:"Privater Verlauf",f6d:"Jeder Download wird nur auf diesem Gerät gemerkt — deine zwölf neuesten, ein Klick zum Wiederherstellen. Jederzeit löschbar.",casesK:"In freier Wildbahn",casesT:"Für echte Momente gemacht",casesS:"Wähl dein Szenario — das Setup steht schon.",c1t:"Visitenkarten",c1d:"Deine Kontaktdaten in einem Scan — direkt aufs Handy.",c2t:"Hochzeiten",c2d:"RSVP, Fotoalben, Kalender-Eintrag. Der Papierkram, ohne Papier.",c3t:"Immobilien",c3d:"Exposés am Schild. Besichtigung in einem Scan buchen.",c4t:"Events",c4d:"Check-in, Ticketprüfung, geteilte Alben.",c5t:"WLAN teilen",c5d:"Gäste in einem Scan online. Nie wieder Passwörter buchstabieren.",c6t:"Google-Bewertungen",c6d:"Aus zufriedenen Kunden Fünf-Sterne direkt an der Theke machen.",p1n:"Nr. 1",p1t:"Deine Daten gehen nirgendwo hin",p1p:"Jeder Code wird auf deinem Gerät gezeichnet — keine Uploads, kein Tracking, keine Konten. Seite laden, Stecker ziehen, alles läuft weiter.",p2n:"Nr. 2",p2t:"Gemacht für die Dauer",p2p:"Ein statischer Code trägt sein Ziel im Muster. Heute drucken, in zehn Jahren scannen. Keine Verlängerung, keine Plattform, die verschwindet.",p3n:"Nr. 3",p3t:"Gratis heißt gratis",p3p:"Kein Wasserzeichen, keine Anmeldewand, kein Ablauf. Kein Pro-Tarif, keine versteckten Kosten — gute Werkzeuge sollten einfach gratis sein.",faqT:"Gut zu wissen",q1:"Laufen kostenlose QR-Codes ab?",a1:"Nie. Das Ziel ist direkt im Muster codiert — der Code funktioniert, solange das Ziel existiert. Bezahlte dynamische Codes laufen über Server des Anbieters und können sterben, wenn du nicht mehr zahlst — ein Grund mehr für statisch.",q2:"Ist mein WLAN-Passwort hier sicher?",a2:"Ja. Dein Passwort verlässt nie deinen Browser — nichts wird irgendwohin gesendet. Vorsichtig? Seite laden, offline gehen, dann tippen.",q3:"Statisch oder dynamisch?",a3:"Wenn sich das Ziel nicht ändert: statisch — WLAN, Visitenkarten, feste Links. Dynamische Codes (änderbare Links + Statistiken) sind für Kampagnen — stehen auf unserer Roadmap.",q4:"Darf ich sie kommerziell nutzen?",a4:"Absolut. Alles, was du hier erstellst, gehört dir — Verpackungen, Speisekarten, Karten, ohne Namensnennung.",q5:"Ist FreeQrly wirklich kostenlos?",a5:"Ja — alles auf dieser Seite ist gratis, ohne Wasserzeichen und ohne Konto. Wir verkaufen keine Abos; das hier ist ein Werkzeug, kein Trichter.",q6:"Brauche ich ein Konto?",a6:"Nein. Es gibt nichts anzumelden — Seite öffnen, Code erstellen.",q7:"Kann ich mein Logo in den QR-Code setzen?",a7:"Ja — lade ein quadratisches Logo hoch, wir setzen es in die Mitte und erhöhen automatisch die Fehlerkorrektur, damit er scanbar bleibt. Für Druck: Q oder H.",fin:"Leise gemacht, in deinem Browser.",dl:"Herunterladen",navScan:"Scanner",history:"Zuletzt",histClear:"Löschen",transparent:"Transparenter Hintergrund",types:{"url": ["Webseite", "Link, Seite, Video"], "text": ["Text", "beliebige Wörter"], "wifi": ["WLAN", "sofort verbinden"], "vcard": ["Kontakt", "vCard"], "email": ["E-Mail", "vorausgefüllt"], "sms": ["SMS", "vorausgefüllter Text"], "phone": ["Anruf", "tippen zum Wählen"], "geo": ["Ort", "Karten-Pin"],"event":["Termin","zum Kalender"],"batch":["Stapel", "viele auf einmal"]},fields:{"url": [["url", "Ziel", "https://example.com"]], "text": [["text", "Nachricht", "textarea", "Hallo, Welt!"]], "wifi": [["ssid", "Netzwerkname", "MeinWLAN"], ["pass", "Passwort", "", "WLAN-Passwort"], ["enc", "Verschlüsselung", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "Vollständiger Name", "Max Mustermann"], ["phone", "Telefon", "+49 170 000000"], ["email", "E-Mail", "max@example.com"]], "email": [["to", "An", "hallo@example.com"], ["subject", "Betreff", "Hallo"], ["body", "Text", "textarea", "E-Mail-Text…"]], "sms": [["phone", "Telefon", "+49 170 000000"], ["body", "Nachricht", "", "Nachricht eingeben…"]], "phone": [["phone", "Telefon", "+49 170 000000"]], "geo": [["lat", "Breitengrad", "52.5200"], ["lng", "Längengrad", "13.4050"]],"event":[["etitle","Titel","","z. B. Geburtstagsparty"],["estart","Beginn","datetime-local"],["eend","Ende","datetime-local"],["eloc","Ort","","z. B. Central Park"],["edesc","Details","textarea","Veranstaltungsdetails…"]]}},
ja:{title:"FreeQrly — 無料QRコード生成 | 登録不要",metaDesc:"ブラウザで無料QRコードを作成。ロゴ入りもOK。登録不要・追跡なし・無期限。PNG / SVGで書き出し。",navStudio:"スタジオ",navWhy:"こだわり",navFaq:"よくある質問",kicker:"無料 · 登録不要 · プライバシー優先",h1a:"静かなコードを、",h1b:"にぎやかな",h1c:"場所へ。",lede:"ブラウザで美しいQRコードを作ろう — 登録不要、追跡なし、無期限。無料で、シンプルで、ずっとあなたのもの。",hc1:"コンテンツの種類",hc2:"書き出し",hc3:"あなたのデータ",hc3v:"あなたの手元に",hc4:"料金",hc4v:"ずっと無料",sOver:"スタジオ",sTitle:"QRコードを作る",appearance:"見た目",ink:"インク",paper:"用紙",background:"背景",dots:"ドットの形",ecc:"誤り訂正",dSquare:"四角",dRound:"丸",dSoft:"やわらか",dPebble:"小石",eL:"低",eM:"中",eQ:"高",eH:"最高",eccHint:"レベルが高いほどロゴや摩耗に強い。",dotsSub:"ドットの形",eccSub:"高いほど丈夫",colors:"色",colorsSub:"タップまたはカスタム",transparentSub:"白背景なし",size:"書き出しサイズ",logo:"ロゴを追加",logoSub:"ブランドまたは自作",privnote:"すべてブラウザ内でローカルに生成されます。",live:"ライブプレビュー — 入力と同時に変わる",bLabel:"1行に1リンク",bGo:"すべて生成",bZip:"ZIPをダウンロード",bEmpty:"まず上にリンクを1つ以上入力してください",featsK:"コードの先へ",featsT:"QRの周りのすべて",featsS:"生成は始まりにすぎません。FreeQrlyにはこんなものも。",f1t:"内蔵スキャナー",f1d:"カメラを向けるか画像をアップ—コードはブラウザ内で直接読み取られ、サーバーに送信されません。オフラインでも動作します。",f1l:"スキャナーを開く →",f2t:"10種類のコード",f2d:"Web、テキスト、WiFi、名刺、メール、SMS、通話、場所、カレンダー予定。各タイプが正しい形式を自動生成—書式を覚える必要なし。",f2l:"全部試す →",f3t:"一括生成",f3d:"リンクを50件まで貼り付けて、ワンクリックで50個の印刷用コードに。個別にもZIPまとめでもダウンロード。",f3l:"一括モード →",f4t:"予定コード",f4d:"スキャンひとつで予定—タイトル・時間・場所—がゲストのカレンダーに。招待状のために生まれました。",f4l:"予定コードを作る →",f5t:"ロゴとスタイル",f5d:"中央にロゴを置けば、読み取り精度を保つため誤り訂正が自動で上がります。ドット・インク・用紙を変更—透明背景も。",f5l:"ロゴ入りコード →",f6t:"プライベート履歴",f6d:"ダウンロードはこのデバイスにだけ記憶—最新12件をワンクリックで復元。いつでも消去できます。",casesK:"現場で",casesT:"リアルな瞬間のために",casesS:"シーンを選ぶだけ—設定は用意済みです。",c1t:"名刺",c1d:"スキャンひとつで連絡先が相手のスマホに。",c2t:"結婚式",c2d:"出欠確認・写真共有・カレンダー登録。紙の手続きを、紙なしで。",c3t:"不動産",c3d:"看板の物件情報をスキャン。そのまま内見予約。",c4t:"イベント",c4d:"チェックイン、チケット確認、共有アルバム。",c5t:"WiFi共有",c5d:"ゲストはスキャンひとつで接続。パスワードを読み上げる時代は終わり。",c6t:"Googleレビュー",c6d:"満足したお客様を、その場で星5つの評価に。",p1n:"その一",p1t:"データはどこにも行かない",p1p:"すべてのコードはあなたのデバイス上で描画 — アップロードなし、追跡なし、アカウント不要。ページを読み込んで、回線を抜いても、そのまま使えます。",p2n:"その二",p2t:"長持ちする作り",p2p:"静的コードは行き先を模様の中に持ちます。今日印刷して、10年後も読み取れます。更新も、消えるプラットフォームの心配もなし。",p3n:"その三",p3t:"無料は、ただの無料",p3p:"透かしなし、登録の壁なし、期限なし。Pro版も隠れた料金もなし — 良い道具は無料であるべきです。",faqT:"知っておきたいこと",q1:"無料のQRコードに期限はある？",a1:"ありません。行き先は模様に直接記録されるので、行き先が有効な限り使えます。有料の動的コードは事業者のサーバー経由で、支払いを止めると使えなくなることも — 静的コードが安心な理由です。",q2:"WiFiのパスワードを入力しても安全？",a2:"安全です。パスワードがブラウザの外に出ることはありません。心配なら、ページを読み込んでからネットを切って入力してください。",q3:"静的と動的、どっちを選ぶ？",a3:"行き先が変わらないなら静的:WiFi、名刺、固定リンク。動的(書き換え可能なリンク+読み取り統計)はキャンペーン向け — ロードマップに入っています。",q4:"商用利用できる？",a4:"もちろんです。ここで作ったコードはすべてあなたのもの — パッケージ、メニュー、名刺に、クレジット表記不要で使えます。",q5:"FreeQrlyは本当に無料？",a5:"本当です。このページの機能はすべて無料、透かしもアカウントも不要。サブスクの販売はしていません — これは道具であって、売り込みではありません。",q6:"アカウントは必要？",a6:"不要です。登録するものは何もありません — ページを開いて、コードを作るだけ。",q7:"QRコードにロゴを入れられる？",a7:"はい — 正方形のロゴをアップすると中央に配置し、誤り訂正を自動で上げて読み取り可能に保ちます。印刷用にはQかHをどうぞ。",fin:"ブラウザの中で、静かに生成。",dl:"ダウンロード",navScan:"スキャナー",history:"履歴",histClear:"クリア",transparent:"透明な背景",types:{"url": ["ウェブサイト", "リンク、ページ、動画"], "text": ["テキスト", "好きな言葉"], "wifi": ["WiFi", "すぐ接続"], "vcard": ["連絡先", "vCard"], "email": ["メール", "下書き付き"], "sms": ["SMS", "本文付き"], "phone": ["電話", "タップで発信"], "geo": ["場所", "マップのピン"],"event":["イベント","カレンダーに追加"],"batch":["一括", "まとめて複数"]},fields:{"url": [["url", "行き先", "https://example.com"]], "text": [["text", "メッセージ", "textarea", "こんにちは、世界！"]], "wifi": [["ssid", "ネットワーク名", "MyWiFi"], ["pass", "パスワード", "", "WiFiパスワード"], ["enc", "暗号化", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "氏名", "山田太郎"], ["phone", "電話", "+81 90 0000 0000"], ["email", "メール", "taro@example.com"]], "email": [["to", "宛先", "hello@example.com"], ["subject", "件名", "こんにちは"], ["body", "本文", "textarea", "メール本文…"]], "sms": [["phone", "電話", "+81 90 0000 0000"], ["body", "メッセージ", "", "メッセージを入力…"]], "phone": [["phone", "電話", "+81 90 0000 0000"]], "geo": [["lat", "緯度", "35.6762"], ["lng", "経度", "139.6503"]],"event":[["etitle","タイトル","","例：誕生日パーティ"],["estart","開始","datetime-local"],["eend","終了","datetime-local"],["eloc","場所","","例：中央公園"],["edesc","詳細","textarea","イベント詳細…"]]}},
ru:{title:"FreeQrly — бесплатный генератор QR-кодов | Без регистрации",metaDesc:"Создавайте QR-коды бесплатно прямо в браузере — даже с вашим логотипом. Без регистрации, без слежки, без срока действия. Экспорт в PNG и SVG.",navStudio:"Студия",navWhy:"Принципы",navFaq:"Вопросы",kicker:"Бесплатно · Без регистрации · Приватность по дизайну",h1a:"Тихие коды для",h1b:"шумных",h1c:"мест.",lede:"Создавайте красивые QR-коды прямо в браузере — без регистрации, без слежки, без срока действия. Бесплатно, просто и навсегда ваши.",hc1:"Типы контента",hc2:"Экспорт",hc3:"Ваши данные",hc3v:"Остаются у вас",hc4:"Цена",hc4v:"Бесплатно, навсегда",sOver:"Студия",sTitle:"Создать QR-код",appearance:"Внешний вид",ink:"Чернила",paper:"Бумага",background:"Фон",dots:"Форма точек",ecc:"Коррекция ошибок",dSquare:"Квадрат",dRound:"Круг",dSoft:"Мягкий",dPebble:"Галька",eL:"Низкий",eM:"Средний",eQ:"Высокий",eH:"Максимум",eccHint:"Чем выше уровень, тем устойчивее к логотипам и износу.",dotsSub:"Форма точек",eccSub:"Выше — прочнее",colors:"Цвета",colorsSub:"Выберите или настройте",transparentSub:"Без белого фона",size:"Размер экспорта",logo:"Добавить логотип",logoSub:"Бренд или свой",privnote:"Всё генерируется локально в вашем браузере.",live:"Живой предпросмотр — меняется при вводе",bLabel:"Одна ссылка на строку",bGo:"Создать все",bZip:"Скачать ZIP",bEmpty:"Сначала введите хотя бы одну ссылку выше",featsK:"Больше, чем код",featsT:"Всё вокруг QR",featsS:"Генерация — только начало. Внутри FreeQrly есть и это.",f1t:"Встроенный сканер",f1d:"Наведите камеру или загрузите изображение — коды расшифровываются прямо в браузере и никуда не отправляются. Работает даже офлайн.",f1l:"Открыть сканер →",f2t:"10 типов кодов",f2d:"Сайт, текст, WiFi, визитки, почта, SMS, звонки, места, события календаря. Каждый тип сам строит правильный формат — ничего запоминать не нужно.",f2l:"Попробовать все →",f3t:"Пакетная генерация",f3d:"Вставьте до 50 ссылок и получите 50 готовых к печати кодов в один клик. Скачивайте по одному или всё сразу в ZIP.",f3l:"Пакетный режим →",f4t:"Коды событий",f4d:"Одно сканирование — и ваше событие с названием, временем и местом окажется в календаре гостя. Создано для приглашений.",f4l:"Создать код события →",f5t:"Логотип и стиль",f5d:"Поставьте логотип в центр — коррекция ошибок повысится сама, чтобы код продолжал считываться. Меняйте точки, чернила и бумагу — или сделайте фон прозрачным.",f5l:"Коды с логотипом →",f6t:"Приватная история",f6d:"Каждое скачивание запоминается только на этом устройстве — двенадцать последних, возврат в один клик. Очистите в любой момент.",casesK:"В реальной жизни",casesT:"Создано для настоящих моментов",casesS:"Выберите свой сценарий — настройка уже готова.",c1t:"Визитки",c1d:"Ваши контакты в одно сканирование — прямо в их телефон.",c2t:"Свадьбы",c2d:"RSVP, общие фото, добавление в календарь. Бумажная волокита — без бумаги.",c3t:"Недвижимость",c3d:"Объявления на стенде. Запись на просмотр в одно сканирование.",c4t:"Мероприятия",c4d:"Регистрация, проверка билетов, общие альбомы.",c5t:"Раздача WiFi",c5d:"Гости в сети в одно сканирование. Больше не диктуйте пароль.",c6t:"Отзывы в Google",c6d:"Превращайте довольных клиентов в пять звёзд прямо у стойки.",p1n:"№ 1",p1t:"Ваши данные никуда не уходят",p1p:"Каждый код рисуется на вашем устройстве — без загрузок, без слежки, без аккаунтов. Загрузите страницу, выдерните кабель — всё продолжит работать.",p2n:"№ 2",p2t:"Сделаны надолго",p2p:"Статический код несёт адрес внутри узора. Напечатайте сегодня — отсканируется и через десять лет. Без продлений и исчезающих платформ.",p3n:"№ 3",p3t:"Бесплатно значит бесплатно",p3p:"Без водяных знаков, без стены регистрации, без срока действия. Без Pro-тарифа и скрытых платежей — хорошие инструменты должны быть бесплатными.",faqT:"Полезно знать",q1:"Бесплатные QR-коды истекают?",a1:"Никогда. Адрес закодирован прямо в узоре, поэтому код работает, пока работает адрес. Платные динамические коды идут через серверы поставщика и могут умереть, если перестать платить, — ещё одна причина любить статику.",q2:"Мой пароль от WiFi здесь в безопасности?",a2:"Да. Пароль никогда не покидает ваш браузер — ничего никуда не отправляется. Перестраховаться? Загрузите страницу, отключитесь и вводите.",q3:"Статический или динамический?",a3:"Если адрес не изменится — статический: WiFi, визитки, постоянные ссылки. Динамические (изменяемые ссылки + статистика) — для кампаний, они в нашей дорожной карте.",q4:"Можно использовать в коммерческих целях?",a4:"Конечно. Всё созданное здесь — ваше: упаковка, меню, визитки, без указания авторства.",q5:"FreeQrly правда бесплатный?",a5:"Да — всё на этой странице бесплатно, без водяных знаков и аккаунта. Мы не продаём подписки; это инструмент, а не воронка.",q6:"Нужен аккаунт?",a6:"Нет. Регистрироваться негде — откройте страницу и создайте код.",q7:"Можно добавить логотип в QR-код?",a7:"Да — загрузите квадратный логотип, мы разместим его в центре и автоматически повысим коррекцию ошибок, чтобы код сканировался. Для печати выбирайте Q или H.",fin:"Сделано тихо, в вашем браузере.",dl:"Скачать",navScan:"Сканер",history:"Недавние",histClear:"Очистить",transparent:"Прозрачный фон",types:{"url": ["Сайт", "ссылка, страница, видео"], "text": ["Текст", "любые слова"], "wifi": ["WiFi", "мгновенное подключение"], "vcard": ["Контакт", "vCard"], "email": ["Почта", "с заготовкой"], "sms": ["SMS", "с текстом"], "phone": ["Звонок", "нажать для вызова"], "geo": ["Место", "метка на карте"],"event":["Событие","в календарь"],"batch":["Пакет", "много сразу"]},fields:{"url": [["url", "Адрес", "https://example.com"]], "text": [["text", "Сообщение", "textarea", "Привет, мир!"]], "wifi": [["ssid", "Имя сети", "MyWiFi"], ["pass", "Пароль", "", "Пароль WiFi"], ["enc", "Защита", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "Полное имя", "Иван Петров"], ["phone", "Телефон", "+7 900 000-00-00"], ["email", "Почта", "ivan@example.com"]], "email": [["to", "Кому", "hello@example.com"], ["subject", "Тема", "Привет"], ["body", "Текст", "textarea", "Текст письма…"]], "sms": [["phone", "Телефон", "+7 900 000-00-00"], ["body", "Сообщение", "", "Введите сообщение…"]], "phone": [["phone", "Телефон", "+7 900 000-00-00"]], "geo": [["lat", "Широта", "55.7558"], ["lng", "Долгота", "37.6173"]],"event":[["etitle","Название","","напр. День рождения"],["estart","Начало","datetime-local"],["eend","Конец","datetime-local"],["eloc","Место","","напр. Центральный парк"],["edesc","Детали","textarea","Детали события…"]]}},
hi:{title:"FreeQrly — मुफ़्त QR कोड जनरेटर | बिना साइन-अप",metaDesc:"अपने ब्राउज़र में मुफ़्त QR कोड बनाएं — अपने लोगो के साथ भी। बिना साइन-अप, बिना ट्रैकिंग, बिना एक्सपायरी। PNG व SVG एक्सपोर्ट।",navStudio:"स्टूडियो",navWhy:"सिद्धांत",navFaq:"सवाल",kicker:"मुफ़्त · बिना साइन-अप · प्राइवेसी पहले",h1a:"शोर वाली जगहों के लिए",h1b:"ख़ामोश",h1c:"कोड।",lede:"अपने ब्राउज़र में ही सुंदर QR कोड बनाएं — बिना साइन-अप, बिना ट्रैकिंग, बिना एक्सपायरी। मुफ़्त, आसान, हमेशा आपका।",hc1:"कंटेंट के प्रकार",hc2:"एक्सपोर्ट",hc3:"आपका डेटा",hc3v:"आपके पास ही रहता है",hc4:"क़ीमत",hc4v:"हमेशा मुफ़्त",sOver:"स्टूडियो",sTitle:"अपना QR कोड बनाएं",appearance:"रूप-रंग",ink:"स्याही",paper:"काग़ज़",background:"पृष्ठभूमि",dots:"बिंदुओं की शैली",ecc:"एरर करेक्शन",dSquare:"चौकोर",dRound:"गोल",dSoft:"नर्म",dPebble:"कंकड़",eL:"कम",eM:"मध्यम",eQ:"उच्च",eH:"अधिकतम",eccHint:"लेवल जितना ऊंचा, लोगो और घिसाव से उतना सुरक्षित।",dotsSub:"QR बिंदु आकार",eccSub:"अधिक टिकाऊ",colors:"रंग",colorsSub:"चुनें या कस्टमाइज़ करें",transparentSub:"सफेद पृष्ठभूमि नहीं",size:"एक्सपोर्ट साइज़",logo:"अपना लोगो जोड़ें",logoSub:"ब्रांड या अपना",privnote:"सब कुछ आपके ब्राउज़र में स्थानीय रूप से बनता है।",live:"लाइव प्रीव्यू — लिखते ही बदलेगा",bLabel:"हर लाइन में एक लिंक",bGo:"सभी बनाएं",bZip:"ZIP डाउनलोड करें",bEmpty:"पहले ऊपर कम से कम एक लिंक लिखें",featsK:"कोड से आगे",featsT:"QR के आसपास सब कुछ",featsS:"बनाना तो शुरुआत है। FreeQrly में ये सब भी है।",f1t:"बिल्ट-इन स्कैनर",f1d:"कैमरा लगाएं या इमेज अपलोड करें — कोड आपके ब्राउज़र में ही डिकोड होता है, कभी सर्वर पर अपलोड नहीं होता। ऑफलाइन भी चलता है।",f1l:"स्कैनर खोलें →",f2t:"10 तरह के कोड",f2d:"वेबसाइट, टेक्स्ट, WiFi, संपर्क कार्ड, ईमेल, SMS, कॉल, लोकेशन, कैलेंडर इवेंट। हर तरह का सही फॉर्मेट अपने आप — कोई syntax याद नहीं करना।",f2l:"सभी आज़माएं →",f3t:"बैच जनरेशन",f3d:"50 लिंक पेस्ट करें, एक क्लिक में 50 प्रिंट-रेडी कोड पाएं। एक-एक करके डाउनलोड करें या ZIP में लें।",f3l:"बैच मोड →",f4t:"कैलेंडर इवेंट कोड",f4d:"एक स्कैन में आपका इवेंट — टाइटल, समय, जगह — सीधे मेहमान के फोन कैलेंडर में। निमंत्रण के लिए बना है।",f4l:"इवेंट कोड बनाएं →",f5t:"लोगो और स्टाइल",f5d:"बीच में अपना लोगो लगाएं, स्कैन होता रहे इसलिए एरर करेक्शन अपने आप बढ़ जाता है। डॉट्स, रंग बदलें — या पारदर्शी बैकग्राउंड।",f5l:"लोगो वाले कोड →",f6t:"प्राइवेट हिस्ट्री",f6d:"हर डाउनलोड सिर्फ इसी डिवाइस पर याद रहता है — आपके 12 ताज़ा, एक क्लिक में वापस। कभी भी साफ़ करें।",casesK:"असल दुनिया में",casesT:"असली पलों के लिए बना",casesS:"अपना सीन चुनें — सेटअप पहले से तैयार है।",c1t:"बिज़नेस कार्ड",c1d:"एक स्कैन में आपके संपर्क — सीधे उनके फोन में।",c2t:"शादियां",c2d:"RSVP, फोटो शेयरिंग, कैलेंडर में जोड़ें। कागज़ी काम, बिना कागज़।",c3t:"रियल एस्टेट",c3d:"साइनबोर्ड पर लिस्टिंग। एक स्कैन में विज़िट बुक करें।",c4t:"इवेंट",c4d:"चेक-इन, टिकट वेरिफिकेशन, शेयर की गई एल्बम।",c5t:"WiFi शेयरिंग",c5d:"मेहमान एक स्कैन में ऑनलाइन। पासवर्ड बोलना बंद।",c6t:"Google रिव्यू",c6d:"खुश ग्राहकों को काउंटर पर ही पांच स्टार बनाएं।",p1n:"नं. 1",p1t:"आपका डेटा कहीं नहीं जाता",p1p:"हर कोड आपके डिवाइस पर बनता है — न अपलोड, न ट्रैकिंग, न अकाउंट। पेज लोड करें, नेट बंद करें, सब चलता रहेगा।",p2n:"नं. 2",p2t:"टिकने के लिए बने",p2p:"स्टैटिक कोड अपना पता पैटर्न में ही रखता है। आज प्रिंट करें, दस साल बाद भी स्कैन होगा। न रिन्यूअल, न ग़ायब होने वाले प्लेटफ़ॉर्म।",p3n:"नं. 3",p3t:"मुफ़्त मतलब मुफ़्त",p3p:"न वॉटरमार्क, न साइन-अप की दीवार, न एक्सपायरी। न Pro प्लान, न छिपे चार्ज — अच्छे टूल मुफ़्त ही होने चाहिए।",faqT:"जानना अच्छा रहेगा",q1:"क्या मुफ़्त QR कोड एक्सपायर होते हैं?",a1:"कभी नहीं। पता पैटर्न में ही कोड होता है, इसलिए जब तक पता चलेगा, कोड चलेगा। पेड डायनामिक कोड कंपनी के सर्वर से चलते हैं और पेमेंट रुकते ही बंद हो सकते हैं — स्टैटिक को चुनने की एक और वजह।",q2:"क्या मेरा WiFi पासवर्ड यहां सुरक्षित है?",a2:"हां। आपका पासवर्ड आपके ब्राउज़र से बाहर नहीं जाता — कुछ भी कहीं नहीं भेजा जाता। ज़्यादा सावधानी? पेज लोड करें, नेट बंद करें, फिर लिखें।",q3:"स्टैटिक या डायनामिक?",a3:"अगर पता नहीं बदलेगा तो स्टैटिक: WiFi, विज़िटिंग कार्ड, फिक्स्ड लिंक। डायनामिक (बदले जा सकने वाले लिंक + स्कैन आंकड़े) कैंपेन के लिए हैं — हमारे रोडमैप में हैं।",q4:"क्या व्यावसायिक इस्तेमाल कर सकते हैं?",a4:"बिल्कुल। यहां बना हर कोड आपका है — पैकेजिंग, मेन्यू, कार्ड, बिना क्रेडिट के।",q5:"क्या FreeQrly सच में मुफ़्त है?",a5:"हां — इस पेज की हर चीज़ मुफ़्त है, बिना वॉटरमार्क और अकाउंट के। हम सब्सक्रिप्शन नहीं बेचते; यह एक टूल है, जाल नहीं।",q6:"क्या अकाउंट चाहिए?",a6:"नहीं। साइन-अप करने को कुछ नहीं है — पेज खोलें और कोड बनाएं।",q7:"क्या QR कोड में अपना लोगो लगा सकते हैं?",a7:"हां — चौकोर लोगो अपलोड करें, हम उसे बीच में लगाएंगे और एरर करेक्शन अपने आप बढ़ा देंगे ताकि स्कैन होता रहे। प्रिंट के लिए Q या H चुनें।",fin:"आपके ब्राउज़र में, चुपचाप बनाया गया।",dl:"डाउनलोड",navScan:"स्कैनर",history:"हाल के",histClear:"साफ़ करें",transparent:"पारदर्शी पृष्ठभूमि",types:{"url": ["वेबसाइट", "लिंक, पेज, वीडियो"], "text": ["टेक्स्ट", "कोई भी शब्द"], "wifi": ["WiFi", "तुरंत जुड़ें"], "vcard": ["संपर्क", "vCard"], "email": ["ईमेल", "पहले से भरा"], "sms": ["SMS", "पहले से भरा टेक्स्ट"], "phone": ["कॉल", "डायल करें"], "geo": ["जगह", "मैप पिन"],"event":["इवेंट","कैलेंडर में जोड़ें"],"batch":["बैच", "एक साथ कई"]},fields:{"url": [["url", "गंतव्य", "https://example.com"]], "text": [["text", "संदेश", "textarea", "नमस्ते दुनिया!"]], "wifi": [["ssid", "नेटवर्क का नाम", "MyWiFi"], ["pass", "पासवर्ड", "", "WiFi पासवर्ड"], ["enc", "सुरक्षा", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "पूरा नाम", "राहुल शर्मा"], ["phone", "फ़ोन", "+91 98765 43210"], ["email", "ईमेल", "rahul@example.com"]], "email": [["to", "प्राप्तकर्ता", "hello@example.com"], ["subject", "विषय", "नमस्ते"], ["body", "मुख्य भाग", "textarea", "ईमेल सामग्री…"]], "sms": [["phone", "फ़ोन", "+91 98765 43210"], ["body", "संदेश", "", "अपना संदेश लिखें…"]], "phone": [["phone", "फ़ोन", "+91 98765 43210"]], "geo": [["lat", "अक्षांश", "28.6139"], ["lng", "देशांतर", "77.2090"]],"event":[["etitle","शीर्षक","","जैसे: जन्मदिन पार्टी"],["estart","प्रारंभ","datetime-local"],["eend","समाप्ति","datetime-local"],["eloc","स्थान","","जैसे: सेंट्रल पार्क"],["edesc","विवरण","textarea","इवेंट विवरण…"]]}},
ar:{title:"FreeQrly — مولّد QR مجاني | بدون تسجيل",metaDesc:"أنشئ رموز QR مجانية في متصفحك — حتى مع شعارك. بدون تسجيل، بدون تتبع، بدون انتهاء. تصدير PNG وSVG.",navStudio:"الاستوديو",navWhy:"المبادئ",navFaq:"أسئلة",kicker:"مجاني · بدون تسجيل · خصوصية أولاً",h1a:"رموز",h1b:"هادئة",h1c:"لأماكن صاخبة.",lede:"اصنع رموز QR جميلة في متصفحك — بدون تسجيل، بدون تتبع، بدون انتهاء. مجاني وبسيط ولك للأبد.",hc1:"أنواع المحتوى",hc2:"تصدير",hc3:"بياناتك",hc3v:"تبقى معك",hc4:"السعر",hc4v:"مجاني للأبد",sOver:"الاستوديو",sTitle:"أنشئ رمز QR الخاص بك",appearance:"المظهر",ink:"الحبر",paper:"الورق",background:"الخلفية",dots:"شكل النقاط",ecc:"تصحيح الأخطاء",dSquare:"مربع",dRound:"دائري",dSoft:"ناعم",dPebble:"حصاة",eL:"منخفض",eM:"متوسط",eQ:"مرتفع",eH:"أقصى",eccHint:"كلما ارتفع المستوى زادت مقاومة الشعارات والتآكل.",dotsSub:"شكل النقاط",eccSub:"الأعلى أكثر متانة",colors:"الألوان",colorsSub:"اختر أو خصص",transparentSub:"بدون خلفية بيضاء",size:"حجم التصدير",logo:"أضف شعارك",logoSub:"علامة أو خاص",privnote:"كل شيء يُنشأ محلياً في متصفحك.",live:"معاينة حية — تتغير أثناء الكتابة",bLabel:"رابط واحد في كل سطر",bGo:"إنشاء الكل",bZip:"تنزيل ZIP",bEmpty:"أدخل رابطًا واحدًا على الأقل أعلاه أولًا",featsK:"أبعد من الرمز",featsT:"كل ما يحيط بالـ QR",featsS:"التوليد مجرد البداية. هذا أيضًا يعيش داخل FreeQrly.",f1t:"ماسح مدمج",f1d:"وجّه الكاميرا أو ارفع صورة — تُفكّ الرموز في متصفحك ولا تُرفع إلى أي خادم أبدًا. يعمل دون اتصال أيضًا.",f1l:"افتح الماسح →",f2t:"10 أنواع من الرموز",f2d:"موقع، نص، WiFi، بطاقات اتصال، بريد، SMS، مكالمات، مواقع، أحداث التقويم. كل نوع يبني التنسيق الصحيح — لا حاجة لحفظ أي صيغة.",f2l:"جرّبها جميعًا →",f3t:"توليد جماعي",f3d:"الصق حتى 50 رابطًا واحصل على 50 رمزًا جاهزًا للطباعة بنقرة واحدة. نزّلها واحدًا واحدًا أو كلها كملف ZIP.",f3l:"الوضع الجماعي →",f4t:"رموز أحداث التقويم",f4d:"مسحة واحدة تُدخل حدثك — العنوان والوقت والمكان — إلى تقويم هاتف الضيف مباشرة. صُنع للدعوات.",f4l:"أنشئ رمز حدث →",f5t:"الشعار والتنسيق",f5d:"ضع شعارك في المنتصف ويرتفع تصحيح الأخطاء تلقائيًا ليبقى قابلًا للمسح. غيّر النقاط والحبر والورق — أو اجعل الخلفية شفافة.",f5l:"رموز بشعار →",f6t:"سجل خاص",f6d:"كل تنزيل يُحفظ على هذا الجهاز فقط — أحدث اثني عشر، بنقرة واحدة للاسترجاع. امسحه متى شئت.",casesK:"في الواقع",casesT:"صُنع للحظات الحقيقية",casesS:"اختر سيناريوك — الإعداد جاهز مسبقًا.",c1t:"بطاقات الأعمال",c1d:"بيانات اتصالك بمسحة واحدة — إلى هاتفهم مباشرة.",c2t:"حفلات الزفاف",c2d:"تأكيد الحضور ومشاركة الصور والإضافة للتقويم. المعاملات الورقية، بلا ورق.",c3t:"العقارات",c3d:"القوائم على اللافتة. احجز معاينة بمسحة واحدة.",c4t:"الفعاليات",c4d:"تسجيل الدخول والتحقق من التذاكر والألبومات المشتركة.",c5t:"مشاركة WiFi",c5d:"الضيوف متصلون بمسحة واحدة. لا تُملي كلمة المرور مجددًا.",c6t:"تقييمات Google",c6d:"حوّل العملاء السعداء إلى خمس نجوم، عند الكاونتر مباشرة.",p1n:"رقم ١",p1t:"بياناتك لا تغادر مكانها",p1p:"كل رمز يُرسم على جهازك — لا رفع، لا تتبع، لا حسابات. حمّل الصفحة، افصل السلك، وسيستمر كل شيء.",p2n:"رقم ٢",p2t:"مصنوعة لتدوم",p2p:"الرمز الثابت يحمل وجهته داخل النقش. اطبعه اليوم وسيُمسح بعد عشر سنوات. لا تجديد ولا منصات تختفي.",p3n:"رقم ٣",p3t:"مجاني يعني مجاني",p3p:"لا علامة مائية، لا جدار تسجيل، لا انتهاء. لا خطة Pro ولا رسوم خفية — الأدوات الجيدة يجب أن تكون مجانية.",faqT:"من الجيد معرفته",q1:"هل تنتهي رموز QR المجانية؟",a1:"أبداً. الوجهة مشفّرة في النقش نفسه، فيعمل الرمز ما دامت الوجهة تعمل. الرموز الديناميكية المدفوعة تمر عبر خوادم المزوّد وقد تموت عند إيقاف الدفع — سبب آخر لتفضيل الثابت.",q2:"هل كلمة مرور WiFi آمنة هنا؟",a2:"نعم. كلمة المرور لا تغادر متصفحك أبداً — لا يُرسل شيء إلى أي مكان. حذر أكثر؟ حمّل الصفحة، افصل الاتصال، ثم اكتب.",q3:"ثابت أم ديناميكي؟",a3:"إذا كانت الوجهة لن تتغير فاختر الثابت: WiFi وبطاقات الأعمال والروابط الثابتة. الديناميكية (روابط قابلة للتعديل + إحصاءات) للحملات — وهي على خارطة طريقنا.",q4:"هل يمكن استخدامها تجارياً؟",a4:"بالتأكيد. كل ما تنشئه هنا لك — التغليف والقوائم والبطاقات، دون نسب.",q5:"هل FreeQrly مجاني حقاً؟",a5:"نعم — كل شيء في هذه الصفحة مجاني، بلا علامة مائية وبلا حساب. لا نبيع اشتراكات؛ هذه أداة وليست فخاً.",q6:"هل أحتاج حساباً؟",a6:"لا. لا يوجد ما تسجّل فيه — افتح الصفحة وأنشئ رمزك.",q7:"هل يمكن إضافة شعاري إلى رمز QR؟",a7:"نعم — ارفع شعاراً مربعاً وسنضعه في المنتصف مع رفع تصحيح الأخطاء تلقائياً ليبقى قابلاً للمسح. للطباعة اختر Q أو H.",fin:"صُنع بهدوء، في متصفحك.",dl:"تنزيل",navScan:"ماسح",history:"الأخيرة",histClear:"مسح",transparent:"خلفية شفافة",types:{"url": ["موقع", "رابط، صفحة، فيديو"], "text": ["نص", "أي كلمات"], "wifi": ["WiFi", "اتصال فوري"], "vcard": ["جهة اتصال", "vCard"], "email": ["بريد", "مُعبأ مسبقاً"], "sms": ["SMS", "نص مُعبأ"], "phone": ["اتصال", "اضغط للاتصال"], "geo": ["مكان", "دبوس خريطة"],"event":["فعالية","إضافة إلى التقويم"],"batch":["دفعة", "عدة مرات"]},fields:{"url": [["url", "الوجهة", "https://example.com"]], "text": [["text", "الرسالة", "textarea", "مرحباً بالعالم!"]], "wifi": [["ssid", "اسم الشبكة", "MyWiFi"], ["pass", "كلمة المرور", "", "كلمة مرور WiFi"], ["enc", "الأمان", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "الاسم الكامل", "أحمد محمد"], ["phone", "الهاتف", "+966 5 0000 0000"], ["email", "البريد", "ahmed@example.com"]], "email": [["to", "إلى", "hello@example.com"], ["subject", "الموضوع", "مرحباً"], ["body", "المتن", "textarea", "متن البريد…"]], "sms": [["phone", "الهاتف", "+966 5 0000 0000"], ["body", "الرسالة", "", "اكتب رسالتك…"]], "phone": [["phone", "الهاتف", "+966 5 0000 0000"]], "geo": [["lat", "خط العرض", "24.7136"], ["lng", "خط الطول", "46.6753"]],"event":[["etitle","العنوان","","مثال: حفلة عيد ميلاد"],["estart","البداية","datetime-local"],["eend","النهاية","datetime-local"],["eloc","المكان","","مثال: الحديقة المركزية"],["edesc","التفاصيل","textarea","تفاصيل الفعالية…"]]}}
};


const LANGS = ["en","zh","es","hi","ar","pt","fr","ru","de","ja"];
const LANGN = {en:"English",zh:"\u4e2d\u6587",es:"Espa\u00f1ol",hi:"\u0939\u093f\u0928\u094d\u0926\u0940",ar:"\u0627\u0644\u0639\u0631\u0628\u064a\u0629",pt:"Portugu\u00eas",fr:"Fran\u00e7ais",ru:"\u0420\u0443\u0441\u0441\u043a\u0438\u0439",de:"Deutsch",ja:"\u65e5\u672c\u8a9e"};
const LANGBCP = {en:"en",zh:"zh-CN",es:"es",hi:"hi",ar:"ar",pt:"pt",fr:"fr",ru:"ru",de:"de",ja:"ja"};
const GEO2LANG = {CN:"zh",HK:"zh",TW:"zh",MO:"zh",ES:"es",MX:"es",AR:"es",CO:"es",CL:"es",PE:"es",VE:"es",EC:"es",GT:"es",CU:"es",BO:"es",DO:"es",HN:"es",PY:"es",SV:"es",NI:"es",CR:"es",PA:"es",UY:"es",BR:"pt",PT:"pt",AO:"pt",MZ:"pt",FR:"fr",BE:"fr",SN:"fr",CI:"fr",DE:"de",AT:"de",JP:"ja",IN:"hi",SA:"ar",EG:"ar",AE:"ar",DZ:"ar",MA:"ar",IQ:"ar",RU:"ru",BY:"ru"};
const TZ2LANG = {"Asia/Shanghai":"zh","Asia/Taipei":"zh","Asia/Hong_Kong":"zh","Asia/Macau":"zh","Asia/Urumqi":"zh","America/Mexico_City":"es","America/Bogota":"es","America/Lima":"es","America/Santiago":"es","America/Argentina/Buenos_Aires":"es","Europe/Madrid":"es","America/Sao_Paulo":"pt","Europe/Lisbon":"pt","Europe/Paris":"fr","Europe/Berlin":"de","Europe/Vienna":"de","Asia/Tokyo":"ja","Asia/Kolkata":"hi","Asia/Dubai":"ar","Asia/Riyadh":"ar","Africa/Cairo":"ar"};
let lang = "en";
/* language: ?lang= > saved choice > timezone hint > IP geolocation > browser language */
function syncGuess(){
  const q = new URLSearchParams(location.search).get("lang");
  if(q && LANGS.includes(q)) return q;
  const dl = document.documentElement.getAttribute("data-lang");
  if(dl && LANGS.includes(dl)) return dl;
  const saved = localStorage.getItem("freeqrly-lang");
  if(saved && LANGS.includes(saved)) return saved;
  try{
    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone||"";
    if(TZ2LANG[tz]) return TZ2LANG[tz];
    const city = tz.split("/").pop();
    for(const z in TZ2LANG){ if(z.endsWith("/"+city)) return TZ2LANG[z]; }
  }catch(e){}
  return null;
}
async function detectLang(){
  const s = syncGuess();
  if(s) return s;
  try{
    const ctrl = new AbortController();
    const t = setTimeout(()=>ctrl.abort(), 1500);
    const r = await fetch("https://ipapi.co/json/", {signal:ctrl.signal});
    clearTimeout(t);
    const j = await r.json();
    if(j && j.country_code && GEO2LANG[j.country_code]) return GEO2LANG[j.country_code];
  }catch(e){}
  const bl = (navigator.language||"en").toLowerCase();
  for(const c of LANGS){ if(c!=="en" && (bl===c || bl.indexOf(c+"-")===0)) return c; }
  return "en";
}
let cur = "url", logoData = null;
const ORDER = ["url","text","wifi","vcard","email","sms","phone","geo","event","batch"];
/* landing pages preselect a type via body[data-type]; ?type= also works */
const _preType = document.body.getAttribute("data-type") || new URLSearchParams(location.search).get("type");
if (_preType && ORDER.includes(_preType)) cur = _preType;

const v = id => { const el = $("f_"+id); if(!el) return ""; return el.value.trim() || (el.placeholder||""); };
function content(){
  switch(cur){
    case "url": return v("url")||"https://example.com";
    case "text": return v("text")||" ";
    case "wifi": return `WIFI:T:${v("enc")};S:${v("ssid")};P:${v("pass")};;`;
    case "vcard": return `BEGIN:VCARD\nVERSION:3.0\nN:${v("name")}\nTEL:${v("phone")}\nEMAIL:${v("email")}\nEND:VCARD`;
    case "email": return `mailto:${v("to")}?subject=${encodeURIComponent(v("subject"))}&body=${encodeURIComponent(v("body"))}`;
    case "sms": return `sms:${v("phone")}?body=${encodeURIComponent(v("body"))}`;
    case "phone": return `tel:${v("phone")}`;
    case "geo": return `geo:${v("lat")},${v("lng")}`;
    case "event": {
      const f = s => { s=(s||"").replace(/-/g,"").replace(/:/g,""); return s.length===13 ? s+"00" : s; };
      return `BEGIN:VEVENT\nSUMMARY:${v("etitle")}\nDTSTART:${f(v("estart"))}\nDTEND:${f(v("eend"))}\nLOCATION:${v("eloc")}\nDESCRIPTION:${v("edesc")}\nEND:VEVENT`;
    };
  }
  return " ";
}
function styleOpts(px){
  return {
    width:px, height:px, data:content(), margin:4,
    qrOptions:{ errorCorrectionLevel:$("ecc").value },
    imageOptions:{ crossOrigin:"anonymous", margin:8, imageSize:.4 },
    dotsOptions:{ color:$("fg").value, type:$("dots").value },
    backgroundOptions:{ color: ($("transp") && $("transp").checked) ? "rgba(0,0,0,0)" : $("bgc").value },
    cornersSquareOptions:{ color:$("fg").value },
    cornersDotOptions:{ color:$("fg").value },
    image: logoData || undefined
  };
}
function draw(){
  if(cur==="batch") return;
  const qr = new QRCodeStyling(styleOpts(236));
  $("qrbox").innerHTML=""; qr.append($("qrbox"));
}
const MASCOT_BASE="https://assets.freeqrly.com/mascots/v1/";
const MASCOT_LOCAL="/assets/img/mascots/";
function updateStudioMascot(){
  const image=document.querySelector("[data-studio-mascot]"); if(!image) return;
  const local={url:"qly-url",text:"qly-text",email:"qly-email",sms:"qly-sms",phone:"qly-phone",geo:"qly-geo"};
  const r2={wifi:"wifi",vcard:"business-card",event:"wedding",batch:"batch"};
  if(local[cur]) image.src=MASCOT_LOCAL+local[cur]+".webp";
  else { const pose=r2[cur] || image.getAttribute("data-mascot-default") || "studio-qr"; image.src=MASCOT_BASE+pose+".webp"; }
}
const TYPE_EMOJI = {url:"🔗",text:"📝",wifi:"📶",vcard:"👤",email:"✉️",sms:"💬",phone:"📞",geo:"📍",event:"📅",batch:"📚"};
function renderTabs(){
  updateStudioMascot();
  const t = $("typerail") || $("tabs"); if(!t) return; t.innerHTML="";
  ORDER.forEach(k=>{
    const [name] = I18N[lang].types[k];
    const b = document.createElement("button");
    b.setAttribute("role","tab");
    b.className = "ttab" + (k===cur ? " on" : "");
    b.setAttribute("aria-selected", k===cur ? "true" : "false");
    const ic = document.createElement("span"); ic.className="tico"; ic.textContent = TYPE_EMOJI[k]||"\u25CF";
    b.appendChild(ic); b.appendChild(document.createTextNode(name));
    b.onclick = ()=>{ cur=k; renderTabs(); renderFields(); draw();
      const bp=$("batchPanel"); if(bp) bp.hidden = cur!=="batch";
    };
    t.appendChild(b);
  });
  const bp = $("batchPanel"); if (bp) bp.hidden = cur !== "batch";
}
/* B3 segmented appearance controls: visual UI syncs hidden native inputs */
function segInit(id, hiddenId, def){
  const seg = $(id); if(!seg) return;
  const hidden = $(hiddenId);
  const sync = (v)=>{ if(hidden){ hidden.value=v; hidden.dispatchEvent(new Event("input",{bubbles:true})); hidden.dispatchEvent(new Event("change",{bubbles:true})); } };
  seg.querySelectorAll("button").forEach(b=>{
    if(b.dataset.v === (hidden ? hidden.value : def)) b.classList.add("on");
    b.addEventListener("click",()=>{
      seg.querySelectorAll("button").forEach(x=>x.classList.remove("on"));
      b.classList.add("on"); sync(b.dataset.v);
    });
  });
}
function dotsInit(){
  [["fgDots","fg"],["bgDots","bgc"]].forEach(([dotsId, hiddenId])=>{
    const box = $(dotsId); if(!box) return;
    const hidden = $(hiddenId);
    const transp = $("transp");
    const curVal = ()=> dotsId==="bgDots" && transp && transp.checked ? "transparent" : (hidden ? hidden.value : "#22303F");
    const mark = (v)=>{ box.querySelectorAll(".cdot").forEach(d=>d.classList.toggle("on", d.dataset.v.toLowerCase()===String(v).toLowerCase())); };
    mark(curVal());
    box.querySelectorAll(".cdot").forEach(d=>d.addEventListener("click",()=>{
      if(d.dataset.v==="transparent"){
        if(transp){ transp.checked=true; transp.dispatchEvent(new Event("change",{bubbles:true})); }
      } else {
        if(transp && dotsId==="bgDots"){ transp.checked=false; }
        if(hidden){ hidden.value=d.dataset.v; hidden.dispatchEvent(new Event("input",{bubbles:true})); hidden.dispatchEvent(new Event("change",{bubbles:true})); }
      }
      mark(d.dataset.v); draw();
    }));
  });
  document.querySelectorAll(".cpick").forEach(btn=>{
    btn.addEventListener("click",e=>{
      e.preventDefault();
      const isFg = btn.querySelector("#fgPick");
      const hidden = $(isFg ? "fg" : "bgc");
      const dotsId = isFg ? "fgDots" : "bgDots";
      window.openColorPicker(btn, hidden?hidden.value:"#22303F", (hex)=>{
        if(hidden){ hidden.value=hex; hidden.dispatchEvent(new Event("input",{bubbles:true})); }
        dotsInit._mark(dotsId, hex);
        const transp=$("transp"); if(transp && !isFg) transp.checked=false;
        draw();
      });
    });
  });
}
dotsInit._mark = (dotsId, v)=>{ const box=document.getElementById(dotsId); if(box) box.querySelectorAll(".cdot").forEach(d=>d.classList.toggle("on", d.dataset.v.toLowerCase()===String(v).toLowerCase())); };

function sizeInit(){
  const seg=$("segSize"), hidden=$("size"), val=$("sizeVal"); if(!seg||!hidden) return;
  const mark=()=>{ seg.querySelectorAll("button").forEach(b=>b.classList.toggle("on", b.dataset.v===hidden.value)); if(val) val.textContent=hidden.value; };
  mark();
  seg.querySelectorAll("button").forEach(b=>b.addEventListener("click",()=>{
    hidden.value=b.dataset.v; mark();
    hidden.dispatchEvent(new Event("input",{bubbles:true}));
  }));
}
function renderFields(){
  const f = $("fields"); f.innerHTML="";
  if(cur==="batch") return;
  I18N[lang].fields[cur].forEach(([id,label,third,ph])=>{
    const lab = document.createElement("div"); lab.className="fl"; lab.textContent=label; f.appendChild(lab);
    let el, defVal="";
    if(third==="textarea"){ el=document.createElement("textarea"); el.placeholder=ph||""; }
    else if(third==="datetime-local"){
      const wrap=document.createElement("div"); wrap.className="dtpair";
      const d=document.createElement("input"); d.type="date"; d.id="f_"+id+"_date"; d.oninput=draw;
      const t=document.createElement("input"); t.type="time"; t.id="f_"+id+"_time"; t.oninput=draw;
      wrap.appendChild(d); wrap.appendChild(t); f.appendChild(wrap);
      el=document.createElement("input"); el.type="hidden"; el.id="f_"+id;
      const sync=()=>{ el.value = d.value && t.value ? d.value+"T"+t.value : (d.value||""); };
      d.oninput=()=>{sync();draw();}; t.oninput=()=>{sync();draw();};
    }
    else if(typeof third==="string" && third.startsWith("select:")){
      const opts=third.slice(7).split(",");
      const wrap=document.createElement("div"); wrap.className="seg"; wrap.style.marginTop="2px";
      const hiddenSel=document.createElement("select"); hiddenSel.hidden=true;
      opts.forEach(o=>{ const op=document.createElement("option"); op.value=o; op.textContent=o; hiddenSel.appendChild(op); });
      opts.forEach((o,i)=>{
        const b=document.createElement("button"); b.type="button"; b.textContent=o; b.dataset.v=o;
        if(i===0) b.classList.add("on");
        b.onclick=()=>{ wrap.querySelectorAll("button").forEach(x=>x.classList.remove("on")); b.classList.add("on"); hiddenSel.value=o; draw(); };
        wrap.appendChild(b);
      });
      el=hiddenSel; f.appendChild(wrap);
    } else { el=document.createElement("input"); el.type="text"; el.placeholder=ph||third||""; }
    el.id="f_"+id; el.oninput=draw; f.appendChild(el);
  });
}
function applyLang(){
  document.documentElement.lang = LANGBCP[lang]||"en";
  document.documentElement.dir = lang==="ar" ? "rtl" : "ltr";
  if (!document.body.hasAttribute("data-lp")) {
    document.title = I18N[lang].title;
    document.querySelector('meta[name="description"]').setAttribute("content", I18N[lang].metaDesc);
  }
  document.querySelectorAll("[data-i18n]").forEach(el=>{
    const k = el.getAttribute("data-i18n");
    if(I18N[lang][k] !== undefined) el.textContent = I18N[lang][k];
  });
  const _sel = $("langBtn");
  if(_sel && _sel.tagName==="SELECT"){
    if(!_sel.options.length) LANGS.forEach(c=>{ const o=document.createElement("option"); o.value=c; o.textContent=LANGN[c]; _sel.appendChild(o); });
    _sel.value = lang;
  } else if(_sel){ _sel.textContent = LANGN[lang]||lang; }
  renderTabs(); renderFields(); renderHist();
  localStorage.setItem("freeqrly-lang", lang);
}
/* batch */
let batchItems = [];
function renderBatch(){
  const grid = $("batchGrid"); grid.innerHTML="";
  batchItems.forEach((it,i)=>{
    const cell = document.createElement("div"); cell.className="bcell";
    const qd = document.createElement("div"); qd.className="bqr"; cell.appendChild(qd);
    const qr = new QRCodeStyling(Object.assign(styleOpts(300),{data:it}));
    qr.append(qd);
    const lab = document.createElement("div"); lab.className="blabel"; lab.textContent = it.length>42 ? it.slice(0,42)+"…" : it; cell.appendChild(lab);
    const btn = document.createElement("button"); btn.textContent = I18N[lang].dl+" PNG";
    btn.onclick = ()=> new QRCodeStyling(Object.assign(styleOpts(1024),{data:it})).download({name:"qr-"+(i+1),extension:"png"});
    cell.appendChild(btn); grid.appendChild(cell);
  });
  $("batchZip").disabled = batchItems.length===0;
}
$("batchGo").onclick = ()=>{
  batchItems = $("batchInput").value.split("\n").map(s=>s.trim()).filter(Boolean).slice(0,50);
  const hint = $("batchHint");
  if(batchItems.length===0){
    hint.textContent = (I18N[lang]&&I18N[lang].bEmpty)||I18N.en.bEmpty;
    hint.hidden = false;
    const ta = $("batchInput");
    ta.classList.remove("shake"); void ta.offsetWidth; ta.classList.add("shake");
    ta.focus();
    return;
  }
  hint.hidden = true;
  track("batch_generate",{count:batchItems.length});
  renderBatch();
};
$("batchZip").onclick = async ()=>{ track("batch_zip",{count:batchItems.length});
  const zip = new JSZip();
  for(let i=0;i<batchItems.length;i++){
    const blob = await new QRCodeStyling(Object.assign(styleOpts(1024),{data:batchItems[i]})).getRawData("png");
    zip.file(`qr-${i+1}.png`, blob);
  }
  const blob = await zip.generateAsync({type:"blob"});
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob); a.download = "freeqrly-batch.zip"; a.click();
  setTimeout(()=>URL.revokeObjectURL(a.href), 4000);
};
/* privacy-first analytics: fire-and-forget, no cookies/ids */
function track(event, props){
  try{
    const body = JSON.stringify(Object.assign({event:event, lang:lang}, props||{}));
    if(navigator.sendBeacon){
      navigator.sendBeacon("/api/track", new Blob([body], {type:"application/json"}));
    }else{
      fetch("/api/track", {method:"POST", headers:{"Content-Type":"application/json"}, body:body, keepalive:true}).catch(()=>{});
    }
  }catch(e){}
}
/* history (local only) */
const HIST_KEY="freeqrly-history";
function getHist(){ try{ return JSON.parse(localStorage.getItem(HIST_KEY))||[]; }catch(e){ return []; } }
function saveHist(){
  if(cur==="batch") return;
  const vals={}; (I18N[lang].fields[cur]||[]).forEach(([id])=>{ vals[id]=v(id); });
  const data=content();
  let h=getHist().filter(x=>x.data!==data);
  h.unshift({type:cur,vals:vals,data:data,ts:Date.now()});
  try{ localStorage.setItem(HIST_KEY, JSON.stringify(h.slice(0,12))); }catch(e){}
  renderHist();
}
function renderHist(){
  const box=$("histList"), sec=$("histSec"); if(!box||!sec) return;
  box.innerHTML="";
  const h=getHist(); sec.hidden = h.length===0;
  h.forEach(it=>{
    const b=document.createElement("button"); b.className="hitem"; b.type="button"; b.title=it.data;
    const tn=(I18N[lang].types[it.type]||[it.type])[0];
    const nm=document.createElement("b"); nm.textContent=tn; b.appendChild(nm);
    const sp=document.createElement("span"); sp.textContent=it.data.length>36?it.data.slice(0,36)+"…":it.data; b.appendChild(sp);
    b.onclick=()=>{ if(!ORDER.includes(it.type)) return; cur=it.type; renderTabs(); renderFields();
      Object.keys(it.vals||{}).forEach(id=>{ const el=$("f_"+id); if(el) el.value=it.vals[id]; });
      draw(); const st=$("studio"); if(st) st.scrollIntoView({behavior:"smooth",block:"start"}); };
    box.appendChild(b);
  });
}
/* controls */
["fg","bgc","dots","ecc"].forEach(id=>{ const el=$(id); if(!el) return; el.addEventListener("input",()=>{draw();}); el.addEventListener("change",()=>{draw();}); });
segInit("segDots","dots","square"); segInit("segEcc","ecc","M"); dotsInit(); sizeInit();
function setLogo(dataURL, preset){
  logoData = dataURL || null;
  if(logoData && ["L","M"].includes($("ecc").value)){
    $("ecc").value="Q";
    const seg=$("segEcc"); if(seg){ seg.querySelectorAll("button").forEach(b=>b.classList.toggle("on", b.dataset.v==="Q")); }
  }
  document.querySelectorAll("#logoRow .logopick[data-preset]").forEach(b=>b.classList.toggle("on", b.dataset.preset===preset));
  draw(); if(cur==="batch") renderBatch();
}
document.querySelectorAll("#logoRow .logopick[data-preset]").forEach(b=>b.addEventListener("click", async ()=>{
  const cur = b.classList.contains("on");
  if(cur){ setLogo(null, null); return; }  // toggle off
  try{
    const res = await fetch("/assets/img/logos/"+b.dataset.preset+".svg");
    const txt = await res.text();
    setLogo("data:image/svg+xml;charset=utf-8,"+encodeURIComponent(txt), b.dataset.preset);
  }catch(e){ /* offline: ignore */ }
}));
$("logo").addEventListener("change",e=>{
  const f=e.target.files[0]; if(!f) return;
  const r=new FileReader();
  r.onload=()=>setLogo(r.result, null);
  r.readAsDataURL(f);
});
async function downloadQR(format){
  const button=$(format==="png"?"dlPng":"dlSvg");
  button.disabled=true;
  try{
    const px=format==="png"?(parseInt($("size").value)||1024):1024;
    await new QRCodeStyling(styleOpts(px)).download({name:"freeqrly",extension:format});
    saveHist(); track("qr_download",{type:cur,format:format});
  
  }catch(e){}
  finally{button.disabled=false;}
}
$("dlPng").onclick=()=>downloadQR("png");
$("dlSvg").onclick=()=>downloadQR("svg");
const _hc=$("histClear"); if(_hc) _hc.onclick=()=>{ try{localStorage.removeItem(HIST_KEY);}catch(e){} renderHist(); };
/* theme */
const root=document.documentElement;
function setTheme(dark){
  if(dark) root.setAttribute("data-theme","dark"); else root.removeAttribute("data-theme");
  localStorage.setItem("freeqrly-theme", dark?"dark":"light");
}
setTheme(localStorage.getItem("freeqrly-theme")==="dark" ||
  (!localStorage.getItem("freeqrly-theme") && matchMedia("(prefers-color-scheme: dark)").matches));
$("themeBtn").onclick=()=> setTheme(root.getAttribute("data-theme")!=="dark");
(function(){ const b=$("langBtn"); if(!b) return;
  if(b.tagName==="SELECT"){ b.addEventListener("change",e=>{ lang=e.target.value; applyLang(); }); }
  else { b.onclick=()=>{ const i=LANGS.indexOf(lang); lang=LANGS[(i+1)%LANGS.length]; applyLang(); }; }
})();


/* Custom color picker popover */
(function(){
  const pop=$("cpop"); if(!pop) return;
  const sat=$("cpopSat"), satDot=$("cpopSatDot"), hue=$("cpopHue"), hueDot=$("cpopHueDot");
  const prev=$("cpopPrev"), hexI=$("cpopHex"), ok=$("cpopOk");
  let H=210, S=30, V=25, target=null, onPick=null, interacted=false;
  function hsv2hex(h,s,v){
    s/=100; v/=100;
    const k=(n)=>(n+h/60)%6, f=(n)=>v*(1-s*Math.max(0,Math.min(k(n),4-k(n),1)));
    const r=Math.round(f(5)*255), g=Math.round(f(3)*255), b=Math.round(f(7)*255);
    return "#"+[r,g,b].map(x=>x.toString(16).padStart(2,"0")).join("").toUpperCase();
  }
  function hex2hsv(hex){
    const r=parseInt(hex.slice(1,3),16)/255, g=parseInt(hex.slice(3,5),16)/255, b=parseInt(hex.slice(5,7),16)/255;
    const mx=Math.max(r,g,b), mn=Math.min(r,g,b), d=mx-mn;
    let h=0; if(d){ if(mx===r) h=((g-b)/d)%6; else if(mx===g) h=(b-r)/d+2; else h=(r-g)/d+4; h*=60; if(h<0)h+=360; }
    return [h, mx?d/mx*100:0, mx*100];
  }
  function render(){
    const hex=hsv2hex(H,S,V);
    sat.style.background=`linear-gradient(to top,#000,transparent),linear-gradient(to right,#fff,transparent),hsl(${H},100%,50%)`;
    satDot.style.left=S+"%"; satDot.style.top=(100-V)+"%";
    hueDot.style.left=(H/360*100)+"%";
    prev.style.background=hex; hexI.value=hex;
    if(onPick && interacted) onPick(hex);
  }
  function fromHex(hex){
    if(!/^#[0-9A-Fa-f]{6}$/.test(hex)) return;
    [H,S,V]=hex2hsv(hex); render();
  }
  sat.addEventListener("pointerdown",e=>{
    interacted=true;
    const move=ev=>{ const r=sat.getBoundingClientRect();
      S=Math.min(100,Math.max(0,(ev.clientX-r.left)/r.width*100));
      V=100-Math.min(100,Math.max(0,(ev.clientY-r.top)/r.height*100));
      render(); };
    move(e);
    const up=()=>{window.removeEventListener("pointermove",move);window.removeEventListener("pointerup",up);};
    window.addEventListener("pointermove",move); window.addEventListener("pointerup",up);
  });
  hue.addEventListener("pointerdown",e=>{
    interacted=true;
    const move=ev=>{ const r=hue.getBoundingClientRect();
      H=Math.min(360,Math.max(0,(ev.clientX-r.left)/r.width*360)); render(); };
    move(e);
    const up=()=>{window.removeEventListener("pointermove",move);window.removeEventListener("pointerup",up);};
    window.addEventListener("pointermove",move); window.addEventListener("pointerup",up);
  });
  hexI.addEventListener("input",()=>{ interacted=true; fromHex(hexI.value); });
  ok.addEventListener("click",()=>{ if(onPick && interacted){ render(); } pop.hidden=true; });
  document.addEventListener("pointerdown",e=>{
    if(!pop.hidden && !pop.contains(e.target) && !e.target.closest(".cpick")) pop.hidden=true;
  });
  window.openColorPicker=function(anchorBtn, initialHex, cb){
    target=anchorBtn; onPick=cb; interacted=false;
    fromHex(initialHex||"#22303F");
    pop.hidden=false;
    const r=anchorBtn.getBoundingClientRect();
    pop.style.left=Math.min(window.innerWidth-250, Math.max(10, r.left-100))+"px";
    pop.style.top=(r.bottom+8+window.scrollY)+"px";
  };
})();

detectLang().then(l=>{ lang = l; applyLang(); draw(); });
})();
