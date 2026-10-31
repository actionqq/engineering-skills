# Upstream Integration

Use for an explicit upstream synchronization request or when a material gap suggests an external method may help. This is a capability review, not a popularity contest or a requirement to browse on every small Skill edit.

## Discover beyond the current shortlist

1. Start from the user's actual workflows and the full current Skill inventory.
2. Search for maintained upstream repositories and relevant individual Skills across different ecosystems, not only the sources already cited by this bundle.
3. Inspect repository trees to discover supporting files and package structure. A `SKILL.md` may depend on references, scripts, templates, agents, assets, evals, plugin tools, or a host-specific workflow.
4. Prioritize sources by relevance, maintenance, demonstrated use, provenance, and whether their capability is generalizable. Stars are discovery signals only.
5. Record the exact revision or observation date. A moving `main` URL is not a reproducible source pin.

## Inspect the whole capability package

For each promising candidate, inspect:
- entrypoint metadata and trigger boundary;
- all behavior-bearing references actually used by the workflow;
- scripts, commands, templates, agents, assets, and runtime dependencies;
- inputs, outputs, state persistence, interruption recovery, and failure behavior;
- evaluation cases, graders, test harnesses, and the evidence behind claimed effectiveness;
- license and required notices for any copied text, code, or assets.

A repository tree or README is discovery evidence, not a full review. Mark what was fully read, sampled, fetched-only, or not inspected. Never claim a whole repository was assessed when only a subset was read.

## Compare capability, not names

Map upstream behavior to user tasks and local responsibilities. Similar names do not prove equivalent behavior; a local Skill's existence is not a reason to reject a better upstream method. Conversely, importing a second entrypoint for an already-owned task may create routing ambiguity without adding capability.

For every candidate, choose one explicit disposition:
- **Adopt:** use the upstream package substantially as-is, with provenance and compatibility checks.
- **Adapt:** incorporate selected methods into an existing entry or reference.
- **Replace:** retire a weaker local method in favor of a better-supported upstream capability.
- **Merge/refactor:** combine overlapping capabilities and update routing, references, and migration records.
- **Create:** add a new entry only when the task has a distinct trigger, inputs, output, and independent user value.
- **Defer/reject:** explain missing evidence, narrow relevance, runtime/license constraints, or harmful workflow assumptions.

Compare the complete behavior: trigger precision, task coverage, decision quality, output usefulness, method depth, resource loading, state recovery, validation, and host portability. Do not reduce the decision to whether the upstream skill title resembles a local one.

## Synthesize without importing accidental policy

Separate the reusable engineering method from the upstream author's workflow preferences. Check fixed stages, agent counts, mandatory trackers, retry thresholds, automatic commits, destructive cleanup, tool assumptions, and user-approval gates against the user's operating model. Retain useful methods while adapting or rejecting unsupported absolutes.

Do not copy source text or executable assets until their exact license and required notices are checked. Prefer an original synthesis when only the underlying idea is needed. Keep third-party notices with any distributed adapted material.

## Record and implement

Use the existing provenance files rather than creating a parallel ledger:
- source lock: repository, exact commit, paths, hashes, and review scope;
- source audit: what was inspected, findings, and limitations;
- method map: upstream method, local disposition, rationale, and destination;
- affected Skill notices: license and attribution where required.

Then inspect local entrypoints and references, implement only justified changes, remove superseded guidance, and update manifest, README, eval definitions, and prior validation claims consistently. Run structural checks and affected tooling tests. Model behavior evaluation is separate: run it only with a meaningful question, available harness, and authorization. Report untested behavior honestly.
