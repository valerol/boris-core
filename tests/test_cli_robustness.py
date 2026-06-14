# SPDX-License-Identifier: MIT
from bois_sima_boris.cli import main


def test_invalid_json_exits_cleanly(tmp_path, capsys):
    bad = tmp_path / 'bad.json'
    bad.write_text('{not valid json', encoding='utf-8')
    try:
        main(['analyze', str(bad)])
    except SystemExit as exc:
        assert exc.code == 2
    else:
        raise AssertionError('invalid JSON should exit with code 2')
    assert 'invalid_json' in capsys.readouterr().err


def test_missing_file_exits_cleanly(capsys):
    try:
        main(['validate', 'missing-input-file.json'])
    except SystemExit as exc:
        assert exc.code == 2
    else:
        raise AssertionError('missing input should exit with code 2')
    assert 'file_not_found' in capsys.readouterr().err
