import pytest
from unittest.mock import patch

from shapely._version import versions_from_parentdir, NotThisMethod, get_versions

@pytest.mark.parametrize("verbose", [True, False])
def test_versions_from_parentdir_success(verbose):
    with patch("os.path.basename", return_value="shapely-1.0.0"):
        result = versions_from_parentdir("shapely-", "/some/path/shapely-1.0.0", verbose)
        assert result == {
            "version": "1.0.0",
            "full-revisionid": None,
            "dirty": False,
            "error": None,
            "date": None,
        }

@pytest.mark.parametrize("verbose", [True, False])
def test_versions_from_parentdir_fail(verbose):
    with patch("os.path.basename", side_effect=["path", "random", "some"]):
        with patch("os.path.dirname", side_effect=["/some/random", "/some", "/"]):
            with pytest.raises(NotThisMethod):
                versions_from_parentdir("shapely-", "/some/random/path", verbose)

def test_versions_from_parentdir_verbose(capsys):
    with patch("os.path.basename", side_effect=["path", "random", "some"]):
        with patch("os.path.dirname", side_effect=["/some/random", "/some", "/"]):
            with pytest.raises(NotThisMethod):
                versions_from_parentdir("shapely-", "/some/random/path", True)
            captured = capsys.readouterr()
            assert "Tried directories ['/some/random/path', '/some/random', '/some'] but none started with prefix shapely-" in captured.out

def test_get_versions_name_error():
    with patch('os.path.realpath', side_effect=NameError):
        result = get_versions()
        assert result == {
            "version": "0+unknown",
            "full-revisionid": None,
            "dirty": None,
            "error": "unable to find root of source tree",
            "date": None,
        }

def test_get_versions_not_this_method():
    with patch('os.path.realpath', return_value="/some/path/_version.py"):
        with patch('os.path.dirname', side_effect=["/some/path", "/some"]):
            with patch('shapely._version.git_pieces_from_vcs', side_effect=NotThisMethod):
                with patch('shapely._version.versions_from_parentdir', side_effect=NotThisMethod):
                    result = get_versions()
                    assert result == {
                        "version": "0+unknown",
                        "full-revisionid": None,
                        "dirty": None,
                        "error": "unable to compute version",
                        "date": None,
                    }

def test_get_versions_parentdir_success():
    with patch('os.path.realpath', return_value="/some/path/_version.py"):
        with patch('os.path.dirname', side_effect=["/some/path", "/some"]):
            with patch('shapely._version.git_pieces_from_vcs', side_effect=NotThisMethod):
                with patch('shapely._version.versions_from_parentdir', return_value={
                    "version": "1.0.0",
                    "full-revisionid": None,
                    "dirty": False,
                    "error": None,
                    "date": None,
                }):
                    result = get_versions()
                    assert result == {
                        "version": "1.0.0",
                        "full-revisionid": None,
                        "dirty": False,
                        "error": None,
                        "date": None,
                    }
