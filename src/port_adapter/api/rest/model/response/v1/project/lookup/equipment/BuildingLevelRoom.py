"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from pydantic import BaseModel


class BuildingLevelRoom(BaseModel):
    id: str
    name: str
    description: str
    # index: int


class BuildingLevelRoomDescriptor(BuildingLevelRoom):
    pass
