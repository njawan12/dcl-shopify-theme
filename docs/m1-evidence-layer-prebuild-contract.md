# Evidence Layer pre-build contract

Status: **APPROVED WITH TWO CORRECTIONS**, finalized 2026-10-04. This contract authorizes no implementation, production work or M2.

This contract inherits the existing [M1 Signature System](m1-signature-system.md), [Product Architecture Contract](m1-product-architecture-contract.md), [Surface Contracts](m1-workflow-contracts.md) and [Control-budget Specimen](m1-token-schema-specimen.md). The limits and schemas below were approved for the Evidence Layer pre-build scope. Human corrections clarify structural URL/rendering validity without source-credibility or claim-validity assessment, and preserve an ordered one-step Process Sequence.

## 1. Purpose and named uncertainty

Evidence Layer must prove that a small, reusable proof language can form a recognizable relationship with product media, product education and editorial statements while preserving factual meaning, purchase clarity and merchant usability.

The defining relationship is:

**A clear subject, attached evidence, and visible qualification or provenance where needed.**

Structural identity must survive ordinary media, neutral typography, monochrome and no motion. Evidence must remain understandable without its visual attachment.

Reuse the established semantic tokens, scale contrast, negative space and restrained edge relationships. Do not copy preserved compositions, create another design system or depend on Monument becoming a primary hero.

## 2. Smallest coherent primitive set

**Three narrow primitives**, with one authored presentation each in the first proof. Do not build alternate compositions before this set is reviewed.

| Primitive | Content it owns | Required attachment proof | Why this boundary |
|---|---|---|---|
| **Evidence note** | Metric, fact/specification, qualified claim, certification, testimonial/editorial quote | PDP media and editorial/Living Canvas | These are attributed statements with optional qualification/source. One renderer avoids five near-duplicate components |
| **Evidence pair** | Before/after **or** honest comparison | PDP education | Both require explicit paired subjects and shared context. Separate semantic modes preserve meaning without separate layout engines |
| **Process sequence** | Usage, process or care steps | PDP education and editorial | Ordered instructions need sequence semantics, not claim or comparison semantics |

Each primitive owns one content responsibility. A merchant chooses the appropriate narrow section/block; there is no universal section that switches among every evidence type.

The presentation may inherit a bounded attachment slot from its host. Merchant coordinates, arbitrary overlap, per-device ordering and independent positioning are prohibited. This keeps setup understandable, shares implementation across surfaces and avoids support-heavy combinations.

## 3. Truthful content and source schema

All content must be merchant-supplied or come from a legitimate connected source. A source link does not itself establish truth; the theme presents evidence and never validates claims automatically. The theme must not claim to assess source credibility, factual trustworthiness or merchant claim validity.

**Evidence note: maximum eight content fields**

`Kind`, `Value`, `Label`, `Body`, `Attribution`, `Source title`, `Source URL`, `Qualification`.

Conditional fields remain part of this budget. Kind controls relevant fields and semantic rendering, not arbitrary layout.

| Kind | Minimum valid content | Additional truth requirement |
|---|---|---|
| Metric | Value and explanatory label | Units, scope and relevant context must be explicit in label/body/qualification; no automatic percentages or inferred results |
| Fact/specification | Label and value or body | Correct product/material/ingredient context; no invented ingredients or inferred attributes |
| Claim | Claim body | Merchant must possess support; qualification must state material limits. Unsupported default claims are forbidden |
| Certification | Certification name and attribution to issuer | Scope must identify what is certified. No default seal, invented issuer or implied product-wide endorsement |
| Quote/testimonial | Quote body and attribution | Authentic supplied quotation and appropriate permission; no fabricated customer identity, rating or “verified buyer” status |

Metric qualifications may include sample, timeframe or method where necessary. Certification scope and validity information may be expressed in body/qualification. Do not create a separate provenance settings panel.

**Evidence pair**

Shared content: heading, optional introduction, qualification, source title and source URL.

- **Before/after:** exactly two labelled media records, each containing label, media, alternative text and optional caption. The merchant must supply genuine related material and disclose materially different conditions. No generated transformation may masquerade as product results.
- **Comparison:** exactly two named subjects and up to four comparison rows. Each row contains criterion, left value, right value and optional qualification. Subjects may be products or factual alternatives; no automatic winner, savings calculation or inferred competitor data.

**Process sequence**

Shared content: heading, optional introduction, source title and source URL. Each step has heading, instruction, optional media, alternative text and optional qualification.

Usage must not silently become an efficacy claim. Care/process instructions must identify relevant limitations.

