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
