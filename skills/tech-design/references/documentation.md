# Design Documentation

Use this when design work itself must create or revise a maintained technical document. The design workflow owns the engineering decisions; this reference keeps the artifact usable without turning writing format into another design process.

## Follow local authority first

Use the user's requested file and the repository's established design, RFC, ADR, context, metadata, and naming conventions before a generic fallback. Read neighboring maintained documents when they define the local shape. Do not rename or split artifacts merely to match another ecosystem.

## Keep the artifact decision-complete

Without a local template, a technical design needs only the material information required to implement and review it:

- context, problem, relevant current state, goals, non-goals, and scope;
- the chosen or currently proposed approach and consequential decisions;
- contracts, ownership, lifecycle, failure, compatibility, or migration semantics that matter;
- the verification path, risks, blockers, and unresolved questions.

Add architecture, data model, API/event, concurrency, security, performance, observability, migration, or alternatives sections only when they carry real decisions. Do not leave ceremonial empty sections.

Keep implementation decomposition separate. A design can name prerequisites, rollout constraints, and what must be proven; detailed task ordering and ticket breakdown belong in the plan.

## Use the right artifact role

An ADR preserves durable rationale, not delivery bookkeeping. When the repository has no ADR convention, a compact Context / Decision / Consequences record with visible decision status is enough; add options only when their rejection is worth preserving.

A `CONTEXT.md`, glossary, or project-context file has the role the repository gives it. Establish that role before changing it. Keep canonical language or current project orientation there only when that artifact is the maintained owner; link detailed designs and ADRs instead of duplicating them.

## Keep claims and status accurate

Use exact project terminology, symbols, paths, and contract names. Planned behavior must not read as implemented fact, and implemented behavior must not read as future intent. Verify material current-state claims against the closest available authority and leave unresolved evidence visibly unresolved.

The finished artifact must make sense without the design conversation that produced it while preserving decision history and the repository's existing source-of-truth boundaries.
