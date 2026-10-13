#!/usr/bin/env python3
"""Patch app.js: add 8 languages, logo FAQ, 10-lang detection, select picker, RTL."""
import json, os, subprocess

os.chdir("/home/hatch/workspace/qr-site/tools")
subprocess.run(["python3", "i18n10a.py"], check=True)
subprocess.run(["python3", "i18n10b.py"], check=True)
p1 = json.loads(open("/tmp/i18n_part1.json").read())
p2 = json.loads(open("/tmp/i18n_part2.json").read())

APP = "/home/hatch/workspace/qr-site/assets/js/app.js"
s = open(APP).read()

# 1. en: SEO-tuned title/meta + logo FAQ
s = s.replace(
  'title:"FreeQrly — QR Code Generator, Private by Design",\n  metaDesc:"FreeQrly is a free QR code generator that runs entirely in your browser. No sign-up, no tracking, no expiry. Export PNG & SVG.",',
  'title:"Free QR Code Generator — No Sign-Up, No Expiry | FreeQrly",\n  metaDesc:"FreeQrly is a free QR code generator that runs entirely in your browser — even with your logo. No sign-up, no tracking, no expiry. Export PNG & SVG.",')
s = s.replace(
  'q6:"Do I need an account?",a6:"No. There is nothing to sign up for — open the page and make your code.",\n  fin:"Made quietly, in your browser.",',
  'q6:"Do I need an account?",a6:"No. There is nothing to sign up for — open the page and make your code.",\n  q7:"Can I add my logo to the QR code?",a7:"Yes — upload any square logo and it goes in the center, with error correction raised automatically so it keeps scanning. For print, use Q or H.",\n  fin:"Made quietly, in your browser.",')

# 2. zh: logo FAQ
s = s.replace(
  'q6:"需要注册账号吗？",a6:"不需要。这里没有什么可注册的——打开页面，直接做码。",\n  fin:"在你的浏览器里，静静生成。",',
  'q6:"需要注册账号吗？",a6:"不需要。这里没有什么可注册的——打开页面，直接做码。",\n  q7:"二维码中间能加我的 Logo 吗？",a7:"可以。上传一张方形 Logo，它会放在正中央，容错等级会自动提高以保证可扫。用来印刷的话，建议选 Q 或 H 容错。",\n  fin:"在你的浏览器里，静静生成。",')

# 3. append 8 languages before the end of I18N
tail_old = '["lng","经度","116.4074"]]}\n}};'
assert tail_old in s, "I18N tail not found"
new_langs = ",\n".join([p1["es"], p1["pt"], p1["fr"], p1["de"],
                        p2["ja"], p2["ru"], p2["hi"], p2["ar"]])
s = s.replace(tail_old, '["lng","经度","116.4074"]]}},\n' + new_langs + '\n};')

