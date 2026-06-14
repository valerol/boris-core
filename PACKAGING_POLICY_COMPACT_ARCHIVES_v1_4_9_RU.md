# Packaging policy [политика упаковки] v1.4.10

## Summary [сводка]

Public Release [публичный релиз] and Full Actual Compact [полная актуальная компактная версия] are separate archive roles [роли архивов]. The working full archive [рабочий полный архив] must not become a container of old full containers [контейнером старых полных контейнеров].

## Applied methods [применённые методы]

```text
Method 3 [метод 3] — manifest-only history [история только через манифест].
Method 6 [метод 6] — canonical-copy rule [правило единственной канонической копии].
Method 7 [метод 7] — archive role separation [разделение ролей архивов].
```

## Public Release [публичный релиз]

Purpose [назначение]: public code [публичный код], documentation [документация], tests [тесты], legal text content [юридическое текстовое содержание], and usable experience changes [изменения по доступному опыту использования].

## Full Actual Compact [полная актуальная компактная версия]

Purpose [назначение]: user restoration [восстановление пользователем], memory continuity [преемственность памяти], legal package [юридический комплект], transition resources [переходные ресурсы], verification reports [отчёты проверки], and history manifest [манифест истории] without embedding old full binary archives [без вложения старых полных бинарных архивов].

## Historical versions [исторические версии]

Historical versions [исторические версии] are preserved locally [локально] and in chat histories [историях чатов]. The working archive [рабочий архив] stores:

```text
file name [имя файла];
role [роль];
size [размер];
SHA-256 checksum [контрольная сумма SHA-256];
digest card [карточка-сводка];
reason for exclusion [причина невключения];
where the binary history is expected to live [где ожидается хранение бинарной истории].
```

## Size gate [ворота размера]

```text
Target [цель]: < 50 MB [мегабайт]
Hard cap [жёсткий потолок]: < 200 MB [мегабайт]
Fail condition [условие ошибки]: old full binary ZIP archive [старый полный бинарный архив ZIP] embedded in Full Actual Compact [полную актуальную компактную версию]
```
