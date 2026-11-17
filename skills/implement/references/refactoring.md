# Behavior-Preserving Change

Use for restructuring existing code, moving modules, changing dependency direction, or consolidating repeated policy without intentionally changing observable behavior.

## Define what is preserved

Identify public callers, return values, error handling, retries, fallback, ordering, resource ownership, persisted formats, and relevant performance. Include best-effort and degraded paths. A replacement that returns the same result on success but starts propagating a previously handled timeout is not equivalent.

Use trustworthy existing tests. Where behavior is unprotected, characterize representative behavior before changing it. Distinguish observed legacy behavior from intended requirements: a known defect should not silently become a permanent requirement, nor should a refactor silently fix it without scope and verification.

If a hard-coded dependency prevents meaningful observation, introduce the smallest useful selection point while preserving behavior. Prefer a real local dependency where practical; consult [Dependency fidelity](fidelity.md) when a substitute is needed.

## Choose a change that removes actual burden

Start from a concrete difficulty in the requested scope: a rule that must be changed in several places, a call path that hides its effects, or branching that makes valid states hard to follow. Use nearby conventions and callers to decide whether a candidate helps; size, repetition, and indirection alone do not establish a problem.

| Observed difficulty | Candidate change | Check before choosing it |
|---|---|---|
| Nested decisions obscure the normal path | Introduce guard clauses or name a coherent decision | Preserve evaluation order, side effects, cleanup, and error precedence; moving a condition can change behavior |
| The same business rule is maintained in several places | Put the rule with its existing owner and reuse it | The sites must share the same contract and reason to change; similar expressions in independent domains may need to stay separate |
| Callers repeatedly reconstruct valid states or dispatch on the same variants | Clarify the type/interface boundary or consolidate dispatch | Preserve supported states, runtime validation at external boundaries, and fallback behavior; a new model should eliminate caller work rather than require another translation layer |
| A forwarding chain makes behavior harder to locate | Inline a layer that contributes no useful contract | Keep boundaries that own authorization, recovery, compatibility, observability, or an independently useful interface |
| Calculation is tangled with I/O or sequencing | Separate the calculation from orchestration at a useful seam | Preserve resource lifetime, transaction scope, ordering, and the meaning of failures; do not split merely to shorten a function |

Choose the candidate whose benefit survives comparison of the whole affected path. A clearer direct implementation can be preferable to a reusable abstraction. Leave code alone when the proposed change only trades one equally understandable form for another or costs more than the current friction justifies. Support performance claims with comparable measurements rather than assuming a cleaner expression is faster.

## Change one kind of thing at a time

Keep behavior changes, responsibility moves, provider inversion, and mechanical file movement distinguishable. After each useful slice, verify the preserved behavior and the new structural property. A mass move combined with changed errors and a new persistence model is difficult to diagnose even if it initially compiles.

For internal APIs that can switch in one cutover, migrate all affected callers and remove the obsolete form in the same change. When supported callers or retained data require old and new forms to coexist, introduce a compatible new form, migrate in bounded groups, and remove the old form after its last required use. Temporary adapters need an explicit retirement condition. Include their cost when assessing complexity.

For package movement, verify actual module roots, package declarations, imports/exports, discovery globs, build contexts, and startup or route registration. Compilation tests only part of the claim; a package can compile while belonging to the wrong architectural layer.

## Demonstrate the result

Keep tests that protect distinct behavior, including adapter equivalence and algorithms. Replace implementation-coupled tests only after their meaningful coverage is preserved. Test failures on the original snapshot remain baseline failures and should be reported separately.

If claiming simpler architecture, compare caller obligations and total affected mechanism across the same scope, including new configuration, adapters, state, and operational work. Fewer lines in one module can merely move the burden elsewhere.

Conclude with preserved behavior, structural changes, actual checks, compatibility still present, and remaining limitations. A refactor's success is the evidence of preservation and the intended structural improvement together.

For moved responsibilities or paths, reconcile affected package indexes, diagrams, decision references, and setup instructions with the resulting structure. Preserve historical ADR rationale and distinguish the target design from any migration work still outstanding.
