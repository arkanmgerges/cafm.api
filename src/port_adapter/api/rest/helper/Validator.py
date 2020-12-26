"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import validators

from src.port_adapter.api.rest.resource.exception.ValidationErrorException import ValidationErrorException


class Validator:
    @classmethod
    def validateEmail(cls, email: str, fields: dict) -> bool:
        if not validators.email(email):
            raise ValidationErrorException({"message": f'email is not valid: {email}', "data": fields})
        return True
