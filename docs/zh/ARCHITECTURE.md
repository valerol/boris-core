# 架构

匿名化最终公共 Alpha 档案

此本地化包提供仅本地运行、无网络的 SIMA 分析器，以及由人类主导使用 BOIS/BORIS 的文档。它产生候选重构，不是最终真理，也不是现场验证。

人类审查者必须设定领域、价值接口、可接受风险和停止条件。

不要将此 Alpha 包用于自主强制治理、医疗/法律/金融/军事决策或隐藏的机构控制。

Layer map:

- BOIS: grammar for incomplete knowledge, protocols, instructions, experience, physiology, and attention.
- SIMA: analytic layer for candidate reconstruction from substrate and observed opers.
- BORIS: human-led implementation layer for a specific domain.
- Tests: validation, self-check, stress cases, risk gates, and rollback.

Data flow: JSON object -> validation -> opers -> operome -> candidate M=<O,E,A,V,R,C,T> -> limits and next step.
