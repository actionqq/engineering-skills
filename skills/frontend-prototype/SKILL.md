---
name: frontend-prototype
description: Build a runnable frontend prototype to explore and validate user flows, information hierarchy, interaction patterns, UI states, responsive behavior, and visual direction. Use for interactive mockups, UI alternatives, and frontend experience experiments. Production feature delivery, backend experiments, and architecture decisions are different tasks; settled business and technical decisions remain inputs.
---

# Frontend Prototype

Turn a product or engineering direction into a runnable interface that can be judged by using it. Communicate in the user's language. The prototype is evidence about frontend experience, not a second requirements or domain-design phase and not production implementation.

## Establish the design basis

Read the relevant requirements, accepted decisions, current product UI, design system, component library, and representative data. Reuse the product's vocabulary and visual language when they exist.

A clear conversational brief is sufficient; formal requirements, a prior prototype, and a design system are not prerequisites. Infer routine reversible choices from the task. Clarify only missing decisions that would materially change the experience being tested, and continue independent parts.

Do not reopen settled business rules merely because the UI is awkward. If the interface exposes a genuine contradiction or missing product decision, identify it precisely and stop that branch at the decision boundary instead of silently inventing behavior.

## Define what the prototype must answer

State the concrete frontend uncertainty before building. Examples include:

- whether a drawer, modal, inline panel, or dedicated page supports the task better;
- how dense configuration should be grouped and progressively disclosed;
- how navigation and page hierarchy communicate where the user is;
- how loading, empty, error, validation, disabled, partial, and long-content states behave;
- how a complex workflow remains understandable at desktop and narrower widths;
- whether two materially different interaction directions deserve side-by-side comparison.

Prefer one coherent direction when the request is clear. Create alternatives only when a real design decision remains unresolved; variants that differ only by decoration are not useful evidence.

## Select the needed methods

| Work in scope | Read |
|---|---|
| Create or change visual direction, hierarchy, layout, typography, or content treatment | [Frontend design foundation](references/design-foundation.md) |
| Create or change a flow, control, UI state, overlay, or responsive interaction | [Interaction and states](references/interaction.md) |
| Exercise and deliver the prototype | [Prototype verification](references/verification.md) |

A new end-to-end prototype normally needs all three. A targeted revision loads only the affected methods and checks that it preserves the rest. Do not redesign an accepted visual direction merely to demonstrate a method.

## Build at the right fidelity

Use real interaction for the part being evaluated. Mock or stub backend behavior that is irrelevant to the frontend question, but use representative data and believable state transitions. Identify simulated effects and make important test states reproducible. Reuse the project's actual frontend stack and components when doing so materially improves fidelity; otherwise choose the smallest runnable form that preserves the interaction being tested. Keep experimental artifacts separate from production behavior unless integration is requested.

Prototype code may be disposable. Do not use that as permission for incoherent structure, fake success paths, inaccessible controls, or impossible responsive behavior. A prototype should be cheap to change, not misleading.

## Verify by using it

Use the verification reference to exercise the critical flow and the states that can change the design decision. Check keyboard/focus behavior where relevant, at least one narrow viewport when the product is responsive, and representative overflow or long-content cases.

Do not claim usability research, accessibility conformance, performance readiness, or production acceptance unless those were actually evaluated with appropriate evidence.

## Deliver

Provide the runnable prototype, how to start it, the frontend question it answers, the design decisions demonstrated, and important limitations. Record any accepted consequence in the project's existing design artifact when that is in scope.

Promotion to production belongs to implementation work. Preserve useful design evidence, but do not make temporary prototype architecture or mock data a production constraint merely because the experiment worked.
