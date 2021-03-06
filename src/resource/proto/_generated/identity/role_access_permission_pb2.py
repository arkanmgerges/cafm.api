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
  serialized_pb=b'\n%identity/role_access_permission.proto\x12\x12\x63\x61\x66m.identity.role\x1a\x13identity/role.proto\x1a\x32identity/permission_with_permission_contexts.proto\x1a\x17identity/resource.proto\x1a\x1aidentity/access_node.proto\"\xcb\x02\n\x14RoleAccessPermission\x12&\n\x04role\x18\x01 \x01(\x0b\x32\x18.cafm.identity.role.Role\x12g\n#permission_with_permission_contexts\x18\x02 \x03(\x0b\x32:.cafm.identity.permission.PermissionWithPermissionContexts\x12\x32\n\x08owned_by\x18\x03 \x01(\x0b\x32 .cafm.identity.resource.Resource\x12\x32\n\x08owner_of\x18\x04 \x03(\x0b\x32 .cafm.identity.resource.Resource\x12:\n\x0b\x61\x63\x63\x65ss_tree\x18\x05 \x03(\x0b\x32%.cafm.identity.access_node.AccessNodeb\x06proto3'
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
      name='permission_with_permission_contexts', full_name='cafm.identity.role.RoleAccessPermission.permission_with_permission_contexts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owned_by', full_name='cafm.identity.role.RoleAccessPermission.owned_by', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner_of', full_name='cafm.identity.role.RoleAccessPermission.owner_of', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_tree', full_name='cafm.identity.role.RoleAccessPermission.access_tree', index=4,
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
  serialized_end=519,
)

_ROLEACCESSPERMISSION.fields_by_name['role'].message_type = identity_dot_role__pb2._ROLE
_ROLEACCESSPERMISSION.fields_by_name['permission_with_permission_contexts'].message_type = identity_dot_permission__with__permission__contexts__pb2._PERMISSIONWITHPERMISSIONCONTEXTS
_ROLEACCESSPERMISSION.fields_by_name['owned_by'].message_type = identity_dot_resource__pb2._RESOURCE
_ROLEACCESSPERMISSION.fields_by_name['owner_of'].message_type = identity_dot_resource__pb2._RESOURCE
_ROLEACCESSPERMISSION.fields_by_name['access_tree'].message_type = identity_dot_access__node__pb2._ACCESSNODE
DESCRIPTOR.message_types_by_name['RoleAccessPermission'] = _ROLEACCESSPERMISSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleAccessPermission = _reflection.GeneratedProtocolMessageType('RoleAccessPermission', (_message.Message,), {
  'DESCRIPTOR' : _ROLEACCESSPERMISSION,
  '__module__' : 'identity.role_access_permission_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAccessPermission)
  })
_sym_db.RegisterMessage(RoleAccessPermission)


# @@protoc_insertion_point(module_scope)
