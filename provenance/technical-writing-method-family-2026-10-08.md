# Technical writing method family research — 2026-10-08

This note records the document-format research and the experimental `tech-writing` entry added on `experiment/pstack-upstream-sync`. It is a branch-level method record. It does not replace the canonical v0.2 source lock or method map until the experiment is promoted deliberately.

## Question

The collection already expects `tech-design` to produce maintained designs and `tech-review` to produce usable review results. The open question was whether document structure and writing rules should be invented locally, copied from one upstream template, or treated as a reusable method family with artifact-specific formats.

The conclusion is **artifact-specific methods, not one universal technical-document template**.

Precedence for every artifact is:

1. explicit user format and edit boundary;
2. established repository template, contribution/style guidance, and neighboring maintained artifacts;
3. an artifact-specific fallback from this method family.

## Primary method evidence

### Cursor pstack

Pinned revision: `ccb5507cec1546dc88135c1139c811e6c59115ba`.

Reviewed:

- `pstack/skills/technical-writing/SKILL.md`

Retained:

- write for a tired engineer's first read;
- cut words that do no work;
- use ordinary language and the codebase's exact vocabulary;
- avoid invented synonyms and jargon;
- select structure by reader purpose rather than one generic layout;
- consistency and unambiguous wording matter more than mechanical prose rules.

Rejected:

- pstack-specific cross-skill invocation and model/runtime conventions;
- treating every document as a mandatory multi-skill pipeline.

### Tech Leads Club agent-skills

Pinned revision: `120b67676388241b314699fa8fa9af25ada6d1d4`.

Reviewed:

- `(development)/docs-writer/SKILL.md`
- `(development)/docs-writer/references/style-guide.md`
- `(creation)/create-technical-design-doc/SKILL.md`
- `(creation)/create-rfc/SKILL.md`
- `(creation)/create-rfc/references/section-templates.md`
- `(creation)/create-adr/SKILL.md`

Retained:

- general documentation, RFC/proposal, technical design, and ADR are different artifact jobs;
- project contribution/style guidance is authoritative when present;
- direct, active, consistent developer prose;
- RFC/proposal criteria should be explicit before comparing serious options;
- technical designs need scope, chosen approach, risks, and conditional operational sections rather than a prose dump;
- ADRs have a mature format family: Nygard for lean records, MADR when structured option comparison is genuinely useful.

Rejected as universal defaults:

- mandatory RACI metadata;
- mandatory option matrices and action-item tables for every proposal;
- a mandatory `Implementation Plan` section inside every technical design;
- a mandatory large ADR template;
- fixed process gates that duplicate `work-plan` or decision authority in this collection.

### mattpocock/skills

Pinned revision: `f3fc5632f401156837ee3872f14fe33ccf1024ea`.

Reviewed:

- `skills/engineering/domain-modeling/SKILL.md`
- `skills/engineering/domain-modeling/ADR-FORMAT.md`
- `skills/engineering/domain-modeling/GLOSSARY-FORMAT.md`
- `skills/engineering/to-spec/SKILL.md`

Retained:

- ADRs can be very small when the decision and rationale are simple;
- ADRs are warranted by consequential, surprising, or genuinely traded-off decisions rather than routine implementation choices;
- domain glossaries use canonical terms, concise definitions, and meaningful avoided aliases;
- specifications separate problem/user behavior/scope from implementation detail.

Rejected:

- treating Matt's current `GLOSSARY.md` filename as a universal repository convention;
- tracker publication as a requirement;
- assuming a repository's existing `CONTEXT.md` must be converted into Matt's glossary role.

## Corroborating sources reviewed, not directly imported

These sources informed the decision but are not used as independent copied method text in the new standalone folder.

### Anthropic `doc-coauthoring`

Revision observed: `683bc88e56f3e09ba94f7055977f3d3aa499f202`.

Strong signal: before choosing structure it asks whether the user/project already has a template or required format. Its cold-reader testing idea is useful for substantial docs. Its full staged interview/brainstorm/section-curation workflow is intentionally not adopted as a mandatory process.

### citypaul technical-writing

