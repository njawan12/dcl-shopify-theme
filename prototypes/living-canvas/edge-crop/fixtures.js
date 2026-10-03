window.EDGE_CROP_FIXTURES = {
  beauty: {
    label: 'Art-directed lifestyle', eyebrow: 'Botanical study 04', heading: 'Care that begins at the source.',
    body: 'A focused daily formula, made with traceable plant oils and designed to leave skin comfortable—not coated.',
    action: 'Read the field notes', image: 'media/lifestyle-wide.svg', mobileImage: 'media/lifestyle-tall.svg',
    alt: 'Amber glass skincare bottles on folded fabric', hotspots: ['origin', 'product']
  },
  packshot: {
    label: 'Ordinary white-background packshot', eyebrow: 'Daily essentials', heading: 'One bottle. A deliberate edge.',
    body: 'The composition must hold when the merchant supplies a centered catalog image rather than campaign photography.',
    action: 'Explore the formula', image: 'media/packshot.svg', mobileImage: null,
    alt: 'Amber pump bottle centered on a white background', hotspots: ['origin', 'product']
  },
  'long-copy': {
    label: 'Long heading and body', eyebrow: 'A deliberately expanded editorial test',
    heading: 'A considered everyday ritual for skin that changes with weather, travel, time, and everything in between.',
    body: 'This intentionally long merchant-authored paragraph tests whether the readable zone can expand without colliding with the media, clipping the call to action, or forcing words into an uncomfortably narrow measure. It also approximates translation expansion while keeping the source order intact and the complete proposition available at every viewport.',
    action: 'Discover our sourcing and formulation approach', image: 'media/lifestyle-wide.svg', mobileImage: 'media/lifestyle-tall.svg',
    alt: 'Amber glass skincare bottles on folded fabric', hotspots: ['origin', 'product']
  },
  'one-info': {
    label: 'One information hotspot', eyebrow: 'Material detail', heading: 'The story inside the object.',
    body: 'A single annotation remains legible without making the media feel unfinished.', action: 'Read the field notes',
    image: 'media/lifestyle-wide.svg', mobileImage: 'media/lifestyle-tall.svg', alt: 'Amber glass skincare bottles on folded fabric', hotspots: ['origin']
  },
  'four-mixed': {
    label: 'Four mixed hotspots', eyebrow: 'Four authored anchors', heading: 'Detail, without freeform placement.',
    body: 'Information and commerce share four bounded positions. At narrow widths they resolve into the same ordered keyed list.',
    action: 'Explore the collection', image: 'media/lifestyle-wide.svg', mobileImage: 'media/lifestyle-tall.svg',
    alt: 'Amber glass skincare bottles on folded fabric', hotspots: ['origin', 'product', 'packaging', 'soldout']
  },
  'missing-product': {
    label: 'Missing product target', eyebrow: 'Broken reference test', heading: 'A missing target leaves no empty floating UI.',
    body: 'The deleted product is omitted, leaving the remaining merchant-authored information intact without a dead destination.',
    action: 'Continue reading', image: 'media/packshot.svg', mobileImage: null, alt: 'Amber pump bottle centered on a white background', hotspots: ['origin'],
    diagnostic: 'Harness diagnostic: the missing product reference has no merchant-authored fallback, so no product hotspot is rendered.'
  },
  'no-mobile': {
    label: 'No mobile-specific image', eyebrow: 'One source, two compositions', heading: 'The crop adapts without a duplicate download.',
    body: 'When no mobile image is supplied, the desktop source is reframed by CSS instead of requested twice.',
    action: 'See the media strategy', image: 'media/lifestyle-wide.svg', mobileImage: null,
    alt: 'Amber glass skincare bottles on folded fabric', hotspots: ['origin', 'product']
  },
  minimal: {
    label: 'Minimal content', eyebrow: '', heading: 'Essential, still intentional.', body: '', action: '',
    image: 'media/packshot.svg', mobileImage: null, alt: 'Amber pump bottle centered on a white background', hotspots: []
  },
  neutral: {
    label: 'Neutral originality torture', eyebrow: 'Object study 01', heading: 'A useful object, clearly presented.',
    body: 'Generic product information occupies the same bounded composition without beauty language, campaign photography, decorative type, or brand-led color.',
    action: 'View object details', image: 'media/neutral-object.svg', mobileImage: null,
    alt: 'Plain dark rectangular object centered on a white background', hotspots: ['material', 'genericProduct'], neutral: true
  }
};

window.EDGE_CROP_HOTSPOTS = {
  origin: { anchor: 'upper-left', kind: 'info', label: 'ingredient origin details', kicker: 'Ingredient note', title: 'Cold-pressed seed oil', body: 'Sourced from a single grower cooperative and pressed without added fragrance.' },
  product: { anchor: 'lower-right', kind: 'product', label: 'Daily Field Oil product details', kicker: 'Featured product', product: { id: 4815162342, handle: 'daily-field-oil', title: 'Daily Field Oil', url: '/products/daily-field-oil', image: 'media/packshot.svg', price: '$48.00', compareAtPrice: '$56.00', available: true } },
  packaging: { anchor: 'upper-right', kind: 'info', label: 'packaging details', kicker: 'Material note', title: 'Glass, designed for reuse', body: 'The bottle is glass; local recycling rules vary for the pump.' },
  soldout: { anchor: 'lower-left', kind: 'product', label: 'Night Field Balm product details', kicker: 'Featured product', product: { id: 4815162399, handle: 'night-field-balm', title: 'Night Field Balm', url: '/products/night-field-balm', image: 'media/packshot.svg', price: '$38.00', compareAtPrice: null, available: false } },
  material: { anchor: 'upper-left', kind: 'info', label: 'object material details', kicker: 'Material', title: 'Powder-coated steel', body: 'A durable, generic material specification supplied by the merchant.' },
  genericProduct: { anchor: 'lower-right', kind: 'product', label: 'Utility Object product details', kicker: 'Product', product: { id: 4815162401, handle: 'utility-object', title: 'Utility Object', url: '/products/utility-object', image: 'media/neutral-object.svg', price: '$40.00', compareAtPrice: null, available: true } }
};
