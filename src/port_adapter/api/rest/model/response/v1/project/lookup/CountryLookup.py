"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class CountryLookup(BaseModel):
    id: int
    name: str

class CountryLookupDescriptor(CountryLookup):
    pass
