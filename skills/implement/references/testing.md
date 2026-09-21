# Behavior-Oriented Test Design

Use for a dedicated test strategy, meaningful coverage work, or a new behavior whose feedback is not already obvious.

## Select what must be protected

Start with observable requirements, invariants, recent defects, and consequences of failure. Connect each important risk to setup, trigger, expected observation, and an appropriate test boundary. Include normal, boundary, and actual failure paths; concurrency, recovery, migration, and permissions belong where the behavior depends on them.

Prefer stable caller-facing contracts for behavior tests. A complex algorithm or coherent internal subsystem can have focused tests when they localize meaningful failure. Avoid exposing private helpers solely to test incidental orchestration, but do not prohibit internal testing as a universal rule.

Observe at the level of the claim. If the requirement is user retrieval, an API-level test may be strongest. If the requirement is a database uniqueness constraint, transaction, or exact stored format, direct database inspection can be necessary evidence. One test surface does not prove every layer.

## Use independent expected results

Derive expectations from the requirement, a manually checked example, a known invariant, a trusted independent implementation, or a legitimate external oracle. Repeating the implementation's arithmetic or algorithm inside the test can reproduce the same mistake.

Example: for a rounding requirement, use worked monetary examples that distinguish rounding modes. Do not calculate every expected value by invoking the same helper as the implementation. For idempotency, observe durable side effects after repeated requests rather than only one mock call in a single invocation.

Ask what plausible incorrect implementation this test would reject. A test that still passes after removing the important operation is weak evidence. Mutation testing can help where it is proportionate or required, but a mutation score is not a substitute for relevant scenarios.

## Iterate through real behavior

For test-first implementation:

1. Add one useful scenario at the chosen boundary.
2. Run it and inspect why it fails; a syntax or environment failure is not the desired behavioral red result.
3. Implement the behavior required for that scenario.
4. Run the targeted check and relevant existing protection.
5. Improve structure under passing tests and choose the next risk-informed scenario.

Avoid writing a large batch of tests against imagined interfaces before feedback teaches you the boundary. Conversely, do not treat one-test-at-a-time as a prohibition on a coherent table of boundary examples or an existing regression suite.

## Choose levels and control nondeterminism

Pure logic and controlled edge cases often fit unit tests. Integration or contract tests establish serialization, queries, transactions, adapter behavior, and dependency compatibility. End-to-end tests cover important cross-layer paths; they need not carry every small variation.

Control time, randomness, external state, and scheduling where they affect the result. Prefer observable completion with a bounded deadline to arbitrary sleeps; use explicit timing assertions when time itself is the requirement. For races, create the relevant interleaving rather than hoping stress will find it.

Read [Dependency fidelity](fidelity.md) when choosing mocks or fakes. Deliver concrete cases and prerequisites for a test-plan-only request; implement tests only when that is requested. Report executed results separately from planned coverage, and preserve existing valid failures instead of weakening assertions to obtain green output.
