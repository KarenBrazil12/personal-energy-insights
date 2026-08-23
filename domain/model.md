# Domain Model

This document defines the human-readable domain meaning adopted by the workspace.

External supplier or device terminology may inform this model but does not define its semantics.

## EnergyFlow

Energy moving across a meaningful boundary.

### GridImport

An `EnergyFlow` entering the premises from the electricity grid.

`GridImport` is not synonymous with `HouseholdLoad`.

### HouseholdLoad

Energy consumed by loads within the premises.

`HouseholdLoad` may be supplied by grid import, local generation, storage discharge or combinations of those sources.

It is not required by the first product slice, but the distinction is retained because it prevents grid import from being misrepresented as total household consumption.

## EnergyMeasurementInterval

An evidenced observation of an `EnergyFlow` over a bounded time interval.

An `EnergyMeasurementInterval` is not the `EnergyFlow` itself.

Conceptual properties include:

- measured flow;
- interval start;
- interval end;
- quantity;
- unit;
- provenance.

Absence of an `EnergyMeasurementInterval` does not assert zero energy.

## SelectedPeriod

The period the user asks the product to analyse.

A `SelectedPeriod` is not necessarily identical to a source measurement interval.

The initial product slice requires a clear rule for how selected-period boundaries relate to complete measurement intervals.

## TariffAgreement

A commercial pricing agreement applicable to an electricity supply during some period.

A `TariffAgreement` is not itself a unit price.

## UnitRate

A monetary price per unit of energy under defined pricing conditions.

A `UnitRate` existing does not by itself establish that it applies to a particular `EnergyMeasurementInterval`.

## Applicable pricing

`ApplicableRate` is currently treated as an evidenced or derived relationship rather than an independent domain entity:

`UnitRate -- appliesTo --> EnergyMeasurementInterval`

The relationship must be established from relevant agreement, pricing and temporal conditions.

## CostedInterval

A derived result relating:

- one `EnergyMeasurementInterval`;
- its evidenced applicable pricing;
- the resulting usage cost.

A `CostedInterval` retains provenance sufficient to explain the calculation.

## CalculationResult

The result of costing evidenced intervals for a selected period.

A `CalculationResult` conceptually contains:

- selected period;
- evidenced grid-import energy;
- evidenced usage cost;
- coverage/completeness;
- identifiable gaps or ambiguities;
- contributing `CostedInterval` results.

A partial evidenced cost is not the same thing as the complete cost of the selected period.

## Key invariants and distinctions

- measurement != measured phenomenon
- `GridImport` != `HouseholdLoad`
- missing measurement != zero measurement
- available rate != applicable rate
- successful execution != complete evidence
- incomplete evidenced cost != complete period cost

## Formalisation status

A small RDF/OWL learning model may be introduced to formally express selected domain semantics.

Machine validation such as SHACL may be introduced where it prevents or clarifies a demonstrated failure.

The human-readable adopted domain meaning in this document remains the primary authoring reference unless a later deliberate decision changes that operating model.

Formal representations must remain reconcilable with the adopted domain meaning rather than becoming an independent competing source of truth.
