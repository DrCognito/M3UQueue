# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for m3uqueue.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import pytest
import pathlib


test_m3utemplate = pathlib.Path("./tests/test_files/test.template")
test_m3upath = pathlib.Path("./tests/test_files/test.m3u")


@pytest.fixture(scope="session", autouse=True)
def m3upath(request):
    return test_m3upath


def prepare_m3u(file_name: pathlib.Path, output_name: pathlib.Path):
    with open(file_name, "r") as file:
        data = file.read()

    # parents[0] should give the absolute path-directory of the file
    abs_path = file_name.absolute().parents[0]
    data = data.replace(r"{full_path}", str(abs_path))

    with open(output_name, "w") as file:
        file.write(data)

    return output_name


if not test_m3upath.exists() and test_m3utemplate.exists():
    prepare_m3u(test_m3utemplate, test_m3upath)
