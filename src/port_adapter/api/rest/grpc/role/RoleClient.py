"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import os
from typing import List

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.AccessNode import AccessNode
from src.port_adapter.api.rest.model.response.AccessNodeData import AccessNodeData
from src.port_adapter.api.rest.model.response.Permission import Permission
from src.port_adapter.api.rest.model.response.PermissionContext import PermissionContext
from src.port_adapter.api.rest.model.response.PermissionWithPermissionContexts import PermissionWithPermissionContexts
from src.port_adapter.api.rest.model.response.Resource import Resource
from src.port_adapter.api.rest.model.response.Role import Role
from src.port_adapter.api.rest.model.response.RoleAccessPermissionData import RoleAccessPermissionData
from src.port_adapter.api.rest.model.response.RoleAccessPermissionDatas import RoleAccessPermissionDatas
from src.port_adapter.api.rest.model.response.Roles import Roles
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.role_app_service_pb2 import RoleAppService_rolesResponse, \
    RoleAppService_rolesRequest, RoleAppService_roleByIdRequest, RoleAppService_roleByIdResponse, \
    RoleAppService_rolesTreesRequest, RoleAppService_rolesTreesResponse, RoleAppService_roleTreeRequest
from src.resource.proto._generated.identity.role_app_service_pb2_grpc import RoleAppServiceStub


class RoleClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def rolesTrees(self) -> RoleAccessPermissionDatas:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{RoleClient.rolesTrees.__qualname__}] - grpc call to retrieve roles from server {self._server}:{self._port}')
                request = RoleAppService_rolesTreesRequest()
                response: RoleAppService_rolesTreesResponse = stub.rolesTrees.with_call(
                    request,
                    metadata=(('token', self.token),('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(RoleClient.rolesTrees.__qualname__))))
                logger.debug(
                    f'[{RoleClient.rolesTrees.__qualname__}] - grpc response: {response}')

                result = []

                roleAccessPermissionsResponse = response[0].roleAccessPermission

                for roleAccessPermissionResponse in roleAccessPermissionsResponse:
                    role = Role(id=roleAccessPermissionResponse.role.id, name=roleAccessPermissionResponse.role.name)
                    # owned by
                    ownedBy = self._resourceFromProtoBuff(roleAccessPermissionResponse.ownedBy)
                    # owner of
                    ownerOfList = []
                    for ownerOfItem in roleAccessPermissionResponse.ownerOf:
                        ownerOfList.append(self._resourceFromProtoBuff(ownerOfItem))

                    # permissions with permission contexts
                    tmp = []
                    for permissionWithContext in roleAccessPermissionResponse.permissionWithPermissionContexts:
                        pcs = []
                        for permissionContext in permissionWithContext.permissionContexts:
                            pcs.append(self._permissionContextFromProtoBuff(permissionContext))

                        tmp.append(PermissionWithPermissionContexts(
                            permission=self._permissionFromProtoBuff(permissionWithContext.permission),
                            permission_contexts=pcs))

                    # role access tree
                    result.append(RoleAccessPermissionData(role=role, owned_by=ownedBy, owner_of=ownerOfList,
                                                           permissions=tmp,
                                                           access_tree=self._accessNodeFromProtoBuff(
                                                               roleAccessPermissionResponse.accessTree)))
                    print(RoleAccessPermissionDatas(roleAccessPermissions=result))
                return RoleAccessPermissionDatas(roleAccessPermissions=result)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def roleTree(self, roleId) -> RoleAccessPermissionDatas:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{RoleClient.roleTree.__qualname__}] - grpc call to retrieve roles from server {self._server}:{self._port}')
                request = RoleAppService_roleTreeRequest(roleId=roleId)
                response: RoleAppService_rolesTreesResponse = stub.roleTree.with_call(
                    request,
                    metadata=(('token', self.token),('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(RoleClient.roleTree.__qualname__))))
                logger.debug(
                    f'[{RoleClient.roleTree.__qualname__}] - grpc response: {response}')

                roleAccessPermissionResponse = response[0].roleAccessPermission
                role = Role(id=roleAccessPermissionResponse.role.id, name=roleAccessPermissionResponse.role.name)
                # owned by
                ownedBy = self._resourceFromProtoBuff(roleAccessPermissionResponse.ownedBy)
                # owner of
                ownerOfList = []
                for ownerOfItem in roleAccessPermissionResponse.ownerOf:
                    ownerOfList.append(self._resourceFromProtoBuff(ownerOfItem))

                # permissions with permission contexts
                tmp = []
                for permissionWithContext in roleAccessPermissionResponse.permissionWithPermissionContexts:
                    pcs = []
                    for permissionContext in permissionWithContext.permissionContexts:
                        pcs.append(self._permissionContextFromProtoBuff(permissionContext))

                    tmp.append(PermissionWithPermissionContexts(
                        permission=self._permissionFromProtoBuff(permissionWithContext.permission),
                        permission_contexts=pcs))

                # role access tree

                return RoleAccessPermissionData(role=role, owned_by=ownedBy, owner_of=ownerOfList,
                                                permissions=tmp,
                                                access_tree=self._accessNodeFromProtoBuff(
                                                    roleAccessPermissionResponse.accessTree))
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _resourceFromProtoBuff(self, protoBuf):
        return Resource(id=protoBuf.id, type=protoBuf.type)

    def _permissionContextFromProtoBuff(self, protoBuf):
        return PermissionContext(id=protoBuf.id, type=protoBuf.type, data=json.loads(protoBuf.data))

    def _accessNodeFromProtoBuff(self, protoBuf):
        result = []
        for node in protoBuf:
            children = self._accessNodeFromProtoBuff(node.children)

            result.append(
                AccessNode(
                    data=AccessNodeData(
                        content=json.loads(node.data.content),
                        content_type=node.data.contentType,
                        context=json.loads(node.data.context),
                    ),
                    children=children))
        return result

    def _permissionFromProtoBuff(self, protoBuf):
        allowedActions = [x for x in protoBuf.allowedActions]
        deniedActions = [x for x in protoBuf.deniedActions]
        return Permission(id=protoBuf.id, name=protoBuf.name, allowed_actions=allowedActions,
                          denied_actions=deniedActions)

    @OpenTelemetry.grpcTraceOTel
    def roles(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> Roles:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{RoleClient.roles.__qualname__}] - grpc call to retrieve roles from server {self._server}:{self._port}')
                request = RoleAppService_rolesRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: RoleAppService_rolesResponse = stub.roles.with_call(
                    request,
                    metadata=(('token', self.token),('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(RoleClient.roles.__qualname__))))
                logger.debug(
                    f'[{RoleClient.roles.__qualname__}] - grpc response: {response}')

                return Roles(roles=[Role(id=role.id, name=role.name) for role in response[0].roles],
                             item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def roleById(self, roleId) -> Role:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{RoleClient.roleById.__qualname__}] - grpc call to retrieve role with roleId: {roleId} from server {self._server}:{self._port}')
                response: RoleAppService_roleByIdResponse = stub.roleById.with_call(
                    RoleAppService_roleByIdRequest(id=roleId),
                    metadata=(('token', self.token),('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(RoleClient.roleById.__qualname__))))
                logger.debug(
                    f'[{RoleClient.roleById.__qualname__}] - grpc response: {response}')

                return Role(id=response[0].role.id, name=response[0].role.name)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
