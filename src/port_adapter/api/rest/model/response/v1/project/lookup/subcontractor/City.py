"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class City(BaseModel):
    id: int
    name: str

class CityDescriptor(City):
    pass
