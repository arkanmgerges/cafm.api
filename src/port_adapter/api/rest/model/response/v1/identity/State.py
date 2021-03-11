"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from pydantic import BaseModel


class State(BaseModel):
    id: int
    name: str


class StateDescriptor(State):
    pass
