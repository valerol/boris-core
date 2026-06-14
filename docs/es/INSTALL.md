# Instalación

## Instalación y ejecución sin instalar

1. Instale Python 3.9 o posterior.
2. Descomprima el paquete.
3. Puede ejecutar directamente antes de instalar:

```bash
python -m bois_sima_boris docs --lang es
python -m bois_sima_boris ego-status
```

4. Instalación local editable opcional:

```bash
python -m pip install --no-index -e .
```

El paquete incluye un mecanismo local de construcción sin dependencias externas para esta ruta de instalación sin conexión.

## Comandos comunes

```bash
python -m bois_sima_boris docs --lang es
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```
