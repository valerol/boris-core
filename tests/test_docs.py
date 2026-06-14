# SPDX-License-Identifier: MIT
from pathlib import Path
from bois_sima_boris.cli import main

ROOT = Path(__file__).resolve().parents[1]

def test_docs_command(capsys):
    assert main(["docs"]) == 0
    out = capsys.readouterr().out
    assert "docs/INDEX.md" in out
    assert "START_HERE_UN.md" in out
    assert "SIMA_ANALYZER_GUIDE" in out

def test_docs_command_lists_only_existing_paths(capsys):
    for lang in ["ar", "zh", "en", "fr", "ru", "es"]:
        assert main(["--lang", lang, "docs"]) == 0
        out = capsys.readouterr().out
        for line in out.splitlines():
            if line.startswith("- "):
                rel = line[2:].strip()
                assert (ROOT / rel).exists(), f"missing CLI-linked path for {lang}: {rel}"
