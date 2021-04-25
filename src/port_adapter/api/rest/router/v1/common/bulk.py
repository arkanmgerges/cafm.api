"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

from fastapi import APIRouter, Body, Request
from starlette import status

import src.port_adapter.api.rest.router.v1.util
import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.identity.ou.OuClient import OuClient
from src.port_adapter.api.rest.grpc.v1.identity.permission.PermissionClient import PermissionClient
from src.port_adapter.api.rest.grpc.v1.identity.permission_context.PermissionContextClient import \
    PermissionContextClient
from src.port_adapter.api.rest.grpc.v1.identity.project.ProjectClient import ProjectClient
from src.port_adapter.api.rest.grpc.v1.identity.realm.RealmClient import RealmClient
from src.port_adapter.api.rest.grpc.v1.identity.role.RoleClient import RoleClient
from src.port_adapter.api.rest.grpc.v1.identity.user_group.UserGroupClient import UserGroupClient
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.port_adapter.messaging.common.model.IdentityCommand import IdentityCommand
from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()

appRoutes = []

@router.post(
    "/_bulk", summary="Create a bulk request", status_code=status.HTTP_201_CREATED
)
@OpenTelemetry.fastApiTraceOTel
async def createBulk(
    *,
    request: Request,
    # _=Depends(CustomHttpBearer()),
    body: dict = Body(..., description="Json data of the bulk", embed=True),
):
    from src.resource.logging.logger import logger
    global appRoutes
    #todo remove me
    Client.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImJkNDg2Y2Y4LWVmYTctNGQ4Zi1iYmUyLTE1NGI0YTk4NGEyNCIsInJvbGVzIjpbeyJpZCI6IjJiZDMxYThjLTgzOTYtNGU2Zi05YjU2LTlmNzViMjU5ZDQ0NSIsIm5hbWUiOiJzdXBlcl9hZG1pbiIsInRpdGxlIjpudWxsfV0sImVtYWlsIjoiYWRtaW5AbG9jYWwubWUiLCJfdG9rZW5fZ2VuX251bSI6ImZmZDY1YzhlLWE1YWItMTFlYi05MDk1LTAyNDJhYzEyMDAxMiJ9.LftHoRXX31sh59OPja-0wxb4Ya8A0727zx6Wtz1vyTQ"
    appRoutesResult = await src.port_adapter.api.rest.router.v1.util.appRoutes(request=request)
    appRoutes = appRoutesResult.routes
    reqId = RequestIdGenerator.generateBulkId()
    dataBody = []
    index = 0
    itemCount = len(body["data"])
    for dataItem in body["data"]:
        for command, commandData in dataItem.items():
            obj = extractData(command=command, commandData=commandData)
            dataBody.append({"_index": index, "_request_data": {"command": command, "command_data": commandData["data"]},
                             "_inner_data": {"microservice_name": obj.microserviceName, "api_path": obj.apiPath}})
            index += 1
    messageRequestData = {"data": dataBody, "item_count": itemCount}
    logger.debug(messageRequestData)

    producer = AppDi.instance.get(SimpleProducer)
    # producer.produce(
    #     obj=IdentityCommand(
    #         id=reqId,
    #         name=CommandConstant.PROCESS_BULK.value,
    #         metadata=json.dumps({"token": Client.token}),
    #         data=json.dumps(messageRequestData),
    #         external=[],
    #     ),
    #     schema=IdentityCommand.get_schema(),
    # )

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.PROCESS_BULK.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(messageRequestData),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


def extractData(command: str, commandData: dict):
    microserviceName = ''
    for route in appRoutes:
        if route.name == command:
            if '/v1/identity/' in route.path:
                microserviceName = 'identity'
            elif '/v1/project/' in route.path:
                microserviceName = 'project'
            else:
                microserviceName = 'unknown'

            entityName = command.replace('create_', '')
            data = commandData["data"]
            if 'create_' in command and entityName in grpcClientList:
                data[f'{entityName}_id'] = grpcClientList[entityName].newId()
            return ItemDetail(microserviceName=microserviceName, apiPath=route.path, commandData=data)
    return ItemDetail(microserviceName='unknown', apiPath='', commandData='')

class ItemDetail:
    def __init__(self, microserviceName, apiPath, commandData):
        self.microserviceName = microserviceName
        self.apiPath = apiPath
        self.commandData = commandData

    def __repr__(self):
        return f'microserviceName: {self.microserviceName}, apiPath: {self.apiPath}, commandData: {self.commandData}'

grpcClientList = {
    'ou': OuClient(),
    'realm': RealmClient(),
    'permission': PermissionClient(),
    'permission_context': PermissionContextClient(),
    'project': ProjectClient(),
    'role': RoleClient(),
    'user_group': UserGroupClient(),
}