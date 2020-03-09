from validator_collection import checkers
import pathlib
import requests
import time

URL_REQUEST_DELAY_S = 5


def is_url(location: str) -> bool:
    """Simple function checks if URL is valid and if it is a http or https URL.

    :param location: Path
    :type location: str
    :return: True or False
    :rtype: bool
    """
    location = location.lower()
    if not checkers.is_url(location):
        return False
    # valid url but we want https or http
    if location.startswith("http:") or location.startswith("https:"):
        return True

    return False


def file_exists(location: str) -> bool:
    pass


def url_accessable(location: str) -> bool:
    """Uses requests.head to test existance of file without download.
    Incurs a URL_REQUEST_DELAY_S (default 5) delay each time, 2s timeout.
    
    :param location: URL to test
    :type location: str
    :return: True or False
    :rtype: bool
    """
    try:
        requests.head(location, timeout=2)
    except IOError:
        return False
    finally:
        time.sleep(URL_REQUEST_DELAY_S)

    return True
