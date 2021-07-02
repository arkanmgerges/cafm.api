# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from project import equipment_project_category_app_service_pb2 as project_dot_equipment__project__category__app__service__pb2


class EquipmentProjectCategoryAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.equipment_project_category_by_id = channel.unary_unary(
                '/cafm.project.equipment_project_category.EquipmentProjectCategoryAppService/equipment_project_category_by_id',
                request_serializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdRequest.SerializeToString,
                response_deserializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse.FromString,
                )
        self.equipment_project_categories = channel.unary_unary(
                '/cafm.project.equipment_project_category.EquipmentProjectCategoryAppService/equipment_project_categories',
                request_serializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest.SerializeToString,
                response_deserializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse.FromString,
                )
        self.equipment_category_groups_by_equipment_project_category_id = channel.unary_unary(
                '/cafm.project.equipment_project_category.EquipmentProjectCategoryAppService/equipment_category_groups_by_equipment_project_category_id',
                request_serializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest.SerializeToString,
                response_deserializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse.FromString,
                )
        self.new_id = channel.unary_unary(
                '/cafm.project.equipment_project_category.EquipmentProjectCategoryAppService/new_id',
                request_serializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_newIdRequest.SerializeToString,
                response_deserializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_newIdResponse.FromString,
                )
        self.equipment_project_categories_by_project_id = channel.unary_unary(
                '/cafm.project.equipment_project_category.EquipmentProjectCategoryAppService/equipment_project_categories_by_project_id',
                request_serializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoriesByProjectIdRequest.SerializeToString,
                response_deserializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoriesByProjectIdResponse.FromString,
                )


class EquipmentProjectCategoryAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def equipment_project_category_by_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def equipment_project_categories(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def equipment_category_groups_by_equipment_project_category_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def new_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def equipment_project_categories_by_project_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EquipmentProjectCategoryAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'equipment_project_category_by_id': grpc.unary_unary_rpc_method_handler(
                    servicer.equipment_project_category_by_id,
                    request_deserializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdRequest.FromString,
                    response_serializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse.SerializeToString,
            ),
            'equipment_project_categories': grpc.unary_unary_rpc_method_handler(
                    servicer.equipment_project_categories,
                    request_deserializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest.FromString,
                    response_serializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse.SerializeToString,
            ),
            'equipment_category_groups_by_equipment_project_category_id': grpc.unary_unary_rpc_method_handler(
                    servicer.equipment_category_groups_by_equipment_project_category_id,
                    request_deserializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest.FromString,
                    response_serializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse.SerializeToString,
            ),
            'new_id': grpc.unary_unary_rpc_method_handler(
                    servicer.new_id,
                    request_deserializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_newIdRequest.FromString,
                    response_serializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_newIdResponse.SerializeToString,
            ),
            'equipment_project_categories_by_project_id': grpc.unary_unary_rpc_method_handler(
                    servicer.equipment_project_categories_by_project_id,
                    request_deserializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoriesByProjectIdRequest.FromString,
                    response_serializer=project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoriesByProjectIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.equipment_project_category.EquipmentProjectCategoryAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EquipmentProjectCategoryAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def equipment_project_category_by_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.equipment_project_category.EquipmentProjectCategoryAppService/equipment_project_category_by_id',
            project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdRequest.SerializeToString,
            project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def equipment_project_categories(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.equipment_project_category.EquipmentProjectCategoryAppService/equipment_project_categories',
            project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest.SerializeToString,
            project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def equipment_category_groups_by_equipment_project_category_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.equipment_project_category.EquipmentProjectCategoryAppService/equipment_category_groups_by_equipment_project_category_id',
            project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest.SerializeToString,
            project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def new_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.equipment_project_category.EquipmentProjectCategoryAppService/new_id',
            project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_newIdRequest.SerializeToString,
            project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def equipment_project_categories_by_project_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.equipment_project_category.EquipmentProjectCategoryAppService/equipment_project_categories_by_project_id',
            project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoriesByProjectIdRequest.SerializeToString,
            project_dot_equipment__project__category__app__service__pb2.EquipmentProjectCategoryAppService_equipmentProjectCategoriesByProjectIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
