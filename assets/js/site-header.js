/* Shared site header — brand left, nav center, account + language + theme right.
 * Usage:
 *   <div id="siteHeader"></div>
 *   <script src="/assets/js/acct-menu.js"></script>
 *   <script src="/assets/js/site-header.js"></script>
 *   <script>
 *     initSiteHeader({
 *       nav: [{href:'/#studio', text:'Studio'}, ...],  // text may be pre-translated
 *       t: k => ...,            // translator for header chrome (signin)
 *       lang: 'en',             // current language code
 *       langs: ['en','zh',...],// available languages
 *       langNames: {en:'English', zh:'中文', ...},
 *       onLangChange: code => {...},
 *       user: null | {email,name,avatar,authMethod},  // null => show Sign in
 *       showDashboard: true     // show Dashboard link in account menu
 *     });
 *   </script>
 * Call window.renderSiteHeader() after language change to retranslate.
 */
(function(){
  var cfg = null;

  function esc(s){
    return String(s == null ? '' : s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  function render(){
    if(!cfg) return;
    var mount = document.getElementById('siteHeader');
    if(!mount) return;
    var t = cfg.t || function(k){ return k; };

    var navH = (cfg.nav || []).map(function(n){
      return '<a href="' + esc(n.href) + '">' + esc(n.text) + '</a>';
    }).join('');

    var acctH;
    if(cfg.user && cfg.user.email){
      acctH = '<span class="shAcctMount"></span>';
    }else{
      acctH = '<a class="shSignin" href="/login/">' + esc(t('signin')) + '</a>';
    }

    var langH = '<select class="shLang" aria-label="Language">' +
      (cfg.langs || ['en']).map(function(c){
        var name = (cfg.langNames && cfg.langNames[c]) || c;
        return '<option value="' + esc(c) + '"' + (c === cfg.lang ? ' selected' : '') + '>' + esc(name) + '</option>';
      }).join('') + '</select>';

    mount.innerHTML =
      '<header class="sh">' +
        '<a class="shBrand" href="/">Free<em>Qrly</em></a>' +
        '<nav class="shNav">' + navH + '</nav>' +
        '<div class="shRight">' + acctH + langH +
          '<button class="shTheme" type="button" aria-label="theme">\u25D0</button>' +
        '</div>' +
      '</header><div class="shLine"></div>';

    // Theme toggle (shared logic)
    var root = document.documentElement;
    function setTheme(dark){
      if(dark) root.setAttribute('data-theme','dark'); else root.removeAttribute('data-theme');
      try{ localStorage.setItem('freeqrly-theme', dark ? 'dark' : 'light'); }catch(e){}
    }
    try{
      if(localStorage.getItem('freeqrly-theme') === 'dark') root.setAttribute('data-theme','dark');
    }catch(e){}
    mount.querySelector('.shTheme').addEventListener('click', function(){
      setTheme(root.getAttribute('data-theme') !== 'dark');
    });

    // Language change
    var sel = mount.querySelector('.shLang');
    sel.addEventListener('change', function(){
      if(cfg.onLangChange) cfg.onLangChange(sel.value);
    });

    // Account menu
    if(cfg.user && cfg.user.email && window.initAcctMenu){
      window.initAcctMenu({
        mount: mount.querySelector('.shAcctMount'),
        user: cfg.user,
        t: t,
        showDashboard: !!cfg.showDashboard,
        onDelete: cfg.onDelete
      });
    }
  }

  window.initSiteHeader = function(opts){
    cfg = opts || {};
    render();
  };
  // Re-render (e.g. after language switch retranslates nav labels).
  // Pass a partial opts to update before re-rendering.
  window.renderSiteHeader = function(opts){
    if(opts) cfg = Object.assign({}, cfg, opts);
    render();
  };
})();
