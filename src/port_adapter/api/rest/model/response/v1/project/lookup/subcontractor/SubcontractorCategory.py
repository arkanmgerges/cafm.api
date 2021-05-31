"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class SubcontractorCategory(BaseModel):
    id: str
    name: str

class SubcontractorCategoryDescriptor(SubcontractorCategory):
    pass
