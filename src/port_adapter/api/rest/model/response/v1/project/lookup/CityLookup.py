"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class CityLookup(BaseModel):
    id: int
    name: str

class CityLookupDescriptor(CityLookup):
    pass
