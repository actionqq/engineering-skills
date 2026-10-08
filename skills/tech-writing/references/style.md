# Writing and Document Structure

Use the repository's established style before a generic writing convention. The rules below are fallbacks and quality checks, not a reason to reformat unrelated text.

## Pick the reader job

Decide what the page primarily helps a reader do:

- **Tutorial:** learn by completing a controlled path.
- **How-to:** accomplish a real task with enough branching for the situation.
- **Reference:** look up exact facts, options, contracts, states, or commands.
- **Explanation:** understand why a bounded concept or design works as it does.

A page can contain supporting material from another mode. Split only when mixed purposes make the audience, next action, or completeness contract unclear. A technical design, ADR, review report, runbook, troubleshooting page, or release note has its own artifact convention and should not be forced into one of these four labels.

## Write like the project, not like a generic assistant

Use the codebase as the vocabulary source. Keep exact symbols, file names, flags, event names, API terms, and domain language. Do not rotate through synonyms for variety.

Prefer direct everyday words. Cut filler, ceremonial introductions, vague praise, marketing language, and phrases that do not change meaning. Active voice and present tense are useful defaults, but clarity matters more than mechanically satisfying a grammar rule.

Vary sentence length naturally. One thought per sentence does not require every sentence to be short. Use concrete conditions and consequences instead of abstract phrases such as “may cause issues.” Do not hide uncertainty behind passive voice or nominalized jargon.

For instructions, put the relevant condition before the action and use an imperative verb. Address the reader as “you” when the repository's documentation style does so. Do not describe an easy operation as “simple,” “obvious,” or “quick” merely to sound reassuring.

## Make structure carry meaning

Use one H1 unless the target format says otherwise. Follow the repository's heading capitalization and hierarchy. A useful heading tells a skimmer what the section gives them, not only its broad topic.

Use numbered lists only when order matters. Use bullets for unordered choices or facts. Use a table when rows share the same fields and comparison matters; do not turn prose into a table just because the data can be tabulated.

Add a table of contents only when it materially improves navigation. Verify generated anchors when readers or tooling depend on them. Deep nesting is a signal to reconsider organization, not an automatic defect.

Put code, commands, paths, configuration keys, and exact UI labels in their established literal form. A code block must either run as shown or be clearly identified as a fragment. Include expected output when the reader needs it to know that a step succeeded.

## Keep technical claims trustworthy

A maintained document must describe the current truth at the scope it claims. Check material behavior, command, option, configuration, compatibility, version, and quantitative claims against source or another authoritative artifact. Date or otherwise scope facts that can age.

Do not claim exhaustive coverage from a partial check. If a command was not run, do not write its expected result as observed evidence. If a document describes a planned design rather than implemented behavior, make that status clear where a reader could confuse the two.

Machine-check what is cheap and deterministic, such as local links, generated anchors, examples, or documented commands, when the task and environment allow it. Manual review remains appropriate for meaning, trade-offs, and audience fit.

## Finish for the cold reader

Remove repetition that exists only because the authoring conversation revisited the same point. Keep prerequisites near the action they govern and important limitations near the decision they affect. Link to the maintained owner of changing details instead of cloning them.

A finished document should make sense without the chat that created it. A reader should be able to tell what is authoritative, what is conditional, what is unresolved, and where to go next.
