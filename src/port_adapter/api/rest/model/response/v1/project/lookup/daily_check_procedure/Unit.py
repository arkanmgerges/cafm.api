"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from pydantic import BaseModel


class Unit(BaseModel):
    id: str
    name: str


class UnitDescriptor(Unit):
    pass
