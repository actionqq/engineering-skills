# Upstream sweep — 2026-10-08

This note records the second read-only upstream sweep behind the `repo-hardening` experiment and the method refinements promoted with it. It is research provenance, not behavior-test evidence.

## Promoted conclusions

- **Repository hardening is a distinct user task.** Repeated mistakes should be attributed to their owning surface and prevented at the strongest proportionate layer. One-off bugs remain diagnosis; current-change findings remain review; Skill authoring remains `skill-dev`.
- **Real session failures are evidence, not automatic Skill edits.** A Skill change is justified only when a missing or wrong instruction owns the failure. Existing correct guidance, model variance, unavailable context, harness failures, product behavior, and repository enforcement remain separate causes.
- **Testing must be falsifiable.** A useful test names the behavior it protects; source-string presence and private-structure change detectors are not substitutes for behavior unless the source rule itself is the contract.
- **Architecture should reduce shared mutation before adding serialization.** Validate external representations at real boundaries, separate independent writers when possible, and design retried mutations to converge from partial prior state.
- **Repeated fixes can share a bad premise.** If fixes that rely on the same assumption keep failing the same gate, measure that assumption directly before another patch.
- **Technical prose preserves truth and ownership.** Editing must not silently strengthen claims or import facts from a voice sample. Plain-language modes preserve exact literals and normative obligation levels.
- **Web-quality evidence has levels.** Field/RUM evidence, controlled lab runs, and static source inspection answer different questions; aggregate audit scores are not proof of quality.

## Upstreams reviewed

The sweep inspected current or latest available revisions of:

- `cursor/plugins` pstack at `ccb5507cec1546dc88135c1139c811e6c59115ba`: `correct`, technical-writing, benchmark/blast-radius, and principle Skills for boundaries, shared state, idempotency, migration, and failed premises.
- `warpdotdev/common-skills` at `2a03b403b4f8d42cb54b8953697737193b2e8306`: `skill-doctor` and `references/skill-improvements.md`.
- `anthropics/skills`: the current eval family (`build-eval`, `eval-audit`, `eval-hillclimb`) as comparative material for evaluation integrity.
- `obra/superpowers`: current test-driven-development guidance, especially falsifiability and change-detector traps.
- `addyosmani/clarity`: provenance-preserving editing and least-invasive rewrite rules.
- `AminBlg/SimpleEnglish` at `a6fcb4fde098b33617cc1578d151ebf58774b883`: plain/controlled technical English as a specialized mode rather than a global default.
- `addyosmani/web-quality-skills`: measurement-first frontend quality review and evidence separation.
- GitHub Spec Kit bug-fix guidance: original-reproduction verification remains distinct from narrower regression checks.

Only sources represented in source locks and method maps are direct method dependencies. The others above remain research comparisons that informed adaptation decisions.

## Deliberate rejections

The collection does not absorb:

- mandatory subagents, model routing, worktrees, arenas, swarms, or transcript fan-out;
- fixed recurrence counts as a prerequisite for hardening;
- automatic Skill edits after every correction;
- documentation-first enforcement when architecture, types, CI, tooling, or tests can own the rule;
- fixed sentence limits or blanket modal-word replacement as the default writing style;
- a claim that `repo-hardening` means security hardening;
- aggregate benchmark, Lighthouse, or eval scores as proof without checking what the measurement actually establishes.

The experiment remains a promotion candidate. Prepared eval and discovery cases are not model-run acceptance evidence.
