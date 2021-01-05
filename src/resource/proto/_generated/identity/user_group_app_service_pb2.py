# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: identity/user_group_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from identity import user_group_pb2 as identity_dot_user__group__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='identity/user_group_app_service.proto',
  package='cafm.identity.user_group',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%identity/user_group_app_service.proto\x12\x18\x63\x61\x66m.identity.user_group\x1a\x19identity/user_group.proto\x1a\x0border.proto\":\n*UserGroupAppService_userGroupByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"e\n+UserGroupAppService_userGroupByNameResponse\x12\x36\n\tuserGroup\x18\x01 \x01(\x0b\x32#.cafm.identity.user_group.UserGroup\"6\n(UserGroupAppService_userGroupByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"c\n)UserGroupAppService_userGroupByIdResponse\x12\x36\n\tuserGroup\x18\x01 \x01(\x0b\x32#.cafm.identity.user_group.UserGroup\"x\n%UserGroupAppService_userGroupsRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"t\n&UserGroupAppService_userGroupsResponse\x12\x37\n\nuserGroups\x18\x01 \x03(\x0b\x32#.cafm.identity.user_group.UserGroup\x12\x11\n\titemCount\x18\x02 \x01(\x05\x32\xe9\x03\n\x13UserGroupAppService\x12\xa0\x01\n\x0fuserGroupByName\x12\x44.cafm.identity.user_group.UserGroupAppService_userGroupByNameRequest\x1a\x45.cafm.identity.user_group.UserGroupAppService_userGroupByNameResponse\"\x00\x12\x9a\x01\n\ruserGroupById\x12\x42.cafm.identity.user_group.UserGroupAppService_userGroupByIdRequest\x1a\x43.cafm.identity.user_group.UserGroupAppService_userGroupByIdResponse\"\x00\x12\x91\x01\n\nuserGroups\x12?.cafm.identity.user_group.UserGroupAppService_userGroupsRequest\x1a@.cafm.identity.user_group.UserGroupAppService_userGroupsResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[identity_dot_user__group__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_USERGROUPAPPSERVICE_USERGROUPBYNAMEREQUEST = _descriptor.Descriptor(
  name='UserGroupAppService_userGroupByNameRequest',
  full_name='cafm.identity.user_group.UserGroupAppService_userGroupByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.identity.user_group.UserGroupAppService_userGroupByNameRequest.name', index=0,
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
  serialized_start=107,
  serialized_end=165,
)


_USERGROUPAPPSERVICE_USERGROUPBYNAMERESPONSE = _descriptor.Descriptor(
  name='UserGroupAppService_userGroupByNameResponse',
  full_name='cafm.identity.user_group.UserGroupAppService_userGroupByNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userGroup', full_name='cafm.identity.user_group.UserGroupAppService_userGroupByNameResponse.userGroup', index=0,
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
  serialized_start=167,
  serialized_end=268,
)


_USERGROUPAPPSERVICE_USERGROUPBYIDREQUEST = _descriptor.Descriptor(
  name='UserGroupAppService_userGroupByIdRequest',
  full_name='cafm.identity.user_group.UserGroupAppService_userGroupByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.identity.user_group.UserGroupAppService_userGroupByIdRequest.id', index=0,
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
  serialized_start=270,
  serialized_end=324,
)


_USERGROUPAPPSERVICE_USERGROUPBYIDRESPONSE = _descriptor.Descriptor(
  name='UserGroupAppService_userGroupByIdResponse',
  full_name='cafm.identity.user_group.UserGroupAppService_userGroupByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userGroup', full_name='cafm.identity.user_group.UserGroupAppService_userGroupByIdResponse.userGroup', index=0,
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
  serialized_start=326,
  serialized_end=425,
)


_USERGROUPAPPSERVICE_USERGROUPSREQUEST = _descriptor.Descriptor(
  name='UserGroupAppService_userGroupsRequest',
  full_name='cafm.identity.user_group.UserGroupAppService_userGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.identity.user_group.UserGroupAppService_userGroupsRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.identity.user_group.UserGroupAppService_userGroupsRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.identity.user_group.UserGroupAppService_userGroupsRequest.order', index=2,
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
  serialized_start=427,
  serialized_end=547,
)


_USERGROUPAPPSERVICE_USERGROUPSRESPONSE = _descriptor.Descriptor(
  name='UserGroupAppService_userGroupsResponse',
  full_name='cafm.identity.user_group.UserGroupAppService_userGroupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userGroups', full_name='cafm.identity.user_group.UserGroupAppService_userGroupsResponse.userGroups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemCount', full_name='cafm.identity.user_group.UserGroupAppService_userGroupsResponse.itemCount', index=1,
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
  serialized_start=549,
  serialized_end=665,
)

