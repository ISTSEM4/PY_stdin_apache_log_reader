from enum import Enum


class Attribute(Enum):
    REMOTE_HOST = 1
    REMOTE_USER = 2
    AUTHENTICATED_USER = 3
    DATE = 4
    TIME = 5
    TIME_ZONE = 6
    HTTP_METHOD = 7
    PATH_INFO = 8
    HTTP_VERSION = 9
    STATUS_CODE = 10
    RESPONSE_SIZE = 11
