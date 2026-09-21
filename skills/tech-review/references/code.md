# Code Review Scope and Evidence

Use for changes or explicitly requested whole-code review. Default to defects introduced by the change; label unrelated pre-existing issues separately when relevant.

## Resolve comparison semantics

Inspect repository state and actual references. Use the user's intended comparison:

| Request | Meaning |
|---|---|
| Branch/PR changes since divergence | Compare the target with the merge base of the specified branches |
| Difference between two exact versions | Compare those trees directly |
| One ordinary commit | Compare it with its parent |
| A merge commit | Establish the relevant parent line or merged-result question |
| All uncommitted changes | Account for index, worktree, and untracked files |

Examples such as `git diff base...head` and `git diff base head` have different meanings; choose after resolving the references. For WIP, inspect status, staged changes, unstaged changes, and new files. A default diff misses some of that scope. An empty tracked diff does not prove there is nothing to review.

Record the resolved revision and covered files. Concurrent edits can make a worktree review inconsistent; reread affected material or state the limitation. Do not commit, reset, or stash someone else's work to simplify the review.

## Follow the behavior beyond the hunk

Start with the diff, then inspect relevant callers, dependencies, configuration, state, and tests. Check concrete changes to correctness, error propagation, resource lifecycle, input bounds, retry, concurrency, identity/permissions, compatibility, and materially changed cost.

Compare failure paths in refactors. A removed catch, fallback, cleanup, or best-effort reconciliation can be a regression even if happy-path output is unchanged. Check how a changed signature affects callers and how a changed stored representation affects readers.

Use the provided requirement and existing project standards. Without a formal spec, review explicit user intent and actual interface obligations, stating the missing coverage. Do not invent a specification and then use it to prove conformance.

## Keep findings discriminating

A reported defect should have a reachable scenario and evidence of its consequence. Check for guards, invariants, callers, framework behavior, or tests that invalidate the suspicion. Style tooling and code-smell catalogs can supply leads, not automatic findings.

For a required-standard deviation, cite the actual rule and why this code violates it. For maintainability, explain concrete change or comprehension cost. Avoid reporting harmless thin adapters merely because they delegate.

Tests can confirm or refute a finding but do not replace source review. Run suitable checks when allowed and worthwhile; honor an explicit static-only request. Report the command and observed result when making an execution claim.

## Deliver precise feedback

Use current file/line locations or verified PR diff coordinates. Give the trigger, impact, evidence, and repair direction in a compact finding. Group duplicate symptoms of one cause when that makes the fix clearer, and rank by actual consequence.

For independent or separate standards/specification checking, read [Independence and synthesis](independence.md). The common output remains one coherent, deduplicated review unless the user or consuming integration requires another structure.
