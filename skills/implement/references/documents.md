# Maintaining Project Documents

Use the project's conventions, status, and references to identify which affected sections still guide work. A design can remain current after delivery, and a document can contain both current guidance and historical material.

## Route durable information to its owner

| Change or finding | Maintained owner |
|---|---|
| Requirements, observable behavior, acceptance, or chosen technical approach | Current specification or design |
| Consequential architectural choice and rationale | Existing ADR mechanism |
| Domain definition, canonical name, or alias | Owning glossary or context artifact |
| Stable project constraint, setup requirement, or operating rule | Existing project guidance or operational documentation |
| Progress, blocker, sequencing, or temporary workaround | Active task, plan, or status record for this change |
| Regression or observable behavioral invariant | Code and executable tests, with documentation where readers need it |

`CONTEXT.md` has the role this project gives it. Record settled changes within scope in the current owner as work proceeds. Link to that owner wherever readers need the same information.

## Reconcile implementation with governing material

When code disproves a design assumption, identify the mismatch and its effect. Resolve ordinary details within existing authority, but do not silently rewrite scope, public behavior, or an accepted architectural constraint to legitimize accidental implementation.

Record resolved terminology promptly. For an authorized rename, update affected code, tests, and maintained documentation together while treating published APIs, events, and schemas according to their compatibility requirements. Structural migrations should refresh affected indexes, diagrams, onboarding instructions, and moved-path links when those artifacts are maintained.

Preserve historical rationale and evidence. When authorized to correct a historical claim or add a follow-up, distinguish the new information with a date. Follow the project's amendment or supersession convention when a governing choice is replaced. Reserve ADRs for consequential decisions.

## Keep state meanings separate

Use the project's existing owners for decisions, progress, and verification, which can be separate sections of the same document. Update the state the work actually changes.

- code existing can advance delivery progress but does not accept a decision;
- a passing check records verification for its stated scope but does not prove runtime acceptance;
- a blocked or unrun check stays blocked or unrun rather than becoming a pass;
- later code, design, or environment changes can make earlier evidence stale without erasing its historical result.

Do not copy a parallel status model into every document. If legacy metadata conflates accepted, implemented, and verified, correct the affected owner within scope or report the ambiguity when it is outside the write boundary.

## Finish without document churn

Check affected current guidance and active records against the agreed behavior and observed evidence. Report material discrepancies outside the task's write scope. Before removing a temporary artifact, preserve any lasting constraint or useful evidence in its real owner when that is within scope.

Honor explicit read-only and file-only boundaries. Documentation consistency does not authorize unrelated policy edits, repository-wide template migrations, global memory changes, or Skill changes based on one project's local experience.
