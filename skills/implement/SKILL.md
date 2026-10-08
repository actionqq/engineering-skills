---
name: implement
description: Deliver defined software changes with proportionate verification, or independently design tests and add meaningful coverage. Use for features, bounded fixes, behavior-preserving refactors, frontend implementation, test plans, and test implementation. Root-cause investigation and read-only review are different tasks; a test-plan-only request does not authorize product edits.
---

# Implementation and Tests

Deliver the requested behavior and evidence that it works. Communicate in the user's language. A clear outcome in the conversation can define the work; a complete specification or prior prototype is not required. Preserve accepted decisions and resolve ordinary implementation details within scope.

## Establish the working basis

Read applicable project instructions, relevant decisions, nearby code, callers, tests, and existing changes. Identify acceptance requirements, project conventions, appropriate verification, and known baseline failures when practical.

Use a direct edit for a bounded change. For larger work, keep only the decomposition needed to preserve coherent outcomes, dependencies, and verification. Do not require another installed Skill or a separate specification file when the task is already clear.

For planned units, read the current brief, relevant design, prerequisites, constraints, and acceptance. Verify prerequisite outputs against actual artifacts and resolve stale instructions before editing. Keep failure semantics and cross-cutting constraints when narrowing context. Adjust an oversized unit within scope; routine local planning needs no new approval gate.

Resolve ordinary implementation details within scope. If actual code or environment contradicts a governing design, surface the concrete mismatch instead of silently changing product behavior or ownership.

## Load only the needed implementation lens

- For user-facing frontend code, read [Frontend implementation](references/frontend.md).
- For new behavior, important coverage gaps, or a test-design task, read [Behavior and test design](references/testing.md).
- When external effects, mocks, clocks, fakes, or integration boundaries matter, read [Dependency fidelity](references/fidelity.md).
- For behavior-preserving restructuring or broad movement, read [Safe refactoring](references/refactoring.md).
- For stored data, published schemas, or mixed-version rollout changes, read [Migration and recovery](references/evolution.md).
- When implementation changes maintained project facts, exposes a design mismatch, or produces durable findings, read [Maintaining project documents](references/documents.md). Record settled changes as work proceeds.

Select references from the changed behavior and its risks, not just the repository's technology stack. Read the relevant sections; do not turn a bounded change into a redesign or a whole-product audit.

## Implement with the smallest trustworthy feedback loop

Protect unrelated work. Prefer existing architecture, components, naming, and testing patterns when they remain sound. Avoid speculative abstraction and unrelated cleanup.

For suitable behavior changes, establish evidence that can fail for the intended reason, implement one useful slice, and verify before expanding. Existing strong protection may be sufficient for mechanical work. Never weaken a valid assertion merely to make an implementation pass.

Separate regressions caused by the change, pre-existing baseline failures, and environment problems. Use an isolated copy when baseline comparison is needed; do not reset or stash user changes for it. Honor explicit testing limits and describe static-only or unverified results accurately. Tool unavailability is not a passing result.

## Complete the task

Run checks proportionate to the actual risk and project requirements. Inspect the final behavior independently of test success, including important failure paths, affected callers, compatibility, and accidental scope growth.

Update maintained project documents when the delivered change makes them inaccurate and the update is within scope. Keep design acceptance, implementation completion, and runtime verification as separate conclusions.

For planned units, record results and downstream-relevant changes in the maintained plan, continue the next authorized ready unit, and finish shared integration checks before claiming the whole request complete. On interruption, preserve the current unit, remaining work, and next action.

Report what changed, what was actually verified, and remaining limitations. Commit, push, deploy, or publish only when authorized.
