# Domain Language and Durable Decisions

Use this when concepts, identity, relationships, invariants, or durable technical decisions are being established. Reading existing vocabulary alone does not require rewriting the model.

## Model meaning before representation

Find the project's terminology and decision conventions. Compare domain descriptions, current code, and intended behavior. Code is evidence of implementation, not automatic authority over business meaning.

For a disputed concept, establish its identity, lifetime, owner, allowed changes, relationships, and invariants. Distinguish a definition from an instance, a logical resource from a running allocation, ownership from access, and an entity from a snapshot when the scenario depends on it.

Use concrete counterexamples. Similar fields or tables do not prove two concepts share identity or lifecycle. A bounded context is justified by differences in language, model authority, invariants, lifecycle, or ownership—not by a convenient folder or team label. Make translations or agreements across contexts explicit.

## Record useful language

Choose canonical terms where ambiguity has consequences and explain important excluded meanings. Preserve established project language unless there is a concrete reason to change it. Use the existing glossary or design location; `CONTEXT.md` may have broader duties and is not universally a dictionary.

Once a term is settled within the task's authority, record its definition, context, and meaningful aliases in the owning artifact. Keep unresolved names visibly provisional. An authorized rename should propagate through the relevant code, tests, and maintained documentation; published APIs, events, and stored schemas need deliberate compatibility treatment.

## Record decisions whose reasoning must survive

Create or update a durable decision record when a future maintainer could reasonably reopen a costly, surprising, or consequential choice without its constraints and alternatives. Routine implementation detail does not need an ADR.

Preserve context, the decision, decisive reasons, meaningful alternatives where useful, consequences, scope, and decision status. Link implementation plans and verification evidence where they are maintained instead of copying their changing state into the ADR.

Accepted decisions preserve history. When the governing choice changes, use the project's amendment or supersession convention and retain the old rationale. Do not mark a proposal accepted because code exists, and do not mark an accepted decision rejected because implementation or verification failed.

## Default document lifecycle

Use the repository's decision vocabulary when it is clear. Without one, these decision states are sufficient:

| State | Meaning |
|---|---|
| `draft` | The decision is still being developed. |
| `proposed` | The choice is ready for an authorized decision. |
| `accepted` | The governing choice has been authorized. |
| `rejected` | The proposal was considered and declined or withdrawn with a recorded reason. |
| `deprecated` | An accepted choice no longer governs new work and has no direct replacement. |
| `superseded` | A linked decision replaces the accepted choice. |

Transitions follow actual decisions, not a mandatory sequence. Record the status-change date and the authority or supporting reference when the project needs that trace. A substantive revision of an accepted design preserves the accepted baseline until the revised choice is actually authorized.

Delivery progress and verification evidence have different owners and lifecycles. Link the active plan and evidence when they exist; do not use `accepted`, `implemented`, `passed`, or one legacy `done` field as synonyms. If old metadata is ambiguous, preserve it as historical data and identify the unresolved meaning rather than inventing approval or verification.

Route information to its maintained owner: behavior and acceptance to the specification/design, durable trade-offs to the ADR, language to the declared glossary/context, and temporary progress to the active plan. Link shared evidence instead of copying changing facts into every document. Respect explicit read-only and file boundaries.
