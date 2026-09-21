# Responsibilities, Contracts, and Module Depth

Use this for logical responsibility and interface shape. Physical movement alone cannot solve a responsibility problem.

## Use precise concepts

A module is a coherent owner of behavior and decisions with one or more caller-facing contracts. Its contract includes everything callers must understand: operations, data, preconditions, ordering, configuration, errors, side effects, lifecycle, and relevant performance or consistency obligations. A short function signature can still impose a large learning burden.

Depth means useful coherent capability behind that burden, not lines of implementation. Caller leverage asks how much a caller gains from learning the contract. Locality asks whether a change, defect, and its verification have one sensible owner.

A seam is a place where behavior can be selected or substituted without editing that location; identify its enabling point, such as construction or configuration. Not every interface is a seam. An adapter supplies or translates a concrete dependency at a useful boundary.

## Find what should be hidden

Trace representative callers and collaborators. Inventory repeated policy, sequencing, validation, error recovery, provider representations, dependency construction, and private setup reconstructed in tests. Include change history when it actually shows common change pressure.

Apply a behavior-preserving inlining thought experiment. If inlining spreads policy, recovery, or representation knowledge among callers, the boundary has value. If it removes only forwarding and leaves callers simpler without spreading knowledge, the layer may be misplaced. Do not pretend that deleting the behavior proves the layer unnecessary.

Look for counterevidence before combining modules: independent authorization, failures, deployment, transactions, ownership, or change axes may require separation. Thin routes, CLI entries, adapters, generated clients, and composition roots can be intentionally thin. A small facade over unrelated policies can create a god module rather than depth.

## Design from caller scenarios

State one coherent responsibility and explicit exclusions. Exercise a common call and relevant invalid-input, partial-failure, cancellation, retry, and lifecycle scenarios. Make important effects and costs visible without exposing the private collaborator graph. An enormous options object or generic command dispatcher often moves orchestration back to callers.

Classify important dependencies across multiple axes:

| Axis | Consequence to check |
|---|---|
| In-process or remote | Serialization, latency, cancellation, partial failure |
| Owned or third-party | Change authority, support, compatibility |
| Trust and identity | Validation, authorization, delegated identity |
| Transaction and consistency | Atomicity, visibility, compensation |
| Resource ownership | Acquisition, sharing, cleanup, shutdown |
| Volatility | Whether hiding provider knowledge buys useful stability |
| Substitute fidelity | What fast tests prove and what requires a real dependency |

Prefer stable dependencies selected at construction to forcing callers to pass the same collaborators repeatedly. Use application-language boundaries for meaningful external capabilities; do not wrap every standard-library function or reproduce an entire vendor API as a “port.”

Read [Competing designs](alternatives.md) before committing to an expensive interface with plausible different shapes. Read [Structure and migration](structure.md) when enforcement or physical placement changes.

## Evolve with evidence

For an existing cluster, establish behavior protection, then move one responsibility at a time. A temporary compatibility facade needs named consumers and a retirement condition. Keep adapter equivalence and algorithm tests that still add distinct evidence; do not delete them merely because a higher-level test exists.

Check whether callers coordinate less, duplicated decisions have one owner, failure semantics remain honest, and tests cover substitute fidelity gaps. If claiming total complexity reduction, compare the same end-to-end scope including new adapters, configuration, operations, and compatibility bridges. Moving complexity out of one file is not evidence that total mechanism decreased.
