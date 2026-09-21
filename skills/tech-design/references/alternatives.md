# Compare Consequential Designs

Use this when a responsibility or interface is costly to reverse and several credible shapes exist. Do not manufacture alternatives for obvious local edits.

Prepare a solution-neutral brief: behavior to own, real callers, common and difficult scenarios, current contract burden, relevant constraints, excluded responsibilities, dependencies, and known test-fidelity gaps. Do not embed the favored signature in the brief.

Generate alternatives that optimize genuinely different concerns, for example:

- reduce the common caller's construction and ordering obligations;
- keep changing policy and invariants under one coherent owner;
- expose partial failure and cancellation without leaking orchestration;
- preserve existing callers during a bounded migration;
- give different actors narrow role-specific capabilities.

Two meaningful options can be enough. More flags or different class names are not different designs. Separate contexts can reduce anchoring when available and permitted; sequential comparison is still useful, but do not call it independent.

Exercise every option with the same scenarios. For each, sketch its complete contract, common and failure usage, hidden decisions, effects, dependency substitutions and fidelity gaps, verification, migration, and strongest objection.

| Compare | Ask |
|---|---|
| Caller burden | What must callers know, construct, sequence, and recover from? |
| Cohesion and locality | Where will the next policy or provider change land? |
| Failure honesty | Are retries, partial success, cancellation, and costs represented accurately? |
| Verification | What can the chosen test surface observe, and what remains unproved? |
| Compatibility | Which consumers break and which temporary bridges must be maintained? |
| Enforcement | Can packages, exports, or boundary tests prevent bypasses? |
| Evolution | Does this serve named variation without speculative extension knobs? |

Do not compare one option's easiest call against another's hardest failure. Reject an option that “simplifies” the interface by hiding necessary obligations or forcing unrelated behavior into a generic manager.

Recommend one option with decisive evidence and the trade-off accepted. Name when the runner-up would become preferable. Combine elements only if their responsibilities remain compatible; taking every appealing feature can erase the advantage of each design. If evidence cannot resolve a material choice, identify the smallest useful experiment or the actual user decision needed.
