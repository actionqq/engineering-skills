# Frontend Implementation

Use this reference only when production work has a user-facing frontend surface.

## Treat design as input

Read accepted requirements, design decisions, existing product UI, relevant prototype evidence, routes, components, tokens, state/data ownership, and API contracts. Do not reopen visual exploration merely because implementation has started.

When no design or prototype settles a consequential interaction, make the smallest locally consistent decision or surface the unresolved product choice when it materially changes behavior.

## Preserve the shared frontend method

Use the same design principles as frontend prototypes:

- product UI favors clarity, useful density, consistency, and predictable controls;
- hierarchy is expressed deliberately through layout, grouping, typography, contrast, spacing, and alignment;
- reuse the existing design system and semantic tokens when sound;
- avoid generic template artifacts, ornamental card nesting, arbitrary gradients, excessive rounding, or motion without purpose;
- implement meaningful loading, empty, error, validation, disabled, progress, and long-content states;
- keep keyboard/focus behavior, semantic controls, and responsive behavior appropriate to the product.

## Add production constraints

Prototype shortcuts must not leak into production architecture. Replace mock behavior with the real data boundary. Follow project ownership for requests, cache, state, routing, schemas, generated clients, feature modules, and design-system primitives.

Prefer maintainable component boundaries over copying a prototype's markup literally. Preserve visual and interaction intent while adapting structure to the project.

Test the critical user behavior at the appropriate level. Verify responsive layouts that are in scope, failure states, and interactions likely to regress. Consider bundle, rendering, and network cost when the change makes them material.

The implementation is complete when the product behavior, design intent, project architecture, and verification agree—not when the prototype has simply been reproduced pixel for pixel.
