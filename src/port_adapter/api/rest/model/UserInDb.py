"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.api.rest.model.User import User


class UserInDb(User):
    hashedPassword: str