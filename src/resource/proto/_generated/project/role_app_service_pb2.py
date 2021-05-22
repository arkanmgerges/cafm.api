# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/role_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import role_pb2 as project_dot_role__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/role_app_service.proto',
  package='cafm.project.role',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eproject/role_app_service.proto\x12\x11\x63\x61\x66m.project.role\x1a\x12project/role.proto\x1a\x0border.proto\"\x9a\x01\n-RoleAppService_rolesByOrganizationTypeRequest\x12\x18\n\x10organizationType\x18\x01 \x01(\t\x12\x12\n\nresultFrom\x18\x02 \x01(\x05\x12\x12\n\nresultSize\x18\x03 \x01(\x05\x12\'\n\x05order\x18\x04 \x03(\x0b\x32\x18.cafm.common.order.Order\"p\n.RoleAppService_rolesByOrganizationTypeResponse\x12&\n\x05roles\x18\x01 \x03(\x0b\x32\x17.cafm.project.role.Role\x12\x16\n\x0etotalItemCount\x18\x02 \x01(\x05\"0\n RoleAppService_roleByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"J\n!RoleAppService_roleByNameResponse\x12%\n\x04role\x18\x01 \x01(\x0b\x32\x17.cafm.project.role.Role\",\n\x1eRoleAppService_roleByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"H\n\x1fRoleAppService_roleByIdResponse\x12%\n\x04role\x18\x01 \x01(\x0b\x32\x17.cafm.project.role.Role\"n\n\x1bRoleAppService_rolesRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"^\n\x1cRoleAppService_rolesResponse\x12&\n\x05roles\x18\x01 \x03(\x0b\x32\x17.cafm.project.role.Role\x12\x16\n\x0etotalItemCount\x18\x02 \x01(\x05\"\x1d\n\x1bRoleAppService_newIdRequest\"*\n\x1cRoleAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xfb\x04\n\x0eRoleAppService\x12\xa0\x01\n\x17rolesByOrganizationType\x12@.cafm.project.role.RoleAppService_rolesByOrganizationTypeRequest\x1a\x41.cafm.project.role.RoleAppService_rolesByOrganizationTypeResponse\"\x00\x12y\n\nroleByName\x12\x33.cafm.project.role.RoleAppService_roleByNameRequest\x1a\x34.cafm.project.role.RoleAppService_roleByNameResponse\"\x00\x12s\n\x08roleById\x12\x31.cafm.project.role.RoleAppService_roleByIdRequest\x1a\x32.cafm.project.role.RoleAppService_roleByIdResponse\"\x00\x12j\n\x05roles\x12..cafm.project.role.RoleAppService_rolesRequest\x1a/.cafm.project.role.RoleAppService_rolesResponse\"\x00\x12j\n\x05newId\x12..cafm.project.role.RoleAppService_newIdRequest\x1a/.cafm.project.role.RoleAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[project_dot_role__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_ROLEAPPSERVICE_ROLESBYORGANIZATIONTYPEREQUEST = _descriptor.Descriptor(
  name='RoleAppService_rolesByOrganizationTypeRequest',
  full_name='cafm.project.role.RoleAppService_rolesByOrganizationTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organizationType', full_name='cafm.project.role.RoleAppService_rolesByOrganizationTypeRequest.organizationType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.role.RoleAppService_rolesByOrganizationTypeRequest.resultFrom', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.role.RoleAppService_rolesByOrganizationTypeRequest.resultSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.role.RoleAppService_rolesByOrganizationTypeRequest.order', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=87,
  serialized_end=241,
)


_ROLEAPPSERVICE_ROLESBYORGANIZATIONTYPERESPONSE = _descriptor.Descriptor(
  name='RoleAppService_rolesByOrganizationTypeResponse',
  full_name='cafm.project.role.RoleAppService_rolesByOrganizationTypeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roles', full_name='cafm.project.role.RoleAppService_rolesByOrganizationTypeResponse.roles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalItemCount', full_name='cafm.project.role.RoleAppService_rolesByOrganizationTypeResponse.totalItemCount', index=1,
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
  serialized_start=243,
  serialized_end=355,
)


_ROLEAPPSERVICE_ROLEBYNAMEREQUEST = _descriptor.Descriptor(
  name='RoleAppService_roleByNameRequest',
  full_name='cafm.project.role.RoleAppService_roleByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.role.RoleAppService_roleByNameRequest.name', index=0,
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
  serialized_start=357,
  serialized_end=405,
)


_ROLEAPPSERVICE_ROLEBYNAMERESPONSE = _descriptor.Descriptor(
  name='RoleAppService_roleByNameResponse',
  full_name='cafm.project.role.RoleAppService_roleByNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='cafm.project.role.RoleAppService_roleByNameResponse.role', index=0,
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
  serialized_start=407,
  serialized_end=481,
)


_ROLEAPPSERVICE_ROLEBYIDREQUEST = _descriptor.Descriptor(
  name='RoleAppService_roleByIdRequest',
  full_name='cafm.project.role.RoleAppService_roleByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.role.RoleAppService_roleByIdRequest.id', index=0,
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
  serialized_start=483,
  serialized_end=527,
)


_ROLEAPPSERVICE_ROLEBYIDRESPONSE = _descriptor.Descriptor(
  name='RoleAppService_roleByIdResponse',
  full_name='cafm.project.role.RoleAppService_roleByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='cafm.project.role.RoleAppService_roleByIdResponse.role', index=0,
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
  serialized_start=529,
  serialized_end=601,
)


_ROLEAPPSERVICE_ROLESREQUEST = _descriptor.Descriptor(
  name='RoleAppService_rolesRequest',
  full_name='cafm.project.role.RoleAppService_rolesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.role.RoleAppService_rolesRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.role.RoleAppService_rolesRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.role.RoleAppService_rolesRequest.order', index=2,
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
  serialized_start=603,
  serialized_end=713,
)


_ROLEAPPSERVICE_ROLESRESPONSE = _descriptor.Descriptor(
  name='RoleAppService_rolesResponse',
  full_name='cafm.project.role.RoleAppService_rolesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roles', full_name='cafm.project.role.RoleAppService_rolesResponse.roles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalItemCount', full_name='cafm.project.role.RoleAppService_rolesResponse.totalItemCount', index=1,
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
  serialized_start=715,
  serialized_end=809,
)


_ROLEAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='RoleAppService_newIdRequest',
  full_name='cafm.project.role.RoleAppService_newIdRequest',
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
  serialized_start=811,
  serialized_end=840,
)


_ROLEAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='RoleAppService_newIdResponse',
  full_name='cafm.project.role.RoleAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.role.RoleAppService_newIdResponse.id', index=0,
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
  serialized_start=842,
  serialized_end=884,
)

_ROLEAPPSERVICE_ROLESBYORGANIZATIONTYPEREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_ROLEAPPSERVICE_ROLESBYORGANIZATIONTYPERESPONSE.fields_by_name['roles'].message_type = project_dot_role__pb2._ROLE
_ROLEAPPSERVICE_ROLEBYNAMERESPONSE.fields_by_name['role'].message_type = project_dot_role__pb2._ROLE
_ROLEAPPSERVICE_ROLEBYIDRESPONSE.fields_by_name['role'].message_type = project_dot_role__pb2._ROLE
_ROLEAPPSERVICE_ROLESREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_ROLEAPPSERVICE_ROLESRESPONSE.fields_by_name['roles'].message_type = project_dot_role__pb2._ROLE
DESCRIPTOR.message_types_by_name['RoleAppService_rolesByOrganizationTypeRequest'] = _ROLEAPPSERVICE_ROLESBYORGANIZATIONTYPEREQUEST
DESCRIPTOR.message_types_by_name['RoleAppService_rolesByOrganizationTypeResponse'] = _ROLEAPPSERVICE_ROLESBYORGANIZATIONTYPERESPONSE
DESCRIPTOR.message_types_by_name['RoleAppService_roleByNameRequest'] = _ROLEAPPSERVICE_ROLEBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['RoleAppService_roleByNameResponse'] = _ROLEAPPSERVICE_ROLEBYNAMERESPONSE
DESCRIPTOR.message_types_by_name['RoleAppService_roleByIdRequest'] = _ROLEAPPSERVICE_ROLEBYIDREQUEST
DESCRIPTOR.message_types_by_name['RoleAppService_roleByIdResponse'] = _ROLEAPPSERVICE_ROLEBYIDRESPONSE
DESCRIPTOR.message_types_by_name['RoleAppService_rolesRequest'] = _ROLEAPPSERVICE_ROLESREQUEST
DESCRIPTOR.message_types_by_name['RoleAppService_rolesResponse'] = _ROLEAPPSERVICE_ROLESRESPONSE
DESCRIPTOR.message_types_by_name['RoleAppService_newIdRequest'] = _ROLEAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['RoleAppService_newIdResponse'] = _ROLEAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleAppService_rolesByOrganizationTypeRequest = _reflection.GeneratedProtocolMessageType('RoleAppService_rolesByOrganizationTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLESBYORGANIZATIONTYPEREQUEST,
  '__module__' : 'project.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.role.RoleAppService_rolesByOrganizationTypeRequest)
  })
