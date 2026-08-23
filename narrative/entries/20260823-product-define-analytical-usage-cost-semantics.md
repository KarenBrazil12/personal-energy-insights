---
date: 2026-08-23
slug: product-define-analytical-usage-cost-semantics
title: "[Product] Define analytical usage-cost semantics"
summary: "Adopt ADR-001 as an `Accepted` / `Product` / `Definitive` decision: historical grid-import usage cost is an analytical insight derived from evidenced source measurements and evidenced applicable pricing, not a reproduction of supplier…"
kind: product
status: accepted
sequence: 2026-08-23T14:03:07.000Z
evidence: "https://github.com/KarenBrazil12/personal-energy-insights/pull/9; merge commit c82bb7a619fabfd414d51771222a43645e7a1734"
---

## Context

The first product slice needs an explicit meaning for historical usage cost. Both analytical costing from evidenced measurements/rates and exact supplier-bill reproduction are plausible implementation choices, but they can produce different results and therefore represent different product semantics. Product intent focuses on evidenced energy economics and explicitly excludes full bill reconciliation, so leaving the choice implicit would force a builder to invent a consequential answer.

## Decision

Adopt ADR-001 as an `Accepted` / `Product` / `Definitive` decision: historical grid-import usage cost is an analytical insight derived from evidenced source measurements and evidenced applicable pricing, not a reproduction of supplier billing semantics. Preserve useful source precision through calculation, avoid supplier-specific intermediate rounding merely to imitate a bill, and round only at an explicit product or presentation boundary.

## Consequences

The product can produce a result that is exact under its declared analytical contract while legitimately differing from a supplier bill. Builders must not silently replace that meaning with supplier-bill reproduction; changing the contract requires deliberate amendment or supersession. Supplier-specific bill reconstruction remains separate future scope requiring its own evidence and decision. The selected-period boundary, pricing applicability mechanism and broader tariff/billing capabilities remain deliberately unresolved.
