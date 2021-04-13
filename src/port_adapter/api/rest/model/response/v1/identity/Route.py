"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel


class Route(BaseModel):
    path: str
    name: str
    methods: List[str]


class RouteDescriptor(Route):
    pass
