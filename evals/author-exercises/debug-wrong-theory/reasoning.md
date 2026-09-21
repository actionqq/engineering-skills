# Author exercise: shared default state

Two calls without an explicit cart reuse the default list. The second append also changes the first caller’s returned list; the behavioral red run shows this. There is no encoding transformation in this path. Allocating only when cart is None fixes implicit-call isolation and preserves the identity of an explicitly supplied cart, including an empty one. The green run covers these three cases. This is a narrow fixture observation, not an independent evaluation of the debug Skill.
