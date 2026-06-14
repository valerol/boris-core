# RULE MAP PUBLIC v1.4.6 [публичная карта правил v1.4.6]

Fixed UTC [согласованное всемирное время]: 2026-06-12T08:45:00Z.

Active kernel [активное ядро]: BOIS/BORIS main v2.19 + SIMA v0.4 + BORIS EGO v1.3.

Active core [активное ядро]: `core/ACTIVE_CORE_REFERENCE_v1_4_6.md`.

## New active rules [новые активные правила]

- BR-108 — Selected Non-English Language Translation Every Occurrence Rule [правило перевода на выбранный неанглийский язык при каждом появлении], v0.2 — at every occurrence [при каждом появлении].
- BR-109 — Local Block Adjacent Translation Rule [правило соседнего перевода в локальном блоке].
- BR-110 — Release Evidence Source Priority and External Feedback Regression Rule [правило приоритета источников релизного доказательства и регрессии по внешним отзывам].
- BR-111 — Changelog Hygiene and Deduplication Rule [правило гигиены и дедупликации журнала изменений].

## Compatibility [совместимость]

Historical rules remain context unless they conflict with the latest active core [активным ядром]. Latest active rule wins [новейшее активное правило имеет приоритет].


## BR-110 — Release Evidence Source Priority Rule [правило приоритета источников релизного доказательства]

ACTIVE_CORE [активное ядро], active core reference [ссылка на активное ядро], rule map [карта правил], memory [память] and QA [проверка качества] have priority over CHANGELOG.md [журналом изменений] if a conflict is found. External feedback must be converted into regression checks [регрессионные проверки] where applicable.

## BR-111 — Changelog Hygiene and Deduplication Rule [правило гигиены и дедупликации журнала изменений]

CHANGELOG.md [журнал изменений] must be chronological or clearly grouped, non-duplicative, and aligned with the active evidence chain.
