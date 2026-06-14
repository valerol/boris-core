# Installation

## Installation et lancement sans installation

1. Installez Python 3.9 ou plus récent.
2. Décompressez le paquet.
3. Vous pouvez lancer directement avant installation :

```bash
python -m bois_sima_boris docs --lang fr
python -m bois_sima_boris ego-status
```

4. Installation locale modifiable facultative :

```bash
python -m pip install --no-index -e .
```

Le paquet contient un mécanisme local de construction sans dépendance externe pour ce chemin d’installation hors ligne.

## Commandes communes

```bash
python -m bois_sima_boris docs --lang fr
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```
