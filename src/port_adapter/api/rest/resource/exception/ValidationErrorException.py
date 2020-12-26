"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json


class ValidationErrorException(Exception):
    def __init__(self, data: dict):
        self.message = data['message']
        self.data = data['data']
        super().__init__()

    def __str__(self):
        return f'{{ "message": "<{self.__class__.__qualname__}> {self.message}", "data": {json.dumps(self.data)} }}'
