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

