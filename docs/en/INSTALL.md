# Installation

## Installation and no-install run

1. Install Python 3.9 or newer.
2. Unzip the package.
3. You can run directly before installation:

```bash
python -m bois_sima_boris docs --lang en
python -m bois_sima_boris ego-status
```

4. Optional local editable installation:

```bash
python -m pip install --no-index -e .
```

The package includes a dependency-free local build backend for this offline editable installation path.

## Common commands

```bash
python -m bois_sima_boris docs --lang en
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```
