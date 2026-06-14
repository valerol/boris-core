# 快速开始

匿名化最终公共 Alpha 档案

此本地化包提供仅本地运行、无网络的 SIMA 分析器，以及由人类主导使用 BOIS/BORIS 的文档。它产生候选重构，不是最终真理，也不是现场验证。

人类审查者必须设定领域、价值接口、可接受风险和停止条件。

不要将此 Alpha 包用于自主强制治理、医疗/法律/金融/军事决策或隐藏的机构控制。

## 命令

```bash
python -m bois_sima_boris docs --lang zh
python -m bois_sima_boris ego-status
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```

说明：BORIS EGO v1.0 默认作为核心的一部分处于活动状态；不需要启动 Mode 10 [模式 10]。
