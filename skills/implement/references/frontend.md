# Frontend Implementation

Use this reference only when production work has a user-facing frontend surface, including product and brand pages. A prior prototype is optional.

## Treat design as input

Read accepted requirements, design decisions, existing product UI, relevant prototype evidence, routes, components, tokens, state/data ownership, and API contracts. Read only what the affected surface needs. Do not reopen settled visual choices merely because implementation has started.

When no design or prototype settles a consequential interaction, make the smallest locally consistent decision or surface the unresolved product choice when it materially changes behavior.

For a new surface without an established visual system, choose a coherent layout, type scale, spacing rhythm, and semantic palette that serve the user's task. Build that direction directly within the authorized implementation; do not require a separate prototype phase. Explore competing directions only when the request or a consequential unresolved choice warrants it.

## Preserve experience quality

Apply the principles relevant to the affected surface:

- product UI favors clarity, useful density, consistency, and predictable controls;
- hierarchy is expressed deliberately through layout, grouping, typography, contrast, spacing, and alignment;
- reuse the existing design system and semantic tokens when sound;
- make visual choices serve the explicit brief and surface; expressive brand work may call for treatments that would distract in dense product UI;
- implement loading, empty, error, validation, disabled, progress, and long-content states that the affected flow can actually encounter;
- use labeled semantic controls, keyboard operation, visible focus, and sensible modal focus containment, dismissal, and return;
- keep status understandable without color alone, text and controls legible, and motion respectful of reduced-motion preferences;
- adapt layout and touch interactions to supported viewports and devices.

## Add production constraints

Prototype shortcuts must not leak into production architecture. Replace mock behavior with the real data boundary. Follow project ownership for requests, cache, state, routing, schemas, generated clients, feature modules, and design-system primitives.

Keep privileged clients and secrets out of browser imports and bundles. Handle stale responses, repeated submissions, cancellation, and optimistic rollback where the flow exposes them; a loading indicator alone does not resolve request ordering or failure semantics.

Prefer maintainable component boundaries over copying a prototype's markup literally. Preserve visual and interaction intent while adapting structure to the project.

Test the critical user behavior at the appropriate level. Inspect the rendered result with an available browser or UI runner, including scoped responsive layouts, failure states, and interactions likely to regress. When that is unavailable, separate static/build evidence from unverified rendering and interaction. Consider bundle, rendering, and network cost when the change makes them material.

A local copy or token adjustment needs focused checks of the affected states and layouts, not a new application-wide design or test program. Broaden verification when the change reaches shared components or evidence reveals a wider regression.

The implementation is complete when the product behavior, design intent, project architecture, and verification agree—not when the prototype has simply been reproduced pixel for pixel.
