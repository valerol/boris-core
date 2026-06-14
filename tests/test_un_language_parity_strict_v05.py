# SPDX-License-Identifier: MIT
from pathlib import Path
import re
from bois_sima_boris.cli import main
from bois_sima_boris.ego import language_parity_manifest, route_calculation

ROOT = Path(__file__).resolve().parents[1]
NON_EN = ["ar", "zh", "fr", "ru", "es"]
FORBIDDEN_WORKFLOW_FRAGMENTS = [
    "Minimal workflow",
    "Describe an object",
    "Validate it",
    "Analyze it",
    "Define domain",
    "Run validation",
    "Review risk flags",
    "Preserve rollback",
    "Do not convert the output",
]


def _strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def test_required_language_docs_and_neutrality_doc_exist():
    required = set(language_parity_manifest()["required_user_docs"])
    required.add("LANGUAGE_NEUTRALITY.md")
    for lang in language_parity_manifest()["languages"]:
        for name in required:
            assert (ROOT / "docs" / lang / name).exists(), f"missing docs/{lang}/{name}"


def test_cli_docs_lists_only_existing_files(capsys):
    for lang in language_parity_manifest()["languages"]:
        assert main(["docs", "--lang", lang]) == 0
        out = capsys.readouterr().out
        for line in out.splitlines():
            if not line.startswith("- "):
                continue
            rel = line[2:].strip()
            assert (ROOT / rel).exists(), f"CLI listed missing file for {lang}: {rel}"


def test_non_english_user_manuals_do_not_retain_core_english_workflow_fragments():
    for lang in NON_EN:
        for name in ["USER_MANUAL_SHORT.md", "USER_MANUAL_FULL.md"]:
            text = _strip_code_blocks((ROOT / "docs" / lang / name).read_text(encoding="utf-8"))
            for frag in FORBIDDEN_WORKFLOW_FRAGMENTS:
                assert frag not in text, f"{frag!r} remains in docs/{lang}/{name}"


def test_non_english_indexes_localize_main_section_labels():
    for lang in NON_EN:
        text = (ROOT / "docs" / lang / "INDEX.md").read_text(encoding="utf-8")
        assert "## Documents" not in text
        assert "## Equal language access" not in text
        assert "No public access language is preferred" not in text


def test_language_parity_conflicts_and_instruction_completeness_route_to_core():
    assert route_calculation("language_parity_conflict") == "BOIS_CORE"
    assert route_calculation("localized_instruction_completeness") == "BOIS_CORE"
