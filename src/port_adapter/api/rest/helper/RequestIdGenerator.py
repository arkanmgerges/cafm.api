"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4


class RequestIdGenerator:
    @classmethod
    def generateId(cls):
        return str(uuid4())

    @classmethod
    def generateListId(cls, numberOfSuccesses: int = 1):
        from src.port_adapter.messaging.listener.CacheType import CacheType

        return f"{CacheType.listId()}:{str(uuid4())}:{numberOfSuccesses}"

    @classmethod
    def generateBulkId(cls):
        from src.port_adapter.messaging.listener.CacheType import CacheType
        return f"{CacheType.bulkId()}:{str(uuid4())}"