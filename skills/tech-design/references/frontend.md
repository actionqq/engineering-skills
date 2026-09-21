# Frontend Ownership and Runtime Boundaries

Use for browser, native-screen, desktop-web, design-system, and full-stack frontend structure. Do not import a backend architecture template just because the application also has a server.

Inspect routes/screens, rendered interactions, component consumers, state stores, requests and mutations, schemas, cache keys, styling/tokens, generated clients, runtime markers, and build conventions. Distinguish:

- navigation entry versus a product interaction reused across entries;
- route-owned UI versus feature UI versus feature-independent visual primitives;
- component, URL, feature, server-cache, and genuinely global state;
- browser, server, worker, native-shell, and safe shared modules;
- an organizational folder versus a package with a public boundary.

## Select a useful organization

For a small app, framework routes with colocated private UI, data, and tests may be sufficient. Extract a feature when a coherent interaction spans routes, needs independent ownership, or becomes difficult to navigate. Routes compose features; a feature is not simply every noun or component.

Keep the framework's discoverable route tree where it belongs. Use its supported colocation and private-module conventions rather than maintaining a duplicate tree. Add local `ui`, `state`, or `api` folders only when they improve navigation within a real owner.

For an explicitly adopted layered frontend method, preserve its actual public APIs and dependency rules. Copying folder names while allowing arbitrary cross-imports does not implement that method. Microfrontends need a genuine deployment or organizational reason; clutter alone is not one.

## Assign state and data to the narrowest owner

Local interaction state stays local; navigation state belongs to routing; remote cache state stays with its data owner. A global-store library is not a reason to centralize all state. If using actors or state machines, say which owner creates, persists, and stops them.

Keep requests, schemas, mapping, cache keys, invalidation, mutations, and optimistic behavior with the route or feature responsible for the interaction. Shared transport and authentication mechanics may belong to a named platform capability. Generated clients remain generated; owned adapters can stop provider shapes spreading through product UI.

Design-system primitives and tokens should not import product features, application stores, or product data clients. Product-specific composites remain with their product owner even when several screens use them.

## Enforce the runtime graph

Server-only modules own privileged clients, secrets, database/filesystem access, and server resource lifecycle. Client modules own interactive browser behavior. Shared modules must be valid in every importing runtime; purity alone does not make a module part of a backend domain.

Use appropriate framework markers, explicit exports, dependency checks, and build inspection. Check the built client graph where leakage matters: a folder called `server` cannot by itself prevent privileged code reaching a bundle. Beware catch-all exports that pull server code into client imports or defeat lazy loading.

During migration, carry a feature's tests, styles, fixtures, stories, state, and data ownership with it. Validate route discovery, loading/error behavior, forms and relevant accessibility, lazy chunks, runtime boundaries, and public imports. The result should make a user-visible flow easier to find without inventing unused layers.
