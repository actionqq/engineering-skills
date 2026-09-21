# Runtime Boundaries and Failure Behavior

Use when correctness depends on multiple processes, durable stores, asynchronous work, or independently failing dependencies. A package diagram alone cannot explain these behaviors. Keep the simplest topology that meets the requirements; queues and services need a concrete reason to exist.

## Follow one operation end to end

Map ingress, execution owners, durable state, external effects, and the result observed by the caller. Distinguish process and trust boundaries from source directories. Show a short sequence or state table where it clarifies ownership and timing.

For each important transition identify the authoritative state, writer, operation identity, and point at which success becomes durable. State what is atomic and what can be temporarily inconsistent. Acknowledged acceptance, completed processing, and an externally visible effect may be different milestones. Define what readers see between them.

## Test the failure windows

Walk through a crash or lost connection before and after each durable write, external effect, and acknowledgement. Include duplicate delivery, concurrent attempts, stale workers, and out-of-order events when the transport permits them. Choose transactions, durable operation records, an outbox, fencing, reconciliation, or compensation only where they close an identified window. Name the remaining window if no available mechanism closes it.

For example, a worker may commit a database update and die before acknowledging a message. Redelivery must not repeat a nonrepeatable effect. A queue's delivery setting alone cannot make an external service effect atomic with the database; the design needs a supported deduplication or recovery path at that boundary.

Define cancellation and timeout semantics: whether work stops, may complete later, or needs reconciliation. Compensation is a new fallible action, not time travel; identify who retries or resolves failed compensation. Make terminal failures and manual recovery visible instead of retrying indefinitely.

## Bound work and expose the right signals

Relate capacity to the actual workload and agreed latency, availability, and recovery requirements. State assumptions needing measurement. Consider request deadlines, retry budgets, bounded concurrency, queue growth, and downstream saturation together; independent retry layers can multiply load. Define overload behavior and the effect on already accepted work.

Select signals that distinguish acceptance, progress, completion, and stuck or failed work. Carry correlation identity across boundaries without exposing secrets. Specify the observation that would trigger recovery and how the recovery can be verified. Where backup or restore is part of the requirement, cover restore evidence and acceptable data loss, not just backup creation.

Deliver the relevant topology, invariants, failure responses, and verification scenarios in the maintained design. A design-only request calls for these decisions and evidence needs, not infrastructure deployment or a new operations program.
