# Trace Causes and Test Explanations

Use when the symptom appears far from the faulty decision, crosses several components, or survives repeated patches.

## Trace the origin, not only the crash site

Start with the concrete invalid value, state, ordering, or resource failure at the symptom. Follow its producer and callers backward: who supplied it, where was it transformed, which assumption first stopped being true, and what original event selected that path?

Example: a filesystem operation runs in the source directory because it receives an empty working-directory value. Catching the final filesystem exception may hide the problem. Trace how the empty value arose—perhaps test setup was read before initialization—and fix the invalid selection or lifecycle assumption. Add a boundary check where it protects an independently exposed operation, rather than repeating the same validation at every helper.

Across components, inspect both sides of meaningful boundaries: request representation, configuration actually received, identity, state before/after, transaction outcome, and error propagation. Check whether a value exists and is correct without dumping secrets. Instrument before the decisive operation when post-failure state is ambiguous.

## Use a working comparison

Compare the failing case with a genuinely comparable working case: revision, input, environment, call order, dependency version, ownership, and timing. A reference pattern must be understood in its relevant context; superficial copying can preserve the hidden difference that caused failure.

For each candidate cause, write a short prediction: if it is true, what new observation should appear or what controlled change should alter the failure? Also identify an observation that would refute it. Prioritize probes by information gained and cost, not by how easy a patch is to write.

Test one causal distinction at a time where feasible. Record the actual observation before moving to the next hypothesis. Discard or revise contradicted explanations. If multiple changes are necessary to create the test environment, separate them from the variable being investigated.

## Break unproductive loops

When attempted fixes add no information, check whether the feedback tests the right symptom, the compared environments are equivalent, the failure is a baseline issue, or hidden shared state invalidates the experiment. Architecture may be involved, but a fixed number of failed patches is not evidence of that conclusion.

Distinguish mitigation from repair. A restart, longer timeout, retry, or fallback may reduce harm without explaining the cause. Verify its consequences, including duplicate side effects and resource accumulation, and preserve the remaining investigation rather than declaring root cause solved.

## Close the causal chain

The explanation should connect trigger, violated assumption, propagated state, and observed outcome. The repair should change that chain, and the regression check should fail when the relevant error is reintroduced. Rerun the original scenario after a minimized check succeeds. Remove temporary probes you added, and retain the useful reproduction and unresolved limits.
