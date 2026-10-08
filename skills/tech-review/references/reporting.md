# Review Reporting

Use this after the review has established its findings and evidence. Reporting must preserve the review's actual scope and uncertainty instead of turning a partial check into a cleaner-looking verdict.

## Follow the target and repository format

Use an existing project review format when it exists. Keep distinct axes separate when they answer different questions, such as specification conformance, project standards, correctness, frontend behavior, or architecture quality. Do not force every review into the same headings or combine semantically different results into one score.

A material report should identify the reviewed target and snapshot, the governing requirements or standards used, validation actually performed, findings, evidence-state limits, and the appropriate conclusion.

## Findings carry evidence, not ceremony

Each reportable finding needs:

- a precise current location or target;
- the trigger or scenario that makes it reachable or relevant;
- supporting evidence or the violated requirement;
- the concrete impact;
- a useful correction direction.

These are information requirements rather than mandatory labels. Prefer one compact paragraph when separate “Problem / Impact / Recommendation” headings add no information.

Order findings by consequence and conditions. Group duplicate symptoms of one cause. Keep confirmed defects, required-standard deviations, unresolved questions, and optional improvements distinguishable when mixing them would overstate or understate severity.

## Preserve verification state

For material checks, use the evidence meanings from the review workflow:

- **Verified** — performed with evidence sufficient for the stated conclusion.
- **Not verified** — applicable, but evidence was missing, blocked, stale, partial, or unusable.
- **Not applicable** — genuinely outside the target or agreed scope.

Do not convert `Not verified` into pass because no defect was observed. A report with skipped or blocked applicable checks cannot claim that all checks passed or that runtime behavior is established.

## Clean reports still need scope

When no finding meets the reporting bar, say so directly and retain the reviewed scope, validation performed, and material limits. “No findings in the checks performed” is appropriate when some applicable areas remain unverified.

For independent or multi-review work, synthesize validated findings rather than votes. Report the actual independence level and snapshot. A majority does not prove a finding, and a minority finding with stronger evidence can be the important one.

Use concrete project language. Replace vague phrases such as “could cause issues” with the actual state, caller, condition, violated contract, or user-visible consequence. The author should be able to act without reconstructing the reviewer conversation.
