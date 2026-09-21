# Migration, Rollout, and Recovery

Use when changes affect persisted state, a published representation, or components that coexist at different versions. A local rename without retained data or independent consumers can use ordinary refactoring checks.

## Define the supported transition

Inspect current readers, writers, schema tooling, startup configuration, and deployment constraints. Identify old/new combinations that can actually coexist, including rollback after new writes. Reuse an accepted migration design; resolve missing behavior before destructive transformation.

Choose expansion, backfill, consumer switch, and retirement stages when coexistence requires them. A coordinated offline migration may be simpler when downtime is explicitly acceptable. Keep compatibility code only as long as the transition requires, with an observable retirement condition. Separate shipping code from enabling new behavior when that makes recovery possible.

## Make the data movement recoverable

Specify the mapping and invariants: identities, null/default meaning, uniqueness, references, and information that would be lost. Detect ambiguous or invalid rows before silently normalizing them. Counts alone cannot prove the values or relationships survived.

Make repeated execution and partial completion safe. For large backfills, define stable batching, checkpoints, restart behavior, and concurrent-write handling. A checkpoint must not advance past uncommitted work. Decide how late updates are captured, how conflicts are resolved, and when the new representation becomes authoritative. Avoid assuming two separate writes succeed together.

Review operation cost in the actual database or runtime: lock duration, transaction size, index creation, disk growth, and bounded load where relevant. A migration tested only on an empty database does not cover an existing dataset.

## Rehearse the likely failure

Use disposable representative data and the relevant real storage behavior. Exercise the transition, interrupted restart, repeated execution, and concurrent writes if supported. Check value-level invariants and both old/new reader behavior during their supported stages. Verify startup and configuration changes as part of the transition, not merely the transformation function.

Distinguish rollback of code from reversal of data. If old code cannot read new data or a transform discards information, state the point beyond which simple rollback is unsafe and provide a tested forward repair or restore approach appropriate to the task. Do not label a backup as a proven recovery without restore evidence.

Deliver scripts, tests, and concise operating instructions needed by the authorized change. Record rollout order, observable stop conditions, recovery limits, and checks that remain unrun. Local implementation and rehearsal do not authorize live deployment, production backfills, or destructive cleanup. Retain accurate implementation and verification status until those separately scoped actions actually occur.
