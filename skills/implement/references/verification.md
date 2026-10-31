# Verification Before Completion

Load this reference before reporting a change as fixed, complete, passing, or ready to merge when the claim depends on execution evidence.

## Evidence rule

A completion statement must be supported by a fresh check of the relevant final state. Identify the exact claim, choose the narrowest command or observable check that proves it, run it after the final relevant edit, inspect the complete result and exit status, and report the actual scope. A previous run, agent summary, code inspection, or a successful weaker check cannot prove a stronger claim.

| Claim | Minimum evidence |
|---|---|
| Unit tests pass | Relevant test command completed with zero failures |
| Build succeeds | Actual build command completed successfully |
| Regression is fixed | A test reproduces the original failure before the fix and passes after it, where practical |
| Behavior works end to end | The relevant runtime path was exercised in a representative environment |
| Requirements are met | Each acceptance item was checked against the final artifact; tests alone are not a substitute |
| Delegated work is integrated | Inspect the resulting diff and independently run the relevant checks |

## Choose verification by risk

- Run focused tests while iterating; run the broader affected suite after integration.
- Check failure and boundary behavior, not only the happy path.
- For regression tests, establish that the assertion detects the original defect when a safe baseline is available. A test that passes on both baseline and patched code does not demonstrate the fix.
- For concurrency, persistence, serialization, or external side effects, test the real boundary or explicitly state what the substitute cannot prove.
- Use mutation testing or property-based testing when example-based tests leave a meaningful oracle or input-space gap; do not add these techniques to every small change.
- If a check is unavailable, flaky, blocked, or intentionally skipped, record that state and its impact. Never convert missing evidence into a pass.

## Final pass

1. Re-read the requested outcome and acceptance criteria.
2. Inspect the final diff for accidental scope, missing callers, and unintended changes.
3. Run the selected checks against the final revision.
4. Read outputs, exit codes, and failure counts; distinguish test failures from harness/environment failures.
5. State exactly what was verified, on which scope, and what remains unverified.

This is an evidence discipline, not a requirement to run every possible check or to delay useful incremental feedback. Do not claim a full-system guarantee from a focused test.
