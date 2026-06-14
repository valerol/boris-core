# SPDX-License-Identifier: MIT
from pathlib import Path
import re

from bois_sima_boris.ego import (
    ACTIVE_PUBLIC_RELEASE, ACTIVE_BORIS_EGO, ACTIVE_BOIS_BORIS_MAIN,
    ACTIVE_CORE_BY_LANG, language_parity_manifest, route_calculation,
)
from bois_sima_boris.cli import main

ROOT = Path(__file__).resolve().parents[1]
LANGS = ["ar", "zh", "en", "fr", "ru", "es"]

def test_v139_active_versions_and_core_files():
    assert ACTIVE_PUBLIC_RELEASE == "1.4.10"
    assert ACTIVE_BOIS_BORIS_MAIN == "2.23"
    assert ACTIVE_BORIS_EGO == "1.7"
    for lang, rel in ACTIVE_CORE_BY_LANG.items():
        assert (ROOT / rel).exists(), f"missing active core for {lang}: {rel}"


def test_user_instruction_alias_parity():
    required = set(language_parity_manifest()["required_user_docs"])
    required.update({"USER_INSTRUCTIONS_SHORT.md", "USER_INSTRUCTIONS_FULL.md"})
    for lang in LANGS:
        for name in required:
            assert (ROOT / "docs" / lang / name).exists(), f"missing docs/{lang}/{name}"


def test_cli_docs_lists_instruction_aliases_and_existing_paths(capsys):
    for lang in LANGS:
        assert main(["docs", "--lang", lang]) == 0
        out = capsys.readouterr().out
        assert f"docs/{lang}/USER_INSTRUCTIONS_SHORT.md" in out
        assert f"docs/{lang}/USER_INSTRUCTIONS_FULL.md" in out
        for line in out.splitlines():
            if line.startswith("- "):
                rel = line[2:].strip()
                assert (ROOT / rel).exists(), f"CLI listed missing path for {lang}: {rel}"


def test_historical_ego_links_resolve():
    for rel in [
        "core/BORIS_EGO_LAYER_v0_1_RU.md", "core/BORIS_EGO_LAYER_v0_1_EN.md",
        "core/BORIS_EGO_LAYER_v0_2_RU.md", "core/BORIS_EGO_LAYER_v0_2_EN.md",
        "core/BORIS_EGO_LAYER_v0_3_RU.md", "core/BORIS_EGO_LAYER_v0_3_EN.md",
    ]:
        assert (ROOT / rel).exists(), rel


def test_release_readiness_routes_to_core():
    assert route_calculation("release_readiness_gate") == "BOIS_CORE"
