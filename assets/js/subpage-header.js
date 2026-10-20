/* Shared header bootstrap for static subpages (about, scan, developers,
   barcode, blog, privacy, terms, 404, login, reset).
   Detects the page language from the URL prefix, renders the shared
   site header with translated chrome (nav + account menu), restores
   the cached account instantly, revalidates it in the background, and
   switches language by navigating to the same page in that language. */
(function () {
  var LANGS = ["en", "zh", "es", "hi", "ar", "pt", "fr", "ru", "de", "ja"];
  var LANGN = { en: "English", zh: "中文", es: "Español", hi: "हिन्दी", ar: "العربية", pt: "Português", fr: "Français", ru: "Русский", de: "Deutsch", ja: "日本語" };
  // [Home, Scanner, FAQ] — same labels as the homepage nav (app.js I18N).
  var NAV_T = {
    en: ["Home", "Scanner", "FAQ"],
    zh: ["首页", "扫码", "常见问题"],
    es: ["Inicio", "Escáner", "Preguntas"],
    hi: ["स्टूडियो", "स्कैनर", "सवाल"],
    ar: ["الاستوديو", "ماسح", "أسئلة"],
    pt: ["Estúdio", "Scanner", "Perguntas"],
    fr: ["Studio", "Scanner", "Questions"],
    ru: ["Студия", "Сканер", "Вопросы"],
    de: ["Studio", "Scanner", "Fragen"],
    ja: ["スタジオ", "スキャナー", "よくある質問"]
  };
  // Header chrome strings, mirroring app.js I18N (signin + account menu).
  var T = {
    en: { signin: "Sign in", acctDashboard: "Dashboard", acctExport: "Export my data", acctDelete: "Delete account", acctLogout: "Log out", acctSignedInWith: "Signed in with {method}", acctDeleteConfirm: "Delete your account? This cannot be undone.", acctDeleteFailed: "Couldn't delete the account. Please try again.", acctNetErr: "Network error. Please try again." },
    zh: { signin: "登录", acctDashboard: "Dashboard", acctExport: "导出我的数据", acctDelete: "删除账号", acctLogout: "退出登录", acctSignedInWith: "通过{method}登录", acctDeleteConfirm: "确定删除账号吗？此操作无法撤销。", acctDeleteFailed: "删除失败，请重试。", acctNetErr: "网络错误，请重试。" },
    es: { signin: "Iniciar sesión", acctDashboard: "Dashboard", acctExport: "Exportar mis datos", acctDelete: "Eliminar cuenta", acctLogout: "Cerrar sesión", acctSignedInWith: "Sesión con {method}", acctDeleteConfirm: "¿Eliminar tu cuenta? No se puede deshacer.", acctDeleteFailed: "No se pudo eliminar. Inténtalo de nuevo.", acctNetErr: "Error de red. Inténtalo de nuevo." },
    hi: { signin: "साइन इन", acctDashboard: "Dashboard", acctExport: "मेरा डेटा निर्यात करें", acctDelete: "खाता हटाएं", acctLogout: "लॉग आउट", acctSignedInWith: "{method} से लॉग इन", acctDeleteConfirm: "अपना खाता हटाएं? इसे पूर्ववत नहीं किया जा सकता।", acctDeleteFailed: "हटाया नहीं जा सका। पुनः प्रयास करें।", acctNetErr: "नेटवर्क त्रुटि। पुनः प्रयास करें।" },
    ar: { signin: "تسجيل الدخول", acctDashboard: "Dashboard", acctExport: "تصدير بياناتي", acctDelete: "حذف الحساب", acctLogout: "تسجيل الخروج", acctSignedInWith: "تم تسجيل الدخول عبر {method}", acctDeleteConfirm: "حذف حسابك؟ لا يمكن التراجع عن هذا.", acctDeleteFailed: "تعذر الحذف. حاول مجددًا.", acctNetErr: "خطأ في الشبكة. حاول مجددًا." },
    pt: { signin: "Entrar", acctDashboard: "Dashboard", acctExport: "Exportar meus dados", acctDelete: "Excluir conta", acctLogout: "Sair", acctSignedInWith: "Sessão com {method}", acctDeleteConfirm: "Excluir sua conta? Não pode ser desfeito.", acctDeleteFailed: "Não foi possível excluir. Tente novamente.", acctNetErr: "Erro de rede. Tente novamente." },
    fr: { signin: "Se connecter", acctDashboard: "Dashboard", acctExport: "Exporter mes données", acctDelete: "Supprimer le compte", acctLogout: "Se déconnecter", acctSignedInWith: "Connecté via {method}", acctDeleteConfirm: "Supprimer votre compte ? Irréversible.", acctDeleteFailed: "Suppression impossible. Réessayez.", acctNetErr: "Erreur réseau. Réessayez." },
    ru: { signin: "Войти", acctDashboard: "Dashboard", acctExport: "Экспортировать мои данные", acctDelete: "Удалить аккаунт", acctLogout: "Выйти", acctSignedInWith: "Вход через {method}", acctDeleteConfirm: "Удалить аккаунт? Это необратимо.", acctDeleteFailed: "Не удалось удалить. Попробуйте ещё раз.", acctNetErr: "Ошибка сети. Попробуйте ещё раз." },
    de: { signin: "Anmelden", acctDashboard: "Dashboard", acctExport: "Meine Daten exportieren", acctDelete: "Konto löschen", acctLogout: "Abmelden", acctSignedInWith: "Angemeldet mit {method}", acctDeleteConfirm: "Konto wirklich löschen? Kann nicht rückgängig gemacht werden.", acctDeleteFailed: "Löschen fehlgeschlagen. Bitte erneut versuchen.", acctNetErr: "Netzwerkfehler. Bitte erneut versuchen." },
    ja: { signin: "ログイン", acctDashboard: "Dashboard", acctExport: "データをエクスポート", acctDelete: "アカウントを削除", acctLogout: "ログアウト", acctSignedInWith: "{method}でログイン中", acctDeleteConfirm: "アカウントを削除しますか？元に戻せません。", acctDeleteFailed: "削除できませんでした。もう一度お試しください。", acctNetErr: "ネットワークエラー。もう一度お試しください。" }
  };
  var path = location.pathname;
  var m = path.match(/^\/(zh|es|hi|ar|pt|fr|ru|de|ja)(\/.*)?$/);
  var lang = m ? m[1] : "en";
  var enPath = m ? (m[2] || "/") : path;
  var prefix = lang === "en" ? "" : "/" + lang;
  var nav = NAV_T[lang] || NAV_T.en;
  var table = T[lang] || T.en;
  function tr(k) { return table[k] || k; }

  function getCachedUser() {
    try {
      var c = localStorage.getItem("freeqrly-user");
      if (!c) return null;
      var u = JSON.parse(c);
      return (u && u.email) ? u : null;
    } catch (e) { return null; }
  }

  if (window.initSiteHeader) {
    window.initSiteHeader({
      nav: [
        { href: prefix + "/", text: nav[0] },
        { href: prefix + "/scan/", text: nav[1] },
        { href: prefix + "/#faq", text: nav[2] }
      ],
      t: tr,
      lang: lang,
      langs: LANGS,
      langNames: LANGN,
      onLangChange: function (code) {
        try { localStorage.setItem("freeqrly-lang", code); } catch (e) {}
        location.href = (code === "en" ? enPath : "/" + code + enPath);
      },
      user: getCachedUser(),
      showDashboard: true
    });
  }

  // Revalidate auth in background; update the header if the state changed.
  fetch("/api/auth/me", { credentials: "same-origin" }).then(function (r) {
    return r.json().catch(function () { return {}; });
  }).then(function (d) {
    var me = d.user || null;
    var user = (me && me.email) ? { email: me.email, name: me.name, avatar: me.avatar || me.avatar_url || null, authMethod: me.authMethod } : null;
    try {
      if (user) localStorage.setItem("freeqrly-user", JSON.stringify(user));
      else localStorage.removeItem("freeqrly-user");
    } catch (e) {}
    if (window.renderSiteHeader) window.renderSiteHeader({ user: user });
  }).catch(function () {});
})();
