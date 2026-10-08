# Plain Technical Language

Use when the reader is outside the immediate specialty, works in a second language, needs text that translates reliably, or explicitly asks for plain or controlled technical English.

This is a communication mode, not permission to simplify away technical meaning.

## Plain mode

Plain mode is the default when the request is simply to make technical prose easier to understand.

- Preserve exact code, identifiers, commands, flags, file paths, product names, quoted errors, and normative protocol terms.
- Put a relevant condition before the instruction it governs.
- Prefer one concrete action per procedural sentence when combining actions would make execution ambiguous.
- Name the actor or system responsible for an action when omission would hide ownership.
- Introduce an unfamiliar technical concept before a step depends on it, using the shortest definition that preserves meaning.
- Break long noun chains and vague abstractions into explicit relationships.
- Prefer facts and consequences over reassuring filler such as “easy,” “simple,” or “seamless.”
- Keep warnings close to the action and state the concrete risk.
- Use consistent terminology; do not rotate synonyms merely for variety.

Do not impose fixed word counts or grammar bans when natural, precise prose is clearer. In standards, API contracts, or requirements, preserve normative meanings such as `MUST`, `SHOULD`, `MAY`, and project-defined equivalents. Readability never authorizes changing obligation level.

## Strict controlled-English mode

Use a strict controlled-language mode only when the user explicitly requests ASD-STE100, Simplified Technical English, or another named controlled-language standard.

Apply the named standard only to the extent its authoritative rules are actually available. Preserve code and project literals exactly. Do not convert normative engineering terms merely to satisfy a vocabulary preference.

If the full standard, required vocabulary, or compliance checker is unavailable, describe the result as controlled-English-inspired or a best-effort rewrite rather than claiming formal compliance.

## Translation-friendly checks

For text intended for localization or non-native readers:

- keep modifiers next to what they modify;
- prefer explicit subjects and relationships over pronouns with unclear antecedents;
- avoid idioms, decorative metaphors, and culture-specific wordplay in procedural text;
- split ambiguous `and` or `or` constructions when grouping matters;
- keep one name for one project concept.

The goal is one unambiguous reading, not robotic prose.
