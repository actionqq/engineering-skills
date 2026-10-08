# Context and Glossary Documents

Do not infer a document's role from the filename `CONTEXT.md`. Repositories use that name for different things. Inspect existing content, references, instructions, and neighboring documents before editing or creating it.

## If the artifact is a domain glossary

Use a compact domain-language shape when the document's job is to keep canonical concepts stable:

```markdown
# <Context or domain name>

<One or two sentences describing the scope of this language.>

## Language

**<Canonical term>**
<One or two sentences defining the concept.>
_Avoid_: <ambiguous or deprecated aliases, when useful>
```

Include only terms whose meaning is specific to the product or bounded domain. General programming vocabulary does not belong merely because the code uses it. Define what the concept is, its important boundary, and meaningful excluded meanings; do not turn the glossary into an implementation reference.

When several bounded contexts use different meanings, keep the distinction explicit and document translations or relationships rather than forcing one global vocabulary. A map/index is useful only when several independently maintained glossaries actually exist.

## If the artifact is project context

Some repositories use a context document as a concise current-truth map for humans or coding agents. When that is the established role, include only the sections the project needs, commonly:

- purpose and scope;
- core domain entities or concepts;
- modules or packages and their responsibilities;
- important user, control, or data flows;
- external systems, stores, and integrations;
- high-level architecture and ownership boundaries;
- project-specific conventions that are consistently evidenced and useful to future work.

Use real paths, symbols, and flows. Keep the map navigational rather than copying full API references, design documents, or README instructions. Link to those maintained owners for detail.

## Keep current truth separate from decisions and history

A context document explains the system and vocabulary that currently govern work. An ADR owns durable decision rationale. A design owns intended behavior and architecture at its scope. A work plan owns temporary execution state. Do not use `CONTEXT.md` as an undifferentiated notebook for all four.

If the current context conflicts with code or an accepted decision, establish which source is authoritative before rewriting either. Code is evidence of what is implemented, not automatic proof of intended business meaning. Mark unresolved contradictions instead of inventing a reconciliation.

## Preserve the repository's role and name

Do not rename `CONTEXT.md` to `GLOSSARY.md`, or the reverse, merely because another ecosystem prefers that convention. Do not repurpose an existing context file from broad project orientation into a dictionary, or from a dictionary into an architecture manual, without explicit authorization.

Create a new context or glossary artifact only when it has material information and a downstream reader. If an existing README, design, or domain document already owns the information clearly, improve or link that owner instead of creating another source of truth.
