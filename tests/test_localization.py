# SPDX-License-Identifier: MIT
from pathlib import Path
import re
import unittest
from bois_sima_boris.cli import main
from bois_sima_boris.ego import language_parity_manifest

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_NON_ENGLISH_PHRASES = [
    "Minimal workflow:",
    "Describe an object in JSON.",
    "Validate it.",
    "Analyze it.",
    "## Workflow",
    "Define domain D and value interface V.",
    "Run validation and analysis.",
    "Review risk flags.",
    "Preserve rollback and stop conditions.",
    "## Documents",
    "## Equal language access",
    "No public access language is preferred.",
]

class TestLocalization(unittest.TestCase):
    def test_docs_languages(self):
        for lang in ["ar", "zh", "en", "fr", "ru", "es"]:
            self.assertEqual(main(["--lang", lang, "docs"]), 0)

    def test_un_language_user_docs_exist(self):
        required = language_parity_manifest()["required_user_docs"]
        for lang in language_parity_manifest()["languages"]:
            for name in required:
                self.assertTrue((ROOT / "docs" / lang / name).exists(), f"missing docs/{lang}/{name}")

    def test_active_core_mirrors_exist(self):
        for lang, rel in language_parity_manifest()["active_core_by_lang"].items():
            self.assertTrue((ROOT / rel).exists(), f"missing active core for {lang}: {rel}")

    def test_non_english_user_manuals_do_not_keep_old_english_workflow(self):
        for lang in ["ar", "zh", "fr", "ru", "es"]:
            for name in ["USER_MANUAL_SHORT.md", "USER_MANUAL_FULL.md", "INDEX.md"]:
                text = (ROOT / "docs" / lang / name).read_text(encoding="utf-8")
                for phrase in FORBIDDEN_NON_ENGLISH_PHRASES:
                    self.assertNotIn(phrase, text, f"{phrase!r} remains in docs/{lang}/{name}")

    def test_start_here_links_exist(self):
        text = (ROOT / "START_HERE_UN.md").read_text(encoding="utf-8")
        refs = sorted(set(re.findall(r"`([^`]+\.md)`", text)))
        for rel in refs:
            self.assertTrue((ROOT / rel).exists(), f"broken START_HERE_UN link: {rel}")

if __name__ == "__main__":
    unittest.main()
