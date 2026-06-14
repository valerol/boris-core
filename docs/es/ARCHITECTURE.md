# Arquitectura

Archivo alfa público final anonimizado

Este paquete localizado proporciona un analizador SIMA local y sin red, más documentación para el uso humano de BOIS/BORIS. Produce reconstrucciones candidatas, no verdad final ni validación de campo.

Una persona revisora debe definir dominio, interfaz de valores, riesgo aceptable y condiciones de parada.

No use este paquete alfa para gobernanza coercitiva autónoma, decisiones médicas/jurídicas/financieras/militares ni control institucional oculto.

Layer map:

- BOIS: grammar for incomplete knowledge, protocols, instructions, experience, physiology, and attention.
- SIMA: analytic layer for candidate reconstruction from substrate and observed opers.
- BORIS: human-led implementation layer for a specific domain.
- Tests: validation, self-check, stress cases, risk gates, and rollback.

Data flow: JSON object -> validation -> opers -> operome -> candidate M=<O,E,A,V,R,C,T> -> limits and next step.
