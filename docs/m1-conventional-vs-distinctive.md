# M1 conventional versus distinctive boundaries

## Purpose

Originality is an overall product-system property. Do not reinvent correct Shopify commerce/accessibility primitives merely to look novel.

## Keep conventional and correct

Navigation, search, product forms, option controls, price/status, media semantics, cart truth, collection filtering/sorting/pagination, dialogs/disclosures, localization/Markets, responsive images, accessibility semantics, app-block contracts, theme-editor lifecycle and required platform resources should follow current Shopify-native and accessible patterns.

These primitives may be visually distinctive, but behavior must remain predictable.

## Where the product must earn distinction

### 1. Beauty/Wellness visual system
A coherent, recognizable art direction and commerce presentation that does not depend solely on demo photography.

### 2. High-value structural flexibility
A bounded set of materially different compositions for surfaces brands repeatedly redesign, especially PDP purchase area, product media, cart and selected content surfaces.

### 3. Agency-informed control selection
Expose controls justified by recurring real customization demand rather than every possible implementation knob.

### 4. Merchant-operable outcomes
Once a supported composition exists, ordinary content/data/variant changes should be safely operable without source edits.

### 5. Clean developer extensibility
When bespoke work is required, narrow contracts, modular assets and predictable styling should make extension straightforward.

### 6. Premium defaults
Standard Shopify data must look complete. Optional structured data enhances the result rather than unlocking basic quality.

### 7. Mobile composition quality
Mobile behavior is explicitly designed around commerce/content priority rather than desktop collapse or merchant-managed duplicate pages.

## Decision test for a proposed feature/control

1. Is it required for platform, commerce, accessibility or content correctness? Use the conventional contract.
2. Is it supported by repeated target-merchant/design/agency need? If not, do not expose it merely for flexibility.
3. Does it create materially different useful output or only cosmetic permutations?
4. Is the responsibility already owned by a global token, surface variant or block?
5. Can Shopify-native templates/sections/blocks/settings/dynamic sources express it cleanly?
6. Does it add app dependency, fabricated claims, inaccessible novelty, avoidable payload or support-heavy combinations? Reject it.
7. Would an experienced merchant understand the consequence from the setting name/help text?
8. Would a developer still be able to extend the system without undoing it?

## Anti-patterns

- one section with every layout/content/breakpoint setting;
- one template per campaign permutation;
- vertical-mode switches;
- mandatory metafield setup for baseline polish;
- copying competitor taxonomy and restyling it;
- arbitrary CSS/pixel/breakpoint controls as normal merchant UX;
- app-specific workflow ownership;
- deep nesting without demonstrated need;
- claiming originality from terminology, section count, theme blocks, presets, metafields, Rollouts compatibility or JSON order.

## Gate

The assembled system must demonstrate target-vertical visual identity plus meaningful structural range on the high-value surfaces without settings-panel explosion. It must preserve premium zero-setup states, merchant operability and clean developer extension.

If it cannot, narrow or reject the architecture rather than adding more controls.
