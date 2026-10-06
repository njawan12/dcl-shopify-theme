/* QR is optional enhancement; the readable native gift code always remains. */
function renderQR() {
  const element = document.querySelector('[data-qr]');
  if (element?.dataset.qr && window.QRCode) {
    new window.QRCode(element, { text: element.dataset.qr, width: 160, height: 160 });
  }
}
if (document.readyState === 'complete') renderQR();
else window.addEventListener('load', renderQR, { once: true });
