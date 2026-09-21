# Handoff Record Contents

Use this guide to preserve actionable state. Follow a requested project format; omit irrelevant sections instead of filling a universal template.

## Goal and constraints

State the receiver's next goal, what is excluded, the current user's important constraints, and decisions still in force. Give reasons for consequential choices so the receiver need not rediscover them. Distinguish actual decisions from suggestions, assumptions, and abandoned ideas.

## Current state

Separate completed work, work in progress, blockers, and the next action. Include partial states precisely: code written, check not run; unit checks passed, integration unavailable; report prepared, not published.

For Git work identify repository, branch, commit, and the relevant staged/unstaged/untracked state. Explain where uncommitted content can be obtained; a branch name or commit alone does not transfer it. For other work, identify the artifact location and enough content identity to detect stale copies.

Record commands and actual outcomes when they matter to continuation. Historical test results belong to the revision and environment that produced them. A live process or temporary environment needs its current state and ownership if the receiver must use or stop it.

## Evidence and reading order

Point to the authoritative design, task list, code, experiment, or review rather than copying it in full. Say why each pointer matters and suggest a useful reading order. Include failed attempts only when they prevent an otherwise plausible repetition, with what evidence ruled them out.

For decomposed work, identify the current unit's execution brief, completed and remaining scope, prerequisite outputs, affected design sections, and pending integration checks. Preserve existing task boundaries unless changed facts require replanning; do not reproduce every sibling brief or expand the handoff into a second design. The receiver must compare the brief's assumptions with current sources and workspace state before continuing; a historical completion label alone does not release a dependency.

Paths must make sense to the receiver. For another machine, use an accessible committed revision, approved shared artifact, or another authorized transfer mechanism. Identify temporary or unavailable material explicitly. Do not promise accessibility that has not been checked.

## Continuation prompt

A portable prompt names the handoff location, next goal, key artifacts, and requirement to compare the record with current state before editing. For example, ask the receiver to read the record, inspect the workspace and current requirements, then perform the named next action.

Do not include an unverified slash command or an assumed installed Skill. Mention a receiver tool only when its availability and meaning are known. The record cannot authorize external actions beyond the current user's instruction.

Completion means the record is written or clearly delivered inline, its critical pointers have been checked as far as available, and the next action is concrete. Successful resumption is a separate observation.
