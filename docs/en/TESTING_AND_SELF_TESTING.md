# Testing and self-testing

Public release-candidate archive

Use only local tests. They verify structure, documentation, CLI behavior, language access, EGO boundaries, archive hygiene and checksums. They do not prove field reliability or machine consciousness.

Commands:

```bash
python -m pytest
python -m bois_sima_boris self-check --root .
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
```

Test groups: philosophical consistency, logic, oper structure, archive structure, localization, security baseline, stress behavior, release hygiene, EGO integration and developed-physiology compatibility.
