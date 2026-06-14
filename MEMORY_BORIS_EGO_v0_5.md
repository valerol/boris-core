# BOIS:SIMA&BORIS — memory file with BORIS EGO v0.6 and strict UN language parity

Type: LONG_TERM_MEMORY / RESTORE MEMORY FILE.
Fixed UTC: 2026-06-11T16:20:00Z.
Status: MEMORY FILE PRESENT.

## Active state

- BOIS/BORIS main: v2.12 — Core calculation control + strict UN language parity.
- SIMA: v0.4 — Design Risk Reduction.
- BORIS EGO: v0.6 — minimal EGO layer, Mode 10, rule edit boundaries, strict localized instruction completeness.
- Public release: v1.3.9 — UN Language Parity Strict / BORIS EGO v0.6.
- Previous public release: v1.3.7 — UN Language Parity / BORIS EGO v0.4.
- Next cycle counter: continue from active conversation counter.

## Active core

Use `core/ACTIVE_CORE_REFERENCE_v1_3_9.md`.
Active mirrors:

- `core/BORIS_EGO_LAYER_v0_6_AR.md`
- `core/BORIS_EGO_LAYER_v0_6_ZH.md`
- `core/BORIS_EGO_LAYER_v0_6_EN.md`
- `core/BORIS_EGO_LAYER_v0_6_FR.md`
- `core/BORIS_EGO_LAYER_v0_6_RU.md`
- `core/BORIS_EGO_LAYER_v0_6_ES.md`

## New/active rules

- BR-083 — UN Language Parity Rule: no natural language is preferred for public access.
- BR-084 — User Instruction Accessibility Rule: each UN language includes short/full user instructions and BORIS EGO user-facing core.
- BR-085 — Strict Localized Instruction Completeness Gate: non-English manuals must not retain core English workflow fragments.
- BR-086 — Language Neutral Entry Gate: root entry points route equally to all six UN languages.
- BR-087 — CLI Link Existence Gate: CLI documentation output must list only existing files.

## Verified repair

Defect found after v1.3.7 preparation: the audit result overstated completion because non-English short and full user manuals still retained English workflow fragments.

Repair in v1.3.9: rewritten `USER_MANUAL_SHORT.md` and `USER_MANUAL_FULL.md` for AR/ZH/FR/RU/ES; added `LANGUAGE_NEUTRALITY.md` in all six language folders; localized index section labels; updated active core mirrors to BORIS EGO v0.6; added strict tests for residual English workflow fragments and CLI link existence.

## Restore sequence

1. Load this memory file first.
2. Load `05_BOOTSTRAP_PROMPTS/RESTORE_PROMPT_BORIS_EGO_v0_6_RU.md` second.
3. Use `START_HERE_UN.md` for public user entry.
4. Use active core reference in Mode 10 and significant rule/release/package answers.
