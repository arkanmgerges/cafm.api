"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class StateLookup(BaseModel):
    id: str
    name: str

class StateLookupDescriptor(StateLookup):
    pass
