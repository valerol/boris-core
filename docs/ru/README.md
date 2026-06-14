# Начните здесь — BOIS:SIMA&BORIS v1.4.3

Публичный alpha-пакет с языковым паритетом ООН и BORIS EGO v1.0.

Ни один язык публичного доступа не является предпочтительным. Порядок языков в индексах фиксирован только для навигации и не означает приоритет.

Быстрый путь: прочитать этот файл, затем `QUICKSTART.md`, затем `USER_MANUAL_SHORT.md`. Для полного использования прочитать `USER_MANUAL_FULL.md` и `BORIS_EGO_LAYER.md`.

## Основные пользовательские ссылки

- Краткий старт: `QUICKSTART.md`
- Краткая пользовательская инструкция: `USER_MANUAL_SHORT.md`
- Полный пользовательский мануал: `USER_MANUAL_FULL.md`
- Слой BORIS EGO: `BORIS_EGO_LAYER.md`
- Языковая нейтральность: `LANGUAGE_NEUTRALITY.md`

## BOIS/BORIS/SIMA/BORIS EGO

```text
BOIS/BORIS main v2.16 + SIMA v0.4 + BORIS EGO v1.0
```


## Команды

```bash
python -m pip install -e .
python -m bois_sima_boris docs --lang ru
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris ego-status --lang ru
python -m bois_sima_boris self-check --root .
python -m pytest
```

Примечание: BORIS EGO v1.0 активен по умолчанию как часть ядра; активация Mode 10 [режима 10] не требуется.
