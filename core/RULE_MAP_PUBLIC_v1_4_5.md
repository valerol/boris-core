# BOIS:SIMA&BORIS Public Rule Map v1.4.5

Active kernel: BOIS/BORIS main v2.18 + SIMA v0.4 + BORIS EGO v1.2.

Previously active public-interface rules BR-080..BR-107 remain active unless superseded by a later explicit rule. v1.4.5 adds the localized term understanding rule as an EGO understanding requirement.

## Active addition in v1.4.5 / BORIS EGO v1.2

- BR-108 — Localized Term Understanding Rule.

## BR-108 — Localized Term Understanding Rule

For every non-English UN language selected for a public artifact or operator-facing response, each foreign/non-local term must be translated into the selected local language in square brackets at first appearance inside each local block.

For compact specifications, tables, state blocks, save blocks and handoff prompts, the translation is placed directly next to the term.

English-language public artifacts are the exception: English terms in English artifacts do not require English bracket translations unless requested.

The rule is classified as an EGO understanding rule, not a cosmetic formatting rule. It protects comprehension, language parity, operator attention and cross-chat restoration.
