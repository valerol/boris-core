# FINAL PROGRAM TEXT PACKAGE RELEASE VERIFICATION [финальная проверка пакета текста программы] v1.4.10

## Active state [активное состояние]

BOIS [бизнес-операционная интеллектуальная система] / BORIS [рациональная операционно-интеллектуальная система бизнеса] main [основная линия] v2.23 + SIMA [Substrate-Independent Machine Analyzer / субстрато-независимый машинный анализатор] v0.4 + BORIS EGO [Ethical Goal Orchestrator / этический оркестратор производных целей] v1.7.

Public Release [публичный релиз]: v1.4.10.

## Defects fixed [исправленные дефекты]

1. Public Release [публичный релиз] v1.4.8 did not provide PROGRAM_TEXT_PACKAGE [пакет текста программы]. v1.4.10 embeds it in `legal/program_text/` and provides a separate sidecar ZIP [сопровождающий ZIP-архив].
2. The staging legal companion Markdown [сопровождающий юридический файл Markdown] had stale SHA-256 [устаревшие контрольные суммы SHA-256]. v1.4.10 adds BR-118 [правило BR-118] and a regression test [регрессионный тест] verifying listed hashes against actual files.

## Checks [проверки]

- Work-tree pytest [автоматические тесты рабочего дерева]: 104 passed [104 теста пройдено].
- Packaged pytest [автоматические тесты упакованного релиза]: 104 passed [104 теста пройдено].
- self-check [самопроверка]: ok=true [успешно].
- docs --lang ru [документы на русском языке]: PASS [пройдено].
- offline editable install --no-index [офлайн-установка в редактируемом режиме без индекса]: PASS [пройдено].
- ego-status [статус EGO]: v1.4.10 / v2.23 / v1.7.
- Legal companion hash check [проверка контрольных сумм юридического сопровождающего документа]: PASS [пройдено] through `tests/test_program_text_companion_integrity_v1410.py`.
- DOCX render [рендер DOCX]: program text package [пакет текста программы] rendered to 16 pages [16 страниц]; legal companion [юридический сопровождающий документ] rendered to 2 pages [2 страницы]; visual contact sheets [контактные листы] inspected [проверены].

## Limits [ограничения]

No legal review [юридическая экспертиза], native-speaker certification [сертификация носителями языков], penetration test [тест на проникновение] or field validation [полевая проверка] was performed. Attorney / claimant [адвокат / заявитель] selects the final deposit copy [депозитную копию].
