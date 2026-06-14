# Modèle de données et schémas

Archive alpha publique finale anonymisée

Ce paquet localisé fournit un analyseur SIMA local sans réseau et une documentation pour un usage BOIS/BORIS dirigé par l’humain. Il produit des reconstructions candidates, non une vérité finale ni une validation de terrain.

Un évaluateur humain doit définir le domaine, l’interface de valeurs, le risque acceptable et les conditions d’arrêt.

N’utilisez pas ce paquet alpha pour une gouvernance coercitive autonome, des décisions médicales/juridiques/financières/militaires ou un contrôle institutionnel caché.

Required top-level JSON keys: `object_id`, `object_type`, `domain`, `value_interface`, `substrate`, `observations`.

Required substrate fields: `units`, `channels`, `memory`, `costs`, `failure_modes`, `stop_authority`.

Required value-interface fields: `goals`, `constraints`, `forbidden_losses`.

Observation fields become opers: `trigger`, `distinction`, `evidence`, `carrier`, `authority`, `value_risk_gate`, `transformation`, `memory_write`, `closure_signal`, `transition_residue`, `cost`, `confidence`.
