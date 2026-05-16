# Mobile Position-Changes Table Width Design

## Goal
On phone-sized screens, keep the company column in **Quarter-over-Quarter Position Changes** readable instead of allowing it to collapse into character-by-character wrapping.

## Root Cause
The mobile grid keeps all five columns inside the available card width while also giving the company column a flexible `minmax(0, …)` track. On narrow screens, the fixed-ish numeric columns consume most of the room, so the company track shrinks nearly to zero and long names wrap one or two characters per line.

## Recommended Approach
Keep the existing desktop and tablet layout unchanged. On small screens, give the ranking table an explicit minimum content width and let only the list/header region scroll horizontally when the viewport is narrower than that minimum. This preserves the current visual hierarchy, keeps numeric columns legible, and gives the company column enough room to read normally.

## Why This Approach
- It is the smallest change that addresses the actual layout failure.
- It avoids degrading the numeric columns just to force everything into one viewport.
- It keeps the current table semantics and styling intact instead of introducing a separate mobile card design.

## Implementation Notes
- Wrap scrolling behavior around the existing change-grid header and list through their current container structure; do not change the rendered HTML or data model.
- Add a mobile-only minimum width to `.change-grid-head` and `.change-pro-list` so they stay aligned.
- Preserve vertical scrolling in the list; horizontal scrolling should only appear when needed.
- Keep the company name wrapping behavior as normal word wrapping once the column has adequate width.

## Verification
- Reproduce at a narrow mobile viewport using a long company label such as `Alphabet (GOOGL) · A`.
- Confirm the company name is no longer broken into near-character columns.
- Confirm the five columns remain aligned between header and rows.
- Confirm the table remains usable on desktop widths.
