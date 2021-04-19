"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from fastapi import APIRouter, Request, Body

from src.port_adapter.api.rest.grpc.v1.identity.authz.AuthzClient import AuthzClient
from src.port_adapter.api.rest.model.response.v1.identity.HashedKeys import HashedKeys
from src.port_adapter.api.rest.model.response.v1.identity.Routes import Routes
from src.port_adapter.api.rest.router.v1.util.UnhashedKeys import UnhashedKeys
from src.resource.common.Util import Util

router = APIRouter()


@router.get(path="/app_routes", summary='Get all routes', response_model=Routes)
async def appRoutes(request: Request):
    matchers = os.getenv('MICROSERVICES', [])
    if matchers:
        matchers = matchers.split(':')
    urlList = [
        {'path': route.path, 'name': Util.camelCaseToLoserSnakeCase(route.name), 'methods': list(map(lambda x: x.lower(), route.methods))} for route in
        request.app.routes if any(match in route.path for match in matchers)
    ]
    return Routes(routes=urlList, item_count=len(urlList))


@router.post(path="/hash_keys", summary='Hash keys', response_model=HashedKeys)
async def hashKeys(*,
                   unhashed_keys: UnhashedKeys = Body(..., description='name of unit', embed=True), ):
    client = AuthzClient()
    result = client.hashKeys(unhashedKeys=unhashed_keys)
    return result
