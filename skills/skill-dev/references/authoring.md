# Authoring and Integrating Methods

Use when deciding what belongs in a Skill or synthesizing upstream approaches.

## Start with a behavioral contract

Describe the requests to handle, necessary inputs, important decisions, output, and observable completion. Keep adjacent non-target tasks explicit where confusion is likely. A list of impressive capabilities is not an instruction set.

For source-based work, inspect the relevant original material and license, including references carrying required behavior. Record the retained, adapted, or rejected methods and why, using the existing provenance mechanism where one exists. Preserve important prerequisites, persistence steps, and authority assumptions; distinguish exact revisions and material read from material merely fetched.

## Integrate by semantic change, not by append

Compare an upstream method with the current local behavior before editing. A demonstrated defect is not required: a clearer explanation, worked example, decision aid, or reusable technique may improve an already-covered task. Identify the choice or action it makes easier and preserve any necessary assumptions and limits. Choose the smallest accurate action:

- **ADD** — introduce a genuinely new concept or user-visible behavior;
- **REPLACE** — use the stronger method and remove the weaker or obsolete expression it supersedes;
- **MERGE** — combine overlapping local rules into one clearer owner;
- **MOVE** — keep the method but relocate its full explanation to the surface that owns it, leaving only task-specific projection elsewhere;
- **DROP** — remove a redundant, obsolete, unsupported, or no-longer-useful rule.

Resolve conflicting upstream rules rather than pasting both. Prefer one complete owner for a method and concise task-specific projections in neighboring references. Do not measure a successful upstream sync by added lines; a stronger revision can be smaller than what it replaces.

## Place detail by when it is needed

Keep decisions every invocation needs in `SKILL.md`. Put substantial mode-specific procedures, examples, schemas, and failure checks in local references. Each pointer should say what the material contains and the condition that requires reading it. A crucial method behind “more information” may never be loaded.

Keep related definitions, constraints, and caveats together. Remove duplicated prose inside one bundle, but do not create cross-Skill runtime dependencies merely to deduplicate a few sentences between independently installable entries.

Do not use a word count as a quality target. Remove a rule because it is irrelevant, redundant, wrong, superseded, or shown not to help—not merely because it makes the entry longer.

## Write executable guidance

Give the executor a recognizable condition, a useful action or choice, and an observable result. At consequential judgments, explain how the action serves the task and which assumptions make it appropriate. This lets the executor apply the method when names or surface details change. Keep explicit constraints where they protect a real contract; explaining a constraint does not make it optional.

Use a worked example when a rule leaves a plausible choice unclear. Show the relevant starting situation, the decision and its reason, then the useful result. Include enough boundary or failure behavior to distinguish the method from an attractive but incorrect shortcut. For a refactoring rule, for example, show which repeated caller decisions move to one owner and which responsibilities stay with callers; a shorter function alone does not demonstrate the benefit.

Examples illustrate a reusable distinction, not a required output to imitate. Mark hypothetical examples and fragments as such, keep their assumptions next to them, and retain the details that carry the reasoning. A contrasting case is useful when it changes the choice. Use actual successful artifacts or traces when available, but separate observed success from a claim that the Skill caused it. Do not require every instruction to acquire an example or a new evaluation run.

Use fixed sequences for actual dependencies or fragile operations, not for open-ended judgment that admits several valid approaches. When shortening, check that the reader can still recover the condition, rationale, action, and evidence of completion. Remove repetition or move branch-specific depth before deleting an explanation that makes the method usable.

Distinguish names and descriptions from instructions: metadata influences selection before the body is read. Use lowercase hyphenated names of at most 64 characters with matching directory names. Keep descriptions discriminating. Normal discovery remains enabled unless explicitly changed by the user.

Do not cache facts that the environment can cheaply answer and that are likely to become stale. Read project commands, package roots, and conventions where needed. When a rule relies on a tool, name the capability and a workable fallback unless that concrete tool is essential to the specialized task.

## Package and preserve provenance

Check all references from an isolated copy of one Skill. Include applicable notices when distributing adapted source text or resources. Record exact source revisions and file hashes; a download is not evidence that the file was read.

Keep code, documentation, source study, and evaluation results distinguishable. Do not ship upstream study directories into discovery paths or create extra `SKILL.md` entrypoints for every reference.

Before installation, check the actual target's effective Skill registries, plugin names, commands, and lookup rules. A prefix may reduce risk but does not prove uniqueness; a bare name may be requested but does not permit overwriting an existing entry. Generation can finish independently of that installation decision.
