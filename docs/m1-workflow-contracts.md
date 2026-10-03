# M1 surface contracts

## Status

This document supersedes the former workflow contracts. Product Launch, Paid Landing Page, Collection Launch, Editorial Story and Product Education are no longer controlling architecture.

Merchant-facing architecture is organized around Shopify-native surfaces and narrow content primitives.

## Contract rule

Every surface/component specification must declare:

- primary shopper/merchant purpose;
- supported Shopify resource/context;
- standard-data requirements and zero-setup fallback;
- optional dynamic-source connections;
- allowed blocks and useful maximums;
- structural variants and why each exists;
- global vs local controls;
- mobile priority/order;
- empty/long/localized content behavior;
- accessibility semantics;
- media/loading behavior;
- app-block seam where appropriate;
- extension boundary;
- setting-count budget.

Reject a component if its purpose requires the word "anything", if it owns unrelated jobs, or if its default is empty until merchants configure several blocks.

## Surface contracts

### Product purchase area
Owns product facts, option selection, quantity, selling-plan/native app seams, availability and purchase action. Structural variants may change composition, not commerce truth.

### Product media
Owns product media presentation, media navigation and objective badge placement. Must support one/no/many and mixed media safely.

### Product education
Owns optional benefits, usage, ingredients/materials/specifications, FAQ, honest comparison and proof/results presentation. No fabricated claims.

### Product card
Owns product identity, media, price/status, supported option cues and purchase/discovery action without impersonating non-products.

### Collection merchandising
Owns collection orientation, canonical products, filter/sort/pagination and clearly non-product promotional/story interruptions.

### Cart
Owns accurate cart state, quantity/update/remove, totals, errors, properties, selling-plan display, factual configured progress messaging and bounded complementary merchandising.

### Storytelling/content
Narrow primitives answer one content question at a time. No universal section.

### Navigation/search
Use conventional accessible platform semantics. Visual quality matters; novelty must not break predictable interaction.

## Control hierarchy

1. global semantic tokens;
2. owning-surface structural variant;
3. block composition/order;
4. dynamic product/content data;
5. bounded local presentation;
6. developer extension.

A lower layer must not duplicate responsibility owned by a higher layer.

## Internal CRO review

Reveal / Explain / Prove / Compare / Act may be used by DCL as an internal critique lens for information hierarchy. It is not schema, merchant terminology, a required sequence or an originality claim.
