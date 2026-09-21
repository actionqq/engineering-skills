# Execution and Recovery

Use before archive-related file, metadata, or index changes. These are execution properties, not a requirement to install a particular CLI or database.

## Select placement and record the operation

Prefer the project's archive layout and identifiers. If none exists and organization is authorized, use one archive root alongside the maintained documentation and a descriptive group name; add a date or release only when it helps distinguish batches. Preserve filenames and useful relative structure. Avoid copying all active documentation or creating a global registry merely to archive a few files.

Use the smallest durable record that supports retrieval and recovery: an existing index entry, or one batch README for a larger move. Record reason and date, original and destination paths, scope/revision when material, current successor links when they exist, and unresolved work destinations. Keep original content dates separate from the archive date. A snapshot also needs its original source and the boundary it freezes; label it as a historical copy.

Before mutation, inspect staged, unstaged, and untracked state and any concurrent writers. Git tracking does not mean current edits have been saved. Preserve a recoverable baseline of affected current contents, including untracked attachments, through the project's versioning mechanism or a bounded local backup. Do not commit unrelated work or assume a commit includes ignored files. Do not read credentials to populate an archive manifest.

## Apply changes in a safe order

1. Resolve source and destination within the authorized tree. Account for symlinks, case sensitivity, existing targets, and nested moves. Treat source/destination overlap or collisions as unresolved, not permission to merge or overwrite.
2. Recheck the evidence and actual file state used for the disposition. If contents changed materially since assessment, reassess the affected item instead of applying stale edits.
3. Carry forward the required current information and live obligations. Verify their destinations before retiring the only prior source. In a batch with shared successors, reconcile conflicting updates and apply dependencies in order.
4. Preserve the historical artifact by the selected mechanism. A move retains the original content; a snapshot leaves the evolving source intact; an in-place archive changes lifecycle/navigation, not identity. For copy-based moves, verify the destination before removing the source within the authorized move.
5. Repair affected incoming and outgoing references, attachments, anchors, and navigation. Rebase relative links in both moved files and moved index entries. Inspect non-Markdown paths used by scripts or tooling as well as visible links.
6. Add concise historical labeling and a current-source pointer when available. Do not relabel an active proposal or enduring ADR merely because neighboring work closed. Preserve original rationale; necessary historical errata are dated additions.
7. Check the resulting paths, content preservation, references, and active/archive entrypoints, then mark the item's actual outcome.

Search within the affected scope for old paths. Distinguish broken consumers from intentional original-path provenance; do not globally replace text that records history. For external links that cannot be edited, retain a small redirect/pointer at the old path when needed, or prefer in-place archival. Report remaining external-reference limitations.

## Interruption and repeat execution

Do not claim multi-file atomicity from individual moves or writes. Keep a source-to-destination mapping and enough current content evidence to distinguish an already completed operation from a collision. When helpers are warranted, use destination-first preservation, atomic individual-file writes where available, and stable identifiers for index deduplication; still report partial batch failure.

On retry, inspect both locations and the indexes:

- Source present, destination absent: reassess that the planned operation still applies.
- Source absent, verified destination present: finish missing reference/index repairs without a second move or changed archive date.
- Both present: determine whether this is an intended snapshot or an interrupted copy. Compare against the operation record; never remove one merely because names match.
- Neither present, or conflicting content: stop that item and report the recovery evidence needed.

Repair an already archived item's index without changing its historical outcome. Do not append duplicate entries or place the same directory inside an existing destination. Continue independent items only when they do not depend on a failed information transfer or shared index update. Report each preserved, completed, deferred, or failed outcome; an attempted move is not completion.

## Verify proportionately

Compare final files with the baseline, allowing only intended metadata, link, and dated-note changes. Confirm attachments, successor coverage, live obligations, anchors, index uniqueness, and discoverability. Use available document/link tooling, or inspect and resolve affected links directly when no checker exists. Check from both a current reader's and a historical reader's starting point.

A bounded documentation move normally needs structural and content checks, not application tests. Run a documentation build or relevant consumer check if moved paths feed executable tooling. State actual verification and any uncheckable external links; do not claim runtime acceptance or universal search exclusion. Never delete an archive, compress away its only readable evidence, commit, tag, or publish as an implicit completion step.
