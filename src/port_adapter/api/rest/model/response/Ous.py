"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.Ou import Ou


class Ous(BaseModel):
    ous: List[Ou]
    itemCount: int
