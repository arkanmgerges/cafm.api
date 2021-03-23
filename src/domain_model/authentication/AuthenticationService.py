"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import hashlib
import os

from src.domain_model.authentication.AuthenticationRepository import AuthenticationRepository
from src.resource.logging.decorator import debugLogger


class AuthenticationService:
    @debugLogger
    def __init__(self, authRepo: AuthenticationRepository):
        self._authRepo = authRepo

    def hashPassword(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def isAuthenticated(self, token: str) -> bool:
        """Check if the user is authenticated, by checking if the token exists, and if exists then refresh it

        Args:
            token (str): The token to be checked

        Returns:
            bool: If the token exists and then it's valid then the response is True, and it returns False otherwise
        """
        try:
            exists = self._authRepo.tokenExists(token=token)
            if exists:
                self._authRepo.refreshToken(token=token, ttl=int(os.getenv('CAFM_IDENTITY_USER_AUTH_TTL_IN_SECONDS', 300)))
            return exists
        except:
            return False