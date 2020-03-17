from m3uqueue import mediapath
import pytest
import pathlib
from typing import List


def test_abspath():
    path_1 = str(pathlib.Path("./tests/test_files/text1.txt").absolute())
    test_1 = mediapath.MediaPath(path_1)

    path_2 = str(pathlib.Path("./tests/test_files/nofile_none.none").absolute())
    test_2 = mediapath.MediaPath(path_2)

    assert test_1.status == mediapath.MediaStatus.Unknown
    assert test_2.status == mediapath.MediaStatus.Unknown

    test_1.update_status()
    test_2.update_status()

    assert test_1.status == mediapath.MediaStatus.Good
    assert test_2.status == mediapath.MediaStatus.Bad


def test_relpath():
    # Base path should be module dir
    path_1 = "LICENSE.txt"
    path_2 = "tests/test_files/text1.txt"
    path_3 = "notvalid.none"
    path_4 = "tests/test_files/notvalid.none"

    test_1 = mediapath.MediaPath(path_1)
    test_2 = mediapath.MediaPath(path_2)
    test_3 = mediapath.MediaPath(path_3)
    test_4 = mediapath.MediaPath(path_4)

    test_1.update_status()
    test_2.update_status()
    test_3.update_status()
    test_4.update_status()

    assert test_1.status == mediapath.MediaStatus.Good
    assert test_2.status == mediapath.MediaStatus.Good
    assert test_3.status == mediapath.MediaStatus.Bad
    assert test_4.status == mediapath.MediaStatus.Bad


def test_changebasedir():
    path_1 = "LICENSE.txt"
    test_1 = mediapath.MediaPath(path_1)
    test_1.update_status()
    assert test_1.status == mediapath.MediaStatus.Good

    test_1.base_dir = pathlib.Path("./tests/test_files/")
    test_1.path = "text1.txt"
    test_1.update_status()
    assert test_1.status == mediapath.MediaStatus.Good

    test_1.path = "not a proper path ~~#"
    test_1.update_status()
    assert test_1.status == mediapath.MediaStatus.Bad


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


def test_loadm3u(m3upath):
    with open(m3upath, "r") as file:
        m3u_text = file.read()

    assert r"{full_path}" not in m3u_text

    media_list = mediapath.loadm3u(m3u_text)

    assert len(media_list) == 6
