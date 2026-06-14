from pathlib import Path
import hashlib, re, json

ROOT = Path(__file__).resolve().parents[1]

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def test_legal_companion_hashes_match_actual_files():
    md = ROOT / "legal" / "copyright" / "BOIS_PUBLIC_ARCHIVE_LEGAL_CODE_REGISTRATION_TEXT_CONTENT_v1_4_10_RU_EN.md"
    text = md.read_text(encoding="utf-8")
    pairs = re.findall(r"`([^`]+)`[^`]+`([a-f0-9]{64})`", text)
    assert pairs, "no SHA-256 entries found in legal companion"
    checked = 0
    for name, expected in pairs:
        path = ROOT / "legal" / "copyright" / name
        if path.exists():
            assert sha(path) == expected, f"stale SHA-256 for {name}"
            checked += 1
    assert checked >= 3

def test_program_text_package_is_embedded_and_manifest_current():
    d = ROOT / "legal" / "program_text"
    assert (ROOT / "PROGRAM_TEXT_PACKAGE.md").exists()
    assert (d / "BOIS_PUBLIC_RELEASE_SOURCE_CODE_FULL_v1_4_10.txt").exists()
    assert (d / "BOIS_PUBLIC_RELEASE_SOURCE_CODE_DEPOSIT_FIRST10_LAST10_v1_4_10.docx").exists()
    assert (d / "BOIS_PUBLIC_RELEASE_SOURCE_CODE_DEPOSIT_FIRST10_LAST10_v1_4_10.pdf").exists()
    manifest = json.loads((d / "BOIS_PROGRAM_TEXT_PACKAGE_MANIFEST_v1_4_10.json").read_text(encoding="utf-8"))
    assert manifest["public_release"] == "1.4.10"
    assert manifest["rule"] == "BR-117"
