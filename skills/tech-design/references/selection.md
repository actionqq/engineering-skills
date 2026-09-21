# Evaluate Technology and Reuse Choices

Select on fitness and total ownership, not popularity or a universal preference for adoption. Building is a legitimate baseline, as are reusing current behavior and doing nothing.

## Choose the depth

- **Local preflight:** inspect existing project, standard-library, framework, and platform capabilities before introducing material generic machinery.
- **Prescribed choice:** verify the named technology's relevant version, compatibility, maintenance, and project constraints; do not reopen the entire market unless a hard constraint fails.
- **Open consequential choice:** compare credible candidates and a genuine bespoke baseline.

Small transparent helpers and routine use of an existing dependency usually do not require a full study. Unclear required behavior should be resolved before comparing products.

## Evaluate the whole adopted system

State the job in product terms, hard constraints, preferences, non-goals, expected lifetime/scale, decision timing, and reversibility. Do not let one candidate's vocabulary redefine the problem.

Apply hard gates before qualitative trade-offs. Mark each relevant gate as supported, failed, unknown, or supported with a specified mitigation. Unknown compatibility or required deployment support is not an implicit pass.

Compare only meaningful dimensions: functional and architectural fit; maintenance and support; security and data handling; license and governance constraints; recovery and observability; representative performance; testability; integration effort; time to value; team capacity; migration and exit.

Count the wrappers, adapters, transitive dependencies, operator procedures, hosted control planes, migration bridges, and remaining custom code on the adoption side. Count documentation, compatibility, operational support, and long-term maintenance on the bespoke side. An attractive steady-state design may lose because its delivery delay is unacceptable.

## Attach evidence to claims

For important external facts, identify exact version or tier, date, source, finding, applicability, and uncertainty. Use official documentation, release/support information, exact license text, source, or a relevant experiment. Popularity and aggregate health scores can identify candidates but cannot establish fitness.

Where security, privacy, licensing, or procurement constraints actually determine adoption, investigate them proportionately and respect the project's responsible decision process. Do not invent a compliance program for ordinary local reuse.

Offline research can support identified local facts; label current external status unverified. A proof-of-fit should target a decision-changing uncertainty with a workload and success boundary. Research alone does not authorize executing untrusted packages, accepting terms, or sending project data to an external service.

## Decide

Classify the outcome as adopt, adapt, combine, build, defer, or keep the current state. Explain the strongest reason against your recommendation, why alternatives lost, the remaining uncertainty, and what would change the decision. Prefer a reversible option when evidence otherwise ties.

For adoption, specify the useful dependency boundary, version/support assumptions, operational owner where known, and exit path. For building, bound the responsibility and maintenance obligations now owned. Preserve actual decision status and existing authorization; do not claim someone accepted a proposal merely because the agent recommended it.

Capture a single authoritative decision with supporting evidence. Reconsider when requirements, supported versions, costs, operational experience, or available platform capabilities materially change.
