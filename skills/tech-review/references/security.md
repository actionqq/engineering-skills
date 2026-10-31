# Security Review Lens

Load this lens when the changed surface handles authentication, authorization, untrusted input, secrets, tenant boundaries, file or network access, deserialization, cryptography, sensitive data, privileged execution, or security-relevant configuration. It supplements the relevant code or architecture lens; it is not a substitute for a specialist audit.

## Establish the boundary

- Identify assets, trust boundaries, entry points, principals, privileges, and data flows affected by the target.
- Trace input from source to sensitive operation, including indirect callers, background jobs, callbacks, templates, logs, and error paths.
- Determine whether the code relies on caller identity, tenant context, object ownership, configuration, or deployment controls. Verify those assumptions in code and tests rather than accepting comments as evidence.
- Separate reachable attack paths from theoretical concerns; state prerequisites and attacker capability.

## Review high-value failure classes

- **Authorization:** authentication is not authorization; check object-level and tenant-level access on every relevant path, including list, export, async, and retry paths.
- **Input and interpretation:** validate at the trust boundary; inspect injection, path traversal, unsafe deserialization, command construction, SSRF, and parser differentials where relevant.
- **Secrets and sensitive data:** inspect storage, transport, logs, telemetry, error messages, caches, and retention; avoid reproducing secret values in findings.
- **State and concurrency:** check replay, idempotency, race windows, confused-deputy behavior, privilege changes, and time-of-check/time-of-use gaps.
- **Cryptography:** verify use of established primitives and protocols, key lifecycle, nonce/IV handling, algorithm choices, and constant-time requirements where applicable. Do not invent cryptographic designs during review.
- **Operational controls:** inspect default permissions, debug endpoints, exposed admin surfaces, dependency and build provenance, and fail-open behavior.

## Validate claims

Use focused adversarial tests or static analysis when available. For a security fix, test the original exploit condition and meaningful variants; include a benign control to ensure the test harness reaches the changed code. A passing scanner or test suite is evidence for its covered checks only.

For a patch, distinguish:
- the vulnerability is reproduced on the baseline;
- the patched revision blocks the exploit;
- expected non-security behavior remains intact;
- coverage gaps or environment limitations remain.

Do not edit the target during a read-only review. Do not execute destructive payloads or probe systems outside the authorized repository and test environment. Escalate specialist protocol, cloud, cryptographic, or compliance questions when the evidence exceeds this lens.

## Report

Each finding should identify the affected location, reachable preconditions, attack path, impact, evidence, and a proportionate remediation direction. Distinguish confirmed vulnerabilities from hardening suggestions and unresolved questions. Never claim the application is secure because no issue was found in a bounded review.
