"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from pydantic import BaseModel


class State(BaseModel):
    id: str
    name: str


class StateDescriptor(State):
    pass
