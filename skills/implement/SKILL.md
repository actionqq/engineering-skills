---
name: implement
description: Deliver defined software changes with proportionate verification, or independently design tests and add meaningful coverage. Use for features, bounded fixes, behavior-preserving refactors, test plans, and test implementation. Root-cause investigation and read-only review are different tasks; a test-plan-only request does not authorize product edits.
---

# Implementation and Tests

Deliver the requested behavior and evidence that it works. Communicate in the user's language. Work can be defined in the conversation, an issue, or a design; a separate specification file is not mandatory for a clear task.

## Establish the working basis

Read applicable project instructions, relevant decisions, nearby code, callers, and tests. Inspect existing changes before editing and protect unrelated work. Identify acceptance requirements, the appropriate verification commands, and known baseline failures when practical.

Check whether the execution basis fits the work. Perform a clear bounded edit directly; use a short checklist for manageable related steps. When outcomes, dependencies, context burden, or independent continuation justify decomposition, establish bounded units before implementation. Each independent unit needs a brief stating its result, relevant design references, prerequisite outputs, essential constraints, and acceptance; an existing issue or plan section can serve. Do not require another installed Skill, a separate spec file for every step, or prewritten implementation code. During an implementation request, necessary local planning is part of the work, not a new approval gate.

For the current unit, read its brief and necessary source sections, confirm prerequisites against actual artifacts, and resolve stale assumptions before editing. Load further context as needed rather than every sibling task and the whole transcript. If the unit grows beyond a coherent result and check, revise its boundary and remaining plan within scope. Preserve relevant failure semantics and cross-cutting constraints when narrowing context.

Identify which existing documents own the affected behavior, decisions, and project context. If implementation changes documented facts, exposes a design mismatch, or produces durable findings, read [Maintaining project documents](references/documents.md). Record settled changes as work proceeds; do not defer all reconciliation to the final response.

Resolve ordinary implementation details within scope. If the design cannot work in the actual environment, explain the concrete mismatch. A change to public behavior, ownership, or a material constraint is a decision to address explicitly, not an incidental refactor.

## Select a feedback strategy

- For new behavior, important coverage gaps, or a test-design task, read [Behavior and test design](references/testing.md).
- When external effects, mocks, clocks, fakes, or integration boundaries matter, read [Dependency fidelity](references/fidelity.md).
- For behavior-preserving restructuring or broad movement, read [Safe refactoring](references/refactoring.md).
- For stored data, published schemas, or mixed-version rollout changes, read [Migration and recovery](references/evolution.md).

Use the smallest feedback loop that can actually catch the target error. For an appropriate behavior change, establish a meaningful failing test, implement one useful slice, then verify it before expanding. Existing strong protection may be sufficient for a mechanical change. Refactor while the relevant behavior remains verified; do not reserve all improvement for a ceremonial final phase.

Avoid speculative abstractions and unrelated cleanup. Retain failure semantics as well as successful results. Select test boundaries from risk and existing project practice; do not repeatedly ask permission for already-authorized routine tests.

## Diagnose failures honestly

Separate new regressions, existing baseline failures, and environment problems. Compare against the original state in an isolated copy when needed; do not reset or stash user changes merely to obtain a baseline. Never weaken a valid assertion or alter an expected result just to make an incorrect implementation pass.

If the user prohibits tests, honor that instruction and describe the result as statically checked or unverified. Tool unavailability is not a passing result.

## Complete the task

Run the checks required by the project and the change's actual risk. Broaden or repeat them when further edits, failures, or unresolved evidence warrant it. Reconcile requested behavior, actual changes, and validation evidence; inspect the final diff for accidental scope growth and remove only this task's temporary instrumentation.

Review the final behavior against acceptance independently of test success: trace the changed success and failure paths, affected callers, ownership, and compatibility. Fix concrete defects found within scope. Passing tests only cover what they exercise; self-review does not claim an independent review.

Check whether this change left related design, ADR, context, or operational documentation inaccurate. Update affected maintained artifacts within scope, link actual verification evidence where relevant, and leave accurate documents untouched. Explicit read-only or file-only limits still apply: report the precise outstanding mismatch instead of editing outside them. Routine in-scope synchronization needs no separate approval ceremony.

Reconcile existing implementation and verification status with the delivered scope, including partial completion, blocked checks, and stale results. Keep design or ADR acceptance separate; writing code cannot accept a proposal. Link the authoritative plan or evidence rather than maintaining duplicate progress records.

For planned units, record results and downstream-relevant changes where the task is maintained, then continue the next authorized ready unit. Finish the shared integration checks before claiming the whole change complete; completing one task does not complete the user's request. On interruption, preserve the current unit, remaining work, and next action so continuation does not depend on the full conversation.

Report what changed, what ran and its result, and remaining limitations. Compilation, unit tests, integration checks, and runtime acceptance have distinct meanings. Commit, push, deploy, or publish only within the task's authorization; implementation itself does not imply those actions.
