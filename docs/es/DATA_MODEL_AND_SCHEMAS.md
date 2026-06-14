# Modelo de datos y esquemas

Archivo alfa público final anonimizado

Este paquete localizado proporciona un analizador SIMA local y sin red, más documentación para el uso humano de BOIS/BORIS. Produce reconstrucciones candidatas, no verdad final ni validación de campo.

Una persona revisora debe definir dominio, interfaz de valores, riesgo aceptable y condiciones de parada.

No use este paquete alfa para gobernanza coercitiva autónoma, decisiones médicas/jurídicas/financieras/militares ni control institucional oculto.

Required top-level JSON keys: `object_id`, `object_type`, `domain`, `value_interface`, `substrate`, `observations`.

Required substrate fields: `units`, `channels`, `memory`, `costs`, `failure_modes`, `stop_authority`.

Required value-interface fields: `goals`, `constraints`, `forbidden_losses`.

Observation fields become opers: `trigger`, `distinction`, `evidence`, `carrier`, `authority`, `value_risk_gate`, `transformation`, `memory_write`, `closure_signal`, `transition_residue`, `cost`, `confidence`.
