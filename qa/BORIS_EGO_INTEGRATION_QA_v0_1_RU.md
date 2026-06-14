# QA report — BORIS EGO v0.1 integration

Fixed UTC: 2026-06-11T14:50:00Z.

## Tests performed

1. Structural insertion check: BORIS EGO files added to `core/`, `docs/ru/`, and `docs/en/`.
2. Rule-map check: `RULE_MAP_PUBLIC_v1_3_4.md` and `.json` added.
3. Boundary check: public-alpha non-autonomous boundary preserved.
4. Ethics check: basic EGO ethical constraints are marked as pre-reasoning constraints and non-editable by BORIS EGO.
5. Minimal-physiology check: layer physiology is limited to ethics gate, counters, active-core reference, version/change note, rollback note, and return-to-BOIS-Core rule.
6. Mode 10 check: activation command, 10-answer counter, active-core reference, final extension offer, early stop, and versioning on changes are specified.

## Result

Passed for document-level integration.

## Limitation

This is not field validation and not proof that every downstream user or model will follow the layer correctly. Runtime conformance still requires self-checking and operator review.
