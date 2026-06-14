# SPDX-License-Identifier: MIT
from pathlib import Path
import json
from bois_sima_boris.ego import active_status, route_calculation
ROOT = Path(__file__).resolve().parents[1]

def test_v149_program_text_package_exists_and_is_active():
    status = active_status()
    assert status["public_release"] == "1.4.10"
    assert status["bois_boris_main"] == "2.23"
    assert status["boris_ego"] == "1.7"
    assert status["program_text_package"]["active"] is True
    assert status["program_text_package"]["sidecar_required"] is True
    assert route_calculation("program_text_package") == "BOIS_CORE"
    assert (ROOT / "PROGRAM_TEXT_PACKAGE.md").exists()

def test_v149_program_text_package_required_files_exist():
    base = ROOT / "legal" / "program_text"
    required = [
        "BOIS_PROGRAM_TEXT_PACKAGE_README_v1_4_10_RU_EN.md",
        "BOIS_PUBLIC_RELEASE_SOURCE_CODE_FULL_v1_4_10.txt",
        "BOIS_PUBLIC_RELEASE_SOURCE_CODE_DEPOSIT_FIRST10_LAST10_v1_4_10.txt",
        "BOIS_PUBLIC_RELEASE_SOURCE_CODE_DEPOSIT_FIRST10_LAST10_v1_4_10.md",
        "BOIS_PUBLIC_RELEASE_SOURCE_CODE_DEPOSIT_FIRST10_LAST10_v1_4_10.docx",
        "BOIS_PUBLIC_RELEASE_SOURCE_CODE_DEPOSIT_FIRST10_LAST10_v1_4_10.pdf",
        "BOIS_PROGRAM_TEXT_PACKAGE_MANIFEST_v1_4_10.json",
    ]
    for name in required:
        assert (base / name).exists(), name

def test_v149_program_text_manifest_covers_required_files():
    manifest = json.loads((ROOT / "legal" / "program_text" / "BOIS_PROGRAM_TEXT_PACKAGE_MANIFEST_v1_4_10.json").read_text(encoding="utf-8"))
    assert manifest["public_release"] == "1.4.10"
    assert manifest["package_type"] == "PROGRAM_TEXT_PACKAGE"
    assert manifest["rule"] == "BR-117"
    names = {Path(item["path"]).name for item in manifest["files"]}
    assert "BOIS_PUBLIC_RELEASE_SOURCE_CODE_FULL_v1_4_10.txt" in names
    assert "BOIS_PUBLIC_RELEASE_SOURCE_CODE_DEPOSIT_FIRST10_LAST10_v1_4_10.docx" in names
    assert "BOIS_PUBLIC_RELEASE_SOURCE_CODE_DEPOSIT_FIRST10_LAST10_v1_4_10.pdf" in names
