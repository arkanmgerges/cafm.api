# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: identity/role_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from identity import role_pb2 as identity_dot_role__pb2
import order_pb2 as order__pb2
from identity import role_access_permission_pb2 as identity_dot_role__access__permission__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='identity/role_app_service.proto',
  package='cafm.identity.role',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fidentity/role_app_service.proto\x12\x12\x63\x61\x66m.identity.role\x1a\x13identity/role.proto\x1a\x0border.proto\x1a%identity/role_access_permission.proto\"\"\n RoleAppService_rolesTreesRequest\"1\n!RoleAppService_rolesTreesResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"1\n\x1eRoleAppService_roleTreeRequest\x12\x0f\n\x07role_id\x18\x01 \x01(\t\"k\n\x1fRoleAppService_roleTreeResponse\x12H\n\x16role_access_permission\x18\x01 \x01(\x0b\x32(.cafm.identity.role.RoleAccessPermission\"0\n RoleAppService_roleByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"K\n!RoleAppService_roleByNameResponse\x12&\n\x04role\x18\x01 \x01(\x0b\x32\x18.cafm.identity.role.Role\",\n\x1eRoleAppService_roleByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"I\n\x1fRoleAppService_roleByIdResponse\x12&\n\x04role\x18\x01 \x01(\x0b\x32\x18.cafm.identity.role.Role\"q\n\x1bRoleAppService_rolesRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"a\n\x1cRoleAppService_rolesResponse\x12\'\n\x05roles\x18\x01 \x03(\x0b\x32\x18.cafm.identity.role.Role\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"\x1d\n\x1bRoleAppService_newIdRequest\"*\n\x1cRoleAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xdb\x05\n\x0eRoleAppService\x12}\n\x0crole_by_name\x12\x34.cafm.identity.role.RoleAppService_roleByNameRequest\x1a\x35.cafm.identity.role.RoleAppService_roleByNameResponse\"\x00\x12w\n\nrole_by_id\x12\x32.cafm.identity.role.RoleAppService_roleByIdRequest\x1a\x33.cafm.identity.role.RoleAppService_roleByIdResponse\"\x00\x12l\n\x05roles\x12/.cafm.identity.role.RoleAppService_rolesRequest\x1a\x30.cafm.identity.role.RoleAppService_rolesResponse\"\x00\x12|\n\x0broles_trees\x12\x34.cafm.identity.role.RoleAppService_rolesTreesRequest\x1a\x35.cafm.identity.role.RoleAppService_rolesTreesResponse\"\x00\x12v\n\trole_tree\x12\x32.cafm.identity.role.RoleAppService_roleTreeRequest\x1a\x33.cafm.identity.role.RoleAppService_roleTreeResponse\"\x00\x12m\n\x06new_id\x12/.cafm.identity.role.RoleAppService_newIdRequest\x1a\x30.cafm.identity.role.RoleAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[identity_dot_role__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,identity_dot_role__access__permission__pb2.DESCRIPTOR,])




_ROLEAPPSERVICE_ROLESTREESREQUEST = _descriptor.Descriptor(
  name='RoleAppService_rolesTreesRequest',
  full_name='cafm.identity.role.RoleAppService_rolesTreesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=128,
  serialized_end=162,
)


_ROLEAPPSERVICE_ROLESTREESRESPONSE = _descriptor.Descriptor(
  name='RoleAppService_rolesTreesResponse',
  full_name='cafm.identity.role.RoleAppService_rolesTreesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='cafm.identity.role.RoleAppService_rolesTreesResponse.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=164,
  serialized_end=213,
)


_ROLEAPPSERVICE_ROLETREEREQUEST = _descriptor.Descriptor(
  name='RoleAppService_roleTreeRequest',
  full_name='cafm.identity.role.RoleAppService_roleTreeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_id', full_name='cafm.identity.role.RoleAppService_roleTreeRequest.role_id', index=0,
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
  serialized_start=215,
  serialized_end=264,
)


_ROLEAPPSERVICE_ROLETREERESPONSE = _descriptor.Descriptor(
  name='RoleAppService_roleTreeResponse',
  full_name='cafm.identity.role.RoleAppService_roleTreeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_access_permission', full_name='cafm.identity.role.RoleAppService_roleTreeResponse.role_access_permission', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=266,
  serialized_end=373,
)


_ROLEAPPSERVICE_ROLEBYNAMEREQUEST = _descriptor.Descriptor(
  name='RoleAppService_roleByNameRequest',
  full_name='cafm.identity.role.RoleAppService_roleByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.identity.role.RoleAppService_roleByNameRequest.name', index=0,
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
  serialized_start=375,
  serialized_end=423,
)


_ROLEAPPSERVICE_ROLEBYNAMERESPONSE = _descriptor.Descriptor(
  name='RoleAppService_roleByNameResponse',
  full_name='cafm.identity.role.RoleAppService_roleByNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='cafm.identity.role.RoleAppService_roleByNameResponse.role', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=425,
  serialized_end=500,
)


_ROLEAPPSERVICE_ROLEBYIDREQUEST = _descriptor.Descriptor(
  name='RoleAppService_roleByIdRequest',
  full_name='cafm.identity.role.RoleAppService_roleByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.identity.role.RoleAppService_roleByIdRequest.id', index=0,
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
  serialized_start=502,
  serialized_end=546,
)


_ROLEAPPSERVICE_ROLEBYIDRESPONSE = _descriptor.Descriptor(
  name='RoleAppService_roleByIdResponse',
  full_name='cafm.identity.role.RoleAppService_roleByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='cafm.identity.role.RoleAppService_roleByIdResponse.role', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=548,
  serialized_end=621,
)


_ROLEAPPSERVICE_ROLESREQUEST = _descriptor.Descriptor(
  name='RoleAppService_rolesRequest',
  full_name='cafm.identity.role.RoleAppService_rolesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.identity.role.RoleAppService_rolesRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.identity.role.RoleAppService_rolesRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.identity.role.RoleAppService_rolesRequest.orders', index=2,
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
  serialized_start=623,
  serialized_end=736,
)


_ROLEAPPSERVICE_ROLESRESPONSE = _descriptor.Descriptor(
  name='RoleAppService_rolesResponse',
  full_name='cafm.identity.role.RoleAppService_rolesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roles', full_name='cafm.identity.role.RoleAppService_rolesResponse.roles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.identity.role.RoleAppService_rolesResponse.total_item_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=738,
  serialized_end=835,
)


_ROLEAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='RoleAppService_newIdRequest',
  full_name='cafm.identity.role.RoleAppService_newIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=837,
  serialized_end=866,
)


_ROLEAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='RoleAppService_newIdResponse',
  full_name='cafm.identity.role.RoleAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.identity.role.RoleAppService_newIdResponse.id', index=0,
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
  serialized_start=868,
  serialized_end=910,
)

_ROLEAPPSERVICE_ROLETREERESPONSE.fields_by_name['role_access_permission'].message_type = identity_dot_role__access__permission__pb2._ROLEACCESSPERMISSION
_ROLEAPPSERVICE_ROLEBYNAMERESPONSE.fields_by_name['role'].message_type = identity_dot_role__pb2._ROLE
_ROLEAPPSERVICE_ROLEBYIDRESPONSE.fields_by_name['role'].message_type = identity_dot_role__pb2._ROLE
_ROLEAPPSERVICE_ROLESREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_ROLEAPPSERVICE_ROLESRESPONSE.fields_by_name['roles'].message_type = identity_dot_role__pb2._ROLE
DESCRIPTOR.message_types_by_name['RoleAppService_rolesTreesRequest'] = _ROLEAPPSERVICE_ROLESTREESREQUEST
DESCRIPTOR.message_types_by_name['RoleAppService_rolesTreesResponse'] = _ROLEAPPSERVICE_ROLESTREESRESPONSE
DESCRIPTOR.message_types_by_name['RoleAppService_roleTreeRequest'] = _ROLEAPPSERVICE_ROLETREEREQUEST
DESCRIPTOR.message_types_by_name['RoleAppService_roleTreeResponse'] = _ROLEAPPSERVICE_ROLETREERESPONSE
DESCRIPTOR.message_types_by_name['RoleAppService_roleByNameRequest'] = _ROLEAPPSERVICE_ROLEBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['RoleAppService_roleByNameResponse'] = _ROLEAPPSERVICE_ROLEBYNAMERESPONSE
DESCRIPTOR.message_types_by_name['RoleAppService_roleByIdRequest'] = _ROLEAPPSERVICE_ROLEBYIDREQUEST
DESCRIPTOR.message_types_by_name['RoleAppService_roleByIdResponse'] = _ROLEAPPSERVICE_ROLEBYIDRESPONSE
DESCRIPTOR.message_types_by_name['RoleAppService_rolesRequest'] = _ROLEAPPSERVICE_ROLESREQUEST
DESCRIPTOR.message_types_by_name['RoleAppService_rolesResponse'] = _ROLEAPPSERVICE_ROLESRESPONSE
DESCRIPTOR.message_types_by_name['RoleAppService_newIdRequest'] = _ROLEAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['RoleAppService_newIdResponse'] = _ROLEAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleAppService_rolesTreesRequest = _reflection.GeneratedProtocolMessageType('RoleAppService_rolesTreesRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLESTREESREQUEST,
  '__module__' : 'identity.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAppService_rolesTreesRequest)
  })
