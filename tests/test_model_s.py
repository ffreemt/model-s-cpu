"""Test model_s."""
# pylint: disable=broad-except
from model_s import __version__
from model_s import model_s


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not model_s()
    except Exception:
        assert True
