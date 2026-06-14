# Instrucciones breves de usuario

Este archivo es una entrada explícita para instrucciones breves de usuario. El texto operativo siguiente coincide con `USER_MANUAL_SHORT.md`.

# Inicio rápido

Paquete público BOIS:SIMA&BORIS v1.4.3 con paridad estricta de idiomas de la ONU y BORIS EGO v1.0.

Este paquete proporciona un analizador SIMA local y sin red, más documentación para el uso humano de BOIS/BORIS. Las salidas son reconstrucciones candidatas, no verdad final ni validación de campo.

Una persona revisora debe definir el dominio, la interfaz de valores, el riesgo aceptable y las condiciones de parada.

No use este paquete para gobernanza coercitiva autónoma, decisiones médicas/jurídicas/financieras/militares ni control institucional oculto.

## Ruta mínima de trabajo

1. Describa el objeto en un archivo JSON.
2. Valide el archivo.
3. Ejecute el análisis.
4. Lea la máquina candidata, las señales de riesgo, el operoma y los límites de aplicabilidad.
5. No convierta la salida en instrucciones locales antes de una prueba de experiencia y una revisión humana.

## Comandos

```bash
python -m bois_sima_boris docs --lang es
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```

## BORIS EGO y núcleo activo

Use `BORIS_EGO_LAYER.md` en esta carpeta como núcleo público activo de BORIS EGO v1.0. Ruta breve: lea este archivo, lea `QUICKSTART.md`, ejecute `python -m bois_sima_boris docs --lang es` y revise `../../START_HERE_UN.md` para acceso lingüístico igual.

Nota: BORIS EGO v1.0 está activo por defecto como parte del núcleo; no se requiere activación del modo 10.
