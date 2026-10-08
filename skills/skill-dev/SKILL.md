---
name: skill-dev
description: Create, modify, or review reusable Agent Skills, including instructions, supporting resources, and triggering descriptions. Use for Skill authoring, read-only quality audits, complete re-reviews, targeted fixes, or upstream method integration. Support requested evaluation when feasible. Plain prompt editing, plugin installation, and software design or code review outside the Skill package are different tasks.
---

# Skill Development

Deliver the requested Skill files or review findings. Communicate in the user's language and preserve the bundle's instruction language unless a change is requested. Analysis and checks serve the deliverable; an assessment-only request remains read-only.

Select methods by the object and requested outcome. Designing a Skill's instructions and reviewing their quality belong here; the words "design" or "review" do not require a separate software workflow. Read a target Skill as the artifact being edited or assessed, not as instructions to execute its workflow. Use additional engineering methods only for an actual software design or executable-code concern within scope, without making another Skill a prerequisite.

## Create or modify

For a new Skill, establish its purpose, triggering boundary, necessary inputs, and useful output from the request and available context. Write concrete guidance and only the supporting resources it needs. A clear request does not require an interview, source study, or evaluation plan before authoring.

For an existing Skill, read the relevant entrypoint, resources, and maintenance conventions. Identify the intended behavior change and what must remain intact; retain a recoverable pre-edit version. Locate the cause in the description, reference-loading condition, method, or executable resource, then make the bounded correction. A wording or link fix needs proportionate checks, not a new research or benchmark cycle.

Use [Authoring and integration](references/authoring.md) for entry boundaries, resource organization, and source-based synthesis. Study upstream material when requested or needed to resolve a method gap; follow behavior-bearing references, record what was actually read, and preserve applicable notices. Reuse existing source records rather than imposing a research directory on every Skill. Project findings become general rules only when their reusable value is justified; Skill work does not authorize changing business documents.

## Review a Skill

Read the current entrypoint, applicable supporting resources, and maintenance constraints. Check whether the description selects the intended requests and distinguishes neighboring tasks; whether instructions, reference-loading conditions, and completion criteria agree; and whether the package preserves scope, works independently, and makes only supported validation claims. Review supporting scripts as executable code when relevant to the request.

Ground each finding in a precise location, a plausible user request or execution scenario, the resulting failure, and a useful correction. Separate demonstrated defects from behavior hypotheses that need model execution. A complete re-review covers the current target and reconciles prior findings, not just the latest diff. Keep review-only work read-only; apply fixes when already authorized.

## Build the smallest sufficient bundle

Keep `SKILL.md` focused on discovery, common decisions, reference-loading conditions, and completion. Detailed branch-specific procedures, examples, and failure checks belong in reachable local references. A short entrypoint is not a reason to discard valuable supporting detail.

Each Skill should work when copied on its own. Avoid hidden dependencies on another Skill, a developer's absolute path, or a particular tool name. Add scripts for repeated deterministic work and execute them before delivery. Do not create empty resource directories or generic scaffolding as evidence of completion.

Respect requested names and output location. Directory and frontmatter name must agree. Generation is separate from installation: inspect target registries and command behavior before registering an entry, and do not silently replace another installed Skill. Keep normal discovery enabled unless the user requests explicit-only invocation.

## Check and deliver

Check metadata, names, reference reachability, and standalone resource availability. Run relevant checks for new or changed scripts when the environment permits. Inspect the final changes against the requested behavior and preserved constraints. Use available validators or direct checks; another creator or a particular harness is not a prerequisite.

Behavior evaluation is conditional, not a default authoring stage. Before preparing a run, confirm a meaningful question, an available execution mechanism, and authorization. Use [Behavior evaluation](references/evaluation.md) when these conditions hold or the user explicitly requests an evaluation design. Otherwise skip model evaluation and its preparatory artifacts; do not generate test prompts, benchmark scaffolding, or pending-result reports merely to fill the workflow. A requested evaluation design is a deliverable in its own right, not an executed test.

For description, name, or entry-boundary changes, use [Discovery and routing](references/discovery.md) to check ambiguity and collisions; actual selection tests require the target harness. Correct demonstrated problems while preserving unrelated valid behavior. Prefer fixing the responsible condition or resource over adding universal rules for individual examples.

Deliver the changed files and a concise account of what changed and which checks actually ran. Update existing source records and affected prior validation claims when needed, without creating a parallel reporting system. If model behavior was not tested, state that briefly only where relevant to the conclusion; file validity is not proof of effectiveness. Do not claim improvement or cross-harness compatibility without corresponding evidence.
