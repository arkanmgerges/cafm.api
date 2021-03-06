from enum import Enum


class MethodType(str, Enum):
    GET = "read"
    POST = "create"
    PUT = "update"
    PATCH = "update"
    DELETE = "delete"
