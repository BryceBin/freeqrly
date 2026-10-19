/* FreeQrly v1.0 — app logic */
(function(){
"use strict";
const $ = id => document.getElementById(id);

const I18N = {
en:{
  title:"FreeQrly — Free QR Code Generator",
  metaDesc:"Make free QR codes in your browser. Static codes need no sign-up. Links, WiFi, contacts and more. Download PNG or SVG. Yours forever.",
  navStudio:"Home",navWhy:"Why free",navFaq:"FAQ",
  kicker:"Free · Static codes need no sign-up · Private by design",
  h1a:"Turn",h1b:"anything",h1c:"into a QR code.",
  lede:"Static codes need no sign-up — made in your browser, yours forever. Dynamic codes need a free sign-in, so you can edit them after printing.",
  hc1:"Content types",hc2:"Export",hc3:"Your data",hc3v:"Private by design",hc4:"Price",hc4v:"Free, always",
  sOver:"Start",sTitle:"Make your QR code",
  appearance:"Style",ink:"Ink",paper:"Paper",background:"Background",dots:"Style",ecc:"Error correction",
  dSquare:"Square",dRound:"Round",dSoft:"Soft",dPebble:"Pebble",
  eL:"Low",eM:"Medium",eQ:"High",eH:"Max",
  eccHint:"Higher = survives logos and covered spots.",dotsSub:"Dot shape",eccSub:"Scans even when covered",colors:"Colors",colorsSub:"Tap or customize",transparentSub:"Transparent background",
  size:"Download size",logo:"Add your logo",logoSub:"Centered in the code",
  privnote:"Static codes are made entirely in your browser.",
  live:"Type and it appears",
  bLabel:"One link per line",bType:"Type",bUpload:"Upload CSV / Excel",bTemplate:"Download template",bGo:"Generate all",bZip:"Download ZIP",bEmpty:"Paste at least one link above",
  p1n:"1",p1t:"Your data goes nowhere",p1p:"Static codes are drawn on your device. Nothing uploaded, nothing tracked, no account needed. Works offline too.",
  p2n:"2",p2t:"Made once, yours forever",p2p:"The destination lives inside the pattern. Print it today, it scans in ten years. No renewals.",
  p3n:"3",p3t:"Free means free",p3p:"No watermark, no fine print. Static codes need no sign-up. Everything is free.",
  faqT:"Questions",
  q1:"Do free QR codes expire?",a1:"No. The destination is encoded in the pattern — as long as it exists, the code works.",
  q2:"Is my WiFi password safe here?",a2:"For a static code, yes — it never leaves your browser. Still unsure? Disconnect and type.",
  q3:"Static or dynamic?",a3:"If the destination won't change, go static: WiFi, business cards, fixed links. Dynamic codes (editable links + scan stats) suit marketing campaigns — they're live now: free sign-in, edit after printing, track scans.",
  q4:"Can I use these commercially?",a4:"Absolutely. Everything you make is yours — use it anywhere, no attribution needed.",
  q5:"Is it really free?",a5:"Yes. Everything is free, no watermark. Static codes need no account.",
  q6:"Do I need an account?",a6:"Not for static codes — open the page and make your code. Dynamic codes need a free sign-in, so you can edit them after they're printed.",
  q7:"Can I add my logo?",a7:"Yes. Upload a square logo, it goes in the center, and error correction bumps up automatically so it still scans.",
  fin:"Static codes, made in your browser.",
  dl:"Download",navScan:"Scanner",history:"Recent",histClear:"Clear",transparent:"Transparent background",frame:"Frame",frameSub:"Border around the code",frameTextLabel:"Frame text",frameNone:"None",frameRounded:"Rounded",frameCta:"With text",frameTextPh:"Scan me",scanGood:"Good contrast",scanBad:"Low contrast — may not scan",featsK:"Beyond generating",featsT:"More than QR codes",featsS:"Generating is just the start. FreeQrly has these too.",f1t:"Built-in scanner",f1d:"Point your camera or upload an image — codes decode right in your browser, never uploaded. Works offline.",f1l:"Open scanner →",f2t:"17 QR code types",f2d:"Web, text, WiFi, contacts, email, SMS, calls, locations, calendar events, Bitcoin, Coupon, App Store, reviews, audio, Google Forms, menus — plus Batch mode for many at once. Each type gets the right format automatically.",f2l:"Try them all →",f3t:"Batch generation",f3d:"Paste 50 links, get 50 print-ready codes in one click. Download one by one or as a ZIP.",f3l:"Batch mode →",f4t:"Calendar event codes",f4d:"One scan and the event — title, time, place — goes straight into their calendar. Made for invitations.",f4l:"Make event code →",f5t:"Logo & styling",f5d:"Put your logo in the center, error correction bumps up automatically so it still scans. Change dots and colors, or go transparent.",f5l:"Codes with logo →",f6t:"Private history",f6d:"Every download is remembered only on this device — your latest 12, one click to restore. Clear anytime.",casesK:"Real scenarios",casesT:"Made for real moments",casesS:"Pick your scenario, the setup is ready.",c1t:"Business cards",c1d:"One scan, your contact goes straight into their phone.",c2t:"Weddings",c2d:"RSVP, photo sharing, calendar reminders. All online.",c3t:"Real estate",c3d:"Scan the yard sign, book a viewing in one tap.",c4t:"Events",c4d:"Check-in, ticket validation, shared albums. One code.",c5t:"WiFi sharing",c5d:"Guests get online with a scan. No more spelling passwords.",c6t:"Google reviews",c6d:"Turn happy customers into five-star reviews at the counter.",types:{url:["Website","link, page, video"],text:["Text","any words"],wifi:["WiFi","join instantly"],vcard:["Contact","vCard"],email:["Email","prefilled"],sms:["SMS","prefilled text"],phone:["Call","tap to dial"],geo:["Place","map pin"],"event":["Event","add to calendar"],"bitcoin":["Bitcoin","crypto payment"],"coupon":["Coupon","promo code"],"appstore":["App Store","iOS + Android"],"review":["Reviews","get 5-star reviews"],"mp3":["Audio","MP3 & sound"],"google-form":["Google Form","collect responses"],"menu":["Menu","restaurant menu"],"batch":["Batch","many at once"]},
  fields:{url:[["url","Destination","https://example.com"]],text:[["text","Message","textarea","Hello, world!"]],
    wifi:[["ssid","Network name","MyWiFi"],["pass","Password","","WiFi password"],["enc","Security","select:WPA,WPA2,WEP,nopass"]],
    vcard:[["name","Full name","Jane Doe"],["phone","Phone","+1 555 0100"],["email","Email","jane@example.com"],["vcorg","Company","","Acme Inc"],["vctitle","Job title","","Designer"],["vcurl","Website","https://example.com"],["vcadr","Address","","123 Main St"],["vcnote","Note","",""]],
    email:[["to","To","hi@example.com"],["subject","Subject","Hello"],["body","Body","textarea","Email body…"]],
    sms:[["phone","Phone","+1 555 0100"],["body","Message","","Type your message…"]],
    phone:[["phone","Phone","+1 555 0100"]],geo:[["lat","Latitude","37.7749"],["lng","Longitude","-122.4194"]],"event":[["etitle","Title","","e.g. Birthday party"],["estart","Starts","datetime-local"],["eend","Ends","datetime-local"],["eloc","Location","","e.g. Central Park"],["edesc","Details","textarea","Event details…"]],"bitcoin":[["btcaddr","Wallet address","bc1q..."],["btcamt","Amount (BTC)","0.001"],["btclabel","Label","","e.g. Coffee"],["btcmsg","Message","","e.g. Thanks"]],"coupon":[["cpcode","Coupon code","SAVE20"],["cpdesc","Description","","e.g. 20% off"]],"appstore":[["appios","App Store link","https://apps.apple.com/app/..."],["appand","Google Play link","https://play.google.com/store/apps/..."]],"review":[["rvlink","Review page link","https://g.page/your-business/review"]],"mp3":[["mp3link","Audio file link","https://example.com/song.mp3"]],"google-form":[["gflink","Form link","https://forms.gle/abc123XYZ"]],"menu":[["mnlink","Menu link","https://example.com/menu"]]}
, "modeStatic":"Static", "modeDynamic":"Dynamic", "modeHint":"Static codes never expire. Dynamic codes can be edited after printing + track scans.", "dynDest":"Destination URL", "dynCreate":"Generate dynamic QR", "dynShort":"Your dynamic QR link:", "copy":"Copy", "dynIntro":"Design your QR — pick a type, fill in content, style it. Then create a dynamic code: the printed QR stays the same, but you can change its content anytime.", "dynHint":"Fill in your content, then hit Generate.", "dynReady":"Your dynamic QR is ready. Print it — the content can change anytime.", "dynBlurHint":"Fill in your content, then hit Generate", "modeTip":"Static: the content lives inside the QR — no sign-in, works forever. Dynamic: scans go through a short link — edit content after printing + see scan stats. Needs a free sign-in.", "dynSigninHint":"Sign in to create dynamic codes", "dynDashLink":"View in Dashboard →","signin":"Sign in","acctDashboard":"Dashboard","acctExport":"Export my data","acctDelete":"Delete account","acctLogout":"Log out","acctDeleteConfirm":"Delete your account? This cannot be undone.","acctDeleteFailed":"Couldn't delete the account. Please try again.","acctNetErr":"Network error. Please try again.","acctSignedInWith":"Signed in with {method}","moreFormats":"More formats","footGenerators":"Generators","footMore":"More","ariaCustomInk":"Custom ink color","ariaCustomBg":"Custom background color","ariaUploadLogo":"Upload logo","ariaLanguage":"Language"},
zh:{
  title:"FreeQrly — 免费二维码生成器",
  metaDesc:"免费在线生成二维码，静态码不用注册。链接、WiFi、名片都能做，下载 PNG 或 SVG，长期有效。",
  navStudio:"首页",navWhy:"为什么免费",navFaq:"常见问题",
  kicker:"免费 · 静态码免注册 · 不上传数据",
  h1a:"输入",h1b:"内容",h1c:"，一秒生成二维码。",
  lede:"静态码不用注册，在浏览器里生成，长期有效。动态码需要免费登录，打印后也能随时改内容。",
  hc1:"内容类型",hc2:"导出",hc3:"你的数据",hc3v:"隐私优先",hc4:"价格",hc4v:"长期免费",
  sOver:"开始",sTitle:"生成二维码",
  appearance:"外观样式",ink:"前景色",paper:"纸色",background:"背景",dots:"样式",ecc:"纠错等级",
  dSquare:"方形",dRound:"圆形",dSoft:"柔和",dPebble:"鹅卵石",
  eL:"低",eM:"中",eQ:"高",eH:"最高",
  eccHint:"纠错越高，遮住一部分也能扫出来，放 Logo 更稳。",dotsSub:"圆点的形状",eccSub:"遮挡也能扫",colors:"颜色",colorsSub:"点选，或自定义",transparentSub:"透明背景",
  size:"下载尺寸",logo:"添加 Logo",logoSub:"放在二维码中间",
  privnote:"静态码全程在你的浏览器里生成。",
  live:"即时输入，即时生成",
  bLabel:"每行一个链接",bType:"类型",bUpload:"上传 CSV / Excel",bTemplate:"下载模板",bGo:"全部生成",bZip:"下载 ZIP",bEmpty:"先在上面输入至少一个链接",featsK:"不止于生成",featsT:"二维码之外，还有更多",featsS:"生成只是开始。FreeQrly 里还有这些。",f1t:"内置扫码器",f1d:"用摄像头对准，或上传图片——二维码在你的浏览器里直接解码，绝不上传到服务器。离线也能用。",f1l:"打开扫码器 →",f2t:"17 种二维码类型",f2d:"网址、文本、WiFi、电子名片、邮件、短信、电话、地点、日历事件、比特币、优惠券、应用商店、评价、音频、谷歌表单、菜单，另有批量模式一次生成多个。每种类型自动生成正确格式，不用记语法。",f2l:"都试试 →",f3t:"批量生成",f3d:"一次粘贴 50 个链接，一键得到 50 个可打印的二维码。逐个下载，或打包成 ZIP。",f3l:"批量模式 →",f4t:"日历事件码",f4d:"扫一下，活动标题、时间、地点直接进手机日历。婚礼、会议都用得上。",f4l:"生成事件码 →",f5t:"Logo 与美化",f5d:"把 logo 放中间，容错等级自动提高，保证扫得出。圆点、颜色随便换，还能透明底。",f5l:"带 logo 的码 →",f6t:"私密历史记录",f6d:"每次下载只记在这台设备上——最近 12 条，一键恢复。随时清空，我们永远看不到。",casesK:"真实场景",casesT:"各种场合都能用",casesS:"选你的场景，方法都准备好了。",c1t:"名片",c1d:"扫一下，联系方式直接进对方手机。",c2t:"婚礼",c2d:"RSVP、照片共享、日历提醒。RSVP、照片共享都在线上搞定。",c3t:"房产",c3d:"房源立牌扫码看，一键预约看房。",c4t:"活动",c4d:"签到、验票、共享相册，一码搞定。",c5t:"WiFi 分享",c5d:"客人扫码上网。再也不用念密码。",c6t:"谷歌评价",c6d:"把满意的客人变成柜台前的五星好评。",
  p1n:"1",p1t:"你的数据，哪儿也不去",p1p:"静态码在你的设备上直接画出来，不上传、不追踪、不用注册。断网也能用。",
  p2n:"2",p2t:"一次生成，长期有效",p2p:"网址直接写进图案里。今天印出来，十年后照样能扫。不用续费。",
  p3n:"3",p3t:"免费，就是免费",p3p:"无水印，没有隐藏收费。静态码不用注册。所有功能都免费。",
  faqT:"常见问题",
  q1:"免费的二维码会过期吗？",a1:"不会。网址直接写在图案里，网址有效、码就有效。",
  q2:"在这里输 WiFi 密码安全吗？",a2:"静态码安全。密码只在你的浏览器里，不会发到任何地方。不放心的话，断网再输。",
  q3:"静态码和动态码怎么选？",a3:"地址不变就用静态码：WiFi、名片、固定链接，一次做好长期用。动态码（可编辑链接 + 扫码统计）适合营销活动——已正式上线：免费登录，打印后仍可编辑，还能查看扫码统计。",
  q4:"可以商用吗？",a4:"可以。生成的码都属于你，印在哪儿都行，不用署名。",
  q5:"真的免费吗？",a5:"真的。所有功能免费，无水印。静态码不用注册。",
  q6:"需要注册账号吗？",a6:"静态码不用。打开即用。动态码需要免费登录，这样打印后还能改内容。",
  q7:"二维码中间能加 Logo 吗？",a7:"可以。上传方形 Logo，会放在正中间，纠错等级自动调高，保证能扫出来。",
  fin:"静态码，在你的浏览器里生成。",
  dl:"下载",navScan:"扫码",history:"最近生成",histClear:"清除",transparent:"透明背景",frame:"边框",frameSub:"码外面的边框",frameTextLabel:"边框文字",frameNone:"无",frameRounded:"圆角",frameCta:"带文字",frameTextPh:"扫我",scanGood:"对比度良好",scanBad:"对比度太低，可能扫不出来",types:{url:["网址","链接、页面、视频"],text:["文本","任意文字"],wifi:["WiFi","一键联网"],vcard:["名片","vCard"],email:["邮箱","预填内容"],sms:["短信","预填内容"],phone:["电话","点击拨号"],geo:["位置","地图标记"],"event":["活动","添加到日历"],"bitcoin":["比特币","加密货币支付"],"coupon":["优惠券","促销码"],"appstore":["应用商店","iOS + 安卓"],"review":["评价","获取五星好评"],"mp3":["音频","MP3 音乐"],"google-form":["谷歌表单","收集问卷填写"],"menu":["菜单","餐厅菜单"],"batch":["批量","一次多个"]},
  fields:{url:[["url","目标地址","https://example.com"]],text:[["text","内容","textarea","你好，世界！"]],
    wifi:[["ssid","网络名称","MyWiFi"],["pass","密码","","WiFi 密码"],["enc","加密方式","select:WPA,WPA2,WEP,nopass"]],
    vcard:[["name","姓名","王小明"],["phone","电话","+86 138 0000 0000"],["email","邮箱","hi@example.com"],["vcorg","公司","","某某公司"],["vctitle","职位","","设计师"],["vcurl","网址","https://example.com"],["vcadr","地址","","某某路123号"],["vcnote","备注","",""]],
    email:[["to","收件人","hi@example.com"],["subject","主题","你好"],["body","正文","textarea","邮件正文…"]],
    sms:[["phone","电话","+86 138 0000 0000"],["body","内容","","输入短信内容…"]],
    phone:[["phone","电话","+86 138 0000 0000"]],geo:[["lat","纬度","39.9042"],["lng","经度","116.4074"]],"event":[["etitle","标题","","例如：生日派对"],["estart","开始","datetime-local"],["eend","结束","datetime-local"],["eloc","地点","","例如：中央公园"],["edesc","详情","textarea","活动详情…"]],"bitcoin":[["btcaddr","钱包地址","bc1q..."],["btcamt","金额 (BTC)","0.001"],["btclabel","标签","","例如：咖啡"],["btcmsg","留言","","例如：谢谢"]],"coupon":[["cpcode","优惠码","SAVE20"],["cpdesc","说明","","例如：满100减20"]],"appstore":[["appios","App Store 链接","https://apps.apple.com/app/..."],["appand","Google Play 链接","https://play.google.com/store/apps/..."]],"review":[["rvlink","评价页面链接","https://g.page/your-business/review"]],"mp3":[["mp3link","音频文件链接","https://example.com/song.mp3"]],"google-form":[["gflink","表单链接","https://forms.gle/abc123XYZ"]],"menu":[["mnlink","菜单链接","https://example.com/menu"]]}, "modeStatic":"静态", "modeDynamic":"动态", "modeHint":"静态码永不过期。动态码打印后可改地址，还能统计扫码。", "dynDest":"目标链接", "dynCreate":"生成动态码", "dynShort":"你的动态码链接：", "copy":"复制", "dynIntro":"先设计二维码——选类型、填内容、调样式。然后生成动态码：印出来的码不变，但内容随时可以改。", "dynHint":"填好内容，然后点生成。", "dynReady":"动态码已生成，打印出来吧——内容随时可以改。", "dynBlurHint":"填好内容，然后点生成", "modeTip":"静态码：内容直接写进二维码里，无需登录，长期有效。动态码：扫码走短链接跳转，打印后可改内容、看扫码统计，需免费登录。","signin":"登录","acctDashboard":"Dashboard","acctExport":"导出我的数据","acctDelete":"删除账号","acctLogout":"退出登录","acctDeleteConfirm":"确定删除账号吗？此操作无法撤销。","acctDeleteFailed":"删除失败，请重试。","acctNetErr":"网络错误，请重试。","acctSignedInWith":"通过{method}登录","moreFormats":"更多格式","footGenerators":"生成器","footMore":"更多","ariaCustomInk":"自定义前景色","ariaCustomBg":"自定义背景色","ariaUploadLogo":"上传 Logo","ariaLanguage":"语言","dynDashLink":"在控制台中查看 →","dynSigninHint":"登录后可创建动态码"},
es:{title:"FreeQrly — Generador de códigos QR gratis",metaDesc:"Crea códigos QR gratis en tu navegador. Los estáticos no necesitan registro. Web, WiFi, contactos y más. Descarga en PNG o SVG, no caducan.",navStudio:"Inicio",navWhy:"Por qué gratis",navFaq:"Preguntas",kicker:"Gratis · Los estáticos no necesitan registro · Privacidad por diseño",h1a:"Convierte",h1b:"cualquier cosa",h1c:"en un QR.",lede:"Los códigos estáticos no necesitan registro: se hacen en tu navegador y son tuyos para siempre. Los dinámicos necesitan una cuenta gratuita, para editarlos después de imprimirlos.",hc1:"Tipos de contenido",hc2:"Exportar",hc3:"Tus datos",hc3v:"Privacidad por diseño",hc4:"Precio",hc4v:"Gratis siempre",sOver:"Empieza",sTitle:"Crea tu código QR",appearance:"Apariencia",ink:"Tinta",paper:"Papel",background:"Fondo",dots:"Estilo",ecc:"Corrección de errores",dSquare:"Cuadrado",dRound:"Redondo",dSoft:"Suave",dPebble:"Guijarro",eL:"Bajo",eM:"Medio",eQ:"Alto",eH:"Máximo",eccHint:"Más corrección = aguanta logos y partes tapadas.",dotsSub:"Forma de los puntos",eccSub:"Aunque se tape, se lee",colors:"Colores",colorsSub:"Toca o personaliza",transparentSub:"Fondo transparente",size:"Tamaño de descarga",logo:"Añade tu logo",logoSub:"En el centro del código",privnote:"Los códigos estáticos se hacen por completo en tu navegador.",live:"Escribe y se crea al momento",bLabel:"Un enlace por línea",bType:"Tipo",bUpload:"Subir CSV / Excel",bTemplate:"Descargar plantilla",bGo:"Generar todos",bZip:"Descargar ZIP",bEmpty:"Pega al menos un enlace arriba",featsK:"Más allá del código",featsT:"Todo lo que rodea al QR",featsS:"Generar es solo el principio. Esto también vive en FreeQrly.",f1t:"Escáner integrado",f1d:"Apunta tu cámara o sube una imagen — los códigos se decodifican en tu navegador y nunca se suben a ningún servidor. Funciona sin conexión.",f1l:"Abrir el escáner →",f2t:"17 tipos de código",f2d:"Web, texto, WiFi, tarjetas de contacto, correo, SMS, llamadas, ubicaciones, eventos de calendario, Bitcoin, Cupón, Tienda de apps, reseñas, audio, formularios de Google, menús — más modo lote para muchos a la vez. Cada tipo genera el formato correcto — sin memorizar sintaxis.",f2l:"Probarlos todos →",f3t:"Generación en lote",f3d:"Pega hasta 50 enlaces y obtén 50 códigos listos para imprimir en un clic. Descárgalos uno por uno o todo en un ZIP.",f3l:"Modo lote →",f4t:"Códigos de evento",f4d:"Un escaneo y tu evento — título, hora, lugar — entra directo al calendario del invitado. Hecho para invitaciones.",f4l:"Crear código de evento →",f5t:"Logo y estilo",f5d:"Pon tu logo en el centro y la corrección de errores sube sola para que siga escaneándose. Cambia puntos, tinta y papel — o usa fondo transparente.",f5l:"Códigos con logo →",f6t:"Historial privado",f6d:"Cada descarga se recuerda solo en este dispositivo — tus doce más recientes, un clic para recuperar. Bórralo cuando quieras.",casesK:"En acción",casesT:"Hecho para momentos reales",casesS:"Elige tu escenario — la configuración ya está resuelta.",c1t:"Tarjetas de visita",c1d:"Tus datos de contacto en un escaneo — directo a su teléfono.",c2t:"Bodas",c2d:"RSVP, fotos compartidas, añadir al calendario. El papeleo, sin papel.",c3t:"Inmobiliaria",c3d:"Anuncios en el cartel. Reserva una visita en un escaneo.",c4t:"Eventos",c4d:"Registro, validación de entradas, álbumes compartidos.",c5t:"Compartir WiFi",c5d:"Invitados conectados en un escaneo. Nunca más deletrees una contraseña.",c6t:"Reseñas de Google",c6d:"Convierte clientes felices en cinco estrellas, en el mostrador.",p1n:"1",p1t:"Tus datos no salen de aquí",p1p:"Los códigos estáticos se dibujan en tu dispositivo. Nada se sube, nada se rastrea, sin cuenta. Sin internet también funciona.",p2n:"2",p2t:"Hecho una vez, vale para siempre",p2p:"El destino va dentro del dibujo. Imprímelo hoy y se leerá en diez años. Sin renovar nada.",p3n:"3",p3t:"Gratis es gratis",p3p:"Sin marca de agua, sin letra pequeña. Los códigos estáticos no necesitan registro. Todo gratis.",faqT:"Preguntas",q1:"¿Caduca un código QR gratuito?",a1:"No. El destino va en el dibujo; mientras el destino exista, funciona.",q2:"¿Mi contraseña WiFi está segura aquí?",a2:"En un código estático, sí: nunca sale de tu navegador. Si dudas, desconéctate y escríbela.",q3:"¿Estático o dinámico?",a3:"Si el destino no cambia, estático: WiFi, tarjetas, enlaces fijos. Los dinámicos (enlaces editables + estadísticas de escaneo) sirven para campañas — ya están disponibles: registro gratuito, edita después de imprimir y consulta las estadísticas.",q4:"¿Puedo usarlos comercialmente?",a4:"Claro. Lo que crees es tuyo — úsalo donde quieras, sin mencionar nada.",q5:"¿De verdad es gratis?",a5:"Sí. Todo gratis, sin marca de agua. Los códigos estáticos no necesitan cuenta.",q6:"¿Necesito una cuenta?",a6:"Para los estáticos, no: abre y crea. Los dinámicos necesitan una cuenta gratuita, para editarlos después de imprimirlos.",q7:"¿Puedo poner mi logo?",a7:"Sí. Sube un logo cuadrado, va al centro y la corrección sube sola para que se siga leyendo.",fin:"Códigos estáticos, hechos en tu navegador.",dl:"Descargar",navScan:"Escáner",history:"Recientes",histClear:"Borrar",transparent:"Fondo transparente",frame:"Marco",frameSub:"Borde alrededor del código",frameTextLabel:"Texto del marco",frameNone:"Ninguno",frameRounded:"Redondeado",frameCta:"Con texto",frameTextPh:"Escanea",scanGood:"Buen contraste",scanBad:"Contraste bajo — puede no leerse",types:{"url": ["Sitio web", "enlace, página, video"], "text": ["Texto", "cualquier palabra"], "wifi": ["WiFi", "conexión instantánea"], "vcard": ["Contacto", "vCard"], "email": ["Correo", "prellenado"], "sms": ["SMS", "texto prellenado"], "phone": ["Llamada", "tocar para llamar"], "geo": ["Lugar", "pin de mapa"],"event":["Evento","añadir al calendario"],"bitcoin":["Bitcoin","pago cripto"],"coupon":["Cupón","código promo"],"appstore":["Tienda de apps","iOS + Android"],"review":["Reseñas","reseñas de 5 estrellas"],"mp3":["Audio","MP3 y sonido"],"google-form":["Formulario","recoge respuestas"],"menu":["Menú","carta del restaurante"],"batch":["Lote", "muchos a la vez"]},fields:{"url": [["url", "Destino", "https://example.com"]], "text": [["text", "Mensaje", "textarea", "¡Hola, mundo!"]], "wifi": [["ssid", "Nombre de red", "MiWiFi"], ["pass", "Contraseña", "", "Contraseña WiFi"], ["enc", "Seguridad", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "Nombre completo", "María García"], ["phone", "Teléfono", "+34 600 000 000"], ["email", "Correo", "maria@example.com"],["vcorg","Empresa","","Acme"],["vctitle","Cargo","","Diseñadora"],["vcurl","Sitio web","https://example.com"],["vcadr","Dirección","","Calle Mayor 123"],["vcnote","Nota","",""]], "email": [["to", "Para", "hola@example.com"], ["subject", "Asunto", "Hola"], ["body", "Cuerpo", "textarea", "Cuerpo del correo…"]], "sms": [["phone", "Teléfono", "+34 600 000 000"], ["body", "Mensaje", "", "Escribe tu mensaje…"]], "phone": [["phone", "Teléfono", "+34 600 000 000"]], "geo": [["lat", "Latitud", "40.4168"], ["lng", "Longitud", "-3.7038"]],"event":[["etitle","Título","","p. ej. Cumpleaños"],["estart","Inicio","datetime-local"],["eend","Fin","datetime-local"],["eloc","Ubicación","","p. ej. Parque Central"],["edesc","Detalles","textarea","Detalles del evento…"]],"bitcoin":[["btcaddr","Dirección de billetera","bc1q..."],["btcamt","Cantidad (BTC)","0.001"],["btclabel","Etiqueta","","p. ej. Café"],["btcmsg","Mensaje","","p. ej. Gracias"]],"coupon":[["cpcode","Código de cupón","AHORRA20"],["cpdesc","Descripción","","p. ej. 20% de descuento"]],"appstore":[["appios","Enlace App Store","https://apps.apple.com/app/..."],["appand","Enlace Google Play","https://play.google.com/store/apps/..."]],"review":[["rvlink","Enlace de reseñas","https://g.page/your-business/review"]],"mp3":[["mp3link","Enlace del audio","https://example.com/song.mp3"]],"google-form":[["gflink","Enlace del formulario","https://forms.gle/abc123XYZ"]],"menu":[["mnlink","Enlace del menú","https://example.com/menu"]]}, "modeStatic":"Estático", "modeDynamic":"Dinámico", "modeHint":"Los códigos estáticos no caducan. Los dinámicos se pueden editar tras imprimir y cuentan escaneos.", "dynDest":"URL de destino", "dynCreate":"Generar QR dinámico", "dynShort":"Tu enlace dinámico:", "copy":"Copiar", "dynIntro":"Diseña tu QR: elige un tipo, rellena el contenido y dale estilo. Luego crea un código dinámico: el QR impreso no cambia, pero puedes modificar su contenido cuando quieras.", "dynHint":"Rellena tu contenido y pulsa Generar.", "dynReady":"Tu código dinámico está listo. Imprímelo: el contenido puede cambiar cuando quieras.", "dynBlurHint":"Rellena tu contenido y pulsa Generar", "modeTip":"Estático: el contenido va dentro del QR — sin registro, vale para siempre. Dinámico: los escaneos pasan por un enlace corto — edita el contenido tras imprimir y ve estadísticas. Necesita registro gratuito.","signin":"Iniciar sesión","acctDashboard":"Dashboard","acctExport":"Exportar mis datos","acctDelete":"Eliminar cuenta","acctLogout":"Cerrar sesión","acctDeleteConfirm":"¿Eliminar tu cuenta? No se puede deshacer.","acctDeleteFailed":"No se pudo eliminar. Inténtalo de nuevo.","acctNetErr":"Error de red. Inténtalo de nuevo.","acctSignedInWith":"Sesión con {method}","moreFormats":"Más formatos","footGenerators":"Generadores","footMore":"Más","ariaCustomInk":"Color de tinta personalizado","ariaCustomBg":"Color de fondo personalizado","ariaUploadLogo":"Subir logotipo","ariaLanguage":"Idioma","dynDashLink":"Ver en el Panel →","dynSigninHint":"Inicia sesión para crear códigos dinámicos"},
pt:{title:"FreeQrly — Gerador de QR Code grátis | Estáticos sem cadastro",metaDesc:"Crie QR codes grátis no seu navegador, até com seu logo. Os estáticos não precisam de cadastro, sem rastreamento, sem expiração. Exporte em PNG e SVG.",navStudio:"Estúdio",navWhy:"Princípios",navFaq:"Perguntas",kicker:"Grátis · Estáticos sem cadastro · Privado por design",h1a:"Transforme",h1b:"qualquer coisa",h1c:"em QR code.",lede:"Os estáticos não precisam de cadastro. Feitos no seu navegador, valem para sempre. Os dinâmicos pedem uma conta grátis, para você editar depois de imprimir.",hc1:"Tipos de conteúdo",hc2:"Exportar",hc3:"Seus dados",hc3v:"Privado por design",hc4:"Preço",hc4v:"Grátis, para sempre",sOver:"O estúdio",sTitle:"Crie seu QR code",appearance:"Aparência",ink:"Tinta",paper:"Papel",background:"Fundo",dots:"Estilo dos pontos",ecc:"Correção de erros",dSquare:"Quadrado",dRound:"Redondo",dSoft:"Suave",dPebble:"Seixo",eL:"Baixo",eM:"Médio",eQ:"Alto",eH:"Máximo",eccHint:"Quanto maior, mais resiste a logos e desgaste.",dotsSub:"Formato dos pontos",eccSub:"Mais alto, mais resistente",colors:"Cores",colorsSub:"Toque ou personalize",transparentSub:"Sem fundo branco",size:"Tamanho de exportação",logo:"Adicione seu logo",logoSub:"Marca ou própria",privnote:"Códigos estáticos são gerados por completo no seu navegador.",live:"Prévia ao vivo — muda ao digitar",bLabel:"Um link por linha",bType:"Tipo",bUpload:"Enviar CSV / Excel",bTemplate:"Baixar modelo",bGo:"Gerar todos",bZip:"Baixar ZIP",bEmpty:"Digite pelo menos um link acima",featsK:"Além do código",featsT:"Tudo ao redor do QR",featsS:"Gerar é só o começo. Isto também vive dentro do FreeQrly.",f1t:"Scanner integrado",f1d:"Aponte a câmera ou suba uma imagem — os códigos são decodificados no seu navegador e nunca enviados a nenhum servidor. Funciona offline.",f1l:"Abrir o scanner →",f2t:"17 tipos de código",f2d:"Site, texto, WiFi, cartões de contato, e-mail, SMS, chamadas, locais, eventos de calendário, Bitcoin, Coupon, App Store, avaliações, áudio, formulários do Google, cardápios — mais modo lote para muitos de uma vez. Cada tipo gera o formato correto — sem decorar sintaxe.",f2l:"Testar todos →",f3t:"Geração em lote",f3d:"Cole até 50 links e receba 50 códigos prontos para impressão em um clique. Baixe um por um ou tudo em ZIP.",f3l:"Modo lote →",f4t:"Códigos de evento",f4d:"Um scan e seu evento — título, hora, local — entra direto no calendário do convidado. Feito para convites.",f4l:"Criar código de evento →",f5t:"Logo e estilo",f5d:"Coloque seu logo no centro e a correção de erros sobe sozinha para continuar escaneável. Mude pontos, tinta e papel — ou use fundo transparente.",f5l:"Códigos com logo →",f6t:"Histórico privado",f6d:"Cada download é lembrado só neste dispositivo — seus doze mais recentes, um clique para recuperar. Limpe quando quiser.",casesK:"No mundo real",casesT:"Feito para momentos reais",casesS:"Escolha seu cenário — a configuração já está pronta.",c1t:"Cartões de visita",c1d:"Seus contatos em um scan — direto para o telefone deles.",c2t:"Casamentos",c2d:"RSVP, fotos compartilhadas, adicionar ao calendário. A papelada, sem papel.",c3t:"Imobiliária",c3d:"Anúncios na placa. Agende uma visita em um scan.",c4t:"Eventos",c4d:"Check-in, validação de ingressos, álbuns compartilhados.",c5t:"Compartilhar WiFi",c5d:"Convidados online em um scan. Nunca mais soletre uma senha.",c6t:"Avaliações no Google",c6d:"Transforme clientes felizes em cinco estrelas, no balcão.",p1n:"N.º 1",p1t:"Seus dados não saem daqui",p1p:"Cada código estático é desenhado no seu dispositivo — sem uploads, sem rastreamento, sem conta. Carregue a página, desconecte-se, tudo continua funcionando.",p2n:"N.º 2",p2t:"Feitos para durar",p2p:"Um código estático carrega o destino dentro do padrão. Imprima hoje e ele será escaneado em dez anos. Sem renovações nem plataformas que desaparecem.",p3n:"N.º 3",p3t:"Grátis significa grátis",p3p:"Sem marca d'água, sem letra pequena. Os estáticos não precisam de cadastro. Sem plano Pro nem taxas ocultas — boas ferramentas deveriam ser grátis.",faqT:"Bom saber",q1:"Um QR code grátis expira?",a1:"Nunca. O destino vai codificado no padrão, então funciona enquanto o destino existir. Códigos dinâmicos pagos passam pelos servidores do fornecedor e podem morrer se você parar de pagar — mais um motivo para preferir o estático.",q2:"Minha senha do WiFi está segura aqui?",a2:"Em um código estático, sim. Sua senha nunca sai do seu navegador — nada é enviado a lugar algum. Precavido? Carregue a página, desconecte-se e digite.",q3:"Estático ou dinâmico?",a3:"Se o destino não vai mudar, use estático: WiFi, cartões, links fixos. Os dinâmicos (links editáveis + estatísticas de leitura) servem para campanhas — já estão no ar: conta grátis, edite depois de imprimir e veja as estatísticas.",q4:"Posso usar comercialmente?",a4:"Claro. Tudo que você criar aqui é seu — embalagens, cardápios, cartões, sem atribuição.",q5:"O FreeQrly é realmente grátis?",a5:"Sim — tudo nesta página é grátis, sem marca d'água. Os estáticos não precisam de conta. Não vendemos assinaturas; isto é uma ferramenta, não um funil.",q6:"Preciso de uma conta?",a6:"Para os estáticos, não. Não há nada para cadastrar — abra a página e crie seu código. Os dinâmicos pedem uma conta grátis, para editar depois de imprimir.",q7:"Posso colocar meu logo no código?",a7:"Sim — envie um logo quadrado e o colocamos no centro, aumentando automaticamente a correção de erros para continuar escaneável. Para impressão, use Q ou H.",fin:"Códigos estáticos, feitos no seu navegador.",dl:"Baixar",navScan:"Scanner",history:"Recentes",histClear:"Limpar",transparent:"Fundo transparente",frame:"Moldura",frameSub:"Borda ao redor do código",frameTextLabel:"Texto da moldura",frameNone:"Nenhuma",frameRounded:"Arredondada",frameCta:"Com texto",frameTextPh:"Escaneie",scanGood:"Bom contraste",scanBad:"Contraste baixo — pode não ler",types:{"url": ["Site", "link, página, vídeo"], "text": ["Texto", "qualquer palavra"], "wifi": ["WiFi", "conexão instantânea"], "vcard": ["Contato", "vCard"], "email": ["E-mail", "pré-preenchido"], "sms": ["SMS", "texto pré-preenchido"], "phone": ["Ligação", "tocar para ligar"], "geo": ["Lugar", "pino no mapa"],"event":["Evento","adicionar ao calendário"],"bitcoin":["Bitcoin","crypto payment"],"coupon":["Coupon","promo code"],"appstore":["App Store","iOS + Android"],"review":["Avaliações","avaliações 5 estrelas"],"mp3":["Áudio","MP3 e som"],"google-form":["Formulário","colete respostas"],"menu":["Cardápio","menu do restaurante"],"batch":["Lote", "vários de uma vez"]},fields:{"url": [["url", "Destino", "https://example.com"]], "text": [["text", "Mensagem", "textarea", "Olá, mundo!"]], "wifi": [["ssid", "Nome da rede", "MinhaWiFi"], ["pass", "Senha", "", "Senha do WiFi"], ["enc", "Segurança", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "Nome completo", "Maria Silva"], ["phone", "Telefone", "+55 11 90000 0000"], ["email", "E-mail", "maria@example.com"],["vcorg","Empresa","","Acme"],["vctitle","Cargo","","Designer"],["vcurl","Site","https://example.com"],["vcadr","Endereço","","Rua Principal 123"],["vcnote","Nota","",""]], "email": [["to", "Para", "ola@example.com"], ["subject", "Assunto", "Olá"], ["body", "Corpo", "textarea", "Corpo do e-mail…"]], "sms": [["phone", "Telefone", "+55 11 90000 0000"], ["body", "Mensagem", "", "Digite sua mensagem…"]], "phone": [["phone", "Telefone", "+55 11 90000 0000"]], "geo": [["lat", "Latitude", "-23.5558"], ["lng", "Longitude", "-46.6396"]],"event":[["etitle","Título","","ex.: Festa de aniversário"],["estart","Início","datetime-local"],["eend","Fim","datetime-local"],["eloc","Local","","ex.: Parque Central"],["edesc","Detalhes","textarea","Detalhes do evento…"]],"bitcoin":[["btcaddr","Wallet address","bc1q..."],["btcamt","Amount (BTC)","0.001"],["btclabel","Label","","e.g. Coffee"],["btcmsg","Message","","e.g. Thanks"]],"coupon":[["cpcode","Coupon code","SAVE20"],["cpdesc","Description","","e.g. 20% off"]],"appstore":[["appios","App Store link","https://apps.apple.com/app/..."],["appand","Google Play link","https://play.google.com/store/apps/..."]],"review":[["rvlink","Link de avaliações","https://g.page/your-business/review"]],"mp3":[["mp3link","Link do áudio","https://example.com/song.mp3"]],"google-form":[["gflink","Link do formulário","https://forms.gle/abc123XYZ"]],"menu":[["mnlink","Link do cardápio","https://example.com/menu"]]}, "modeStatic":"Estático", "modeDynamic":"Dinâmico", "modeHint":"Códigos estáticos nunca expiram. Códigos dinâmicos podem ser editados após imprimir e contam escaneamentos.", "dynDest":"URL de destino", "dynCreate":"Gerar QR dinâmico", "dynShort":"Seu link dinâmico:", "copy":"Copiar", "dynIntro":"Desenhe seu QR — escolha um tipo, preencha o conteúdo, estilize. Depois crie um código dinâmico: o QR impresso não muda, mas você pode alterar o conteúdo quando quiser.", "dynHint":"Preencha seu conteúdo e clique em Gerar.", "dynReady":"Seu QR dinâmico está pronto. Imprima-o: o conteúdo pode mudar quando quiser.", "dynBlurHint":"Preencha seu conteúdo e clique em Gerar", "modeTip":"Estático: o conteúdo vai dentro do QR — sem conta, vale para sempre. Dinâmico: escaneamentos passam por um link curto — edite o conteúdo após imprimir + estatísticas. Precisa de conta gratuita.","signin":"Entrar","acctDashboard":"Dashboard","acctExport":"Exportar meus dados","acctDelete":"Excluir conta","acctLogout":"Sair","acctDeleteConfirm":"Excluir sua conta? Não pode ser desfeito.","acctDeleteFailed":"Não foi possível excluir. Tente novamente.","acctNetErr":"Erro de rede. Tente novamente.","acctSignedInWith":"Sessão com {method}","moreFormats":"Mais formatos","footGenerators":"Geradores","footMore":"Mais","ariaCustomInk":"Cor de tinta personalizada","ariaCustomBg":"Cor de fundo personalizada","ariaUploadLogo":"Enviar logotipo","ariaLanguage":"Idioma","dynDashLink":"Ver no Painel →","dynSigninHint":"Entre para criar códigos dinâmicos"},
fr:{title:"FreeQrly — Générateur de QR code gratuit | Statiques sans inscription",metaDesc:"Créez des QR codes gratuits dans votre navigateur, même avec votre logo. Les statiques sans inscription, sans suivi, sans expiration. Export PNG et SVG.",navStudio:"Studio",navWhy:"Principes",navFaq:"Questions",kicker:"Gratuit · Statiques sans inscription · Privé par design",h1a:"Transformez",h1b:"n’importe quoi",h1c:"en QR code.",lede:"Les codes statiques sans inscription. Faits dans votre navigateur, pour toujours. Les dynamiques demandent un compte gratuit, pour les modifier après impression.",hc1:"Types de contenu",hc2:"Exporter",hc3:"Vos données",hc3v:"Privé par design",hc4:"Prix",hc4v:"Gratuit, pour toujours",sOver:"Le studio",sTitle:"Créez votre QR code",appearance:"Apparence",ink:"Encre",paper:"Papier",background:"Fond",dots:"Style des points",ecc:"Correction d'erreur",dSquare:"Carré",dRound:"Rond",dSoft:"Doux",dPebble:"Galet",eL:"Faible",eM:"Moyen",eQ:"Élevé",eH:"Maximal",eccHint:"Plus le niveau est haut, plus il résiste aux logos et à l'usure.",dotsSub:"Forme des points",eccSub:"Plus résistant",colors:"Couleurs",colorsSub:"Touchez ou personnalisez",transparentSub:"Sans fond blanc",size:"Taille d'export",logo:"Ajoutez votre logo",logoSub:"Marque ou perso",privnote:"Les codes statiques sont générés entièrement dans votre navigateur.",live:"Aperçu en direct — change à la frappe",bLabel:"Un lien par ligne",bType:"Type",bUpload:"Importer CSV / Excel",bTemplate:"Télécharger le modèle",bGo:"Tout générer",bZip:"Télécharger ZIP",bEmpty:"Saisissez au moins un lien ci-dessus",featsK:"Au-delà du code",featsT:"Tout autour du QR",featsS:"Générer n'est que le début. Ceci vit aussi dans FreeQrly.",f1t:"Scanner intégré",f1d:"Pointez votre caméra ou envoyez une image — les codes sont décodés dans votre navigateur et ne sont jamais téléversés. Fonctionne même hors ligne.",f1l:"Ouvrir le scanner →",f2t:"17 types de codes",f2d:"Site web, texte, WiFi, cartes de visite, e-mail, SMS, appels, lieux, événements, Bitcoin, Coupon, App Store, avis, audio, formulaires Google, menus — plus le mode lot pour plusieurs à la fois. Chaque type génère le bon format — aucune syntaxe à retenir.",f2l:"Tous les essayer →",f3t:"Génération en lot",f3d:"Collez jusqu'à 50 liens et obtenez 50 codes prêts à imprimer en un clic. Téléchargez un par un ou tout en ZIP.",f3l:"Mode lot →",f4t:"Codes d'événement",f4d:"Un scan et votre événement — titre, heure, lieu — entre dans le calendrier de l'invité. Pensé pour les invitations.",f4l:"Créer un code d'événement →",f5t:"Logo et style",f5d:"Placez votre logo au centre et la correction d'erreur augmente seule pour rester scannable. Changez points, encre et papier — ou passez au transparent.",f5l:"Codes avec logo →",f6t:"Historique privé",f6d:"Chaque téléchargement est mémorisé sur cet appareil uniquement — vos douze plus récents, un clic pour retrouver. Effacez à tout moment.",casesK:"Sur le terrain",casesT:"Pensé pour les vrais moments",casesS:"Choisissez votre scénario — la configuration est déjà prête.",c1t:"Cartes de visite",c1d:"Vos coordonnées en un scan — directement dans leur téléphone.",c2t:"Mariages",c2d:"RSVP, photos partagées, ajout au calendrier. La paperasse, sans papier.",c3t:"Immobilier",c3d:"Les annonces sur le panneau. Réservez une visite en un scan.",c4t:"Événements",c4d:"Enregistrement, validation des billets, albums partagés.",c5t:"Partage WiFi",c5d:"Invités connectés en un scan. Fini d'épeler les mots de passe.",c6t:"Avis Google",c6d:"Transformez vos clients satisfaits en cinq étoiles, au comptoir.",p1n:"N° 1",p1t:"Vos données ne bougent pas d'ici",p1p:"Chaque code statique est dessiné sur votre appareil — aucun envoi, aucun suivi, aucun compte. Chargez la page, déconnectez-vous, tout continue de marcher.",p2n:"N° 2",p2t:"Faits pour durer",p2p:"Un code statique porte sa destination dans le motif. Imprimez-le aujourd'hui, il se scannera dans dix ans. Ni renouvellement, ni plateforme qui disparaît.",p3n:"N° 3",p3t:"Gratuit veut dire gratuit",p3p:"Sans filigrane, sans petits caractères. Les statiques sans inscription. Ni offre Pro, ni frais cachés — les bons outils devraient être gratuits.",faqT:"Bon à savoir",q1:"Un QR code gratuit expire-t-il ?",a1:"Jamais. La destination est encodée dans le motif, donc il marche tant que la destination existe. Les codes dynamiques payants passent par les serveurs du fournisseur et peuvent mourir si vous arrêtez de payer — une raison de plus de préférer le statique.",q2:"Mon mot de passe WiFi est-il en sécurité ici ?",a2:"Pour un code statique, oui. Votre mot de passe ne quitte jamais votre navigateur — rien n'est envoyé nulle part. Prudent ? Chargez la page, déconnectez-vous, puis tapez.",q3:"Statique ou dynamique ?",a3:"Si la destination ne changera pas, prenez statique : WiFi, cartes de visite, liens fixes. Les dynamiques (liens modifiables + stats de scan) servent aux campagnes — c'est en ligne : compte gratuit, modifiez après impression et suivez les stats.",q4:"Puis-je les utiliser commercialement ?",a4:"Bien sûr. Tout ce que vous créez ici vous appartient — emballages, menus, cartes, sans attribution.",q5:"FreeQrly est-il vraiment gratuit ?",a5:"Oui — tout sur cette page est gratuit, sans filigrane. Les statiques sans compte. Nous ne vendons pas d'abonnements ; c'est un outil, pas un entonnoir.",q6:"Faut-il un compte ?",a6:"Pour les statiques, non. Il n'y a rien à quoi s'inscrire — ouvrez la page et créez votre code. Les dynamiques demandent un compte gratuit, pour les modifier après impression.",q7:"Puis-je ajouter mon logo au QR code ?",a7:"Oui — envoyez un logo carré, nous le plaçons au centre en augmentant automatiquement la correction d'erreur pour qu'il reste scannable. Pour l'impression, utilisez Q ou H.",fin:"Codes statiques, faits dans votre navigateur.",dl:"Télécharger",navScan:"Scanner",history:"Récents",histClear:"Effacer",transparent:"Fond transparent",frame:"Cadre",frameSub:"Bordure autour du code",frameTextLabel:"Texte du cadre",frameNone:"Aucun",frameRounded:"Arrondi",frameCta:"Avec texte",frameTextPh:"Scannez",scanGood:"Bon contraste",scanBad:"Faible contraste — peut ne pas se lire",types:{"url": ["Site web", "lien, page, vidéo"], "text": ["Texte", "n'importe quels mots"], "wifi": ["WiFi", "connexion instantanée"], "vcard": ["Contact", "vCard"], "email": ["E-mail", "pré-rempli"], "sms": ["SMS", "texte pré-rempli"], "phone": ["Appel", "toucher pour appeler"], "geo": ["Lieu", "épingle carte"],"event":["Événement","ajouter au calendrier"],"bitcoin":["Bitcoin","crypto payment"],"coupon":["Coupon","promo code"],"appstore":["App Store","iOS + Android"],"review":["Avis","avis 5 étoiles"],"mp3":["Audio","MP3 et son"],"google-form":["Formulaire","recueillez des réponses"],"menu":["Menu","carte du restaurant"],"batch":["Lot", "plusieurs à la fois"]},fields:{"url": [["url", "Destination", "https://example.com"]], "text": [["text", "Message", "textarea", "Bonjour, le monde !"]], "wifi": [["ssid", "Nom du réseau", "MonWiFi"], ["pass", "Mot de passe", "", "Mot de passe WiFi"], ["enc", "Sécurité", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "Nom complet", "Marie Dupont"], ["phone", "Téléphone", "+33 6 00 00 00 00"], ["email", "E-mail", "marie@example.com"],["vcorg","Entreprise","","Acme"],["vctitle","Fonction","","Designer"],["vcurl","Site web","https://example.com"],["vcadr","Adresse","","123 rue Principale"],["vcnote","Note","",""]], "email": [["to", "À", "bonjour@example.com"], ["subject", "Objet", "Bonjour"], ["body", "Corps", "textarea", "Corps de l'e-mail…"]], "sms": [["phone", "Téléphone", "+33 6 00 00 00 00"], ["body", "Message", "", "Écrivez votre message…"]], "phone": [["phone", "Téléphone", "+33 6 00 00 00 00"]], "geo": [["lat", "Latitude", "48.8566"], ["lng", "Longitude", "2.3522"]],"event":[["etitle","Titre","","ex. : Anniversaire"],["estart","Début","datetime-local"],["eend","Fin","datetime-local"],["eloc","Lieu","","ex. : Parc Central"],["edesc","Détails","textarea","Détails de l'événement…"]],"bitcoin":[["btcaddr","Wallet address","bc1q..."],["btcamt","Amount (BTC)","0.001"],["btclabel","Label","","e.g. Coffee"],["btcmsg","Message","","e.g. Thanks"]],"coupon":[["cpcode","Coupon code","SAVE20"],["cpdesc","Description","","e.g. 20% off"]],"appstore":[["appios","App Store link","https://apps.apple.com/app/..."],["appand","Google Play link","https://play.google.com/store/apps/..."]],"review":[["rvlink","Lien de la page d'avis","https://g.page/your-business/review"]],"mp3":[["mp3link","Lien du fichier audio","https://example.com/song.mp3"]],"google-form":[["gflink","Lien du formulaire","https://forms.gle/abc123XYZ"]],"menu":[["mnlink","Lien du menu","https://example.com/menu"]]}, "modeStatic":"Statique", "modeDynamic":"Dynamique", "modeHint":"Les codes statiques n’expirent jamais. Les codes dynamiques peuvent être modifiés après impression et comptent les scans.", "dynDest":"URL de destination", "dynCreate":"Générer un QR dynamique", "dynShort":"Votre lien dynamique :", "copy":"Copier", "dynIntro":"Concevez votre QR : choisissez un type, remplissez le contenu, personnalisez. Puis créez un code dynamique : le QR imprimé ne change pas, mais vous pouvez modifier son contenu à tout moment.", "dynHint":"Remplissez votre contenu, puis cliquez sur Générer.", "dynReady":"Votre QR dynamique est prêt. Imprimez-le : le contenu peut changer à tout moment.", "dynBlurHint":"Remplissez votre contenu, puis cliquez sur Générer", "modeTip":"Statique : le contenu est dans le QR — sans compte, valable toujours. Dynamique : les scans passent par un lien court — modifiez le contenu après impression + statistiques. Compte gratuit requis.","signin":"Se connecter","acctDashboard":"Dashboard","acctExport":"Exporter mes données","acctDelete":"Supprimer le compte","acctLogout":"Se déconnecter","acctDeleteConfirm":"Supprimer votre compte ? Irréversible.","acctDeleteFailed":"Suppression impossible. Réessayez.","acctNetErr":"Erreur réseau. Réessayez.","acctSignedInWith":"Connecté via {method}","moreFormats":"Plus de formats","footGenerators":"Générateurs","footMore":"Plus","ariaCustomInk":"Couleur d'encre personnalisée","ariaCustomBg":"Couleur d'arrière-plan personnalisée","ariaUploadLogo":"Téléverser un logo","ariaLanguage":"Langue","dynDashLink":"Voir dans le Tableau de bord →","dynSigninHint":"Connectez-vous pour créer des codes dynamiques"},
de:{title:"FreeQrly — Kostenloser QR-Code-Generator | Statische ohne Anmeldung",metaDesc:"QR-Codes kostenlos im Browser erstellen – sogar mit deinem Logo. Statische ohne Anmeldung, ohne Tracking, ohne Ablauf. Export als PNG & SVG.",navStudio:"Studio",navWhy:"Prinzipien",navFaq:"Fragen",kicker:"Kostenlos · Statische ohne Anmeldung · Privat per Design",h1a:"Verwandle",h1b:"alles",h1c:"in einen QR-Code.",lede:"Statische Codes ohne Anmeldung. Im Browser erstellt – für immer deiner. Dynamische brauchen ein kostenloses Konto, damit du sie nach dem Druck noch ändern kannst.",hc1:"Inhaltstypen",hc2:"Export",hc3:"Deine Daten",hc3v:"Privat per Design",hc4:"Preis",hc4v:"Für immer gratis",sOver:"Das Studio",sTitle:"QR-Code erstellen",appearance:"Darstellung",ink:"Tinte",paper:"Papier",background:"Hintergrund",dots:"Punktstil",ecc:"Fehlerkorrektur",dSquare:"Eckig",dRound:"Rund",dSoft:"Weich",dPebble:"Kiesel",eL:"Niedrig",eM:"Mittel",eQ:"Hoch",eH:"Maximal",eccHint:"Höher = robuster gegen Logos und Verschleiß.",dotsSub:"Punktform",eccSub:"Höher = robuster",colors:"Farben",colorsSub:"Tippen oder anpassen",transparentSub:"Ohne weißen Hintergrund",size:"Exportgröße",logo:"Logo hinzufügen",logoSub:"Marke oder eigen",privnote:"Statische Codes werden komplett in deinem Browser erzeugt.",live:"Live-Vorschau — ändert sich beim Tippen",bLabel:"Ein Link pro Zeile",bType:"Typ",bUpload:"CSV / Excel hochladen",bTemplate:"Vorlage herunterladen",bGo:"Alle erzeugen",bZip:"ZIP laden",bEmpty:"Gib oben mindestens einen Link ein",featsK:"Mehr als Code",featsT:"Alles rund um den QR",featsS:"Generieren ist nur der Anfang. Das steckt auch in FreeQrly.",f1t:"Scanner eingebaut",f1d:"Kamera draufhalten oder Bild hochladen — Codes werden direkt in deinem Browser entschlüsselt und nirgends hochgeladen. Funktioniert sogar offline.",f1l:"Scanner öffnen →",f2t:"17 Code-Typen",f2d:"Website, Text, WLAN, Visitenkarten, E-Mail, SMS, Anrufe, Orte, Kalenderevents, Bitcoin, Coupon, App Store, Bewertungen, Audio, Google-Formulare, Speisekarten — plus Stapelmodus für viele auf einmal. Jeder Typ baut automatisch das richtige Format — keine Syntax pauken.",f2l:"Alle ausprobieren →",f3t:"Stapelverarbeitung",f3d:"Bis zu 50 Links einfügen, 50 druckfertige Codes mit einem Klick. Einzeln laden oder alles als ZIP.",f3l:"Stapelmodus →",f4t:"Kalender-Event-Codes",f4d:"Ein Scan und deine Veranstaltung — Titel, Zeit, Ort — landet direkt im Kalender des Gastes. Gemacht für Einladungen.",f4l:"Event-Code erstellen →",f5t:"Logo & Styling",f5d:"Logo in die Mitte setzen — die Fehlerkorrektur steigt automatisch, damit es scanbar bleibt. Punkte, Tinte, Papier anpassen — oder transparent.",f5l:"Codes mit Logo →",f6t:"Privater Verlauf",f6d:"Jeder Download wird nur auf diesem Gerät gemerkt — deine zwölf neuesten, ein Klick zum Wiederherstellen. Jederzeit löschbar.",casesK:"In freier Wildbahn",casesT:"Für echte Momente gemacht",casesS:"Wähl dein Szenario — das Setup steht schon.",c1t:"Visitenkarten",c1d:"Deine Kontaktdaten in einem Scan — direkt aufs Handy.",c2t:"Hochzeiten",c2d:"RSVP, Fotoalben, Kalender-Eintrag. Der Papierkram, ohne Papier.",c3t:"Immobilien",c3d:"Exposés am Schild. Besichtigung in einem Scan buchen.",c4t:"Events",c4d:"Check-in, Ticketprüfung, geteilte Alben.",c5t:"WLAN teilen",c5d:"Gäste in einem Scan online. Nie wieder Passwörter buchstabieren.",c6t:"Google-Bewertungen",c6d:"Aus zufriedenen Kunden Fünf-Sterne direkt an der Theke machen.",p1n:"Nr. 1",p1t:"Deine Daten gehen nirgendwo hin",p1p:"Jeder statische Code wird auf deinem Gerät gezeichnet — keine Uploads, kein Tracking, kein Konto. Seite laden, Stecker ziehen, alles läuft weiter.",p2n:"Nr. 2",p2t:"Gemacht für die Dauer",p2p:"Ein statischer Code trägt sein Ziel im Muster. Heute drucken, in zehn Jahren scannen. Keine Verlängerung, keine Plattform, die verschwindet.",p3n:"Nr. 3",p3t:"Gratis heißt gratis",p3p:"Kein Wasserzeichen, kein Kleingedrucktes. Statische ohne Anmeldung. Kein Pro-Tarif, keine versteckten Kosten — gute Werkzeuge sollten einfach gratis sein.",faqT:"Gut zu wissen",q1:"Laufen kostenlose QR-Codes ab?",a1:"Nie. Das Ziel ist direkt im Muster codiert — der Code funktioniert, solange das Ziel existiert. Bezahlte dynamische Codes laufen über Server des Anbieters und können sterben, wenn du nicht mehr zahlst — ein Grund mehr für statisch.",q2:"Ist mein WLAN-Passwort hier sicher?",a2:"Bei einem statischen Code ja. Dein Passwort verlässt nie deinen Browser — nichts wird irgendwohin gesendet. Vorsichtig? Seite laden, offline gehen, dann tippen.",q3:"Statisch oder dynamisch?",a3:"Wenn sich das Ziel nicht ändert: statisch — WLAN, Visitenkarten, feste Links. Dynamische Codes (änderbare Links + Scan-Statistiken) sind für Kampagnen — jetzt live: kostenloses Konto, nach dem Druck änderbar, Scans im Blick.",q4:"Darf ich sie kommerziell nutzen?",a4:"Absolut. Alles, was du hier erstellst, gehört dir — Verpackungen, Speisekarten, Karten, ohne Namensnennung.",q5:"Ist FreeQrly wirklich kostenlos?",a5:"Ja — alles auf dieser Seite ist gratis, ohne Wasserzeichen. Statische ohne Konto. Wir verkaufen keine Abos; das hier ist ein Werkzeug, kein Trichter.",q6:"Brauche ich ein Konto?",a6:"Für statische nicht. Es gibt nichts anzumelden — Seite öffnen, Code erstellen. Dynamische brauchen ein kostenloses Konto, damit du sie nach dem Druck noch ändern kannst.",q7:"Kann ich mein Logo in den QR-Code setzen?",a7:"Ja — lade ein quadratisches Logo hoch, wir setzen es in die Mitte und erhöhen automatisch die Fehlerkorrektur, damit er scanbar bleibt. Für Druck: Q oder H.",fin:"Statische Codes, im Browser erstellt.",dl:"Herunterladen",navScan:"Scanner",history:"Zuletzt",histClear:"Löschen",transparent:"Transparenter Hintergrund",frame:"Rahmen",frameSub:"Rahmen um den Code",frameTextLabel:"Rahmentext",frameNone:"Keiner",frameRounded:"Abgerundet",frameCta:"Mit Text",frameTextPh:"Scannen",scanGood:"Guter Kontrast",scanBad:"Niedriger Kontrast — evtl. nicht lesbar",types:{"url": ["Webseite", "Link, Seite, Video"], "text": ["Text", "beliebige Wörter"], "wifi": ["WLAN", "sofort verbinden"], "vcard": ["Kontakt", "vCard"], "email": ["E-Mail", "vorausgefüllt"], "sms": ["SMS", "vorausgefüllter Text"], "phone": ["Anruf", "tippen zum Wählen"], "geo": ["Ort", "Karten-Pin"],"event":["Termin","zum Kalender"],"bitcoin":["Bitcoin","crypto payment"],"coupon":["Coupon","promo code"],"appstore":["App Store","iOS + Android"],"review":["Bewertungen","5-Sterne-Bewertungen"],"mp3":["Audio","MP3 & Sound"],"google-form":["Formular","Antworten sammeln"],"menu":["Speisekarte","Restaurantmenü"],"batch":["Stapel", "viele auf einmal"]},fields:{"url": [["url", "Ziel", "https://example.com"]], "text": [["text", "Nachricht", "textarea", "Hallo, Welt!"]], "wifi": [["ssid", "Netzwerkname", "MeinWLAN"], ["pass", "Passwort", "", "WLAN-Passwort"], ["enc", "Verschlüsselung", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "Vollständiger Name", "Max Mustermann"], ["phone", "Telefon", "+49 170 000000"], ["email", "E-Mail", "max@example.com"],["vcorg","Firma","","Acme"],["vctitle","Berufsbezeichnung","","Designer"],["vcurl","Webseite","https://example.com"],["vcadr","Adresse","","Hauptstraße 123"],["vcnote","Notiz","",""]], "email": [["to", "An", "hallo@example.com"], ["subject", "Betreff", "Hallo"], ["body", "Text", "textarea", "E-Mail-Text…"]], "sms": [["phone", "Telefon", "+49 170 000000"], ["body", "Nachricht", "", "Nachricht eingeben…"]], "phone": [["phone", "Telefon", "+49 170 000000"]], "geo": [["lat", "Breitengrad", "52.5200"], ["lng", "Längengrad", "13.4050"]],"event":[["etitle","Titel","","z. B. Geburtstagsparty"],["estart","Beginn","datetime-local"],["eend","Ende","datetime-local"],["eloc","Ort","","z. B. Central Park"],["edesc","Details","textarea","Veranstaltungsdetails…"]],"bitcoin":[["btcaddr","Wallet address","bc1q..."],["btcamt","Amount (BTC)","0.001"],["btclabel","Label","","e.g. Coffee"],["btcmsg","Message","","e.g. Thanks"]],"coupon":[["cpcode","Coupon code","SAVE20"],["cpdesc","Description","","e.g. 20% off"]],"appstore":[["appios","App Store link","https://apps.apple.com/app/..."],["appand","Google Play link","https://play.google.com/store/apps/..."]],"review":[["rvlink","Link zur Bewertungsseite","https://g.page/your-business/review"]],"mp3":[["mp3link","Link zur Audiodatei","https://example.com/song.mp3"]],"google-form":[["gflink","Link zum Formular","https://forms.gle/abc123XYZ"]],"menu":[["mnlink","Link zur Speisekarte","https://example.com/menu"]]}, "modeStatic":"Statisch", "modeDynamic":"Dynamisch", "modeHint":"Statische Codes laufen nie ab. Dynamische Codes lassen sich nach dem Druck ändern und zählen Scans.", "dynDest":"Ziel-URL", "dynCreate":"Dynamischen QR generieren", "dynShort":"Ihr dynamischer Link:", "copy":"Kopieren", "dynIntro":"Gestalten Sie Ihren QR: Typ wählen, Inhalt eingeben, stylen. Erstellen Sie dann einen dynamischen Code: Der gedruckte QR bleibt gleich, aber Sie können seinen Inhalt jederzeit ändern.", "dynHint":"Füllen Sie Ihren Inhalt aus und klicken Sie auf Generieren.", "dynReady":"Ihr dynamischer QR ist fertig. Drucken Sie ihn — der Inhalt kann jederzeit geändert werden.", "dynBlurHint":"Füllen Sie Ihren Inhalt aus und klicken Sie auf Generieren", "modeTip":"Statisch: Der Inhalt steckt im QR — ohne Konto, für immer gültig. Dynamisch: Scans laufen über einen Kurzlink — Inhalt nach dem Druck ändern + Statistiken. Kostenloses Konto erforderlich.","signin":"Anmelden","acctDashboard":"Dashboard","acctExport":"Meine Daten exportieren","acctDelete":"Konto löschen","acctLogout":"Abmelden","acctDeleteConfirm":"Konto wirklich löschen? Kann nicht rückgängig gemacht werden.","acctDeleteFailed":"Löschen fehlgeschlagen. Bitte erneut versuchen.","acctNetErr":"Netzwerkfehler. Bitte erneut versuchen.","acctSignedInWith":"Angemeldet mit {method}","moreFormats":"Weitere Formate","footGenerators":"Generatoren","footMore":"Mehr","ariaCustomInk":"Benutzerdefinierte Tintenfarbe","ariaCustomBg":"Benutzerdefinierte Hintergrundfarbe","ariaUploadLogo":"Logo hochladen","ariaLanguage":"Sprache","dynDashLink":"Im Dashboard ansehen →","dynSigninHint":"Melde dich an, um dynamische Codes zu erstellen"},
ja:{title:"FreeQrly — 無料QRコード生成 | 静的コードは登録不要",metaDesc:"ブラウザで無料QRコードを作成。ロゴ入りもOK。静的コードは登録不要・追跡なし・無期限。PNG / SVGで書き出し。",navStudio:"スタジオ",navWhy:"こだわり",navFaq:"よくある質問",kicker:"無料 · 静的コードは登録不要 · プライバシー優先",h1a:"",h1b:"何でも",h1c:"QRコードに。",lede:"静的コードは登録不要。ブラウザで作成、ずっと使える。動的コードは無料登録が必要で、印刷後も内容を変更できます。",hc1:"コンテンツの種類",hc2:"書き出し",hc3:"あなたのデータ",hc3v:"プライバシー優先",hc4:"料金",hc4v:"ずっと無料",sOver:"スタジオ",sTitle:"QRコードを作成",appearance:"見た目",ink:"インク",paper:"用紙",background:"背景",dots:"ドットの形",ecc:"誤り訂正",dSquare:"四角",dRound:"丸",dSoft:"やわらか",dPebble:"小石",eL:"低",eM:"中",eQ:"高",eH:"最高",eccHint:"レベルが高いほどロゴや摩耗に強い。",dotsSub:"ドットの形",eccSub:"高いほど丈夫",colors:"色",colorsSub:"タップまたはカスタム",transparentSub:"白背景なし",size:"書き出しサイズ",logo:"ロゴを追加",logoSub:"ブランドまたは自作",privnote:"静的コードはすべてブラウザ内でローカルに生成されます。",live:"ライブプレビュー — 入力と同時に変わる",bLabel:"1行に1リンク",bType:"Type",bUpload:"Upload CSV / Excel",bTemplate:"Download template",bGo:"すべて生成",bZip:"ZIPをダウンロード",bEmpty:"まず上にリンクを1つ以上入力してください",featsK:"コードの先へ",featsT:"QRの周りのすべて",featsS:"生成は始まりにすぎません。FreeQrlyにはこんなものも。",f1t:"内蔵スキャナー",f1d:"カメラを向けるか画像をアップ—コードはブラウザ内で直接読み取られ、サーバーに送信されません。オフラインでも動作します。",f1l:"スキャナーを開く →",f2t:"17種類のコード",f2d:"Web、テキスト、WiFi、名刺、メール、SMS、通話、場所、カレンダー予定、ビットコイン、クーポン、App Store、レビュー、音声、Google フォーム、メニュー — 一括モードでまとめて複数も可。各タイプが正しい形式を自動生成—書式を覚える必要なし。",f2l:"全部試す →",f3t:"一括生成",f3d:"リンクを50件まで貼り付けて、ワンクリックで50個の印刷用コードに。個別にもZIPまとめでもダウンロード。",f3l:"一括モード →",f4t:"予定コード",f4d:"スキャンひとつで予定—タイトル・時間・場所—がゲストのカレンダーに。招待状のために生まれました。",f4l:"予定コードを作る →",f5t:"ロゴとスタイル",f5d:"中央にロゴを置けば、読み取り精度を保つため誤り訂正が自動で上がります。ドット・インク・用紙を変更—透明背景も。",f5l:"ロゴ入りコード →",f6t:"プライベート履歴",f6d:"ダウンロードはこのデバイスにだけ記憶—最新12件をワンクリックで復元。いつでも消去できます。",casesK:"現場で",casesT:"リアルな瞬間のために",casesS:"シーンを選ぶだけ—設定は用意済みです。",c1t:"名刺",c1d:"スキャンひとつで連絡先が相手のスマホに。",c2t:"結婚式",c2d:"出欠確認・写真共有・カレンダー登録。紙の手続きを、紙なしで。",c3t:"不動産",c3d:"看板の物件情報をスキャン。そのまま内見予約。",c4t:"イベント",c4d:"チェックイン、チケット確認、共有アルバム。",c5t:"WiFi共有",c5d:"ゲストはスキャンひとつで接続。パスワードを読み上げる時代は終わり。",c6t:"Googleレビュー",c6d:"満足したお客様を、その場で星5つの評価に。",p1n:"その一",p1t:"データはどこにも行かない",p1p:"静的コードはすべてあなたのデバイス上で描画 — アップロードなし、追跡なし、アカウント不要。ページを読み込んで、回線を抜いても、そのまま使えます。",p2n:"その二",p2t:"長持ちする作り",p2p:"静的コードは行き先を模様の中に持ちます。今日印刷して、10年後も読み取れます。更新も、消えるプラットフォームの心配もなし。",p3n:"その三",p3t:"無料は、ただの無料",p3p:"透かしなし、小さな文字の条件なし。静的コードは登録不要。Pro版も隠れた料金もなし — 良い道具は無料であるべきです。",faqT:"知っておきたいこと",q1:"無料のQRコードに期限はある？",a1:"ありません。行き先は模様に直接記録されるので、行き先が有効な限り使えます。有料の動的コードは事業者のサーバー経由で、支払いを止めると使えなくなることも — 静的コードが安心な理由です。",q2:"WiFiのパスワードを入力しても安全？",a2:"静的コードなら安全です。パスワードがブラウザの外に出ることはありません。心配なら、ページを読み込んでからネットを切って入力してください。",q3:"静的と動的、どっちを選ぶ？",a3:"行き先が変わらないなら静的:WiFi、名刺、固定リンク。動的(書き換え可能なリンク+読み取り統計)はキャンペーン向け — すでに公開中:無料登録、印刷後の編集、スキャン統計の確認が可能。",q4:"商用利用できる？",a4:"もちろんです。ここで作ったコードはすべてあなたのもの — パッケージ、メニュー、名刺に、クレジット表記不要で使えます。",q5:"FreeQrlyは本当に無料？",a5:"本当です。このページの機能はすべて無料、透かしなし。静的コードはアカウント不要。サブスクの販売はしていません — これは道具であって、売り込みではありません。",q6:"アカウントは必要？",a6:"静的コードは不要です。登録するものは何もありません — ページを開いて、コードを作るだけ。動的コードは無料登録が必要で、印刷後も内容を変更できます。",q7:"QRコードにロゴを入れられる？",a7:"はい — 正方形のロゴをアップすると中央に配置し、誤り訂正を自動で上げて読み取り可能に保ちます。印刷用にはQかHをどうぞ。",fin:"静的コードはブラウザで作成。",dl:"ダウンロード",navScan:"スキャナー",history:"履歴",histClear:"クリア",transparent:"透明な背景",types:{"url": ["ウェブサイト", "リンク、ページ、動画"], "text": ["テキスト", "好きな言葉"], "wifi": ["WiFi", "すぐ接続"], "vcard": ["連絡先", "vCard"], "email": ["メール", "下書き付き"], "sms": ["SMS", "本文付き"], "phone": ["電話", "タップで発信"], "geo": ["場所", "マップのピン"],"event":["イベント","カレンダーに追加"],"bitcoin":["ビットコイン","暗号資産決済"],"coupon":["クーポン","プロモコード"],"appstore":["App Store","iOS + Android"],"review":["レビュー","高評価を集める"],"mp3":["音声","MP3・サウンド"],"google-form":["フォーム","回答を集める"],"menu":["メニュー","レストランメニュー"],"batch":["一括", "まとめて複数"]},fields:{"url": [["url", "行き先", "https://example.com"]], "text": [["text", "メッセージ", "textarea", "こんにちは、世界！"]], "wifi": [["ssid", "ネットワーク名", "MyWiFi"], ["pass", "パスワード", "", "WiFiパスワード"], ["enc", "暗号化", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "氏名", "山田太郎"], ["phone", "電話", "+81 90 0000 0000"], ["email", "メール", "taro@example.com"],["vcorg","会社","","Acme"],["vctitle","役職","","デザイナー"],["vcurl","ウェブサイト","https://example.com"],["vcadr","住所","","メインストリート123"],["vcnote","メモ","",""]], "email": [["to", "宛先", "hello@example.com"], ["subject", "件名", "こんにちは"], ["body", "本文", "textarea", "メール本文…"]], "sms": [["phone", "電話", "+81 90 0000 0000"], ["body", "メッセージ", "", "メッセージを入力…"]], "phone": [["phone", "電話", "+81 90 0000 0000"]], "geo": [["lat", "緯度", "35.6762"], ["lng", "経度", "139.6503"]],"event":[["etitle","タイトル","","例：誕生日パーティ"],["estart","開始","datetime-local"],["eend","終了","datetime-local"],["eloc","場所","","例：中央公園"],["edesc","詳細","textarea","イベント詳細…"]],"bitcoin":[["btcaddr","ウォレットアドレス","bc1q..."],["btcamt","金額 (BTC)","0.001"],["btclabel","ラベル","","例：コーヒー"],["btcmsg","メッセージ","","例：ありがとう"]],"coupon":[["cpcode","クーポンコード","SAVE20"],["cpdesc","説明","","例：20%オフ"]],"appstore":[["appios","App Store リンク","https://apps.apple.com/app/..."],["appand","Google Play リンク","https://play.google.com/store/apps/..."]],"review":[["rvlink","レビューページのリンク","https://g.page/your-business/review"]],"mp3":[["mp3link","音声ファイルのリンク","https://example.com/song.mp3"]],"google-form":[["gflink","フォームのリンク","https://forms.gle/abc123XYZ"]],"menu":[["mnlink","メニューのリンク","https://example.com/menu"]]}, "modeStatic":"静的", "modeDynamic":"動的", "modeHint":"静的コードは有効期限がありません。動的コードは印刷後も変更でき、スキャン数を数えられます。", "dynDest":"遷移先URL", "dynCreate":"動的QRを生成", "dynShort":"動的QRリンク:", "copy":"コピー", "dynIntro":"QRをデザインしてください — タイプを選び、内容を入力し、スタイルを整えます。次に動的コードを作成：印刷されたQRは変わりませんが、内容はいつでも変更できます。", "dynHint":"内容を入力して「生成」を押してください。", "dynReady":"動的QRができました。印刷してください — 内容はいつでも変更できます。", "dynBlurHint":"内容を入力して「生成」を押してください", "modeTip":"静的：内容はQR内に直接 — 登録不要、永久有効。動的：スキャンは短縮リンク経由 — 印刷後に内容変更＋統計表示。無料登録が必要です。","signin":"ログイン","acctDashboard":"Dashboard","acctExport":"データをエクスポート","acctDelete":"アカウントを削除","acctLogout":"ログアウト","acctDeleteConfirm":"アカウントを削除しますか？元に戻せません。","acctDeleteFailed":"削除できませんでした。もう一度お試しください。","acctNetErr":"ネットワークエラー。もう一度お試しください。","acctSignedInWith":"{method}でログイン中","moreFormats":"その他の形式","footGenerators":"ジェネレーター","footMore":"その他","ariaCustomInk":"カスタムインク色","ariaCustomBg":"カスタム背景色","ariaUploadLogo":"ロゴをアップロード","ariaLanguage":"言語","dynDashLink":"ダッシュボードで見る →","dynSigninHint":"動的コードを作成するにはログインしてください","frame":"フレーム","frameSub":"コードの周りの枠","frameTextLabel":"フレームテキスト","frameNone":"なし","frameRounded":"角丸","frameCta":"テキスト付き","frameTextPh":"スキャン","scanGood":"コントラスト良好","scanBad":"コントラストが低いため読み取れない場合があります"},
ru:{title:"FreeQrly — бесплатный генератор QR-кодов | Статические без регистрации",metaDesc:"Создавайте QR-коды бесплатно прямо в браузере — даже с вашим логотипом. Статические без регистрации, без слежки, без срока действия. Экспорт в PNG и SVG.",navStudio:"Студия",navWhy:"Принципы",navFaq:"Вопросы",kicker:"Бесплатно · Статические без регистрации · Приватность по дизайну",h1a:"Превратите",h1b:"что угодно",h1c:"в QR-код.",lede:"Статические коды без регистрации. Создаются в вашем браузере — навсегда ваши. Динамические требуют бесплатный аккаунт, чтобы менять их после печати.",hc1:"Типы контента",hc2:"Экспорт",hc3:"Ваши данные",hc3v:"Приватность по дизайну",hc4:"Цена",hc4v:"Бесплатно, навсегда",sOver:"Студия",sTitle:"Создать QR-код",appearance:"Внешний вид",ink:"Чернила",paper:"Бумага",background:"Фон",dots:"Форма точек",ecc:"Коррекция ошибок",dSquare:"Квадрат",dRound:"Круг",dSoft:"Мягкий",dPebble:"Галька",eL:"Низкий",eM:"Средний",eQ:"Высокий",eH:"Максимум",eccHint:"Чем выше уровень, тем устойчивее к логотипам и износу.",dotsSub:"Форма точек",eccSub:"Выше — прочнее",colors:"Цвета",colorsSub:"Выберите или настройте",transparentSub:"Без белого фона",size:"Размер экспорта",logo:"Добавить логотип",logoSub:"Бренд или свой",privnote:"Статические коды генерируются полностью в вашем браузере.",live:"Живой предпросмотр — меняется при вводе",bLabel:"Одна ссылка на строку",bType:"Type",bUpload:"Upload CSV / Excel",bTemplate:"Download template",bGo:"Создать все",bZip:"Скачать ZIP",bEmpty:"Сначала введите хотя бы одну ссылку выше",featsK:"Больше, чем код",featsT:"Всё вокруг QR",featsS:"Генерация — только начало. Внутри FreeQrly есть и это.",f1t:"Встроенный сканер",f1d:"Наведите камеру или загрузите изображение — коды расшифровываются прямо в браузере и никуда не отправляются. Работает даже офлайн.",f1l:"Открыть сканер →",f2t:"17 типов кодов",f2d:"Сайт, текст, WiFi, визитки, почта, SMS, звонки, места, события календаря, Биткоин, Купон, Магазин приложений, отзывы, аудио, Google-формы, меню — плюс пакетный режим для многих сразу. Каждый тип сам строит правильный формат — ничего запоминать не нужно.",f2l:"Попробовать все →",f3t:"Пакетная генерация",f3d:"Вставьте до 50 ссылок и получите 50 готовых к печати кодов в один клик. Скачивайте по одному или всё сразу в ZIP.",f3l:"Пакетный режим →",f4t:"Коды событий",f4d:"Одно сканирование — и ваше событие с названием, временем и местом окажется в календаре гостя. Создано для приглашений.",f4l:"Создать код события →",f5t:"Логотип и стиль",f5d:"Поставьте логотип в центр — коррекция ошибок повысится сама, чтобы код продолжал считываться. Меняйте точки, чернила и бумагу — или сделайте фон прозрачным.",f5l:"Коды с логотипом →",f6t:"Приватная история",f6d:"Каждое скачивание запоминается только на этом устройстве — двенадцать последних, возврат в один клик. Очистите в любой момент.",casesK:"В реальной жизни",casesT:"Создано для настоящих моментов",casesS:"Выберите свой сценарий — настройка уже готова.",c1t:"Визитки",c1d:"Ваши контакты в одно сканирование — прямо в их телефон.",c2t:"Свадьбы",c2d:"RSVP, общие фото, добавление в календарь. Бумажная волокита — без бумаги.",c3t:"Недвижимость",c3d:"Объявления на стенде. Запись на просмотр в одно сканирование.",c4t:"Мероприятия",c4d:"Регистрация, проверка билетов, общие альбомы.",c5t:"Раздача WiFi",c5d:"Гости в сети в одно сканирование. Больше не диктуйте пароль.",c6t:"Отзывы в Google",c6d:"Превращайте довольных клиентов в пять звёзд прямо у стойки.",p1n:"№ 1",p1t:"Ваши данные никуда не уходят",p1p:"Каждый статический код рисуется на вашем устройстве — без загрузок, без слежки, без аккаунтов. Загрузите страницу, выдерните кабель — всё продолжит работать.",p2n:"№ 2",p2t:"Сделаны надолго",p2p:"Статический код несёт адрес внутри узора. Напечатайте сегодня — отсканируется и через десять лет. Без продлений и исчезающих платформ.",p3n:"№ 3",p3t:"Бесплатно значит бесплатно",p3p:"Без водяных знаков, без мелкого шрифта. Статические без регистрации. Без Pro-тарифа и скрытых платежей — хорошие инструменты должны быть бесплатными.",faqT:"Полезно знать",q1:"Бесплатные QR-коды истекают?",a1:"Никогда. Адрес закодирован прямо в узоре, поэтому код работает, пока работает адрес. Платные динамические коды идут через серверы поставщика и могут умереть, если перестать платить, — ещё одна причина любить статику.",q2:"Мой пароль от WiFi здесь в безопасности?",a2:"Для статического кода — да. Пароль никогда не покидает ваш браузер — ничего никуда не отправляется. Перестраховаться? Загрузите страницу, отключитесь и вводите.",q3:"Статический или динамический?",a3:"Если адрес не изменится — статический: WiFi, визитки, постоянные ссылки. Динамические (изменяемые ссылки + статистика сканов) — для кампаний, уже работают: бесплатный аккаунт, правки после печати, просмотр статистики.",q4:"Можно использовать в коммерческих целях?",a4:"Конечно. Всё созданное здесь — ваше: упаковка, меню, визитки, без указания авторства.",q5:"FreeQrly правда бесплатный?",a5:"Да — всё на этой странице бесплатно, без водяных знаков. Статические без аккаунта. Мы не продаём подписки; это инструмент, а не воронка.",q6:"Нужен аккаунт?",a6:"Для статических — нет. Регистрироваться негде — откройте страницу и создайте код. Динамические требуют бесплатный аккаунт, чтобы менять их после печати.",q7:"Можно добавить логотип в QR-код?",a7:"Да — загрузите квадратный логотип, мы разместим его в центре и автоматически повысим коррекцию ошибок, чтобы код сканировался. Для печати выбирайте Q или H.",fin:"Статические коды, сделаны в вашем браузере.",dl:"Скачать",navScan:"Сканер",history:"Недавние",histClear:"Очистить",transparent:"Прозрачный фон",types:{"url": ["Сайт", "ссылка, страница, видео"], "text": ["Текст", "любые слова"], "wifi": ["WiFi", "мгновенное подключение"], "vcard": ["Контакт", "vCard"], "email": ["Почта", "с заготовкой"], "sms": ["SMS", "с текстом"], "phone": ["Звонок", "нажать для вызова"], "geo": ["Место", "метка на карте"],"event":["Событие","в календарь"],"bitcoin":["Биткоин","криптоплатёж"],"coupon":["Купон","промокод"],"appstore":["Магазин приложений","iOS + Android"],"review":["Отзывы","собирайте отзывы"],"mp3":["Аудио","MP3 и звук"],"google-form":["Google-форма","собирайте ответы"],"menu":["Меню","меню ресторана"],"batch":["Пакет", "много сразу"]},fields:{"url": [["url", "Адрес", "https://example.com"]], "text": [["text", "Сообщение", "textarea", "Привет, мир!"]], "wifi": [["ssid", "Имя сети", "MyWiFi"], ["pass", "Пароль", "", "Пароль WiFi"], ["enc", "Защита", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "Полное имя", "Иван Петров"], ["phone", "Телефон", "+7 900 000-00-00"], ["email", "Почта", "ivan@example.com"],["vcorg","Компания","","Акме"],["vctitle","Должность","","Дизайнер"],["vcurl","Сайт","https://example.com"],["vcadr","Адрес","","ул. Главная, 123"],["vcnote","Заметка","",""]], "email": [["to", "Кому", "hello@example.com"], ["subject", "Тема", "Привет"], ["body", "Текст", "textarea", "Текст письма…"]], "sms": [["phone", "Телефон", "+7 900 000-00-00"], ["body", "Сообщение", "", "Введите сообщение…"]], "phone": [["phone", "Телефон", "+7 900 000-00-00"]], "geo": [["lat", "Широта", "55.7558"], ["lng", "Долгота", "37.6173"]],"event":[["etitle","Название","","напр. День рождения"],["estart","Начало","datetime-local"],["eend","Конец","datetime-local"],["eloc","Место","","напр. Центральный парк"],["edesc","Детали","textarea","Детали события…"]],"bitcoin":[["btcaddr","Адрес кошелька","bc1q..."],["btcamt","Сумма (BTC)","0.001"],["btclabel","Метка","","напр.: Кофе"],["btcmsg","Сообщение","","напр.: Спасибо"]],"coupon":[["cpcode","Код купона","SKIDKA20"],["cpdesc","Описание","","напр.: скидка 20%"]],"appstore":[["appios","Ссылка App Store","https://apps.apple.com/app/..."],["appand","Ссылка Google Play","https://play.google.com/store/apps/..."]],"review":[["rvlink","Ссылка на отзывы","https://g.page/your-business/review"]],"mp3":[["mp3link","Ссылка на аудио","https://example.com/song.mp3"]],"google-form":[["gflink","Ссылка на форму","https://forms.gle/abc123XYZ"]],"menu":[["mnlink","Ссылка на меню","https://example.com/menu"]]}, "modeStatic":"Статический", "modeDynamic":"Динамический", "modeHint":"Статические коды не истекают. Динамические можно редактировать после печати и отслеживать сканы.", "dynDest":"Целевой URL", "dynCreate":"Создать динамический QR", "dynShort":"Ваша динамическая ссылка:", "copy":"Копировать", "dynIntro":"Оформите QR — выберите тип, заполните содержимое, настройте стиль. Затем создайте динамический код: напечатанный QR не изменится, но его содержимое можно менять в любое время.", "dynHint":"Заполните содержимое и нажмите «Создать».", "dynReady":"Динамический QR готов. Печатайте — содержимое можно менять в любое время.", "dynBlurHint":"Заполните содержимое и нажмите «Создать»", "modeTip":"Статический: контент внутри QR — без аккаунта, навсегда. Динамический: сканы идут через короткую ссылку — меняйте контент после печати + статистика. Нужен бесплатный аккаунт.","signin":"Войти","acctDashboard":"Dashboard","acctExport":"Экспортировать мои данные","acctDelete":"Удалить аккаунт","acctLogout":"Выйти","acctDeleteConfirm":"Удалить аккаунт? Это необратимо.","acctDeleteFailed":"Не удалось удалить. Попробуйте ещё раз.","acctNetErr":"Ошибка сети. Попробуйте ещё раз.","acctSignedInWith":"Вход через {method}","moreFormats":"Другие форматы","footGenerators":"Генераторы","footMore":"Ещё","ariaCustomInk":"Пользовательский цвет чернил","ariaCustomBg":"Пользовательский цвет фона","ariaUploadLogo":"Загрузить логотип","ariaLanguage":"Язык","dynDashLink":"Посмотреть в Панели управления →","dynSigninHint":"Войдите, чтобы создавать динамические коды","frame":"Рамка","frameSub":"Рамка вокруг кода","frameTextLabel":"Текст рамки","frameNone":"Без","frameRounded":"Скруглённая","frameCta":"С текстом","frameTextPh":"Сканируйте","scanGood":"Хороший контраст","scanBad":"Низкий контраст — может не считываться"},
hi:{title:"FreeQrly — मुफ़्त QR कोड जनरेटर | स्टैटिक बिना साइन-अप",metaDesc:"अपने ब्राउज़र में मुफ़्त QR कोड बनाएं — अपने लोगो के साथ भी। स्टैटिक बिना साइन-अप, बिना ट्रैकिंग, बिना एक्सपायरी। PNG व SVG एक्सपोर्ट।",navStudio:"स्टूडियो",navWhy:"सिद्धांत",navFaq:"सवाल",kicker:"मुफ़्त · स्टैटिक बिना साइन-अप · प्राइवेसी पहले",h1a:"",h1b:"कुछ भी",h1c:"बनाएं QR कोड।",lede:"स्टैटिक कोड बिना साइन-अप। आपके ब्राउज़र में बनते हैं, हमेशा आपके। डायनामिक कोड के लिए मुफ़्त साइन-अप चाहिए, ताकि प्रिंट के बाद भी बदल सकें।",hc1:"कंटेंट के प्रकार",hc2:"एक्सपोर्ट",hc3:"आपका डेटा",hc3v:"प्राइवेसी पहले",hc4:"क़ीमत",hc4v:"हमेशा मुफ़्त",sOver:"स्टूडियो",sTitle:"QR कोड बनाएं",appearance:"रूप-रंग",ink:"स्याही",paper:"काग़ज़",background:"पृष्ठभूमि",dots:"बिंदुओं की शैली",ecc:"एरर करेक्शन",dSquare:"चौकोर",dRound:"गोल",dSoft:"नर्म",dPebble:"कंकड़",eL:"कम",eM:"मध्यम",eQ:"उच्च",eH:"अधिकतम",eccHint:"लेवल जितना ऊंचा, लोगो और घिसाव से उतना सुरक्षित।",dotsSub:"QR बिंदु आकार",eccSub:"अधिक टिकाऊ",colors:"रंग",colorsSub:"चुनें या कस्टमाइज़ करें",transparentSub:"सफेद पृष्ठभूमि नहीं",size:"एक्सपोर्ट साइज़",logo:"अपना लोगो जोड़ें",logoSub:"ब्रांड या अपना",privnote:"स्टैटिक कोड पूरी तरह आपके ब्राउज़र में बनते हैं।",live:"लाइव प्रीव्यू — लिखते ही बदलेगा",bLabel:"हर लाइन में एक लिंक",bType:"प्रकार",bUpload:"CSV / Excel अपलोड करें",bTemplate:"टेम्पलेट डाउनलोड करें",bGo:"सभी बनाएं",bZip:"ZIP डाउनलोड करें",bEmpty:"पहले ऊपर कम से कम एक लिंक लिखें",featsK:"कोड से आगे",featsT:"QR के आसपास सब कुछ",featsS:"बनाना तो शुरुआत है। FreeQrly में ये सब भी है।",f1t:"बिल्ट-इन स्कैनर",f1d:"कैमरा लगाएं या इमेज अपलोड करें — कोड आपके ब्राउज़र में ही डिकोड होता है, कभी सर्वर पर अपलोड नहीं होता। ऑफलाइन भी चलता है।",f1l:"स्कैनर खोलें →",f2t:"17 तरह के कोड",f2d:"वेबसाइट, टेक्स्ट, WiFi, संपर्क कार्ड, ईमेल, SMS, कॉल, लोकेशन, कैलेंडर इवेंट, Bitcoin, Coupon, App Store, समीक्षाएं, ऑडियो, Google फ़ॉर्म, मेनू — साथ में बैच मोड से एक साथ कई। हर तरह का सही फॉर्मेट अपने आप — कोई syntax याद नहीं करना।",f2l:"सभी आज़माएं →",f3t:"बैच जनरेशन",f3d:"50 लिंक पेस्ट करें, एक क्लिक में 50 प्रिंट-रेडी कोड पाएं। एक-एक करके डाउनलोड करें या ZIP में लें।",f3l:"बैच मोड →",f4t:"कैलेंडर इवेंट कोड",f4d:"एक स्कैन में आपका इवेंट — टाइटल, समय, जगह — सीधे मेहमान के फोन कैलेंडर में। निमंत्रण के लिए बना है।",f4l:"इवेंट कोड बनाएं →",f5t:"लोगो और स्टाइल",f5d:"बीच में अपना लोगो लगाएं, स्कैन होता रहे इसलिए एरर करेक्शन अपने आप बढ़ जाता है। डॉट्स, रंग बदलें — या पारदर्शी बैकग्राउंड।",f5l:"लोगो वाले कोड →",f6t:"प्राइवेट हिस्ट्री",f6d:"हर डाउनलोड सिर्फ इसी डिवाइस पर याद रहता है — आपके 12 ताज़ा, एक क्लिक में वापस। कभी भी साफ़ करें।",casesK:"असल दुनिया में",casesT:"असली पलों के लिए बना",casesS:"अपना सीन चुनें — सेटअप पहले से तैयार है।",c1t:"बिज़नेस कार्ड",c1d:"एक स्कैन में आपके संपर्क — सीधे उनके फोन में।",c2t:"शादियां",c2d:"RSVP, फोटो शेयरिंग, कैलेंडर में जोड़ें। कागज़ी काम, बिना कागज़।",c3t:"रियल एस्टेट",c3d:"साइनबोर्ड पर लिस्टिंग। एक स्कैन में विज़िट बुक करें।",c4t:"इवेंट",c4d:"चेक-इन, टिकट वेरिफिकेशन, शेयर की गई एल्बम।",c5t:"WiFi शेयरिंग",c5d:"मेहमान एक स्कैन में ऑनलाइन। पासवर्ड बोलना बंद।",c6t:"Google रिव्यू",c6d:"खुश ग्राहकों को काउंटर पर ही पांच स्टार बनाएं।",p1n:"नं. 1",p1t:"आपका डेटा कहीं नहीं जाता",p1p:"हर स्टैटिक कोड आपके डिवाइस पर बनता है — न अपलोड, न ट्रैकिंग, न अकाउंट। पेज लोड करें, नेट बंद करें, सब चलता रहेगा।",p2n:"नं. 2",p2t:"टिकने के लिए बने",p2p:"स्टैटिक कोड अपना पता पैटर्न में ही रखता है। आज प्रिंट करें, दस साल बाद भी स्कैन होगा। न रिन्यूअल, न ग़ायब होने वाले प्लेटफ़ॉर्म।",p3n:"नं. 3",p3t:"मुफ़्त मतलब मुफ़्त",p3p:"न वॉटरमार्क, न बारीक शर्तें। स्टैटिक बिना साइन-अप। न Pro प्लान, न छिपे चार्ज — अच्छे टूल मुफ़्त ही होने चाहिए।",faqT:"जानना अच्छा रहेगा",q1:"क्या मुफ़्त QR कोड एक्सपायर होते हैं?",a1:"कभी नहीं। पता पैटर्न में ही कोड होता है, इसलिए जब तक पता चलेगा, कोड चलेगा। पेड डायनामिक कोड कंपनी के सर्वर से चलते हैं और पेमेंट रुकते ही बंद हो सकते हैं — स्टैटिक को चुनने की एक और वजह।",q2:"क्या मेरा WiFi पासवर्ड यहां सुरक्षित है?",a2:"स्टैटिक कोड के लिए, हां। आपका पासवर्ड आपके ब्राउज़र से बाहर नहीं जाता — कुछ भी कहीं नहीं भेजा जाता। ज़्यादा सावधानी? पेज लोड करें, नेट बंद करें, फिर लिखें।",q3:"स्टैटिक या डायनामिक?",a3:"अगर पता नहीं बदलेगा तो स्टैटिक: WiFi, विज़िटिंग कार्ड, फिक्स्ड लिंक। डायनामिक (बदले जा सकने वाले लिंक + स्कैन आंकड़े) कैंपेन के लिए हैं — अब लाइव हैं: मुफ़्त साइन-अप, प्रिंट के बाद भी बदलें, स्कैन आंकड़े देखें।",q4:"क्या व्यावसायिक इस्तेमाल कर सकते हैं?",a4:"बिल्कुल। यहां बना हर कोड आपका है — पैकेजिंग, मेन्यू, कार्ड, बिना क्रेडिट के।",q5:"क्या FreeQrly सच में मुफ़्त है?",a5:"हां — इस पेज की हर चीज़ मुफ़्त है, बिना वॉटरमार्क के। स्टैटिक बिना अकाउंट। हम सब्सक्रिप्शन नहीं बेचते; यह एक टूल है, जाल नहीं।",q6:"क्या अकाउंट चाहिए?",a6:"स्टैटिक के लिए नहीं। साइन-अप करने को कुछ नहीं है — पेज खोलें और कोड बनाएं। डायनामिक के लिए मुफ़्त साइन-अप चाहिए, ताकि प्रिंट के बाद भी बदल सकें।",q7:"क्या QR कोड में अपना लोगो लगा सकते हैं?",a7:"हां — चौकोर लोगो अपलोड करें, हम उसे बीच में लगाएंगे और एरर करेक्शन अपने आप बढ़ा देंगे ताकि स्कैन होता रहे। प्रिंट के लिए Q या H चुनें।",fin:"स्टैटिक कोड, आपके ब्राउज़र में बने।",dl:"डाउनलोड",navScan:"स्कैनर",history:"हाल के",histClear:"साफ़ करें",transparent:"पारदर्शी पृष्ठभूमि",frame:"फ़्रेम",frameSub:"कोड के चारों ओर बॉर्डर",frameTextLabel:"फ़्रेम टेक्स्ट",frameNone:"कोई नहीं",frameRounded:"गोल",frameCta:"पाठ के साथ",frameTextPh:"स्कैन करें",scanGood:"अच्छा कंट्रास्ट",scanBad:"कम कंट्रास्ट — स्कैन नहीं हो सकता",types:{"url": ["वेबसाइट", "लिंक, पेज, वीडियो"], "text": ["टेक्स्ट", "कोई भी शब्द"], "wifi": ["WiFi", "तुरंत जुड़ें"], "vcard": ["संपर्क", "vCard"], "email": ["ईमेल", "पहले से भरा"], "sms": ["SMS", "पहले से भरा टेक्स्ट"], "phone": ["कॉल", "डायल करें"], "geo": ["जगह", "मैप पिन"],"event":["इवेंट","कैलेंडर में जोड़ें"],"bitcoin":["Bitcoin","crypto payment"],"coupon":["Coupon","promo code"],"appstore":["App Store","iOS + Android"],"review":["समीक्षाएं","5-स्टार रिव्यू पाएं"],"mp3":["ऑडियो","MP3 और साउंड"],"google-form":["Google फ़ॉर्म","जवाब इकट्ठा करें"],"menu":["मेनू","रेस्तरां मेनू"],"batch":["बैच", "एक साथ कई"]},fields:{"url": [["url", "गंतव्य", "https://example.com"]], "text": [["text", "संदेश", "textarea", "नमस्ते दुनिया!"]], "wifi": [["ssid", "नेटवर्क का नाम", "MyWiFi"], ["pass", "पासवर्ड", "", "WiFi पासवर्ड"], ["enc", "सुरक्षा", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "पूरा नाम", "राहुल शर्मा"], ["phone", "फ़ोन", "+91 98765 43210"], ["email", "ईमेल", "rahul@example.com"],["vcorg","Company","","Acme Inc"],["vctitle","Job title","","Designer"],["vcurl","Website","https://example.com"],["vcadr","Address","","123 Main St"],["vcnote","Note","",""]], "email": [["to", "प्राप्तकर्ता", "hello@example.com"], ["subject", "विषय", "नमस्ते"], ["body", "मुख्य भाग", "textarea", "ईमेल सामग्री…"]], "sms": [["phone", "फ़ोन", "+91 98765 43210"], ["body", "संदेश", "", "अपना संदेश लिखें…"]], "phone": [["phone", "फ़ोन", "+91 98765 43210"]], "geo": [["lat", "अक्षांश", "28.6139"], ["lng", "देशांतर", "77.2090"]],"event":[["etitle","शीर्षक","","जैसे: जन्मदिन पार्टी"],["estart","प्रारंभ","datetime-local"],["eend","समाप्ति","datetime-local"],["eloc","स्थान","","जैसे: सेंट्रल पार्क"],["edesc","विवरण","textarea","इवेंट विवरण…"]],"bitcoin":[["btcaddr","Wallet address","bc1q..."],["btcamt","Amount (BTC)","0.001"],["btclabel","Label","","e.g. Coffee"],["btcmsg","Message","","e.g. Thanks"]],"coupon":[["cpcode","Coupon code","SAVE20"],["cpdesc","Description","","e.g. 20% off"]],"appstore":[["appios","App Store link","https://apps.apple.com/app/..."],["appand","Google Play link","https://play.google.com/store/apps/..."]],"review":[["rvlink","समीक्षा पेज लिंक","https://g.page/your-business/review"]],"mp3":[["mp3link","ऑडियो फ़ाइल लिंक","https://example.com/song.mp3"]],"google-form":[["gflink","फ़ॉर्म लिंक","https://forms.gle/abc123XYZ"]],"menu":[["mnlink","मेनू लिंक","https://example.com/menu"]]}, "modeStatic":"स्थिर", "modeDynamic":"गतिशील", "modeHint":"स्थिर कोड कभी समाप्त नहीं होते। गतिशील कोड छपने के बाद भी बदले जा सकते हैं और स्कैन गिने जा सकते हैं।", "dynDest":"गंतव्य URL", "dynCreate":"गतिशील QR जनरेट करें", "dynShort":"आपका गतिशील QR लिंक:", "copy":"कॉपी करें", "dynIntro":"अपना QR डिज़ाइन करें — प्रकार चुनें, सामग्री भरें, स्टाइल करें। फिर गतिशील कोड बनाएं: छपा QR वही रहेगा, लेकिन आप इसकी सामग्री कभी भी बदल सकते हैं।", "dynHint":"अपनी सामग्री भरें, फिर जनरेट दबाएं।", "dynReady":"आपका गतिशील QR तैयार है। इसे प्रिंट करें — सामग्री कभी भी बदली जा सकती है।", "dynBlurHint":"अपनी सामग्री भरें, फिर जनरेट दबाएं", "modeTip":"स्टैटिक: सामग्री QR के अंदर — बिना खाते, हमेशा वैध। डायनामिक: स्कैन शॉर्ट लिंक से — प्रिंट के बाद सामग्री बदलें + आंकड़े देखें। मुफ्त खाता आवश्यक।","signin":"साइन इन","acctDashboard":"Dashboard","acctExport":"मेरा डेटा निर्यात करें","acctDelete":"खाता हटाएं","acctLogout":"लॉग आउट","acctDeleteConfirm":"अपना खाता हटाएं? इसे पूर्ववत नहीं किया जा सकता।","acctDeleteFailed":"हटाया नहीं जा सका। पुनः प्रयास करें।","acctNetErr":"नेटवर्क त्रुटि। पुनः प्रयास करें।","acctSignedInWith":"{method} से लॉग इन","moreFormats":"और प्रारूप","footGenerators":"जनरेटर","footMore":"और","ariaCustomInk":"कस्टम स्याही रंग","ariaCustomBg":"कस्टम पृष्ठभूमि रंग","ariaUploadLogo":"लोगो अपलोड करें","ariaLanguage":"भाषा","dynDashLink":"डैशबोर्ड में देखें →","dynSigninHint":"डायनामिक कोड बनाने के लिए साइन इन करें"},
ar:{title:"FreeQrly — مولّد QR مجاني | الثابتة بدون تسجيل",metaDesc:"أنشئ رموز QR مجانية في متصفحك — حتى مع شعارك. الثابتة بدون تسجيل، بدون تتبع، بدون انتهاء. تصدير PNG وSVG.",navStudio:"الاستوديو",navWhy:"المبادئ",navFaq:"أسئلة",kicker:"مجاني · الثابتة بدون تسجيل · خصوصية أولاً",h1a:"حوّل",h1b:"أي شيء",h1c:"إلى رمز QR.",lede:"الرموز الثابتة بدون تسجيل. تُصنع في متصفحك، لك للأبد. الديناميكية تحتاج حساباً مجانياً، لتعديلها بعد الطباعة.",hc1:"أنواع المحتوى",hc2:"تصدير",hc3:"بياناتك",hc3v:"خصوصية أولاً",hc4:"السعر",hc4v:"مجاني للأبد",sOver:"الاستوديو",sTitle:"أنشئ رمز QR",appearance:"المظهر",ink:"الحبر",paper:"الورق",background:"الخلفية",dots:"شكل النقاط",ecc:"تصحيح الأخطاء",dSquare:"مربع",dRound:"دائري",dSoft:"ناعم",dPebble:"حصاة",eL:"منخفض",eM:"متوسط",eQ:"مرتفع",eH:"أقصى",eccHint:"كلما ارتفع المستوى زادت مقاومة الشعارات والتآكل.",dotsSub:"شكل النقاط",eccSub:"الأعلى أكثر متانة",colors:"الألوان",colorsSub:"اختر أو خصص",transparentSub:"بدون خلفية بيضاء",size:"حجم التصدير",logo:"أضف شعارك",logoSub:"علامة أو خاص",privnote:"الرموز الثابتة تُنشأ بالكامل في متصفحك.",live:"معاينة حية — تتغير أثناء الكتابة",bLabel:"رابط واحد في كل سطر",bType:"Type",bUpload:"Upload CSV / Excel",bTemplate:"Download template",bGo:"إنشاء الكل",bZip:"تنزيل ZIP",bEmpty:"أدخل رابطًا واحدًا على الأقل أعلاه أولًا",featsK:"أبعد من الرمز",featsT:"كل ما يحيط بالـ QR",featsS:"التوليد مجرد البداية. هذا أيضًا يعيش داخل FreeQrly.",f1t:"ماسح مدمج",f1d:"وجّه الكاميرا أو ارفع صورة — تُفكّ الرموز في متصفحك ولا تُرفع إلى أي خادم أبدًا. يعمل دون اتصال أيضًا.",f1l:"افتح الماسح →",f2t:"17 نوع من الرموز",f2d:"موقع، نص، WiFi، بطاقات اتصال، بريد، SMS، مكالمات، مواقع، أحداث التقويم، بيتكوين، قسيمة، متجر التطبيقات، التقييمات، الصوت، نماذج Google، القوائم — بالإضافة إلى الوضع الجماعي لإنشاء عدة رموز دفعة واحدة. كل نوع يبني التنسيق الصحيح — لا حاجة لحفظ أي صيغة.",f2l:"جرّبها جميعًا →",f3t:"توليد جماعي",f3d:"الصق حتى 50 رابطًا واحصل على 50 رمزًا جاهزًا للطباعة بنقرة واحدة. نزّلها واحدًا واحدًا أو كلها كملف ZIP.",f3l:"الوضع الجماعي →",f4t:"رموز أحداث التقويم",f4d:"مسحة واحدة تُدخل حدثك — العنوان والوقت والمكان — إلى تقويم هاتف الضيف مباشرة. صُنع للدعوات.",f4l:"أنشئ رمز حدث →",f5t:"الشعار والتنسيق",f5d:"ضع شعارك في المنتصف ويرتفع تصحيح الأخطاء تلقائيًا ليبقى قابلًا للمسح. غيّر النقاط والحبر والورق — أو اجعل الخلفية شفافة.",f5l:"رموز بشعار →",f6t:"سجل خاص",f6d:"كل تنزيل يُحفظ على هذا الجهاز فقط — أحدث اثني عشر، بنقرة واحدة للاسترجاع. امسحه متى شئت.",casesK:"في الواقع",casesT:"صُنع للحظات الحقيقية",casesS:"اختر سيناريوك — الإعداد جاهز مسبقًا.",c1t:"بطاقات الأعمال",c1d:"بيانات اتصالك بمسحة واحدة — إلى هاتفهم مباشرة.",c2t:"حفلات الزفاف",c2d:"تأكيد الحضور ومشاركة الصور والإضافة للتقويم. المعاملات الورقية، بلا ورق.",c3t:"العقارات",c3d:"القوائم على اللافتة. احجز معاينة بمسحة واحدة.",c4t:"الفعاليات",c4d:"تسجيل الدخول والتحقق من التذاكر والألبومات المشتركة.",c5t:"مشاركة WiFi",c5d:"الضيوف متصلون بمسحة واحدة. لا تُملي كلمة المرور مجددًا.",c6t:"تقييمات Google",c6d:"حوّل العملاء السعداء إلى خمس نجوم، عند الكاونتر مباشرة.",p1n:"رقم ١",p1t:"بياناتك لا تغادر مكانها",p1p:"كل رمز ثابت يُرسم على جهازك — لا رفع، لا تتبع، لا حسابات. حمّل الصفحة، افصل السلك، وسيستمر كل شيء.",p2n:"رقم ٢",p2t:"مصنوعة لتدوم",p2p:"الرمز الثابت يحمل وجهته داخل النقش. اطبعه اليوم وسيُمسح بعد عشر سنوات. لا تجديد ولا منصات تختفي.",p3n:"رقم ٣",p3t:"مجاني يعني مجاني",p3p:"لا علامة مائية، لا شروط صغيرة. الثابتة بدون تسجيل. لا خطة Pro ولا رسوم خفية — الأدوات الجيدة يجب أن تكون مجانية.",faqT:"من الجيد معرفته",q1:"هل تنتهي رموز QR المجانية؟",a1:"أبداً. الوجهة مشفّرة في النقش نفسه، فيعمل الرمز ما دامت الوجهة تعمل. الرموز الديناميكية المدفوعة تمر عبر خوادم المزوّد وقد تموت عند إيقاف الدفع — سبب آخر لتفضيل الثابت.",q2:"هل كلمة مرور WiFi آمنة هنا؟",a2:"للرمز الثابت، نعم. كلمة المرور لا تغادر متصفحك أبداً — لا يُرسل شيء إلى أي مكان. حذر أكثر؟ حمّل الصفحة، افصل الاتصال، ثم اكتب.",q3:"ثابت أم ديناميكي؟",a3:"إذا كانت الوجهة لن تتغير فاختر الثابت: WiFi وبطاقات الأعمال والروابط الثابتة. الديناميكية (روابط قابلة للتعديل + إحصاءات المسح) للحملات — أصبحت متاحة الآن: حساب مجاني، تعديل بعد الطباعة، وعرض إحصاءات المسح.",q4:"هل يمكن استخدامها تجارياً؟",a4:"بالتأكيد. كل ما تنشئه هنا لك — التغليف والقوائم والبطاقات، دون نسب.",q5:"هل FreeQrly مجاني حقاً؟",a5:"نعم — كل شيء في هذه الصفحة مجاني، بلا علامة مائية. الثابتة بلا حساب. لا نبيع اشتراكات؛ هذه أداة وليست فخاً.",q6:"هل أحتاج حساباً؟",a6:"للثابتة، لا. لا يوجد ما تسجّل فيه — افتح الصفحة وأنشئ رمزك. الديناميكية تحتاج حساباً مجانياً، لتعديلها بعد الطباعة.",q7:"هل يمكن إضافة شعاري إلى رمز QR؟",a7:"نعم — ارفع شعاراً مربعاً وسنضعه في المنتصف مع رفع تصحيح الأخطاء تلقائياً ليبقى قابلاً للمسح. للطباعة اختر Q أو H.",fin:"رموز ثابتة، صُنعت في متصفحك.",dl:"تنزيل",navScan:"ماسح",history:"الأخيرة",histClear:"مسح",transparent:"خلفية شفافة",types:{"url": ["موقع", "رابط، صفحة، فيديو"], "text": ["نص", "أي كلمات"], "wifi": ["WiFi", "اتصال فوري"], "vcard": ["جهة اتصال", "vCard"], "email": ["بريد", "مُعبأ مسبقاً"], "sms": ["SMS", "نص مُعبأ"], "phone": ["اتصال", "اضغط للاتصال"], "geo": ["مكان", "دبوس خريطة"],"event":["فعالية","إضافة إلى التقويم"],"bitcoin":["بيتكوين","دفع مشفر"],"coupon":["قسيمة","رمز ترويجي"],"appstore":["متجر التطبيقات","iOS + Android"],"review":["التقييمات","احصل على تقييم 5 نجوم"],"mp3":["الصوت","MP3 وصوتيات"],"google-form":["نموذج Google","اجمع الردود"],"menu":["القائمة","قائمة المطعم"],"batch":["دفعة", "عدة مرات"]},fields:{"url": [["url", "الوجهة", "https://example.com"]], "text": [["text", "الرسالة", "textarea", "مرحباً بالعالم!"]], "wifi": [["ssid", "اسم الشبكة", "MyWiFi"], ["pass", "كلمة المرور", "", "كلمة مرور WiFi"], ["enc", "الأمان", "select:WPA,WPA2,WEP,nopass"]], "vcard": [["name", "الاسم الكامل", "أحمد محمد"], ["phone", "الهاتف", "+966 5 0000 0000"], ["email", "البريد", "ahmed@example.com"],["vcorg","الشركة","","أكمي"],["vctitle","المسمى الوظيفي","","مصمم"],["vcurl","الموقع","https://example.com"],["vcadr","العنوان","","123 الشارع الرئيسي"],["vcnote","ملاحظة","",""]], "email": [["to", "إلى", "hello@example.com"], ["subject", "الموضوع", "مرحباً"], ["body", "المتن", "textarea", "متن البريد…"]], "sms": [["phone", "الهاتف", "+966 5 0000 0000"], ["body", "الرسالة", "", "اكتب رسالتك…"]], "phone": [["phone", "الهاتف", "+966 5 0000 0000"]], "geo": [["lat", "خط العرض", "24.7136"], ["lng", "خط الطول", "46.6753"]],"event":[["etitle","العنوان","","مثال: حفلة عيد ميلاد"],["estart","البداية","datetime-local"],["eend","النهاية","datetime-local"],["eloc","المكان","","مثال: الحديقة المركزية"],["edesc","التفاصيل","textarea","تفاصيل الفعالية…"]],"bitcoin":[["btcaddr","عنوان المحفظة","bc1q..."],["btcamt","المبلغ (BTC)","0.001"],["btclabel","تسمية","","مثال: قهوة"],["btcmsg","رسالة","","مثال: شكراً"]],"coupon":[["cpcode","رمز القسيمة","SAVE20"],["cpdesc","الوصف","","مثال: خصم 20%"]],"appstore":[["appios","رابط متجر التطبيقات","https://apps.apple.com/app/..."],["appand","رابط Google Play","https://play.google.com/store/apps/..."]],"review":[["rvlink","رابط صفحة التقييمات","https://g.page/your-business/review"]],"mp3":[["mp3link","رابط الملف الصوتي","https://example.com/song.mp3"]],"google-form":[["gflink","رابط النموذج","https://forms.gle/abc123XYZ"]],"menu":[["mnlink","رابط القائمة","https://example.com/menu"]]}, "modeStatic":"ثابت", "modeDynamic":"ديناميكي", "modeHint":"الرموز الثابتة لا تنتهي أبدًا. الرموز الديناميكية يمكن تعديلها بعد الطباعة وتتبع عمليات المسح.", "dynDest":"رابط الوجهة", "dynCreate":"إنشاء رمز ديناميكي", "dynShort":"رابط رمزك الديناميكي:", "copy":"نسخ", "dynIntro":"صمّم رمزك — اختر نوعًا، املأ المحتوى، ونسّقه. ثم أنشئ رمزًا ديناميكيًا: يبقى الرمز المطبوع كما هو، لكن يمكنك تغيير محتواه في أي وقت.", "dynHint":"املأ المحتوى ثم اضغط إنشاء.", "dynReady":"رمزك الديناميكي جاهز. اطبعه — يمكن تغيير المحتوى في أي وقت.", "dynBlurHint":"املأ المحتوى ثم اضغط إنشاء", "modeTip":"ثابت: المحتوى داخل الرمز — بدون حساب، صالح للأبد. ديناميكي: المسح يمر برابط قصير — عدّل المحتوى بعد الطباعة وشاهد الإحصاءات. يحتاج حسابًا مجانيًا.","signin":"تسجيل الدخول","acctDashboard":"Dashboard","acctExport":"تصدير بياناتي","acctDelete":"حذف الحساب","acctLogout":"تسجيل الخروج","acctDeleteConfirm":"حذف حسابك؟ لا يمكن التراجع عن هذا.","acctDeleteFailed":"تعذر الحذف. حاول مجددًا.","acctNetErr":"خطأ في الشبكة. حاول مجددًا.","acctSignedInWith":"تم تسجيل الدخول عبر {method}","moreFormats":"تنسيقات أخرى","footGenerators":"المولدات","footMore":"المزيد","ariaCustomInk":"لون حبر مخصص","ariaCustomBg":"لون خلفية مخصص","ariaUploadLogo":"تحميل الشعار","ariaLanguage":"اللغة","dynDashLink":"عرض في لوحة التحكم →","dynSigninHint":"سجّل الدخول لإنشاء رموز ديناميكية","frame":"إطار","frameSub":"حدود حول الرمز","frameTextLabel":"نص الإطار","frameNone":"بدون","frameRounded":"مستدير","frameCta":"مع نص","frameTextPh":"امسح","scanGood":"تباين جيد","scanBad":"تباين منخفض — قد لا يُقرأ"}
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
let dynamicMode = false;
let dynamicShortUrl = '';
let dynamicGenerated = false;
const ORDER = ["url","text","wifi","vcard","email","sms","phone","geo","event","bitcoin","coupon","appstore","review","mp3","google-form","menu","batch"];
/* landing pages preselect a type via body[data-type]; ?type= also works */
const _preType = document.body.getAttribute("data-type") || new URLSearchParams(location.search).get("type");
if (_preType && ORDER.includes(_preType)) cur = _preType;

const v = id => { const el = $("f_"+id); if(!el) return ""; return el.value.trim() || (el.placeholder||""); };
function content(){
  switch(cur){
    case "url": return v("url")||"https://example.com";
    case "text": return v("text")||" ";
    case "wifi": return `WIFI:T:${v("enc")};S:${v("ssid")};P:${v("pass")};;`;
    case "vcard": {
      let s = `BEGIN:VCARD\nVERSION:3.0\nN:${v("name")}\n`;
      if(v("vcorg")) s += `ORG:${v("vcorg")}\n`;
      if(v("vctitle")) s += `TITLE:${v("vctitle")}\n`;
      s += `TEL:${v("phone")}\nEMAIL:${v("email")}\n`;
      if(v("vcurl")) s += `URL:${v("vcurl")}\n`;
      if(v("vcadr")) s += `ADR:;;${v("vcadr")}\n`;
      if(v("vcnote")) s += `NOTE:${v("vcnote")}\n`;
      return s + "END:VCARD";
    }
    case "email": return `mailto:${v("to")}?subject=${encodeURIComponent(v("subject"))}&body=${encodeURIComponent(v("body"))}`;
    case "sms": return `sms:${v("phone")}?body=${encodeURIComponent(v("body"))}`;
    case "phone": return `tel:${v("phone")}`;
    case "geo": return `geo:${v("lat")},${v("lng")}`;
    case "bitcoin": {
      const addr = v("btcaddr");
      const q = [];
      if(v("btcamt")) q.push("amount="+encodeURIComponent(v("btcamt")));
      if(v("btclabel")) q.push("label="+encodeURIComponent(v("btclabel")));
      if(v("btcmsg")) q.push("message="+encodeURIComponent(v("btcmsg")));
      return "bitcoin:" + addr + (q.length ? "?" + q.join("&") : "");
    }
    case "coupon": {
      const code = v("cpcode"), desc = v("cpdesc");
      return desc ? `${desc}\nCode: ${code}` : `Code: ${code}`;
    }
    case "appstore": {
      const ios = v("appios"), and = v("appand");
      // Return a simple landing format - iOS first, fallback Android
      return ios || and || "";
    }
    case "review": return v("rvlink")||"";
    case "mp3": return v("mp3link")||"";
    case "google-form": return v("gflink")||"";
    case "menu": return v("mnlink")||"";
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
async function draw(){
  if(cur==="batch") return;
  scanScore();
  const qr = new QRCodeStyling(styleOpts(236));
  try{
    // Use SVG (synchronous data) instead of canvas append (async, may be blank)
    const svgBlob = await qr.getRawData("svg");
    let svgText = await svgBlob.text();
    svgText = frameWrap(svgText, 236);
    const box = $("qrbox");
    if(box) box.innerHTML = `<img src="data:image/svg+xml,${encodeURIComponent(svgText)}" alt="QR code preview">`;
  }catch(e){
    // Fallback to canvas append
    $("qrbox").innerHTML=""; qr.append($("qrbox"));
  }
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
const TYPE_EMOJI = {url:"🔗",text:"📝",wifi:"📶",vcard:"👤",email:"✉️",sms:"💬",phone:"📞",geo:"📍",event:"📅",bitcoin:"₿",coupon:"🎟️",appstore:"📱",review:"⭐",mp3:"🎵","google-form":"📋",menu:"🍽️",batch:"📚"};
function renderTabs(){
  // Batch can't be dynamic (one code at a time) — hide the toggle, force static
  const seg = $("segMode");
  if(seg){
    seg.style.display = (cur === "batch") ? "none" : "";
    if(cur === "batch" && dynamicMode){
      dynamicMode = false; dynamicShortUrl = ''; dynamicGenerated = false;
      seg.querySelectorAll("button[data-mode]").forEach(b => b.classList.toggle("on", b.dataset.mode === "static"));
      if(window.refreshDynamicUI) window.refreshDynamicUI();
    }
  }
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
  if(cur === "batch"){ batchTypeInit(); ensureXLSX(); ensureJSZip(); }
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
      const isFg = btn.dataset.kind === "fg";
      const hidden = $(isFg ? "fg" : "bgc");
      const dotsId = isFg ? "fgDots" : "bgDots";
      window.openColorPicker(btn, hidden?hidden.value:"#22303F", (hex)=>{
        if(hidden){ hidden.value=hex; hidden.dispatchEvent(new Event("input",{bubbles:true})); }
        // Add or update a custom color dot in the options
        const box=document.getElementById(dotsId);
        let custom = box ? box.querySelector(".cdot.custom") : null;
        if(box && !custom){
          custom=document.createElement("button");
          custom.type="button"; custom.className="cdot custom";
          custom.setAttribute("aria-label","Custom color");
          box.insertBefore(custom, box.querySelector(".cpick"));
          custom.addEventListener("click",()=>{
            if(hidden){ hidden.value=custom.dataset.v; hidden.dispatchEvent(new Event("input",{bubbles:true})); }
            dotsInit._mark(dotsId, custom.dataset.v);
            const transp=$("transp"); if(transp && !isFg) transp.checked=false;
            draw();
          });
        }
        if(custom){ custom.dataset.v=hex; custom.style.background=hex; custom.title=hex; }
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
  document.querySelectorAll("[data-i18n-ph]").forEach(el=>{
    const k = el.getAttribute("data-i18n-ph");
    if(I18N[lang][k] !== undefined) el.placeholder = I18N[lang][k];
  });
  document.querySelectorAll("[data-i18n-aria]").forEach(el=>{
    const k = el.getAttribute("data-i18n-aria");
    if(I18N[lang][k] !== undefined) el.setAttribute("aria-label", I18N[lang][k]);
  });
  document.querySelectorAll(".cdot.custom").forEach(el=>{
    const grp = el.closest(".cgroup");
    const cp = grp ? grp.querySelector(".cpick") : null;
    const k = (cp && cp.dataset.kind === "bg") ? "ariaCustomBg" : "ariaCustomInk";
    if(I18N[lang][k] !== undefined) el.setAttribute("aria-label", I18N[lang][k]);
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
let batchType = "url";

// Convert one line to QR payload for the selected batch type.
// Multi-field types use | as separator.
function batchPayload(type, line){
  const parts = line.split("|").map(s=>s.trim());
  switch(type){
    case "url": case "text": return line;
    case "email": {
      const [to, subj, body] = parts;
      let r = "mailto:" + (to||"");
      const q = [];
      if(subj) q.push("subject="+encodeURIComponent(subj));
      if(body) q.push("body="+encodeURIComponent(body));
      if(q.length) r += "?" + q.join("&");
      return r;
    }
    case "sms": {
      const [ph, body] = parts;
      return "sms:" + (ph||"") + (body ? "?body="+encodeURIComponent(body) : "");
    }
    case "phone": return "tel:" + line;
    case "geo": return "geo:" + line;
    case "bitcoin": {
      const [addr, amt, label, msg] = parts;
      const q = [];
      if(amt) q.push("amount="+encodeURIComponent(amt));
      if(label) q.push("label="+encodeURIComponent(label));
      if(msg) q.push("message="+encodeURIComponent(msg));
      return "bitcoin:" + (addr||"") + (q.length ? "?" + q.join("&") : "");
    }
    case "coupon": {
      const [code, desc] = parts;
      return desc ? `${desc}\nCode: ${code}` : `Code: ${code||""}`;
    }
    case "appstore": {
      const [ios, and] = parts;
      return ios || and || "";
    }
    case "wifi": {
      const [ssid, pass, enc] = parts;
      const t = (enc||"WPA").toUpperCase();
      return `WIFI:T:${t};S:${ssid||""};P:${pass||""};;`;
    }
    case "vcard": {
      const [name, ph, em] = parts;
      return `BEGIN:VCARD\nVERSION:3.0\nN:${name||""}\nTEL:${ph||""}\nEMAIL:${em||""}\nEND:VCARD`;
    }
    case "event": {
      const [title, start, end, loc, desc] = parts;
      const f = s => (s||"").replace(/-/g,"").replace(/:/g,"").replace(/T/g,"T");
      return `BEGIN:VEVENT\nSUMMARY:${title||""}\nDTSTART:${f(start)}\nDTEND:${f(end)}\nLOCATION:${loc||""}\nDESCRIPTION:${desc||""}\nEND:VEVENT`;
    }
    default: return line;
  }
}

// Format hints per type (shown under the textarea)

// Lazy-load heavy libs only when batch features are used
const _libCache = {};
function loadLib(src){
  if(_libCache[src]) return _libCache[src];
  _libCache[src] = new Promise((res, rej)=>{
    const s = document.createElement("script");
    s.src = src; s.onload = res; s.onerror = rej;
    document.head.appendChild(s);
  });
  return _libCache[src];
}
const ensureXLSX = ()=>loadLib("/assets/lib/xlsx.min.js");
const ensureJSZip = ()=>loadLib("/assets/lib/jszip.min.js");

const BATCH_FMT = {
  url: "https://example.com/a",
  text: "Any text, one per line",
  email: "to@example.com | Subject | Body",
  sms: "+1234567890 | Message",
  phone: "+1234567890",
  geo: "37.7749,-122.4194",
  wifi: "MyWiFi | password | WPA",
  vcard: "Jane Doe | +1234567890 | jane@example.com",
  event: "Party | 2026-10-20T19:00 | 2026-10-20T22:00 | Home | Bring snacks",
  review: "https://g.page/your-business/review",
  mp3: "https://example.com/song.mp3",
  "google-form": "https://forms.gle/abc123XYZ",
  menu: "https://example.com/menu",
};

function batchTypeInit(){
  const sel = $("batchType"); if(!sel) return;
  if(sel.options.length) return;
  const types = ["url","text","email","sms","phone","geo","wifi","vcard","event","bitcoin","coupon","appstore","review","mp3","google-form","menu"];
  types.forEach(t=>{
    const o = document.createElement("option");
    o.value = t;
    o.textContent = (I18N[lang].types[t] && I18N[lang].types[t][0]) || t;
    sel.appendChild(o);
  });
  sel.value = "url";
  const updateFmt = ()=>{
    batchType = sel.value;
    const fmt = $("batchFmt");
    if(fmt) fmt.textContent = BATCH_FMT[batchType] || "";
    const ta = $("batchInput");
    if(ta) ta.placeholder = BATCH_FMT[batchType] || "";
  };
  sel.addEventListener("change", updateFmt);
  updateFmt();
}
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
  batchType = ($("batchType") && $("batchType").value) || "url";
  batchItems = $("batchInput").value.split("\n").map(s=>s.trim()).filter(Boolean).slice(0,50)
    .map(line=>batchPayload(batchType, line));
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
/* Batch: CSV / Excel upload - one sheet per type for .xlsx */
const SHEET_TO_TYPE = {
  "url": "url", "website": "url", "link": "url", "links": "url",
  "text": "text",
  "email": "email", "emails": "email",
  "sms": "sms",
  "phone": "phone", "call": "phone", "phones": "phone",
  "geo": "geo", "place": "geo", "location": "geo",
  "wifi": "wifi",
  "vcard": "vcard", "contact": "vcard", "contacts": "vcard",
  "event": "event", "events": "event",
};

function batchParseCSV(text){
  // Simple CSV parser (handles quoted fields)
  const rows = [];
  let row = [], field = "", inQ = false;
  for(let i=0; i<text.length; i++){
    const c = text[i];
    if(inQ){
      if(c === '"'){
        if(text[i+1] === '"'){ field += '"'; i++; }
        else inQ = false;
      } else field += c;
    } else {
      if(c === '"') inQ = true;
      else if(c === ","){ row.push(field); field = ""; }
      else if(c === "\n" || c === "\r"){
        if(c === "\r" && text[i+1] === "\n") i++;
        row.push(field); field = "";
        if(row.length > 1 || row[0]) rows.push(row);
        row = [];
      } else field += c;
    }
  }
  if(field || row.length){ row.push(field); rows.push(row); }
  return rows;
}

function batchRowsToPayloads(type, rows){
  // Skip header row if it looks like one
  const first = rows[0] || [];
  const isHeader = first.some(c => /^(name|title|url|text|ssid|phone|email|lat|link)/i.test(c||""));
  const data = isHeader ? rows.slice(1) : rows;
  return data.filter(r => r.some(c => (c||"").trim()))
    .map(r => batchPayload(type, r.map(c=>(c||"").trim()).join(" | ")))
    .slice(0, 50);
}

function batchHandleFile(file){
  const isXlsx = /\.xlsx?$/i.test(file.name);
  const reader = new FileReader();
  reader.onload = async (e)=>{
    try{
      if(isXlsx){ await ensureXLSX(); }
      if(isXlsx && typeof XLSX !== "undefined"){
        const wb = XLSX.read(e.target.result, {type: "array"});
        let all = [];
        wb.SheetNames.forEach(sheetName=>{
          const type = SHEET_TO_TYPE[sheetName.toLowerCase().trim()] || "url";
          const ws = wb.Sheets[sheetName];
          const rows = XLSX.utils.sheet_to_json(ws, {header: 1, defval: ""});
          const payloads = batchRowsToPayloads(type, rows);
          all = all.concat(payloads);
        });
        batchItems = all.slice(0, 50);
        const hint = $("batchHint");
        if(batchItems.length === 0){
          hint.textContent = "No rows found in file.";
          hint.hidden = false;
        } else {
          hint.textContent = `${batchItems.length} rows loaded from ${file.name}`;
          hint.hidden = false;
          track("batch_generate",{count:batchItems.length});
          renderBatch();
        }
      } else {
        // CSV: single type (current selector)
        const rows = batchParseCSV(e.target.result);
        batchType = ($("batchType") && $("batchType").value) || "url";
        batchItems = batchRowsToPayloads(batchType, rows);
        const hint = $("batchHint");
        if(batchItems.length === 0){
          hint.textContent = "No rows found in file.";
          hint.hidden = false;
        } else {
          hint.textContent = `${batchItems.length} rows loaded from ${file.name}`;
          hint.hidden = false;
          track("batch_generate",{count:batchItems.length});
          renderBatch();
        }
      }
    }catch(err){
      const hint = $("batchHint");
      hint.textContent = "Could not read file: " + err.message;
      hint.hidden = false;
    }
  };
  if(isXlsx) reader.readAsArrayBuffer(file);
  else reader.readAsText(file);
}

// Wire up file input
const _bf = $("batchFile");
if(_bf){
  _bf.addEventListener("change", ()=>{
    const f = _bf.files[0];
    if(f) batchHandleFile(f);
    _bf.value = "";
  });
}

// Template download
const _bt = $("batchTemplate");
if(_bt){
  _bt.addEventListener("click", async ()=>{
    // Multi-sheet Excel: one sheet per type, each with headers + example rows
    const sheets = {
      url: [["URL"], ["https://example.com/a"], ["https://example.com/b"]],
      text: [["Text"], ["Hello world"], ["Second line"]],
      email: [["To","Subject","Body"], ["a@b.com","Hi","Hello there"], ["b@c.com","Meeting","See you at 3pm"]],
      sms: [["Phone","Message"], ["+1234567890","Hi there"], ["+0987654321","Reminder"]],
      phone: [["Phone"], ["+1234567890"], ["+0987654321"]],
      geo: [["Latitude","Longitude"], ["37.7749","-122.4194"], ["40.7128","-74.0060"]],
      wifi: [["SSID","Password","Encryption"], ["MyWiFi","secret123","WPA"], ["OfficeNet","pass456","WPA2"]],
      vcard: [["Name","Phone","Email","Company","Title","Website","Address","Note"], ["Jane Doe","+1234567890","jane@example.com","Acme Inc","Designer","https://example.com","123 Main St","Friend"], ["John Smith","+0987654321","john@example.com","Beta LLC","Manager","https://beta.com","456 Oak Ave","Colleague"]],
      event: [["Title","Start","End","Location","Description"], ["Party","2026-10-20T19:00","2026-10-20T22:00","Home","Bring snacks"], ["Meeting","2026-10-21T10:00","2026-10-21T11:00","Office","Weekly sync"]],
      bitcoin: [["Address","Amount","Label","Message"], ["bc1q...","0.001","Coffee","Thanks"], ["bc1p...","0.005","Lunch","Enjoy"]],
      coupon: [["Code","Description"], ["SAVE20","20% off"], ["WELCOME10","10% off first order"]],
      appstore: [["App Store Link","Google Play Link"], ["https://apps.apple.com/app/...","https://play.google.com/store/apps/..."], ["https://apps.apple.com/app/...","https://play.google.com/store/apps/..."]],
      review: [["Review Link"], ["https://g.page/your-business/review"], ["https://example.com/reviews"]],
      mp3: [["Audio Link"], ["https://example.com/song.mp3"], ["https://example.com/episode1.mp3"]],
      "google-form": [["Form Link"], ["https://forms.gle/abc123XYZ"], ["https://docs.google.com/forms/d/e/xyz/viewform"]],
      menu: [["Menu Link"], ["https://example.com/menu"], ["https://restaurant.com/menu.pdf"]],
    };
    await ensureXLSX();
    if(typeof XLSX !== "undefined"){
      const wb = XLSX.utils.book_new();
      for(const [name, rows] of Object.entries(sheets)){
        const ws = XLSX.utils.aoa_to_sheet(rows);
        XLSX.utils.book_append_sheet(wb, ws, name);
      }
      XLSX.writeFile(wb, "freeqrly-batch-template.xlsx");
    } else {
      // Fallback: CSV for current type only
      batchType = ($("batchType") && $("batchType").value) || "url";
      const rows = sheets[batchType] || sheets.url;
      const csv = rows.map(r=>r.map(c=>`"${c}"`).join(",")).join("\n");
      const blob = new Blob([csv], {type: "text/csv"});
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = `freeqrly-batch-${batchType}.csv`;
      a.click();
    }
  });
}

$("batchZip").onclick = async ()=>{ track("batch_zip",{count:batchItems.length});
  await ensureJSZip();
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
/* Frame: wrap QR with border + optional CTA text */
function frameWrap(svgStr, px){
  const frame = (typeof getFrame === "function" ? getFrame() : "none");
  if(frame === "none") return svgStr;
  const fg = $("fg").value, bg = ($("transp") && $("transp").checked) ? "#FFFFFF" : $("bgc").value;
  const pad = Math.round(px * 0.06);
  const ctaH = frame === "cta" ? Math.round(px * 0.14) : 0;
  // Width: QR + padding both sides (QR centered horizontally)
  // Height: QR + padding top/bottom + CTA area (CTA text sits below QR)
  const w = px + pad * 2;
  const h = px + pad * 2 + ctaH;
  const ctaText = ($("frameText") && $("frameText").value) || (I18N[lang] && I18N[lang].frameTextPh) || "Scan me";
  // Always rounded corners for a soft look (both Rounded and With text)
  const radius = Math.round(px * 0.05);
  const esc = s => s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
  // Embed QR SVG as <image> — avoids fragile string surgery on QR internals
  const qrUri = "data:image/svg+xml," + encodeURIComponent(svgStr);
  // CTA text vertically centered in its area (between QR bottom and frame bottom)
  const ctaY = pad + px + (ctaH + pad) / 2;
  return `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">` +
    `<rect width="${w}" height="${h}" rx="${radius}" fill="${bg}"/>` +
    `<rect x="2" y="2" width="${w-4}" height="${h-4}" rx="${Math.max(0,radius-2)}" fill="none" stroke="${fg}" stroke-width="2"/>` +
    `<image href="${qrUri}" xlink:href="${qrUri}" x="${pad}" y="${pad}" width="${px}" height="${px}"/>` +
    (frame === "cta" ? `<text x="${w/2}" y="${ctaY}" text-anchor="middle" dominant-baseline="middle" font-family="system-ui,sans-serif" font-size="${Math.round(px*0.055)}" font-weight="600" fill="${fg}">${esc(ctaText)}</text>` : "") +
    `</svg>`;
}

/* Scannability: contrast ratio between ink and background */
function scanScore(){
  const el = $("scanScore"); if(!el) return;
  const hex2lum = (hex)=>{
    if(!hex || hex === "transparent") return 1;
    const n = parseInt(hex.slice(1), 16);
    const ch = (c)=>{ c/=255; return c<=0.03928 ? c/12.92 : Math.pow((c+0.055)/1.055, 2.4); };
    return 0.2126*ch((n>>16)&255) + 0.7152*ch((n>>8)&255) + 0.0722*ch(n&255);
  };
  const fg = $("fg").value;
  const bg = ($("transp") && $("transp").checked) ? "#FFFFFF" : $("bgc").value;
  const l1 = hex2lum(fg), l2 = hex2lum(bg);
  const ratio = (Math.max(l1,l2)+0.05)/(Math.min(l1,l2)+0.05);
  // Only warn when contrast is too low — no number, just text
  const ok = ratio >= 3;
  el.hidden = ok;
  el.className = "scanScore bad";
  const t = I18N[lang];
  if(!ok) el.textContent = t.scanBad || "Low contrast — may not scan";
}

async function downloadQR(format){
  const btnMap = {png:"dlPng", svg:"dlSvg", pdf:"dlPdf", eps:"dlEps"};
  const button=$(btnMap[format] || "dlPng");
  if(button) button.disabled=true;
  try{
    const px=format==="png"?(parseInt($("size").value)||1024):1024;
    const dlOpts = styleOpts(px);
    // Dynamic mode: download the short-URL QR (same styling, short URL data)
    if(dynamicMode && dynamicShortUrl) dlOpts.data = dynamicShortUrl;
    const qr = new QRCodeStyling(dlOpts);
    if(format === "pdf"){
      // Get SVG, wrap with frame, embed in PDF via canvas
      const svgBlob = await qr.getRawData("svg");
      let svgText = await svgBlob.text();
      svgText = frameWrap(svgText, px);
      // Render SVG to canvas, then to PDF (simple: download as PDF via print-like blob)
      const img = new Image();
      const url = URL.createObjectURL(new Blob([svgText], {type:"image/svg+xml"}));
      await new Promise((res, rej)=>{ img.onload=res; img.onerror=rej; img.src=url; });
      const canvas = document.createElement("canvas");
      canvas.width = px; canvas.height = px;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#fff"; ctx.fillRect(0,0,px,px);
      ctx.drawImage(img, 0, 0, px, px);
      URL.revokeObjectURL(url);
      // Minimal valid PDF (binary-safe assembly + xref table)
      const b64 = canvas.toDataURL("image/jpeg", 0.92).split(",")[1];
      const bin = atob(b64);
      const jpg = new Uint8Array(bin.length);
      for (let i = 0; i < bin.length; i++) jpg[i] = bin.charCodeAt(i);
      const enc = new TextEncoder();
      const E = s => enc.encode(s);
      const body5 = `q ${px} 0 0 ${px} 0 0 cm /I1 Do Q`;
      const objBody = [
        E(`<</Type/Catalog/Pages 2 0 R>>`),
        E(`<</Type/Pages/Kids[3 0 R]/Count 1>>`),
        E(`<</Type/Page/Parent 2 0 R/MediaBox[0 0 ${px} ${px}]/Resources<</XObject<</I1 4 0 R>>>>/Contents 5 0 R>>`),
        null,
        E(body5),
      ];
      const chunks = [E(`%PDF-1.4\n`)];
      const offsets = [0];
      let pos = chunks[0].length;
      for (let n = 1; n <= 5; n++) {
        offsets[n] = pos;
        const open = E(`${n} 0 obj\n`), close = E(`\nendobj\n`);
        if (n === 4) {
          const dict = E(`<</Type/XObject/Subtype/Image/Width ${px}/Height ${px}/ColorSpace/DeviceRGB/BitsPerComponent 8/Filter/DCTDecode/Length ${jpg.length}>>\nstream\n`);
          const tail = E(`\nendstream`);
          chunks.push(open, dict, jpg, tail, close);
          pos += open.length + dict.length + jpg.length + tail.length + close.length;
        } else if (n === 5) {
          const dict = E(`<</Length ${body5.length}>>\nstream\n`);
          const tail = E(`\nendstream`);
          chunks.push(open, dict, objBody[n-1], tail, close);
          pos += open.length + dict.length + objBody[n-1].length + tail.length + close.length;
        } else {
          chunks.push(open, objBody[n-1], close);
          pos += open.length + objBody[n-1].length + close.length;
        }
      }
      let xref = `xref\n0 6\n0000000000 65535 f \n`;
      for (let n = 1; n <= 5; n++) xref += String(offsets[n]).padStart(10, "0") + ` 00000 n \n`;
      xref += `trailer\n<</Size 6/Root 1 0 R>>\nstartxref\n${pos}\n%%EOF`;
      chunks.push(E(xref));
      const pdfBytes = new Uint8Array(chunks.reduce((a, c) => a + c.length, 0));
      let wp = 0;
      for (const c of chunks) { pdfBytes.set(c, wp); wp += c.length; }
      const blob = new Blob([pdfBytes], {type:"application/pdf"});
      const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = "freeqrly.pdf"; a.click();
    } else if(format === "eps"){
      // Render QR to canvas, then emit real PostScript rectangles
      const svgBlob = await qr.getRawData("svg");
      let svgText = await svgBlob.text();
      svgText = frameWrap(svgText, px);
      const img = new Image();
      const url = URL.createObjectURL(new Blob([svgText], {type:"image/svg+xml"}));
      await new Promise((res, rej)=>{ img.onload=res; img.onerror=rej; img.src=url; });
      const canvas = document.createElement("canvas");
      canvas.width = px; canvas.height = px;
      const ctx = canvas.getContext("2d");
      ctx.drawImage(img, 0, 0, px, px);
      URL.revokeObjectURL(url);
      const data = ctx.getImageData(0, 0, px, px).data;
      // Sample at module resolution: find module size by scanning
      // Use a fixed grid: assume QR occupies full canvas, sample every px/25 for coarse grid
      // Better: extract black rectangles at pixel level, grouped by rows
      const fg = $("fg").value.replace("#","");
      const r = parseInt(fg.slice(0,2),16)/255, g = parseInt(fg.slice(2,4),16)/255, b = parseInt(fg.slice(4,6),16)/255;
      let ps = `%!PS-Adobe-3.0 EPSF-3.0\n%%BoundingBox: 0 0 ${px} ${px}\n%%Creator: FreeQrly\n`;
      ps += `${r.toFixed(3)} ${g.toFixed(3)} ${b.toFixed(3)} setrgbcolor\n`;
      // Emit rectangles for dark pixels, merged horizontally per row
      const step = Math.max(1, Math.floor(px / 200)); // limit to 200x200 grid for file size
      for(let y = 0; y < px; y += step){
        let xStart = -1;
        for(let x = 0; x <= px; x += step){
          const idx = ((y * px) + Math.min(x, px-1)) * 4;
          const dark = data[idx] < 128 && data[idx+3] > 128;
          if(dark && xStart === -1) xStart = x;
          if(!dark && xStart !== -1){
            ps += `${xStart} ${px - y - step} ${x - xStart} ${step} rectfill\n`;
            xStart = -1;
          }
        }
        if(xStart !== -1) ps += `${xStart} ${px - y - step} ${px - xStart} ${step} rectfill\n`;
      }
      ps += `showpage\n%%EOF`;
      const blob = new Blob([ps], {type:"application/postscript"});
      const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = "freeqrly.eps"; a.click();
    } else if(format === "svg"){
      // Apply frame to SVG download
      const svgBlob = await qr.getRawData("svg");
      let svgText = await svgBlob.text();
      svgText = frameWrap(svgText, px);
      const blob = new Blob([svgText], {type:"image/svg+xml"});
      const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = "freeqrly.svg"; a.click();
      setTimeout(()=>URL.revokeObjectURL(a.href), 5000);
    } else {
      // PNG: render framed SVG to canvas, then download
      const svgBlob = await qr.getRawData("svg");
      let svgText = await svgBlob.text();
      svgText = frameWrap(svgText, px);
      const img = new Image();
      const url = URL.createObjectURL(new Blob([svgText], {type:"image/svg+xml"}));
      await new Promise((res, rej)=>{ img.onload=res; img.onerror=rej; img.src=url; });
      // Framed size: width = QR + padding, height = QR + padding + CTA
      const frame = (typeof getFrame === "function" ? getFrame() : "none");
      const pad = frame === "none" ? 0 : Math.round(px * 0.06);
      const ctaH = frame === "cta" ? Math.round(px * 0.14) : 0;
      const fw = px + pad * 2;
      const fh = px + pad * 2 + ctaH;
      const canvas = document.createElement("canvas");
      canvas.width = fw; canvas.height = fh;
      const ctx = canvas.getContext("2d");
      ctx.drawImage(img, 0, 0, fw, fh);
      URL.revokeObjectURL(url);
      const a = document.createElement("a");
      a.href = canvas.toDataURL("image/png");
      a.download = "freeqrly.png"; a.click();
    }
    saveHist(); track("qr_download",{type:cur,format:format});
  }catch(e){}
  finally{ if(button) button.disabled=false; }
}
$("dlPng").onclick=()=>downloadQR("png");
// Dropdown menu: SVG / PDF / EPS
document.querySelectorAll("#dlMenu button").forEach(btn=>{
  btn.addEventListener("click", ()=>downloadQR(btn.dataset.fmt));
});
// Arrow button also toggles menu on click (for touch devices)
const _arrow = $("dlArrow");
if(_arrow) _arrow.addEventListener("click", (e)=>{
  e.stopPropagation();
  const menu = $("dlMenu");
  if(menu) menu.style.opacity = menu.style.opacity === "1" ? "0" : "1";
  if(menu) menu.style.visibility = menu.style.visibility === "visible" ? "hidden" : "visible";
});
document.addEventListener("click", (e)=>{
  const menu = $("dlMenu");
  if(menu && !e.target.closest(".dlSplit")){
    menu.style.opacity = "0"; menu.style.visibility = "hidden";
  }
});
// Frame segmented control wiring
let frameVal = "none";
const _segFrame = $("segFrame");
if(_segFrame){
  _segFrame.addEventListener("click", (e)=>{
    const btn = e.target.closest("button"); if(!btn) return;
    frameVal = btn.dataset.v;
    _segFrame.querySelectorAll("button").forEach(b=>b.classList.toggle("on", b === btn));
    const fe = $("frameExpand");
    if(fe) fe.classList.toggle("show", frameVal === "cta");
    draw(); scanScore();
  });
  // Default: mark "None" as active
  const _none = _segFrame.querySelector('button[data-v="none"]');
  if(_none) _none.classList.add("on");
}
const _ft = $("frameText");
if(_ft) _ft.addEventListener("input", ()=>{ draw(); });
// Helper: current frame value (used by frameWrap and draw)
function getFrame(){ return frameVal; }
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
    pop.style.top=Math.min(window.innerHeight-320, r.bottom+8)+"px";
  };
})();


/* Draft: preserve the generator state across the sign-in redirect.
   Saved to sessionStorage (same-tab only) right before leaving for /login/;
   restored on return when the URL carries ?draft=1 and the user is signed in. */
const DRAFT_KEY = "freeqrly-draft";
function saveDraft(){
  if(cur === "batch") return;
  try{
    const fields = {};
    document.querySelectorAll("#fields input, #fields textarea, #fields select").forEach(el => {
      if(el.id) fields[el.id] = el.value;
    });
    const preset = document.querySelector('#logoRow .logopick[data-preset].on');
    const draft = {
      type: cur, fields,
      dots: $("dots") ? $("dots").value : "square",
      ecc: $("ecc") ? $("ecc").value : "M",
      fg: $("fg") ? $("fg").value : "#22303F",
      bgc: $("bgc") ? $("bgc").value : "#ffffff",
      transp: !!($("transp") && $("transp").checked),
      size: $("size") ? $("size").value : "1024",
      frame: (typeof getFrame === "function" ? getFrame() : "none"),
      frameText: ($("frameText") && $("frameText").value) || "",
      logoPreset: preset ? preset.dataset.preset : null,
      // Custom uploaded logos can be large — only keep small ones.
      logoData: (typeof logoData !== "undefined" && logoData && logoData.length < 1024 * 1024) ? logoData : null,
      ts: Date.now()
    };
    sessionStorage.setItem(DRAFT_KEY, JSON.stringify(draft));
  }catch(e){ /* storage full/blocked: continue without a draft */ }
}
function loginNextUrl(){
  const u = new URL(location.href);
  u.searchParams.set("draft", "1");
  return u.pathname + u.search;
}
function switchToDynamic(){
  if(cur === "batch") return;
  const btn = document.querySelector('#segMode button[data-mode="dynamic"]');
  if(btn && !dynamicMode) btn.click();
}
function ensureCustomDot(boxId, hex, hiddenId, isFg){
  const box = document.getElementById(boxId); if(!box) return;
  const known = Array.from(box.querySelectorAll(".cdot[data-v]")).some(b => b.dataset.v.toLowerCase() === hex.toLowerCase());
  if(known) return;
  let custom = box.querySelector(".cdot.custom");
  if(!custom){
    custom = document.createElement("button");
    custom.type = "button"; custom.className = "cdot custom";
    custom.setAttribute("aria-label", "Custom color");
    box.insertBefore(custom, box.querySelector(".cpick"));
    custom.addEventListener("click", () => {
      const hidden = $(hiddenId);
      if(hidden){ hidden.value = custom.dataset.v; hidden.dispatchEvent(new Event("input", { bubbles: true })); }
      dotsInit._mark(boxId, custom.dataset.v);
      const transp = $("transp"); if(transp && !isFg) transp.checked = false;
      draw();
    });
  }
  custom.dataset.v = hex; custom.style.background = hex; custom.title = hex;
}
function restoreDraft(){
  let draft;
  try{ draft = JSON.parse(sessionStorage.getItem(DRAFT_KEY) || "null"); }catch(e){ draft = null; }
  if(!draft || !ORDER.includes(draft.type) || draft.type === "batch") return false;
  cur = draft.type; renderTabs(); renderFields();
  // Fields (raw values, incl. date/time parts + hidden select/datetime inputs)
  Object.keys(draft.fields || {}).forEach(id => {
    const el = document.getElementById(id);
    if(el){ el.value = draft.fields[id]; el.dispatchEvent(new Event("input", { bubbles: true })); }
  });
  // Select-type fields: sync the visible segmented buttons with the hidden select
  (I18N[lang].fields[draft.type] || []).forEach(([id, , third]) => {
    if(typeof third === "string" && third.startsWith("select:")){
      const el = $("f_" + id);
      if(el && el.previousElementSibling) el.previousElementSibling.querySelectorAll("button").forEach(b => b.classList.toggle("on", b.dataset.v === el.value));
    }
  });
  // Style controls: hidden value + visual state
  const setSeg = (segId, val) => { const seg = $(segId); if(!seg) return; seg.querySelectorAll("button").forEach(b => b.classList.toggle("on", b.dataset.v === val)); };
  if($("dots")){ $("dots").value = draft.dots || "square"; setSeg("segDots", $("dots").value); }
  if($("ecc")){ $("ecc").value = draft.ecc || "M"; setSeg("segEcc", $("ecc").value); }
  if($("fg")) $("fg").value = draft.fg || "#22303F";
  if($("bgc")) $("bgc").value = draft.bgc || "#ffffff";
  if($("transp")) $("transp").checked = !!draft.transp;
  ensureCustomDot("fgDots", $("fg").value, "fg", true);
  if(!draft.transp) ensureCustomDot("bgDots", $("bgc").value, "bgc", false);
  if(typeof dotsInit !== "undefined" && dotsInit._mark){
    dotsInit._mark("fgDots", $("fg").value);
    dotsInit._mark("bgDots", draft.transp ? "transparent" : $("bgc").value);
  }
  if($("size")){ $("size").value = draft.size || "1024"; setSeg("segSize", $("size").value); const sv = $("sizeVal"); if(sv) sv.textContent = $("size").value; }
  if(typeof frameVal !== "undefined"){ frameVal = draft.frame || "none"; setSeg("segFrame", frameVal); const fe = $("frameExpand"); if(fe) fe.classList.toggle("show", frameVal === "cta"); }
  if($("frameText")) $("frameText").value = draft.frameText || "";
  // Logo
  if(draft.logoPreset){
    const b = document.querySelector('#logoRow .logopick[data-preset="' + draft.logoPreset + '"]');
    if(b && !b.classList.contains("on")) b.click();
  } else if(draft.logoData && typeof setLogo === "function"){
    setLogo(draft.logoData, null);
  }
  draw();
  return true;
}

/* --- Dynamic QR mode (preview-integrated) --- */
/* Toggle lives at top of preview. Dynamic: preview blurs + download disabled
   + Generate button appears. After generation: QR clears, download enabled,
   result shows link + 8-char edit key. No manage section. */
(function(){
  const seg = $("segMode"); if(!seg) return;
  const genBtn = $("dynCreate");
  const hintLine = $("modeHintLine");
  const qrpaper = document.querySelector(".qrpaper");
  const dlRow = document.querySelector(".dlrow");

  function refreshDynamicUI(){
    if(!hintLine) return;
    const t = I18N[lang] || I18N.en;
    if(dynamicMode){
      // Dynamic: blur preview, disable download, show Generate (if not yet generated)
      if(qrpaper) qrpaper.classList.toggle("blurred", !dynamicGenerated);
      if(dlRow) dlRow.classList.toggle("disabled", !dynamicGenerated);
      if(genBtn) genBtn.hidden = false; // stays visible — can generate a new code anytime
      if(!dynamicGenerated){
        hintLine.textContent = t.dynHint || "Fill in your content, then hit Generate.";
      } else {
        hintLine.textContent = t.dynReady || "Your dynamic QR is ready. Print it — the content can change anytime.";
      }
      // Dynamic codes require an account: nudge logged-out users to sign in.
      const signinHint = $("dynSigninHint");
      if(signinHint){
        const st = window.__authState || {};
        const show = !!st.loaded && !st.user;
        signinHint.hidden = !show;
        if(show){
          const l = $("dynSigninLink");
          if(l){ l.href = "/login/?next=" + encodeURIComponent(loginNextUrl()); l.onclick = () => { saveDraft(); }; }
        }
      }
    } else {
      // Static: normal
      if(qrpaper) qrpaper.classList.remove("blurred");
      if(dlRow) dlRow.classList.remove("disabled");
      if(genBtn) genBtn.hidden = true;
      const sh = $("dynSigninHint"); if(sh) sh.hidden = true;
      hintLine.textContent = t.live || "Live preview — updates as you type";
      const res = $("dynResult"); if(res) res.hidden = true;
    }
    draw();
  }

  seg.addEventListener("click", e => {
    const infoBtn = e.target.closest("#modeInfoBtn");
    if(infoBtn){
      // "?" toggles the static/dynamic explainer (works for touch; hover covers mouse)
      const tip = document.getElementById("modeTip");
      if(tip) tip.classList.toggle("show");
      e.stopPropagation();
      return;
    }
    const btn = e.target.closest("button[data-mode]"); if(!btn) return;
    seg.querySelectorAll("button[data-mode]").forEach(b => b.classList.toggle("on", b === btn));
    dynamicMode = btn.dataset.mode === "dynamic";
    // Switching back to static resets dynamic state
    if(!dynamicMode){ dynamicShortUrl = ''; dynamicGenerated = false; }
    refreshDynamicUI();
  });
  // Tapping elsewhere hides the static/dynamic explainer
  document.addEventListener("click", e => {
    if(!e.target.closest("#modeInfoBtn")){
      const tip = document.getElementById("modeTip");
      if(tip) tip.classList.remove("show");
    }
  });

  // Current generator style (saved with each dynamic code so Manage can
  // re-render the exact QR + prefill the editor). Custom uploaded logos
  // are uploaded to R2 first (POST /api/logos) and stored as logoKey.
  async function currentStyle(){
    const preset = document.querySelector('#logoRow .logopick[data-preset].on');
    const style = {
      fg: $("fg").value, bg: $("bgc").value,
      transparent: !!($("transp") && $("transp").checked),
      dots: $("dots").value, ecc: $("ecc").value,
      frame: (typeof getFrame === "function" ? getFrame() : "none"),
      frameText: ($("frameText") && $("frameText").value) || "",
      logoPreset: preset ? preset.dataset.preset : null,
      logoKey: null
    };
    if(logoData && !style.logoPreset){
      try{
        const blob = await (await fetch(logoData)).blob();
        const fd = new FormData(); fd.append("file", blob, "logo");
        const r = await fetch("/api/logos", { method: "POST", credentials: "same-origin", body: fd });
        const d = await r.json().catch(() => ({}));
        if(r.ok && d.key) style.logoKey = d.key;
      }catch(e){ /* logo upload failed: code still saves, just without the logo */ }
    }
    return style;
  }
  // Create dynamic code from CURRENT generator state
  if(genBtn) genBtn.addEventListener("click", async () => {
    const payload = content();
    if(!payload){ alert("Please enter content first"); return; }
    // Dynamic codes require an account — send logged-out users to sign in,
    // then back here.
    {
      const st = await window.getAuthState();
      if(!st.user){ saveDraft(); location.href = "/login/?next=" + encodeURIComponent(loginNextUrl()); return; }
    }
    genBtn.disabled = true;
    genBtn.innerHTML = '<span class="spinner"></span>Generating…';
    try{
      const style = await currentStyle();
      const r = await fetch("/api/codes", { method:"POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify({ type: cur, payload, style }) });
      const d = await r.json();
      if(!r.ok){
        if(r.status === 401){ saveDraft(); location.href = "/login/?next=" + encodeURIComponent(loginNextUrl()); return; }
        alert(d.error || "Failed to create"); return;
      }
      dynamicShortUrl = d.shortUrl;
      dynamicGenerated = true;
      const res = $("dynResult"); if(res) res.hidden = false;
      const link = $("dynShortUrl"); if(link){ link.href = d.shortUrl; link.textContent = d.shortUrl.replace(/^https?:\/\//, ''); }
      // New code: show Dashboard + Manage links (session-owned, no EditKey).
      const dashLink = $("dynDashLink");
      const mLink = $("dynManageLink");
      if(mLink){ mLink.hidden = false; mLink.href = "/dashboard/?c=" + encodeURIComponent(d.code); }
      if(dashLink) dashLink.hidden = false;
      refreshDynamicUI();
    }catch(e){ alert("Network error"); }
    finally{
      genBtn.disabled = false;
      genBtn.innerHTML = (I18N[lang] && I18N[lang].dynCreate ? I18N[lang].dynCreate : 'Generate dynamic QR') + ' →';
    }
  });


  // Expose refresh for draw() to call when content changes
  window.refreshDynamicUI = refreshDynamicUI;

})();

// Switch the type rail to a given type
function switchToType(type){
  if(!ORDER.includes(type)) return;
  cur = type;
  renderTabs();
  renderFields();
  updateStudioMascot();
}

// Reverse-parse a stored payload into the generator fields (Manage page)
// Shared auth state: one GET /api/auth/me per page load, cached.
// Shape-tolerant: backend returns {user:{...}}; older callers used a flat object.
window.__authState = { loaded:false, user:null };
window.getAuthState = function(){
  if(window.__authStatePromise) return window.__authStatePromise;
  window.__authStatePromise = fetch("/api/auth/me", {credentials:"same-origin"}).then(r => {
    if(!r.ok) return null;
    return r.json().catch(()=>null);
  }).then(d => {
    const u = (d && d.user) || d || null;
    window.__authState = { loaded:true, user: (u && u.email) ? u : null };
    return window.__authState;
  }).catch(() => {
    window.__authState = { loaded:true, user:null };
    return window.__authState;
  });
  return window.__authStatePromise;
};

// Header auth state + quota hint. Fail-open: anonymous use is unaffected
// if /api/auth/me is unreachable, 401s, or returns anything unexpected.
// Logged in: avatar + name trigger, click/hover opens the account menu
// (Dashboard, Export, Delete, Log out) — same module as the dashboard.
function initAuthHeader(){
  try{
    const area = $("authArea");
    const quotaEl = $("quotaHint");
    const tr = k => (I18N[lang] && I18N[lang][k]) || I18N.en[k] || k;
    const escH = s => String(s == null ? "" : s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
    window.getAuthState().then(st => {
      const me = st.user;
      if(window.refreshDynamicUI) window.refreshDynamicUI();
      if(!me) return;
      if(quotaEl && typeof me.codeCount === "number" && typeof me.codeLimit === "number"){
        if(me.codeCount >= me.codeLimit){
          quotaEl.textContent = "You've reached your code limit (" + me.codeCount + "/" + me.codeLimit + ")";
          quotaEl.hidden = false;
        }
      }
      if(area){
        area.textContent = "";
        const avatarUrl = me.avatar || me.avatar_url;
        const displayName = me.name || me.email;
        const avHtml = avatarUrl
          ? `<img class="hAcctAvatar" src="${escH(avatarUrl)}" alt="" referrerpolicy="no-referrer">`
          : `<span class="hAcctAvatar">${escH(displayName.trim().charAt(0).toUpperCase())}</span>`;
        const providerLabel = { password: "Email", email: "Email", google: "Google", github: "GitHub" };
        const wrap = document.createElement("span");
        wrap.className = "hAcct";
        wrap.innerHTML =
          `<button class="hAcctTrigger" type="button" aria-haspopup="menu">${avHtml}<span class="hAcctName">${escH(displayName)}</span><span class="hAcctChev">▾</span></button>` +
          `<span class="hAcctMenu" role="menu">` +
            `<div class="mEmail">${escH(me.email)}</div>` +
            `<div class="mProv">${escH(tr("acctSignedInWith").replace("{method}", providerLabel[me.authMethod] || "Email"))}</div>` +
            `<div class="menuSep"></div>` +
            `<a href="/dashboard/" role="menuitem">${escH(tr("acctDashboard"))}</a>` +
            `<button type="button" data-act="export" role="menuitem">${escH(tr("acctExport"))}</button>` +
            `<button type="button" class="dangerItem" data-act="delete" role="menuitem">${escH(tr("acctDelete"))}</button>` +
            `<div class="menuSep"></div>` +
            `<button type="button" data-act="logout" role="menuitem">${escH(tr("acctLogout"))}</button>` +
          `</span>`;
        area.appendChild(wrap);
        const trig = wrap.querySelector(".hAcctTrigger");
        trig.addEventListener("click", e => { e.stopPropagation(); wrap.classList.toggle("open"); });
        document.addEventListener("click", e => { if(!e.target.closest(".hAcct")) wrap.classList.remove("open"); });
        wrap.querySelector('[data-act="export"]').addEventListener("click", () => { location.href = "/api/auth/export"; });
        wrap.querySelector('[data-act="logout"]').addEventListener("click", async (e) => {
          const btn = e.currentTarget;
          if(btn.disabled) return;
          btn.disabled = true;
          btn.style.opacity = ".55";
          btn.style.pointerEvents = "none";
          try{ await fetch("/api/auth/logout", { method: "POST", credentials: "same-origin" }); }catch(err){}
          location.href = "/login/";
        });
        wrap.querySelector('[data-act="delete"]').addEventListener("click", async () => {
          if(!confirm(tr("acctDeleteConfirm"))) return;
          try{
            const r = await fetch("/api/auth/delete-account", { method: "POST", credentials: "same-origin" });
            const d = await r.json().catch(() => ({}));
            if(!r.ok){ alert(d.error || tr("acctDeleteFailed")); return; }
            location.href = "/";
          }catch(err){ alert(tr("acctNetErr")); }
        });
      }
    }).catch(()=>{});
  }catch(e){}
}
detectLang().then(async l => {
  lang = l; applyLang(); draw();
  initAuthHeader(); // after lang is set, so the account menu uses the right language
  if(window.refreshDynamicUI) window.refreshDynamicUI();
  const params = new URLSearchParams(location.search);
  if(params.get("draft") === "1"){
    try{
      const st = await window.getAuthState();
      if(st.user && restoreDraft()){
        switchToDynamic();
        try{ sessionStorage.removeItem(DRAFT_KEY); }catch(e){}
        const u = new URL(location.href); u.searchParams.delete("draft");
        history.replaceState(null, "", u.pathname + u.search + u.hash);
      }
    }catch(e){}
  } else if(params.get("mode") === "dynamic"){
    switchToDynamic();
  }
});
})();
