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

If several attempted fixes all depend on the same premise and fail the same gate, promote that premise to an explicit hypothesis before writing another fix. State the shared assumption and measure or probe it directly. In a distribution or concurrency problem this may mean measuring ownership or skew by actor; elsewhere it may be a configuration value, lifecycle state, dependency behavior, or workload property. Repeated failure is a reason to test the premise, not proof that it is false.

Distinguish mitigation from repair. A restart, longer timeout, retry, or fallback may reduce harm without explaining the cause. Verify its consequences, including duplicate side effects and resource accumulation, and preserve the remaining investigation rather than declaring root cause solved.

## Look for other instances when the cause may recur

Use this after establishing a defect when the user asks for similar instances or evidence of copied logic or shared API misuse makes a bounded search worthwhile. State the violated contract and the conditions that expose it. Match the search scope to the likely propagation mechanism within the authorized area: copied logic suggests sibling implementations; misuse of a shared API suggests its callers, which may cross module boundaries. One defect does not require a whole-repository audit.

Calibrate a search against the known instance before broadening it. If the instance has already been fixed, use a preserved faulty revision or a faithful example to check the search. A miss can mean an incorrect query, scope, or representation; resolve it rather than treating zero hits as absence of the defect. Generalize one meaningful dimension at a time, such as identifiers, operation shape, or a related API. Inspect newly found candidates before widening again. Use text search when sufficient and syntax or data-flow analysis when the causal relationship needs it; tool installation is not a prerequisite.

For each candidate, trace the relevant inputs and callers and look for protections that defeat the suspected failure: validation, type constraints, locking, transaction boundaries, or an unreachable state. For example, two read-then-write sequences do not share a race if one is protected by a transaction that enforces the required invariant. Similar text is a lead, not confirmation. Keep a latent concern without a reachable scenario distinct from a demonstrated defect.

When broadening produces mostly unrelated matches, refine the causal condition or try another justified direction. Stop when the relevant directions are checked or evidence no longer supports useful expansion. Report confirmed instances, material exclusions, and the actual search limits; no further confirmed instances is a valid result. Search findings do not expand an authorized fix's scope automatically.

## Close the causal chain

The explanation should connect trigger, violated assumption, propagated state, and observed outcome. The repair should change that chain, and the regression check should fail when the relevant error is reintroduced. After a minimized check succeeds, rerun the original scenario when its conditions are available within scope. Report minimized-check evidence at its actual scope. Remove temporary probes you added, and retain the useful reproduction and unresolved limits.
