/* FreeQrly v1.0 — app logic */
(function(){
"use strict";
const $ = id => document.getElementById(id);

const I18N = {
en:{
  title:"FreeQrly — QR Code Generator, Private by Design",
  metaDesc:"FreeQrly is a free QR code generator that runs entirely in your browser. No sign-up, no tracking, no expiry. Export PNG & SVG.",
  navStudio:"Studio",navWhy:"Principles",navFaq:"FAQ",
  kicker:"Free · No sign-up · Private by design",
  h1a:"Quiet codes for",h1b:"loud",h1c:"places.",
  lede:"Make beautiful QR codes right in your browser — no sign-up, no tracking, no expiry. Free, simple, and yours to keep.",
  hc1:"Content types",hc2:"Export",hc3:"Your data",hc3v:"Stays with you",hc4:"Price",hc4v:"Free, forever",
  sOver:"The studio",sTitle:"Create your QR code",
  appearance:"Style",ink:"Ink",paper:"Paper",dots:"Dot style",ecc:"Error correction",
  dSquare:"Square",dRound:"Round",dSoft:"Soft",dPebble:"Pebble",
  eL:"L — light",eM:"M — medium",eQ:"Q — strong",eH:"H — maximum",
  eccHint:"Higher levels survive logos and wear.",
  size:"Export size",logo:"Add your logo",
  privnote:"Everything is generated locally in your browser. Disconnect from the internet after the page loads — it still works.",
  live:"Live preview — updates as you type",
  bLabel:"One link per line",bGo:"Generate all",bZip:"Download ZIP",
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
  fin:"Made quietly, in your browser.",
  dl:"Download",
  types:{url:["Website","link, page, video"],text:["Text","any words"],wifi:["WiFi","join instantly"],vcard:["Contact","vCard"],email:["Email","prefilled"],sms:["SMS","prefilled text"],phone:["Call","tap to dial"],geo:["Place","map pin"],batch:["Batch","many at once"]},
  fields:{url:[["url","Destination","https://example.com"]],text:[["text","Message","textarea","Hello, world!"]],
    wifi:[["ssid","Network name","MyWiFi"],["pass","Password",""],["enc","Security","select:WPA,WPA2,WEP,nopass"]],
    vcard:[["name","Full name","Jane Doe"],["phone","Phone","+1 555 0100"],["email","Email","jane@example.com"]],
    email:[["to","To","hi@example.com"],["subject","Subject","Hello"],["body","Body","textarea",""]],
    sms:[["phone","Phone","+1 555 0100"],["body","Message",""]],
    phone:[["phone","Phone","+1 555 0100"]],geo:[["lat","Latitude","37.7749"],["lng","Longitude","-122.4194"]]}
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
  appearance:"外观样式",ink:"墨色",paper:"纸色",dots:"码点形状",ecc:"容错等级",
  dSquare:"方形",dRound:"圆形",dSoft:"柔和",dPebble:"鹅卵石",
  eL:"L — 低",eM:"M — 中",eQ:"Q — 高",eH:"H — 最高",
  eccHint:"容错越高，越耐磨损、越适合加 Logo。",
  size:"导出尺寸",logo:"添加 Logo",
  privnote:"所有生成都在你的浏览器里完成。页面加载后断网，也照样能用。",
  live:"实时预览，输入即变",
  bLabel:"每行一个链接",bGo:"全部生成",bZip:"下载 ZIP",
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
  fin:"在你的浏览器里，静静生成。",
  dl:"下载",
  types:{url:["网址","链接、页面、视频"],text:["文本","任意文字"],wifi:["WiFi","一键联网"],vcard:["名片","vCard"],email:["邮箱","预填内容"],sms:["短信","预填内容"],phone:["电话","点击拨号"],geo:["位置","地图标记"],batch:["批量","一次多个"]},
  fields:{url:[["url","目标地址","https://example.com"]],text:[["text","内容","textarea","你好，世界！"]],
    wifi:[["ssid","网络名称","MyWiFi"],["pass","密码",""],["enc","加密方式","select:WPA,WPA2,WEP,nopass"]],
    vcard:[["name","姓名","王小明"],["phone","电话","+86 138 0000 0000"],["email","邮箱","hi@example.com"]],
    email:[["to","收件人","hi@example.com"],["subject","主题","你好"],["body","正文","textarea",""]],
    sms:[["phone","电话","+86 138 0000 0000"],["body","内容",""]],
    phone:[["phone","电话","+86 138 0000 0000"]],geo:[["lat","纬度","39.9042"],["lng","经度","116.4074"]]}
}};

let lang = "en";
/* language: ?lang= > saved choice > timezone hint > IP geolocation > browser language */
function syncGuess(){
  const q = new URLSearchParams(location.search).get("lang");
  if(q==="en"||q==="zh") return q;
  const saved = localStorage.getItem("freeqrly-lang");
  if(saved==="en"||saved==="zh") return saved;
  try{
    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone||"";
    if(/Asia\/(Shanghai|Taipei|Hong_Kong|Macau|Urumqi|Chongqing)/.test(tz)) return "zh";
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
    if(j && ["CN","HK","TW","MO"].includes(j.country_code)) return "zh";
  }catch(e){}
  return ((navigator.language||"en").toLowerCase().startsWith("zh")) ? "zh" : "en";
}
let cur = "url", logoData = null;
const ORDER = ["url","text","wifi","vcard","email","sms","phone","geo","batch"];

const v = id => { const el = $("f_"+id); return el ? el.value.trim() : ""; };
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
  }
  return " ";
}
function styleOpts(px){
  return {
    width:px, height:px, data:content(), margin:4,
    qrOptions:{ errorCorrectionLevel:$("ecc").value },
    imageOptions:{ crossOrigin:"anonymous", margin:8, imageSize:.4 },
    dotsOptions:{ color:$("fg").value, type:$("dots").value },
    backgroundOptions:{ color:$("bgc").value },
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
function renderTabs(){
  const t = $("tabs"); t.innerHTML="";
  ORDER.forEach(k=>{
    const [name, sub] = I18N[lang].types[k];
    const b = document.createElement("button");
    b.setAttribute("role","tab");
    b.innerHTML = `${name}<small>${sub}</small>`;
    b.className = k===cur ? "on" : "";
    b.onclick = ()=>{ cur=k; renderTabs(); renderFields(); draw();
      $("batchPanel").hidden = cur!=="batch";
    };
    t.appendChild(b);
  });
}
function renderFields(){
  const f = $("fields"); f.innerHTML="";
  if(cur==="batch") return;
  I18N[lang].fields[cur].forEach(([id,label,kind,ph])=>{
    const lab = document.createElement("div"); lab.className="fl"; lab.textContent=label; f.appendChild(lab);
    let el;
    if(kind==="textarea"){ el=document.createElement("textarea"); el.placeholder=ph||""; }
    else if(typeof kind==="string" && kind.startsWith("select:")){
      el=document.createElement("select");
      kind.slice(7).split(",").forEach(o=>{ const op=document.createElement("option"); op.value=o; op.textContent=o; el.appendChild(op); });
    } else { el=document.createElement("input"); el.type="text"; el.placeholder=kind||""; }
    el.id="f_"+id; el.oninput=draw; f.appendChild(el);
  });
}
function applyLang(){
  document.documentElement.lang = lang==="zh" ? "zh-CN" : "en";
  document.title = I18N[lang].title;
  document.querySelector('meta[name="description"]').setAttribute("content", I18N[lang].metaDesc);
  document.querySelectorAll("[data-i18n]").forEach(el=>{
    const k = el.getAttribute("data-i18n");
    if(I18N[lang][k] !== undefined) el.textContent = I18N[lang][k];
  });
  $("langBtn").textContent = lang==="en" ? "中文" : "EN";
  renderTabs(); renderFields();
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
  renderBatch();
};
$("batchZip").onclick = async ()=>{
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
/* controls */
function syncHex(){ $("fgHex").textContent=$("fg").value; $("bgHex").textContent=$("bgc").value; }
["fg","bgc","dots","ecc"].forEach(id=>{ $(id).addEventListener("input",()=>{syncHex();draw();}); $(id).addEventListener("change",()=>{syncHex();draw();}); });
$("size").addEventListener("input",()=>{ $("sizeVal").textContent=$("size").value; });
$("logo").addEventListener("change",e=>{
  const f=e.target.files[0]; if(!f) return;
  const r=new FileReader();
  r.onload=()=>{ logoData=r.result; if(["L","M"].includes($("ecc").value)) $("ecc").value="Q"; draw(); if(cur==="batch") renderBatch(); };
  r.readAsDataURL(f);
});
$("dlPng").onclick=()=> new QRCodeStyling(styleOpts(parseInt($("size").value)||1024)).download({name:"freeqrly",extension:"png"});
$("dlSvg").onclick=()=> new QRCodeStyling(styleOpts(1024)).download({name:"freeqrly",extension:"svg"});
/* theme */
const root=document.documentElement;
function setTheme(dark){
  if(dark) root.setAttribute("data-theme","dark"); else root.removeAttribute("data-theme");
  localStorage.setItem("freeqrly-theme", dark?"dark":"light");
}
setTheme(localStorage.getItem("freeqrly-theme")==="dark" ||
  (!localStorage.getItem("freeqrly-theme") && matchMedia("(prefers-color-scheme: dark)").matches));
$("themeBtn").onclick=()=> setTheme(root.getAttribute("data-theme")!=="dark");
$("langBtn").onclick=()=>{ lang = lang==="en"?"zh":"en"; applyLang(); };

syncHex();
detectLang().then(l=>{ lang = l; applyLang(); draw(); });
})();
