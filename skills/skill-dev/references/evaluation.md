# Evaluate Behavior and Comparative Value

Use for a requested evaluation design, or a justified behavior check with an available execution mechanism and authorization. This is optional support for Skill development, not a prerequisite for creating or modifying files.

## Confirm execution before preparing cases

Identify the question and a real way to run the candidate instructions on raw inputs: a supported fresh session, an authorized agent, or a suitable local runner. Keep the setup native to the current or intended harness; do not require Claude Code or install another host merely to satisfy this procedure. A schema validator or fixture exporter does not execute a Skill.

If no suitable mechanism is available, skip the behavior evaluation and its setup artifacts. Continue the requested authoring and feasible checks, without producing a substitute benchmark or pending-case report. Only prepare a standalone evaluation plan or cases when the user explicitly requests them. An explicitly requested run that cannot execute should be reported as unavailable, not silently replaced by planning.

## Start from real failures when available

Recent real sessions, review corrections, failed tasks, support examples, and production-shaped cases can reveal Skill gaps that synthetic cases miss. Treat them as evidence inputs, not automatic instructions to edit the Skill.

Before proposing a Skill change, attribute the failure to the owning surface. Ask whether a competent agent following the current Skill already had the instruction needed to succeed. If the answer is yes, distinguish model variance, missing context, trigger/discovery failure, harness or tool failure, product behavior, and repository enforcement from an instruction gap. Do not append more prose when another layer owns the failure.

Cluster repeated failures by root cause and verify them against the current Skill and repository before generalizing. A no-change conclusion is valid when the evidence does not establish a reusable instruction gap.

## Construct discriminating tasks

Cover every substantive mode with realistic requests and raw materials. Include difficult valid cases, harmless lookalikes, missing inputs, unavailable tools, and scope constraints. Expected behavior should concern meaningful outcomes, not matching headings or repeating the Skill's wording.

Think of an executable evaluation as three separable parts: inputs, the runner or environment, and the grader. Check each part before blaming the candidate Skill. Ground-truth labels need a traceable source. Avoid leaking expected answers through filenames, setup text, grader wording, or examples the executor can see. Old cases can become stale as the repository or harness changes.

Keep grading expectations and seeded-defect answers out of the execution packet. An executor receives the task, raw materials, legitimate setup, and whichever Skill condition is being tested. If setup reveals the answer, the case cannot test discovery of that answer.

Check the artifacts and actions as well as the final reply. A test-plan request fails if it edits product code; a review may be wrong despite a polished report; a declared test pass needs execution evidence. An assertion should reject a plausible bad output, not just confirm that a file exists.

Treat runner crashes, unavailable tools, timeouts, and malformed fixtures as harness or environment failures unless evidence shows the model caused them. Distinguish a model that explicitly concludes "no issue" from a run that never produced an answer; they are different outcomes.

## Compare like with like

Choose the comparison for the question. When changing an existing Skill, use its recoverable prior version to check the intended change and relevant regressions. For a new Skill's incremental value, use the harness's normal behavior without the candidate. Include upstream methods only when that comparison is needed. Keep the task, starting files, model/settings, tools, permissions, and environment equivalent; never weaken the native baseline. An unsupported setup is not evidence that a method lost.

Each execution uses fresh supported context and an isolated working copy. Do not give one condition the other condition's outputs. Parallel runs are optional and subject to actual authorization; they are not a prerequisite for rigorous sequential comparison.

Record actual model and harness identity, Skill and input fingerprints, outcome artifacts, trace location, environment, and available time/usage. Preserve null or unknown metrics rather than fabricating them.

## Judge substance

Grade each requirement with supporting artifact or transcript evidence. Include incorrect extra claims and unauthorized side effects that the initial rubric missed. Distinguish passed, failed, environment-blocked, and not-run; missing evidence cannot silently become a pass.

For a blinded comparison, hide condition labels and source identity from the evaluator, compare outputs against the same task, and inspect significant correctness before cosmetic quality. Ties are legitimate. Do not force a winner or let a high presentation score outweigh a functional failure.

Critique the tests too. Cases both conditions trivially pass show little incremental benefit. A check satisfied by an empty or wrong artifact is weak. High variance may indicate a flaky environment, ambiguous rubric, unstable instruction, or an evaluation with too little headroom above its noise floor.

## Revise without overfitting

Read transcripts to detect unnecessary searches, repeated questions, pointless artifacts, and hidden dependencies. Improve the responsible instruction or resource rather than accumulating bans for every observed instance. Use repeated critical cases and holdout tasks not used for editing. Improvement on the cases used to tune the Skill is not enough; check whether the change survives fresh holdout cases.

When hill-climbing a Skill or evaluator, change one material variable at a time where feasible so the effect can be attributed. If a case generator or grader has a systematic defect, fix that mechanism rather than hand-editing every symptom. Report cost and quality together where measurable.

If execution becomes unavailable, stop that evaluation and report the actual limitation; do not manufacture a substitute author exercise to count it complete. Structural checks and direct script tests remain useful on their own, but do not establish model behavior. Cross-harness acceptance requires actual execution in each claimed environment.

Conclude with what has been demonstrated, what failed, what changed, and which combinations remain untested. A source-faithful rewrite is a reason to test, not proof of equal effectiveness.
