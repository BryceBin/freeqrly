/* QRForge v1.0 — app logic */
(function(){
"use strict";
const $ = id => document.getElementById(id);

const I18N = {
en:{
  title:"QRForge — Free QR Code Generator, Private by Design",
  metaDesc:"Generate beautiful QR codes in your browser. Free forever, no sign-up, nothing uploaded. PNG & SVG export.",
  navStudio:"Studio",navWhy:"Principles",navFaq:"FAQ",
  kicker:"Free · No sign-up · Private by design",
  h1a:"Quiet codes for",h1b:"loud",h1c:"places.",
  lede:"A calm little studio for making QR codes. Everything happens in your browser — no accounts, no tracking, no expiry. Just a code that works, for as long as you need it.",
  hc1:"Content types",hc2:"Export",hc3:"Data uploaded",hc3v:"Nothing",hc4:"Price",hc4v:"Free, forever",
  sOver:"The studio",sTitle:"Make your code",
  appearance:"Appearance",ink:"Ink",paper:"Paper",dots:"Module style",ecc:"Error correction",
  dSquare:"Square",dRound:"Round",dSoft:"Soft",dPebble:"Pebble",
  eL:"L — light",eM:"M — medium",eQ:"Q — strong",eH:"H — maximum",
  size:"Export size",logo:"Add your logo",
  privnote:"Everything is generated locally in your browser. Disconnect from the internet after the page loads — it still works.",
  live:"— a live preview, drawn as you type —",
  bLabel:"One link per line",bGo:"Generate all",bZip:"Download ZIP",
  p1n:"No. 1",p1t:"Nothing leaves your desk",p1p:"Codes are drawn by JavaScript on your own device. Load the page, disconnect the network — it keeps working. There is no server to trust, because none is involved.",
  p2n:"No. 2",p2t:"Made to be permanent",p2p:"A static code holds its destination inside its pattern. Print it today; it scans in a decade. No subscription to lapse, no platform to vanish.",
  p3n:"No. 3",p3t:"Free without footnotes",p3p:"No watermark, no sign-up wall, no expiry. The studio is the whole product, and the whole product is free.",
  faqT:"Questions, answered gently",
  q1:"Do free QR codes expire?",a1:"Never. The destination lives inside the pattern itself, so a code works as long as its destination does. Paid \"dynamic\" codes route through a vendor's servers and can stop working when you cancel.",
  q2:"Is my WiFi password safe here?",a2:"Yes — it never leaves your browser. For peace of mind, load this page once, disconnect from the internet, and then type.",
  q3:"Static or dynamic — which should I choose?",a3:"Static for anything permanent: WiFi cards, contact details, fixed links. Dynamic (editable + scan analytics) suits campaigns, and is on our roadmap.",
  q4:"Can I use these commercially?",a4:"Yes. Everything you generate here is yours — packaging, menus, business cards, no attribution required.",
  fin:"Set quietly, printed in your browser.",
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
  title:"QRForge — 免费二维码生成器，隐私优先",
  metaDesc:"直接在浏览器里生成精美二维码。永久免费、免注册、不上传任何数据。支持 PNG / SVG 导出。",
  navStudio:"工作台",navWhy:"理念",navFaq:"常见问题",
  kicker:"免费 · 免注册 · 隐私优先",
  h1a:"安静的码，",h1b:"热闹",h1c:"的地方用。",
  lede:"一个安静的二维码小作坊。所有生成都在你的浏览器里完成——无需账号、无追踪、永不过期。就是一个能用的码，能用多久用多久。",
  hc1:"内容类型",hc2:"导出",hc3:"上传数据",hc3v:"无",hc4:"价格",hc4v:"永久免费",
  sOver:"工作台",sTitle:"生成你的二维码",
  appearance:"外观",ink:"前景色",paper:"背景色",dots:"码点样式",ecc:"容错级别",
  dSquare:"方形",dRound:"圆形",dSoft:"柔和",dPebble:"鹅卵石",
  eL:"L — 低",eM:"M — 中",eQ:"Q — 高",eH:"H — 最高",
  size:"导出尺寸",logo:"添加 Logo",
  privnote:"所有生成都在你的浏览器本地完成。页面加载后断开网络也能用。",
  live:"—— 实时预览，输入即更新 ——",
  bLabel:"每行一个链接",bGo:"全部生成",bZip:"下载 ZIP",
  p1n:"其一",p1t:"数据不离开你的桌子",p1p:"二维码由你设备上的 JavaScript 绘制。加载页面后断网，它照样工作。没有服务器可信任——因为根本没有服务器参与。",
  p2n:"其二",p2t:"为永久而生",p2p:"静态码把目标地址直接编码在图案里。今天印出来，十年后照样能扫。没有会过期的订阅，没有会消失的平台。",
  p3n:"其三",p3t:"免费，没有小字",p3p:"无水印、无注册墙、永不过期。工作台就是全部产品，而全部产品都是免费的。",
  faqT:"常见问题，轻声解答",
  q1:"免费二维码会过期吗？",a1:"永不过期。目标地址直接编码在图案里，只要目标地址有效，码就一直有效。付费的动态码要经过服务商的服务器，停付可能失效。",
  q2:"在这里输入 WiFi 密码安全吗？",a2:"安全，密码不会离开你的浏览器。更放心的话，页面加载后断网再输入。",
  q3:"静态码和动态码怎么选？",a3:"目标不变就用静态码：WiFi 卡、名片、固定链接。动态码（可编辑+扫码统计）适合营销活动，已在路线图上。",
  q4:"可以商用吗？",a4:"可以。这里生成的一切都属于你——包装、菜单、名片，无需署名。",
  fin:"安静排版，在你的浏览器里印刷。",
  dl:"下载",
  types:{url:["网址","链接、页面、视频"],text:["文本","任意文字"],wifi:["WiFi","一键联网"],vcard:["名片","vCard"],email:["邮箱","预填内容"],sms:["短信","预填内容"],phone:["电话","点击拨号"],geo:["位置","地图标记"],batch:["批量","一次多个"]},
  fields:{url:[["url","目标地址","https://example.com"]],text:[["text","内容","textarea","你好，世界！"]],
    wifi:[["ssid","网络名称","MyWiFi"],["pass","密码",""],["enc","加密方式","select:WPA,WPA2,WEP,nopass"]],
    vcard:[["name","姓名","王小明"],["phone","电话","+86 138 0000 0000"],["email","邮箱","hi@example.com"]],
    email:[["to","收件人","hi@example.com"],["subject","主题","你好"],["body","正文","textarea",""]],
    sms:[["phone","电话","+86 138 0000 0000"],["body","内容",""]],
    phone:[["phone","电话","+86 138 0000 0000"]],geo:[["lat","纬度","39.9042"],["lng","经度","116.4074"]]}
}};

let lang = localStorage.getItem("qrforge-lang") || ((navigator.language||"en").startsWith("zh") ? "zh" : "en");
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
  localStorage.setItem("qrforge-lang", lang);
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
  a.href = URL.createObjectURL(blob); a.download = "qrforge-batch.zip"; a.click();
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
$("dlPng").onclick=()=> new QRCodeStyling(styleOpts(parseInt($("size").value)||1024)).download({name:"qrforge",extension:"png"});
$("dlSvg").onclick=()=> new QRCodeStyling(styleOpts(1024)).download({name:"qrforge",extension:"svg"});
/* theme */
const root=document.documentElement;
function setTheme(dark){
  if(dark) root.setAttribute("data-theme","dark"); else root.removeAttribute("data-theme");
  localStorage.setItem("qrforge-theme", dark?"dark":"light");
}
setTheme(localStorage.getItem("qrforge-theme")==="dark" ||
  (!localStorage.getItem("qrforge-theme") && matchMedia("(prefers-color-scheme: dark)").matches));
$("themeBtn").onclick=()=> setTheme(root.getAttribute("data-theme")!=="dark");
$("langBtn").onclick=()=>{ lang = lang==="en"?"zh":"en"; applyLang(); };

applyLang(); syncHex(); draw();
})();
