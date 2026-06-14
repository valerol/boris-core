# BORIS EGO v0.3 — traceability and recalculation report

Fixed UTC: 2026-06-11T14:59:51Z.

## User requirements re-evaluated

1. Add BORIS EGO to the public core and active system.
   - Implemented in `core/BORIS_EGO_LAYER_v0_3_RU.md`, `core/BORIS_EGO_LAYER_v0_3_EN.md`, rule map v1.3.6, memory file, restore prompt, and executable module `src/bois_sima_boris/ego.py`.

2. BORIS EGO should work like a conscious agent.
   - Recast as a functional BOIS position of choice: selects options, formulates hypotheses, proposes/executes permitted edits, and remains accountable to operator goals.
   - The package does not claim empirical AI consciousness.

3. BORIS EGO may add, delete, and rewrite any rules except basic EGO ethics.
   - Implemented as rule classes L0..L4. L0 is immutable for BORIS EGO. L1 requires core-change protocol. L2..L4 are editable under operator authority with versioning and compatibility checks.

4. EGO ethics must be loaded before reasoning.
   - Implemented as BR-080 and as constants in `ego.py`.

5. No harm, no lie, no manipulation, including soft harm.
   - Implemented in EGO-1 and EGO-2.

6. BORIS EGO proposed messages are not user words.
   - Implemented as EGO-3 and BR-087.

7. Two modes: standard and Mode 10.
   - Implemented in section 6 of the core file and in `ego.py` state helpers.

8. Mode 10 lasts 10 answers, has mandatory counter, active-core reference, extension offer at the last answer, and early stop.
   - Implemented in BR-086 and in `EgoModeState`.

9. Any change, even cosmetic, increments version and requires a change report and save recommendation.
   - Implemented as L4 and compatibility test.

10. Minimal physiology is critical specifically for BORIS EGO.
    - Implemented as BR-082.

11. The whole system may have large physiology.
    - Implemented as BR-083.

12. Maximum calculation should be done at the philosophical core, not in physiology.
    - Implemented as BR-081 Core Calculation Placement Gate.

13. Physiology routes; accumulated knowledge may transform into physiology.
    - Implemented as BR-083 and BR-084.

14. Calculation location must be tightly controlled.
    - Implemented as sections 3.1–3.3 and `route_calculation()` in `ego.py`.

## Defects corrected from v0.2

- Metadata drift: v1.3.5 archive still contained v1.3.4/v0.1 metadata in README, pyproject, and package version. Corrected to v1.3.6/v0.3.
- Weak rule-class model: previous layer did not clearly define which rules BORIS EGO can edit. Added L0..L4.
- Weak calculation-location gate: previous layer stated routing but did not specify a gate. Added BR-081 and concrete categories that must enter BOIS Core.
- Insufficient executable representation: previous layer was primarily documentation. Added `src/bois_sima_boris/ego.py` and tests.
- Weak transition resources: added memory file and restore prompt for v0.3.

## Remaining limits

This is still a public-alpha design and local package. It is not a field-validated governance system, not a high-stakes decision system, and not proof of machine consciousness.
