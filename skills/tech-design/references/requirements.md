# Requirements and Decision Dependencies

Use this when different interpretations would change behavior, scope, or acceptance. An already-clear edit can reuse the existing agreement.

## Establish the intended change

Name the user or caller, the problem, the desired outcome, and what remains outside the change. Read the existing behavior before specifying its replacement. Keep three things distinct: what the software currently does, what the project already promises, and what this change proposes.

For an existing system, describe added, changed, removed, and deliberately unchanged behavior. A delta is useful for implementation review, but it does not remove the need to check the resulting whole for consistency. Do not create a second “source of truth” when the requested design already serves that role.

## Resolve the right questions

Represent material decisions with their prerequisites. Ask about a dependent choice only after enough prerequisites are known to make the answer meaningful. Investigate discoverable facts yourself. A question about an existing API's behavior usually requires reading or testing it, not interviewing the user.

Distinguish:

- **Fact:** verify through code, documentation, data, or experiment.
- **Business choice:** identify the alternatives and their consequences; ask if necessary.
- **Implementation detail:** decide within the authorized scope when reversible and adequately constrained.
- **Assumption:** state its consequence and the observation that would invalidate it.

Do not exhaust every conceivable branch. Stop clarifying when important work is unambiguous, its acceptance can be described, and remaining questions have bounded effects. A user request to decide autonomously is meaningful; avoid inventing approval gates for ordinary choices.

## Specify observable behavior

For representative scenarios describe initial conditions, action, outcome, and important side effects. Cover relevant rejection and recovery paths rather than padding a long story list. In stateful work, ask who may perform an operation, which states allow it, which outcomes are terminal, and what happens after a retry or partial success.

Example: “support retry” is incomplete for a payment request. Determine whether repeating the same business operation may charge again, how a committed result is retrieved after response loss, and whether a different payload with the same request identity is rejected. The observable behavior comes before choosing a retry library.

Turn vague qualities into evidence: what would demonstrate adequate latency, usability, reliability, or scale? Use agreed targets or identify a target as unresolved; do not invent numeric limits to make a template look finished.

## Keep acceptance connected

Each important requirement needs a distinguishing example or measurable condition. Use stable requirement IDs when several tasks or sessions need traceability; simple edits do not need artificial numbering. Avoid making acceptance depend on a private class structure unless that structure is itself a project requirement.

Include known constraints, meaningful non-goals, and unresolved decisions with their impact. Reuse exact interface snippets or experimental state models when they state a decision more precisely than prose; label their role and do not paste a whole demo.

Completion means relevant work can be implemented and evaluated without inventing material behavior. It does not mean every field in a generic template has been filled.

Use the [default document lifecycle](domain.md#default-document-lifecycle) for maintained designs. An existing template that equates review, acceptance, implementation, and verification must be clarified within the authorized scope rather than copied uncritically. A review that finds no blocking issues does not itself constitute stakeholder acceptance. Record acceptance or rejection when supported by actual decision authority, and link a replacement when the design is superseded. Use concise metadata or an equivalent visible status block; do not create documents solely to populate fields.

Keep implementation progress and verification results separately identifiable, preferably by linking the maintained plan and evidence. When requirements, constraints, or acceptance criteria materially change, identify which previous review or test conclusions no longer cover the design. Preserve their dates and scope as historical evidence; mark affected conclusions as needing renewed assessment without invalidating unrelated checks or reversing a still-valid decision.
