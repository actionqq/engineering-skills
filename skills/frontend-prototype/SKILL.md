---
name: frontend-prototype
description: Build a quick, low-cost frontend prototype to answer a concrete question about layout, user flow, interaction, or visual direction. Use for lightweight interactive mockups and comparing UI options. Implement only what affects the decision; production feature delivery, backend experiments, and architecture design are separate tasks.
---

# Frontend Prototype

Help the user judge a design with the least implementation needed. Communicate in the user's language. The deliverable is a lightweight, runnable demonstration and useful observations, not a head start on production architecture.

## Identify the question

Establish what the user needs to judge: for example, whether a drawer preserves enough context, a form's grouping is understandable, or a page layout communicates the main action. A clear conversational brief is enough; do not require a specification or an interview for ordinary reversible choices.

Read only the project context that affects this question. Preserve settled business rules. If an unresolved product decision changes the answer, identify it and proceed with independent parts rather than silently deciding it through the demo.

Name the interaction or visual detail that must be represented and what can remain simulated or omitted. One direction is the default. Build alternatives only when comparing them is the actual question, using the same task and sample content.

## Choose the cheapest useful form

For a standalone prototype, prefer HTML, CSS, and a little JavaScript, in one file or a few simple files that are easy to open and change. Do not scaffold an application merely to display a prototype.

In an existing product, reuse its stack and components only when that is clearly cheaper or the surrounding interface is necessary to judge the result. Use an isolated demo entry or explicit prototype switch; do not alter production behavior. A framework is an option when it reduces the work, not a default architectural commitment.

Keep sample data local and state in memory. Simulate service responses and saving. Do not introduce a backend, database, authentication system, shared state library, or reusable architecture for possible future production use.

## Build only what changes the answer

| Question in scope | Read |
|---|---|
| Layout, content hierarchy, or visual direction | [Layout and visual sketches](references/design-foundation.md) |
| Flow, controls, or a particular UI state | [Interaction sketches](references/interaction.md) |
| Inspecting and handing over the result | [Prototype walkthrough](references/verification.md) |

Use working controls for the interaction being judged. Static content and placeholders are sufficient elsewhere. Make simulated effects clear; a demo success message is not evidence of a real operation.

Include additional states, responsive layouts, or visual detail only when omitting them could change the decision. Do not build a complete state matrix, design system, or polished application. Future reuse is not a reason to add abstractions now.

## Walk through and deliver

Open the prototype, try the target interaction, and fix defects that prevent judging it. Do not write automated tests or add test frameworks, coverage targets, CI, performance work, or a production acceptance checklist.

Stop when the user can judge the question. Deliver the artifact, how to open it, what to try, and the important simulated or unexamined parts. Separate what was observed from what still needs user feedback; a runnable demo does not establish that users prefer the design.

Keep the explanation brief. Update an existing decision artifact only when that is in scope. Production implementation is separate work and need not inherit the prototype's code structure.
