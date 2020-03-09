from m3uqueue import mediapath
import pytest


def test_pathadd():
    test = mediapath.MediaPath("./conftest.py")

    assert test.path == "./conftest.py"


def test_pathtype():
    test = mediapath.MediaPath("./conftest.py")

    assert test.type == mediapath.MediaType.Path

    test_url = mediapath.MediaPath("http://test.com/arrr.mkv")

    assert test_url.type == mediapath.MediaType.Url


def test_statusurls():
    existing = "https://www.google.com/robots.txt"
    missing = "https://www.google.invalid/robots.txt"

    test_1 = mediapath.MediaPath(existing)
    test_2 = mediapath.MediaPath(missing)

    assert test_1.status == mediapath.MediaStatus.Unknown
    assert test_2.status == mediapath.MediaStatus.Unknown

    test_1.update_status()
    test_2.update_status()

    assert test_1.status == mediapath.MediaStatus.Good
    assert test_2.status == mediapath.MediaStatus.Bad


def test_status_unknownfails():
    dummy = ""
    test_1 = mediapath.MediaPath(dummy)
    test_1._type = mediapath.MediaType.Unknown

    with pytest.raises(TypeError) as excinfo:
        test_1.update_status()

    assert str(excinfo.value).startswith("Unknown MediaType")


def test_mediatypes():
    assert mediapath.MediaType.Path is not None
    assert mediapath.MediaType.Url is not None
    assert mediapath.MediaType.Unknown is not None


def test_mediastatus():
    assert mediapath.MediaStatus.Good is not None
    assert mediapath.MediaStatus.Bad is not None
    assert mediapath.MediaStatus.Unknown is not None
