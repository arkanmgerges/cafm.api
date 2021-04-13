"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import os

from fastapi import APIRouter, Request

from src.port_adapter.api.rest.model.response.v1.identity.Routes import Routes
from src.resource.common.Util import Util

router = APIRouter()


@router.get(path="/app_routes", summary='Get all routes', response_model=Routes)
async def appRoutes(request: Request):
    matchers = os.getenv('MICROSERVICES', [])
    if matchers:
        matchers = matchers.split(':')
    urlList = [
        {'path': route.path, 'name': Util.camelCaseToLoserSnakeCase(route.name), 'methods': route.methods} for route in request.app.routes if any(match in route.path for match in matchers)
    ]
    return Routes(routes=urlList, item_count=len(urlList))
