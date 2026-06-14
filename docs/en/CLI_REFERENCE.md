# CLI reference

Anonymized final public alpha archive

This localized package provides a local-only, non-networked SIMA analyzer and documentation for human-led BOIS/BORIS use. It produces candidate reconstructions, not final truth or field validation.

A human reviewer must set domain, value interface, acceptable risk, and stop conditions.

Do not use this alpha package for autonomous coercive governance, medical/legal/financial/military decisions, or hidden institutional control.

## Commands

```bash
python -m bois_sima_boris docs --lang en
python -m bois_sima_boris ego-status
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```
