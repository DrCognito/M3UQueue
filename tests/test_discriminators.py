from m3uqueue import discriminators as disc
import pytest


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
        "ftp://notawebserver/tastyfile.mkv",
    ]

    # assert not disc.is_url(url_1)
    for i in urls:
        res = disc.is_url(i)
        assert not res and res is not None


def test_absolutepath():
    paths = [
        "C:\\test\\",
        "/unix/path/",
        "Z://test//t",
    ]

    for p in paths:
        assert disc.is_absolute_path(p)


def test_badabspaths():
    paths = [
        "sentence really",
        "word",
        "Https://arrr",
    ]

    for p in paths:
        res = disc.is_absolute_path(p)
        print(p)
        assert not res and res is not None


# @pytest.mark.skip("Long due to URL access time waiting")
def test_urlaccessable():
    urls = [
        "https://www.google.com/robots.txt",
        "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
    ]

    for url in urls:
        assert disc.url_accessable(url) is True


# @pytest.mark.skip("Long due to URL access time waiting")
def test_badurlaccessable():
    urls = [
        "actually just a string",
        "xml://somewherenonesense.com/notfile/txt",
        "http://something.invalid/juicyfile.iso",
    ]

    for url in urls:
        assert disc.url_accessable(url) is False
