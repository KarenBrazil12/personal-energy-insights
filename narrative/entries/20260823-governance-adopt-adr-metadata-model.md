---
date: 2026-08-23
slug: governance-adopt-adr-metadata-model
title: "[Governance] Adopt ADR metadata model"
summary: "Adopt ADR-000: every ADR carries explicit Status, Scope and Decision strength using a defined repository vocabulary."
kind: governance
status: accepted
sequence: 2026-08-23T13:39:44.000Z
evidence: "https://github.com/KarenBrazil12/personal-energy-insights/pull/11; merge commit 3f7f91743e132a380e2d95472b4668c111ffe942"
---

## Context

Before adopting the first product ADR, the repository exposed an ambiguity in its own ADR contract: `AGENTS.md` required Status, Scope and Decision strength to remain separate but did not define the allowed values or what they meant. Prior governed architecture work had already developed and exercised a useful three-dimensional model, so inventing a new vocabulary here would discard learning while copying the full prior governance process would import unnecessary ceremony.

## Decision

Adopt ADR-000: every ADR carries explicit Status, Scope and Decision strength using a defined repository vocabulary. Reuse the learned values for lifecycle, applicability and constraint strength, adapted to this repository's authority model without importing prior-repository CODEOWNERS, approval thresholds or mandatory two-step acceptance.

## Consequences

Future ADRs can be interpreted without hidden context, and the first product ADR can state `Accepted` / `Product` / `Definitive` with an explicit meaning and departure path. The metadata model itself becomes a Definitive Meta (governance) decision; changing it requires deliberate amendment or supersession. Automated enforcement remains deliberately unintroduced until a demonstrated need exists.
