# Commencer ici — BOIS:SIMA&BORIS v1.4.3

Paquet alpha public avec parité des langues de l’ONU et BORIS EGO v1.0.

Aucune langue d’accès public n’est préférée. L’ordre des langues dans les index sert seulement à la navigation et n’indique pas une priorité.

Chemin rapide : lire ce fichier, puis `QUICKSTART.md`, puis `USER_MANUAL_SHORT.md`. Pour l’usage complet, lire `USER_MANUAL_FULL.md` et `BORIS_EGO_LAYER.md`.

## Liens utilisateur essentiels

- Démarrage rapide: `QUICKSTART.md`
- Instructions utilisateur courtes: `USER_MANUAL_SHORT.md`
- Manuel utilisateur complet: `USER_MANUAL_FULL.md`
- Couche BORIS EGO: `BORIS_EGO_LAYER.md`
- Neutralité linguistique: `LANGUAGE_NEUTRALITY.md`

## BOIS/BORIS/SIMA/BORIS EGO

```text
BOIS/BORIS main v2.16 + SIMA v0.4 + BORIS EGO v1.0
```


## Commandes

```bash
python -m pip install -e .
python -m bois_sima_boris docs --lang fr
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris ego-status --lang fr
python -m bois_sima_boris self-check --root .
python -m pytest
```

Note : BORIS EGO v1.0 est actif par défaut comme partie du noyau ; aucune activation du mode 10 n’est requise.
