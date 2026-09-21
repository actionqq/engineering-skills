# Structure, Enforcement, and Migration

Use for source trees, package boundaries, dependency rules, or file migrations. Distinguish an audit, proposal, migration plan, and authorized implementation before moving anything.

## Classify before drawing a tree

Inspect actual entrypoints, behavior owners, manifests, source roots, imports, public exports, framework discovery, generated code, tests, deployment units, and existing conventions. A folder label is a claim; dependency and discovery checks determine whether it is true.

Choose the least structure that expresses the actual project:

| Evidence | Useful starting shape |
|---|---|
| Small cohesive package | Flat or shallow |
| Ordinary application | Feature/use-case ownership |
| Distinct model authority | Context-oriented organization |
| Explicit provider-independent policy | Ports and adapters with enforceable direction |
| Endpoint-heavy edge service | Discoverable route entries with separate shared workflows |
| Framework-required entry paths | Keep them discoverable and thin |
| Operational/CLI work | Named workflows or commands |
| Several build/release owners | Real packages grouped by capability |

Frontend runtime and ownership need [Frontend structure](frontend.md). DDD, ports and adapters, and monorepos are independent choices, not a bundle inferred from one another.

## Make ownership and direction explicit

Every new directory in a proposed tree should own actual files, a real package, or a named responsibility. State where a future folder might belong in prose rather than adding empty symmetry. Separate grouping directories from buildable modules and executable hosts.

For an explicitly chosen ports-and-adapters design, place provider-independent policy and owned port protocols inside, concrete transport/provider implementations outside, and concrete resource construction/lifecycle in the executable host. Application policy may call injected effects while remaining independent of concrete I/O. A library does not need its own composition root merely to match a template.

Ports belong to the policy that consumes the conversation, usually application policy. A provider-shaped API is not improved merely by adding “Port” to its name. Reusable fakes and adapter contract suites are test infrastructure; production imports must not depend on them. Focused colocated tests can use that infrastructure through test-only dependencies.

Protect useful boundaries with proportionate enforcement: explicit public exports for a small package, restricted imports or architecture tests in one app, manifests and dependency checks across packages. Inspect both source edges and declared dependencies; either alone can miss a violation. Validate language package declarations against the actual module source root.

## Prove the proposed depth is discoverable

Before moving packages, inspect workspace globs, build/test/coverage discovery, aliases, project references, release tooling, and container/build contexts. Exercise a fixture at the deepest proposed target path. Check that allowed packages are found and forbidden edges are rejected; current shallow packages cannot prove recursive discovery works.

## Separate semantic and mechanical change

Identify behavior and consumers, establish appropriate protection, prepare discovery and direction checks, then migrate in bounded slices. Keep provider inversion, behavioral decomposition, file moves, and compatibility removal distinguishable. Reparenting a provider-dependent package does not make it provider-independent.

Preserve public names and exports where useful during movement. Remove old paths only after consumers migrate; state which temporary aliases exist and when they can disappear. Verify consumer builds, public imports, route/startup discovery, resource shutdown, and project-required tests. Check production versus test/development edges.

Deliver the selected shape, placement rules, permitted dependency direction, enforcement, migration sequence, and verification. A visually simpler tree or successful compile alone is not proof of architectural compliance or reduced total complexity.

Include affected package indexes, architecture decisions, terminology, diagrams, and onboarding instructions in the migration's completion criteria. Update them during authorized migration and check moved-path links; for a proposal, identify these deliverables without performing the migration or marking the target structure as already current.
