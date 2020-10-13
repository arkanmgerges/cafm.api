"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from pydantic import BaseModel


class ResourceType(BaseModel):
    id: str
    name: str

