"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.portadapter.api.rest.model.User import User


class UserInDb(User):
    hashedPassword: str