_sym_db.RegisterMessage(RoleAppService_rolesByOrganizationTypeRequest)

RoleAppService_rolesByOrganizationTypeResponse = _reflection.GeneratedProtocolMessageType('RoleAppService_rolesByOrganizationTypeResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLESBYORGANIZATIONTYPERESPONSE,
  '__module__' : 'project.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.role.RoleAppService_rolesByOrganizationTypeResponse)
  })
_sym_db.RegisterMessage(RoleAppService_rolesByOrganizationTypeResponse)

RoleAppService_roleByNameRequest = _reflection.GeneratedProtocolMessageType('RoleAppService_roleByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLEBYNAMEREQUEST,
  '__module__' : 'project.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.role.RoleAppService_roleByNameRequest)
  })
_sym_db.RegisterMessage(RoleAppService_roleByNameRequest)

RoleAppService_roleByNameResponse = _reflection.GeneratedProtocolMessageType('RoleAppService_roleByNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLEBYNAMERESPONSE,
  '__module__' : 'project.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.role.RoleAppService_roleByNameResponse)
  })
_sym_db.RegisterMessage(RoleAppService_roleByNameResponse)

RoleAppService_roleByIdRequest = _reflection.GeneratedProtocolMessageType('RoleAppService_roleByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLEBYIDREQUEST,
  '__module__' : 'project.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.role.RoleAppService_roleByIdRequest)
  })
