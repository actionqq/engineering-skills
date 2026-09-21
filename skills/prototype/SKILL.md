---
name: prototype
description: Build a small runnable prototype or experiment to answer a concrete engineering question. Use for interactive state models, UI alternatives, compatibility spikes, representative performance probes, or migration rehearsals. A prototype is evidence for a decision, not automatic production implementation.
---

# Prototypes and Experiments

Choose the experiment from the question, not from a preferred demo format. Communicate the question, results, and limitations in the user's language.

Write down the uncertainty, the observation that could support or disprove the hypothesis, the relevant conditions, and a proportionate time/resource bound. A runnable program alone is not a successful experiment. Derive thresholds from requirements or identify them as assumptions.

## Choose the appropriate form

- For business state transitions, data shape, or UI alternatives, read [Interactive prototypes](references/interactive.md).
- For compatibility, performance, persistence, concurrency, or migration, read [Engineering experiments](references/experiments.md).

Keep only machinery needed for a credible answer. Simplify incidental dependencies, but retain the boundary that determines the result: an in-memory collection cannot validate a database transaction guarantee, and a static mockup cannot establish interaction behavior.

## Run and interpret

Use the requested location or an identified disposable workspace. Keep prototype state and mutations away from live business resources unless the task explicitly requires and authorizes their use. Use available execution capabilities; a temporary folder is not by itself a security sandbox for untrusted code.

Record enough input, environment, commands, and observations to repeat the experiment. Add assertions, measurement, and error handling when they are necessary to trust the evidence. Do not ban tests simply because the work is called a prototype.

Keep failed observations. If you change the hypothesis, threshold, implementation, or workload, distinguish the runs. Stop at a supported conclusion, a specific missing prerequisite, or the agreed resource boundary. Do not convert an unavailable environment into a fabricated success.

## Deliver

Provide the artifact and run instructions, actual results, conclusion about the original question, and what was not tested. Keep useful evidence accessible to the next task. Capture accepted design consequences in the authorized project artifact; promoting experimental code to production, committing it, or publishing it follows the user's scope rather than happening automatically.

Link the experiment's conditions and results from any affected design or decision record updated within scope. A successful experiment does not accept an ADR or establish production verification. Before deleting disposable artifacts, preserve needed evidence and route lasting constraints to their existing project owner; report outstanding updates when they fall outside the task.
