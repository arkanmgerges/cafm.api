"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.authentication.AuthenticationService import AuthenticationService
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class AuthenticationApplicationService:
    def __init__(self, authService: AuthenticationService):
        self._authService: AuthenticationService = authService

    def hashPassword(self, password: str) -> str:
        """Hash password string

        Args:
            password (str): password string to hash

        Returns:
            str: password hash code
        """
        return self._authService.hashPassword(password=password)

    @debugLogger
    def isAuthenticated(self, token: str) -> bool:
        """Check if the user is authenticated based on the token

        Args:
            token (str): Token has information about the user

        Returns:
            bool: True if the user is authenticated, False otherwise

        """
        logger.debug(
            f"[{AuthenticationApplicationService.isAuthenticated.__qualname__}] - Received token: {token}"
        )
        return self._authService.isAuthenticated(token=token)
