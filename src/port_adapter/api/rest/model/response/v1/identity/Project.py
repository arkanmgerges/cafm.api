"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from pydantic import BaseModel


class Project(BaseModel):
    id: str
    name: str


class ProjectDescriptor(Project):
    pass
