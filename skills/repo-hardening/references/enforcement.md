# Enforcement and Proof

Use this reference to convert a repeated failure into the smallest durable mechanism that addresses its root class rather than its latest wording.

## Build the failure class from evidence

Collect concrete examples from the repository's available history: reverts, review comments, CI failures, incidents, repeated user corrections, agent transcripts, or workarounds that document the same mistake. Preserve enough context to distinguish one root cause from several unrelated symptoms.

Cluster by the violated contract. "Imported the wrong module", "copied the deprecated helper", and "bypassed the supported client" may be one class if the real problem is that two public paths expose the same capability. Similar text is not evidence of a shared cause.

Verify the class against the current repository before changing anything. A historical mistake can already be impossible because architecture, tooling, or ownership changed.

## Identify the owning surface

Ask which surface could have prevented the failure without requiring every contributor to remember a warning.

| Owning problem | Prefer |
|---|---|
| Multiple valid-looking paths or duplicate owners | architecture, API shape, visibility, deletion of obsolete paths |
| Invalid combinations or states | types, constructors, schema, explicit domain model |
| Mechanically recognizable forbidden change | lint, dependency rule, static check, CI |
| Repetitive transformation or setup | canonical helper, generator, migration script, tool |
| Observable behavioral regression | focused behavior or contract test |
| Context-dependent judgment | maintained guidance, Agent Skill, review criterion |

A prose rule is appropriate when the decision genuinely requires judgment. It is weak enforcement for a mechanically detectable mistake.

Before editing an instruction surface, ask whether a competent agent following the current instruction should already have behaved correctly. If yes, do not restate the instruction by default. Check trigger visibility, context availability, model variance, harness behavior, or another owning layer.

## Remove competing paths when safe

When the failure comes from an obsolete internal API or convention, inventory its callers. If there are no external compatibility obligations and callers can migrate together, prefer moving callers and deleting the old path in the same bounded change. A temporary adapter needs a named consumer and retirement condition.

Do not apply this to public compatibility commitments, independently deployed consumers, persisted wire formats, or other contracts that require staged migration.

## Prove the guardrail on the old mistake

A new mechanism should demonstrate value against evidence from the failure class:

1. reproduce or construct a faithful form of a real past mistake;
2. show the new guardrail rejects or detects it for the intended reason;
3. show the supported path still works;
4. run the same check at the place where future contributors will encounter it, such as CI when CI is the enforcement point.

A check that fails only because exact source text changed is not proof of behavioral prevention. A test that still passes when the harmful behavior is restored is too weak.

If a faithful replay is unavailable, state the evidence limit. Do not substitute a synthetic toy case and claim the historical failure is fully covered.

## Keep instructions smaller after hardening

When a structural mechanism now owns a rule, remove or shorten duplicate instructions that exist only to compensate for the old weakness. Keep concise navigation or rationale where a future maintainer needs to understand the mechanism.

The goal is not more guardrails. The goal is fewer ways to make the same consequential mistake.
