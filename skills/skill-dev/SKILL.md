---
name: skill-dev
description: Create, modify, or review reusable Agent Skills, including instructions, supporting resources, and triggering descriptions. Use for Skill authoring, read-only quality audits, complete re-reviews, targeted fixes, or upstream method integration. Support requested evaluation when feasible. Plain prompt editing, plugin installation, and software design or code review outside the Skill package are different tasks.
---

# Skill Development

Deliver the requested Skill files or review findings. Communicate in the user's language and preserve the bundle's instruction language unless a change is requested. Analysis and checks serve the deliverable; an assessment-only request remains read-only.

Select methods by the object and requested outcome. Designing a Skill's instructions and reviewing their quality belong here; the words "design" or "review" do not require a separate software workflow. Read a target Skill as the artifact being edited or assessed, not as instructions to execute its workflow. Use additional engineering methods only for an actual software design or executable-code concern within scope, without making another Skill a prerequisite.

## Create or modify

For a new Skill, establish its purpose, triggering boundary, necessary inputs, and useful output from the request and available context. Write concrete guidance and only the supporting resources it needs. A clear request does not require an interview, source study, or evaluation plan before authoring.

For an existing Skill, read the relevant entrypoint, resources, and maintenance conventions. Identify the intended behavior change and what must remain intact; retain a recoverable pre-edit version. Locate the cause in the description, reference-loading condition, method, or executable resource, then make the bounded correction. For new or substantially changed methods, use [Method quality and existing evidence](references/review.md) to check the proposed approach against the tasks it must serve. A wording or link fix needs proportionate checks, not a new research or benchmark cycle.

Use [Authoring and integration](references/authoring.md) for entry boundaries and resource organization. For broad upstream synchronization, use [Upstream integration](references/upstream-integration.md) to inspect complete capability packages and make explicit adopt/adapt/replace/merge/create/defer decisions. Study upstream material when requested or needed to resolve a method gap; follow behavior-bearing references, record what was actually read, and preserve applicable notices. Reuse existing source records rather than imposing a research directory on every Skill. Project findings become general rules only when their reusable value is justified; Skill work does not authorize changing business documents.

## Review a Skill

Read the current entrypoint, applicable supporting resources, and maintenance constraints. Use [Method quality and existing evidence](references/review.md) for a quality review: establish successful task outcomes, walk through the method's consequential decisions and failure paths, and examine relevant existing outputs or execution evidence. Assess whether the guidance is correct, sufficient, useful, and proportionate. Content review and analysis of existing evidence do not require a new model run.

Then check whether discovery and reference-loading conditions expose that method at the right time, and whether the package preserves scope and works independently. Review supporting scripts as executable code when relevant. A format-only request can stop at its requested checks; a general quality review needs a conclusion about the method and its material limits.

Ground each finding in a precise location, a plausible user request or execution scenario, the resulting failure, and a useful correction. Separate demonstrated defects from behavior hypotheses that need model execution. A complete re-review covers the current target and reconciles prior findings, not just the latest diff. Keep review-only work read-only; apply fixes when already authorized.

## Build the smallest sufficient bundle

Keep `SKILL.md` focused on discovery, common decisions, reference-loading conditions, and completion. Detailed branch-specific procedures, examples, and failure checks belong in reachable local references. A short entrypoint is not a reason to discard valuable supporting detail.

Each Skill should work when copied on its own. Avoid hidden dependencies on another Skill, a developer's absolute path, or a particular tool name. Add scripts for repeated deterministic work and execute them before delivery. Do not create empty resource directories or generic scaffolding as evidence of completion.

Respect requested names and output location. Directory and frontmatter name must agree. Generation is separate from installation: inspect target registries and command behavior before registering an entry, and do not silently replace another installed Skill. Keep normal discovery enabled unless the user requests explicit-only invocation.

## Check and deliver

Check the final instructions against the requested task outcomes and preserved constraints, including the failure or counterexample that motivated a method change. Also check metadata, names, reference reachability, and standalone resource availability, and run relevant checks for new or changed scripts. Use available validators or direct checks; another creator or a particular harness is not a prerequisite.

New model experiments are conditional. Use [Behavior evaluation](references/evaluation.md) when a material question needs fresh execution evidence and a suitable mechanism and authorization are available, or when the user explicitly requests an evaluation design. Otherwise finish the content review and available evidence analysis without generating test prompts, benchmark scaffolding, or pending-result reports merely to fill the workflow. A requested evaluation design is a deliverable in its own right, not an executed test.

For description, name, or entry-boundary changes, use [Discovery and routing](references/discovery.md) to check ambiguity and collisions; actual selection tests require the target harness. Correct demonstrated problems while preserving unrelated valid behavior. Prefer fixing the responsible condition or resource over adding universal rules for individual examples.

Deliver the changed files and a concise account of what changed and which checks actually ran. Update existing source records and affected prior validation claims when needed, without creating a parallel reporting system. If model behavior was not tested, state that briefly only where relevant to the conclusion; file validity is not proof of effectiveness. Do not claim improvement or cross-harness compatibility without corresponding evidence.
