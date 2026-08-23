# Personal Energy Insights

A product experiment for developing and testing a governed AI-assisted architecture workspace against a real product need.

## Current product slice

Historical grid-import usage costing.

For a selected historical period, determine evidenced electricity imported from the grid, correlate it with applicable pricing, and produce an explainable usage-cost result.

## Experiment goal

Test whether repository artefacts can preserve enough intent, domain meaning, evidence, decisions and behaviour for a fresh AI coding agent to implement the intended solution without access to the shaping conversation that created them.

Ambiguity discovered by the builder is evidence about the quality of the specification and governance model. It must not be silently patched in code.

## Start here

- How AI and tools should work here: [`AGENTS.md`](AGENTS.md)
- Why the product and current slice exist: [`product/intent.md`](product/intent.md)
- What is currently known, inferred, questioned or deferred: [`product/understanding.md`](product/understanding.md)
- What the domain terms mean: [`domain/model.md`](domain/model.md)
- What the current slice must do: [`specs/historical-usage-cost/spec.md`](specs/historical-usage-cost/spec.md)
- How architectural understanding changed over time: [`Narrative.md`](Narrative.md)

Durable architecture decisions are introduced only when a decision has earned an ADR.

Project Narrative is scaffolded before the first durable architecture decision so the history mechanism is ready without creating an entry prematurely. Its first reviewed fragment is created only when a meaningful change actually earns one. `Narrative.md` is generated from those reviewed fragments and is not hand-authored.
