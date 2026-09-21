# Behavior-Preserving Change

Use for restructuring existing code, moving modules, changing dependency direction, or consolidating repeated policy without intentionally changing observable behavior.

## Define what is preserved

Identify public callers, return values, error handling, retries, fallback, ordering, resource ownership, persisted formats, and relevant performance. Include best-effort and degraded paths. A replacement that returns the same result on success but starts propagating a previously handled timeout is not equivalent.

Use trustworthy existing tests. Where behavior is unprotected, characterize representative behavior before changing it. Distinguish observed legacy behavior from intended requirements: a known defect should not silently become a permanent requirement, nor should a refactor silently fix it without scope and verification.

If a hard-coded dependency prevents meaningful observation, introduce the smallest useful selection point while preserving behavior. Prefer a real local dependency where practical; consult [Dependency fidelity](fidelity.md) when a substitute is needed.

## Change one kind of thing at a time

Keep behavior changes, responsibility moves, provider inversion, and mechanical file movement distinguishable. After each useful slice, verify the preserved behavior and the new structural property. A mass move combined with changed errors and a new persistence model is difficult to diagnose even if it initially compiles.

For broad API migration, expand a compatible new form, migrate consumers in bounded groups, then remove the old form after checking remaining callers. Temporary adapters need an explicit retirement condition. Do not count a compatibility facade as proof that complexity disappeared.

For package movement, verify actual module roots, package declarations, imports/exports, discovery globs, build contexts, and startup or route registration. Compilation tests only part of the claim; a package can compile while belonging to the wrong architectural layer.

## Demonstrate the result

Keep tests that protect distinct behavior, including adapter equivalence and algorithms. Replace implementation-coupled tests only after their meaningful coverage is preserved. Test failures on the original snapshot remain baseline failures and should be reported separately.

If claiming simpler architecture, compare caller obligations and total affected mechanism across the same scope, including new configuration, adapters, state, and operational work. Fewer lines in one module can merely move the burden elsewhere.

Conclude with preserved behavior, structural changes, actual checks, compatibility still present, and remaining limitations. A refactor's success is the evidence of preservation and the intended structural improvement together.

For moved responsibilities or paths, reconcile affected package indexes, diagrams, decision references, and setup instructions with the resulting structure. Preserve historical ADR rationale and distinguish the target design from any migration work still outstanding.