These schemas favour readable authored context over a proprietary evidence database. They remain compatible with ordinary Shopify content and avoid review, certification or scientific-validation engines.

## 4. Manual baseline and optional enhancement

Manual content must produce the complete supported result. No app, metafield or metaobject is required.

Compatible dynamic sources may populate the **same fields**. They change content, never placement or architecture. Use Shopify-supported connections; do not promise that every field accepts every source type.

Legitimate review content belongs in a generic app-block seam. Evidence notes may render editorial/customer quotations, but must never simulate a reviews app or manufacture stars/counts.

This preserves zero-setup usability, native extensibility and a small production boundary.

## 5. Omission, invalidity and disconnection

- Empty optional fields disappear without residual spacing or punctuation.
- A note missing its required content is omitted.
- Missing source fields do not create a “verified” or “sourced” label.
- A disconnected source may use a valid explicitly authored manual fallback. Otherwise omit the affected content; never retain stale connected values silently.
- An incomplete before/after pair is omitted. Do not present one image as a valid pair.
- A comparison without two named subjects or any complete row is omitted. Incomplete rows are removed.
- Invalid process steps are omitted; remaining steps are numbered consecutively. One remaining valid step remains semantically an ordered one-step process, retaining the Process Sequence presentation.
- Invalid optional media is removed while valid text remains.
- Links render only when their URL is structurally valid for the supported field: a well-formed HTTP(S) URL, supported root-relative path or valid same-document fragment, with context-correct attribute escaping. Empty/malformed URLs, unsupported schemes and unresolved same-document fragment targets produce no link; valid text remains. This is URL/rendering validity handling, not an assessment of destination credibility, factual trustworthiness or merchant claim validity. It does not promise remote destination availability.
- When all evidence disappears, the host remains deliberate and complete. Editor diagnostics never appear to shoppers.

The theme can validate required-field completeness and structural rendering validity, not source credibility, factual trustworthiness or merchant claim validity. This boundary prevents misleading UI without introducing moderation or verification services.

## 6. Block caps and complete control budget

| Primitive/context | Maximum content | Initial presentation decisions | Conditional presentation decisions |
|---|---|---|---|
| Evidence notes | 3 notes per attachment | Density; emphasis | 0 |
| Evidence pair | 1 pair; comparison maximum 4 rows | Semantic mode; density; emphasis | 0 |
| Process sequence | 4 steps | Density; emphasis | 0 |
| Generic review-app seam | 1 app block per designated seam in this proof | 0 | 0 |

Semantic mode means before/after or comparison; it is counted as a decision even though it determines content semantics.

Further limits:

- PDP media and Living Canvas accept **one Evidence note group**, maximum three notes.
- The initial PDP education proof may contain one pair and one process sequence as separate narrow sections.
- The editorial proof uses either a note group or a process sequence, rather than stacking every primitive.
- Each repeated note or child record stays within eight content fields.
- Source connections and content fields are inventoried separately from presentation decisions; they are not hidden complexity.
- Density uses existing system choices. Emphasis uses existing semantic schemes.
- Attachment geometry, responsive order, spacing, typography and media containment are theme-owned.
- No additional alignment, width, columns, icon-library, animation, sticky, crop-coordinate or mobile-specific controls.
- Existing host app settings and token decisions must be reused, not duplicated.

These caps sit below the established product-education and storytelling ceilings. They limit merchant decisions, cap DOM/media growth and prevent evidence from overwhelming commerce.

## 7. Desktop and mobile semantic order

One semantic DOM serves every width.

- **PDP media attachment:** subject media, associated notes and qualification/source. Evidence must not enter or reorder the purchase form.
- **Editorial attachment:** editorial statement and relevant media, attached evidence, then any editorial action.
- **Before/after:** heading/context, before item, after item, shared qualification/source.
- **Comparison:** heading/context, named subjects, then each criterion with both values in a consistent reading sequence.
- **Process:** heading/context, ordered steps, then shared source.

Desktop may express attachment through adjacent edges, alignment and bounded asymmetry. Mobile places evidence in normal flow beside its semantic subject in reading order.

No overlay is necessary to understand the relationship. No mobile carousel, duplicated content, positional JavaScript or new sticky owner is permitted. This maintains predictable reading while allowing structural character.

## 8. Accessibility, localization and apps

A static first proof: no before/after slider, disclosure widget or required animation.

Required behaviour:

