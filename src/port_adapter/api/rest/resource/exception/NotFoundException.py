"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


class NotFoundException(Exception):
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__()
