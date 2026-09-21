# Interactive State and UI Prototypes

Use when people need to manipulate a model or compare interactions to resolve a design question. Choose a logic or UI experiment deliberately; attractive screens do not validate a state model.

## State and data models

Put the question visibly in the artifact so a later reader knows what is being tested. Isolate the model from the presentation: a reducer, explicit state machine, pure transformation functions, or a small state-owning module as the problem requires. Rendering should call the model rather than contain a second copy of its rules.

Expose relevant state in domain language after each action. Provide free exploration plus repeatable scenarios with a known reset state. Useful scenarios include the normal path, a difficult sequence, and an illegal or repeated action. If the question concerns cancellation after success, make that sequence actually executable and show the result.

A self-contained HTML file is useful when sharing a local model with non-developers. It is not a requirement for a question whose meaning depends on a framework or real service boundary. Keep the presentation understandable without exposing raw implementation details unless those details help the intended reader.

Preserve a model or reducer that precisely expresses a validated decision, but distinguish it from production-ready implementation. A user clicking a demo has not established real concurrency, durability, authorization, or operational recovery.

## UI alternatives

Compare meaningful differences in information hierarchy, flow, or primary interaction rather than only colors. Use enough alternatives to explore the real decision; fixed variant counts are unnecessary.

When context matters, evaluate alternatives against the existing page's navigation, density, component system, and representative data. Use an isolated development route, copy, or clearly gated preview appropriate to the project. A prototype request does not imply permission to expose an experimental path to real users.

Keep variants directly comparable with stable selection and reset behavior. A URL parameter or clear selector can make an option reproducible. Support keyboard use appropriately; do not steal navigation keys from focused form controls.

Use inert data or stubs for mutations that are irrelevant to the question. Preserve meaningful states such as empty, loading, error, validation failure, and long content when they affect the choice. Do not make every alternative look viable by showing only idealized data.

## Capture the result

Record the original question, scenarios actually exercised, observed problems, chosen direction if any, and remaining uncertainty. Keep the evidence artifact accessible. If no option wins, identify the unresolved trade-off or next experiment rather than inventing consensus. Production promotion requires proper implementation and validation within the actual request.
