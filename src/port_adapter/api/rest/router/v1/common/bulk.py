"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import re

from fastapi import APIRouter, Body, Request
from fastapi.params import Depends
from starlette import status

import src.port_adapter.AppDi as AppDi
import src.port_adapter.api.rest.router.v1.util
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.identity.ou.OuClient import OuClient
from src.port_adapter.api.rest.grpc.v1.identity.permission.PermissionClient import PermissionClient
from src.port_adapter.api.rest.grpc.v1.identity.permission_context.PermissionContextClient import (
    PermissionContextClient,
)
from src.port_adapter.api.rest.grpc.v1.project.project.ProjectClient import ProjectClient
from src.port_adapter.api.rest.grpc.v1.identity.user_group.UserGroupClient import UserGroupClient
from src.port_adapter.api.rest.grpc.v1.project.daily_check.procedure.DailyCheckProcedureClient import (
    DailyCheckProcedureClient,
)
from src.port_adapter.api.rest.grpc.v1.project.daily_check.procedure.operation.DailyCheckProcedureOperationClient import (
    DailyCheckProcedureOperationClient,
)
from src.port_adapter.api.rest.grpc.v1.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterClient import (
    DailyCheckProcedureOperationParameterClient,
)
from src.port_adapter.api.rest.grpc.v1.project.equipment.EquipmentClient import EquipmentClient
from src.port_adapter.api.rest.grpc.v1.project.equipment.category.group.EquipmentCategoryGroupClient import (
    EquipmentCategoryGroupClient,
)
from src.port_adapter.api.rest.grpc.v1.project.equipment.input.EquipmentInputClient import EquipmentInputClient
from src.port_adapter.api.rest.grpc.v1.project.equipment.model.EquipmentModelClient import EquipmentModelClient
from src.port_adapter.api.rest.grpc.v1.project.equipment.project_category.EquipmentProjectCategoryClient import (
    EquipmentProjectCategoryClient,
)
from src.port_adapter.api.rest.grpc.v1.project.maintenance.procedure.MaintenanceProcedureClient import (
    MaintenanceProcedureClient,
)
from src.port_adapter.api.rest.grpc.v1.project.maintenance.procedure.operation.MaintenanceProcedureOperationClient import (
    MaintenanceProcedureOperationClient,
)
from src.port_adapter.api.rest.grpc.v1.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameterClient import (
    MaintenanceProcedureOperationParameterClient,
)
from src.port_adapter.api.rest.grpc.v1.project.maintenance.standard_procedure.StandardMaintenanceProcedureClient import (
    StandardMaintenanceProcedureClient,
)
from src.port_adapter.api.rest.grpc.v1.project.manufacturer.ManufacturerClient import ManufacturerClient
from src.port_adapter.api.rest.grpc.v1.project.organization.OrganizationClient import OrganizationClient
from src.port_adapter.api.rest.grpc.v1.project.standard_equipment.StandardEquipmentClient import StandardEquipmentClient
from src.port_adapter.api.rest.grpc.v1.project.standard_equipment.standard_category.StandardEquipmentCategoryClient import (
    StandardEquipmentCategoryClient,
)
from src.port_adapter.api.rest.grpc.v1.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupClient import (
    StandardEquipmentCategoryGroupClient,
)
from src.port_adapter.api.rest.grpc.v1.project.subcontractor.SubcontractorClient import SubcontractorClient
from src.port_adapter.api.rest.grpc.v1.project.subcontractor.category.SubcontractorCategoryClient import (
    SubcontractorCategoryClient,
)
from src.port_adapter.api.rest.grpc.v1.project.unit.UnitClient import UnitClient
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.router.v1.common.BulkBodyData import BulkBodyData, BulkBodyDataItemValue
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.port_adapter.messaging.common.model.IdentityCommand import IdentityCommand
from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()

appRoutes = []
microserviceNamePatternCompiled = re.compile("/v[0-9]/([^/]+)?/")


@router.post("/_bulk", summary="Create a bulk request", status_code=status.HTTP_201_CREATED)
@OpenTelemetry.fastApiTraceOTel
async def createBulk(
    *,
    request: Request,
    _=Depends(CustomHttpBearer()),
    body: BulkBodyData = Body(..., description="Json data of the bulk", embed=True),
):
    from src.resource.logging.logger import logger

    global appRoutes
    appRoutesResult = await src.port_adapter.api.rest.router.v1.util.appRoutes(request=request)
    appRoutes = appRoutesResult.routes
    reqId = RequestIdGenerator.generateBulkId()
    dataBody = []
    index = 0
    totalItemCount = len(body.data)
    for dataItem in body.data:
        for command, commandData in dataItem.items():
            obj = extractData(command=command, commandData=commandData)
            dataBody.append(
                {
                    "_index": index,
                    "_request_data": {"command": command, "command_data": obj.commandData},
                    "_inner_data": {"microservice_name": obj.microserviceName, "api_path": obj.apiPath},
                }
            )
            index += 1
    batchedDataItems = _batchByMicroserviceName(dataBody)
    producer = AppDi.instance.get(SimpleProducer)

    for microserviceName, dataBodyItems in batchedDataItems.items():
        messageRequestData = {"data": dataBodyItems, "total_item_count": totalItemCount}
        if microserviceName == "identity":
            producer.produce(
                obj=IdentityCommand(
                    id=reqId,
                    name=CommandConstant.PROCESS_BULK.value,
                    metadata=json.dumps({"token": Client.token}),
                    data=json.dumps(messageRequestData),
                    external=[],
                ),
                schema=IdentityCommand.get_schema(),
            )
        elif microserviceName == "project":
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


