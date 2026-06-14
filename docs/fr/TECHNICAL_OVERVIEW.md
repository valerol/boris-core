# Vue technique

Archive alpha publique finale anonymisée

Ce paquet localisé fournit un analyseur SIMA local sans réseau et une documentation pour un usage BOIS/BORIS dirigé par l’humain. Il produit des reconstructions candidates, non une vérité finale ni une validation de terrain.

Un évaluateur humain doit définir le domaine, l’interface de valeurs, le risque acceptable et les conditions d’arrêt.

N’utilisez pas ce paquet alpha pour une gouvernance coercitive autonome, des décisions médicales/juridiques/financières/militaires ou un contrôle institutionnel caché.

The package contains a small Python CLI with no runtime dependencies. It reads local JSON, validates required fields, maps observations into opers, builds an operome, and returns a candidate philosophical-machine map.

Runtime boundaries: no network, no shell execution, no dynamic code execution, no autonomous action.
