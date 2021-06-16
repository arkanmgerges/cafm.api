"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Optional

from pydantic import BaseModel


class UserHasOneTimePassword(BaseModel):
    result: bool


class UserHasOneTimePasswordDescriptor(UserHasOneTimePassword):
    pass