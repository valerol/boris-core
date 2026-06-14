# SPDX-License-Identifier: MIT
from pathlib import Path
import json
from bois_sima_boris.ego import active_status, route_calculation

ROOT = Path(__file__).resolve().parents[1]


def test_v148_legal_code_registration_artifacts_exist():
    assert (ROOT / "LEGAL_CODE_REGISTRATION_TEXT_CONTENT.md").exists()
    legal = ROOT / "legal" / "copyright"
    required = [
        "BOIS_PUBLIC_ARCHIVE_LEGAL_CODE_REGISTRATION_TEXT_CONTENT_v1_4_10_RU_EN.md",
        "BOIS_PUBLIC_ARCHIVE_SOURCE_CODE_FULL_v1_4_10.txt",
        "BOIS_PUBLIC_ARCHIVE_FULL_TEXT_CONTENT_v1_4_10.txt",
        "BOIS_PUBLIC_ARCHIVE_TEXT_MANIFEST_v1_4_10.json",
    ]
    for name in required:
        assert (legal / name).exists(), name


def test_v148_legal_rule_is_active_and_core_routed():
    status = active_status()
    assert status["public_release"] == "1.4.10"
    assert status["boris_ego"] == "1.7"
    assert status["legal_code_registration"]["active"] is True
    assert status["legal_code_registration"]["attorney_selects_final_deposit_copy"] is True
    assert route_calculation("legal_code_registration_text_content") == "BOIS_CORE"


def test_v148_legal_manifest_identifies_source_and_text_content():
    manifest = json.loads((ROOT / "legal" / "copyright" / "BOIS_PUBLIC_ARCHIVE_TEXT_MANIFEST_v1_4_10.json").read_text(encoding="utf-8"))
    assert manifest["public_release"] == "1.4.10"
    assert manifest["bois_boris_main"] == "2.23"
    assert manifest["boris_ego"] == "1.7"
    assert manifest["source_code_files_count"] >= 1
    assert any(item["path"] == "src/bois_sima_boris/ego.py" for item in manifest["source_code_files"])
    assert manifest["extraction_scope"] == "public archive textual content excluding generated self-referential full-text file"
