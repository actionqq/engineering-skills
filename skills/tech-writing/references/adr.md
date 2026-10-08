# Architecture Decision Records

Use the repository's existing ADR location, numbering, metadata, status vocabulary, and template when they exist. An ADR is a durable record of a consequential decision and its rationale, not a second implementation plan.

## Choose the smallest format that preserves the decision

When the project has no ADR convention, use a Nygard-style core by default:

```markdown
# <Decision title>

**Status:** <proposed | accepted | deprecated | superseded>
**Date:** <date>

## Context

<The forces, constraints, and situation that made the decision necessary.>

## Decision

<What was decided and the decisive reason.>

## Consequences

<Important benefits, costs, constraints, and follow-on effects.>
```

Metadata can use frontmatter or the project's established form. Keep the title a decision-oriented noun phrase or direct statement rather than the question that preceded it.

For a very small decision, the repository may legitimately use a one-paragraph ADR. For a decision with several serious options and explicit drivers, a MADR-style extension can add decision drivers, considered options, and structured trade-offs. Do not expand every ADR into an options matrix when the extra structure preserves no useful history.

## Record rationale, not delivery bookkeeping

Context explains why a decision was necessary without pretending the chosen option was inevitable. Decision states what governs future work. Consequences record meaningful positive, negative, and neutral effects.

Add alternatives when a future maintainer could reasonably reopen them without the recorded reason. Represent rejected options honestly; do not construct weak alternatives merely to make the chosen one look good.

Link the active design, work plan, implementation, or verification record when useful. Do not copy a full implementation plan, task list, test matrix, or current delivery status into the ADR. Those facts change on a different lifecycle from the durable decision.

## Preserve history

An accepted ADR is historical evidence. Do not rewrite its core rationale so it appears always to have supported a later decision. When the governing decision changes, follow the repository's amendment or supersession convention and link the records in both directions when possible.

Use `deprecated` for a decision that no longer governs new work without a direct replacement, and `superseded` when a replacement exists. Do not mark a decision rejected merely because implementation failed or later evidence caused reconsideration.

A proposal is not accepted because code was written. A successful test is not decision approval. Preserve the distinction between decision status, implementation state, and verification evidence.

## Keep terminology and scope precise

Explain project-specific terms before relying on them, or link to the maintained glossary/context that owns them. One ADR should capture one coherent decision; consequences that follow directly from that decision can stay with it, while independently reversible decisions deserve their own records.

Create an ADR only when the reasoning is worth preserving: the choice is costly or non-obvious to reverse, surprising without context, or the result of a real trade-off. Routine implementation detail does not become architectural merely because it can be written as an ADR.
