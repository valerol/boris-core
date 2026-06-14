# Instructions utilisateur complètes

Ce fichier est une entrée explicite pour les instructions utilisateur complètes. Le texte opérationnel ci-dessous correspond à `USER_MANUAL_FULL.md`.

# Manuel utilisateur complet

Paquet public BOIS:SIMA&BORIS v1.4.3 avec parité stricte des langues de l’ONU et BORIS EGO v1.0.

Ce paquet fournit un analyseur SIMA local sans réseau et une documentation pour un usage BOIS/BORIS dirigé par l’humain. Les sorties sont des reconstructions candidates, non une vérité finale ni une validation de terrain.

Un évaluateur humain doit définir le domaine, l’interface de valeurs, le risque acceptable et les conditions d’arrêt.

N’utilisez pas ce paquet pour une gouvernance coercitive autonome, des décisions médicales/juridiques/financières/militaires ou un contrôle institutionnel caché.

## Flux de travail

1. Définissez le domaine D et l’interface de valeurs V.
2. Déclarez le substrat S : unités, canaux, mémoire, coûts, modes de défaillance et autorité d’arrêt.
3. Ajoutez les observations comme opers : déclencheur, distinction, preuve, porteur, autorité, porte valeur/risque, transformation, écriture en mémoire, signal de clôture, résidu de transition, coût et confiance.
4. Lancez la validation et l’analyse.
5. Traitez M=<O,E,A,V,R,C,T> comme une reconstruction candidate.
6. Examinez les signaux de risque.
7. Lancez un test d’expérience avant de créer des instructions BORIS locales.
8. Conservez le chemin de retour arrière et les conditions d’arrêt.

## Commandes

```bash
python -m bois_sima_boris docs --lang fr
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```

## Noyau actif et parité linguistique

Le paquet complet prend en charge l’arabe, le chinois, l’anglais, le français, le russe et l’espagnol sans langue publique préférée. Utilisez `BORIS_EGO_LAYER.md` pour la couche EGO active et `../../core/ACTIVE_CORE_REFERENCE_v1_4_8.md` pour tous les miroirs du noyau.

## Limites d’usage

Ceci est un paquet public expérimental. Ne l’utilisez pas comme gouverneur indépendant, comme substitut aux experts de domaine, ni comme preuve de conscience machinique. Tout passage de l’analyse à l’instruction exige une revue humaine, des limites d’applicabilité et des signaux d’arrêt.
