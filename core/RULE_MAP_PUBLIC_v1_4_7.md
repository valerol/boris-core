# RULE MAP PUBLIC v1.4.7 [публичная карта правил v1.4.7]

Active kernel [активное ядро]: BOIS/BORIS main v2.20 + SIMA v0.4 + BORIS EGO v1.4.
Active core [активное ядро]: `core/ACTIVE_CORE_REFERENCE_v1_4_7.md`.

## Active additions [активные добавления]

- BR-108 — Selected Non-English Language Translation Every Occurrence Rule [правило перевода на выбранный неанглийский язык при каждом появлении].
- BR-109 — Local Block Adjacent Translation Rule [правило соседнего перевода в локальном блоке].
- BR-110 — Release Evidence Source Priority and External Feedback Regression Rule [правило приоритета источников релизного доказательства и регрессии по внешним отзывам].
- BR-111 — Changelog Hygiene and Deduplication Rule [правило гигиены и дедупликации журнала изменений].
- BR-112 — Legal Code Registration Text Content Companion Rule [правило сопровождения текстовым содержанием для регистрации кода].


## BR-108 — Selected Non-English Language Translation Every Occurrence Rule [правило перевода на выбранный неанглийский язык при каждом появлении]

Active wording [активная формулировка]: every foreign/non-local project term must be translated at every occurrence [при каждом появлении] in the selected non-English UN language [выбранном неанглийском языке ООН], with the translation placed in square brackets [квадратных скобках].

## BR-110 — Release Evidence Source Priority Rule [правило приоритета источников релизного доказательства]

Active evidence source [активный источник доказательства]: ACTIVE_CORE.md → active core reference [ссылка на активное ядро] → rule map [карта правил] → memory [память] → QA / verification [проверка качества / проверка] → CHANGELOG [журнал изменений].

## BR-111 — Changelog Hygiene and Deduplication Rule [правило гигиены и дедупликации журнала изменений]

CHANGELOG [журнал изменений] must stay chronological, non-duplicative, and non-canonical for active behavior.

## BR-112 — Legal Code Registration Text Content Companion Rule [правило сопровождения текстовым содержанием для регистрации кода]

Каждый новый public release [публичный релиз] должен сопровождаться legal code registration text content document [документом текстового содержания для регистрации кода]. Минимальный состав:

```text
archive identity [идентичность архива]
source code [исходный код] в текстовом виде
text-file manifest [манифест текстовых файлов]
binary / non-text inventory [перечень бинарных / нетекстовых файлов]
checksum references [ссылки на контрольные суммы]
publication boundary [граница публикации]
attorney selection note [примечание для выбора адвокатом] по deposit copy [депозитной копии]
```

Финальное решение о deposit copy [депозитной копии] принимает attorney / claimant [адвокат / заявитель]. Это release physiology [релизная физиология], а не изменение BOIS Core [ядра BOIS].

## Evidence priority [приоритет доказательств]

`ACTIVE_CORE.md` → `core/ACTIVE_CORE_REFERENCE_v1_4_7.md` → `core/RULE_MAP_PUBLIC_v1_4_7.md/json` → `MEMORY_BORIS_EGO_v1_4.md` → QA [проверка качества] / verification [проверка] files [файлы] → `CHANGELOG.md`.
