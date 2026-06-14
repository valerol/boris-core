# Pruebas y autopruebas

Archivo público candidato a publicación

Use solo pruebas locales. Verifican estructura, documentación, comportamiento CLI, acceso lingüístico, límites de EGO, limpieza del archivo y sumas de control. No prueban fiabilidad de campo ni conciencia de máquina.

Comandos:

```bash
python -m pytest
python -m bois_sima_boris self-check --root .
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
```

Grupos de prueba: coherencia filosófica, lógica, estructura de opers, estructura del archivo, localización, base de seguridad, comportamiento bajo carga, higiene de publicación, integración EGO y compatibilidad con la fisiología desarrollada.
