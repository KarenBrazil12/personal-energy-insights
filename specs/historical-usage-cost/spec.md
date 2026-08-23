# Historical Grid-Import Usage Cost

**Status:** SHAPING  
**Builder-ready:** NO

This specification defines the current adopted behaviour for the historical grid-import usage-cost slice. Builder handoff must not occur while material behaviour remains unresolved.

## Outcome

For a selected historical period, produce an explainable calculation of the usage cost associated with evidenced grid-import energy.

## Calculation semantics

Historical grid-import usage cost is an analytical result based on evidenced measurements and evidenced applicable pricing. It is not a reproduction of supplier billing semantics.

[`../../decisions/ADR-001-analytical-usage-cost-semantics.md`](../../decisions/ADR-001-analytical-usage-cost-semantics.md) defines this product-semantic boundary.

## Conceptual inputs

The capability requires:

- a selected historical period;
- evidenced `GridImport` measurements;
- sufficient tariff/pricing evidence to establish the price applicable to each costed measurement interval.

No API, protocol or integration mechanism is selected by this specification.

## Required output

Produce a result containing:

- selected period;
- evidenced grid-import quantity;
- evidenced usage cost;
- completeness status;
- identifiable gaps or ambiguities;
- traceable interval-level calculation evidence.

## Required behaviour

1. Only measurements representing `GridImport` are in scope for this calculation.
2. Every costed measurement interval must resolve to exactly one acceptable pricing interpretation.
3. Different prices within the selected period must be applied to the intervals to which they actually apply.
4. A tariff/agreement transition within the selected period must not cause the whole period to be priced using one agreement merely for convenience.
5. Missing measurement evidence must not be interpreted as zero.
6. Missing pricing evidence must not be guessed.
7. Ambiguous pricing evidence must not be resolved arbitrarily.
8. Incomplete source retrieval must not produce a result marked complete merely because execution succeeded.
9. A partial evidenced cost may be shown, but it must not be represented as the complete cost of the selected period.
10. Every cost contribution must remain traceable to the measurement and pricing evidence used to derive it.
11. Completeness must be assessed from meaningful temporal/evidence coverage rather than a fixed expected record count.
12. Analytical costing must preserve the useful precision of the evidenced measurements and applicable pricing through the calculation.
13. Supplier-specific intermediate rounding must not be introduced merely to reproduce or approximate a supplier bill.
14. Currency rounding must occur only at an explicit product or presentation boundary and must not be confused with the analytical calculation semantics.

## Acceptance examples

### Complete period

Given acceptable measurement coverage for the selected period and exactly one applicable pricing interpretation for every included interval,

then:

- the result is `Complete`;
- all included intervals are costed;
- total cost equals the aggregate of interval costs;
- each contribution is explainable.

### Variable pricing

Given rates change during the selected period,

then each measurement interval is costed using the pricing applicable to that interval.

### Tariff transition

Given the selected period crosses an agreement boundary,

then intervals on either side are resolved using their governing agreement/pricing evidence.

### Analytical precision

Given evidenced measurements or applicable pricing contain more precision than the final displayed currency amount,

then:

- the calculation uses the useful source precision rather than supplier-specific billing-rounding rules;
- intermediate interval contributions are not rounded merely to imitate a bill;
- presentation rounding is applied only at the explicit output boundary;
- a legitimate difference from a supplier bill is not by itself treated as a calculation defect.

### Missing measurement

Given part of the selected period lacks an evidenced measurement,

then:

- no zero measurement is invented;
- the evidenced portion may be calculated;
- the overall result is `Incomplete`;
- the missing coverage is identified.

### Missing pricing

Given a measurement exists but no acceptable applicable price can be established,

then:

- the interval is unpriced;
- no price is guessed;
- the result is `Incomplete`.

### Ambiguous pricing

Given more than one incompatible pricing interpretation could apply,

then:

- no interpretation is silently selected;
- the ambiguity is reported;
- the result is `Incomplete`.

### Calendar / DST boundary

Given the selected period crosses a daylight-saving or other calendar boundary,

then completeness is assessed from temporal coverage and source semantics rather than assuming a calendar day always contains a fixed number of measurement records.

### Retrieval incompleteness

Given a source request technically succeeds but required pages or evidence are missing,

then:

- technical execution may be reported as successful;
- evidence completeness is reported separately;
- the calculation must not claim a complete period result.

## Current exclusions

This slice does not require:

- standing charges;
- exact supplier bill reconstruction;
- export valuation;
- inverter or home-energy-system telemetry;
- local generation modelling;
- household-load reconstruction;
- battery state or flow modelling;
- storage scheduling;
- alternative-tariff comparison;
- optimisation.

## Builder blockers

Material unresolved questions are owned in [`../../product/understanding.md`](../../product/understanding.md).

The specification becomes `Builder-ready: YES` only when all behaviour needed for independent implementation is either:

- resolved and promoted into authoritative repository artefacts; or
- deliberately constrained so that the builder does not need to invent an architectural answer.
