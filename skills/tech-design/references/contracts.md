# Published Interfaces and Compatibility

Use for APIs, events, schemas, or libraries whose consumers cannot change atomically with their provider. A private function edited with all callers does not need a public versioning scheme.

## Establish the consumer boundary

Identify actual consumers, ownership, deployed versions, generated clients, and rollout constraints. Inspect the wire representation and serializer behavior as well as source types. Record which old/new producer-consumer combinations must work, for how long, and how that will be checked. Unknown consumers are an uncertainty to resolve, not proof that none exist.

Specify observable inputs, outputs, errors, and side effects before choosing a protocol shape. Distinguish omitted values, explicit null, empty values, defaults, and unknown fields. Define stable machine-readable errors and their retry meaning without leaking internal details. Reuse the project's protocol; look up authoritative version-specific standards when exact wire syntax matters.

## Evolve deliberately

Classify changes by what real consumers observe. An optional field may still break a strict decoder; a new enum value may break exhaustive switches. A rename in source is not automatically a safe rename on the wire. Check representative consumers or contract fixtures at the actual boundary, not only shared types compiled at the new version.

Prefer compatible extension when independently deployed consumers need continuity. An explicitly authorized coordinated break is valid: state affected consumers, deployment order, and recovery limits. Avoid maintaining versions forever without a support requirement. For deprecation, identify the replacement when one exists, communication owner, retirement condition, and evidence that remaining consumers are accounted for; do not invent a removal date.

## Make retries and authority explicit

A timeout means the caller lacks a result; it does not establish that no effect committed. For retryable mutations, specify operation identity and scope, same-key/different-payload behavior, concurrent duplicates, result recovery, and retention. Deduplication must survive the failures covered by the promise. Explain how the identity record and effect remain consistent; an in-memory cache or an uncoordinated check-then-write cannot establish durable at-most-once effects.

Separate authentication from permission to act on an object, tenant, or field. Derive ownership from trusted context and validate both incoming requests and third-party responses. Forward-compatible parsing must not pass arbitrary privileged fields into a mutation. For user-supplied fetch destinations, account for redirects and resolved addresses rather than relying on a hostname string check.

Bound costly input, result size, and work. Where pagination applies, define ordering, tie-breaking, cursor scope, and behavior under concurrent writes; state whether the view is a snapshot or may change. Use justified limits, not invented capacity numbers.

Finish with concrete compatibility and failure examples: an older reader, an unknown value, a lost response followed by retry, and an unauthorized cross-owner operation when applicable. Preserve the existing document owner rather than creating a second API specification.
