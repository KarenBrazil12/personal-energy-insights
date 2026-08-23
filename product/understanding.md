# Current Understanding

This is the working architectural staging area.

Statements retain their epistemic status until deliberately promoted into Domain, Specification or Decisions. Once understanding has matured into an authoritative home, prefer removing or reducing the duplicated working wording here rather than maintaining parallel sources of truth.

## Facts from external discovery

- The initial energy provider documents programmatic access to interval electricity consumption data.
- The initial energy provider documents tariff/agreement and pricing information with temporal applicability.
- Pricing structures are not universally identical; generic tariff support should not be claimed beyond evidenced scenarios.
- External source vocabulary does not by itself define this product's canonical domain semantics.
- Missing source evidence and an evidenced zero measurement are different situations.

The relevant official evidence should be captured or linked by the issues that rely upon it rather than accumulated in a central evidence warehouse by default.

## Inferences

- The first product slice appears feasible without inverter, battery or home-energy-system telemetry.
- Metered grid import is the appropriate quantity for the initial usage-cost capability.
- A provider field named `consumption` should not automatically become a canonical product concept named Consumption.
- The first slice can probably remain much narrower than full bill reconstruction.

## Assumptions requiring real evidence

- The test account has sufficiently complete historical import data for an initially selected period.
- The pricing evidence required to resolve the applicable price for that same period is available and coherent.
- Meter or account history will not introduce an unmodelled discontinuity in the first test period.
- The selected period can be chosen so the minimum evidence chain can be demonstrated without introducing unrelated tariff complexity.

## Open questions

### Product / calculation semantics

- Should analytical usage costing use source measurement precision or reproduce supplier billing-rounding semantics?
- What selected-period boundary should the first user-facing capability support: whole local calendar dates, arbitrary complete measurement intervals, or something else?

### Evidence / integration discovery

- What tariff structure exists in the actual initial test period?
- Does meter replacement or account history affect continuity?
- Which available provider capability gives the clearest evidence for the relationship between a measurement interval and its applicable price?
- What practical historical depth and completeness are available for the test account?

## Decision candidates

These are **not ADRs**. They are candidates to be tested through issues and promoted only if they prove durable, consequential and ADR-worthy.

### Analytical costing semantics

Candidate proposition:

> Historical usage costing is an analytical insight based on evidenced measurements and applicable pricing, not an attempt to reconstruct the supplier bill.

Possible consequence:

- use source measurement precision for analytical costing;
- keep supplier billing-rounding semantics as known evidence;
- treat exact bill reconstruction as a separate future capability.

This appears to be a strong candidate for the first ADR because it changes the meaning of the result and is likely to matter to future capabilities.

### Selected-period semantics

Candidate proposition:

> The first capability should cost only complete evidenced measurement intervals and should not prorate or invent partial-interval consumption.

The final user-facing period model still requires shaping.

### Pricing applicability boundary

Candidate proposition:

> An interval is costable only where exactly one acceptable pricing interpretation can be evidenced for that interval.

This is already reflected as required behaviour, but the eventual architectural boundary for establishing that relationship remains undecided.

## Deferred

- standing charges as part of a broader tariff-cost view;
- exact bill reconciliation;
- export valuation;
- inverter/home-energy-system telemetry;
- local generation;
- household load;
- battery state and energy flows;
- storage schedules and optimisation;
- alternative-tariff comparison;
- formal ontology as a production dependency;
- REST vs GraphQL vs MCP or another integration mechanism;
- persistence technology;
- UI technology;
- deployment architecture.
