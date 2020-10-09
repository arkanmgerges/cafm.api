"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

import redis
from redis.client import Redis


class RedisCache:
    def __init__(self):
        try:
            self.cache: Redis = redis.Redis(host=os.getenv('CAFM_API_REDIS_HOST', 'localhost'),
                                            port=os.getenv('CAFM_API_REDIS_PORT', 6379))
            self.cacheResponseKeyPrefix = os.getenv('CAFM_API_REDIS_RSP_KEY_PREFIX', 'cafm.api.rsp.')
        except Exception as e:
            raise Exception(
                f'[{RedisCache.__init__.__qualname__}] Could not connect to the redis, message: {e}')

    def client(self) -> Redis:
        return self.cache

    def cacheResponseKeyPrefix(self):
        return self.cacheResponseKeyPrefix
