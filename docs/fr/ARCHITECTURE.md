# Architecture

Archive alpha publique finale anonymisée

Ce paquet localisé fournit un analyseur SIMA local sans réseau et une documentation pour un usage BOIS/BORIS dirigé par l’humain. Il produit des reconstructions candidates, non une vérité finale ni une validation de terrain.

Un évaluateur humain doit définir le domaine, l’interface de valeurs, le risque acceptable et les conditions d’arrêt.

N’utilisez pas ce paquet alpha pour une gouvernance coercitive autonome, des décisions médicales/juridiques/financières/militaires ou un contrôle institutionnel caché.

Layer map:

- BOIS: grammar for incomplete knowledge, protocols, instructions, experience, physiology, and attention.
- SIMA: analytic layer for candidate reconstruction from substrate and observed opers.
- BORIS: human-led implementation layer for a specific domain.
- Tests: validation, self-check, stress cases, risk gates, and rollback.

Data flow: JSON object -> validation -> opers -> operome -> candidate M=<O,E,A,V,R,C,T> -> limits and next step.
