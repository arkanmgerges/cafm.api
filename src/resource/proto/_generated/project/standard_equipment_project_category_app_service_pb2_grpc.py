# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from project import (
    standard_equipment_project_category_app_service_pb2 as project_dot_standard__equipment__project__category__app__service__pb2,
)


class StandardEquipmentProjectCategoryAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.standard_equipment_project_category_by_id = channel.unary_unary(
            "/cafm.project.standard_equipment_project_category.StandardEquipmentProjectCategoryAppService/standard_equipment_project_category_by_id",
            request_serializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoryByIdRequest.SerializeToString,
            response_deserializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoryByIdResponse.FromString,
        )
        self.standard_equipment_project_categories = channel.unary_unary(
            "/cafm.project.standard_equipment_project_category.StandardEquipmentProjectCategoryAppService/standard_equipment_project_categories",
            request_serializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesRequest.SerializeToString,
            response_deserializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesResponse.FromString,
        )
        self.new_id = channel.unary_unary(
            "/cafm.project.standard_equipment_project_category.StandardEquipmentProjectCategoryAppService/new_id",
            request_serializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_newIdRequest.SerializeToString,
            response_deserializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_newIdResponse.FromString,
        )
        self.standard_equipment_project_categories_by_organization_id = channel.unary_unary(
            "/cafm.project.standard_equipment_project_category.StandardEquipmentProjectCategoryAppService/standard_equipment_project_categories_by_organization_id",
            request_serializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesByOrganizationIdRequest.SerializeToString,
            response_deserializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesByOrganizationIdResponse.FromString,
        )


class StandardEquipmentProjectCategoryAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def standard_equipment_project_category_by_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def standard_equipment_project_categories(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def new_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def standard_equipment_project_categories_by_organization_id(
        self, request, context
    ):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_StandardEquipmentProjectCategoryAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "standard_equipment_project_category_by_id": grpc.unary_unary_rpc_method_handler(
            servicer.standard_equipment_project_category_by_id,
            request_deserializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoryByIdRequest.FromString,
            response_serializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoryByIdResponse.SerializeToString,
        ),
        "standard_equipment_project_categories": grpc.unary_unary_rpc_method_handler(
            servicer.standard_equipment_project_categories,
            request_deserializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesRequest.FromString,
            response_serializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesResponse.SerializeToString,
        ),
        "new_id": grpc.unary_unary_rpc_method_handler(
            servicer.new_id,
            request_deserializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_newIdRequest.FromString,
            response_serializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_newIdResponse.SerializeToString,
        ),
        "standard_equipment_project_categories_by_organization_id": grpc.unary_unary_rpc_method_handler(
            servicer.standard_equipment_project_categories_by_organization_id,
            request_deserializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesByOrganizationIdRequest.FromString,
            response_serializer=project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesByOrganizationIdResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "cafm.project.standard_equipment_project_category.StandardEquipmentProjectCategoryAppService",
        rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class StandardEquipmentProjectCategoryAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def standard_equipment_project_category_by_id(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/cafm.project.standard_equipment_project_category.StandardEquipmentProjectCategoryAppService/standard_equipment_project_category_by_id",
            project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoryByIdRequest.SerializeToString,
            project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoryByIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def standard_equipment_project_categories(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/cafm.project.standard_equipment_project_category.StandardEquipmentProjectCategoryAppService/standard_equipment_project_categories",
            project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesRequest.SerializeToString,
            project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def new_id(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/cafm.project.standard_equipment_project_category.StandardEquipmentProjectCategoryAppService/new_id",
            project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_newIdRequest.SerializeToString,
            project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_newIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def standard_equipment_project_categories_by_organization_id(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/cafm.project.standard_equipment_project_category.StandardEquipmentProjectCategoryAppService/standard_equipment_project_categories_by_organization_id",
            project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesByOrganizationIdRequest.SerializeToString,
            project_dot_standard__equipment__project__category__app__service__pb2.StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesByOrganizationIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
