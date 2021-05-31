"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class State(BaseModel):
    id: str
    name: str

class StateDescriptor(State):
    pass