_sym_db.RegisterMessage(RoleAppService_rolesTreesRequest)

RoleAppService_rolesTreesResponse = _reflection.GeneratedProtocolMessageType('RoleAppService_rolesTreesResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLESTREESRESPONSE,
  '__module__' : 'identity.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAppService_rolesTreesResponse)
  })
_sym_db.RegisterMessage(RoleAppService_rolesTreesResponse)

RoleAppService_roleTreeRequest = _reflection.GeneratedProtocolMessageType('RoleAppService_roleTreeRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLETREEREQUEST,
  '__module__' : 'identity.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAppService_roleTreeRequest)
  })
_sym_db.RegisterMessage(RoleAppService_roleTreeRequest)

RoleAppService_roleTreeResponse = _reflection.GeneratedProtocolMessageType('RoleAppService_roleTreeResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLETREERESPONSE,
  '__module__' : 'identity.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAppService_roleTreeResponse)
  })
_sym_db.RegisterMessage(RoleAppService_roleTreeResponse)

RoleAppService_roleByNameRequest = _reflection.GeneratedProtocolMessageType('RoleAppService_roleByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLEBYNAMEREQUEST,
  '__module__' : 'identity.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAppService_roleByNameRequest)
  })
_sym_db.RegisterMessage(RoleAppService_roleByNameRequest)

