"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Optional

from pydantic import BaseModel

class OrganizationLocation(BaseModel):
    organization_id: Optional[str]
    building_id: Optional[str]
    building_name: Optional[str]
    building_level_id: Optional[str]
    building_level_name: Optional[str]
    building_level_room_id: Optional[str]
    building_level_room_name: Optional[str]

class OrganizationLocationDescriptor(OrganizationLocation):
    pass
