from typing import List

from pydantic import BaseModel


class UnhashedKey(BaseModel):
    key: str


class UnhashedKeys(BaseModel):
    keys: List[UnhashedKey]
