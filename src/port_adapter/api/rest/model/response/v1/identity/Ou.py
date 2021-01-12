"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class Ou(BaseModel):
    id: str
    name: str
    description: str


class OuDescriptor(Ou):
    pass
