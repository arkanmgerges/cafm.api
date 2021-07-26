"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import os
import pickle
import zlib
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.identity.AccessNode import AccessNode
from src.port_adapter.api.rest.model.response.v1.identity.AccessNodeData import (
    AccessNodeData,
)
from src.port_adapter.api.rest.model.response.v1.identity.Permission import Permission
from src.port_adapter.api.rest.model.response.v1.identity.PermissionContext import (
    PermissionContext,
)
from src.port_adapter.api.rest.model.response.v1.identity.PermissionWithPermissionContexts import (
    PermissionWithPermissionContexts,
)
from src.port_adapter.api.rest.model.response.v1.identity.Resource import Resource
from src.port_adapter.api.rest.model.response.v1.identity.Role import RoleDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.RoleAccessPermissionData import (
    RoleAccessPermissionDataDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.identity.RoleAccessPermissionDatas import (
    RoleAccessPermissionDatas,
)
from src.port_adapter.api.rest.model.response.v1.identity.Roles import Roles
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.role_app_service_pb2 import (
    RoleAppService_rolesResponse,
    RoleAppService_rolesRequest,
    RoleAppService_roleByIdRequest,
    RoleAppService_roleByIdResponse,
    RoleAppService_rolesTreesRequest,
    RoleAppService_rolesTreesResponse,
    RoleAppService_roleTreeRequest,
    RoleAppService_newIdRequest,
    RoleAppService_newIdResponse,
)
from src.resource.proto._generated.identity.role_app_service_pb2_grpc import (
    RoleAppServiceStub,
)


class RoleClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{RoleClient.newId.__qualname__}] - grpc call to retrieve roles from server {self._server}:{self._port}"
                )
                request = RoleAppService_newIdRequest()
                response: RoleAppService_newIdResponse = stub.new_id.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                RoleClient.newId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{RoleClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def rolesTrees(self, token: str = None) -> RoleAccessPermissionDatas:
        innerToken = self.token if token is None else token
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{RoleClient.rolesTrees.__qualname__}] - grpc call to retrieve roles from server {self._server}:{self._port}"
                )
                request = RoleAppService_rolesTreesRequest()
                response: RoleAppService_rolesTreesResponse = stub.roles_trees.with_call(
                    request,
                    metadata=(
                        ("token", innerToken),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                RoleClient.rolesTrees.__qualname__
                            ),
                        ),
                    ),
                )

                result = []
                roleAccessPermissionsBytesData = response[0].data
                roleAccessPermissionsData = pickle.loads(zlib.decompress(roleAccessPermissionsBytesData))
                logger.debug(
                    f"[{RoleClient.rolesTrees.__qualname__}] - grpc response after decompression: {roleAccessPermissionsData}"
                )
                for roleAccessPermissionDataItem in roleAccessPermissionsData:
                    role = self._descriptorByDataItem(
                        dataItem={**roleAccessPermissionDataItem["role"], **{'id': roleAccessPermissionDataItem["role"]['role_id']}} if "role" in roleAccessPermissionDataItem else None
                    )
                    # owned by
                    ownedBy = None
                    if ("owned_by" in roleAccessPermissionDataItem
                        and roleAccessPermissionDataItem["owned_by"] is not None
                        and "resource_id" in roleAccessPermissionDataItem["owned_by"]
                        and roleAccessPermissionDataItem["owned_by"]["resource_id"] is not None
                        and "type" in roleAccessPermissionsData
                        and roleAccessPermissionsData["type"] is not None
                    ):
                        ownedBy = self._resourceFromDataItem(
                            dataItem={**roleAccessPermissionDataItem["owned_by"],
                                      **{'id': roleAccessPermissionDataItem["owned_by"]['resource_id']}})

                    # owner of
                    ownerOfList = []
                    if "owner_of" in roleAccessPermissionDataItem and len(roleAccessPermissionDataItem["owner_of"]) > 0:
                        for ownerOfItem in roleAccessPermissionDataItem["owner_of"]:
                            ownerOfList.append(self._resourceFromDataItem({**ownerOfItem, **{'id': ownerOfItem['resource_id']}}))

                    # permissions with permission contexts
                    tmp = []
                    if "permissions" in roleAccessPermissionDataItem and \
                        len(roleAccessPermissionDataItem["permissions"]) > 0:
                        for (
                            permissionWithContext
                        ) in roleAccessPermissionDataItem["permissions"]:
                            pcs = []
                            if "permission_contexts" in permissionWithContext and len(permissionWithContext["permission_contexts"]) > 0:
                                for (
                                    permissionContext
                                ) in permissionWithContext["permission_contexts"]:
                                    pcs.append(
                                        self._permissionContextFromDataItem({**permissionContext, **{'id': permissionContext['permission_context_id']}})
                                    )

                                tmp.append(
                                    PermissionWithPermissionContexts(
                                        permission=self._permissionFromDataItem(
                                            {**permissionWithContext["permission"], **{'id': permissionWithContext["permission"]['permission_id']}}
                                        ),
                                        permission_contexts=pcs,
                                    )
                                )

                    # role access tree
                    result.append(
                        RoleAccessPermissionDataDescriptor(
                            role=role,
                            owned_by=ownedBy,
                            owner_of=ownerOfList,
                            permissions=tmp,
                            access_tree=self._accessNodeFromDataItem(
                                roleAccessPermissionDataItem["access_tree"]
                            ),
                        )
                    )
                return RoleAccessPermissionDatas(role_access_permissions=result)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def roleTree(self, roleId) -> RoleAccessPermissionDataDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{RoleClient.roleTree.__qualname__}] - grpc call to retrieve roles from server {self._server}:{self._port}"
                )
                request = RoleAppService_roleTreeRequest(role_id=roleId)
                response: RoleAppService_rolesTreesResponse = stub.role_tree.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                RoleClient.roleTree.__qualname__
                            ),
                        ),
                    ),
                )

                roleAccessPermissionBytesData = response[0].data
                roleAccessPermissionsData = pickle.loads(zlib.decompress(roleAccessPermissionBytesData))
                logger.debug(
                    f"[{RoleClient.roleTree.__qualname__}] - grpc response after decompression: {roleAccessPermissionsData}"
                )

                role = self._descriptorByDataItem(
                    dataItem={**roleAccessPermissionsData["role"], **{'id': roleAccessPermissionsData["role"][
                        'role_id']}} if "role" in roleAccessPermissionsData else None
                )
                # owned by
                ownedBy = None
                if ("owned_by" in roleAccessPermissionsData
                        and roleAccessPermissionsData["owned_by"] is not None
                        and "resource_id" in roleAccessPermissionsData["owned_by"]
                        and roleAccessPermissionsData["owned_by"]["resource_id"] is not None
                        and "type" in roleAccessPermissionsData
                        and roleAccessPermissionsData["type"] is not None):
                    ownedBy = self._resourceFromDataItem(
                        dataItem={**roleAccessPermissionsData["owned_by"],
                                  **{'id': roleAccessPermissionsData["owned_by"]['resource_id']}})

                # owner of
                ownerOfList = []
                if "owner_of" in roleAccessPermissionsData and len(roleAccessPermissionsData["owner_of"]) > 0:
                    for ownerOfItem in roleAccessPermissionsData["owner_of"]:
                        ownerOfList.append(
                            self._resourceFromDataItem({**ownerOfItem, **{'id': ownerOfItem['resource_id']}}))

                # permissions with permission contexts
                tmp = []
                if "permissions" in roleAccessPermissionsData and \
                        len(roleAccessPermissionsData["permissions"]) > 0:
                    for (
                            permissionWithContext
                    ) in roleAccessPermissionsData["permissions"]:
                        pcs = []
                        if "permission_contexts" in permissionWithContext and len(
                                permissionWithContext["permission_contexts"]) > 0:
                            for (
                                    permissionContext
                            ) in permissionWithContext["permission_contexts"]:
                                pcs.append(
                                    self._permissionContextFromDataItem({**permissionContext, **{
                                        'id': permissionContext['permission_context_id']}})
                                )

                            tmp.append(
                                PermissionWithPermissionContexts(
                                    permission=self._permissionFromDataItem(
                                        {**permissionWithContext["permission"],
                                         **{'id': permissionWithContext["permission"]['permission_id']}}
                                    ),
                                    permission_contexts=pcs,
                                )
                            )

                # role access tree

                return RoleAccessPermissionDataDescriptor(
                            role=role,
                            owned_by=ownedBy,
                            owner_of=ownerOfList,
                            permissions=tmp,
                            access_tree=self._accessNodeFromDataItem(
                                roleAccessPermissionsData["access_tree"]
                            ),
                        )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _resourceFromDataItem(self, dataItem):
        return Resource(id=dataItem["id"], type=dataItem["type"])

    def _permissionContextFromDataItem(self, dataItem):
        return PermissionContext(
            id=dataItem["id"], type=dataItem["type"], data=dataItem["data"]
        )

    def _accessNodeFromDataItem(self, dataItem):
        result = []
        if dataItem is not None and len(dataItem) > 0:
            for node in dataItem:
                children = self._accessNodeFromDataItem(node["children"])

                result.append(
                    AccessNode(
                        data=AccessNodeData(
                            content=node["content"],
                            content_type=node["content_type"],
                            context=node["context"],
                        ),
                        children=children,
                    )
                )
        return result

    def _permissionFromDataItem(self, dataItem):
        allowedActions = [x for x in dataItem["allowed_actions"]]
        deniedActions = [x for x in dataItem["denied_actions"]]
        return Permission(
            id=dataItem["id"],
            name=dataItem["name"],
            allowed_actions=allowedActions,
            denied_actions=deniedActions,
        )

    @OpenTelemetry.grpcTraceOTel
    def roles(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> Roles:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{RoleClient.roles.__qualname__}] - grpc call to retrieve roles from server {self._server}:{self._port}"
                )
                request = RoleAppService_rolesRequest(
                    result_from=resultFrom, result_size=resultSize
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: RoleAppService_rolesResponse = stub.roles.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                RoleClient.roles.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{RoleClient.roles.__qualname__}] - grpc response: {response}"
                )

                return Roles(
                    roles=[
                        self._descriptorByObject(obj=role) for role in response[0].roles
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def roleById(self, roleId) -> RoleDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{RoleClient.roleById.__qualname__}] - grpc call to retrieve role with roleId: {roleId} from server {self._server}:{self._port}"
                )
                response: RoleAppService_roleByIdResponse = stub.role_by_id.with_call(
                    RoleAppService_roleByIdRequest(id=roleId),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                RoleClient.roleById.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{RoleClient.roleById.__qualname__}] - grpc response: {response}"
                )

                return self._descriptorByObject(obj=response[0].role)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByDataItem(self, dataItem: Any) -> RoleDescriptor:
        if dataItem is not None:
            return RoleDescriptor(id=dataItem["id"], name=dataItem["name"], title=dataItem["title"])
        return None

    def _descriptorByObject(self, obj: Any) -> RoleDescriptor:
        if obj is not None:
            return RoleDescriptor(id=obj.id, name=obj.name, title=obj.title)
        return None