_sym_db.RegisterMessage(RoleAppService_roleByIdRequest)

RoleAppService_roleByIdResponse = _reflection.GeneratedProtocolMessageType('RoleAppService_roleByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLEBYIDRESPONSE,
  '__module__' : 'project.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.role.RoleAppService_roleByIdResponse)
  })
_sym_db.RegisterMessage(RoleAppService_roleByIdResponse)

RoleAppService_rolesRequest = _reflection.GeneratedProtocolMessageType('RoleAppService_rolesRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLESREQUEST,
  '__module__' : 'project.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.role.RoleAppService_rolesRequest)
  })
_sym_db.RegisterMessage(RoleAppService_rolesRequest)

RoleAppService_rolesResponse = _reflection.GeneratedProtocolMessageType('RoleAppService_rolesResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_ROLESRESPONSE,
  '__module__' : 'project.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.role.RoleAppService_rolesResponse)
  })
_sym_db.RegisterMessage(RoleAppService_rolesResponse)

RoleAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('RoleAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'project.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.role.RoleAppService_newIdRequest)
  })
_sym_db.RegisterMessage(RoleAppService_newIdRequest)

RoleAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('RoleAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'project.role_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.role.RoleAppService_newIdResponse)
  })
_sym_db.RegisterMessage(RoleAppService_newIdResponse)



_ROLEAPPSERVICE = _descriptor.ServiceDescriptor(
  name='RoleAppService',
  full_name='cafm.project.role.RoleAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=887,
  serialized_end=1522,
  methods=[
  _descriptor.MethodDescriptor(
    name='rolesByOrganizationType',
    full_name='cafm.project.role.RoleAppService.rolesByOrganizationType',
    index=0,
    containing_service=None,
    input_type=_ROLEAPPSERVICE_ROLESBYORGANIZATIONTYPEREQUEST,
    output_type=_ROLEAPPSERVICE_ROLESBYORGANIZATIONTYPERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='roleByName',
    full_name='cafm.project.role.RoleAppService.roleByName',
    index=1,
    containing_service=None,
    input_type=_ROLEAPPSERVICE_ROLEBYNAMEREQUEST,
    output_type=_ROLEAPPSERVICE_ROLEBYNAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='roleById',
    full_name='cafm.project.role.RoleAppService.roleById',
    index=2,
    containing_service=None,
    input_type=_ROLEAPPSERVICE_ROLEBYIDREQUEST,
    output_type=_ROLEAPPSERVICE_ROLEBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='roles',
    full_name='cafm.project.role.RoleAppService.roles',
    index=3,
    containing_service=None,
    input_type=_ROLEAPPSERVICE_ROLESREQUEST,
    output_type=_ROLEAPPSERVICE_ROLESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='newId',
    full_name='cafm.project.role.RoleAppService.newId',
    index=4,
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
