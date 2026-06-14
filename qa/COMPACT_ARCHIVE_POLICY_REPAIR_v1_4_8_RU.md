# Compact archive policy repair [ремонт политики компактного архива] v1.4.8

## Facts [факты]

The previous full archive [предыдущий полный архив] exceeded the compactness principle [принцип компактности] because it embedded old full binary ZIP archives [старые полные бинарные архивы ZIP].

## Decision [решение]

The operator selected Method 3 [метод 3], Method 6 [метод 6], and Method 7 [метод 7]. Historical versions [исторические версии] are stored locally [локально] and in chat histories [историях чатов].

## Applied repair [применённый ремонт]

- Added BR-113 [правило 113]: manifest-only historical continuity [историческая преемственность только через манифест].
- Added BR-114 [правило 114]: canonical-copy rule [правило единственной канонической копии].
- Added BR-115 [правило 115]: archive role separation [разделение ролей архивов].
- Added BR-116 [правило 116]: Full Actual Compact size gate [ворота размера полной актуальной компактной версии].

## Non-loss boundary [граница отсутствия потери]

Meaning [смысл], active memory [активная память], restore prompts [промпты восстановления], legal package [юридический комплект], verification [проверка], and history identity [идентичность истории] are preserved. Old binary history [старая бинарная история] is not physically duplicated in the working compact archive [рабочем компактном архиве].
