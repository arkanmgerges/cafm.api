"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


class NotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__()

    def __str__(self):
        return f"<{self.__class__.__qualname__}> {self.message}"
