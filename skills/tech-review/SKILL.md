---
name: tech-review
description: Review software architecture, design documents, or code changes for evidence-backed problems and actionable improvements. Use for architecture audits, design readiness, PR/branch/commit/worktree reviews, and complete re-reviews. Default to read-only; apply fixes only when the task authorizes them. Do not confuse ordinary proofreading or author self-checks with independent review.
---

# Engineering Review

Match the conclusion to the object actually reviewed. Communicate in the user's language. Use the repository's required output format where one exists; otherwise prioritize important findings over ceremony.

## Fix the target and choose the lens

Identify requested scope, current revision or content snapshot, governing requirements, and available validation. Infer a clear target from context instead of asking redundant questions. Resolve genuine comparison ambiguity before relying on a diff.

| Review target | Read |
|---|---|
| Existing responsibilities, dependencies, or architecture investment | [Architecture audit](references/architecture.md) |
| A design, proposal, specification, or implementation plan | [Design review](references/design.md) |
| A PR, branch, commit, exact snapshots, or uncommitted code | [Code review](references/code.md) |
| Independent review, separate review axes, or several reviewers | [Independence and synthesis](references/independence.md) |

Mixed work can combine lenses without running three unrelated full audits. A request for a complete re-review requires rereading the current full target and relevant governing material, closing prior findings, and looking for new contradictions—not merely inspecting the repair diff.

## Establish a finding

Trace enough surrounding code, calls, states, or document sections to test the suspicion. Look for evidence against it. Existing review comments and author explanations are hypotheses, not established defects or proof of correctness.

A reportable issue needs a precise location, a concrete trigger or scenario, supporting evidence or violated requirement, impact, and a useful correction direction. Distinguish defects, required-standard deviations, unresolved questions, and optional improvements. A code smell, aesthetic preference, or hypothetical possibility alone is not a blocking finding.

Check relevant code, current design, accepted ADRs, and declared context/glossary roles for material inconsistencies and unsupported completion claims. Distinguish a historical superseded decision from stale current guidance; do not demand all documents repeat the same facts. Report missing synchronization when it would mislead implementation or operation. Review remains read-only unless correction is authorized, including for apparently obvious documentation fixes.

Check whether design changes invalidate the scope of earlier review or validation claims and whether progress summaries agree with the maintained plan. Report affected stale conclusions without treating a still-valid accepted decision as rejected. A favorable review is a readiness assessment, not stakeholder acceptance or runtime verification.

Order findings by actual consequence and conditions. Remove duplicates and unsupported allegations. Report no findings when none meet the bar; do not invent issues to make a review appear useful.

## Preserve scope and evidence

The subject is read-only unless fixes are part of the request. Existing authorization to correct issues remains valid: verify each issue, make the bounded correction, and check the result rather than asking for the same authorization again. Do not overwrite unrelated work or silently reconcile conflicting standards by editing them.

Author self-checks are valuable but not independent. Claim isolation only when the context actually excluded author reasoning and expected answers. If unavailable, perform ordinary review and state that limit.

Deliver actionable findings, reviewed scope, actual validation, and the appropriate readiness judgment. Passing tests do not replace review; static review does not establish runtime acceptance. A later change can invalidate a prior conclusion.
