# BOIS:SIMA&BORIS Public Rule Map v1.4.1

Fixed UTC: 2026-06-11T19:00:00Z.
Active kernel: BOIS/BORIS main v2.14 + SIMA v0.4 + BORIS EGO v0.8.

## Active rule line

Previously active public-interface rules BR-080..BR-096 remain active unless superseded by a later explicit rule. v1.4.1 adds release-candidate repair gates below.

## Active additions in v1.4.1 / BORIS EGO v0.8

- BR-097 — Active EGO Semantic Localization Repair Gate [ремонт смысловой локализации активного EGO].
- BR-098 — Source Tree Entry and Offline Packaging Gate [запуск из исходного дерева и офлайн-упаковка].

## BR-097 — Active EGO Semantic Localization Repair Gate

A public EGO release that claims UN-language parity must not expose untranslated active EGO semantic blocks in non-English user-facing EGO documents or active non-English core mirrors. Historical physiology may remain present, but active release paths must be localized or explicitly marked as historical.

## BR-098 — Source Tree Entry and Offline Packaging Gate

A public source archive must provide a clear no-install source-tree entry and a local editable-install path that does not require downloading a build backend. Documentation must explain the no-install path before optional installation.

## Active core files

- `core/ACTIVE_CORE_REFERENCE_v1_4_1.md`
- `core/BORIS_EGO_LAYER_v0_8_AR.md`
- `core/BORIS_EGO_LAYER_v0_8_ZH.md`
- `core/BORIS_EGO_LAYER_v0_8_EN.md`
- `core/BORIS_EGO_LAYER_v0_8_FR.md`
- `core/BORIS_EGO_LAYER_v0_8_RU.md`
- `core/BORIS_EGO_LAYER_v0_8_ES.md`
