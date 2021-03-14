"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os

import redis

from src.domain_model.authentication.AuthenticationRepository import AuthenticationRepository
from src.port_adapter.api.rest.cache.RedisCache import RedisCache
from src.resource.logging.decorator import debugLogger


class AuthenticationRepositoryImpl(AuthenticationRepository):
    def __init__(self):
        try:
            import src.port_adapter.AppDi as AppDi
            self._cache = AppDi.instance.get(RedisCache).client()
            self._cacheSessionKeyPrefix = os.getenv('CAFM_IDENTITY_REDIS_SESSION_KEY_PREFIX',
                                                    'cafm.identity.session.')
        except Exception as e:
            raise Exception(
                f'[{AuthenticationRepositoryImpl.__init__.__qualname__}] Could not connect to the redis, message: {e}')

    @debugLogger
    def refreshToken(self, token: str, ttl: int = 300) -> None:
        self._cache.setex(f'{self._cacheSessionKeyPrefix}{token}', ttl, token)

    @debugLogger
    def tokenExists(self, token: str) -> bool:
        return self._cache.exists(f'{self._cacheSessionKeyPrefix}{token}') == 1
