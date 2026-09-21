# Reproduction, Timing, and Observability

Use when the current signal is too weak to distinguish causes or to know whether a fix worked.

## Build a signal for the actual symptom

Capture input, version, configuration, relevant state, expected result, and observed failure. A useful loop reaches the failing path and observes the user's symptom; “process did not crash” is insufficient when the defect is incorrect data or a missing side effect.

Choose an appropriate form: a failing test, a small API or CLI call, captured request replay, a reduced local harness, differential execution, controlled property generation, or a targeted trace. Prefer the shortest reliable loop that preserves the meaningful conditions. Do not require a complex harness when a two-call reproducer suffices.

Keep the original scenario while reducing inputs or dependencies one at a time. Rerun after each reduction. If the reduced case exhibits a different error, restore the discarded condition. For a human-only interaction, record repeatable steps and the observation needed; inability to automate does not erase available evidence.

Separate a behavioral failure from setup failures. Missing credentials, unavailable services, or a broken test runner can block an experiment without supporting any causal explanation of the original bug.

## Intermittent and order-dependent failures

Record sample count, failure frequency, seeds, concurrency, and environment. Use explicit barriers or controlled event ordering to force the suspected race when possible. Repeated random stress can support a hypothesis but does not explain which interleaving caused it.

If a test fails only after another, compare isolated and ordered runs, then narrow the preceding sequence. Check leaked globals, mutable defaults, shared files, database state, environment changes, retained timers, and unfinished tasks. Keep the same setup semantics while reducing; a passing isolated test does not establish correctness under the original suite.

Wait for an observable condition with a bounded deadline and useful diagnostics rather than adding a longer arbitrary sleep. Read fresh state inside a wait loop. Where elapsed time is itself the requirement—debounce, lease expiration, rate limiting—control the clock or use a justified timing assertion; condition polling must not hide a broken deadline.

## Narrow a regression boundary

When the same reliable check distinguishes a known-good and known-bad revision, use bisection to narrow the introducing change. Run it in an isolated checkout with controlled dependencies and state; preserve the user's working tree. Record the tested revisions and observations.

Treat build failures, missing services, and incompatible test harnesses as untestable revisions, not occurrences of the target defect. Skipped revisions may leave several candidates. Flaky outcomes or a regression later fixed and reintroduced weaken the single-transition assumption; resolve that uncertainty before naming a culprit. Confirm a narrowed candidate through the changed path and a targeted reproduction or controlled reversal. A bisect result locates a boundary; it does not by itself explain the cause.

## Performance regressions

Measure the user-relevant metric under comparable workload, data size, cache state, runtime, and resource conditions. Distinguish latency, throughput, errors, and resource cost. Find where time or contention accumulates with profiling, query plans, or targeted timing; logging everything may itself change the failure.

Use a known-good revision or configuration when available. Account for warm-up and variability. A local improvement can coexist with a system regression if the work moved elsewhere or increased tail latency.

## Missing reproduction

Use existing traces and source to narrow hypotheses, clearly separating confirmed facts from possibilities. State what was attempted, what it excludes, and the smallest next artifact or access needed. Do not demand a perfect automated reproducer before reading code, and do not call an unobserved post-patch outcome verified.

Keep observations limited to useful, appropriately redacted data. Temporary production instrumentation requires the applicable authorization and a removal plan; an investigation request alone does not imply unrestricted production changes.
