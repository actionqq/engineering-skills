# Evaluate Discovery and Routing

Use when descriptions, entry boundaries, or names change. Loading a Skill explicitly and obtaining a good result does not prove natural-language selection works.

For routine edits, inspect metadata, neighboring entry boundaries, and known naming constraints directly. Prepare runtime queries only when an actual target-harness selection test can and should run, or the user explicitly requests an evaluation design. Without that mechanism, finish the feasible authoring checks; do not create a dormant trigger suite or claim discovery was verified.

## Separate three questions

1. Does the harness discover the installed package and its metadata?
2. Does a natural request select the appropriate entry and mode?
3. Does the selected instruction produce the right behavior?

A file schema validator answers none of the runtime questions by itself. A name can be valid yet collide with a built-in entry or resolve differently under plugin and standalone installations.

## Build realistic queries

Use natural requests with enough context to make the intended task clear. Include the user's actual languages, informal wording, paths, partial context, and cases where a competing entry would be plausible.

Examples of useful distinctions include designing an architecture versus reviewing one; deciding a technology versus checking a single fact; arranging implementation versus implementing; designing tests versus auditing their quality; preserving context versus writing a general summary.

Near-misses should share meaningful vocabulary. An irrelevant joke is a weak negative case for an engineering Skill. A one-line fact that the harness handles directly may legitimately select no Skill; define acceptable outcomes rather than rewarding maximum invocation.

For combined requests, specify acceptable entry/mode combinations and required final scope. Do not demand a fixed internal invocation order when several paths can accomplish the task correctly.

## Run through the actual selection mechanism

Use the real available catalog and target harness rather than a keyword classifier that only approximates it. Keep expected labels out of the execution context. Measure errors against adjacent entries as well as non-invocation, and inspect why a request was misrouted.

Separate tuning and held-out queries. Select changes using development evidence, then report holdout results without repeatedly editing against that same holdout. Repeat important cases to understand variability rather than reporting a single lucky selection.

Change descriptions to clarify purpose, triggering conditions, and genuine exclusions. Do not respond to one missed invocation with a universal “always use this” that captures unrelated work. Avoid synonym lists that add context cost without distinguishing another mode.

Record actual registry/source resolution when testing installation collisions. Do not assume that a native command and a Skill with the same name override each other—or coexist safely—without verifying that harness's mechanism.

## Test occupied names and competing sources

Classify exact native-command collisions, aliases, bundled-Skill replacement, duplicate Skill identities, and merely similar names separately. Check the real invocation syntax: a shell subcommand, slash command, and explicit Skill mention may occupy different namespaces.

Inspect all effective discovery locations, including user, project, parent, plugin, and bundled sources. A different directory does not guarantee a distinct identity. Do not silently overwrite files or merge two same-named Skills. Use an unambiguous supported namespace or select the intended source deliberately.

Record the host version, interface, installation layout, invocation, resolved source path or identity, and content fingerprint. A plausible final answer does not prove which instructions loaded. Verify that the intended Skill loads and unrelated native behavior stays intact. Inspect dispatch or use a side-effect-free test environment when a competing command uploads diagnostics or transfers sessions; do not trigger those actions merely to test a name.

When renaming, update the directory, frontmatter, UI metadata, active references, and evaluation labels together. Check for stale installations; an old-name alias can reintroduce the collision. Keep historical source names and execution records unchanged, and separate prepared cases from actual installation tests.
