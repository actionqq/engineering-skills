# Interaction and UI States

Design the complete task, not only the happy screenshot.

## Flows and controls

Prefer familiar controls for familiar actions. Make the primary action obvious, destructive actions distinguishable, and secondary actions discoverable without competing with the main task.

Choose modal, drawer, popover, inline disclosure, or dedicated route from task duration, context needed, amount of information, navigation expectations, and whether the user must compare with the underlying page. Do not choose an overlay solely because it looks compact.

Forms need clear labels, useful defaults, validation close to the cause, preserved input after recoverable errors, and an obvious completion state. Error messages should explain what happened and what action is available.

## Represent meaningful states

Prototype states that can change the design:

- initial and normal content;
- loading or pending;
- empty;
- validation failure;
- recoverable and blocking error;
- disabled or unavailable action;
- long names, long values, dense lists, and overflow;
- partial completion or background progress when relevant.

Do not use only ideal data if real data density determines whether the layout works.

## Keyboard, focus, and access

Use semantic buttons, links, and labeled inputs. For web interfaces, support keyboard operation and visible focus. Modal interactions need sensible initial focus, focus containment, dismissal, and return to the trigger. Do not trap focus in non-modal content.

Keep text and controls distinguishable from their backgrounds and communicate status beyond color. Respect reduced-motion preferences when adding animation. Announce asynchronous feedback where assistive technology would otherwise miss a state change.

Targets should remain usable on touch screens when mobile or tablet is in scope. Do not hide essential information behind hover-only behavior.

## Responsive behavior

Responsive design is not "shrink the desktop". Decide what reflows, wraps, collapses, scrolls, becomes sequential, or remains fixed. Preserve task priority at narrower widths.

Test actual representative widths rather than assuming a breakpoint solved the layout.
