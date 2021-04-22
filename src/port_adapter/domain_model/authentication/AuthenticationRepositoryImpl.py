"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os

import redis

from src.domain_model.authentication.AuthenticationRepository import (
    AuthenticationRepository,
)
from src.port_adapter.api.rest.cache.RedisCache import RedisCache
from src.resource.logging.decorator import debugLogger


class AuthenticationRepositoryImpl(AuthenticationRepository):
    def __init__(self):
        try:
            import src.port_adapter.AppDi as AppDi

            cache = AppDi.instance.get(RedisCache)
            self._cache = cache.client()
            self._cacheSessionKeyPrefix = cache.cacheSessionKeyPrefix()
            self._refreshTokenTtl = cache.refreshTokenTtl()
        except Exception as e:
            raise Exception(
                f"[{AuthenticationRepositoryImpl.__init__.__qualname__}] Could not connect to the redis, message: {e}"
            )

    @debugLogger
    def persistToken(self, token: str, ttl: int = -1) -> None:
        ttl = ttl if ttl > 0 else self._refreshTokenTtl
        self._cache.setex(f"{self._cacheSessionKeyPrefix}{token}", ttl, token)

    @debugLogger
    def refreshToken(self, token: str, ttl: int = -1) -> None:
        ttl = ttl if ttl > 0 else self._refreshTokenTtl
        self._cache.setex(f"{self._cacheSessionKeyPrefix}{token}", ttl, token)

    @debugLogger
    def tokenExists(self, token: str) -> bool:
        return self._cache.exists(f"{self._cacheSessionKeyPrefix}{token}") == 1

    @debugLogger
    def deleteToken(self, token: str) -> None:
        return self._cache.delete(f"{self._cacheSessionKeyPrefix}{token}")
