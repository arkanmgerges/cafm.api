"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import Optional

from pydantic import BaseModel


class Tag(BaseModel):
    id: str
    name: str


class TagDescriptor(Tag):
    pass
