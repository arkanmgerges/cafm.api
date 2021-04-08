# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from project import standard_equipment_category_group_app_service_pb2 as project_dot_standard__equipment__category__group__app__service__pb2


class StandardEquipmentCategoryGroupAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.standardEquipmentCategoryGroupById = channel.unary_unary(
                '/cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService/standardEquipmentCategoryGroupById',
                request_serializer=project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest.SerializeToString,
                response_deserializer=project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse.FromString,
                )
        self.standardEquipmentCategoryGroups = channel.unary_unary(
                '/cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService/standardEquipmentCategoryGroups',
                request_serializer=project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest.SerializeToString,
                response_deserializer=project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse.FromString,
                )
        self.newId = channel.unary_unary(
                '/cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService/newId',
                request_serializer=project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_newIdRequest.SerializeToString,
                response_deserializer=project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_newIdResponse.FromString,
                )


class StandardEquipmentCategoryGroupAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def standardEquipmentCategoryGroupById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def standardEquipmentCategoryGroups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def newId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StandardEquipmentCategoryGroupAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'standardEquipmentCategoryGroupById': grpc.unary_unary_rpc_method_handler(
                    servicer.standardEquipmentCategoryGroupById,
                    request_deserializer=project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest.FromString,
                    response_serializer=project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse.SerializeToString,
            ),
            'standardEquipmentCategoryGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.standardEquipmentCategoryGroups,
                    request_deserializer=project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest.FromString,
                    response_serializer=project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse.SerializeToString,
            ),
            'newId': grpc.unary_unary_rpc_method_handler(
                    servicer.newId,
                    request_deserializer=project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_newIdRequest.FromString,
                    response_serializer=project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_newIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StandardEquipmentCategoryGroupAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def standardEquipmentCategoryGroupById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService/standardEquipmentCategoryGroupById',
            project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest.SerializeToString,
            project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def standardEquipmentCategoryGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService/standardEquipmentCategoryGroups',
            project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest.SerializeToString,
            project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService/newId',
            project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_newIdRequest.SerializeToString,
            project_dot_standard__equipment__category__group__app__service__pb2.StandardEquipmentCategoryGroupAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
