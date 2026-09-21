---
name: tech-design
description: Design or revise software behavior, domain models, technology choices, interfaces, and system architecture. Use for technical decisions, API evolution, runtime or source layout, and maintaining designs or ADRs. Select only the needed modes. Fact-finding alone, implementation scheduling, read-only review, and visual styling are separate tasks.
---

# Software Design

Turn the requested problem into decisions an implementer can use and a reviewer can verify. Preserve the user's outcome, existing decisions, and authorized scope. A question or suggestion is input to evaluate, not an instruction to reverse the previous design. Communicate in the user's language; retain the project's established terminology.

## Select the work

Read the relevant project instructions, current design, accepted decisions, and enough implementation to distinguish intended behavior from current behavior. Choose references by the unresolved question; several may apply, but they are not a pipeline.

| Question | Read before resolving it |
|---|---|
| What behavior, scope, and acceptance are intended? | [Requirements](references/requirements.md) |
| What do concepts mean, or how should decisions and document status be maintained? | [Domain and decisions](references/domain.md) |
| Adopt, adapt, combine, build, defer, or keep what exists? | [Technology choices](references/selection.md) |
| What responsibility and complete caller contract should a module own? | [Architecture and module depth](references/architecture.md) |
| Consumers evolve independently, or a public API, event, or schema changes | [Published interfaces](references/contracts.md) |
| Work crosses processes, stores, or asynchronous workers | [Runtime behavior](references/systems.md) |
| Several consequential interface shapes are plausible | [Competing designs](references/alternatives.md) |
| Where should code live, and how is dependency direction enforced? | [Structure and migration](references/structure.md) |
| Routes, UI reuse, state/data ownership, or client/server boundaries matter | [Frontend structure](references/frontend.md) |

For a design-only request, produce or revise the design. For a read-only assessment, report findings without rewriting its subject. An already-authorized implementation may use these methods to resolve necessary design details without restarting a separate approval workflow.

## Keep the decision grounded

Separate known requirements, verified facts, existing implementation, assumptions, and actual decisions. Investigate facts directly. Ask only for missing business choices or constraints that materially change the result and cannot reasonably be inferred. Resolve ordinary reversible details within scope yourself.

Evaluate proposals against all important constraints. A shorter name, smaller file, newer framework, or fewer layers is not sufficient evidence of a better overall design. State what a recommendation improves, what it costs, and what evidence would overturn it.

Use representative caller or user scenarios to connect behavior, responsibilities, failures, and acceptance. Research or experiments may supply missing evidence; another installed Skill is not a prerequisite. Reuse sound existing artifacts rather than reproducing them under new filenames.

## Deliver a usable decision

Maintain the requested design as scope, constraints, and the chosen approach become settled or change. Record resolved domain language and warranted decisions as they emerge, using the project's existing document roles and locations. A file named `CONTEXT.md` is not necessarily a glossary. Create an artifact only when there is material content and a downstream reader; a discussion alone does not require a new document set.

Prefer the requested existing document. Give the chosen approach, decisive trade-offs, necessary contracts, verification path, and unresolved blockers at the depth the task requires. Preserve decision status: a recommendation is not automatically a team-approved ADR. Conversely, do not ask again for an action the user has already authorized.

Keep design organization separate from implementation decomposition. Length alone is not a reason to split a design. When independently maintained topics justify splitting an existing or user-requested single document, propose concrete boundaries and navigation and obtain agreement unless reorganization is already authorized. Respect an explicit choice to keep it whole; use stable sections and targeted reading, and do not require document splitting before implementation can be divided into tasks. An authorized split preserves the original entrypoint, governing constraints, acceptance coverage, decision history, and affected links.

Describe behavior, decisions, interfaces, and failure semantics without prewriting production classes or complete tests. Use a small signature, payload, or pseudocode example only where it resolves a consequential ambiguity; reference maintained code or contracts instead of copying them. Detailed execution sequencing belongs in the plan, not another implementation embedded in the design.

Use the default lifecycle in [Domain and decisions](references/domain.md) for maintained designs and ADRs. Existing conventions are evidence to inspect, not proof of good practice: within the authorized document scope, replace ambiguous status with explicit decision, delivery, and verification meanings. Preserve equivalent local labels, historical evidence, and required tooling compatibility. After material design changes, reassess affected conclusions against the new scope.

Check terminology, lifecycle, ownership, failure behavior, migration, and acceptance for contradictions across the current design. If a governing decision conflicts, identify the conflict where the user authorized changes; do not silently rewrite the governing document. State which work can proceed and which depends on unresolved evidence. Design readiness, implementation completion, and runtime acceptance are different conclusions.
