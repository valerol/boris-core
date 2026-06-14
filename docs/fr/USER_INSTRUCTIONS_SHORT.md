# Instructions utilisateur courtes

Ce fichier est une entrée explicite pour les instructions utilisateur courtes. Le texte opérationnel ci-dessous correspond à `USER_MANUAL_SHORT.md`.

# Démarrage rapide

Paquet public BOIS:SIMA&BORIS v1.4.3 avec parité stricte des langues de l’ONU et BORIS EGO v1.0.

Ce paquet fournit un analyseur SIMA local sans réseau et une documentation pour un usage BOIS/BORIS dirigé par l’humain. Les sorties sont des reconstructions candidates, non une vérité finale ni une validation de terrain.

Un évaluateur humain doit définir le domaine, l’interface de valeurs, le risque acceptable et les conditions d’arrêt.

N’utilisez pas ce paquet pour une gouvernance coercitive autonome, des décisions médicales/juridiques/financières/militaires ou un contrôle institutionnel caché.

## Parcours minimal

1. Décrivez l’objet dans un fichier JSON.
2. Validez le fichier.
3. Lancez l’analyse.
4. Lisez la machine candidate, les signaux de risque, l’opérome et les limites d’applicabilité.
5. Ne transformez pas la sortie en instructions locales avant un test d’expérience et une revue humaine.

## Commandes

```bash
python -m bois_sima_boris docs --lang fr
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```

## BORIS EGO et noyau actif

Utilisez `BORIS_EGO_LAYER.md` dans ce dossier comme noyau public actif de BORIS EGO v1.0. Chemin bref : lire ce fichier, lire `QUICKSTART.md`, exécuter `python -m bois_sima_boris docs --lang fr` et consulter `../../START_HERE_UN.md` pour l’accès linguistique égal.

Note : BORIS EGO v1.0 est actif par défaut comme partie du noyau ; aucune activation du mode 10 n’est requise.
