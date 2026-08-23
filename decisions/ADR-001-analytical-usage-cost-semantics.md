# ADR-001: Treat historical usage cost as analytical insight, not bill reproduction

**Status:** Accepted  
**Scope:** Historical grid-import usage-cost capability  
**Decision strength:** Durable

## Context

The current product slice answers a user question that can sound deceptively simple: what did the evidenced electricity imported from the grid cost during a selected historical period?

Two plausible interpretations exist:

1. calculate an analytical cost from evidenced source measurements and the pricing evidenced as applicable to those measurements; or
2. reproduce the supplier's billing result, including supplier-specific rounding, aggregation and other bill-production semantics.

Those interpretations can produce different monetary results even when they start from the same underlying energy and pricing evidence.

The product intent is to understand household energy economics from evidenced grid import and applicable pricing. Full bill reconciliation is outside the current slice. The specification also requires every cost contribution to remain traceable to its measurement and pricing evidence.

Leaving the semantic choice implicit would force a builder to invent a consequential product meaning.

## Decision

Historical grid-import usage cost is an **analytical insight** derived from evidenced source measurements and evidenced applicable pricing. It is **not** an attempt to reproduce supplier billing semantics.

Within this scope:

- use the useful precision provided by the evidenced source measurements and applicable pricing;
- do not introduce supplier-specific intermediate rounding merely to imitate a supplier bill;
- perform monetary arithmetic at sufficient precision to avoid avoidable calculation loss;
- round only at an explicit product or presentation boundary where a currency representation requires it;
- retain interval-level provenance so the analytical result remains explainable.

An analytical result is exact according to this declared calculation contract when its required evidence is complete. A difference from a supplier bill does not by itself make the analytical result approximate or incorrect; the two results may be governed by different semantics.

## Consequences

### Positive

- The product meaning aligns with the stated goal of understanding evidenced energy economics rather than reconstructing a bill.
- A builder does not need to invent supplier-specific rounding or aggregation behaviour.
- Calculation precision and explainability remain tied to the evidence actually available.
- The capability remains more vendor-neutral because supplier billing mechanics are not silently promoted into the product's core semantics.

### Trade-offs

- The displayed analytical usage cost may differ from a supplier bill even when both are legitimate within their respective calculation contracts.
- The product must avoid wording that implies exact bill reproduction or reconciliation.
- Presentation rounding must remain distinguishable from calculation semantics.

### Future implications

Supplier billing-rounding rules and other bill-production behaviour remain useful evidence, but exact bill reconstruction is a separate future capability. Introducing that capability would require explicit scope, sufficient supplier-specific evidence, and a deliberate decision about its semantics rather than changing this analytical contract implicitly.

Standing charges, account-level adjustments, credits, discounts and other bill-reconciliation concerns remain outside this decision unless separately brought into scope.

## Alternatives considered

### Reproduce supplier billing semantics

Rejected for the current slice.

It would answer a different product question and would require supplier-specific evidence about rounding, aggregation and other billing mechanics that the current product does not promise to reproduce. It would also couple the initial analytical capability more tightly to incidental supplier behaviour.

### Leave the choice to implementation

Rejected.

Both analytical costing and bill reproduction are plausible implementations, but they carry materially different product meaning. Treating the choice as an implementation detail would allow a builder to change the product contract without an architecture decision.

## Remaining open questions

This decision does not resolve:

- the final user-facing `SelectedPeriod` boundary;
- the architectural mechanism used to establish `ApplicableRate`;
- the exact source/tariff scenarios supported beyond those evidenced by the experiment;
- future bill-reconciliation semantics;
- standing charges or other non-usage bill components;
- REST, GraphQL, MCP or another integration mechanism;
- persistence, UI or deployment technology.

## Evidence and traceability

- Issue #2 records the proposition, shaping evidence and human decision used to propose this ADR.
- [`../product/intent.md`](../product/intent.md) defines the current outcome and excludes full bill reconciliation.
- [`../product/understanding.md`](../product/understanding.md) records the working semantic fork that this ADR resolves.
- [`../specs/historical-usage-cost/spec.md`](../specs/historical-usage-cost/spec.md) defines the behaviour that must be reconciled with this decision.

This ADR becomes repository authority only when the pull request carrying it is reviewed and merged.