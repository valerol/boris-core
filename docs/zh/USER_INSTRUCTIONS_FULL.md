# 完整用户说明

此文件是完整用户说明的明确入口。下方的操作文本与 `USER_MANUAL_FULL.md` 相同。

# 完整用户手册

BOIS:SIMA&BORIS 公共包 v1.4.3，包含严格的联合国语言平等和 BORIS EGO v1.0。

本包提供本地、无网络的 SIMA 分析器，以及由人类主导使用 BOIS/BORIS 的文档。输出是候选重构，不是最终真理，也不是现场验证。

人类审查者必须设定领域、价值接口、可接受风险和停止条件。

请勿将本包用于自主强制治理、医疗/法律/金融/军事决策，或隐藏的机构控制。

## 工作流程

1. 定义领域 D 和价值接口 V。
2. 声明基底 S：单元、通道、记忆、成本、失效模式和停止权限。
3. 将观察加入为 opers：触发、区分、证据、承载者、权限、价值/风险门、转换、记忆写入、闭合信号、过渡残余、成本和置信度。
4. 运行验证和分析。
5. 将 M=<O,E,A,V,R,C,T> 视为候选重构。
6. 审查风险标志。
7. 在创建本地 BORIS 指令之前，先运行经验测试。
8. 保留回滚路径和停止条件。

## 命令

```bash
python -m bois_sima_boris docs --lang zh
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```

## 活动核心与语言平等

完整包支持阿拉伯语、中文、英语、法语、俄语和西班牙语，不设优先公共语言。使用 `BORIS_EGO_LAYER.md` 查看活动 EGO 层，使用 `../../core/ACTIVE_CORE_REFERENCE_v1_4_8.md` 查看所有核心镜像。

## 使用边界

这是公共实验包。不要把它当作独立治理者、领域专家替代品或机器意识证明。从分析转为指令的每一步都需要人工审查、适用边界和停止信号。
