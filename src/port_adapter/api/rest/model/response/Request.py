"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from pydantic import BaseModel

class BoolRequestResponse(BaseModel):
    success: bool


class ResultRequestResponse(BaseModel):
    result: dict
