"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class Ou(BaseModel):
    id: str
    name: str


class OuDescriptor(Ou):
    pass
