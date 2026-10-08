---
name: repo-hardening
description: Find recurring engineering mistakes in a repository and make them harder or impossible to repeat by changing the strongest owning layer: architecture, types, APIs, lint or CI, tests, tooling, or instructions. Use when the user asks to stop agents or contributors from repeating the same repository mistake, turn repeated review corrections into enforceable guardrails, or harden a codebase against recurring failure classes. This is repository and engineering-process hardening, not security hardening; one-off bugs belong to diagnosis and ordinary current-change inspection belongs to review.
---

# Repository Hardening

Turn repeated engineering mistakes into durable prevention. Start from evidence that a failure class has happened, identify the surface that actually owns it, and strengthen that surface instead of adding another reminder by default.

## Confirm that this is a recurrence problem

Use this Skill when the task is to prevent a class of mistakes from recurring across future changes or agent runs. Useful evidence includes repeated reverts, review corrections, CI failures, incident follow-ups, agent transcripts, duplicated workarounds, or the same user correction appearing again.

A single defect is normally diagnosis. A review of one current change is review. Designing a new subsystem is design. Editing or auditing an Agent Skill as the primary task is Skill development. Implementing an already-decided guardrail is implementation.

One severe occurrence can still reveal a missing hard contract, but do not manufacture a "pattern" merely to justify repository-wide changes.

## Attribute the failure before adding rules

Verify that the historical mistake still applies to the current repository and cluster examples by root cause, not wording. Name the behavior that should have been impossible or reliably rejected and the surface that owns that contract.

Do not assume that more instructions are the fix. If the repository or Skill already stated the correct rule and the failure came from model variance, unavailable context, a broken tool, product behavior, or infrastructure, fix or report that owning surface instead. Repeating the same sentence in another file is not hardening.

Read [Enforcement and proof](references/enforcement.md) before proposing or applying a guardrail.

## Prefer the strongest proportionate enforcement

Prefer a mechanism that makes the wrong path unavailable or visibly fail:

1. simplify ownership, API shape, or architecture so there is one supported path;
2. make invalid states or calls unrepresentable with types or public boundaries;
3. reject bad changes with lint, dependency rules, CI, or another deterministic check;
4. provide a canonical helper, generator, script, or tool when repetition is mechanical;
5. protect the behavior with a regression test;
6. use documentation, AGENTS files, or Skills for judgment that cannot be enforced mechanically.

This is an ordering heuristic, not a demand to redesign the repository. Choose the highest useful layer whose cost and blast radius fit the failure.

## Prove the prevention

Where feasible, replay a real historical mistake or a minimally faithful version of it against the new guardrail. Show that the guardrail rejects the bad case for the intended reason and still permits the valid path.

Do not claim a mistake is "impossible" because a document now warns against it. State exactly what the mechanism prevents, what it only detects, and what remains dependent on judgment.

## Respect scope and ownership

Read-only hardening requests produce findings and proposed enforcement, not unrequested repository edits. When changes are authorized, keep them bounded to the proven recurrence. Do not create a new framework for a two-line rule, and do not preserve obsolete parallel paths merely to avoid migrating internal callers when coordinated removal is safe.

If the correct owning surface is an Agent Skill, use the Skill-development rules for that edit rather than inventing a second Skill-authoring process here.

## Deliver the hardening result

For each material failure class, report:

- the concrete recurrence evidence;
- the owning surface and reusable rule;
- the enforcement level chosen and why a stronger level was unnecessary or unsuitable;
- the proof that the guardrail catches the historical mistake or faithful replay;
- remaining cases that are still not mechanically prevented.

No recurrence evidence or no verified owning surface is a valid reason to make no change.
