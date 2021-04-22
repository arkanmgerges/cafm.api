# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from project import (
    user_lookup_app_service_pb2 as project_dot_user__lookup__app__service__pb2,
)


class UserLookupAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.userLookupByUserEmail = channel.unary_unary(
            "/cafm.project.user_lookup.UserLookupAppService/userLookupByUserEmail",
            request_serializer=project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupByUserEmailRequest.SerializeToString,
            response_deserializer=project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupByUserEmailResponse.FromString,
        )
        self.userLookupByUserId = channel.unary_unary(
            "/cafm.project.user_lookup.UserLookupAppService/userLookupByUserId",
            request_serializer=project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupByUserIdRequest.SerializeToString,
            response_deserializer=project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupByUserIdResponse.FromString,
        )
        self.userLookups = channel.unary_unary(
            "/cafm.project.user_lookup.UserLookupAppService/userLookups",
            request_serializer=project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupsRequest.SerializeToString,
            response_deserializer=project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupsResponse.FromString,
        )


class UserLookupAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def userLookupByUserEmail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def userLookupByUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def userLookups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_UserLookupAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "userLookupByUserEmail": grpc.unary_unary_rpc_method_handler(
            servicer.userLookupByUserEmail,
            request_deserializer=project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupByUserEmailRequest.FromString,
            response_serializer=project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupByUserEmailResponse.SerializeToString,
        ),
        "userLookupByUserId": grpc.unary_unary_rpc_method_handler(
            servicer.userLookupByUserId,
            request_deserializer=project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupByUserIdRequest.FromString,
            response_serializer=project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupByUserIdResponse.SerializeToString,
        ),
        "userLookups": grpc.unary_unary_rpc_method_handler(
            servicer.userLookups,
            request_deserializer=project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupsRequest.FromString,
            response_serializer=project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "cafm.project.user_lookup.UserLookupAppService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class UserLookupAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def userLookupByUserEmail(
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
            "/cafm.project.user_lookup.UserLookupAppService/userLookupByUserEmail",
            project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupByUserEmailRequest.SerializeToString,
            project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupByUserEmailResponse.FromString,
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
    def userLookupByUserId(
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
            "/cafm.project.user_lookup.UserLookupAppService/userLookupByUserId",
            project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupByUserIdRequest.SerializeToString,
            project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupByUserIdResponse.FromString,
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
    def userLookups(
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
            "/cafm.project.user_lookup.UserLookupAppService/userLookups",
            project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupsRequest.SerializeToString,
            project_dot_user__lookup__app__service__pb2.UserLookupAppService_userLookupsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
