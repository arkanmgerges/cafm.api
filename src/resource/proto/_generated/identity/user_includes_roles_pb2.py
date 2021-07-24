# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: identity/user_includes_roles.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from identity import role_pb2 as identity_dot_role__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='identity/user_includes_roles.proto',
  package='cafm.identity.policy',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"identity/user_includes_roles.proto\x12\x14\x63\x61\x66m.identity.policy\x1a\x13identity/role.proto\"W\n\x11UserIncludesRoles\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\'\n\x05roles\x18\x03 \x03(\x0b\x32\x18.cafm.identity.role.Roleb\x06proto3'
  ,
  dependencies=[identity_dot_role__pb2.DESCRIPTOR,])




_USERINCLUDESROLES = _descriptor.Descriptor(
  name='UserIncludesRoles',
  full_name='cafm.identity.policy.UserIncludesRoles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.identity.policy.UserIncludesRoles.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='cafm.identity.policy.UserIncludesRoles.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roles', full_name='cafm.identity.policy.UserIncludesRoles.roles', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=81,
  serialized_end=168,
)

_USERINCLUDESROLES.fields_by_name['roles'].message_type = identity_dot_role__pb2._ROLE
DESCRIPTOR.message_types_by_name['UserIncludesRoles'] = _USERINCLUDESROLES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserIncludesRoles = _reflection.GeneratedProtocolMessageType('UserIncludesRoles', (_message.Message,), {
  'DESCRIPTOR' : _USERINCLUDESROLES,
  '__module__' : 'identity.user_includes_roles_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.policy.UserIncludesRoles)
  })
_sym_db.RegisterMessage(UserIncludesRoles)


# @@protoc_insertion_point(module_scope)
