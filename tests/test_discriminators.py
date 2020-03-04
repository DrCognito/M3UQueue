from m3uqueue import discriminators as disc


def test_goodurls():
    urls = [
        "http://test.com/arrr.mkv",
        "https://test.com/arrr.mkv",
        "HTTPS://test.com/arrr.mkv",
        "HTTP://test.com/arrr.mkv",
    ]

    for i in urls:
        assert disc.is_url(i)


def test_badurls():
    urls = [
        "clearlynot a url",
        "httptrickedyou",
        "httpstoplying",
        "just_a_file.com",
        "/usr/notinternet/ohno",
        "C:\\Windows\\offline",
        "ftp://notawebserver/tastyfile.mkv"
    ]

    # assert not disc.is_url(url_1)
    for i in urls:
        res = disc.is_url(i)
        assert not res and res is not None


def test_absolutepath():
    path_1 = "C:\\test\\"
    path_2 = "/unix/path/"
    path_3 = "Z://test//t"

    assert disc.is_absolute_path(path_1)
    assert disc.is_absolute_path(path_2)
    assert disc.is_absolute_path(path_3)


def test_badabspaths():
    path_1 = "Https://arrr"
    path_2 = "sentence really"
    path_3 = "word"
