---
name: work-plan
description: Organize software work into unresolved decisions or verifiable implementation tasks with dependencies and completion evidence. Use for delivery planning, task decomposition, broad migrations, and recovering an existing execution plan. Do not redesign settled requirements or force a planning artifact on a clear small edit.
---

# Engineering Planning

Make the next useful work and its prerequisites explicit. Communicate in the user's language. Begin from the current request, existing decisions, actual artifacts, and observed progress rather than assuming every task is still unstarted.

## When the route is uncertain

Build a decision map rather than pretending implementation is ready. Each material question should name:

- the decision or deliverable it blocks;
- known constraints and unsettled prerequisites;
- the evidence, experiment, or user choice needed;
- what would count as resolution.

Distinguish a precise unanswered question from an area that cannot yet be specified. Resolve prerequisites before manufacturing downstream details. Facts can be investigated, alternatives evaluated, or uncertainties tested; these are methods, not mandatory separate tickets or Skill invocations.

Keep the destination and exclusions visible. Discovering a new possibility does not put it in scope. Already-defined work that does not depend on the uncertainty can proceed when execution is authorized.

## When work is ready to arrange

Choose the execution shape by outcome boundaries, real dependencies, context burden, verification, and independent continuation needs. A clear small edit can proceed without a planning artifact; several bounded steps may need only a checklist. Work that must be executed or resumed independently needs a task specification. This may be a plan section, an existing issue, or a separate file, not a second design document. Read [Delivery and migration planning](references/delivery.md) when decomposition or an independently executable unit is needed.

Prefer small outcomes that can be demonstrated or verified. A task should state its deliverable, relevant acceptance requirements, real blockers, validation, and any necessary write boundary. A layer name such as “backend” is not a completion criterion. Keep the plan about sequencing and results; reference the design rather than copying it or prewriting implementation and test code. A small interface or data example is useful only when it resolves material ambiguity.

Include necessary updates to existing design, decisions, terminology, and operating documentation in the affected task's completion criteria. Name the owning artifact and the change that triggers its update; do not add a generic documentation phase or require new ADR/CONTEXT files for every task. Planning alone does not authorize changing those governing artifacts.

Prefer vertical slices when one end-to-end behavior can remain working. For a mechanical change across many consumers, use a compatibility expansion, bounded consumer migrations, then retirement. When intermediate work cannot pass independently, name the shared integration point and do not advertise those tasks as independently shippable.

Check missing acceptance coverage, cycles, false dependencies, overlapping writers, and shared environments. Parallel scheduling is appropriate only where both dependencies and the current harness permit it; a plan is not authorization to launch other agents.

## Keep state truthful

Use the project's existing task system or a proportionate local checklist. Publishing external tickets follows the user's authorization; a request to draft a plan does not require creating a tracker account or installing a workflow. Do not force one ticket per session or estimate work from a fixed token budget.

Use delivery states `not-started`, `in-progress`, `blocked`, and `implemented`; identify completed and remaining scope for partial work. Track verification separately per criterion as `not-run`, `passed`, `failed`, `blocked`, or `stale`, with evidence. Equivalent local labels can remain; improve a legacy single `done` field when it hides these distinctions. Record blockers as actionable missing inputs. If design or code changes, update affected dependencies, acceptance references, and stale verification claims while retaining decisions that still hold.

Keep the plan authoritative for delivery progress where the project assigns it that role. Reconcile any in-scope design summary or link it to the plan when work starts, becomes partial or blocked, or completes. Progress and successful verification do not themselves accept or reject a design or ADR.

Deliver the plan, important assumptions, and the next executable unit. Stop at the plan for a planning-only request; continue authorized implementation when planning was just a necessary part of that task.
