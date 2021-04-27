from starlette.requests import Request
from src.domain_model.authorization.AuthorizationService import AuthorizationService
from src.resource.logging.decorator import debugLogger
from src.port_adapter.api.rest.model.response.v1.identity.RoleAccessPermissionDatas import (
    RoleAccessPermissionDatas,
)


class AuthorizationApplicationService:
    def __init__(self, authorizationService: AuthorizationService):
        self._authorizationService: AuthorizationService = authorizationService

    @debugLogger
    def isAuthorized(self, roleTrees: RoleAccessPermissionDatas, request: Request) -> bool:
        """Check if the user is authenticated based on the token

        Args:
            roleTrees (RoleAccessPermissionDatas): Trees with roles
            request (Request): The request used

        Returns:
            bool: True if the user is authenticated, False otherwise

        """
        return self._authorizationService.isAuthorized(roleTrees=roleTrees, request=request)
