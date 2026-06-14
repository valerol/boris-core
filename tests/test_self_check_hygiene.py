# SPDX-License-Identifier: MIT
from pathlib import Path
from bois_sima_boris.self_check import run_self_check


def test_self_check_ignores_local_virtualenv(tmp_path: Path):
    root = tmp_path / "pkg"
    root.mkdir()
    (root / "safe.py").write_text("print('ok')\n", encoding="utf-8")
    venv = root / ".venv" / "lib" / "python" / "site-packages" / "example"
    venv.mkdir(parents=True)
    prohibited_import = "import sub" + "process\n"
    (venv / "bad.py").write_text(prohibited_import, encoding="utf-8")
    result = run_self_check(root)
    assert result["ok"] is True
    assert result["findings"] == []
