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


def test_render_pep440_branch_clean():
    pieces = {
        "closest-tag": "v1.0.0",
        "branch": "master",
        "distance": 0,
        "dirty": False,
        "short": "abc123"
    }
    result = render_pep440_branch(pieces)
    assert result == "v1.0.0"


def test_render_pep440_branch_dirty():
    pieces = {
        "closest-tag": "v1.0.0",
        "branch": "master",
        "distance": 0,
        "dirty": True,
        "short": "abc123"
    }
    result = render_pep440_branch(pieces)
    assert result == "v1.0.0+0.gabc123.dirty"


def test_render_pep440_branch_no_tags_clean():
    pieces = {
        "closest-tag": None,
        "branch": "feature",
        "distance": 10,
        "dirty": False,
        "short": "abc123"
    }
    result = render_pep440_branch(pieces)
    assert result == "0.dev0+untagged.10.gabc123"


def test_render_pep440_no_tags_dirty():
    pieces = {
        "closest-tag": None,
        "branch": "feature",
        "distance": 10,
        "dirty": True,
        "short": "abc123"
    }
    result = render_pep440_branch(pieces)
    assert result == "0.dev0+untagged.10.gabc123.dirty"