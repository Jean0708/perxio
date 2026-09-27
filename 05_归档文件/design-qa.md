# Perxio V05 Design QA

## Evidence

- Source visual truth: `qa-v04-reference-1280x720.png`, `qa-v04-data-reference-1280x720.png`, V04 browser comments 1-6.
- Implementation: `qa-v05-dashboard-1280x720.png`, `qa-v05-data-diagnosis-1280x720.png`.
- Combined comparison: `qa-v04-v05-comparison.png`.
- Viewport: 1280 x 720 CSS px; captured content is 1265 x 712 px after browser scrollbar/chrome exclusion.
- Density normalization: source and implementation captures are equal pixel dimensions and displayed at equal widths in the comparison page.
- States: dashboard default; data processing / AI diagnosis.

## Full-View Comparison

V04 presents a marketing-style global header and long-page sections before or around the product console. V05 opens directly into a persistent Web management shell. Primary navigation now maps to task domains, and dashboard content prioritizes activity status, tasks, samples, current stage and next action.

## Focused Comparison

The data region was checked separately because the user requested a functional data workflow. V04 uses six explanatory cards. V05 uses four executable stages: import data, clean data, AI diagnosis and initial conclusion. The AI diagnosis state includes evidence-aware dialogue, a vertically arranged confidence chart and a route from the conclusion to the data report.

## Comparison History

### Pass 1

- P1: Product navigation represented page sections instead of user tasks. Fixed by removing the launch/closed-loop/MVP sections and introducing seven task-domain entries.
- P1: Data processing was explanatory and had no usable workflow. Fixed with imported-source status, cleaning rules, diagnosis dialogue, initial conclusions and report routing.
- P2: Confidence chart competed horizontally with campaign text. Fixed by placing the ring below the diagnosis summary in a vertical card.
- P2: Number labels had low contrast and weak alignment. Fixed with 40-42 px numbered blocks, 18 px white centered numbers.
- P2: The six-stage strip squeezed the dashboard action area, and the 390 px layout inherited page-level horizontal overflow. Fixed by using a three-column desktop stage grid and constraining responsive grid children to `min-width: 0`.

### Pass 2

- Desktop dashboard and AI diagnosis were recaptured after fixes. Stage labels, next action and confidence chart are fully visible.
- At 390 px, document-level horizontal overflow was removed; the primary navigation remains horizontally scrollable, with its system scrollbar hidden.
- Core interactions were retested: language switch, new activity validation, H5 preview, cleaning, AI follow-up, conclusion generation and report routing.

## Required Fidelity Surfaces

- Typography: system Chinese UI stack retained; page headings are 24/32, section headings 14-16, body text 11-14. No oversized marketing type remains.
- Spacing and layout: persistent 224 px navigation, 24 px content padding, 12 px operational grid, 7-8 px radii. No overlapping controls or page-level overflow remain.
- Colors and tokens: V04 dark neutral base, purple primary action, cyan data state, lime active stage, coral/warning priorities are retained with clearer semantic roles.
- Image quality: the operational target has no required photography or illustration. The previous marketing video/fallback asset region was removed because it had no task value.
- Copy and content: explanatory slogans were removed. Visible copy now names tasks, states, evidence, thresholds, owners and next actions.
- Icons: no new decorative icon set was introduced. Existing mnemonic navigation codes are applied consistently.
- Accessibility: buttons and form controls use semantic elements; focus-visible styles are present; modal fields have labels; status feedback uses an ARIA live region.

## Findings

No actionable P0, P1 or P2 findings remain for the requested redesign.

## Follow-Up Polish

- P3: Several secondary table actions are prototype-only and do not persist data.
- P3: English translation covers navigation and main dashboard labels; detailed mock-data content remains Chinese.

## Verification

- JavaScript syntax: passed.
- Duplicate HTML IDs: none.
- Browser console errors/warnings: none.
- Primary interaction flow: passed.
- Responsive layout: desktop passed; mobile body overflow passed.

final result: passed
