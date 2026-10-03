(() => {
  let savedTheme = null;
  try {
    savedTheme = localStorage.getItem('bavly-theme');
  } catch (_) {
    // Storage may be unavailable in private or restricted browsing contexts.
  }
  document.documentElement.dataset.theme = savedTheme || 'dark';
})();
