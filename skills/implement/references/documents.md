# Maintaining Project Documents

Use when implementation changes documented behavior, architecture, terminology, or operating constraints. Reuse the project's maintained owners and update only what the delivered change makes inaccurate.

## Route durable information to its owner

| Change or finding | Maintained owner |
|---|---|
| Requirements, observable behavior, acceptance, or chosen technical approach | Current specification or design |
| Consequential architectural choice and rationale | Existing ADR mechanism |
| Domain definition, canonical name, or alias | Owning glossary or context artifact |
| Stable project constraint, setup requirement, or operating rule | Existing project guidance or operational documentation |
| Progress, blocker, sequencing, or temporary workaround | Active plan or status record |
| Regression or observable behavioral invariant | Code and executable tests, with documentation where readers need it |

`CONTEXT.md` has the role this project gives it. Reuse existing owners and link changing facts rather than cloning them across documents.

## Reconcile implementation with governing material

When code disproves a design assumption, identify the mismatch and its effect. Resolve ordinary details within existing authority, but do not silently rewrite scope, public behavior, or an accepted architectural constraint to legitimize accidental implementation.

Record resolved terminology promptly. For an authorized rename, update affected code, tests, and maintained documentation together while treating published APIs, events, and schemas according to their compatibility requirements. Structural migrations should refresh affected indexes, diagrams, onboarding instructions, and moved-path links when those artifacts are maintained.

Preserve accepted decision history. A reversal of the governing choice needs the project's amendment or supersession mechanism; routine fixes do not need a new ADR.

## Keep state meanings separate

Use the lifecycle and labels already owned by the project's design/ADR, plan, and verification records. Implementation should update the event it actually changes:

- code existing can advance delivery progress but does not accept a decision;
- a passing check records verification for its stated scope but does not prove runtime acceptance;
- a blocked or unrun check stays blocked or unrun rather than becoming a pass;
- later code, design, or environment changes can make earlier evidence stale without erasing its historical result.

Do not copy a parallel status model into every document. If legacy metadata conflates accepted, implemented, and verified, correct the affected owner within scope or report the ambiguity when it is outside the write boundary.

## Finish without document churn

Inspect the affected maintained documents against the final behavior and observed evidence. If they remain accurate, leave them unchanged. Before removing a temporary artifact, preserve any lasting constraint or useful evidence in its real owner when that is within scope.

Honor explicit read-only and file-only boundaries. Documentation consistency does not authorize unrelated policy edits, repository-wide template migrations, global memory changes, or Skill changes based on one project's local experience.
