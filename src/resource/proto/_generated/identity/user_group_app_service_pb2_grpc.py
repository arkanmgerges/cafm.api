# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from identity import (
    user_group_app_service_pb2 as identity_dot_user__group__app__service__pb2,
)


class UserGroupAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.userGroupByName = channel.unary_unary(
            "/cafm.identity.user_group.UserGroupAppService/userGroupByName",
            request_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByNameRequest.SerializeToString,
            response_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByNameResponse.FromString,
        )
        self.userGroupById = channel.unary_unary(
            "/cafm.identity.user_group.UserGroupAppService/userGroupById",
            request_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByIdRequest.SerializeToString,
            response_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByIdResponse.FromString,
        )
        self.userGroups = channel.unary_unary(
            "/cafm.identity.user_group.UserGroupAppService/userGroups",
            request_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupsRequest.SerializeToString,
            response_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupsResponse.FromString,
        )
        self.newId = channel.unary_unary(
            "/cafm.identity.user_group.UserGroupAppService/newId",
            request_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_newIdRequest.SerializeToString,
            response_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_newIdResponse.FromString,
        )


class UserGroupAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def userGroupByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def userGroupById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def userGroups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def newId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_UserGroupAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "userGroupByName": grpc.unary_unary_rpc_method_handler(
            servicer.userGroupByName,
            request_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByNameRequest.FromString,
            response_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByNameResponse.SerializeToString,
        ),
        "userGroupById": grpc.unary_unary_rpc_method_handler(
            servicer.userGroupById,
            request_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByIdRequest.FromString,
            response_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByIdResponse.SerializeToString,
        ),
        "userGroups": grpc.unary_unary_rpc_method_handler(
            servicer.userGroups,
            request_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupsRequest.FromString,
            response_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupsResponse.SerializeToString,
        ),
        "newId": grpc.unary_unary_rpc_method_handler(
            servicer.newId,
            request_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_newIdRequest.FromString,
            response_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_newIdResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "cafm.identity.user_group.UserGroupAppService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class UserGroupAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def userGroupByName(
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
            "/cafm.identity.user_group.UserGroupAppService/userGroupByName",
            identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByNameRequest.SerializeToString,
            identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByNameResponse.FromString,
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
    def userGroupById(
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
            "/cafm.identity.user_group.UserGroupAppService/userGroupById",
            identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByIdRequest.SerializeToString,
            identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByIdResponse.FromString,
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
    def userGroups(
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
            "/cafm.identity.user_group.UserGroupAppService/userGroups",
            identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupsRequest.SerializeToString,
            identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupsResponse.FromString,
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
    def newId(
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
            "/cafm.identity.user_group.UserGroupAppService/newId",
            identity_dot_user__group__app__service__pb2.UserGroupAppService_newIdRequest.SerializeToString,
            identity_dot_user__group__app__service__pb2.UserGroupAppService_newIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
