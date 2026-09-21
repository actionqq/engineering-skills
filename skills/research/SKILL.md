---
name: research
description: Investigate substantive technical questions using primary sources, source code, and reproducible evidence. Use to resolve conflicting claims, verify version-dependent capabilities, or establish what is known and uncertain. Summarizing supplied text, routine code navigation, and implementing an already-decided choice do not need a research workflow.
---

# Technical Research

Produce an answer with traceable evidence and explicit limits. Communicate in the user's language. Research quality depends on resolving uncertainty, not collecting the most links.

## Frame a question that can be answered

Identify the actual question, its decision context, disqualifying constraints, and the kind of answer needed. Preserve a prescribed technology or product unless evidence reveals a material incompatibility. Do not turn a question about one capability into a market-wide selection exercise.

Define what evidence would settle the important claims. For a version-specific capability, this may be a supported configuration in official documentation plus a reproducer. For a performance claim, identify the workload and measurement that would make a comparison relevant. Investigate facts yourself; surface missing decision criteria only when they could change the answer.

## Gather independent evidence

Read [Evidence practice](references/evidence.md) for conflicting, time-sensitive, consequential, or multi-source work.

Start with the closest available evidence: project code/configuration for local behavior, exact documentation or source for a dependency, original papers or data for research claims. Verify current versions, support, pricing, or other changing facts when they matter. Offline access permits a bounded answer from identified local material, not a claim about current external status.

Search with different vocabulary and for adverse evidence: limitations, incidents, migration away, unsupported modes, failed experiments. Trace repeated claims to their origin. Ten articles repeating one measurement are one line of evidence. A vendor's assertion establishes what it promises, not that an independent benchmark confirms it.

Read the material you cite. Search snippets and secondhand references are discovery aids. Record the observation and conditions, not just the URL. Distinguish an official guarantee, an implementation detail at a pinned revision, an experimental observation, and your inference.

## Resolve and stop

Explain disagreements through versions, definitions, workloads, configurations, measurement, or evidence quality. If the evidence cannot decide between explanations, say what remains unknown and which next observation would discriminate. Do not average incompatible measurements or invent certainty.

Stop when the question is supported at the required confidence and more collection is unlikely to change the decision. If an essential fact is unavailable, give the useful bounded conclusion and the missing evidence. Do not conduct an open-ended survey to conceal that one blocker.

## Deliver

Lead with the answer, then the reasoning, evidence, conditions, and what could change it. Put citations beside supported claims. Save a reusable record only when the task or downstream work needs it, using the existing project location. Record dates and versions for facts that can age.

Identify which current design assumption or decision the evidence supports or challenges. Keep observations and recommendations distinct from accepted decisions. Update the requested research artifact; change governing design, ADR, or context documents only when that is within the task, preserving their decision status. Do not create a document set merely to store a research answer.

A recommendation does not itself authorize procurement, account creation, installation, production access, or implementation. Continue only the actions covered by the actual task.
