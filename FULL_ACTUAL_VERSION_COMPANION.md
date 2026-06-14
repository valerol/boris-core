# PUBLIC_RELEASE [публичный релиз] + FULL_ACTUAL_COMPACT [полная актуальная компактная версия] v1.4.10

## Purpose [назначение]

This public line [публичная линия] now provides two companion artifacts [сопровождающих артефакта]:

```text
1. PUBLIC_RELEASE [публичный релиз]
   open-publication archive [архив для открытой публикации] and code-registration baseline [база для регистрации кода].

2. FULL_ACTUAL_COMPACT [полная актуальная компактная версия]
   user-continuity archive [архив пользовательской преемственности] with active memory [активной памятью], restore resources [ресурсами восстановления], legal bundle [юридическим комплектом], QA [проверкой качества], and manifest-only history [историей только через манифест].
```

Historical versions [исторические версии] are not embedded as binary ZIP archives [бинарные архивы ZIP] inside FULL_ACTUAL_COMPACT [полную актуальную компактную версию]. They remain local [локальными] and in chat histories [историях чатов], while the working archive stores digest cards [карточки-сводки], SHA-256 [контрольные суммы SHA-256], sizes [размеры], roles [роли], and storage notes [заметки о хранении].

## Size policy [политика размера]

```text
Target [цель]: < 50 MB [МБ]
Warning [предупреждение]: > 100 MB [МБ]
Hard ceiling [жёсткий потолок]: 200 MB [МБ]
```

## Operator-facing rule [правило для оператора]

After each public release [публичный релиз] change, provide both:

```text
- updated PUBLIC_RELEASE [публичный релиз];
- updated FULL_ACTUAL_COMPACT [полная актуальная компактная версия].
```
