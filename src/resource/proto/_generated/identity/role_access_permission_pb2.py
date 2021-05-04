# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: identity/role_access_permission.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from identity import role_pb2 as identity_dot_role__pb2
from identity import permission_with_permission_contexts_pb2 as identity_dot_permission__with__permission__contexts__pb2
from identity import resource_pb2 as identity_dot_resource__pb2
from identity import access_node_pb2 as identity_dot_access__node__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='identity/role_access_permission.proto',
  package='cafm.identity.role',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%identity/role_access_permission.proto\x12\x12\x63\x61\x66m.identity.role\x1a\x13identity/role.proto\x1a\x32identity/permission_with_permission_contexts.proto\x1a\x17identity/resource.proto\x1a\x1aidentity/access_node.proto\"\xc5\x02\n\x14RoleAccessPermission\x12&\n\x04role\x18\x01 \x01(\x0b\x32\x18.cafm.identity.role.Role\x12\x64\n permissionWithPermissionContexts\x18\x02 \x03(\x0b\x32:.cafm.identity.permission.PermissionWithPermissionContexts\x12\x31\n\x07ownedBy\x18\x03 \x01(\x0b\x32 .cafm.identity.resource.Resource\x12\x31\n\x07ownerOf\x18\x04 \x03(\x0b\x32 .cafm.identity.resource.Resource\x12\x39\n\naccessTree\x18\x05 \x03(\x0b\x32%.cafm.identity.access_node.AccessNodeb\x06proto3'
  ,
  dependencies=[identity_dot_role__pb2.DESCRIPTOR,identity_dot_permission__with__permission__contexts__pb2.DESCRIPTOR,identity_dot_resource__pb2.DESCRIPTOR,identity_dot_access__node__pb2.DESCRIPTOR,])




_ROLEACCESSPERMISSION = _descriptor.Descriptor(
  name='RoleAccessPermission',
  full_name='cafm.identity.role.RoleAccessPermission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='cafm.identity.role.RoleAccessPermission.role', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissionWithPermissionContexts', full_name='cafm.identity.role.RoleAccessPermission.permissionWithPermissionContexts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ownedBy', full_name='cafm.identity.role.RoleAccessPermission.ownedBy', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ownerOf', full_name='cafm.identity.role.RoleAccessPermission.ownerOf', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accessTree', full_name='cafm.identity.role.RoleAccessPermission.accessTree', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=513,
)

_ROLEACCESSPERMISSION.fields_by_name['role'].message_type = identity_dot_role__pb2._ROLE
_ROLEACCESSPERMISSION.fields_by_name['permissionWithPermissionContexts'].message_type = identity_dot_permission__with__permission__contexts__pb2._PERMISSIONWITHPERMISSIONCONTEXTS
_ROLEACCESSPERMISSION.fields_by_name['ownedBy'].message_type = identity_dot_resource__pb2._RESOURCE
_ROLEACCESSPERMISSION.fields_by_name['ownerOf'].message_type = identity_dot_resource__pb2._RESOURCE
_ROLEACCESSPERMISSION.fields_by_name['accessTree'].message_type = identity_dot_access__node__pb2._ACCESSNODE
DESCRIPTOR.message_types_by_name['RoleAccessPermission'] = _ROLEACCESSPERMISSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleAccessPermission = _reflection.GeneratedProtocolMessageType('RoleAccessPermission', (_message.Message,), {
  'DESCRIPTOR' : _ROLEACCESSPERMISSION,
  '__module__' : 'identity.role_access_permission_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAccessPermission)
  })
_sym_db.RegisterMessage(RoleAccessPermission)


# @@protoc_insertion_point(module_scope)
