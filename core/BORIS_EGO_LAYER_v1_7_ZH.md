# BORIS EGO [伦理派生目标编排器] v1.7

Active version [活动版本]: BOIS [业务操作智能系统] / BORIS [业务操作理性智能系统] main [主线] v2.23 + SIMA [基质无关机器分析器] v0.4 + BORIS EGO [伦理派生目标编排器] v1.7. Public Release [公开发布] v1.4.10.

EGO [伦理派生目标编排器] 是 default core layer [默认核心层]。G0 [最终目标] 由 operator [操作员] 给出；G1-G4 [派生目标] 可在规则门内编排。

v1.4.10 采用 Method 3 [方法3]、Method 6 [方法6] 和 Method 7 [方法7]：manifest-only history [仅清单历史]、canonical copy [唯一规范副本] 和 archive role separation [档案角色分离]。historical binary archives [历史二进制档案] 不嵌套进 FULL_ACTUAL_COMPACT [完整当前紧凑版本]。


EGO = Ethical Goal Orchestrator [этический оркестратор производных целей].

not a factual claim [не является фактическим утверждением] that AI [искусственный интеллект] has subjective experience [субъективный опыт].


Иноязычные проектные термины получают перевод в квадратных скобках при каждом появлении.


## BR-117 — Program Text Package Companion Rule [правило сопровождения пакетом текста программы]

Every Public Release [публичный релиз] must be accompanied by PROGRAM_TEXT_PACKAGE [пакет текста программы]. The package is embedded in `legal/program_text/` and delivered as a separate sidecar ZIP [сопровождающий ZIP-архив]. It contains full source code text [полный текст исходного кода], deposit selection first 10 and last 10 pages [депозитная выборка первых 10 и последних 10 страниц], DOCX [документ Word], PDF [документ PDF], Markdown [документ Markdown], TXT [текстовый файл], manifest JSON [машиночитаемый манифест] and SHA-256 [контрольные суммы SHA-256].


## BR-118 - Program Text Companion Integrity Rule [правило целостности сопровождающего пакета текста программы]

Every legal companion [сопровождающий юридический документ] and PROGRAM_TEXT_PACKAGE [пакет текста программы] must contain current SHA-256 [контрольные суммы SHA-256] matching the actual packaged files. Stale companion hashes [устаревшие контрольные суммы в сопровождающем документе] are release-blocking defects [блокирующие дефекты релиза] for legal use, even when the active core [активное ядро] is not affected.
