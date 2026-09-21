# Disposition and Authority

Use when assessing accumulated documents or preparing an archive batch.

## Build enough context to decide

Identify document roles, ownership, explicit status and replacement links, current plans, and the entrypoints that readers actually use. Establish which branch, release, system, or environment a claim describes. Use code, change history, and recorded checks where they help distinguish implementation from intent; implementation alone does not approve a decision. Do not rerun application tests just to file historical evidence.

Find incoming and outgoing references, including indexes, project instructions, code comments, scripts, attachments, and embedded paths. Distinguish a historical citation from a dependency on current guidance. A citation to an old experiment can remain useful; a runbook whose only prerequisite lives in a supposedly retired document needs attention.

Age, naming, size, similar titles, and inactivity are candidate signals. They are not retirement evidence. Compare scope and contents before calling two documents duplicates. Prefer explicit authorized decisions and replacement relationships, matched scope, and declared topic ownership over timestamps. If they conflict, describe the conflict and retain uncertain material rather than selecting the newest file.

## Separate the meanings

| Question | Examples | Consequence |
|---|---|---|
| What happened to the work? | Implemented, cancelled, deferred, blocked | Preserve its actual outcome and unresolved obligations |
| What is the document's role now? | Current contract, active plan, useful reference, historical account | Decide whether readers still need it in active navigation |
| How is it organized? | Active location, historical location, historical index, snapshot | Choose placement independently of approval or test results |

Preserve meaningful project labels; do not replace decision or verification status with a single `archived` field. A completed design effort may leave an active implementation specification and historical discussion notes. An accepted ADR may remain authoritative after delivery. A rejected option may be valuable historical evidence. Reference material can be old and still useful without being a current specification.

## Choose the disposition

| Disposition | Use when | Required result |
|---|---|---|
| Retain | Current guidance, ongoing work, or useful active reference | Keep a clear current entrypoint; no fabricated rewrite |
| Carry forward, then archive | A retiring document uniquely holds established current information or a live obligation | Identify its maintained destination and confirm the material survived before retirement |
| Move | The document or coherent group is historical and affected paths can be reconciled | Preserve contents, references, and a discoverable archive entry |
| Archive in place | Stable IDs, extensive external links, or project conventions make movement costly | Mark its historical role and adjust active navigation while keeping the path |
| Snapshot | A rolling document must continue while a stage needs a fixed record | Label the snapshot's scope/revision and keep one current owner |
| Defer | Authority, ownership, successor coverage, or a dependency is unresolved | Name the missing evidence; do not hide the item as completed |

Carry-forward work is limited to established information and authorized document maintenance. If synthesis requires choosing between conflicting designs, changing an accepted contract, or editing an excluded owner, retain the affected source and explain the decision needed. A new canonical specification is not a compulsory archive prerequisite.

For partially superseded documents, identify the surviving sections. Retain the document with precise replacement pointers, or extract established current material to its appropriate owner when authorized. Retire the entire original only after verifying coverage of those surviving claims. Keep decision rationale and rejected alternatives as history instead of rewriting them to match today's outcome.

Open work must not disappear inside a historical bundle. Keep its live plan, or transfer the obligation to a real active record with a link and its actual status. Do not invent an owner, deadline, acceptance, or resolution. Deferral and inactivity alone are not terminal outcomes.

## Define a bounded batch

Group by meaningful relationships: a change, feature, investigation, release, or obsolete document set. Use a milestone only when the project actually has one. Exclude still-active shared documents and preserve links to them rather than copying them into each archive.

Produce a compact table in the response or existing work record: source; current role and evidence; disposition and reason; successor or live obligation destination; archive target; reference repairs or blockers. Keep uncertain candidates separate. A user who requested assessment should be able to review concrete effects without receiving a directory of empty plans. For authorized execution, use the table as the execution record and proceed within settled scope.
