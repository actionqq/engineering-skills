# Third-party notices

This Skill is an English synthesis rewritten for engineering-skills v0.2. It does not copy any one upstream workflow as the runtime contract, and no upstream endorsement is implied.

The frontend method family was studied from these pinned sources:

- [Anthropic frontend-design](https://raw.githubusercontent.com/anthropics/claude-code/dec92bc87ab6fe9c7be0fcba1f97966f902dd243/plugins/frontend-design/skills/frontend-design/SKILL.md) — intentional visual direction, typography, copy, responsive/focus quality floor, and anti-template critique.
- [Impeccable](https://raw.githubusercontent.com/pbakaus/impeccable/114ea1d3838fca73b253af45f873b9c4f5f213c8/skill/SKILL.src.md) — product/brand surface modes, incumbent-design continuity, bounded visual verification, interaction quality, and production-vs-design workflow separation.
- [UI/UX Pro Max](https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/09170eec67eefd46a7ae85de61b40c194020f997/.claude/skills/ui-ux-pro-max/SKILL.md) — organized UI/UX knowledge categories covering accessibility, interaction, responsive behavior, typography, forms, navigation, and stack-aware implementation guidance.
- [Taste Skill](https://raw.githubusercontent.com/tasteskill/tasteskill/37c8c376b92ebc02456f7c70776b514fddda88e1/skills/taste-skill/SKILL.md) — anti-slop heuristics for hierarchy, card overuse, state completeness, density, motion, and generated-content tells.
- [Vercel Web Interface Guidelines](https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1/README.md) — keyboard/focus, forms, responsive behavior, content, motion, semantics, and interface-quality checks.
- Matt Pocock's pinned prototype material already recorded by this repository — prototype-as-evidence boundaries and the distinction between experimental artifacts and production implementation.

Adaptations in v0.2 are deliberate:

- settled business/domain behavior is input to a frontend prototype rather than something the prototype redesigns;
- compatibility, performance, persistence, concurrency, and migration spikes are not responsibilities of this entry;
- fixed aesthetic dials, framework defaults, universal font/color bans, perpetual motion, and other source-specific taste rules are not adopted as universal requirements;
- existing product conventions and an explicit user brief outrank novelty;
- implementation and review reuse selected frontend principles through their own small references instead of embedding the full prototype workflow.

Exact source commits and SHA-256 values are recorded in `provenance/sources.lock.json`. Consult each upstream repository's license and notices before redistributing upstream text or assets.
