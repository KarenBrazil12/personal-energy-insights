# Repository Operating Instructions

## Core principle

**AI compresses information; the architect expands judgement.**

AI may gather and compress evidence, draft repository changes, identify inconsistencies, surface questions and propose interpretations. It must not quietly turn generated output into architectural authority.

The operating loop is:

**notice → reason → capture → test → review → decide → leave a durable trail**

A common change path is:

**observation → issue → proposed change → PR → automated evidence → human review → merge → Narrative**

## Sources of authority

Treat adopted repository content according to its purpose and scope.

- **Intent** establishes why the product or slice exists and its boundaries.
- **Understanding** is a working staging area containing mixed epistemic states. Presence there does not make a statement an architectural commitment.
- **Domain** establishes adopted meaning and relationships.
- **Specification** establishes adopted required behaviour for its stated status and scope.
- **Decisions** establish durable consequential choices once adopted through an ADR.
- **Narrative**, once introduced, is an authoritative historical account of meaningful architectural change, but it does not override current Domain, Specification or Decisions.

AI-generated text has no additional authority because AI generated it.

## Epistemic discipline

Keep these distinct:

- **Fact** — supported by evidence.
- **Assumption** — currently relied upon but not yet established.
- **Inference** — a conclusion drawn from evidence or other statements.
- **Open question** — materially unresolved.
- **Deferred** — deliberately not being answered in the current scope.
- **Decision candidate** — a possible durable commitment that has not yet crossed the human decision boundary.
- **Architectural commitment** — an adopted consequential decision within a stated scope.

Do not silently promote:

- assumptions into facts;
- inferences into facts;
- questions into answers;
- decision candidates into commitments;
- generated recommendations into decisions.

## Builder autonomy

A builder may choose ordinary implementation details where those choices do not alter established Intent, Domain, Specification or Decisions.

If material behaviour, meaning, ownership, failure behaviour or a required boundary is ambiguous, surface the ambiguity rather than inventing an architectural answer merely to continue implementation.

Builder-discovered ambiguity is specification evidence.

## Evidence and controls

Use deterministic automation for things machines can genuinely establish.

A deterministic check establishes only what it actually tested.

Examples include:

- syntax and schema validity;
- calculation correctness against known examples;
- completeness checks where completeness is mechanically defined;
- internal link integrity;
- deterministic domain constraints.

AI or semantic review is an **evidence-generating second pair of eyes**, not approval and not a source of truth.

Controls should produce evidence a human can understand well enough to act on.

Meaningful human control should put the relevant question and evidence in front of the human while the decision can still change the outcome.

## Public repository safety

This repository is deliberately public. Public visibility is part of the experiment, but credentials and identifiable personal data are not architecture artefacts.

Never commit:

- API keys, access tokens, passwords, private keys or other credentials;
- personal energy-account identifiers;
- MPANs, meter serial numbers, home addresses or other identifiers that connect repository data to a real household;
- identifiable household energy readings or exports from a real account;
- screenshots, logs or fixtures containing any of the above.

Real account data used for discovery or testing must remain local or in an explicitly private environment. Repository fixtures must be synthetic or deliberately sanitised.

Use environment variables or an appropriate secret store for credentials. Do not echo secret values or private account data into CI logs, issues, pull requests or review comments.

The fact that a value is not detected by automated secret scanning does not make it safe to publish.

## Issue naming

Issue titles should normally use:

**`[Area] Clear action-oriented title`**

The title should describe the proposition, question or outcome being worked, not pre-decide the artefact expected to result.

For example, prefer:

- `[Product] Resolve analytical usage-cost semantics`

rather than:

- `[ADR] Create ADR-001`

because the issue may ultimately be resolved by an ADR, a specification change, a domain clarification, a deliberate deferral or another appropriate outcome.

Reuse an existing area prefix when it accurately describes the work. Introduce a new area only when it makes the issue set easier to understand; do not create prefixes merely for specificity or decoration.

Examples of useful areas may include `[Product]`, `[Governance]`, `[Domain]`, `[Evidence]` and `[Build]`, but this list is **emergent guidance, not an authoritative registry**.

Do not add role prefixes such as `[Architect]`, `[Builder]` or `[AI]` unless a demonstrated need makes role distinction useful to the work itself.

Issue naming is guidance rather than a mechanically enforced rule. Add stronger validation only if inconsistent naming later creates a real navigation or governance problem.

## Architecture review lens

For meaningful changes ask:

- What is actually decided?
- What remains unproven?
- Who owns or is responsible for what?
- What happens on failure?
- Where is meaningful human control?

When a review reveals another concern, ask:

**Did this change create the problem, or did reviewing this change merely reveal it?**

If the concern is pre-existing and does not invalidate the current proposition, normally capture it as separate follow-up work rather than bloating or blocking the change.

**Not blocking does not mean not worth understanding.**

## ADR discipline

Not every decision deserves an ADR.

Use an ADR when future humans or agents are likely to need to know that a consequential choice was deliberately made, what alternatives mattered, why the choice was made, and what its stated scope and decision strength are.

Keep **Status**, **Scope** and **Decision strength** separate. An accepted experimental decision is not automatically universal or immutable.

Decision candidates should normally mature in Understanding and through proposition-led issues before promotion into an ADR.

A PR that introduces or materially changes an ADR should normally include or update Narrative when the architectural understanding has materially changed.

## Reconciliation

Merging an implementation artefact does not by itself mean the originating intent has been fulfilled.

Before closing meaningful parent intent, reconcile:

- what was intended;
- what was learned;
- what was adopted into Domain or Specification;
- what was decided;
- what was implemented;
- what remains unresolved;
- what was deliberately deferred.

PR review is a **local sensor** for what a change may have disturbed.

Occasional whole-repository reconciliation is a **system-level health check** for cumulative semantic or architectural drift that no individual PR necessarily caused.
