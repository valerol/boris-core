# Data model and schemas

Anonymized final public alpha archive

This localized package provides a local-only, non-networked SIMA analyzer and documentation for human-led BOIS/BORIS use. It produces candidate reconstructions, not final truth or field validation.

A human reviewer must set domain, value interface, acceptable risk, and stop conditions.

Do not use this alpha package for autonomous coercive governance, medical/legal/financial/military decisions, or hidden institutional control.

Required top-level JSON keys: `object_id`, `object_type`, `domain`, `value_interface`, `substrate`, `observations`.

Required substrate fields: `units`, `channels`, `memory`, `costs`, `failure_modes`, `stop_authority`.

Required value-interface fields: `goals`, `constraints`, `forbidden_losses`.

Observation fields become opers: `trigger`, `distinction`, `evidence`, `carrier`, `authority`, `value_risk_gate`, `transformation`, `memory_write`, `closure_signal`, `transition_residue`, `cost`, `confidence`.
