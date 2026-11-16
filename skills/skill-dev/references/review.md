# Method Quality and Existing Evidence

Use for a Skill quality review, a substantive method revision, or investigation of reported Skill failures. Review the work the instructions would guide, including behavior-bearing references and tools. Metadata and file organization are supporting checks.

## Establish what successful work requires

Identify the intended tasks, necessary inputs, important constraints, and useful outcomes from the request, the target Skill, and available domain evidence. Distinguish the Skill's promises from the actual user's need. Define success in terms of a correct, usable result; completing the Skill's own checklist is insufficient if the task remains unsolved.

Read existing upstream sources when assessing an inherited method or resolving a material method gap. Compare the relevant decision rules and supporting resources, not just titles or entrypoint length. Verify consequential technical claims against the owning code, specification, or primary source when needed. An upstream instruction is evidence of a method, not proof that the method is sound in every context.

## Walk through the method

For the substantive modes in scope, use representative tasks to follow the path from available input to decisions, actions, failure handling, and completion. Include a meaningful variation or adverse case where it could change the conclusion. These walkthroughs are reasoning about instructions, not model executions or a requirement to create a test suite.

At consequential steps, check:

- **Decision quality:** Are the premises correct, and do the criteria distinguish plausible alternatives? Identify cases where following the rule would select a wrong action.
- **Sufficiency:** Can the executor reach the outcome with the available information and resources? Locate missing domain steps, unsupported assumptions, and recovery gaps. Leave ordinary judgment to the model where several approaches are valid.
- **Completion:** Does the stopping condition establish the required result, or allow premature success after an intermediate action? Required downstream work must remain visible.
- **Usefulness and cost:** What does the guidance add through domain knowledge, useful reminders, tools, or decision support? Check for unnecessary investigation, artifacts, repeated work, or rigid procedures that obstruct valid solutions. Do not infer what a model reliably knows, or delete useful reminders, from intuition alone.

Choose checks by the kind of capability:

| Capability | Inspect through the task |
|---|---|
| Technique or procedure | Whether its steps work on a realistic variation, preserve prerequisites, and recover from relevant failure |
| Judgment or mental model | Whether its criteria distinguish choices, explain trade-offs, and identify when the approach should not apply |
| Reference or tool use | Whether the needed information can be found, is accurate, and can be applied with the actual inputs and dependencies |
| Discipline or constraint | Whether the rule serves the task, has observable conditions, and remains usable under competing demands; actual compliance needs execution evidence |
| Artifact production | Whether the resulting content can be correct, complete, and usable for its reader, beyond having the requested filename or headings |

For example, a review method that treats a successful build of local callers as proof that a field rename is safe misses independently deployed consumers of the serialized field. Trace an old consumer reading a new payload to explain the gap; recommend checking the wire contract and supported consumers. This is a content finding even when the Skill's metadata and links are valid. If its references already cover that boundary, investigate whether the loading condition exposes them before proposing another rule.

## Use existing execution evidence

Use relevant supplied or otherwise authorized conversations, corrections, outputs, and command results when available. Inspect the actual artifact where possible instead of relying on the agent's success summary. Identify the request, consequential action or omission, and effect on the result or user effort. Existing evidence can be analyzed without launching an experiment or scanning unrelated conversation history.

Check which Skill revision and resources the executor actually had when that affects attribution. Compare historical failures with the current instructions; an old failure may already be addressed. Missing load evidence leaves uncertainty about discovery or instruction following.

Trace a proposed correction to its owner:

- If following the current guidance can still produce the failure, identify the missing, incorrect, or underspecified decision or step.
- If useful guidance exists but its trigger or loading condition misses the task, repair that condition.
- If the executor had clear applicable guidance and ignored it, distinguish noncompliance or model variance from an instruction gap; another reminder is not an established remedy.
- If missing context, tools, product behavior, repository enforcement, or the grader explains the failure, address or report that owner rather than expanding the Skill.

Group repeated observations by cause. Before proposing an instruction edit, explain how it would change the consequential choice while preserving valid neighboring cases. Prefer replacing the responsible guidance over appending prohibitions for individual incidents. A single decisive counterexample can expose an incorrect rule; recurrence or controlled runs provide different evidence about frequency and causation.

## Conclude at the strength of the evidence

Lead with method or outcome problems and their consequences when found, followed by relevant discovery, packaging, and tooling findings. For each material issue, give the location, task or observed failure, evidence, and smallest useful correction. Distinguish a demonstrated logical gap, an observed execution failure with uncertain attribution, and a behavior hypothesis needing a fresh run.

When no substantive issue is found, state which task paths and methods were examined and what remains uncertain. Do not manufacture findings or require a numerical score. Structural validity alone cannot establish that the method is adequate; a content walkthrough alone cannot establish model reliability or comparative improvement.

Use [Behavior evaluation](evaluation.md) when the remaining question requires new execution evidence, such as whether a revised loading condition is selected reliably or a method change improves outcomes. Missing execution capability limits those conclusions; it does not prevent reviewing the method or analyzing evidence already available.
