# Engineering Experiments

Use when feasibility depends on real protocols, versions, data, timing, resources, or migration behavior.

## Write an experiment brief

Specify the question, hypothesis, competing explanation, observation, decision threshold, relevant environment, representative input, and bounded resources. State which variables are controlled and which differences remain. The brief can be a short note near the experiment; it need not become a formal report.

Keep the decisive boundary real. A mock is useful for preparing a client but cannot prove the remote protocol. A memory store can test application policy but not a target database's constraints, transaction isolation, or crash durability.

## Compatibility

Pin the runtime/dependency versions and relevant configuration. Exercise the actual protocol or supported API, including important error behavior and serialization. For rolling upgrades, test old reader/new writer, new reader/old writer, retained data or queued messages, and supported fallback behavior as applicable. Record a missing combination rather than claiming universal compatibility.

## Performance

Record the baseline, data scale and distribution, request mix, concurrency, hardware/runtime, warm-up, cache state, repeated runs, and measurement method. Distinguish throughput, latency distribution, resource cost, and failure rate. Prevent the generator, logging, or unrelated environment contention from becoming the hidden bottleneck.

Before acting on a performance number, prove that the measured work actually happened inside the timed region and produced correct output. Count failures, retries, rejected work, and incomplete output when they can change the apparent speed. A fast no-op, timeout, cached shortcut, or overloaded load generator is not evidence that the target path improved.

Run compared sides under production-relevant and equivalent settings. When environment drift, warm-up, or cache state can bias the result, interleave A/B runs rather than measuring one side in a block and the other later. Report enough repetitions and variability to show whether the claimed gap is larger than run-to-run noise.

Name the limiting resource when the result will drive a design or adoption decision. Check basic physical or algorithmic bounds against the claim: CPU time, cores, storage/network bandwidth, request work, and the measured component's share of end-to-end latency. An implausible result is a reason to inspect the harness before celebrating it.

Compare under equivalent conditions. Show variability where it matters. A faster median with worse tail latency or error rate may fail the actual requirement. A microbenchmark can identify a local cost but cannot by itself prove system capacity. If a side cannot be tuned or its limiter cannot be established, narrow the conclusion or call the comparison inconclusive rather than declaring a winner from a misleading run.

## Migration and recovery

Use disposable representative data and state what production characteristics it omits. Test conversion correctness, restartability, duplicate execution, partial failure, old/new coexistence, and the actual recovery path. Validate counts and content where applicable, not only a successful process exit.

Distinguish reverting application code from restoring changed data. A rehearsal that can only roll forward should say so. Preserve required evidence before cleaning up experimental outputs.

## Environment and interpretation

Check authorization before real side effects or executing unfamiliar artifacts. Use actual isolation appropriate to the risk; do not describe a temporary directory as a sandbox. Do not install broad tooling merely to complete a low-value probe when a narrower check can answer the question.

If the target resource is unavailable, prepare what can be prepared and name the untested claim. Do not substitute an easier experiment and carry over the original conclusion. Report evidence that supports, refutes, or leaves the hypothesis unresolved. Failed experiments can be useful outcomes.
