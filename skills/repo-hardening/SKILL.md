---
name: repo-hardening
description: "Find recurring engineering mistakes in a repository and make them harder or impossible to repeat by changing the strongest owning layer: architecture, types, APIs, lint or CI, tests, tooling, or instructions. Use when the user asks to stop agents or contributors from repeating the same repository mistake, turn repeated review corrections into enforceable guardrails, or harden a codebase against recurring failure classes. This is repository and engineering-process hardening, not security hardening; one-off bugs belong to diagnosis and ordinary current-change inspection belongs to review."
---

# Repository Hardening

Turn repeated engineering mistakes into durable prevention. Start from evidence that a failure class has happened, identify the surface that owns the contract, and strengthen that surface instead of adding another reminder by default.

## Confirm the task is recurrence prevention

Use this Skill when the goal is to prevent a class of mistakes across future changes or agent runs. Evidence can include repeated reverts, review corrections, CI failures, incident follow-ups, agent transcripts, or duplicated workarounds.

A single uncertain defect is normally diagnosis. Reviewing one current change is review. Designing a new subsystem is design. Editing an Agent Skill as the primary task is Skill development. Implementing an already-decided guardrail is implementation. One severe occurrence can still reveal a missing hard contract, but do not manufacture a pattern to justify repository-wide work.

## Attribute the failure before changing rules

Verify that the historical mistake still applies to the current repository and cluster examples by violated contract, not wording. Name the behavior that should have been impossible or reliably rejected and the surface that owns it.

If existing guidance already required the correct behavior, do not restate it by default. Check context availability, trigger visibility, model variance, tooling, product behavior, infrastructure, or a stronger repository layer before treating the failure as an instruction gap.

Read [Enforcement and proof](references/enforcement.md) to choose the strongest proportionate mechanism and prove it against the historical class.

## Keep the change bounded

Read-only requests produce findings and proposed enforcement. When changes are authorized, change only what the recurrence evidence supports. Do not create a framework for a two-line rule, and do not keep obsolete duplicate paths merely to avoid a safe coordinated cleanup.

If the owning surface is an Agent Skill, use the Skill-development rules for that edit rather than creating a second authoring process here.

## Deliver the hardening result

For each material failure class, report the recurrence evidence, owning surface, chosen enforcement level, proof against a real or faithful historical mistake, and what remains dependent on judgment.

Do not claim a mistake is impossible because documentation warns against it. No recurrence evidence or no verified owning surface is a valid reason to make no change.
