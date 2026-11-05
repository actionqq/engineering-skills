# v0.2 promotion status — 2026-10-08

This record covers the promotion candidate on `experiment/pstack-upstream-sync`. It supplements the historical maintenance log in `status.md`.

## Scope promoted in this candidate

- add `tech-writing` as the eleventh entrypoint and `technical-writing` as the seventeenth capability;
- add artifact-specific writing methods for general developer docs, settled technical designs, ADRs, context/glossary documents, and existing review reports;
- keep `tech-design` and `tech-review` responsible for writing their own deliverables without a runtime dependency on `tech-writing`;
- integrate pstack blast-radius proof into code review;
- integrate pstack benchmark-validity checks into research experiments;
- promote the exact pstack source records into the canonical source set;
- add canonical method-map, behavior-case, and discovery-routing fragments for the promoted work.

## Canonical bookkeeping

`tooling/validate.py --full` reads the historical base files plus dated canonical fragments:

- `provenance/sources.lock.json` + `provenance/sources.lock.*.json`;
- `provenance/method-map.json` + `provenance/method-map.*.json`;
- `evals/cases.json` + `evals/cases.*.json`;
- `evals/discovery.json` + `evals/discovery.*.json`.

For this candidate the merged totals are:

- 11 Skill entrypoints;
- 17 capabilities;
- 42 reachable local references;
- 106 pinned source files;
- 36 method groups;
- 59 prepared behavior cases;
- 83 prepared discovery requests;
- 8 prepared host-name scenarios.

## Validation state

Prepared in source:

- JSON syntax for the new canonical fragments;
- exact pstack content SHA-256 values at `cursor/plugins@ccb5507cec1546dc88135c1139c811e6c59115ba`;
- targeted behavior cases for technical writing, benchmark validity, and cross-boundary review;
- targeted routing cases separating `tech-writing` from `tech-design`, `tech-review`, and `research`;
- a validator regression proving that dated case fragments are included by full validation.

GitHub Actions run `37755130213` validated candidate commit `c02b06b3f52623e6de0867448dee83fc008ddb4b` successfully on 2026-10-08. The workflow completed all three repository checks successfully:

1. `python tooling/validate.py`;
2. `python tooling/validate.py --full`;
3. `python -B -m unittest discover -s tooling -p 'test_*.py' -v`.

This establishes source-level structural consistency, local resource closure, evaluation/provenance bookkeeping consistency, and maintenance-tool regression status for that candidate snapshot. It does not turn prepared model cases into executed model evidence.

## Still not established by structural validation

Even with all repository checks passing, the following remain deliberately unclaimed:

- independent model behavior quality for `tech-writing`;
- natural-language routing quality in each target host;
- cross-host installation and invocation acceptance;
- measured improvement over the pre-promotion baseline;
- independent behavior baselines for `frontend-prototype` and the newer frontend lenses.

These are not blockers for keeping the authored source internally consistent, but they are required before claiming model effectiveness or cross-host compatibility.
