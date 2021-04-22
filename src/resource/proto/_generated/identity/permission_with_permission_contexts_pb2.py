# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: identity/permission_with_permission_contexts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from identity import permission_pb2 as identity_dot_permission__pb2
from identity import permission_context_pb2 as identity_dot_permission__context__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="identity/permission_with_permission_contexts.proto",
    package="cafm.identity.permission",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n2identity/permission_with_permission_contexts.proto\x12\x18\x63\x61\x66m.identity.permission\x1a\x19identity/permission.proto\x1a!identity/permission_context.proto"\xa5\x01\n PermissionWithPermissionContexts\x12\x38\n\npermission\x18\x01 \x01(\x0b\x32$.cafm.identity.permission.Permission\x12G\n\x12permissionContexts\x18\x02 \x03(\x0b\x32+.cafm.identity.permission.PermissionContextb\x06proto3',
    dependencies=[
        identity_dot_permission__pb2.DESCRIPTOR,
        identity_dot_permission__context__pb2.DESCRIPTOR,
    ],
)


_PERMISSIONWITHPERMISSIONCONTEXTS = _descriptor.Descriptor(
    name="PermissionWithPermissionContexts",
    full_name="cafm.identity.permission.PermissionWithPermissionContexts",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="permission",
            full_name="cafm.identity.permission.PermissionWithPermissionContexts.permission",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="permissionContexts",
            full_name="cafm.identity.permission.PermissionWithPermissionContexts.permissionContexts",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=143,
    serialized_end=308,
)

_PERMISSIONWITHPERMISSIONCONTEXTS.fields_by_name[
    "permission"
].message_type = identity_dot_permission__pb2._PERMISSION
_PERMISSIONWITHPERMISSIONCONTEXTS.fields_by_name[
    "permissionContexts"
].message_type = identity_dot_permission__context__pb2._PERMISSIONCONTEXT
DESCRIPTOR.message_types_by_name[
    "PermissionWithPermissionContexts"
] = _PERMISSIONWITHPERMISSIONCONTEXTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PermissionWithPermissionContexts = _reflection.GeneratedProtocolMessageType(
    "PermissionWithPermissionContexts",
    (_message.Message,),
    {
        "DESCRIPTOR": _PERMISSIONWITHPERMISSIONCONTEXTS,
        "__module__": "identity.permission_with_permission_contexts_pb2"
        # @@protoc_insertion_point(class_scope:cafm.identity.permission.PermissionWithPermissionContexts)
    },
)
_sym_db.RegisterMessage(PermissionWithPermissionContexts)


# @@protoc_insertion_point(module_scope)
