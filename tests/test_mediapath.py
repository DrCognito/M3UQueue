from m3uqueue import mediapath


def test_pathadd():
    test = mediapath.MediaPath("./conftest.py")

    assert test.path == "./conftest.py"


def test_pathtype():
    test = mediapath.MediaPath("./conftest.py")

    assert test.type == mediapath.MediaType.Path

    test_url = mediapath.MediaPath("http://test.com/arrr.mkv")

    assert test_url.type == mediapath.MediaType.Url


def test_mediatypes():
    assert mediapath.MediaType.Path is not None
    assert mediapath.MediaType.Url is not None
    assert mediapath.MediaType.Unknown is not None


def test_mediastatus():
    assert mediapath.MediaStatus.Good is not None
    assert mediapath.MediaStatus.Bad is not None
    assert mediapath.MediaStatus.Unknown is not None
