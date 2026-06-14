# ARCHIVE_PACKAGING_POLICY [archive packaging policy] v1.4.8

## Summary [краткий итог]

BOIS [бизнес-операционная интеллектуальная система] accepts Method 3 [метод 3], Method 6 [метод 6] and Method 7 [метод 7] as active packaging physiology [активная упаковочная физиология].

## Rules [правила]

1. Manifest-only history [история только через манифест]: старые full ZIP archives [полные архивы ZIP] не вкладываются в working full actual archive [рабочий полный актуальный архив].
2. Canonical copy [каноническая копия]: один активный файл — одна физическая копия; повторения заменяются manifest references [ссылками в манифесте].
3. Artifact type separation [разделение типов артефактов]: Public Release [публичный релиз] и Full Actual Compact [полная актуальная компактная версия] имеют разные назначения.
4. Size gate [ворота размера]: Full Actual Compact [полная актуальная компактная версия] должна быть меньше 200 MB [200 мегабайт], target [цель] — меньше 50 MB [50 мегабайт].

## Preservation [сохранение]

Historical versions [исторические версии] сохраняются locally [локально] и in chat histories [в историях чатов]. Working archive [рабочий архив] хранит SHA-256 [контрольные суммы SHA-256], sizes [размеры], roles [роли] and digest cards [карточки-сводки].
