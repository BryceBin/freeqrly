/* Browser-local vCard 3.0 serialization and legacy-card compatibility. */
(function(root){
"use strict";
function escapeText(value){
  return String(value||"").replace(/\\/g,"\\\\").replace(/\r\n|\r|\n/g,"\\n").replace(/;/g,"\\;").replace(/,/g,"\\,");
}
function fold(line){
  const encoder=new TextEncoder();
  let result="",bytes=0;
  for(const char of line){
    const size=encoder.encode(char).length;
    if(bytes+size>75){result+="\r\n ";bytes=1;}
    result+=char;bytes+=size;
  }
  return result;
}
function serialize(lines){return lines.map(fold).join("\r\n")+"\r\n";}
function build(contact){
  const name=String(contact.name||contact.phone||contact.email||"Contact").trim()||"Contact";
  const lines=["BEGIN:VCARD","VERSION:3.0","N:;"+escapeText(name)+";;;","FN:"+escapeText(name)];
  if(contact.phone) lines.push("TEL;TYPE=CELL:"+String(contact.phone).replace(/[\r\n]/g,""));
  if(contact.email) lines.push("EMAIL;TYPE=INTERNET:"+escapeText(contact.email));
  lines.push("END:VCARD");
  return serialize(lines);
}
function isVCard(data){return /^BEGIN:VCARD\r?\n[\s\S]*\r?\nEND:VCARD$/i.test(String(data||"").trim());}
function normalize(data){
  if(!isVCard(data)) throw new Error("Not a vCard");
  const lines=String(data).trim().replace(/\r\n|\r/g,"\n").replace(/\n[ \t]/g,"").split("\n");
  // Repair only a single legacy 3.0 card; preserve other versions and all fields.
  if(lines.filter(line=>/^BEGIN:VCARD$/i.test(line)).length===1 && lines.some(line=>/^VERSION:3\.0$/i.test(line))){
    const n=lines.findIndex(line=>/^N(?:;[^:]*)?:/i.test(line));
    const fn=lines.findIndex(line=>/^FN(?:;[^:]*)?:/i.test(line));
    if(n>=0 && !lines[n].slice(lines[n].indexOf(":")+1).includes(";")) lines[n]+=";;;;";
    if(fn<0){
      const name=n>=0 ? lines[n].slice(lines[n].indexOf(":")+1).split(";").filter(Boolean).join(" ") : "Contact";
      lines.splice(2,0,"FN:"+(name||"Contact"));
    }
    if(n<0){
      const name=lines.find(line=>/^FN(?:;[^:]*)?:/i.test(line));
      lines.splice(2,0,"N:;"+name.slice(name.indexOf(":")+1)+";;;");
    }
  }
  return serialize(lines);
}
const api={build,normalize,isVCard};
root.FreeQrlyVCard=api;
if(typeof module==="object" && module.exports) module.exports=api;
})(typeof globalThis!=="undefined"?globalThis:this);
