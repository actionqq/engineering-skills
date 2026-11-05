# Promoted method additions — 2026-10-08

This file is the human-readable companion to `method-map.2026-10-08.json`. The JSON fragment is part of the canonical method set and is validated together with `method-map.json`.

| Method | Destination | Primary source | Decision |
|---|---|---|---|
| technical-writing-style | `tech-writing` core + `style.md` | Cursor pstack `technical-writing` + existing writing-for-agents source | Keep reader-first, direct, project-exact prose; reject runtime cross-skill dependencies and rigid sentence rules. |
| technical-document-format | `tech-writing/design-doc.md`, `tech-design/documentation.md` | pstack writing + existing to-spec | Existing repository format wins; otherwise use a small stable core and conditional risk sections. Do not embed a second work plan. |
| adr-context-writing | `tech-writing/adr.md`, `tech-writing/context.md` | existing Matt ADR/context + writing source | Prefer lean ADRs and repository-defined context roles. Do not impose a universal `CONTEXT.md`/`GLOSSARY.md` convention. |
| review-report-writing | `tech-writing/review-report.md`, `tech-review/reporting.md` | pstack writing + existing code-review source | Preserve evidence-bearing finding fields and review limits without forcing a visible template or re-running the review. |
| blast-radius-proof | `tech-review/code.md` | Cursor pstack `blast-radius` | Follow non-symbol boundaries and prove safety-critical facts proportionately; unproved applicable claims stay unverified. |
| benchmark-validity | `research/experiments.md` | Cursor pstack `benchmark-checklist` + existing experiment source | Verify work/output/errors/config equivalence/variance/limiter/bounds before acting on performance numbers; allow clearly labelled ballparks. |
| repository-hardening-enforcement | `repo-hardening` core + `enforcement.md` | Warp Skill Doctor + existing structural-enforcement source | Attribute recurring mistakes to their owning surface, enforce them at the strongest proportionate layer, and prove the guardrail against a historical mistake. |
| plain-technical-language | `tech-writing` core + `plain-language.md` | Cursor pstack `technical-writing` | Use explicit, translation-friendly technical prose when requested while preserving literals and normative meaning; do not claim controlled-language compliance without evidence. |

The broader research and rejected alternatives remain in `technical-writing-method-family-2026-10-08.md` and `pstack-capability-assessment-2026-10-08.md`.
