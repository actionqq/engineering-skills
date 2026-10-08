# Review Reports

This reference formats findings that a review has already established. It does not perform the review, invent additional defects, or turn missing evidence into a finding.

## Preserve the review's real axes

Follow the repository's review format when one exists. Keep materially different review dimensions separate when their distinction helps the reader: for example, specification conformance and project standards can both matter without being combined into one score.

Do not force every review into a universal issue/impact/recommendation template. The report structure should reflect the target and the review method. A design-readiness review, code-change review, frontend review, and security compliance review may need different grouping.

## Always expose scope and evidence limits

A material report should let a cold reader identify:

- the target and exact snapshot, revision, or file scope reviewed;
- the requirements, standards, or other authorities used;
- validation actually performed;
- applicable areas that were **Verified**, **Not verified**, or **Not applicable**;
- the resulting findings and readiness conclusion, if one is warranted.

`Not verified` is not a softer word for pass. Name the missing or unusable evidence. `Not applicable` means the check genuinely does not apply. If the review only covered part of an applicable check, keep the limitation visible in the conclusion.

## Make each finding self-contained

A useful finding carries enough information for the author to reproduce the concern and decide what to change:

- **Location or target:** current file/line, component, UI state, design section, contract, or other precise referent.
- **Trigger or scenario:** the condition under which the problem matters.
- **Evidence or violated requirement:** what establishes the conflict.
- **Impact:** the incorrect behavior, risk, maintenance cost, or decision consequence.
- **Correction direction:** the constraint the repair must satisfy, without prewriting a large unrelated redesign.

These are information requirements, not mandatory subheadings. Prefer one compact paragraph when five labels would make the report harder to read.

Rank findings by consequence and conditions. Deduplicate several symptoms of one cause. Separate confirmed defects, required-standard deviations, unresolved questions, and optional improvements when mixing them would imply the wrong severity.

## Write useful clean reports too

When no reportable finding survives review, say so directly. Still state the reviewed scope, validation that actually ran, and material evidence limits. “No findings in the checks performed” is stronger and more accurate than claiming the whole target is correct when some applicable behavior was not verified.

For independent or multi-review work, synthesize evidence rather than counting votes. Agreement increases attention, not truth; a lone well-supported finding can matter more than several duplicated weak observations. State independence limits when reviewers shared author context or did not use isolated snapshots.

## Keep prose concrete

Avoid generic review filler such as “this may cause issues” or “consider improving robustness.” Name the actual state transition, caller, request, persisted value, user effect, violated rule, or missing evidence. Use the project vocabulary and current locations. A reader should know why the issue matters without reconstructing the review conversation.
