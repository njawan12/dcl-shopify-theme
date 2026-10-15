/* Theme editor only: when a merchant selects an image detail block, open its popover
   so edits are visible in the preview. Not loaded on the live storefront. */
const toggle = (event, open) => {
  const note = event.target.querySelector?.('[popover]');
  if (!note || typeof note.showPopover !== 'function') return;
  try {
    if (open) note.showPopover();
    else note.hidePopover();
  } catch (error) {
    /* The popover was already in the requested state. */
  }
};
document.addEventListener('shopify:block:select', (event) => toggle(event, true));
document.addEventListener('shopify:block:deselect', (event) => toggle(event, false));
