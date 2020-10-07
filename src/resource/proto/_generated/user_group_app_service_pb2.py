# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_group_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user_group_app_service.proto',
  package='cafm.identity.userGroup',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cuser_group_app_service.proto\x12\x17\x63\x61\x66m.identity.userGroup\":\n*UserGroupAppService_userGroupByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"G\n+UserGroupAppService_userGroupByNameResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"O\n%UserGroupAppService_userGroupsRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\":\n&UserGroupAppService_userGroupsResponse\x12\x10\n\x08response\x18\x01 \x01(\t2\xc8\x02\n\x13UserGroupAppService\x12\x9e\x01\n\x0fuserGroupByName\x12\x43.cafm.identity.userGroup.UserGroupAppService_userGroupByNameRequest\x1a\x44.cafm.identity.userGroup.UserGroupAppService_userGroupByNameResponse\"\x00\x12\x8f\x01\n\nuserGroups\x12>.cafm.identity.userGroup.UserGroupAppService_userGroupsRequest\x1a?.cafm.identity.userGroup.UserGroupAppService_userGroupsResponse\"\x00\x62\x06proto3'
)




_USERGROUPAPPSERVICE_USERGROUPBYNAMEREQUEST = _descriptor.Descriptor(
  name='UserGroupAppService_userGroupByNameRequest',
  full_name='cafm.identity.userGroup.UserGroupAppService_userGroupByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.identity.userGroup.UserGroupAppService_userGroupByNameRequest.name', index=0,
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
  serialized_start=57,
  serialized_end=115,
)


_USERGROUPAPPSERVICE_USERGROUPBYNAMERESPONSE = _descriptor.Descriptor(
  name='UserGroupAppService_userGroupByNameResponse',
  full_name='cafm.identity.userGroup.UserGroupAppService_userGroupByNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.identity.userGroup.UserGroupAppService_userGroupByNameResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.identity.userGroup.UserGroupAppService_userGroupByNameResponse.name', index=1,
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
  serialized_start=117,
  serialized_end=188,
)


_USERGROUPAPPSERVICE_USERGROUPSREQUEST = _descriptor.Descriptor(
  name='UserGroupAppService_userGroupsRequest',
  full_name='cafm.identity.userGroup.UserGroupAppService_userGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.identity.userGroup.UserGroupAppService_userGroupsRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.identity.userGroup.UserGroupAppService_userGroupsRequest.resultSize', index=1,
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
  serialized_start=190,
  serialized_end=269,
)


_USERGROUPAPPSERVICE_USERGROUPSRESPONSE = _descriptor.Descriptor(
  name='UserGroupAppService_userGroupsResponse',
  full_name='cafm.identity.userGroup.UserGroupAppService_userGroupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='cafm.identity.userGroup.UserGroupAppService_userGroupsResponse.response', index=0,
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
  serialized_start=271,
  serialized_end=329,
)

DESCRIPTOR.message_types_by_name['UserGroupAppService_userGroupByNameRequest'] = _USERGROUPAPPSERVICE_USERGROUPBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['UserGroupAppService_userGroupByNameResponse'] = _USERGROUPAPPSERVICE_USERGROUPBYNAMERESPONSE
DESCRIPTOR.message_types_by_name['UserGroupAppService_userGroupsRequest'] = _USERGROUPAPPSERVICE_USERGROUPSREQUEST
DESCRIPTOR.message_types_by_name['UserGroupAppService_userGroupsResponse'] = _USERGROUPAPPSERVICE_USERGROUPSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserGroupAppService_userGroupByNameRequest = _reflection.GeneratedProtocolMessageType('UserGroupAppService_userGroupByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERGROUPAPPSERVICE_USERGROUPBYNAMEREQUEST,
  '__module__' : 'user_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.userGroup.UserGroupAppService_userGroupByNameRequest)
  })
_sym_db.RegisterMessage(UserGroupAppService_userGroupByNameRequest)

UserGroupAppService_userGroupByNameResponse = _reflection.GeneratedProtocolMessageType('UserGroupAppService_userGroupByNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERGROUPAPPSERVICE_USERGROUPBYNAMERESPONSE,
  '__module__' : 'user_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.userGroup.UserGroupAppService_userGroupByNameResponse)
  })
_sym_db.RegisterMessage(UserGroupAppService_userGroupByNameResponse)

UserGroupAppService_userGroupsRequest = _reflection.GeneratedProtocolMessageType('UserGroupAppService_userGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERGROUPAPPSERVICE_USERGROUPSREQUEST,
  '__module__' : 'user_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.userGroup.UserGroupAppService_userGroupsRequest)
  })
_sym_db.RegisterMessage(UserGroupAppService_userGroupsRequest)

UserGroupAppService_userGroupsResponse = _reflection.GeneratedProtocolMessageType('UserGroupAppService_userGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERGROUPAPPSERVICE_USERGROUPSRESPONSE,
  '__module__' : 'user_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.userGroup.UserGroupAppService_userGroupsResponse)
  })
_sym_db.RegisterMessage(UserGroupAppService_userGroupsResponse)



_USERGROUPAPPSERVICE = _descriptor.ServiceDescriptor(
  name='UserGroupAppService',
  full_name='cafm.identity.userGroup.UserGroupAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=332,
  serialized_end=660,
  methods=[
  _descriptor.MethodDescriptor(
    name='userGroupByName',
    full_name='cafm.identity.userGroup.UserGroupAppService.userGroupByName',
    index=0,
    containing_service=None,
    input_type=_USERGROUPAPPSERVICE_USERGROUPBYNAMEREQUEST,
    output_type=_USERGROUPAPPSERVICE_USERGROUPBYNAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='userGroups',
    full_name='cafm.identity.userGroup.UserGroupAppService.userGroups',
    index=1,
    containing_service=None,
    input_type=_USERGROUPAPPSERVICE_USERGROUPSREQUEST,
    output_type=_USERGROUPAPPSERVICE_USERGROUPSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERGROUPAPPSERVICE)

DESCRIPTOR.services_by_name['UserGroupAppService'] = _USERGROUPAPPSERVICE

# @@protoc_insertion_point(module_scope)
