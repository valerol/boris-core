# Финальная проверка v1.4.7 — legal code registration text content [текстовое содержание для регистрации кода]

Дата UTC: 2026-06-12.

## Активное состояние

```text
Public Release [публичный релиз]: v1.4.7
BOIS/BORIS main [основная линия BOIS/BORIS]: v2.20
SIMA [Substrate-Independent Machine Analyzer / субстрато-независимый машинный анализатор]: v0.4
BORIS EGO [Ethical Goal Orchestrator / этический оркестратор производных целей]: v1.4
```

## Изменение

Добавлен legal code registration text content document [документ текстового содержания для регистрации кода] и BR-112 — Legal Code Registration Text Content Companion Rule [правило сопровождения текстовым содержанием для регистрации кода].

## Юридическая граница

Документ является release artifact [релизным артефактом], а не legal advice [юридической консультацией]. Финальную deposit copy [депозитную копию] выбирает attorney / claimant [адвокат / заявитель].

## Артефакты

```text
LEGAL_CODE_REGISTRATION_TEXT_CONTENT.md
legal/copyright/BOIS_PUBLIC_ARCHIVE_LEGAL_CODE_REGISTRATION_TEXT_CONTENT_v1_4_7_RU_EN.md
legal/copyright/BOIS_PUBLIC_ARCHIVE_LEGAL_CODE_REGISTRATION_TEXT_CONTENT_v1_4_7_RU_EN.docx
legal/copyright/BOIS_PUBLIC_ARCHIVE_LEGAL_CODE_REGISTRATION_TEXT_CONTENT_v1_4_7_RU_EN.pdf
legal/copyright/BOIS_PUBLIC_ARCHIVE_SOURCE_CODE_FULL_v1_4_7.txt
legal/copyright/BOIS_PUBLIC_ARCHIVE_FULL_TEXT_CONTENT_v1_4_7.txt
legal/copyright/BOIS_PUBLIC_ARCHIVE_TEXT_MANIFEST_v1_4_7.json
```

## Проверки рабочего дерева

```text
pytest [автоматические тесты]: 95 passed in 0.48s
self-check [самопроверка]: returncode 0
ego-status [статус EGO]: returncode 0
docs --lang ru [документы на русском]: returncode 0
DOCX render [рендер DOCX]: 45 pages [страниц]
```

## Privacy boundary [граница приватности]

Article text [текст статей] остаётся в `articles/` и учитывается в manifest [манифесте], но не дублируется в legal full-text extract [юридической полной текстовой выгрузке], чтобы не копировать author/correspondence metadata [метаданные автора/корреспонденции] вне article bundle [пакета статей].

## Ограничения

Не выполнялись legal review [юридическая экспертиза], native-speaker certification [сертификация носителями языков], penetration test [тест на проникновение], field validation [полевая валидация] и доказательство сознания ИИ.

## Вложенные language packages [языковые пакеты]

- ar: BOIS_SIMA_BORIS_Public_Release_v1_4_7_AR_Legal_Code_Text_Content_2026-06-12.zip — 129 files [файлов], testzip [проверка ZIP]: OK
- zh: BOIS_SIMA_BORIS_Public_Release_v1_4_7_ZH_Legal_Code_Text_Content_2026-06-12.zip — 129 files [файлов], testzip [проверка ZIP]: OK
- en: BOIS_SIMA_BORIS_Public_Release_v1_4_7_EN_Legal_Code_Text_Content_2026-06-12.zip — 129 files [файлов], testzip [проверка ZIP]: OK
- fr: BOIS_SIMA_BORIS_Public_Release_v1_4_7_FR_Legal_Code_Text_Content_2026-06-12.zip — 129 files [файлов], testzip [проверка ZIP]: OK
- ru: BOIS_SIMA_BORIS_Public_Release_v1_4_7_RU_Legal_Code_Text_Content_2026-06-12.zip — 129 files [файлов], testzip [проверка ZIP]: OK
- es: BOIS_SIMA_BORIS_Public_Release_v1_4_7_ES_Legal_Code_Text_Content_2026-06-12.zip — 129 files [файлов], testzip [проверка ZIP]: OK
