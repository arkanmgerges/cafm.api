"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel


class MessageDetail(BaseModel):
    message: str


class ValidationMessageDetail(BaseModel):
    message: str
    data: dict


class Message(BaseModel):
    detail: List[MessageDetail]


class ValidationMessage(BaseModel):
    detail: List[ValidationMessageDetail]
