---
name: tech-writing
description: Create or revise developer-facing technical documents when the technical substance is already established or can be verified from supplied or repository evidence. Use for READMEs, guides, reference or explanation pages, settled design documents, ADRs, context or glossary documents, and editing an existing review or research report. Unresolved software design, substantive fact-finding, and performing the review itself remain separate engineering tasks.
---

# Technical Writing

Turn established technical content into a document a developer can skim, trust, and maintain. Communicate in the user's language unless the target repository or requested artifact has an explicit language convention. Preserve the project's own terminology, symbols, paths, commands, and document roles.

## Resolve the document authority first

Do not impose a house template on a repository that already has one. Use this precedence:

1. the user's explicit format or file boundary;
2. the repository's existing template, contribution guide, neighboring maintained documents, or generator;
3. the closest artifact-specific convention in this Skill.

Read the current target before editing it. When creating a new document, inspect the maintained documents that serve the same reader or lifecycle. Reuse established metadata, naming, section order, status vocabulary, and link style when they are meaningful and not misleading.

Choose the reference by the artifact, not by filename alone:

| Artifact or question | Read |
|---|---|
| General style, README, guide, tutorial, reference, explanation, or documentation edit | [Writing and document structure](references/style.md) |
| A settled technical design, proposal, specification, or RFC-shaped document | [Technical design documents](references/design-doc.md) |
| An architecture decision record | [Architecture decision records](references/adr.md) |
| `CONTEXT.md`, glossary, project context, or another maintained context artifact | [Context and glossary documents](references/context.md) |
| Formatting or editing review findings that already exist | [Review reports](references/review-report.md) |

Several references can apply, but they are not a required sequence.

## Keep claims grounded

Documentation about a system is a claim about that system. Verify material current-state claims against the closest available authority: source and configuration for implemented behavior, accepted decisions for durable rationale, current specifications or designs for intended behavior, and actual command output for runnable examples when proportionate.

Use exact project names instead of inventing synonyms. Mark examples as fragments when they are not runnable as shown. Do not manufacture version numbers, status, ownership, approval, test results, performance numbers, or evidence to make a document look complete. If a material claim cannot be checked, state the evidence limit rather than smoothing it into confident prose.

Keep historical and current truth separate. Do not rewrite an accepted ADR so it appears always to have contained a later decision. Do not turn an obsolete implementation detail into current context merely because an old document mentions it.

## Preserve task ownership

This Skill owns document creation and editing, not every engineering judgment that may appear in a document. If the requested document requires unresolved software behavior, architecture, contracts, or trade-offs to be decided, those decisions belong to the software-design work. If it requires new external or experimental evidence, the research question must be resolved. If it requires finding defects, the review work owns the findings.

When the necessary substance is already present in the request, repository, accepted design, review findings, or research evidence, write the document directly. Do not force the user through another design, review, or research ceremony merely because the output is Markdown.

## Deliver the maintained artifact

Write for the document's actual reader and purpose. Keep sections that carry information; remove empty ceremonial headings. Prefer links to maintained owners over copying changing facts into several documents. Do not create a document set when one requested or existing artifact is sufficient.

Before handing the document back, reread it as a cold reader. Check that terminology is consistent, important claims are supported, status and scope are not overstated, links or exact strings are usable, and the document answers the reader's likely question without requiring the author conversation.
