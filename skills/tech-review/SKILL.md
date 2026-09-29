---
name: tech-review
description: Review software architecture, design documents, code changes, or user-facing frontend work for evidence-backed problems and actionable improvements. Use for architecture audits, design readiness, PR/branch/commit/worktree reviews, frontend quality review, and complete re-reviews. Default to read-only.
---

# Engineering Review

Match the review lens to the object actually under review. Keep the entrypoint small: review method and evidence standards live here; domain-specific checks live in references.

## Fix the target and choose the lens

Identify scope, revision or snapshot, governing requirements, and available validation. Infer an obvious target from context instead of asking redundant questions.

| Review target | Read |
|---|---|
| Existing responsibilities, dependencies, or architecture investment | [Architecture audit](references/architecture.md) |
| A design, proposal, specification, or implementation plan | [Design review](references/design.md) |
| A PR, branch, commit, exact snapshots, or uncommitted code | [Code review](references/code.md) |
| User-facing frontend behavior, interaction, responsive behavior, or UI quality | [Frontend review](references/frontend.md) |
| Independent review, separate review axes, or several reviewers | [Independence and synthesis](references/independence.md) |

Mixed work may combine lenses without running several unrelated full audits. A frontend PR can use the code lens plus the frontend lens; a design document does not need code checks unless implementation is actually part of the target.

## Establish a finding

Trace enough surrounding code, calls, UI states, or document sections to test the suspicion. Look for evidence against it.

A reportable issue needs a precise location, concrete trigger or scenario, supporting evidence or violated requirement, impact, and a useful correction direction. Distinguish defects, required-standard deviations, unresolved questions, and optional improvements.

Do not turn personal taste into a defect. For frontend work, compare against the project's accepted design, component system, product conventions, interaction states, accessibility/responsive requirements, and actual rendered behavior when evidence is available.

Remove duplicates and unsupported allegations. Report no findings when none meet the bar.

## Preserve scope and evidence

The subject is read-only unless fixes are part of the request. Passing tests do not replace review; static review does not establish runtime acceptance; a visually polished page does not prove the critical flow works.

A complete re-review rereads the current full target and relevant governing material rather than checking only the repair diff.

Deliver actionable findings, reviewed scope, actual validation, and the appropriate readiness conclusion. Do not claim independent review when the context was not independent.