- Native headings, lists, quotations and comparison semantics appropriate to content.
- Explicit before/after labels plus meaningful alternatives and explanatory captions where required.
- Qualifications remain available to assistive technology and are not decorative microtext.
- No meaning dependent solely on color, position, icons or motion.
- Visible keyboard focus and primary interactive targets at least 44 CSS px.
- No clipped text, fixed content heights or required hover interaction.
- Layout survives 30–50% expansion, long unbroken strings, CJK and bidirectional samples; use logical properties where appropriate.
- Zoom/reflow follows the single-column reading model before collisions occur.
- Dynamic/app content must not be moved into labels, media masks or unsafe overlays.

The app seam sits in ordinary document flow near related content. Insertion, removal, duplication and awkward app height must preserve surrounding order and spacing. No-app state is complete; the theme does not inspect or restyle vendor internals.

Production app-context support, editor lifecycle, assistive-technology testing, cross-browser testing and performance require separate evidence. Prototype inspection cannot certify them.

## 9. Required torture fixtures

Use the same primitives and schema across all fixtures.

| Fixture group | Required challenge |
|---|---|
| Beauty/Wellness | Ordinary product media; supported ingredients/facts, qualified results context and usage |
| Neutral | System sans, accessible monochrome, no motion, ordinary non-beauty rectangular media and generic truthful content |
| Jewelry | Materials, dimensions/provenance and care; no architecture change |
| Food | Ingredients/nutrition/serving or process content; no architecture change |
| Short | Minimal valid note, short pair labels, ordered one-step process |
| Long | Long heading/body, metric context, attribution, source title, comparison values and step instructions |
| Missing/invalid | Zero notes, missing required field, missing image, incomplete pair/row/step, structurally invalid URL/rendering target, disconnected source |
| Maximum | Three notes, four comparison rows, four steps |
| App | Absent, inserted, removed and unusually tall generic guest block |
| Instance isolation | Two instances with independent IDs and content |

Reuse the established eight evidence widths: **320, 375, 390, 430, 768, 1024, 1280 and 1440**. These are test points, not merchant breakpoints.

No invented clinical claims, certifications, reviews or outcomes may be used to make the proof persuasive. Any synthetic fixture data must be explicitly identified as test content.

## 10. Exact verdict criteria

**PASS TO PRESERVE** requires all of the following:

- Human review recognizes a coherent attached-evidence language in neutral PDP and editorial proofs.
- Product scanning, purchase hierarchy and evidence qualifications remain clear.
- All three primitives meet their semantic responsibilities without becoming interchangeable containers.
- Manual content works; missing/disconnected content and absent apps leave coherent hosts.
- Neutral, Jewelry and Food fixtures use the same architecture.
- Block/control caps are met without rescue settings.
- Required width/content checks show no destructive collisions, page overflow, duplicate IDs or corrupted reading order.
- No fabricated proof, duplicated responsive DOM, layout JS or specialist app logic.
- Known untested production gates are explicitly recorded.

**NARROW AND HOLD** applies when truth and engineering remain sound, but signature distinction survives only in a subset of attachment contexts or primitives. Preserve useful conventional education; reduce the signature claim and supported scope. Do not add variants or settings to rescue it.

**FAIL AND KILL** applies when:

- Neutral proof reduces to generic proof widgets with no meaningful attachment relationship.
- Distinction depends on exceptional photography, beauty vocabulary, fonts, color or motion.
- Evidence misleads, hides material qualification or requires unsupported claims.
- Commerce clarity or accessibility is materially harmed.
- Ordinary content requires arbitrary placement, duplicated mobile content, vendor dependency or vertical forks.
- The system needs a universal mega-section or exceeds budgets to remain usable.

Failed evidence must not be rescued by adding animation, ornamental badges, more components or a settings drawer.

## 11. Ordinary education versus signature IP

Ingredient/specification lists, basic comparison tables, labelled before/after media, process instructions, quotes, certification text and app-review hosts remain conventional capabilities.

They qualify as Evidence Layer signature expression only when their **authored attachment to the subject**, shared hierarchy and cross-surface relationships remain recognizable under neutralization.

Accurate content and good accessibility are mandatory quality foundations. They are not, by themselves, originality claims. A useful conventional primitive may remain in product education even if its signature claim is rejected.

## 12. Gate before implementation

Human approval establishes the three primitive boundaries, schemas, caps, host attachments, fixture matrix and verdict criteria above.

Any later implementation brief must name the isolated path, preservation boundaries, exact tests/evidence, complexity report and stop condition. Implementation must stop at **PENDING HUMAN REVIEW**; automated checks cannot award the visual verdict.

Production Shopify integration, source/editor lifecycle, real app compatibility, accessibility certification, cross-browser validation and measured performance remain later gates. Approval of this contract does not authorize M2.