def _batchByMicroserviceName(data):
    result = {}
    for item in data:
        microserviceName = item["_inner_data"]["microservice_name"]
        if microserviceName not in result:
            result[microserviceName] = []
        result[microserviceName].append(item)
    return result


def extractData(command: str, commandData: BulkBodyDataItemValue):
    for route in appRoutes:
        if route.name == command:
            microserviceName = _extractMicroserviceName(route.path)
            if microserviceName is not None:
                data = commandData.data
                entityName = command[command.index("_") + 1 :]
                # If it is a create, then add the id and use newId()
                if "create_" in command and entityName in entityToGrpcClientList:
                    if entityName == "building":
                        data[f"{entityName}_id"] = entityToGrpcClientList[entityName].newBuildingId()
                    elif entityName == "building_level":
                        data[f"{entityName}_id"] = entityToGrpcClientList[entityName].newBuildingLevelId()
                    elif entityName == "building_level_room":
                        data[f"{entityName}_id"] = entityToGrpcClientList[entityName].newBuildingLevelRoomId()
                    elif entityName == "permission":
                        data[f"{entityName}_id"] = entityToGrpcClientList[entityName].idByString(string=data["name"])
                    elif entityName == "permission_context":
                        stringArray = [str(x) for x in data["data"].values()]
                        stringArray.append(data["type"])
                        data[f"{entityName}_id"] = entityToGrpcClientList[entityName].idByString(string="".join(stringArray))
                    else:
                        data[f"{entityName}_id"] = entityToGrpcClientList[entityName].newId()
                return ItemDetail(microserviceName=microserviceName, apiPath=route.path, commandData=data)
    return ItemDetail(microserviceName="unknown", apiPath="", commandData="")


def _extractMicroserviceName(routePath):
    m = microserviceNamePatternCompiled.search(routePath)
    if m.group(1):
        return m.group(1)
    else:
        return None


class ItemDetail:
    def __init__(self, microserviceName, apiPath, commandData):
        self.microserviceName = microserviceName
        self.apiPath = apiPath
        self.commandData = commandData

    def __repr__(self):
        return f"microserviceName: {self.microserviceName}, apiPath: {self.apiPath}, commandData: {self.commandData}"


entityToGrpcClientList = {
    # 'realm': RealmClient(),
    # 'project': ProjectClient(),
    # 'user': UserClient(),
    # 'role': RoleClient(),
    "ou": OuClient(),
    "permission": PermissionClient(),
    "permission_context": PermissionContextClient(),
    "user_group": UserGroupClient(),
    "organization": OrganizationClient(),
    "unit": UnitClient(),
    "building": ProjectClient(),
    "building_level": ProjectClient(),
    "building_level_room": ProjectClient(),
    "subcontractor": SubcontractorClient(),
    "subcontractor_category": SubcontractorCategoryClient(),
    "equipment": EquipmentClient(),
    "equipment_category_group": EquipmentCategoryGroupClient(),
    "equipment_input": EquipmentInputClient(),
    "equipment_model": EquipmentModelClient(),
    "equipment_project_category": EquipmentProjectCategoryClient(),
    "daily_check_procedure": DailyCheckProcedureClient(),
    "daily_check_procedure_operation": DailyCheckProcedureOperationClient(),
    "daily_check_procedure_operation_parameter": DailyCheckProcedureOperationParameterClient(),
    "maintenance_procedure": MaintenanceProcedureClient(),
    "maintenance_procedure_operation": MaintenanceProcedureOperationClient(),
    "maintenance_procedure_operation_parameter": MaintenanceProcedureOperationParameterClient(),
    "standard_maintenance_procedure": StandardMaintenanceProcedureClient(),
    "manufacturer": ManufacturerClient(),
    "standard_equipment": StandardEquipmentClient(),
    "standard_equipment_category": StandardEquipmentCategoryClient(),
    "standard_equipment_category_group": StandardEquipmentCategoryGroupClient(),
}
