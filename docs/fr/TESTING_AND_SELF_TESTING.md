# Tests et auto-tests

Archive publique candidate à la publication

Utilisez seulement des tests locaux. Ils vérifient la structure, la documentation, le comportement CLI, l’accès linguistique, les limites EGO, la propreté de l’archive et les sommes de contrôle. Ils ne prouvent ni la fiabilité de terrain ni la conscience d’une machine.

Commandes :

```bash
python -m pytest
python -m bois_sima_boris self-check --root .
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
```

Groupes de tests : cohérence philosophique, logique, structure des opers, structure d’archive, localisation, base de sécurité, comportement sous charge, hygiène de publication, intégration EGO et compatibilité avec la physiologie développée.
