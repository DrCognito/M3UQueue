from validator_collection import checkers


def is_url(location: str) -> bool:
    location = location.lower()
    if not checkers.is_url(location):
        return False
    # valid url but we want https or http
    if location.startswith("http") or location.startswith("https"):
        return True

    return False


def is_absolute_path(location: str) -> bool:
    pass


def file_exists(location: str) -> bool:
    pass


def url_accessable(location: str) -> bool:
    pass
