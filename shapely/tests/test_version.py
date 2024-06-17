from unittest.mock import mock_open, patch
from shapely._version import git_get_keywords
from shapely._version import render_pep440_branch

def test_git_get_keywords_all():
    mock_file_content = """
    git_refnames = "refs/heads/main"
    git_full = "abcdef1234567890"
    git_date = "2023-06-13T12:34:56Z"
    """
    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        result = git_get_keywords("dummy_path")
        assert result == {
            "refnames": "refs/heads/main",
            "full": "abcdef1234567890",
            "date": "2023-06-13T12:34:56Z"}


def test_can_get_git_keywords_none():
    mock_file_content = """
    key_1 = "non_existining"
    key_2 = "non_mathcing_key"
    """
    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        result = git_get_keywords("false_path")
        assert result == {}


def test_git_get_keywords_oserror():
    with patch("builtins.open", side_effect=OSError):
        result = git_get_keywords("invalid_path")
        assert result == {}


def test_render_pep440_branch_clean():
    pieces = {
        "closest-tag": "v1.0.0",
        "branch": "master",
        "distance": 0,
        "dirty": False,
        "short": "letters"
    }
    result = render_pep440_branch(pieces)
    assert result == "v1.0.0"


def test_render_pep440_branch_non_master():
    pieces = {
        "closest-tag": "v1.0.0",
        "distance": 5,
        "short": "letters",
        "dirty": False,
        "branch": "feature"
    }
    result = render_pep440_branch(pieces)
    assert result == "v1.0.0.dev0+5.gletters"


def test_render_pep440_branch_dirty():
    pieces = {
        "closest-tag": "v1.0.0",
        "branch": "master",
        "distance": 0,
        "dirty": True,
        "short": "letters"
    }
    result = render_pep440_branch(pieces)
    assert result == "v1.0.0+0.gletters.dirty"


def test_render_pep440_branch_no_tag_not_dirty():
    pieces = {
        "closest-tag": None,
        "distance": 5,
        "short": "letters",
        "dirty": False,
        "branch": "master"
    }
    result = render_pep440_branch(pieces)
    assert result == "0+untagged.5.gletters"