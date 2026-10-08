# Technical Design Documents

Use the project's existing design, proposal, RFC, or specification format when one exists. Do not replace a working local convention with this reference merely to make documents look uniform.

## Distinguish the document's job

A proposal or RFC helps decide between consequential options. A technical design explains the chosen or currently proposed system behavior in enough detail that implementation and review can proceed. A feature specification may emphasize user scenarios and acceptance rather than internal architecture.

Do not mix these jobs accidentally. When a decision is still genuinely open, expose the criteria, options, and unresolved outcome. When the decision has been made, lead with the chosen design instead of preserving the whole discussion as if every alternative were still live.

Implementation sequencing and work breakdown belong in the maintained work plan when one exists. A design can identify migration phases, prerequisites, and verification needs without becoming a ticket list.

## Default shape when the repository has no template

Keep a small stable core and add conditional sections only when they carry decisions:

1. **Context / problem / current state** — what exists, what is inadequate, and the constraints that shape the design.
2. **Goals and non-goals / scope** — what the design must accomplish and adjacent work it deliberately does not solve.
3. **Chosen approach and key decisions** — the mechanism, responsibilities, contracts, and decisive trade-offs.
4. **Failure and verification semantics** — important failure behavior, recovery expectations, and what evidence will distinguish a correct implementation.
5. **Risks, blockers, and open questions** — only items that remain material to implementation, rollout, or acceptance.

Add sections such as these when the design actually needs them:

- architecture or data flow;
- domain/data model and ownership;
- APIs, events, schemas, compatibility, or versioning;
- runtime state, concurrency, retries, idempotency, or recovery;
- security or privacy;
- performance or scale constraints;
- observability and operational diagnostics;
- migration, rollout, backward compatibility, and rollback;
- alternatives whose rejection is important enough that a future reader would otherwise reopen them.

A small, self-contained mechanism does not need a system-design table of contents. A distributed migration may need most of these sections. Depth follows risk and the number of decisions, not a fixed page count.

## Keep the design implementable without prewriting the implementation

Name complete caller or user-visible contracts, ownership, states, invariants, failures, and compatibility rules. Use diagrams, signatures, payloads, schemas, or pseudocode where prose would leave an important ambiguity. Keep examples minimal and consistent with the terminology in the surrounding text.

Do not fill the document with production classes, complete tests, or file-by-file tasks that will immediately drift. A testing or verification section states what must be proven and the appropriate boundary; the detailed scenario matrix or execution plan lives with its maintained owner when the project has one.

## Write current design, not meeting history

A design document describes the system or proposed system as it stands. Do not narrate every abandoned draft. Preserve a rejected alternative only when its rationale is likely to matter again.

Use status and tense consistently. Planned behavior must not read as verified current behavior. Implemented behavior must not be described as a future intention. Keep unresolved items visibly unresolved instead of writing plausible filler.

When a design changes materially, update affected contracts, diagrams, acceptance, migration, and links together. Do not silently rewrite an accepted ADR to make its historical rationale match the new design; supersede or amend the decision record according to the project's ADR convention.
