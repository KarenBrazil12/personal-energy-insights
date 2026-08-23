# Product Intent

## Product goal

Help a user understand household energy economics using evidenced energy and pricing data, progressively exploring whether different tariffs, energy-use patterns or storage strategies could have produced a better outcome.

The product should remain neutral about particular inverter, battery or home-energy-system vendors until a useful product capability requires a concrete boundary.

## Current outcome

For a selected historical period, calculate and explain the cost of evidenced electricity imported from the grid using the pricing applicable to that import.

## Why this slice comes first

It establishes a trustworthy baseline before attempting comparison, prediction or optimisation.

## Success

The user can:

- see how much grid electricity was evidenced for the selected period;
- see the evidenced usage cost;
- understand how the result was derived;
- see clearly when the available evidence is incomplete.

## Current boundaries

Not part of this slice:

- inverter or home-energy-system telemetry;
- household-load reconstruction;
- local generation analysis;
- battery state or energy-flow modelling;
- charge/discharge scheduling;
- export valuation;
- alternative-tariff comparison;
- tariff switching;
- forecasting;
- optimisation;
- full bill reconciliation.

No integration mechanism is selected by this intent.

## Current experiment context

The first concrete evidence source is an Octopus Energy account because it provides a real test environment for the product proposition.

This is experiment context, not a commitment that the product domain or architecture is defined by Octopus-specific terminology or mechanisms.

A real environment should be used as evidence and a test fixture. Incidental characteristics of that environment should not be promoted into product architecture unless the product need requires them.

## Workspace experiment goal

Test whether repository artefacts can preserve enough intent, domain meaning, decisions, evidence and behaviour for a fresh AI coding agent to implement the intended solution without access to the shaping conversation.

Ambiguity discovered by the builder is specification evidence and should not be silently repaired in code.
