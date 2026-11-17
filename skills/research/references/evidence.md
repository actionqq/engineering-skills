# Evidence, Disagreement, and Confidence

Use for research whose result depends on source quality, currentness, or conflicting observations.

## Keep an evidence ledger when it helps

Record the claim, original source and locator, exact revision/version/tier, date observed, relevant environment, finding, and limitation. A short answer may carry these inline; a consequential comparison benefits from a compact ledger.

Classify claims by what supports them:

- A documented guarantee applies only within the documented configuration and support scope.
- Source code establishes implementation at the inspected revision, not an everlasting supported API.
- An experiment establishes an observation under its recorded inputs and environment.
- An inference combines evidence and assumptions; make the assumptions visible.

An absence is different from a guarantee. Not finding an advisory does not prove safety. Not finding a documented limit does not prove there is no limit. Several derivative articles do not provide independent confirmation of their shared origin.

## Distinguish mechanism, recorded motive, and present judgment

Identify what the question asks before selecting evidence. A question phrased as "why" can concern a mechanism, an original decision, or whether that decision still makes sense today.

| Claim | Evidence that can support it |
|---|---|
| How the system behaves at a revision | The relevant code and configuration, plus execution when the claim needs it |
| Why a design or threshold was chosen | The introducing decision record, commit or PR discussion, issue, or other attributable account of the choice |
| Whether the choice is appropriate now | Current requirements, alternatives, constraints, and observed behavior, with the assessment identified as present judgment |

For a historical-motive question, locate the change that introduced the behavior and read its rationale in context. Inspect later changes when they affect the explanation. A line's most recent editor may only have formatted or moved it; a comment may describe a later interpretation. Connect the record to the actual decision, and distinguish a proposed rationale from the accepted choice. One adequate record can settle a bounded question; an exhaustive repository history is not required.

State separately what the implementation shows, what the record attributes to the authors, and what you infer. Code can support or contradict a proposed mechanism without establishing an author's motive. A missing record leaves that motive unknown; a plausible engineering benefit remains an inference. Conflicting accounts should retain their dates and scope instead of being merged into a tidy retrospective story.

Illustrative example: current code caches a provider response for ten minutes. That establishes a reuse mechanism, and measurement could establish fewer provider calls. If the introducing PR explicitly chose ten minutes to remain within a provider quota, that record supports the original reason. It does not establish that ten minutes remains appropriate under today's quota and freshness requirements. If the rationale is unavailable, explain the mechanism and label quota reduction as a possible reason rather than writing that it was the reason.

## Search to challenge the provisional answer

Use terminology from different communities, older and current versions where relevant, and failure-oriented queries. Look for the strongest plausible objection, such as an unsupported deployment mode, a migration incident, or an unrepresentative benchmark. Do not insist on locating a dissenting source if none is available; state the search limit.

Prefer sources close to the actual claim. Official technical material is appropriate for supported behavior; reproducible independent measurements are useful for performance. Record incentives and limitations without dismissing a source solely because it has an interest.

## Diagnose conflicts

Compare definitions, version, mode, workload, hardware, scale, measurement window, and success criteria before deciding that sources disagree. Identify whether a conflict is explained, one source is obsolete or mistaken, or the evidence remains insufficient.

Example: a new version may permit concurrent server-side batches while its offline mode still requires serialization. “Version 2 supports concurrency” cannot settle a question about the offline project. Similarly, warm-cache throughput does not rebut a cold-start latency observation.

When performance matters, seek representative reproduction and expose what a measurement excludes. Avoid combining incompatible numbers into a synthetic ranking.

## State confidence usefully

Explain which important claims are directly supported, which rely on inference, and what remains missing. Use a qualitative confidence description when helpful; do not invent probabilities. A recommendation can be useful with limited confidence if its conditions and reversibility are explicit.

Stop when additional evidence no longer changes a material decision. If one unresolved fact could reverse the conclusion, state the smallest next check and its consequence instead of accumulating peripheral sources. Preserve enough source identity for another investigator to verify the argument later.
