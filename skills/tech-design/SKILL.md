---
name: tech-design
description: Design or revise software behavior, domain models, technology choices, interfaces, and system architecture. Use for technical decisions, API evolution, runtime or source layout, and maintaining designs or ADRs. Select only the needed modes. Agent Skill authoring or instruction review, fact-finding alone, implementation scheduling, read-only review, and visual styling are separate tasks.
---

# Software Design

Turn the requested problem into decisions an implementer can use and a reviewer can verify. Preserve the user's outcome, existing decisions, and authorized scope. A question or suggestion is input to evaluate, not an instruction to reverse the previous design. Communicate in the user's language and retain established project terminology.

## Select the work

Apply this workflow to software decisions, not to creating or revising an Agent Skill's instructions, triggers, or resource organization. Read the relevant project instructions, current design, accepted decisions, and enough implementation to distinguish intended behavior from current behavior. Choose references by the unresolved question; they are not a pipeline.

| Question | Read before resolving it |
|---|---|
| What behavior, scope, and acceptance are intended? | [Requirements](references/requirements.md) |
| What do concepts mean, or how should durable decisions be maintained? | [Domain and decisions](references/domain.md) |
| Adopt, adapt, combine, build, defer, or keep what exists? | [Technology choices](references/selection.md) |
| What responsibility and complete caller contract should a module own? | [Architecture and module depth](references/architecture.md) |
| Consumers evolve independently, or a public API, event, or schema changes | [Published interfaces](references/contracts.md) |
| Work crosses processes, stores, or asynchronous workers | [Runtime behavior](references/systems.md) |
| Several consequential interface shapes are plausible | [Competing designs](references/alternatives.md) |
| Where should code live, and how is dependency direction enforced? | [Structure and migration](references/structure.md) |
| Routes, UI reuse, state/data ownership, or client/server boundaries matter | [Frontend structure](references/frontend.md) |
| How should the resulting design, ADR, or context artifact be organized? | [Design documentation](references/documentation.md) |

For a design-only request, produce or revise the design. For a read-only assessment, report findings without rewriting its subject. An already-authorized implementation may use these methods to resolve necessary design details without restarting a separate approval workflow.

## Keep the decision grounded

Separate known requirements, verified facts, existing implementation, assumptions, and actual decisions. Investigate discoverable facts directly. Ask only for missing business choices or constraints that materially change the result and cannot reasonably be inferred; resolve ordinary reversible details within scope.

Evaluate proposals against the important constraints. State what a recommendation improves, what it costs, and what evidence would overturn it. Use representative caller or user scenarios to connect behavior, responsibilities, failures, and acceptance. Research or experiments may supply missing evidence; another installed Skill is not a prerequisite.

## Deliver a usable decision

Prefer the requested existing artifact and reuse sound maintained material rather than reproducing it under new filenames. Give the chosen approach, decisive trade-offs, necessary contracts, verification path, and unresolved blockers at the depth the task requires. Preserve decision authority: a recommendation is not automatically accepted, and an already-authorized choice does not need another approval gate.

When design work creates or revises a maintained design, ADR, or context artifact, use [Design documentation](references/documentation.md) for the artifact-specific fallback. Keep design organization separate from implementation decomposition. Detailed task order belongs in the plan; production classes and complete tests do not belong in a design merely to make it look executable.

Use [Domain and decisions](references/domain.md) for durable decision status. Delivery progress belongs to the maintained plan and verification results belong to their evidence owner; link them instead of copying parallel state models into the design.

## Check completion

Check terminology, lifecycle, ownership, failure behavior, compatibility or migration, and acceptance for contradictions across the current design. If a governing decision conflicts, identify the conflict within the authorized scope instead of silently rewriting its owner. State which work can proceed and which depends on unresolved evidence.

Design readiness, implementation completion, and runtime acceptance are different conclusions. A design is complete when the material behavior and decisions are clear enough to implement and review without inventing consequential requirements.
