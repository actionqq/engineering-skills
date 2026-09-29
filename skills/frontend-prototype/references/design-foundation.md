# Frontend Design Foundation

Use these rules for both prototypes and production frontend work; the delivery profile changes, not the underlying design judgment.

## Start from the product register

Distinguish product UI from brand or campaign UI. Product interfaces such as admin tools, workflow builders, settings, dashboards, and developer tools should optimize for comprehension, task completion, consistency, and appropriate information density. Brand surfaces may justify more expressive composition and motion.

Existing product conventions outrank novelty unless the task is explicitly a redesign. Inspect the current navigation, spacing, typography, components, tokens, density, icon language, and recurring interaction patterns before inventing a new visual grammar.

## Make hierarchy intentional

Use position, grouping, size, weight, contrast, whitespace, and alignment to show what is primary, secondary, related, or dangerous. Do not make every region a card. Containers should express a real grouping or interaction boundary.

Choose typography for readability and product character. Avoid changing font families simply to appear distinctive when an established product system exists. Use a restrained type scale and preserve useful numerical alignment for dense data.

Use color to communicate structure and state, not to decorate every region. Prefer existing semantic tokens. Ensure status does not rely on color alone.

Spacing should reveal relationships. Repeated arbitrary gaps, nested padding, excessive rounded boxes, and decorative dividers are common signs that the hierarchy is unresolved.

## Avoid template-shaped UI

Do not default to a hero-like composition, purple/blue gradients, floating glass cards, icon tiles above every heading, oversized headings, or motion everywhere. These patterns can be appropriate when the product context warrants them; they are not neutral defaults.

A strong design has a specific reason for its composition. For product UI, one deliberate improvement to hierarchy or interaction is usually more valuable than many stylistic flourishes.

## Preserve design-system continuity

Reuse existing primitives and tokens where they fit. Product-specific composites may remain local even when visually built from shared primitives. Do not distort a shared primitive to encode one feature's business rule.

When no design system exists, keep a small consistent vocabulary: spacing rhythm, type scale, surface levels, border treatment, focus treatment, semantic colors, and interaction states.
