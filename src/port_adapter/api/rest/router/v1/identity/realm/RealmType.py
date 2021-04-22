"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from enum import Enum


class RealmType(str, Enum):
    PROVIDER = "provider"
    BENEFICIARY = "beneficiary"
    TENANT = "tenant"
