import enum
import m3uqueue.discriminators as disc


class MediaType(enum.Enum):
    Path = enum.auto()
    Url = enum.auto()
    Unknown = enum.auto()


class MediaPath:
    def __init__(self, path: str = None):
        self.path = path
        self._type: MediaType = None

    @property
    def type(self):
        if self._type is not None:
            return self._type

        if disc.is_url(self.path):
            self._type = MediaType.Url
        else:
            self._type = MediaType.Path

        return self._type
