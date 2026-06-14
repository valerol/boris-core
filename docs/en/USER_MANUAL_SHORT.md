# Quick start

BOIS:SIMA&BORIS public package v1.4.3 with strict UN language parity and BORIS EGO v1.0.

This package provides a local-only, non-networked SIMA analyzer and documentation for human-led BOIS/BORIS use. Outputs are candidate reconstructions, not final truth and not field validation.

A human reviewer must set the domain, value interface, acceptable risk, and stop conditions.

Do not use this package for autonomous coercive governance, medical/legal/financial/military decisions, or hidden institutional control.

## Minimal workflow

1. Describe the object in a JSON file.
2. Validate the file.
3. Run analysis.
4. Read the candidate machine, risk flags, operome, and applicability limits.
5. Do not convert the output into local instructions before an experience test and human review.

## Commands

```bash
python -m bois_sima_boris docs --lang en
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```

## BORIS EGO and active core

Use `BORIS_EGO_LAYER.md` in this folder as the active public core for BORIS EGO v1.0. Short path: read this file, then `QUICKSTART.md`, run `python -m bois_sima_boris docs --lang en`, and check `../../START_HERE_UN.md` for equal language access.

Note: BORIS EGO v1.0 is active by default as part of the core; no Mode 10 activation is required.
