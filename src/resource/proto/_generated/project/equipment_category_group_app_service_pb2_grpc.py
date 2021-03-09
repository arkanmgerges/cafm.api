# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from project import equipment_category_group_app_service_pb2 as project_dot_equipment__category__group__app__service__pb2


class EquipmentCategoryGroupAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.equipmentCategoryGroupById = channel.unary_unary(
                '/cafm.project.equipment_category_group.EquipmentCategoryGroupAppService/equipmentCategoryGroupById',
                request_serializer=project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest.SerializeToString,
                response_deserializer=project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse.FromString,
                )
        self.equipmentCategoryGroups = channel.unary_unary(
                '/cafm.project.equipment_category_group.EquipmentCategoryGroupAppService/equipmentCategoryGroups',
                request_serializer=project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest.SerializeToString,
                response_deserializer=project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse.FromString,
                )
        self.newId = channel.unary_unary(
                '/cafm.project.equipment_category_group.EquipmentCategoryGroupAppService/newId',
                request_serializer=project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_newIdRequest.SerializeToString,
                response_deserializer=project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_newIdResponse.FromString,
                )


class EquipmentCategoryGroupAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def equipmentCategoryGroupById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def equipmentCategoryGroups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def newId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EquipmentCategoryGroupAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'equipmentCategoryGroupById': grpc.unary_unary_rpc_method_handler(
                    servicer.equipmentCategoryGroupById,
                    request_deserializer=project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest.FromString,
                    response_serializer=project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse.SerializeToString,
            ),
            'equipmentCategoryGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.equipmentCategoryGroups,
                    request_deserializer=project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest.FromString,
                    response_serializer=project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse.SerializeToString,
            ),
            'newId': grpc.unary_unary_rpc_method_handler(
                    servicer.newId,
                    request_deserializer=project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_newIdRequest.FromString,
                    response_serializer=project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_newIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.equipment_category_group.EquipmentCategoryGroupAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EquipmentCategoryGroupAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def equipmentCategoryGroupById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.equipment_category_group.EquipmentCategoryGroupAppService/equipmentCategoryGroupById',
            project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest.SerializeToString,
            project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def equipmentCategoryGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.equipment_category_group.EquipmentCategoryGroupAppService/equipmentCategoryGroups',
            project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest.SerializeToString,
            project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def newId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.equipment_category_group.EquipmentCategoryGroupAppService/newId',
            project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_newIdRequest.SerializeToString,
            project_dot_equipment__category__group__app__service__pb2.EquipmentCategoryGroupAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
