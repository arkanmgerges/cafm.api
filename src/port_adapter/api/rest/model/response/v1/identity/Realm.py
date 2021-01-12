"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from pydantic import BaseModel


class Realm(BaseModel):
    id: str
    name: str
    realm_type: str


class RealmDescriptor(Realm):
    pass
