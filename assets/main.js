document.querySelectorAll('[data-year]').forEach((element) => { element.textContent = new Date().getFullYear(); });
const copyButton = document.querySelector('[data-copy-email]');
const copyStatus = document.querySelector('[data-copy-status]');
if (copyButton && copyStatus) {
  copyButton.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText('sideforgeapps@gmail.com');
      copyStatus.textContent = 'Email address copied.';
    } catch {
      copyStatus.textContent = 'Copy failed. Select the email address beside this button and copy it manually.';
    }
  });
}
