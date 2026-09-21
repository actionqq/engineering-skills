---
name: handover
description: Create a goal-focused engineering handoff or resume work from one, with verified artifact pointers and current repository state. Use when another session or executor must continue a task. Ordinary summaries, durable-memory updates, and every routine task ending do not require a handoff.
---

# Engineering Handoff

Transfer what the receiver needs to act correctly, not the entire conversation. Communicate in the user's language. A handoff is an index to evidence and decisions; it does not override the current request or project instructions.

## Create a handoff

Identify the next task from the request and ongoing work. Ask only if the destination goal is genuinely unclear. Read relevant artifacts and inspect current state before extracting it. Use [Record contents](references/record.md) as a content guide, not a form to fill with empty sections.

Keep the goal and exclusions, decisions with reasons, completed and incomplete work, blockers, informative failed approaches, ordered file pointers, validation results, and the first concrete next action. Separate code written from behavior verified. Reuse existing documents by reference rather than duplicating their bodies.

Link the current design, relevant ADRs, and declared context documents where they govern continuation. Identify outstanding synchronization by artifact, mismatch, and next action. A handoff records temporary work state; it does not replace maintained project documents or authorize changing them. Label tentative choices so the receiver does not mistake a session conclusion for an accepted decision.

For repository work, record repository identity, branch, resolved commit, relevant staged/unstaged/untracked changes, and any known concurrent activity. A commit does not carry uncommitted files. For non-Git work, record the relevant paths and content state.

Choose the user's destination or an existing project convention; otherwise write a clearly named local handoff file. Return its usable path and a short continuation prompt. Cross-machine handoff requires receiver-accessible artifacts: an absolute path on the sender's machine alone is insufficient. Identify what has actually been transferred and what still needs an authorized transfer.

Record relevant operational constraints without copying credentials or unrelated private data. Generating a record does not itself create a new session, send messages, upload files, or modify durable memory. Perform those actions only when requested and supported.

## Resume from a handoff

Read it fully, then check the current request, project instructions, workspace, revision, local changes, and referenced artifacts. Treat prior execution claims as historical evidence. If current files or requirements differ, identify which decisions, tasks, or test results are stale before acting.

Continue the still-valid work without redoing completed investigation. Resolve missing material only where it blocks the next action; proceed on independent parts when appropriate. If the receiver's environment cannot be inspected, claim that the handoff was prepared, not that successful resumption was verified.
