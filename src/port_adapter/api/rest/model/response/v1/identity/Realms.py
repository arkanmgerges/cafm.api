"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.identity.Realm import RealmDescriptor


class Realms(BaseModel):
    realms: List[RealmDescriptor]
    total_item_count: int
