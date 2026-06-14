from pathlib import Path


def test_local_build_backend_version_matches_active_release():
    backend = Path("build_backend/bois_sima_boris_build_backend.py").read_text(encoding="utf-8")
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    assert "VERSION = \"1.4.10\"" in backend
    assert "version = \"1.4.10\"" in pyproject
    assert "VERSION = \"1.4.2\"" not in backend
