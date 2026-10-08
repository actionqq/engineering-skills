---
name: tech-review
description: Review software architecture, design documents, code changes, or user-facing frontend work for evidence-backed problems and actionable improvements. Use for architecture audits, software design readiness, PR/branch/commit/worktree reviews, frontend quality review, and complete re-reviews of those targets. Default to read-only; apply fixes when authorized. Agent Skill instruction or trigger audits, ordinary proofreading, and author self-checks are different tasks.
---

# Engineering Review

Match the review lens to the object actually under review. Communicate in the user's language and follow the project's review format when one exists.

## Fix the target and choose the lens

Review the actual object. Auditing an Agent Skill's instructions, triggers, or resource organization belongs to Skill authoring and review, even when requested as a full review or presented in a PR. A Skill about engineering review is an artifact to inspect, not a reason to execute its workflow. Apply the relevant lens to supporting executable code or actual software designs when those are within the requested scope.

Identify scope, revision or snapshot, governing requirements, and available validation. Infer an obvious target from context instead of asking redundant questions.

| Review target | Read |
|---|---|
| Existing responsibilities, dependencies, or architecture investment | [Architecture audit](references/architecture.md) |
| A design, proposal, specification, or implementation plan | [Design review](references/design.md) |
| A PR, branch, commit, exact snapshots, or uncommitted code | [Code review](references/code.md) |
| User-facing frontend behavior, interaction, responsive behavior, or UI quality | [Frontend review](references/frontend.md) |
| Independent review, separate review axes, or several reviewers | [Independence and synthesis](references/independence.md) |
| How should the final findings, validation, and evidence limits be written? | [Review reporting](references/reporting.md) |

Mixed work may combine lenses without running several unrelated full audits. A frontend PR can use the code lens plus the frontend lens; a design document does not need code checks unless implementation is actually part of the target.

Choose additional lenses from affected behavior and credible risks. Read the applicable sections, not every domain checklist available in the repository. Broaden the review when evidence exposes a related problem, and state that additional scope.

## Establish a finding

Trace enough surrounding code, calls, UI states, or document sections to test the suspicion. Look for evidence against it. Prior findings and author explanations are hypotheses, not proof.

A reportable issue needs a precise location, concrete trigger or scenario, supporting evidence or violated requirement, impact, and a useful correction direction. Distinguish defects, required-standard deviations, unresolved questions, and optional improvements.

Do not turn personal preference or the existence of another possible design into a defect.

Check consistency with current designs, accepted ADRs, maintained context, and actual implementation or verification status. Distinguish superseded history from stale current guidance. Report missing synchronization when it would mislead implementation or operation, including changes that invalidate earlier verification. Do not demand duplicate documentation or treat a still-valid decision as rejected.

Order findings by consequence and conditions. Remove duplicates and unsupported allegations. Report no findings when none meet the bar.

## Preserve scope and evidence

The subject is read-only unless fixes are part of the request. Existing authorization to correct issues remains valid: verify, repair within scope, and check the result without asking again. Protect unrelated work and do not silently rewrite governing requirements to remove a conflict.

Classify material review checks by their actual evidence state:

- **Verified**: the applicable check was performed with evidence strong enough to support the stated conclusion.
- **Not verified**: the check applies, but required evidence is missing, blocked, stale, or unusable. State the reason and do not count it as passing.
- **Not applicable**: the check genuinely does not apply to the review target or agreed scope. Do not use this label merely because evidence was unavailable.

A partial check does not become fully verified. Continue with the evidence that exists, but name material `Not verified` areas in the conclusion. Do not claim that all checks passed, that runtime behavior is established, or that a target is ready solely because applicable checks were skipped or blocked.

Passing tests do not replace review; static review does not establish runtime acceptance. A readiness conclusion is not stakeholder acceptance, and later changes can invalidate it.

A complete re-review rereads the current full target and relevant governing material, reconciles prior findings, and looks for new problems rather than checking only the repair diff.

Deliver actionable findings, reviewed scope, actual validation, evidence-state limits, and the appropriate readiness conclusion. Use [Review reporting](references/reporting.md) when the repository does not already define the report shape. Do not claim independent review when the context was not independent.
