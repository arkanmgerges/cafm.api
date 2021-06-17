from starlette.requests import Request

from src.domain_model.authorization.MethodType import MethodType
from src.port_adapter.api.rest.model.response.v1.identity.RoleAccessPermissionDatas import (
    RoleAccessPermissionDatas,
)
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class AuthorizationService:
    @debugLogger
    def __init__(self):
        super().__init__()

    @staticmethod
    def isAuthorized(roleTrees: RoleAccessPermissionDatas, request: Request) -> bool:
        """Check if the user is authenticated, by checking if the token exists, and if exists then refresh it

        Args:
            roleTrees (RoleAccessPermissionDatas): Trees with roles
            request (Request): The request used

        Returns:
            bool: If the token exists and then it's valid then the response is True, and it returns False otherwise
        """
        try:
            method = AuthorizationService.getMethod(request.method)
            for tree in roleTrees.role_access_permissions:
                if tree.role.name == "super_admin" or tree.role.name == "sys_admin":
                    return True

            for tree in roleTrees.role_access_permissions:
                if len(tree.permissions) == 0:
                    return False

                for permissionObject in tree.permissions:
                    if (
                        hasattr(permissionObject.permission, "denied_actions")
                        and permissionObject.permission.denied_actions == method
                    ):
                        return False

                    exist = next((x for x in permissionObject.permission.allowed_actions if x == method), [False])

                    if exist is not False:
                        for context in permissionObject.permission_contexts:
                            path = request.url.path
                            if 'path' in context.data and context.data['path'] == path:
                                return True
            return False
        except Exception as e:
            logger.error({e})
            return False

    @staticmethod
    def getMethod(method: str = None):
        if method not in [e.name for e in MethodType]:
            raise ValueError("Invalid method, it should be one of these: " + ", ".join([e.name for e in MethodType]))

        return MethodType[method]
