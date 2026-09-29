---
name: implement
description: Deliver defined software changes with proportionate verification, or independently design tests and add meaningful coverage. Use for features, bounded fixes, behavior-preserving refactors, frontend implementation, test plans, and test implementation. Root-cause investigation and read-only review are different tasks.
---

# Implementation and Tests

Deliver the requested behavior and evidence that it works. Treat accepted requirements, design decisions, and frontend prototypes as implementation inputs rather than invitations to restart design exploration.

## Establish the working basis

Read applicable project instructions, relevant decisions, nearby code, callers, tests, and existing changes. Identify acceptance requirements, project conventions, appropriate verification, and known baseline failures when practical.

Use a direct edit for a bounded change. For larger work, keep only the decomposition needed to preserve coherent outcomes, dependencies, and verification. Do not require another installed Skill or a separate specification file when the task is already clear.

Resolve ordinary implementation details within scope. If actual code or environment contradicts a governing design, surface the concrete mismatch instead of silently changing product behavior or ownership.

## Load only the needed implementation lens

- For frontend product code, read [Frontend implementation](references/frontend.md).
- For new behavior, important coverage gaps, or a test-design task, read [Behavior and test design](references/testing.md).
- When external effects, mocks, clocks, fakes, or integration boundaries matter, read [Dependency fidelity](references/fidelity.md).
- For behavior-preserving restructuring or broad movement, read [Safe refactoring](references/refactoring.md).
- For stored data, published schemas, or mixed-version rollout changes, read [Migration and recovery](references/evolution.md).
- When implementation changes maintained project facts or decisions, read [Maintaining project documents](references/documents.md).

Do not load every reference by default.

## Implement with the smallest trustworthy feedback loop

Protect unrelated work. Prefer existing architecture, components, naming, and testing patterns when they remain sound. Avoid speculative abstraction and unrelated cleanup.

For suitable behavior changes, establish evidence that can fail for the intended reason, implement one useful slice, and verify before expanding. Existing strong protection may be sufficient for mechanical work. Never weaken a valid assertion merely to make an implementation pass.

Separate regressions caused by the change, pre-existing baseline failures, and environment problems. Tool unavailability is not a passing result.

## Complete the task

Run checks proportionate to the actual risk and project requirements. Inspect the final behavior independently of test success, including important failure paths, affected callers, compatibility, and accidental scope growth.

Keep production frontend work distinct from frontend exploration: an accepted prototype or design should be implemented faithfully unless real constraints require a change. Conversely, prototype code is not automatically production architecture.

Update maintained project documents when the delivered change makes them inaccurate and the update is within scope. Keep design acceptance, implementation completion, and runtime verification as separate conclusions.

Report what changed, what was actually verified, and remaining limitations. Commit, push, deploy, or publish only when authorized.