# 4. replace language detection block
old_detect = '''let lang = "en";
/* language: ?lang= > saved choice > timezone hint > IP geolocation > browser language */
function syncGuess(){
  const q = new URLSearchParams(location.search).get("lang");
  if(q==="en"||q==="zh") return q;
  const saved = localStorage.getItem("freeqrly-lang");
  if(saved==="en"||saved==="zh") return saved;
  try{
    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone||"";
    if(/Asia\\/(Shanghai|Taipei|Hong_Kong|Macau|Urumqi|Chongqing)/.test(tz)) return "zh";
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
}'''
new_detect = '''const LANGS = ["en","zh","es","hi","ar","pt","fr","ru","de","ja"];
const LANGN = {en:"English",zh:"\\u4e2d\\u6587",es:"Espa\\u00f1ol",hi:"\\u0939\\u093f\\u0928\\u094d\\u0926\\u0940",ar:"\\u0627\\u0644\\u0639\\u0631\\u0628\\u064a\\u0629",pt:"Portugu\\u00eas",fr:"Fran\\u00e7ais",ru:"\\u0420\\u0443\\u0441\\u0441\\u043a\\u0438\\u0439",de:"Deutsch",ja:"\\u65e5\\u672c\\u8a9e"};
const LANGBCP = {en:"en",zh:"zh-CN",es:"es",hi:"hi",ar:"ar",pt:"pt",fr:"fr",ru:"ru",de:"de",ja:"ja"};
const GEO2LANG = {CN:"zh",HK:"zh",TW:"zh",MO:"zh",ES:"es",MX:"es",AR:"es",CO:"es",CL:"es",PE:"es",VE:"es",EC:"es",GT:"es",CU:"es",BO:"es",DO:"es",HN:"es",PY:"es",SV:"es",NI:"es",CR:"es",PA:"es",UY:"es",BR:"pt",PT:"pt",AO:"pt",MZ:"pt",FR:"fr",BE:"fr",SN:"fr",CI:"fr",DE:"de",AT:"de",JP:"ja",IN:"hi",SA:"ar",EG:"ar",AE:"ar",DZ:"ar",MA:"ar",IQ:"ar",RU:"ru",BY:"ru"};
const TZ2LANG = {"Asia/Shanghai":"zh","Asia/Taipei":"zh","Asia/Hong_Kong":"zh","Asia/Macau":"zh","Asia/Urumqi":"zh","America/Mexico_City":"es","America/Bogota":"es","America/Lima":"es","America/Santiago":"es","America/Argentina/Buenos_Aires":"es","Europe/Madrid":"es","America/Sao_Paulo":"pt","Europe/Lisbon":"pt","Europe/Paris":"fr","Europe/Berlin":"de","Europe/Vienna":"de","Asia/Tokyo":"ja","Asia/Kolkata":"hi","Asia/Dubai":"ar","Asia/Riyadh":"ar","Africa/Cairo":"ar"};
let lang = "en";
/* language: ?lang= > saved choice > timezone hint > IP geolocation > browser language */
function syncGuess(){
  const q = new URLSearchParams(location.search).get("lang");
  if(q && LANGS.includes(q)) return q;
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
}'''
assert old_detect in s, "detect block not found"
s = s.replace(old_detect, new_detect)

# 5. applyLang: bcp47 + rtl + select population
old_apply = '''function applyLang(){
  document.documentElement.lang = lang==="zh" ? "zh-CN" : "en";'''
new_apply = '''function applyLang(){
  document.documentElement.lang = LANGBCP[lang]||"en";
  document.documentElement.dir = lang==="ar" ? "rtl" : "ltr";'''
assert old_apply in s, "applyLang head not found"
s = s.replace(old_apply, new_apply)

old_btn = '''  $("langBtn").textContent = lang==="en" ? "中文" : "EN";'''
new_btn = '''  const _sel = $("langBtn");
  if(_sel && _sel.tagName==="SELECT"){
    if(!_sel.options.length) LANGS.forEach(c=>{ const o=document.createElement("option"); o.value=c; o.textContent=LANGN[c]; _sel.appendChild(o); });
    _sel.value = lang;
  } else if(_sel){ _sel.textContent = LANGN[lang]||lang; }'''
assert old_btn in s, "langBtn text not found"
s = s.replace(old_btn, new_btn)

# 6. langBtn init: toggle -> select change
old_init = '''$("langBtn").onclick=()=>{ lang = lang==="en"?"zh":"en"; applyLang(); };'''
new_init = '''(function(){ const b=$("langBtn"); if(!b) return;
  if(b.tagName==="SELECT"){ b.addEventListener("change",e=>{ lang=e.target.value; applyLang(); }); }
  else { b.onclick=()=>{ const i=LANGS.indexOf(lang); lang=LANGS[(i+1)%LANGS.length]; applyLang(); }; }
})();'''
assert old_init in s, "langBtn init not found"
s = s.replace(old_init, new_init)

open(APP, "w").write(s)
print("patched OK, size:", len(s))
