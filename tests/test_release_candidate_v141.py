# SPDX-License-Identifier: MIT
from pathlib import Path
import venv
import sys
from bois_sima_boris.ego import ACTIVE_PUBLIC_RELEASE, ACTIVE_BORIS_EGO, ACTIVE_BOIS_BORIS_MAIN, ACTIVE_CORE_BY_LANG

ROOT = Path(__file__).resolve().parents[1]
NON_EN = ["ar", "zh", "fr", "ru", "es"]
KNOWN_ENGLISH_BLOCKS = [
    "BORIS EGO is a minimal agent-like choice surface.",
    "This is not a factual claim",
    "Basic EGO ethical constraints",
    "The operator is the source of final goals.",
    "Harm to beings capable",
    "Lying and manipulation are forbidden.",
    "BORIS EGO-proposed messages are not user words.",
    "The overall system may have large physiology:",
    "Immune tests check:",
    "Standard mode:",
    "Mode 10 starts only",
    "Run: `python -m pytest`",
    "Test classes: philosophical",
    "Install Python 3.9+",
    "Unzip the package.",
]

def test_v142_active_versions_and_files():
    assert ACTIVE_PUBLIC_RELEASE == "1.4.10"
    assert ACTIVE_BOIS_BORIS_MAIN == "2.23"
    assert ACTIVE_BORIS_EGO == "1.7"
    assert (ROOT / "core" / "ACTIVE_CORE_REFERENCE_v1_4_10.md").exists()
    assert (ROOT / "core" / "RULE_MAP_PUBLIC_v1_4_10.json").exists()
    for rel in ACTIVE_CORE_BY_LANG.values():
        assert "v1_7" in rel
        assert (ROOT / rel).exists()

def test_active_non_english_ego_docs_have_no_known_english_blocks():
    for lang in NON_EN:
        paths = [ROOT / "docs" / lang / "BORIS_EGO_LAYER.md", ROOT / ACTIVE_CORE_BY_LANG[lang], ROOT / "docs" / lang / "TESTING_AND_SELF_TESTING.md", ROOT / "docs" / lang / "INSTALL.md"]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            for block in KNOWN_ENGLISH_BLOCKS:
                assert block not in text, f"{block!r} remains in {path.relative_to(ROOT)}"

def test_no_install_source_tree_shim_exists():
    assert (ROOT / "bois_sima_boris" / "__main__.py").exists()
    assert (ROOT / "bois_sima_boris" / "__init__.py").exists()

def test_dependency_free_build_backend_exists():
    backend = ROOT / "build_backend" / "bois_sima_boris_build_backend.py"
    assert backend.exists()
    text = backend.read_text(encoding="utf-8")
    assert "get_requires_for_build_editable" in text
    assert "return []" in text
