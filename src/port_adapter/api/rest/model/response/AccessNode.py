"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, ForwardRef

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.AccessNodeData import AccessNodeData

AccessNode = ForwardRef('AccessNode')


class AccessNode(BaseModel):
    data: AccessNodeData
    children: List[AccessNode] = []


AccessNode.update_forward_refs()
