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

    def isAuthorized(self, roleTrees: RoleAccessPermissionDatas, request: Request) -> bool:
        """Check if the user is authenticated, by checking if the token exists, and if exists then refresh it

        Args:
            roleTrees (RoleAccessPermissionDatas): Trees with roles
            request (Request): The request used

        Returns:
            bool: If the token exists and then it's valid then the response is True, and it returns False otherwise
        """
        try:
            method = self.getMethod(request.method)
            for tree in roleTrees.role_access_permissions:
                if tree.role.name == "super_admin" or tree.role.name == "sys_admin":
                    return True

            for tree in roleTrees.role_access_permissions:
                for permissionObject in tree.permissions:
                    if (
                        hasattr(permissionObject.permission, "denied_actions")
                        and method in permissionObject.permission.denied_actions
                    ):
                        return False

                    exist = method in permissionObject.permission.allowed_actions
                    if exist:
                        for context in permissionObject.permission_contexts:
                            path = request.url.path
                            originalPath = self._convertToOriginalPath(urlPath=path, pathParams=request.path_params)
                            if 'path' in context.data and context.data['path'] == originalPath:
                                return True
            return False
        except Exception as e:
            logger.error({e})
            return False

    def _convertToOriginalPath(self, urlPath: str, pathParams: dict = None):
        if pathParams is not None and isinstance(pathParams, dict):
            for arg, value in pathParams.items():
                urlPath = urlPath.replace(value, f'{{{arg}}}')
        return urlPath

    def getMethod(self, method: str = None):
        from enum import Enum
        methodType: Enum
        if method not in [methodType.name for methodType in MethodType]:
            raise ValueError("Invalid method, it should be one of these: " + ", ".join([methodType.name for methodType in MethodType]))

        return MethodType[method]
