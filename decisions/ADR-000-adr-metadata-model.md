# ADR-000: Adopt explicit ADR status, scope and decision-strength model

**Status:** Accepted  
**Scope:** Meta (governance) — repository ADR interpretation model  
**Decision strength:** Definitive

## Context

The repository already requires ADRs to keep **Status**, **Scope** and **Decision strength** separate, but it does not define the allowed values or what those values mean.

That ambiguity became concrete while preparing the first product ADR. A future human or agent could see an ADR described as `Accepted`, `Product` or `Definitive` without knowing the alternatives, the ownership/applicability boundary, or the permitted departure path.

Prior governed architecture work already developed a useful three-dimensional model. This repository should reuse that learning rather than invent a parallel vocabulary, while avoiding prior-repository ceremony that is not needed here.

## Decision

Every ADR carries three orthogonal dimensions:

| Dimension | Question answered |
|---|---|
| **Status** | Where is the decision in its lifecycle? |
| **Scope** | Who owns it and how broadly should it be treated as applicable or reusable? |
| **Decision strength** | How strongly does it constrain future work, and what is the permitted departure or change path? |

The dimensions must not be inferred from one another. An `Accepted` ADR is not automatically `Definitive`; a `Platform` ADR is not automatically stronger than a `Product` ADR.

### Status

Allowed Status values are:

| Status | Meaning |
|---|---|
| `Draft` | Under investigation and still accepting material shaping; not yet a firm recommendation. |
| `Proposed` | A firm recommendation is available, but the human decision is still pending. |
| `Accepted` | The decision has been deliberately made and is binding within its stated scope once authoritative in `main`. |
| `Rejected` | A deliberate decision has been made not to adopt the proposal. Keep the record rather than deleting it. |
| `Withdrawn` | The proposal was stopped before a decision was reached. Keep the record without treating it as a rejection. |
| `Superseded` | A later ADR has replaced the decision. Reference the replacement. |
| `Blocked` | The decision cannot currently progress because a material dependency or evidence gap prevents resolution. |

Status is a property of the ADR content and changes only through a deliberate edit. PR approval or merge must not silently transform `Draft` or `Proposed` into `Accepted`.

An ADR may be authored as `Accepted` when the relevant human decision has already been explicitly reached during shaping and the PR makes that decision and its consequences reconstructable. A branch or PR is still not repository authority: merge to `main` adopts the file into the authoritative repository state.

### Scope

Allowed Scope values are:

| Scope | Meaning |
|---|---|
| `Platform` | An inherited external or platform constraint that this repository records but does not own. Treat it as given within its evidenced context rather than re-deciding it locally. |
| `Pattern` | A reusable architectural approach or shape that is not specific to this product and may inform similar future solutions. |
| `Product` | A decision owned by and specific to this product or one of its explicitly stated slices. |
| `Meta (governance)` | A decision about this repository's own architecture/governance operating model rather than the energy product itself. |

Scope describes ownership and applicability, not rigidity. A `Product` decision may be `Definitive`; a `Platform` constraint may need amendment when its external source changes.

### Decision strength

Allowed Decision strength values are:

| Decision strength | Meaning | Departure or change path |
|---|---|---|
| `Definitive` | A boundary, constraint or semantic commitment that must hold within the ADR's stated scope. | Do not silently depart. Change through deliberate amendment, superseding decision, or changed external authority where applicable. |
| `Design choice` | An approach deliberately selected from credible alternatives. | Use it as the baseline. Reconsider when new evidence, changed requirements or implementation learning justify a different choice, and record the replacement at the appropriate level. |
| `Guideline` | A preferred default or working practice for consistency or quality. | Start from it, but a reasoned and visible deviation is allowed without first superseding the ADR. |

An ADR should normally have one primary Decision strength. If materially different-strength decisions are bundled together, split them or move the weaker detail to a lighter authoritative artefact rather than relying on an implicit "strongest wins" rule.

These exact values are repository governance vocabulary, not energy-domain ontology concepts. A future ontology linter should recognise or explicitly allow them rather than treating their use as accidental domain vocabulary.

## Reuse boundary

This ADR reuses the learned semantic model only. It does **not** import prior-repository:

- CODEOWNERS decision-authority rules;
- enterprise approval thresholds;
- replay-specific process;
- mandatory two-step ADR acceptance;
- automated enforcement of ADR metadata values.

Those controls or practices should be introduced only if this repository develops a demonstrated need for them.

## Consequences

- Future humans and agents can interpret ADR lifecycle, applicability and constraint strength without hidden conversational context.
- ADR-001 can state `Accepted` / `Product` / `Definitive` with a defined meaning.
- The repository can reuse prior governance learning without pretending to have re-derived every part of the original process.
- Changing this metadata model is itself a governance decision and should amend or supersede this ADR deliberately.
- Deterministic validation of these values remains optional future work; the absence of automated enforcement does not weaken the semantic contract.

## Alternatives considered

### Define only Decision strength

Rejected.

The first product ADR exposed the missing Decision-strength vocabulary, but Status and Scope were equally undefined in this repository. Defining only one dimension would leave the interpretation model incomplete.

### Copy the prior governance ADRs and lifecycle wholesale

Rejected.

The useful learning is the three-dimensional interpretation model. Importing repository-specific approval mechanics and ceremony would add controls without evidence that this repository needs them.

### Leave the fields as free-form prose

Rejected.

Free-form values would make comparison and interpretation dependent on inference, undermining the purpose of making the dimensions explicit.

## Evidence and traceability

- Issue #10 records the proposition and adoption boundary for this governance decision.
- `AGENTS.md` already requires Status, Scope and Decision strength to remain separate and is reconciled by the PR carrying this ADR.
- The reused model was shaped and exercised in prior governed architecture work; this ADR intentionally adopts the learning rather than reproducing that repository's full process.

This ADR becomes repository authority only when the pull request carrying it is reviewed and merged.
