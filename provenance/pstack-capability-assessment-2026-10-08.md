# Cursor pstack capability assessment — 2026-10-08

This note compares the current Cursor `pstack` plugin with the entrypoints on `experiment/pstack-upstream-sync`. The goal is not to mirror pstack's command inventory. A capability is promoted only when it exposes a distinct user task or closes a concrete method gap in an existing task.

Upstream observation: `cursor/plugins@ccb5507cec1546dc88135c1139c811e6c59115ba`, primarily `pstack/README.md` and the specific Skill files named below.

## Selected syncs

### `technical-writing` → new `tech-writing` entry

Reason: the collection previously had no standalone owner for requests whose primary task is writing or restructuring technical documentation, while `tech-design` and `tech-review` still need their own local output-writing methods. The new entry owns doc-only work; it does not become a mandatory post-step for design or review.

See `provenance/technical-writing-method-family-2026-10-08.md` for the broader document-format research and source comparison.

### `blast-radius` → `tech-review` code-review method

Upstream value retained:

- a small diff can have effects that symbol/caller search does not reveal;
- safety often depends on one or a few concrete facts;
- a convincing explanation is weaker than proving the safety-critical fact with the strongest cheap evidence available.

Destination: `skills/tech-review/references/code.md`.

Adaptation:

- no requirement to create a separate blast-radius report;
- no mandatory arena or multi-model review;
- proof strength is proportional to the actual risk and authorization;
- an unproved safety fact is reported as an evidence limit, not converted automatically into a defect.

### `benchmark-checklist` → `research` performance-experiment method

Upstream value retained:

- confirm that timed work actually happened and produced correct output;
- count errors/retries/rejections that can make a path look faster;
- interleave A/B runs when drift, cache state, or warm-up can bias comparison;
- identify the limiting resource and sanity-check physical/algorithmic bounds before acting on a surprising number;
- do not declare a winner from an untuned or otherwise inconclusive comparison.

Destination: `skills/research/references/experiments.md`.

Adaptation:

- no universal minimum run count; repetitions follow variance and decision stakes;
- no fixed operating-system command set;
- a user-requested ballpark can remain lightweight when clearly labelled;
- performance method remains a conditional research/experiment branch rather than a top-level Skill.

## Existing coverage: no new entry

| pstack capability | Current owner | Decision |
|---|---|---|
| `how` | `research` plus ordinary code navigation | No new Skill. Understanding a subsystem is evidence gathering/explanation, not a new engineering lifecycle. |
| `why` | `research`, current designs/ADRs/context | No new Skill. Historical rationale is reconstructed from evidence and maintained decisions. |
| `recall` | `handover` | Existing handover/context recovery already owns resumable state. |
| `architect` | `tech-design` | Existing architecture, contracts, runtime, structure, and alternatives methods are broader. |
| `interrogate` | `tech-review` independence/synthesis | Existing method already separates review contexts when useful and synthesizes findings rather than votes. No fixed reviewer panel is added. |
| `tdd` | `implement` | Already covered by behavior-first testing, boundary selection, and regression evidence. |
| `unslop` | `tech-writing` style | Absorbed as direct, non-generic technical prose rather than a standalone cleanup command. |
| `teach` | `research` + `tech-writing` | Explanation is an output purpose, not a separate engineering authority. |
| `automate-me` | `skill-dev` | Creating a reusable mode/Skill is Skill authoring. No second authoring entry. |
| `create-verification-skill` / `maintain-verification-skill` | `skill-dev` + `implement` | Project-local verification Skills are authored as Skills and validated against the real app when authorized; no specialized top-level generator is required. |
| `no-comments` | `implement` / `tech-review` as applicable | Comment quality is a local code-quality concern. A universal comment-stripping workflow would be too opinionated. |
| TypeScript-specific best practices | language/project standards | No language-specific top-level Skill in this general collection. |
| `pr`-style PR writing | `tech-writing` | PR bodies are a technical writing artifact when requested; no separate PR-writing entry. |

## Harness/orchestration capabilities: deliberately not synchronized

`poteto-mode`, `arena`, `swarm`, `figure-it-out`, autonomous-run/playbook orchestration, model routing, and setup/model-selection commands belong to the host or orchestration layer. This collection is intentionally usable across several harnesses and does not impose Cursor Task-tool semantics, fixed model panels, worktree fleets, or a default mode that captures every non-trivial request.

The user can still orchestrate several harnesses externally. That is different from making the Skills themselves require that topology.

## Product-specific capabilities: not synchronized

`make-bot-ui` and similar pstack product/environment utilities solve a specific runtime or organizational setup. They do not represent general software-engineering task categories for this collection.

## Observe, do not promote yet

### `correct`

The useful principle is to move repeated mechanical mistakes toward architecture, types, deterministic lint/CI checks, or tests instead of accumulating prose rules. This is strong repository-governance advice, but the task currently spans existing design, implementation, review, and Skill/instruction work rather than forming a clean user-task entrypoint. Do not add a top-level Skill until repeated real use shows a stable trigger and deliverable that those owners cannot express cleanly.

### `reflect` / engineering retrospective

Session retrospectives can reveal navigation problems, missing checks, tool inefficiency, or stale steering instructions. They are useful, but adding a permanent entry now would create a process-optimization category without evidence that it is a common standalone task in this collection. Observe usage first. If adopted later, it should improve the environment from session evidence rather than become a mandatory end-of-task ceremony.

### decision trails / `show-me-your-work`

A durable audit trail is valuable only when the task actually requires one. Existing design, ADR, plan, review, and handover artifacts already record the decisions relevant to their lifecycles. Do not require a second universal log.

## Result

The pstack review does **not** justify cloning its Skill count. It produced one new user-task entry and two selective method additions:

1. `tech-writing` — new standalone entry for document-authoring tasks;
2. blast-radius proof — integrated into code review;
3. benchmark validity — integrated into research experiments.

Everything else is already covered, belongs to the harness layer, is product/language-specific, or remains an observe-first candidate.
