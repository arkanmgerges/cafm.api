"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class HashedKey(BaseModel):
    key: str
    hash_code: str


class HashedKeyDescriptor(HashedKey):
    pass
