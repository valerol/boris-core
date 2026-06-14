# SPDX-License-Identifier: MIT
from pathlib import Path
from bois_sima_boris.cli import main

ROOT = Path(__file__).resolve().parents[1]

def test_docs_command_printed_paths_exist(capsys):
    for lang in ["ar", "zh", "en", "fr", "ru", "es"]:
        assert main(["docs", "--lang", lang]) == 0
        out = capsys.readouterr().out
        for line in out.splitlines():
            if line.startswith("- "):
                rel = line[2:].strip()
                assert (ROOT / rel).exists(), f"docs command printed missing path for {lang}: {rel}"
