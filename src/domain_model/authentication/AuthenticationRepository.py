"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod


class AuthenticationRepository(ABC):
    @abstractmethod
    def refreshToken(self, token: str, ttl: int = 300) -> None:
        """Refresh the ttl of the token

        Args:
            token (str): The token to be refreshed
            ttl (int): time to live measured in seconds, if the ttl is -1 then the token will be persisted forever
        """

    @abstractmethod
    def tokenExists(self, token: str) -> bool:
        """Check if the token does exist

        Args:
            token (str): The token to be checked

        Returns:
            bool: If True then the token exists, False if it does not exist
        """
