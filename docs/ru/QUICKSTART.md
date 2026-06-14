# Краткий старт

Обезличенный финальный публичный alpha-архив

Этот локализованный пакет содержит локальный несетевой анализатор SIMA и документацию для BOIS/BORIS под управлением человека. Он выдаёт кандидатные реконструкции, а не окончательную истину и не полевую валидацию.

Человек-рецензент задаёт область, ценностный интерфейс, допустимый риск и стоп-условия.

Не используйте этот alpha-пакет для автономного принудительного управления, медицинских/юридических/финансовых/военных решений или скрытого управления институтами.

## Команды

```bash
python -m bois_sima_boris docs --lang ru
python -m bois_sima_boris ego-status
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```

Примечание: BORIS EGO v1.0 активен по умолчанию как часть ядра; активация Mode 10 [режима 10] не требуется.
