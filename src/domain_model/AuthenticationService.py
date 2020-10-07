"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import hashlib


class AuthenticationService:
    def hashPassword(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
