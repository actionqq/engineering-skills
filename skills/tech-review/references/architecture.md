# Architecture Audit

Use to determine where architecture work is justified or to assess a named structure. An audit discovers and ranks problems; it does not automatically design exact replacement interfaces or implement a refactor.

## Establish intent and evidence

Fix the requested subsystem or pain point. Read applicable decisions, public entrypoints, callers, tests, dependency/build metadata, and relevant change history. Inspect enough history to distinguish recurring change pressure from a one-off mechanical migration. Exclude generated or vendored churn when it would distort the signal.

Trace representative behavior from entry to outcome. Record who owns policy, state, sequencing, configuration, provider shapes, error recovery, lifecycle, and verification. Identify intentionally thin routes, adapters, and composition. Ask what callers must reconstruct and which files or owners change together.

## Generate bounded candidates

Possible improvements include concentrating repeated policy, removing a forwarding chain, splitting incoherent responsibilities, moving a volatility seam, repairing dependency direction, restoring locality, or making an interface's effects and errors explicit.

A candidate needs evidence of current friction, why it matters now, affected files or modules, the proposed responsibility change, counterevidence, migration risk, and a verification path. Do not infer architectural failure from file size, directory depth, one adapter, or the mere existence of similar code.

To evaluate a thin layer, imagine inlining it while preserving its behavior. Would callers now need duplicated recovery, translation, or policy? If so, the boundary may be earning its place. Similar code in independently evolving contexts may be better left separate.

For physical-layout findings, inspect actual source roots, package declarations, exports, imports, discovery, and enforcement. A directory named for an architectural role can contain code that violates that role even when it compiles.

## Rank before elaborating

Compare current change pressure, caller burden, locality, ownership and runtime honesty, verification quality, migration cost, reversibility, and the strongest objection. Keep recommendation strength separate from confidence in the evidence. Avoid weighted numbers that suggest precision the data does not support.

If no candidate has enough current value, recommend no architecture investment now and identify the signal that would justify revisiting. A credible audit can conclude that an existing structure is appropriate.

Before/after diagrams should reflect observed and proposed responsibility, not conceal uncertainty behind polished graphics. Use visuals when they clarify the result; a standalone HTML report is not mandatory for every audit.

For an authorized selected improvement, proceed to the relevant design or implementation. Otherwise deliver ranked, bounded findings. If claiming reduced complexity, account for the same entire path—including configuration, adapters, state, compatibility, and operations—rather than counting only removed files.
