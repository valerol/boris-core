# 测试与自测

公共发布候选档案

只使用本地测试。它们检查结构、文档、CLI 行为、语言访问、EGO 边界、档案清洁度和校验和。它们不证明现场可靠性，也不证明机器意识。

命令：

```bash
python -m pytest
python -m bois_sima_boris self-check --root .
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
```

测试组：哲学一致性、逻辑、opers 结构、档案结构、本地化、安全基线、压力行为、发布卫生、EGO 集成以及与发达生理结构的兼容性。
