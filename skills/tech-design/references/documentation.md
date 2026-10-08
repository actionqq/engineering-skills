# Design Documentation

Use this reference when the design work itself must produce or revise a maintained technical document. The design workflow owns the decisions; these rules only keep the resulting artifact useful and consistent.

## Follow existing document authority

Use the user's requested file and the repository's established design, RFC, ADR, context, metadata, and naming conventions before a generic structure. Read neighboring maintained documents when they define the local format. Do not rename or split artifacts merely to match another ecosystem.

## Technical design fallback

When no local template exists, keep a small core:

- context, problem, and relevant current state;
- goals, non-goals, and scope;
- chosen approach and consequential decisions;
- contracts, ownership, lifecycle, failure or compatibility semantics needed to implement safely;
- verification path, risks, blockers, and unresolved questions.

Add architecture/data flow, data model, APIs/events, concurrency/state, security, performance, observability, migration/rollback, or alternatives only when those topics carry material decisions. Do not leave empty ceremonial sections.

A proposal whose decision is still open can show criteria and serious options. Once a choice is settled, write the current design rather than preserving the whole discussion as live alternatives.

Implementation decomposition remains separate. The design may identify prerequisites, migration phases, and evidence required, but detailed task order and ticket breakdown belong in the work plan. A testing section describes what must be proven and at what boundary; it need not duplicate an owned scenario matrix.

## ADR fallback

Use the repository's ADR convention first. Without one, prefer a lean Context / Decision / Consequences record with status and date. Add decision drivers or considered options only when their rationale is worth preserving. Keep implementation progress and verification results linked rather than copied into the ADR.

Accepted decisions preserve history. Supersede or amend them according to the project's convention instead of rewriting the historical core. Decision acceptance, implementation completion, and verification are different states.

## Context and glossary documents

Establish the artifact's existing role before changing it. A `CONTEXT.md` may be a domain glossary, a broad project-current-truth map, or something else. Do not assume it is a dictionary and do not rename it to `GLOSSARY.md` merely because another source uses that name.

For a glossary role, keep canonical domain terms, concise meanings, important excluded meanings, and context boundaries. For a broad project-context role, keep concise current purpose, concepts, module responsibilities, major flows, integrations, architecture boundaries, and genuinely established conventions. Link detailed designs and ADRs rather than duplicating them.

## Writing quality

Use the project's exact terminology, symbols, paths, and contract names. Prefer direct concrete prose over generic engineering language. Status controls tense: planned behavior must not read as implemented fact, and implemented behavior must not be written as a future intention.

Verify material current-state claims against code, configuration, or the maintained authority available to the task. Mark unresolved evidence instead of inventing confidence. The finished artifact must make sense without the design conversation that produced it.
