# Domain Language and Durable Decisions

Use this when concepts, identity, relationships, or invariants are being decided. Reading existing vocabulary alone does not require rewriting the model.

## Model meaning before representation

Find the project's terminology and decision conventions. Compare domain descriptions, current code, and the user's intended behavior. Code provides evidence of implementation, not automatic authority over business meaning.

For a disputed concept, establish its identity, lifetime, owner, allowed changes, relationships, and invariants. Distinguish a definition from an instance, a logical resource from a running allocation, ownership from access, and an entity from a snapshot when the scenario depends on that distinction.

Use concrete counterexamples. If “model” names an algorithm definition, a trained artifact, and a deployment, ask what deletion means for each, whether multiple deployments share one artifact, and whether a later training run changes existing deployments. These observations determine whether separate identities are needed; similar field names do not.

A bounded context is justified by differences in language and model authority, invariants, lifecycle, or ownership—not by a table, noun, team label, or convenient folder. Specify the translation or explicit agreement across contexts instead of forcing one global definition.

## Record useful language

Choose canonical terms where ambiguity has consequences and explain important excluded meanings. Preserve established project language unless there is a concrete reason to change it. Do not silently rename concepts throughout the repository while discussing one design.

Keep definitions concise and domain-specific. Use the existing glossary or design location; `CONTEXT.md` may have broader duties and is not universally a dictionary. Create a vocabulary artifact only when it has material information and an actual consumer.

Once a term is settled within the task's decision authority, record its definition, context, and meaningful aliases in the owning artifact immediately rather than collecting unrecorded decisions until handoff. Keep unresolved names visibly provisional. For an authorized rename, update the relevant code, tests, and maintained documentation in the same reviewable change; a design-only task describes the required propagation without performing it. Published APIs, events, and stored schemas need deliberate compatibility treatment.

## Record a decision when its reasoning must survive

A durable record is useful when a future maintainer could reasonably reconsider an expensive or surprising choice without knowing its constraints and alternatives. Routine local details do not need ADRs.

A useful decision record identifies context and pressure, the decision, meaningful alternatives, decisive reasons, consequences, and when to revisit it. Include scope and explicit decision status. Reuse useful parts of the project's template, correcting omissions or ambiguous status within scope. Link implementation plans and evidence where they live rather than forcing an ADR to duplicate all tasks and test details.

Preserve historical intent: a superseding decision should identify what changed and link to the earlier decision. Do not silently rewrite an accepted record so it appears always to have said the new thing. Do not mark a proposal as accepted by a person who has not accepted it.

Distinguish the evolving current design from historical decision rationale. Update a draft as the choice develops. For an accepted ADR, maintain its status and append dated implementation evidence or later findings without erasing the original reasoning. Reversing the core decision calls for a new superseding record and links in both directions. Keep any existing decision index and affected references current. Acceptance, implementation completion, and verified operation are separate facts.

Apply status changes when the authorized decision actually occurs and record the date, reason, and decision authority or supporting reference. Implementation or a successful test does not change a proposal into an accepted decision; an implementation failure does not automatically reject an accepted decision. Explain when new evidence requires reconsideration and preserve the current decision until it is actually changed.

## Default document lifecycle

Use these meanings for maintained designs and ADRs. This is the bundle's recommended convention, not a claim that every upstream uses one state machine.

| Dimension | Default states and meaning |
|---|---|
| Decision | `draft`: being developed; `proposed`: ready for a decision; `accepted`: authorized choice; `rejected`: considered and declined; `deprecated`: no longer governs new work without a direct replacement; `superseded`: replaced by a linked decision |
| Delivery | `not-started`, `in-progress`, `blocked`, `implemented`; partial completion stays `in-progress` with completed and remaining scope identified |
| Verification | Per criterion: `not-run`, `passed`, `failed`, `blocked`, `stale`; each result identifies scope/revision, check, date, and evidence or blocker |

A maintained design or ADR should expose its decision status and status-change date, plus a link to the delivery plan and verification evidence when these exist. Inline concise delivery and verification entries when there is no separate owner; do not create empty plan or evidence files. Use the user's language or equivalent labels while preserving these meanings. A single `done` or `approved` field cannot stand for all three dimensions. Not-applicable work should be identified with a reason, never represented as passed.

Transitions follow events, not a compulsory sequence: a sufficient authorized decision can directly establish `accepted`. Withdrawal of an unaccepted proposal may use `rejected` with a withdrawal reason; a precise existing `withdrawn` state is also valid. Retiring an accepted decision uses `deprecated` or `superseded`, not retroactive rejection. A substantive revision of an accepted design preserves the accepted baseline and identifies the changed proposal until a new decision is made; an already-authorized revision records that decision without asking again.

When adopting this convention, map old labels from their documented meaning and actual evidence. If a label is ambiguous, retain it as historical data and identify the unresolved status rather than inventing acceptance or verification. Improve deficient metadata on the documents in scope; do not migrate the entire repository just because one document is being edited. Preserve stable paths and links, account for readers that parse status fields, and respect explicit project constraints. In read-only or excluded files, report the required change. Existing custom alone is not a reason to preserve a misleading state model.

Route information to its maintained owner: behavior and acceptance to the specification/design, durable trade-offs to the ADR, language to the declared glossary, project constraints to the established guidance or context document, and temporary progress to the active plan. Link shared evidence instead of copying the same changing facts into every document. Do not repurpose an existing context file or impose a new directory convention.

The user's requested edit boundary still applies. If only `design.md` may change, record a conflict with another document there and explain its effect; do not edit the ADR or glossary merely because consistency would be convenient.
