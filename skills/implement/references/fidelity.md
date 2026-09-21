# Dependency Substitutes and Test Fidelity

Use when test results depend on mocks, fakes, real resources, time, or environment selection.

## State the substitution boundary

Choose a boundary because a dependency is nondeterministic, costly, remote, independently owned, or otherwise important to control. Identify where the substitute is selected. Do not mock every owned collaborator by reflex: long internal interaction chains often verify an implementation script rather than behavior.

Favor operation-shaped interfaces in application terms over a generic request function whose test setup reimplements routing. Keep provider-specific representations behind meaningful adapters. Do not add an interface solely to give a mocking framework something to intercept.

Choose the lightest faithful dependency:

| Dependency | Useful fast feedback | Evidence still needed |
|---|---|---|
| Owned pure logic | Real implementation | Boundary/algorithm examples |
| Local storage | Disposable real resource where practical | Actual schema, constraints, transaction semantics |
| Remote owned API | Deterministic fake of the agreed behavior | Serialization, errors, compatibility against real adapter |
| Third-party service | Bounded fake or approved recorded responses | Supported provider behavior, auth, limits, important failure modes |
| Clock/randomness/scheduler | Controlled values or scheduling | Real integration/timing where required |

## Make fidelity gaps explicit

A fake that accepts duplicate keys does not represent a database that rejects them. A local queue that processes in order does not prove a provider's delivery ordering. An HTTP stub does not establish authentication, quotas, cancellation, or retry semantics.

When implementations are intended to be interchangeable, run a shared behavioral contract against relevant implementations or otherwise demonstrate equivalence at the required boundary. Record provider features a substitute omits. A fast fake is useful only when its limitations are understood.

Prefer outcomes and effects over incidental call order. Interaction assertions are valid when the interaction itself is the requirement, such as bounded retries, an emitted audit event, or a mandated external request; explain that connection instead of banning all call-count checks.

Select stable dependencies at composition when possible, without forcing every caller to pass a clock or client it never varies. Control resources and cleanup so parallel tests do not corrupt one another. When a real integration environment is absent, report that part as unverified rather than stretching unit-test evidence to cover it.
