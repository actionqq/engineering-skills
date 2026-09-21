# Design and Plan Review

Use for readiness and consistency of a proposed or revised design. Judge the proposal at its level: it needs sufficiently defined behavior and feasible decisions, not every implementation detail.

## Read the current whole

Read the requested current document, relevant goals and acceptance, governing decisions, and enough actual implementation to test feasibility. Search helps locate material; selected search hits do not establish that a complete document was reviewed.

For a change review, inspect the proposed delta and its surrounding obligations. For a complete re-review, read the current whole, then reconcile previous findings and look for new problems. An old checklist is not the complete scope.

## Check the decision and behavior

Evaluate alignment with the actual goal, completeness of important scenarios, clarity of acceptance, internal consistency, technical feasibility, and compatibility with existing requirements. Identify scope growth rather than inventing missing sections from a universal template.

Follow important behavior through preconditions, action, state change, side effects, success, and failure. Depending on the task, check:

- identity, version, ownership, and lifetime of referenced objects;
- transitions, terminal states, cancellation, retry, duplication, ordering, and concurrency;
- partial success, recovery, compensation, and observable user outcomes;
- authorization, trust, and data ownership across boundaries;
- old/new readers and writers, retained data, migration, and rollback versus forward recovery;
- whether acceptance can distinguish intended behavior from the likely wrong implementation.

Do not require a distributed-systems mechanism for a local function that does not need one. Conversely, “handle errors” is not sufficient when partial success determines whether the design can work.

## Classify issues accurately

Assess the status model itself, not only compliance with the existing template. A design or ADR needs a distinguishable decision state; delivery progress and per-criterion verification need their own evidence or links. A legacy `done` field that conflates these can mislead a concrete release or implementation decision and warrants correction. Equivalent labels with clear meanings are not defects. Recommend a bounded clarification, preserving decision history and tooling compatibility; do not rewrite templates or subjects during a read-only review.

Distinguish a contradiction, an important missing decision, an unverified assumption, and an optional improvement. Verify facts available in code or existing documents before asking the author. Locate both sides of a conflict where possible.

A useful finding states the scenario that makes the flaw matter, why the design cannot currently satisfy it, and the smallest correction or evidence needed. Suggested rewrites should preserve intended scope. Do not edit a governing ADR simply to make the proposal appear consistent.

For PR inline feedback, obtain locations from the actual reviewed diff and correct side. If the location is outside that diff, place the issue in the overall report rather than inventing inline coordinates. Follow a requested output schema only when the integration actually needs it; creating a report does not authorize posting it externally.

## Conclude at the right level

State whether the current design can enter implementation, can do so after named conditions are resolved, or contains blockers. Close previous issues as resolved, still present, or superseded with current evidence. Do not equate design approval with implementation or runtime acceptance. An unresolved conflict with an effective requirement precludes an unconditional readiness conclusion.
