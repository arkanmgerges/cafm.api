"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.identity.HashedKey import (
    HashedKeyDescriptor,
)


class HashedKeys(BaseModel):
    hashed_keys: List[HashedKeyDescriptor]
    total_item_count: int
