# PStack upstream sync — 2026-10-08

This note records the selective upstream synchronization performed on `experiment/pstack-upstream-sync`. It is an experiment-layer record, not a claim that the whole upstream repositories were merged or that the v0.2 source lock was globally repinned.

## Base

- Repository: `actionqq/engineering-skills`
- Base branch: `main`
- Base commit: `aa523b1464d1a2c3a5013d075e519acc9a8c3206`

## Upstream observations used

### mattpocock/skills

Pinned observation commit: `f3fc5632f401156837ee3872f14fe33ccf1024ea`

Files reviewed:

- `skills/engineering/tdd/SKILL.md`
- `skills/engineering/diagnosing-bugs/SKILL.md`
- `skills/productivity/grilling/SKILL.md`

Methods absorbed:

1. **Test-boundary tradeoffs**: when several test seams are plausible, state what each seam can catch and what it cannot observe before choosing the boundary.
2. **Forced-red integrity check**: when a failing result is deliberately produced by mutating code, fixtures, configuration, or a fault, confirm that the mutation actually landed before trusting the red signal.
3. **Decision-frontier batching**: ask independent decisions with the same settled prerequisites in one round, then recompute newly unblocked dependent choices. This remains an efficiency rule rather than a mandatory multi-round interview.

Explicitly not synchronized:

- the `CONTEXT.md` to `GLOSSARY.md` convention;
- tracker-specific setup and issue workflow;
- mandatory sub-agent/worktree orchestration from `implement-spec`;
- automatic PR/retro workflow coupling;
- a fixed 3–5 hypothesis requirement or a prohibition on useful source investigation without a perfect reproducer.

### Fission-AI/OpenSpec

Pinned observation commit: `9111a7654d7800391459431fff4eaf66e33a3d2e`

File reviewed:

- `skills/openspec-verify-change/SKILL.md`

Method absorbed:

- **Evidence-state separation**: distinguish an applicable check that is supported by evidence (`Verified`), an applicable check whose evidence is missing or unusable (`Not verified`), and a check that genuinely does not apply (`Not applicable`). A skipped or blocked applicable check must not be counted as passing or used to justify an unconditional readiness claim.

OpenSpec-specific schemas, CLI commands, artifact identifiers, archive gates, scoring, and directory conventions were not imported.

## Destination changes

| Destination | Synchronized method |
|---|---|
| `skills/tech-review/SKILL.md` | Verified / Not verified / Not applicable evidence semantics and readiness limits |
| `skills/diagnose/references/reproduction.md` | forced-red mutation integrity check |
| `skills/implement/references/testing.md` | seam catches/misses tradeoff |
| `skills/tech-design/references/requirements.md` | same-frontier independent decision batching |

No new Skill entry was created and no existing entry was renamed.

## Provenance handling

`provenance/sources.lock.json` and the canonical method maps describe the v0.2 pinned source set. This experiment does not partially rewrite that global lock because doing so for only four refinements would make the lock internally inconsistent with the rest of the source family. This file pins the exact upstream commits used by the experiment.

Before promoting this experiment into the next released baseline, regenerate or deliberately update the canonical source lock/method maps together, then run the repository's structural, resource-closure, and relevant behavior checks. Do not present this experiment note itself as validation evidence.
