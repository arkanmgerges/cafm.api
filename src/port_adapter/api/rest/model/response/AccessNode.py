"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, ForwardRef, Any

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.Resource import Resource

AccessNode = ForwardRef('AccessNode')

class AccessNodeData:
    _content: Any
    _type: str
    _context: dict

class AccessNode(BaseModel):
    resource: Resource
    resource_name: str
    data: AccessNodeData
    children: List[AccessNode] = []



AccessNode.update_forward_refs()
