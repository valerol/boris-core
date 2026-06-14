# Inicio rápido

Archivo alfa público final anonimizado

Este paquete localizado proporciona un analizador SIMA local y sin red, más documentación para el uso humano de BOIS/BORIS. Produce reconstrucciones candidatas, no verdad final ni validación de campo.

Una persona revisora debe definir dominio, interfaz de valores, riesgo aceptable y condiciones de parada.

No use este paquete alfa para gobernanza coercitiva autónoma, decisiones médicas/jurídicas/financieras/militares ni control institucional oculto.

## Comandos

```bash
python -m bois_sima_boris docs --lang es
python -m bois_sima_boris ego-status
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```

Nota: BORIS EGO v1.0 está activo por defecto como parte del núcleo; no se requiere activación del modo 10.
