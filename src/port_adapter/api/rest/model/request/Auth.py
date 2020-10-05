"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from pydantic import BaseModel


class Auth(BaseModel):
    id: str
    name: str
    password: str

