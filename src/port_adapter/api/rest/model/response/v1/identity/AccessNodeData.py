"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic.main import BaseModel


class AccessNodeData(BaseModel):
    content: dict
    content_type: str
    context: dict
