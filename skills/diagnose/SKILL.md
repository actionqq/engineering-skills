---
name: diagnose
description: Investigate software failures, intermittent bugs, failing tests, and performance regressions, then fix them when requested. Use when the cause is uncertain, the initial explanation conflicts with evidence, or repeated patches have not resolved the symptom. Do not replace a defined feature task with open-ended diagnosis.
---

# Evidence-Based Debugging

Explain the causal path from trigger to symptom and verify the requested fix. Communicate in the user's language. A visible, low-risk defect can take a short path; an uncertain defect needs discriminating evidence, not a fixed number of phases.

## Establish the failure

Identify expected behavior, exact symptom, triggering input, affected revision, and environment. Distinguish the user's failure from another error encountered during investigation. Read [Reproduction and observability](references/reproduction.md) when a useful feedback loop is missing, flaky, slow, or performance-related.

Code reading may help build the reproduction. Prefer a failing test, minimal invocation, replay, controlled schedule, or observation that can separate explanations. Preserve the original scenario while minimizing it. Record the baseline rather than relying on remembered behavior.

## Test a causal explanation

Read [Tracing and hypothesis tests](references/tracing.md) for failures spanning call chains, components, environments, or test order.

For each plausible explanation, state the supporting observation and a prediction that could distinguish it from competitors. Choose the smallest informative probe. Change one causal variable at a time where possible; avoid stacking patches whose effects cannot be separated.

Seek a working comparison and inspect meaningful differences. Update the hypothesis when evidence contradicts it. Repeated attempts without new information are a reason to revisit observations and assumptions, not proof that the whole architecture is wrong.

Without reproduction, continue useful source and artifact investigation but label causal claims by their actual support. Specify the next missing observation. Emergency mitigation may be appropriate within authorization; record it separately from a demonstrated root-cause fix.

## Fix and verify

For diagnosis-only work, provide evidence and the repair direction without editing the subject. For authorized fixes, change the responsible behavior and add a proportionate regression check at a boundary that reproduces the real failure.

Compare the expected behavior with relevant design, accepted decisions, and the project's declared context documents. During an authorized fix, update documentation only where behavior or a newly established constraint makes it inaccurate; a routine bug fix need not create an ADR. Preserve accepted decision history, append supported outcomes where useful, and surface material conflicts instead of silently changing the governing choice. Diagnosis-only and explicit file limits also apply to documentation.

Rerun the original scenario and affected checks. A single quiet run does not establish that an intermittent failure is gone. Separate baseline failures and blocked checks from the fix result. Remove temporary probes added by this task and preserve useful, appropriately redacted reproduction evidence.

Deliver the cause-to-symptom explanation, experiments and actual observations, change or mitigation, verification, and unresolved uncertainty. Do not claim success solely because a plausible patch was written.
