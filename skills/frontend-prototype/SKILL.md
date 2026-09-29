---
name: frontend-prototype
description: Build a runnable frontend prototype to explore and validate user flows, information hierarchy, interaction patterns, UI states, responsive behavior, and visual direction before production implementation. Treat settled business behavior and technical decisions as inputs rather than redesigning them.
---

# Frontend Prototype

Turn an already-understood product or engineering direction into a runnable interface that can be judged by using it. The prototype is evidence about frontend experience, not a second requirements or domain-design phase and not production implementation.

## Establish the design basis

Read the relevant requirements, accepted decisions, current product UI, design system, component library, and representative data. Reuse the product's vocabulary and visual language when they exist.

Do not reopen settled business rules merely because the UI is awkward. If the interface exposes a genuine contradiction or missing product decision, identify it precisely and stop that branch at the decision boundary instead of silently inventing behavior.

Read [Frontend design foundation](references/design-foundation.md) for visual hierarchy, product-vs-brand register, typography, spacing, color, and anti-template guidance. Read [Interaction and states](references/interaction.md) for flows, forms, overlays, feedback, accessibility, responsive behavior, and representative states.

## Define what the prototype must answer

State the concrete frontend uncertainty before building. Examples include:

- whether a drawer, modal, inline panel, or dedicated page supports the task better;
- how dense configuration should be grouped and progressively disclosed;
- how navigation and page hierarchy communicate where the user is;
- how loading, empty, error, validation, disabled, partial, and long-content states behave;
- how a complex workflow remains understandable at desktop and narrower widths;
- whether two materially different interaction directions deserve side-by-side comparison.

Prefer one coherent direction when the request is clear. Create alternatives only when a real design decision remains unresolved; variants that differ only by decoration are not useful evidence.

## Build at the right fidelity

Use real interaction for the part being evaluated. Mock or stub backend behavior that is irrelevant to the frontend question, but use representative data and believable state transitions. Reuse the project's actual frontend stack and components when doing so materially improves fidelity; otherwise choose the smallest runnable form that preserves the interaction being tested.

Prototype code may be disposable. Do not use that as permission for incoherent structure, fake success paths, inaccessible controls, or impossible responsive behavior. A prototype should be cheap to change, not misleading.

Keep the visual treatment intentional. Avoid generic AI defaults, ornamental card grids, arbitrary gradients, excessive rounding, decorative motion, or novelty that competes with a product task. Product UI normally favors clarity, density, consistency, and predictable controls over spectacle.

## Verify by using it

Read [Prototype verification](references/verification.md). Exercise the critical flow and the states that can change the design decision. Check keyboard/focus behavior where relevant, at least one narrow viewport when the product is responsive, and representative overflow or long-content cases.

Do not claim usability research, accessibility conformance, performance readiness, or production acceptance unless those were actually evaluated with appropriate evidence.

## Deliver

Provide the runnable prototype, how to start it, the frontend question it answers, the design decisions demonstrated, and important limitations. Record any accepted consequence in the project's existing design artifact when that is in scope.

Promotion to production belongs to implementation work. Preserve useful design evidence, but do not make temporary prototype architecture or mock data a production constraint merely because the experiment worked.
