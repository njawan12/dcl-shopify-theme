/* Only request Shopify's model UI when a model is actually present. */
class ProductModel extends HTMLElement {
  connectedCallback() {
    if (this.viewer || !window.Shopify?.loadFeatures) return;
    window.Shopify.loadFeatures([{ name: 'model-viewer-ui', version: '1.0', onLoad: (error) => {
      if (!error && this.isConnected && !this.viewer && window.Shopify.ModelViewerUI) {
        this.viewer = new window.Shopify.ModelViewerUI(this.querySelector('model-viewer'));
      }
    } }]);
  }
  disconnectedCallback() { this.viewer?.destroy?.(); this.viewer = null; }
}
if (!customElements.get('product-model')) customElements.define('product-model', ProductModel);
