"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


class UnknownCacheTypeException(Exception):
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__()
