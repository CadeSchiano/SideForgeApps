// Keep the copyright current without making page content depend on JavaScript.
document.querySelectorAll('[data-year]').forEach((element) => {
  element.textContent = new Date().getFullYear();
});