_USERGROUPAPPSERVICE_USERGROUPBYNAMERESPONSE.fields_by_name['userGroup'].message_type = identity_dot_user__group__pb2._USERGROUP
_USERGROUPAPPSERVICE_USERGROUPBYIDRESPONSE.fields_by_name['userGroup'].message_type = identity_dot_user__group__pb2._USERGROUP
_USERGROUPAPPSERVICE_USERGROUPSREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_USERGROUPAPPSERVICE_USERGROUPSRESPONSE.fields_by_name['userGroups'].message_type = identity_dot_user__group__pb2._USERGROUP
DESCRIPTOR.message_types_by_name['UserGroupAppService_userGroupByNameRequest'] = _USERGROUPAPPSERVICE_USERGROUPBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['UserGroupAppService_userGroupByNameResponse'] = _USERGROUPAPPSERVICE_USERGROUPBYNAMERESPONSE
DESCRIPTOR.message_types_by_name['UserGroupAppService_userGroupByIdRequest'] = _USERGROUPAPPSERVICE_USERGROUPBYIDREQUEST
DESCRIPTOR.message_types_by_name['UserGroupAppService_userGroupByIdResponse'] = _USERGROUPAPPSERVICE_USERGROUPBYIDRESPONSE
DESCRIPTOR.message_types_by_name['UserGroupAppService_userGroupsRequest'] = _USERGROUPAPPSERVICE_USERGROUPSREQUEST
DESCRIPTOR.message_types_by_name['UserGroupAppService_userGroupsResponse'] = _USERGROUPAPPSERVICE_USERGROUPSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserGroupAppService_userGroupByNameRequest = _reflection.GeneratedProtocolMessageType('UserGroupAppService_userGroupByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERGROUPAPPSERVICE_USERGROUPBYNAMEREQUEST,
  '__module__' : 'identity.user_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.user_group.UserGroupAppService_userGroupByNameRequest)
  })
_sym_db.RegisterMessage(UserGroupAppService_userGroupByNameRequest)

UserGroupAppService_userGroupByNameResponse = _reflection.GeneratedProtocolMessageType('UserGroupAppService_userGroupByNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERGROUPAPPSERVICE_USERGROUPBYNAMERESPONSE,
  '__module__' : 'identity.user_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.user_group.UserGroupAppService_userGroupByNameResponse)
  })
_sym_db.RegisterMessage(UserGroupAppService_userGroupByNameResponse)

UserGroupAppService_userGroupByIdRequest = _reflection.GeneratedProtocolMessageType('UserGroupAppService_userGroupByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERGROUPAPPSERVICE_USERGROUPBYIDREQUEST,
  '__module__' : 'identity.user_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.user_group.UserGroupAppService_userGroupByIdRequest)
  })
_sym_db.RegisterMessage(UserGroupAppService_userGroupByIdRequest)

UserGroupAppService_userGroupByIdResponse = _reflection.GeneratedProtocolMessageType('UserGroupAppService_userGroupByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERGROUPAPPSERVICE_USERGROUPBYIDRESPONSE,
  '__module__' : 'identity.user_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.user_group.UserGroupAppService_userGroupByIdResponse)
  })
_sym_db.RegisterMessage(UserGroupAppService_userGroupByIdResponse)

UserGroupAppService_userGroupsRequest = _reflection.GeneratedProtocolMessageType('UserGroupAppService_userGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERGROUPAPPSERVICE_USERGROUPSREQUEST,
  '__module__' : 'identity.user_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.user_group.UserGroupAppService_userGroupsRequest)
  })
_sym_db.RegisterMessage(UserGroupAppService_userGroupsRequest)

UserGroupAppService_userGroupsResponse = _reflection.GeneratedProtocolMessageType('UserGroupAppService_userGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERGROUPAPPSERVICE_USERGROUPSRESPONSE,
  '__module__' : 'identity.user_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.user_group.UserGroupAppService_userGroupsResponse)
  })
_sym_db.RegisterMessage(UserGroupAppService_userGroupsResponse)



_USERGROUPAPPSERVICE = _descriptor.ServiceDescriptor(
  name='UserGroupAppService',
  full_name='cafm.identity.user_group.UserGroupAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=668,
  serialized_end=1157,
  methods=[
  _descriptor.MethodDescriptor(
    name='userGroupByName',
    full_name='cafm.identity.user_group.UserGroupAppService.userGroupByName',
    index=0,
    containing_service=None,
    input_type=_USERGROUPAPPSERVICE_USERGROUPBYNAMEREQUEST,
    output_type=_USERGROUPAPPSERVICE_USERGROUPBYNAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='userGroupById',
    full_name='cafm.identity.user_group.UserGroupAppService.userGroupById',
    index=1,
    containing_service=None,
    input_type=_USERGROUPAPPSERVICE_USERGROUPBYIDREQUEST,
    output_type=_USERGROUPAPPSERVICE_USERGROUPBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='userGroups',
    full_name='cafm.identity.user_group.UserGroupAppService.userGroups',
    index=2,
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