# RULE MAP PUBLIC [публичная карта правил] v1.4.10

Active kernel [активное ядро]: BOIS [бизнес-операционная интеллектуальная система] / BORIS [рациональная операционно-интеллектуальная система бизнеса] main [основная линия] v2.23 + SIMA [Substrate-Independent Machine Analyzer / субстрато-независимый машинный анализатор] v0.4 + BORIS EGO [Ethical Goal Orchestrator / этический оркестратор производных целей] v1.7.

Active core [активное ядро]: `core/ACTIVE_CORE_REFERENCE_v1_4_10.md`.

## Active additions [активные добавления]

- BR-113 — Manifest-Only History Reference Rule [правило ссылочной истории только через манифест].
- BR-114 — Canonical Copy Packaging Rule [правило упаковки с единственной канонической копией].
- BR-115 — Archive Role Separation Rule [правило разделения ролей архивов].
- BR-116 — Public Release + Full Actual Companion Rule [правило пары публичного релиза и полной актуальной версии].

## BR-113 — Manifest-Only History Reference Rule [правило ссылочной истории только через манифест]

Historical versions [исторические версии] are not physically nested [не вкладываются физически] inside FULL_ACTUAL_COMPACT [полной актуальной компактной версии]. The compact archive [компактный архив] keeps manifest [манифест], digest card [карточку-сводку], size [размер] and SHA-256 [контрольную сумму SHA-256] when available.

## BR-114 — Canonical Copy Packaging Rule [правило упаковки с единственной канонической копией]

Each artifact class [класс артефакта] has one canonical physical copy [единственную каноническую физическую копию]. Other locations use manifest references [ссылки в манифесте], not duplicated binary payloads [дублированные бинарные данные].

## BR-115 — Archive Role Separation Rule [правило разделения ролей архивов]

Active roles [активные роли] are:

```text
PUBLIC_RELEASE [публичный релиз]
FULL_ACTUAL_COMPACT [полная актуальная компактная версия]
```

PUBLIC_RELEASE [публичный релиз] is for open publication [открытая публикация]. FULL_ACTUAL_COMPACT [полная актуальная компактная версия] is for operator recovery [восстановление оператором], memory continuity [преемственность памяти] and legal/QA continuity [юридическая и проверочная преемственность].

## BR-116 — Public Release + Full Actual Companion Rule [правило пары публичного релиза и полной актуальной версии]

Every new public release [публичный релиз] produced from usage experience [опыта использования] should be accompanied by a separate FULL_ACTUAL_COMPACT [полная актуальная компактная версия] for the user. Asking for confirmation merely to provide the companion artifact [сопровождающий артефакт] after authorized changes is attention theft [кража внимания].

## Size gate [ворота размера]

```text
FULL_ACTUAL_COMPACT target [цель]: < 50 MB [МБ]
FULL_ACTUAL_COMPACT hard limit [жёсткий предел]: 200 MB [МБ]
Nested old full binary archives [вложенные старые полные бинарные архивы]: forbidden [запрещены]
```

- Canonical Single-Copy Rule [регрессионный маркер].

- Compact Full Actual Size Gate Rule [регрессионный маркер].


Release Evidence Source Priority Rule [правило приоритета источников релизного доказательства].


at every occurrence [при каждом появлении].


Changelog Hygiene and Deduplication Rule [служебная строка регрессионной проверки].

- Manifest-Only Historical Continuity Rule [регрессионный маркер].


Changelog Hygiene and Deduplication Rule [правило гигиены и дедупликации журнала изменений].


## BR-117 — Program Text Package Companion Rule [правило сопровождения пакетом текста программы]

Every Public Release [публичный релиз] must be accompanied by PROGRAM_TEXT_PACKAGE [пакет текста программы] as embedded `legal/program_text/` artifacts and as a separate sidecar ZIP [сопровождающий ZIP-архив].
