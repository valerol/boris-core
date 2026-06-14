# Active core reference — BOIS:SIMA&BORIS v1.3.9 / BORIS EGO v0.6

Fixed UTC: 2026-06-11T17:00:00Z.

Active kernel:

```text
BOIS/BORIS main v2.12 + SIMA v0.4 + BORIS EGO v0.6
```

UN-language active public-core mirrors:

- Arabic / العربية: `core/BORIS_EGO_LAYER_v0_6_AR.md`
- Chinese / 中文: `core/BORIS_EGO_LAYER_v0_6_ZH.md`
- English: `core/BORIS_EGO_LAYER_v0_6_EN.md`
- French / Français: `core/BORIS_EGO_LAYER_v0_6_FR.md`
- Russian / Русский: `core/BORIS_EGO_LAYER_v0_6_RU.md`
- Spanish / Español: `core/BORIS_EGO_LAYER_v0_6_ES.md`

No natural language is preferred. The order above follows a conventional UN official-language listing and does not indicate priority. Semantic conflicts are resolved through BOIS invariants, rule maps, explicit operator intent, applicability limits, tests, and rollback paths.

Rule map:

```text
core/RULE_MAP_PUBLIC_v1_3_9.md
core/RULE_MAP_PUBLIC_v1_3_9.json
```

Release-readiness additions in v1.3.9 / BORIS EGO v0.6:

- explicit short/full `USER_INSTRUCTIONS_*` aliases in every UN language;
- clean public artifact hygiene gate: no `.pytest_cache` or `__pycache__` in release archives;
- resolvable historical EGO rule-map links;
- release-readiness audit report and machine-readable result;
- transition package aligned with active memory and restore prompt.

Operational rule: in Mode 10 every answer must include the active-core reference. In standard mode, significant rule/release/package answers should include it.
