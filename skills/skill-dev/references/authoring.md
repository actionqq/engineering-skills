# Authoring and Integrating Methods

Use when deciding what belongs in a Skill or synthesizing upstream approaches.

## Start with a behavioral contract

Describe the requests to handle, necessary inputs, important decisions, output, and observable completion. Keep adjacent non-target tasks explicit where confusion is likely. A list of impressive capabilities is not an instruction set.

For source-based work, inspect the relevant original material and license, including references carrying required behavior. Record the retained, adapted, or rejected methods and why, using the existing provenance mechanism where one exists. Preserve important prerequisites, persistence steps, and authority assumptions; distinguish exact revisions and material read from material merely fetched.

## Integrate by semantic change, not by append

Compare an upstream method with the current local behavior before editing. Choose the smallest accurate action:

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

Prefer concrete decisions, observable outcomes, and meaningful examples over generic exhortations. Explain why unusual rules matter. Use fixed sequences for actual dependencies or fragile operations, not for open-ended judgment that admits several valid approaches.

Distinguish names and descriptions from instructions: metadata influences selection before the body is read. Use lowercase hyphenated names of at most 64 characters with matching directory names. Keep descriptions discriminating. Normal discovery remains enabled unless explicitly changed by the user.

Do not cache facts that the environment can cheaply answer and that are likely to become stale. Read project commands, package roots, and conventions where needed. When a rule relies on a tool, name the capability and a workable fallback unless that concrete tool is essential to the specialized task.

## Package and preserve provenance

Check all references from an isolated copy of one Skill. Include applicable notices when distributing adapted source text or resources. Record exact source revisions and file hashes; a download is not evidence that the file was read.

Keep code, documentation, source study, and evaluation results distinguishable. Do not ship upstream study directories into discovery paths or create extra `SKILL.md` entrypoints for every reference.

Before installation, check the actual target's effective Skill registries, plugin names, commands, and lookup rules. A prefix may reduce risk but does not prove uniqueness; a bare name may be requested but does not permit overwriting an existing entry. Generation can finish independently of that installation decision.
