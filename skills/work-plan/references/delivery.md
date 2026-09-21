# Delivery Units, Dependencies, and Migration

Use this for work spanning several verifiable units or requiring coordination.

## Define a unit by its result

A useful unit identifies an observable deliverable, acceptance references, prerequisites, validation, and any necessary ownership or write boundary. Include relevant current paths when they help an executor locate work, but do not invent exact paths merely to make a plan appear concrete.

Prefer a narrow working path through the required layers rather than completing every schema, then every service, then every UI. A slice does not have to touch all layers if the user-visible behavior only needs some. Separate preparatory work only when it creates a necessary test seam, compatibility path, or other prerequisite.

Size units so that context and verification remain manageable, not to a universal token estimate. A description such as “implement API” needs the specific behavior and acceptance that determine done. Mark a genuinely unresolved design dependency rather than handing an executor an invented answer. A coherent unit closes a scoped result and its checks; it need not be one file, commit, or independently deployable change.

## Choose how much execution guidance is needed

| Work shape | Lightest sufficient guidance |
|---|---|
| Clear small change with a bounded check | Execute from the request and existing context; no new planning document |
| Several related steps that remain manageable together | A short checklist with outcomes and verification |
| A unit needing independent assignment, resumption, or substantial context isolation | A task specification that can be read independently |
| Risky interface evolution, data migration, or cross-system behavior | Add the specific compatibility, recovery, and integration conditions the risk requires |

Split when a task combines independently verifiable outcomes or requires too many unrelated decisions and artifacts to work on coherently. Keep tightly coupled steps together when separation merely repeats context or prevents meaningful checks. A large design can remain one document while implementation is divided; a short design may still require several execution units. Document length and file count do not determine task granularity.

## Prepare an independently executable task

A task specification is the execution brief for one unit, not a fresh requirements or design document. Reuse an issue body or a clearly addressable plan section when sufficient; prefer a separate file when independent reading and handoff benefit. Ordinary coding steps inside the unit do not each need a specification.

State the outcome and acceptance, point to the governing design sections, and add only what execution needs: exclusions, prerequisite outputs and release conditions, relevant code entrypoints, constraints, and scoped verification. An unfamiliar executor should be able to start from this brief and its named sources without reconstructing the conversation. Important failure semantics and cross-cutting constraints must not disappear in the summary. Reuse existing source identifiers or revision information where available so changed assumptions can be detected.

Do not duplicate the full design, production functions, or complete tests in the brief. Reference maintained contracts; retain only a short signature, payload, or example when prose leaves a consequential ambiguity. Required detail follows risk, not a mandatory form. A simple unit may need only its goal, sources, and acceptance.

Map the overall outcomes and dependencies first, then elaborate units whose prerequisites are sufficiently known. Later units can retain their deliverable, blockers, and open decisions until they are ready; do not fabricate downstream implementation details. Before declaring a unit ready, ensure its necessary execution guidance exists and the overall acceptance requirements have owners, including shared integration checks.

## Keep execution context bounded

Name the relevant design sections, shared constraints, code entrypoints, and prerequisite results rather than requiring every executor to reload the entire design and task history. Preserve enough context for investigation, editing, and verification; if the prerequisite material is still too broad, revisit the unit boundary instead of deleting essential constraints to meet an arbitrary size target.

Record actual outcomes, checks, remaining work, and downstream effects in the maintained task or evidence record. The next unit loads its brief and necessary current sources, not accumulated transcripts. A fresh session can help when supported, but neither a new session nor another agent is mandatory or authorized by decomposition alone. Creating small files by itself does not bound the context the executor loads.

## Build honest dependency edges

An edge means the dependent work cannot be correctly completed or validated without its prerequisite. State the result that releases it: an agreed contract, available implementation, or a particular passing check, not just an ambiguous “done” label. Shared subject matter alone is not a blocker. Review for cycles, missing prerequisites, unnecessary serialization, and work that appears independent but shares mutable files, data, or deployment state.

For parallel plans, give writers separate responsibility or isolated checkouts and name the integration owner. Two tasks can edit distinct files yet still require integration because they change the same interface. A read-then-write task claim is not a lock.

## Wide refactors

When one mechanical change affects too many consumers for a working vertical slice:

1. Introduce the compatible new form alongside the old.
2. Migrate bounded consumer groups with relevant checks.
3. Verify no required consumers still depend on the old form.
4. Remove the compatibility form and run integration checks.

For example, adding a replacement field may require dual writes, backfill with restartability, read migration, old-version retirement, then removal. Application rollback can be possible while data rollback is not; capture that distinction.

If intermediate groups cannot remain independently valid, specify a shared integration branch or workspace and a final verification unit. Do not promise green intermediate states that the design cannot support. Separate behavior changes, dependency inversion, and mass movement enough to diagnose failures.

## Progress and replanning

Use actual evidence for status transitions. “Implemented” means code exists; “verified” means the stated acceptance has evidence. A task assigned to an executor is not complete. Record blockers with the missing decision, artifact, access, or environment and the next resolution step.

When a requirement, governing design, or prerequisite result changes, trace its affected task briefs and tests, preserve unaffected progress, and remove obsolete dependencies. Reconcile stale briefs before executing them; a task specification cannot override its governing design. If work becomes out of scope, record that explicitly rather than leaving it indistinguishable from an unresolved future task. Passing unit-level acceptance does not replace the plan's shared integration acceptance.

Finish with the next executable unit and the integration/acceptance conditions for the whole effort. Use the existing tracker or a local plan at the scale needed; neither external publishing nor one-file-per-ticket is inherent in this method.
