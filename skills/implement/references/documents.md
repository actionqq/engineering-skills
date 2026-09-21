# Maintaining Project Documents

Use when implementation affects documented behavior, architecture, terminology, or operating constraints. Inspect the project's locations, templates, document roles, and decision authority. Reuse what preserves clear ownership and truthful status; improve deficient conventions within scope using the defaults below. Preserve explicit constraints and tooling compatibility. Read relevant material rather than collecting every document in the repository.

## Record information where it is maintained

| Change or finding | Maintained owner |
|---|---|
| Requirements, observable behavior, acceptance, or chosen technical approach | Current specification or design |
| Consequential architectural choice and rejected alternatives | Existing ADR mechanism |
| Domain definition, canonical name, or alias | Owning context's declared glossary |
| Stable project constraint, setup requirement, or non-obvious operating rule | Existing project guidance, context, or operational documentation |
| Progress, blocker, sequencing, or temporary workaround | Active plan or status record |
| Regression or observable behavioral invariant | Code and executable tests, with documentation where readers need it |

`CONTEXT.md` has the role this project gives it. Do not turn a project overview into a glossary or add task logs to a domain dictionary. Reuse existing owners; create a document only when material information needs one. Link a maintained fact or evidence record rather than duplicating it across documents.

## Reconcile during implementation

When implementation disproves a design assumption, identify the mismatch and its effect. Resolve ordinary details within existing authority and update the current design as the approach settles. A change to scope, public behavior, or an accepted architectural constraint needs an explicit decision; do not silently rewrite the design to legitimize accidental code behavior. Continue independent authorized work while a necessary decision remains unresolved.

Record resolved terms promptly. When a rename is authorized, keep the glossary and affected code, tests, and maintained documentation in the same reviewable change; preserve or deliberately migrate published API/event/schema names. For structural migrations, refresh affected package indexes, diagrams, onboarding instructions, and moved-path links.

## Preserve decision history

Use a lightweight ADR for reasoning that would otherwise be lost; routine local fixes do not need one. Link implementation tasks and evidence where they already live unless the project requires them inside the ADR.

Update draft decisions as they develop. Maintain accepted-record status and append dated outcomes or new evidence without rewriting the original rationale. A reversal of the core decision needs a superseding ADR with links in both directions and an updated index where one exists. Do not claim human acceptance that did not occur.

After implementing a decision, check its applicable verification criteria and record results or links in the project's designated evidence location, including an ADR outcome section where appropriate. Mark blocked or unrun checks honestly. An accepted decision is not proof of implementation, and a passing unit test is not runtime acceptance.

## Maintain status at the event that changes it

Use this default state model. Equivalent local labels are acceptable when their meanings remain separate; ambiguous legacy conventions should be corrected within the authorized document scope.

| Dimension | Default states |
|---|---|
| Decision | `draft`, `proposed`, `accepted`, `rejected`, `deprecated`, `superseded` |
| Delivery | `not-started`, `in-progress`, `blocked`, `implemented` |
| Verification | Per criterion: `not-run`, `passed`, `failed`, `blocked`, `stale` |

- **Decision:** `draft` is being developed, `proposed` awaits a decision, and `accepted` records an authorized choice. `rejected` means declined; withdrawal can carry a reason or retain a precise local `withdrawn` label. `deprecated` retires an accepted choice without a direct replacement; `superseded` links its replacement. Record the status-change date, reason, and authority or supporting reference. A sufficient authorized decision need not pass through every preceding state.
- **Implementation:** track the agreed scope in the maintained plan. Partial work stays `in-progress` with completed and remaining scope identified; `implemented` means the scoped implementation exists, not that verification passed. If the design carries a progress summary, reconcile it or link the plan instead of maintaining contradictory copies.
- **Verification:** what was checked, against which scope or revision, with what result and evidence. Update when a check runs, fails, is blocked, or becomes inapplicable; preserve distinctions between static review, local tests, integration checks, and runtime acceptance.

A maintained design or ADR should expose decision status and its change date, and link the delivery plan and evidence where they exist. Without separate owners, use concise inline delivery and verification entries rather than creating empty files. Record not-applicable work with a reason, not a fabricated pass. Never map an old `done` label to accepted, implemented, and passed without evidence for each meaning. Preserve ambiguous old labels as historical data while identifying unresolved status; do not guess the date or approving person.

Improve misleading fields on affected documents without a repository-wide template migration. Preserve stable links and required machine-readable fields or adapt their consumers within scope. Explicit read-only/file boundaries still apply. If a substantive revision changes an accepted design, preserve the accepted baseline and distinguish the revised proposal until the actual decision occurs; existing authorization can supply that decision.

When the design, code, or environment changes materially, reassess affected prior evidence before carrying forward a completion claim. Preserve the historical result and mark the scope needing revalidation; do not erase passing history or invalidate unrelated checks. A completed local implementation can still have blocked integration verification. Neither state implies the design was rejected.

## Finish without unnecessary document changes

Inspect the affected documents against the final behavior and observed evidence. If they remain accurate, leave them unchanged. Before removing a temporary artifact, preserve any lasting constraint or useful evidence in its maintained owner within scope; otherwise report the unresolved destination and retain needed material.

Honor explicit read-only and file-only boundaries. Report excluded document mismatches with the affected location and required correction. Do not use documentation consistency to expand the task, edit unrelated project policy, or update global memory or Skills from one project's local experience.
