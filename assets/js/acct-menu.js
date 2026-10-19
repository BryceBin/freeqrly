/* Shared account dropdown menu — used by homepage and dashboard.
 * Usage: window.initAcctMenu({ mount, user, t, showDashboard })
 *   mount: element to render into (replaced content)
 *   user: { email, name, avatar (url or null), authMethod }
 *   t: function(key) -> translated string
 *   showDashboard: bool — include the "Dashboard" link (homepage only)
 *   onDelete: optional custom delete handler; default uses confirm()+alert()
 * The menu re-renders via window.renderAcctMenu() on language switch.
 */
(function(){
  var PROVIDER_LABEL = { password: 'Email', email: 'Email', google: 'Google', github: 'GitHub' };
  function esc(s){
    return String(s == null ? '' : s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  function menuHTML(user, t, showDashboard){
    var prov = PROVIDER_LABEL[user.authMethod] || 'Email';
    var h = '<div class="amHead"><div class="amEmail">' + esc(user.email) + '</div>' +
      '<div class="amProv">' + esc(t('acctSignedInWith').replace('{method}', prov)) + '</div></div>' +
      '<div class="amSep"></div>';
    if(showDashboard) h += '<a href="/dashboard/" role="menuitem">' + esc(t('acctDashboard')) + '</a>';
    h += '<button type="button" data-act="export" role="menuitem">' + esc(t('acctExport')) + '</button>' +
      '<button type="button" class="amDanger" data-act="delete" role="menuitem">' + esc(t('acctDelete')) + '</button>' +
      '<div class="amSep"></div>' +
      '<button type="button" data-act="logout" role="menuitem">' + esc(t('acctLogout')) + '</button>';
    return h;
  }

  window.initAcctMenu = function(opts){
    var mount = opts.mount, user = opts.user, t = opts.t;
    if(!mount || !user) return;
    var displayName = user.name || user.email;
    var av = user.avatar
      ? '<img class="amAvatar" src="' + esc(user.avatar) + '" alt="" referrerpolicy="no-referrer">'
      : '<span class="amAvatar amAvatarLetter">' + esc(displayName.trim().charAt(0).toUpperCase()) + '</span>';
    mount.innerHTML =
      '<span class="amWrap"><button class="amTrigger" type="button" aria-haspopup="menu">' + av +
      '<span class="amName">' + esc(displayName) + '</span></button>' +
      '<span class="amMenu" role="menu"></span></span>';

    var wrap = mount.querySelector('.amWrap');
    wrap._amUser = user; wrap._amT = t; wrap._amShowDash = !!opts.showDashboard;

    window.renderAcctMenu = function(){
      var w = document.querySelector('.amWrap');
      if(!w || !w._amUser) return;
      var m = w.querySelector('.amMenu');
      if(m) m.innerHTML = menuHTML(w._amUser, w._amT, w._amShowDash);
    };
    window.renderAcctMenu();

    wrap.querySelector('.amTrigger').addEventListener('click', function(e){
      e.stopPropagation();
      wrap.classList.toggle('open');
    });
    document.addEventListener('click', function(e){
      if(!e.target.closest('.amWrap')) wrap.classList.remove('open');
    });
    wrap.querySelector('.amMenu').addEventListener('click', function(e){
      var btn = e.target.closest('[data-act]');
      if(!btn || btn.disabled) return;
      var act = btn.getAttribute('data-act');
      var tt = wrap._amT;
      if(act === 'export'){ location.href = '/api/auth/export'; return; }
      if(act === 'logout'){
        btn.disabled = true; btn.style.opacity = '.55'; btn.style.pointerEvents = 'none';
        fetch('/api/auth/logout', { method: 'POST', credentials: 'same-origin' })
          .catch(function(){})
          .then(function(){ location.href = '/login/'; });
        return;
      }
      if(act === 'delete'){
        if(opts.onDelete){ opts.onDelete(wrap._amT); return; }
        if(!confirm(tt('acctDeleteConfirm'))) return;
        fetch('/api/auth/delete-account', { method: 'POST', credentials: 'same-origin' })
          .then(function(r){ return r.json().catch(function(){ return {}; }).then(function(d){ return {ok:r.ok, d:d}; }); })
          .then(function(res){
            if(!res.ok){ alert(res.d.error || tt('acctDeleteFailed')); return; }
            location.href = '/';
          })
          .catch(function(){ alert(tt('acctNetErr')); });
      }
    });
  };
})();
