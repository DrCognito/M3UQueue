import enum
import m3uqueue.discriminators as disc


class MediaType(enum.Enum):
    Path = enum.auto()
    Url = enum.auto()
    Unknown = enum.auto()


class MediaStatus(enum.Enum):
    Good = enum.auto()
    Bad = enum.auto()
    Unknown = enum.auto()


class MediaPath:
    def __init__(self, path: str = None):
        self.path = path
        self._type: MediaType = None
        self.status = MediaStatus.Unknown

    @property
    def type(self):
        if self._type is not None:
            return self._type

        if disc.is_url(self.path):
            self._type = MediaType.Url
        else:
            self._type = MediaType.Path

        return self._type

    def update_status(self):
        if self.type == MediaType.Url:
            if disc.url_accessable(self.path):
                self.status = MediaStatus.Good
            else:
                self.status = MediaStatus.Bad
        elif self.type == MediaType.Path:
            pass
        else:
            raise TypeError(f"Unknown MediaType {self._type}")

        return self.status
