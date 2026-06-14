# Full user manual

BOIS:SIMA&BORIS public package v1.4.3 with strict UN language parity and BORIS EGO v1.0.

This package provides a local-only, non-networked SIMA analyzer and documentation for human-led BOIS/BORIS use. Outputs are candidate reconstructions, not final truth and not field validation.

A human reviewer must set the domain, value interface, acceptable risk, and stop conditions.

Do not use this package for autonomous coercive governance, medical/legal/financial/military decisions, or hidden institutional control.

## Workflow

1. Define domain D and value interface V.
2. Declare substrate S: units, channels, memory, costs, failure modes, and stop authority.
3. Add observations as opers: trigger, distinction, evidence, carrier, authority, value/risk gate, transformation, memory write, closure signal, transition residue, cost, and confidence.
4. Run validation and analysis.
5. Treat M=<O,E,A,V,R,C,T> as a candidate reconstruction.
6. Review risk flags.
7. Run an experience test before creating local BORIS instructions.
8. Preserve rollback path and stop conditions.

## Commands

```bash
python -m bois_sima_boris docs --lang en
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```

## Active core and language parity

The full package supports Arabic, Chinese, English, French, Russian, and Spanish without a preferred public language. Use `BORIS_EGO_LAYER.md` for the active EGO layer and `../../core/ACTIVE_CORE_REFERENCE_v1_4_8.md` for all core mirrors.

## Use boundaries

This is a public experimental package. Do not use it as an independent governor, a substitute for domain experts, or proof of machine consciousness. Every transition from analysis to instruction requires human review, applicability limits, and stop signals.
