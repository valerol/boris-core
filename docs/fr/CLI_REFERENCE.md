# Référence CLI

Archive alpha publique finale anonymisée

Ce paquet localisé fournit un analyseur SIMA local sans réseau et une documentation pour un usage BOIS/BORIS dirigé par l’humain. Il produit des reconstructions candidates, non une vérité finale ni une validation de terrain.

Un évaluateur humain doit définir le domaine, l’interface de valeurs, le risque acceptable et les conditions d’arrêt.

N’utilisez pas ce paquet alpha pour une gouvernance coercitive autonome, des décisions médicales/juridiques/financières/militaires ou un contrôle institutionnel caché.

## Commandes

```bash
python -m bois_sima_boris docs --lang fr
python -m bois_sima_boris ego-status
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```
