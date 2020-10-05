# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: permission_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='permission_app_service.proto',
  package='cafm.identity.permission',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cpermission_app_service.proto\x12\x19\x63oral.identity.permission\"<\n,PermissionAppService_permissionByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"I\n-PermissionAppService_permissionByNameResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t2\xc0\x01\n\x14PermissionAppService\x12\xa7\x01\n\x10permissionByName\x12G.cafm.identity.permission.PermissionAppService_permissionByNameRequest\x1aH.cafm.identity.permission.PermissionAppService_permissionByNameResponse\"\x00\x62\x06proto3'
)




_PERMISSIONAPPSERVICE_PERMISSIONBYNAMEREQUEST = _descriptor.Descriptor(
  name='PermissionAppService_permissionByNameRequest',
  full_name='cafm.identity.permission.PermissionAppService_permissionByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.identity.permission.PermissionAppService_permissionByNameRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=59,
  serialized_end=119,
)


_PERMISSIONAPPSERVICE_PERMISSIONBYNAMERESPONSE = _descriptor.Descriptor(
  name='PermissionAppService_permissionByNameResponse',
  full_name='cafm.identity.permission.PermissionAppService_permissionByNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.identity.permission.PermissionAppService_permissionByNameResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.identity.permission.PermissionAppService_permissionByNameResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=121,
  serialized_end=194,
)

DESCRIPTOR.message_types_by_name['PermissionAppService_permissionByNameRequest'] = _PERMISSIONAPPSERVICE_PERMISSIONBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['PermissionAppService_permissionByNameResponse'] = _PERMISSIONAPPSERVICE_PERMISSIONBYNAMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PermissionAppService_permissionByNameRequest = _reflection.GeneratedProtocolMessageType('PermissionAppService_permissionByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSIONAPPSERVICE_PERMISSIONBYNAMEREQUEST,
  '__module__' : 'permission_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.permission.PermissionAppService_permissionByNameRequest)
  })
_sym_db.RegisterMessage(PermissionAppService_permissionByNameRequest)

PermissionAppService_permissionByNameResponse = _reflection.GeneratedProtocolMessageType('PermissionAppService_permissionByNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSIONAPPSERVICE_PERMISSIONBYNAMERESPONSE,
  '__module__' : 'permission_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.permission.PermissionAppService_permissionByNameResponse)
  })
_sym_db.RegisterMessage(PermissionAppService_permissionByNameResponse)



_PERMISSIONAPPSERVICE = _descriptor.ServiceDescriptor(
  name='PermissionAppService',
  full_name='cafm.identity.permission.PermissionAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=197,
  serialized_end=389,
  methods=[
  _descriptor.MethodDescriptor(
    name='permissionByName',
    full_name='cafm.identity.permission.PermissionAppService.permissionByName',
    index=0,
    containing_service=None,
    input_type=_PERMISSIONAPPSERVICE_PERMISSIONBYNAMEREQUEST,
    output_type=_PERMISSIONAPPSERVICE_PERMISSIONBYNAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PERMISSIONAPPSERVICE)

DESCRIPTOR.services_by_name['PermissionAppService'] = _PERMISSIONAPPSERVICE

# @@protoc_insertion_point(module_scope)
