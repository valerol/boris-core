# SPDX-License-Identifier: MIT
from pathlib import Path

def s(*codes):
    return "".join(chr(c) for c in codes)

FORBIDDEN = [
    s(65,108,97,115,107,97,32,83,116,111,110,101),
    s(65,108,97,115,107,97,32,83,116,111,110,101,115),
    s(65,108,97,115,107,97,95,83,116,111,110,101),
    s(65,108,97,115,107,97,95,83,116,111,110,101,115),
    s(69,103,111,114),
    s(84,101,109,110,105,107,111,118),
    s(1045,1075,1086,1088),
    s(1058,1077,1084,1085,1080,1082,1086,1074),
    s(101,103,111,114,46,116,101,109,110,105,107),
    s(103,109,97,105,108,46,99,111,109),
    s(83,104,111,114,101,108,105,110,101),
    s(74,101,119,105,115,104,32,65,117,116,111,110,111,109,111,117,115),
    s(1045,1040,1054),
]
SKIP_DIRS = {".venv", "venv", "__pycache__", ".pytest_cache", "build", "dist"}
TEXT_EXT = {".md", ".py", ".json", ".toml", ".txt", ".csv", ".cff", ""}
ALLOWED_PRIVATE_PREFIXES = {"articles"}

def test_public_tree_has_no_known_private_tokens_outside_bundled_articles():
    root = Path(__file__).resolve().parents[1]
    hits = []
    for p in root.rglob("*"):
        rel_parts = p.relative_to(root).parts
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if rel_parts and rel_parts[0] in ALLOWED_PRIVATE_PREFIXES:
            # The article bundle intentionally contains public author metadata.
            continue
        if p.is_file() and p.suffix.lower() in TEXT_EXT:
            text = p.read_text(encoding="utf-8", errors="ignore")
            for token in FORBIDDEN:
                if token in text:
                    hits.append((str(p.relative_to(root)), "redacted-token"))
    assert hits == []

def test_bundled_article_exists_in_english_and_local_language():
    root = Path(__file__).resolve().parents[1]
    assert (root / "articles" / "en").exists()
    package_dirs = [p for p in (root / "articles").iterdir() if p.is_dir() and p.name.startswith("package_language_")]
    # Master packages may instead contain all language folders directly; language packages contain package_language_*.
    if package_dirs:
        assert any(d.glob("*.pdf") for d in package_dirs)
    else:
        assert any((root / "articles" / code).exists() for code in ("ar", "en", "es", "fr", "ru", "zh"))
