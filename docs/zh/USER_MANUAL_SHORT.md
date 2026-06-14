# 快速开始

BOIS:SIMA&BORIS 公共包 v1.4.3，包含严格的联合国语言平等和 BORIS EGO v1.0。

本包提供本地、无网络的 SIMA 分析器，以及由人类主导使用 BOIS/BORIS 的文档。输出是候选重构，不是最终真理，也不是现场验证。

人类审查者必须设定领域、价值接口、可接受风险和停止条件。

请勿将本包用于自主强制治理、医疗/法律/金融/军事决策，或隐藏的机构控制。

## 最短操作流程

1. 在 JSON 文件中描述对象。
2. 验证该文件。
3. 运行分析。
4. 阅读候选机器、风险标志、操作组、以及适用边界。
5. 在经验测试和人工审查之前，不要把输出转换为本地指令。

## 命令

```bash
python -m bois_sima_boris docs --lang zh
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```

## BORIS EGO 与活动核心

请使用本文件夹中的 `BORIS_EGO_LAYER.md` 作为 BORIS EGO v1.0 的活动公共核心。简短路径：阅读本文件，阅读 `QUICKSTART.md`，运行 `python -m bois_sima_boris docs --lang zh`，并查看 `../../START_HERE_UN.md` 以获得平等语言访问。

说明：BORIS EGO v1.0 默认作为核心的一部分处于活动状态；不需要启动 Mode 10 [模式 10]。
