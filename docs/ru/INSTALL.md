# Установка

## Установка и запуск без установки

1. Установите Python 3.9 или новее.
2. Распакуйте пакет.
3. Можно запускать напрямую до установки:

```bash
python -m bois_sima_boris docs --lang ru
python -m bois_sima_boris ego-status
```

4. Необязательная локальная установка в редактируемом режиме:

```bash
python -m pip install --no-index -e .
```

Пакет содержит локальный сборочный механизм без внешних зависимостей для этого офлайн-пути установки.

## Общие команды

```bash
python -m bois_sima_boris docs --lang ru
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```
