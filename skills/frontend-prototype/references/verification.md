# Prototype Verification

Verification should answer the design question, not imitate a full production QA program.

Run the critical user flow from its real entry point. Reset to a known state and repeat any comparison consistently. Exercise every state that materially affects the chosen layout or interaction.

Check at minimum:

- the main task can be completed without hidden knowledge;
- the primary action and current state are clear;
- focus is visible and overlays return focus sensibly where applicable;
- representative loading, empty, error, validation, and long-content states do not break the design;
- the layout works at the target desktop width and a meaningful narrower width when responsive behavior matters;
- labels and messages use the product's established terminology.

Record what was actually exercised. A visually convincing screen is not evidence that the flow works, and a clickable flow is not evidence of production quality.
