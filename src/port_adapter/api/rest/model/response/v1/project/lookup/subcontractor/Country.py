"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class Country(BaseModel):
    id: int
    name: str

class CountryDescriptor(Country):
    pass
