# Interaction Sketches

Implement the smallest sequence that lets the user judge the proposed interaction. The prototype need not reproduce the entire product flow.

## Keep the decisive interaction real

For a drawer comparison, make it open, close, and show enough surrounding content to judge the trade-off. For a multi-step form, make the relevant steps navigable. Prefer native buttons, links, and labeled inputs to custom control machinery.

Use sample data and in-memory state by default. When recovery after a reload or return is the behavior being judged, keep only the needed sample values in browser-local storage and try that recovery path. For other saves, an in-memory update or simulated result is enough. Provide a simple way to return to the starting point when the comparison needs repetition.

## Demonstrate only relevant states

Loading, empty, failure, disabled, and partial-progress views are optional scenarios, not a required checklist. Include a state only when it changes the interaction being judged. A preset or a small demo toggle can show an error without implementing the real failure path.

For example, judging whether inline errors are understandable needs an editable field and a representative error. Judging whether a drawer leaves enough space for the list usually does not need form validation at all.

Keep controls needed for the question usable. Elaborate focus behavior, gesture alternatives, or animation timing belong here only when they affect the question. Avoid building a general interaction or accessibility framework for a disposable demo.

Clearly distinguish simulated effects and unfinished areas so the user knows which actions are meaningful.
