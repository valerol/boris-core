# BOIS:SIMA&BORIS Public Rule Map v1.3.9

Fixed UTC: 2026-06-11T16:20:00Z.
Active kernel: BOIS/BORIS main v2.12 + SIMA v0.4 + BORIS EGO v0.6.

## Active additions since v1.3.6

- BR-080 — Core Calculation Placement Gate [ворота размещения расчёта в ядре].
- BR-081 — BORIS EGO Minimal Physiology Rule [минимальная физиология BORIS EGO].
- BR-082 — Knowledge-to-Physiology Transform Rule [превращение проверенного знания в физиологию].
- BR-083 — UN Language Parity Rule [языковой паритет шести официальных языков ООН].
- BR-084 — User Instruction Accessibility Rule [легкодоступные краткие и полные пользовательские инструкции].
- BR-085 — Strict Localized Instruction Completeness Gate [строгая полнота локализованных инструкций].
- BR-086 — Language Neutral Entry Gate [нейтральный языковой вход].
- BR-087 — CLI Link Existence Gate [CLI не должен показывать несуществующие пользовательские файлы].

## BR-083 — UN Language Parity Rule

Public user-facing materials must be available in Arabic, Chinese, English, French, Russian, and Spanish without declaring any natural language as preferred for public access. Ordering, source history, or file naming does not create language priority.

## BR-084 — User Instruction Accessibility Rule

Each public language must provide at minimum `INDEX.md`, `QUICKSTART.md`, `USER_MANUAL_SHORT.md`, `USER_MANUAL_FULL.md`, `LANGUAGE_NEUTRALITY.md`, `RESPONSIBLE_USE.md`, `RELEASE_BOUNDARIES.md`, `FAQ.md`, and `BORIS_EGO_LAYER.md`. The CLI documentation index must not list a localized file unless it exists.

## BR-085 — Strict Localized Instruction Completeness Gate

Short and full user instructions must be directly understandable in the selected public language. Non-English manuals must not retain core English workflow sentences such as “Minimal workflow”, “Describe an object”, “Validate it”, “Analyze it”, “Define domain”, “Run validation”, “Review risk flags”, or “Preserve rollback” outside command blocks or technical names.

## BR-086 — Language Neutral Entry Gate

The root public entry must direct users equally to all six UN languages and must not present one natural language as the normative user path. A source/canonical language for article provenance is not a preferred user language.

## BR-087 — CLI Link Existence Gate

Every localized file printed by `python -m bois_sima_boris docs --lang <code>` must exist in the archive. Tests must check link existence rather than only command exit status.

## Active core files

- `core/ACTIVE_CORE_REFERENCE_v1_3_9.md`
- `core/BORIS_EGO_LAYER_v0_6_AR.md`
- `core/BORIS_EGO_LAYER_v0_6_ZH.md`
- `core/BORIS_EGO_LAYER_v0_6_EN.md`
- `core/BORIS_EGO_LAYER_v0_6_FR.md`
- `core/BORIS_EGO_LAYER_v0_6_RU.md`
- `core/BORIS_EGO_LAYER_v0_6_ES.md`
