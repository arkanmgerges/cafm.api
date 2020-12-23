"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


class InProgressException(Exception):
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__()
