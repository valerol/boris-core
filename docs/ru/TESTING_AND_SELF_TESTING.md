# Тесты и самотесты

Публичный архив релизного кандидата

Используйте только локальные тесты. Они проверяют структуру, документацию, поведение CLI, языковой доступ, границы EGO, чистоту архива и контрольные суммы. Они не доказывают полевую надёжность и не доказывают сознание машины.

Команды:

```bash
python -m pytest
python -m bois_sima_boris self-check --root .
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
```

Группы тестов: философская согласованность, логика, структура opers, структура архива, локализация, базовая безопасность, стресс-поведение, релизная гигиена, интеграция EGO и совместимость с развитой физиологией.