RoleAppService_roleByNameResponse = _reflection.GeneratedProtocolMessageType('RoleAppService_roleByNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLEBYNAMERESPONSE,
  '__module__' : 'identity.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAppService_roleByNameResponse)
  })
_sym_db.RegisterMessage(RoleAppService_roleByNameResponse)

RoleAppService_roleByIdRequest = _reflection.GeneratedProtocolMessageType('RoleAppService_roleByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLEBYIDREQUEST,
  '__module__' : 'identity.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAppService_roleByIdRequest)
  })
_sym_db.RegisterMessage(RoleAppService_roleByIdRequest)

RoleAppService_roleByIdResponse = _reflection.GeneratedProtocolMessageType('RoleAppService_roleByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLEBYIDRESPONSE,
  '__module__' : 'identity.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAppService_roleByIdResponse)
  })
_sym_db.RegisterMessage(RoleAppService_roleByIdResponse)

RoleAppService_rolesRequest = _reflection.GeneratedProtocolMessageType('RoleAppService_rolesRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLESREQUEST,
  '__module__' : 'identity.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAppService_rolesRequest)
  })
_sym_db.RegisterMessage(RoleAppService_rolesRequest)

RoleAppService_rolesResponse = _reflection.GeneratedProtocolMessageType('RoleAppService_rolesResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLESRESPONSE,
  '__module__' : 'identity.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAppService_rolesResponse)
  })
_sym_db.RegisterMessage(RoleAppService_rolesResponse)

RoleAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('RoleAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'identity.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAppService_newIdRequest)
  })
_sym_db.RegisterMessage(RoleAppService_newIdRequest)

RoleAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('RoleAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'identity.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.role.RoleAppService_newIdResponse)
  })
_sym_db.RegisterMessage(RoleAppService_newIdResponse)



_ROLEAPPSERVICE = _descriptor.ServiceDescriptor(
  name='RoleAppService',
  full_name='cafm.identity.role.RoleAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=913,
  serialized_end=1644,
  methods=[
  _descriptor.MethodDescriptor(
    name='role_by_name',
    full_name='cafm.identity.role.RoleAppService.role_by_name',
    index=0,
    containing_service=None,
    input_type=_ROLEAPPSERVICE_ROLEBYNAMEREQUEST,
    output_type=_ROLEAPPSERVICE_ROLEBYNAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='role_by_id',
    full_name='cafm.identity.role.RoleAppService.role_by_id',
    index=1,
    containing_service=None,
    input_type=_ROLEAPPSERVICE_ROLEBYIDREQUEST,
    output_type=_ROLEAPPSERVICE_ROLEBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='roles',
    full_name='cafm.identity.role.RoleAppService.roles',
    index=2,
    containing_service=None,
    input_type=_ROLEAPPSERVICE_ROLESREQUEST,
    output_type=_ROLEAPPSERVICE_ROLESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='roles_trees',
    full_name='cafm.identity.role.RoleAppService.roles_trees',
    index=3,
    containing_service=None,
    input_type=_ROLEAPPSERVICE_ROLESTREESREQUEST,
    output_type=_ROLEAPPSERVICE_ROLESTREESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='role_tree',
    full_name='cafm.identity.role.RoleAppService.role_tree',
    index=4,
    containing_service=None,
    input_type=_ROLEAPPSERVICE_ROLETREEREQUEST,
    output_type=_ROLEAPPSERVICE_ROLETREERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_id',
    full_name='cafm.identity.role.RoleAppService.new_id',
    index=5,
    containing_service=None,
    input_type=_ROLEAPPSERVICE_NEWIDREQUEST,
    output_type=_ROLEAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROLEAPPSERVICE)

DESCRIPTOR.services_by_name['RoleAppService'] = _ROLEAPPSERVICE

# @@protoc_insertion_point(module_scope)
