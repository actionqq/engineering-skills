# Enforcement and Proof

Use this to convert a repeated failure into the smallest durable mechanism that addresses its root class rather than its latest wording.

## Build the failure class from evidence

Collect concrete examples from available repository history: reverts, review comments, CI failures, incidents, repeated user corrections, agent transcripts, or workarounds. Preserve enough context to distinguish one root cause from several unrelated symptoms.

Cluster by the violated contract. Similar wording is not evidence of a shared cause. Verify the class against the current repository before changing anything; architecture, tooling, or ownership may already have made an old failure impossible.

## Choose the owning surface

Ask which surface could have prevented the failure without requiring every contributor to remember a warning.

| Owning problem | Prefer |
|---|---|
| Multiple valid-looking paths or duplicate owners | architecture, API shape, visibility, or removal of an obsolete internal path |
| Invalid combinations or states | types, constructors, schema, or explicit domain model |
| Mechanically recognizable forbidden change | lint, dependency rule, static check, or CI |
| Repetitive transformation or setup | canonical helper, generator, migration script, or tool |
| Observable behavioral regression | focused behavior or contract test |
| Context-dependent judgment | maintained guidance, Agent Skill, or review criterion |

Choose the strongest useful layer whose cost and blast radius fit the recurrence. A prose rule is appropriate for irreducible judgment; it is weak enforcement for a mechanically detectable mistake.

Before editing instructions, ask whether a competent agent following the current instruction should already have behaved correctly. If yes, investigate visibility, context, model variance, harness behavior, tooling, or another owning layer instead of duplicating the sentence.

When enforcement requires a test, API cleanup, architecture change, or migration, use that owner's normal method rather than reproducing its whole procedure here. Hardening chooses the surface and the proof obligation; it does not replace implementation or design guidance.

## Prove the guardrail on the historical mistake

Where feasible:

1. reproduce or construct a faithful form of a real past mistake;
2. show the new guardrail rejects or detects it for the intended reason;
3. show the supported path still works;
4. exercise the mechanism where future contributors will encounter it, such as CI when CI is the enforcement point.

The proof concerns this failure class. A synthetic toy case that misses the historical mechanism, a source-text check with no real policy contract, or a warning that nobody executed is insufficient evidence of prevention. If faithful replay is unavailable, state the limit.

## Remove obsolete compensating prose

When a structural mechanism now owns a rule, remove or shorten instructions that existed only to compensate for the old weakness. Keep concise navigation or rationale when a maintainer still needs it.

The goal is not more guardrails. The goal is fewer ways to repeat the same consequential mistake.
