import unittest
import pytest
from unittest.mock import mock_open, patch
from shapely._version import git_get_keywords
from shapely._version import render_pep440_branch
from shapely._version import render
from shapely._version import render_git_describe
from shapely._version import versions_from_parentdir, NotThisMethod, get_versions


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

class TestRenderFunction(unittest.TestCase):
    #testing render_git_describe()
    def setUp(self):
        self.pieces = {
            "error": None,
            "long": "abcdef123456",
            "dirty": False,
            "closest-tag": "v1.0.0",
            "distance": 0,
            "short": "abcdef1",
            "date": "2024-01-01T00:00:00"
        }


    def test_render_with_error(self):
        self.pieces["error"] = "some error"
        result = render(self.pieces, "pep440")
        expected = {"version": "unknown",
                    "full-revisionid": self.pieces["long"],
                    "dirty": None,
                    "error": self.pieces["error"],
                    "date": None}
        self.assertEqual(result, expected)

    def test_render_default_style(self):
        result = render(self.pieces, None)
        self.assertEqual(result["error"], None)

    @patch('shapely._version.render_pep440', return_value="v1.0.0")
    def test_render_pep440_style(self, mock_render_pep440):
        result = render(self.pieces, "pep440")
        self.assertEqual(result["version"], "v1.0.0")

    @patch('shapely._version.render_pep440_branch', return_value="v1.0.0-branch")
    def test_render_pep440_branch_style(self, mock_render_pep440_branch):
        result = render(self.pieces, "pep440-branch")
        self.assertEqual(result["version"], "v1.0.0-branch")


    @patch('shapely._version.render_pep440_pre', return_value="v1.0.0-pre")
    def test_render_pep440_pre_style(self, mock_render_pep440_pre):
        result = render(self.pieces, "pep440-pre")
        self.assertEqual(result["version"], "v1.0.0-pre")

    @patch('shapely._version.render_pep440_post', return_value="v1.0.0-post")
    def test_render_pep440_post_style(self, mock_render_pep440_post):
        result = render(self.pieces, "pep440-post")
        self.assertEqual(result["version"], "v1.0.0-post")

    @patch('shapely._version.render_pep440_post_branch', return_value="v1.0.0-post-branch")
    def test_render_pep440_post_branch_style(self, mock_render_pep440_post_branch):
        result = render(self.pieces, "pep440-post-branch")
        self.assertEqual(result["version"], "v1.0.0-post-branch")

    @patch('shapely._version.render_pep440_old', return_value="v1.0.0-old")
    def test_render_pep440_old_style(self, mock_render_pep440_old):
        result = render(self.pieces, "pep440-old")
        self.assertEqual(result["version"], "v1.0.0-old")

    @patch('shapely._version.render_git_describe', return_value="v1.0.0-describe")
    def test_render_git_describe_style(self, mock_render_git_describe):
        result = render(self.pieces, "git-describe")
        self.assertEqual(result["version"], "v1.0.0-describe")

    @patch('shapely._version.render_git_describe_long', return_value="v1.0.0-describe-long")
    def test_render_git_describe_long_style(self, mock_render_git_describe_long):
        result = render(self.pieces, "git-describe-long")
        self.assertEqual(result["version"], "v1.0.0-describe-long")

    def test_render_unknown_style(self):
        with self.assertRaises(ValueError) as context:
            render(self.pieces, "unknown-style")
        self.assertIn("unknown style", str(context.exception))

    #testing render()
    def test_tagged_version(self):
        pieces = {
            "closest-tag": "v1.0.0",
            "distance": 5,
            "short": "abcdef1",
            "dirty": False
        }
        result = render_git_describe(pieces)
        self.assertEqual(result, "v1.0.0-5-gabcdef1")

    def test_untagged_version(self):
        pieces = {
            "closest-tag": None,
            "distance": 0,
            "short": "abcdef1",
            "dirty": False
        }
        result = render_git_describe(pieces)
        self.assertEqual(result, "abcdef1")


    def test_dirty_tagged_version(self):
        pieces = {
            "closest-tag": "v1.0.0",
            "distance": 5,
            "short": "abcdef1",
            "dirty": True
        }
        result = render_git_describe(pieces)
        self.assertEqual(result, "v1.0.0-5-gabcdef1-dirty")


    def test_dirty_untagged_version(self):
        pieces = {
            "closest-tag": None,
            "distance": 0,
            "short": "abcdef1",
            "dirty": True
        }
        result = render_git_describe(pieces)
        self.assertEqual(result, "abcdef1-dirty")


    def test_no_distance_tagged_version(self):
        pieces = {
            "closest-tag": "v1.0.0",
            "distance": 0,
            "short": "abcdef1",
            "dirty": False
        }
        result = render_git_describe(pieces)
        self.assertEqual(result, "v1.0.0")


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
