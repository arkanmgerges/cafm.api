"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Optional

from pydantic import BaseModel


class HasUserPasswordSet(BaseModel):
    result: bool


class HasUserPasswordSetDescriptor(HasUserPasswordSet):
    pass