---
date: 2026-09-01
slug: migrate-narrative-consumers-to-explicit-kind
title: "Migrate Narrative consumers to explicit kind"
summary: "Migrate PEI experimentally to Narrative candidate `4088093e522bd29201d33b7b47ca000239190368`, updating both action pins, the PR template, and canonical agent instructions together."
kind: experiment
status: accepted
sequence: 2026-09-01T12:14:17.000Z
evidence: "https://github.com/KarenBrazil12/personal-energy-insights/pull/16; merge commit 90bc8a3c1c48d5eadda072aa928f83909348d057"
---

## Context

The Narrative processor is being evolved from a hard-coded `product` Kind to explicit bounded Kind evidence supplied by a qualifying pull request. PEI is being used as a real existing consumer to test the manual migration contract before the candidate Narrative implementation is proposed for adoption.

## Decision

Migrate PEI experimentally to Narrative candidate `4088093e522bd29201d33b7b47ca000239190368`, updating both action pins, the PR template, and canonical agent instructions together.

The existing pre-merge Narrative evidence behaviour is deliberately left unchanged so it can be observed separately.

## Consequences

PEI’s branch configuration now describes the explicit six-value Narrative Kind contract and will use the candidate processor after merge.

This PR was intentionally created without a ## Narrative Kind section so the existing pre-merge validation behaviour could be observed. The body was corrected to the four-section contract before merge consideration.
