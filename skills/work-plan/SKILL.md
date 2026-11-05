---
name: work-plan
description: Organize software work into unresolved decisions or verifiable implementation tasks with dependencies and completion evidence. Use for delivery planning, task decomposition, broad migrations, and recovering an existing execution plan. Do not redesign settled requirements or force a planning artifact on a clear small edit.
---

# Engineering Planning

Make the next useful work and its prerequisites explicit. Communicate in the user's language. Begin from the current request, existing decisions, actual artifacts, and observed progress rather than assuming every task is unstarted.

## Plan uncertainty before tasks

When implementation is not ready, identify each material unresolved decision, what it blocks, known constraints, and the evidence or user choice that would resolve it. Investigate facts and testable uncertainties instead of manufacturing downstream task details. Already-defined work that does not depend on the uncertainty can proceed when execution is authorized.

## Choose the lightest useful execution shape

A clear small edit needs no new planning artifact. A short checklist is enough for related steps handled together and can record their dependencies. Use a task specification when a unit needs independent assignment, resumption, or substantial context isolation.

Read [Delivery and migration planning](references/delivery.md) when decomposition, migration sequencing, or an independently executable unit is needed. That reference owns the detailed unit, dependency, parallelism, migration, and replanning method.

Keep the plan about outcomes, prerequisites, and verification. Reference governing designs instead of copying them or prewriting implementation and tests. Include required updates to existing design, terminology, and operating documentation in the affected unit's completion criteria; do not create a generic documentation phase.

Parallel work is appropriate only where dependencies, ownership, mutable state, and the actual harness permit it. A plan is not authorization to launch agents or publish external tickets.

Write tasks as directions a future executor can follow without reconstructing the conversation. Put prerequisites and conditions before actions, name the owning artifact, use the design's established terms, and specify the evidence that distinguishes completion from attempted work. Keep background and rationale linked to their source rather than padding each task with repeated explanation.

## Keep plan state truthful

Use the project's existing task system or a proportionate local checklist. For plans that need explicit state, delivery may use `not-started`, `in-progress`, `blocked`, and `implemented`; partial work remains `in-progress` with completed and remaining scope identified.

When a plan needs ongoing verification tracking, record verification separately per criterion as `not-run`, `passed`, `failed`, `blocked`, or `stale`, with the relevant evidence or blocker. Equivalent local labels are fine when they preserve the distinction. Assignment is not implementation, and implementation is not successful verification.

If requirements, governing design, code, or prerequisites change, update affected dependencies and mark verification stale only where its scope no longer applies. Preserve still-valid decisions and historical results.

Deliver the plan, important assumptions, and the next executable unit. Stop at the plan for a planning-only request; continue authorized implementation when planning was only a necessary part of the task.
