"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, ForwardRef

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.Resource import Resource

AccessNode = ForwardRef('AccessNode')

class AccessNode(BaseModel):
    resource: Resource
    resource_name: str
    children: List[AccessNode] = []

AccessNode.update_forward_refs()
