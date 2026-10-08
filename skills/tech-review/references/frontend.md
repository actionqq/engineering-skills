# Frontend Review

Apply this lens only when the target includes user-facing frontend behavior or UI.

## Establish the governing basis

Prefer, in order, explicit product requirements, accepted design/prototype decisions, the project's design system and established product conventions, and general interface guidance. Do not override an intentional local design with a generic external preference.

Choose checks from the requested scope: a visual refinement needs rendered hierarchy and consistency checks; an interactive feature also needs flow and state checks; a shared component or data-boundary change may require wider consumer checks. The existence of this checklist does not make every item a mandatory audit of the whole application.

## Review the experience

Check whether information hierarchy makes the main task understandable and whether controls communicate their role and current state. Look for accidental density, unnecessary containers, inconsistent spacing, unclear emphasis, or decorative patterns that obscure the task.

Trace the critical flow rather than judging a screenshot alone. Check meaningful loading, empty, error, validation, disabled, progress, long-content, and destructive-action states when they can occur.

Check semantic controls, labels, error recovery, touch target practicality for supported devices, and responsive behavior at meaningful widths. For web interfaces, trace keyboard access, visible focus, modal containment/dismissal/return, contrast and non-color status cues, and reduced-motion behavior where animation exists. For data-driven flows, check stale responses, repeat submission, and optimistic failure recovery when applicable; also inspect client/server imports where privileged code could enter a browser bundle.

Compare implementation with the project's components and tokens. Flag divergence when it causes inconsistency, duplicated behavior, accessibility regression, or unnecessary maintenance—not merely because a different style is possible.

## Keep taste evidence-based

Generic AI-looking composition, gratuitous gradients, card nesting, excessive rounding, oversized decorative headings, or motion everywhere may be useful warning signs, but they are not findings by themselves. Report them only when they conflict with the product register, existing design language, task hierarchy, usability, or explicit requirements.

Use an available browser or UI runner for in-scope rendered checks. When rendered evidence is unavailable, distinguish static-code concerns from observed UI defects and state which flows or viewports remain unverified.
