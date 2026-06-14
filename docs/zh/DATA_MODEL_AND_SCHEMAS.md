# 数据模型与模式

匿名化最终公共 Alpha 档案

此本地化包提供仅本地运行、无网络的 SIMA 分析器，以及由人类主导使用 BOIS/BORIS 的文档。它产生候选重构，不是最终真理，也不是现场验证。

人类审查者必须设定领域、价值接口、可接受风险和停止条件。

不要将此 Alpha 包用于自主强制治理、医疗/法律/金融/军事决策或隐藏的机构控制。

Required top-level JSON keys: `object_id`, `object_type`, `domain`, `value_interface`, `substrate`, `observations`.

Required substrate fields: `units`, `channels`, `memory`, `costs`, `failure_modes`, `stop_authority`.

Required value-interface fields: `goals`, `constraints`, `forbidden_losses`.

Observation fields become opers: `trigger`, `distinction`, `evidence`, `carrier`, `authority`, `value_risk_gate`, `transformation`, `memory_write`, `closure_signal`, `transition_residue`, `cost`, `confidence`.