Revision observed: `cd4028d57d6e4e95814f7b8ee55ca13c23a9c2f0`.

Strong signal: one primary reader job, scannable structure, material claims need evidence, maintained docs describe current truth, exact strings matter for humans and agents. The experiment keeps the same ideas through the selected pstack/TLC sources rather than adding another direct dependency.

### Vercel ADR skill

Already part of the collection's source family. Its simple and MADR templates put implementation plans and verification checklists inside the ADR. That is useful for agent-first ADR workflows, but it conflicts with this collection's separate design / work-plan / verification lifecycles. The experiment therefore keeps links to delivery evidence rather than duplicating full plans inside ADRs.

### github/spec-kit

Already part of the collection's source family. Its separate specification and implementation-plan templates support keeping behavior/specification ownership distinct from work decomposition.

### simplyblock operator design-doc

Its project-specific design skill is intentionally detailed, but it explicitly separates design doc, test plan, and work plan and says to include only the design sections that are actually needed. This corroborates the collection's conditional-section approach; the Kubernetes/operator-specific template is not imported.

### dotcontext

Its `.context/CONTEXT.md` is a broad project-current-truth artifact covering entities, modules, flows, integrations, architecture, glossary, and conventions. Matt's historical `CONTEXT.md` was effectively a domain glossary. The incompatibility is evidence that `CONTEXT.md` is a project-defined role, not a universal document type.

### GitHub awesome-copilot

Technical-writer and reviewer agents corroborate Nygard ADR structure, audience-aware documentation, file/line evidence, and finding fields such as evidence, impact, and remediation. Their broad project-documentation and machine-JSON report formats remain task-specific and are not adopted as universal layouts.

## Organization chosen for this experiment

Add one user-task entry:

- `tech-writing`: create or revise technical documents when their substantive engineering conclusions are already established or can be verified from available evidence.

Do **not** add separate top-level entries for `adr`, `context`, `rfc`, or `review-report`. They are document/artifact methods, not broad user-task categories.

`tech-writing` contains conditional references for:

- general style and document structure;
- technical design documents;
- ADRs;
- context/glossary documents;
- review reports.

The existing owners remain responsible for their own deliverables:

- `tech-design` decides software behavior/architecture and writes the resulting design, ADR, or context artifact without requiring a second Skill invocation;
- `tech-review` performs the review and writes the report without requiring a second Skill invocation;
- `research`, `work-plan`, `handover`, and other entries continue to write their own outputs as part of their work.

This follows the same organization principle used by the v0.2 frontend method family: share method principles, keep task-specific entrypoints, and avoid runtime Skill-to-Skill dependencies.

## Default artifact decisions

### Technical design

Existing repository format wins. Without one, use a small core: context/problem, goals/non-goals, chosen approach/key decisions, important contracts/failure semantics, verification path, risks/blockers/open questions. Add data flow, APIs, state/concurrency, security, performance, observability, migration/rollback, or alternatives only when relevant. Detailed task decomposition remains in `work-plan`.

### ADR

Existing repository format wins. Without one, default to lean Nygard-style Context / Decision / Consequences plus status/date. Use MADR-like drivers/options only when the trade-off history materially benefits from it. Do not make implementation plans and test matrices mandatory ADR content.

### CONTEXT / glossary

Determine the existing artifact role first. A domain glossary gets canonical terms and definitions. A broad project-context artifact can carry current purpose, concepts, modules, flows, integrations, architecture boundaries, and consistently evidenced conventions. Do not rename or repurpose an existing `CONTEXT.md` just to follow another ecosystem.

### Review report

Preserve the review method's meaningful axes and repository format. Every finding must still contain a precise target, trigger/scenario, evidence or violated requirement, impact, and correction direction. Report review scope, actual validation, and `Verified / Not verified / Not applicable` evidence limits. These are information requirements, not mandatory visible subheadings.

## Validation status

This is an authored experiment. Adding the entry and local references does not prove natural-language routing, document quality, or cross-host behavior. Before promotion, update the canonical source lock/method maps deliberately and run structural/resource-closure checks plus targeted behavior/routing cases for the new entry and the changed `tech-design` / `tech-review` outputs.
