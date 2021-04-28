from fastapi import HTTPException
from fastapi.security import HTTPBearer
from starlette.requests import Request
from starlette.status import (
    HTTP_401_UNAUTHORIZED,
)

from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.identity.authz.AuthzClient import AuthzClient
from src.port_adapter.api.rest.grpc.v1.identity.role.RoleClient import RoleClient


class CustomAuthorization(HTTPBearer):
    def __init__(self):
        super().__init__()

    async def __call__(self, request: Request):
        ret = await super().__call__(request)
        import src.port_adapter.AppDi as AppDi

        client = RoleClient()
        authzClient = AppDi.instance.get(AuthzClient)

        Client.token = ret.credentials
        roleTrees = client.rolesTrees(token=ret.credentials)

        if ret is not None and not authzClient.isAuthorized(roleTrees=roleTrees, request=request):
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Invalid authorization",
            )
