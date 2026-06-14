# BORIS EGO v1.7 — compact actual packaging

Active version: BOIS/BORIS main v2.23 + SIMA v0.4 + BORIS EGO v1.7. Public Release v1.4.10.

EGO = Ethical Goal Orchestrator. It is a default core layer. G0 final goals remain operator-supplied; G1-G4 derivative goals may be orchestrated by EGO inside rule gates.

v1.4.10 accepts Method 3, Method 6 and Method 7: manifest-only history references, canonical-copy packaging, and separation of archive roles. Public releases are paired with a separate full actual compact archive. Historical binary archives are not nested in the working compact archive; they are referenced by manifest, digest cards, size and SHA-256 when available.

not a factual claim [не является фактическим утверждением] that AI [искусственный интеллект] has subjective experience [субъективный опыт].


## BR-117 — Program Text Package Companion Rule [правило сопровождения пакетом текста программы]

Every Public Release [публичный релиз] must be accompanied by PROGRAM_TEXT_PACKAGE [пакет текста программы]. The package is embedded in `legal/program_text/` and delivered as a separate sidecar ZIP [сопровождающий ZIP-архив]. It contains full source code text [полный текст исходного кода], deposit selection first 10 and last 10 pages [депозитная выборка первых 10 и последних 10 страниц], DOCX [документ Word], PDF [документ PDF], Markdown [документ Markdown], TXT [текстовый файл], manifest JSON [машиночитаемый манифест] and SHA-256 [контрольные суммы SHA-256].
