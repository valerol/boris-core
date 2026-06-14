# 安装

## 安装与免安装运行

1. 安装 Python 3.9 或更新版本。
2. 解压软件包。
3. 安装前可以直接运行：

```bash
python -m bois_sima_boris docs --lang zh
python -m bois_sima_boris ego-status
```

4. 可选的本地可编辑安装：

```bash
python -m pip install --no-index -e .
```

软件包包含无外部依赖的本地构建后端，用于这条离线安装路径。

## 常用命令

```bash
python -m bois_sima_boris docs --lang zh
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```
