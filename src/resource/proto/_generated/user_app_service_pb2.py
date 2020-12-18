# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import user_pb2 as user__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='user_app_service.proto',
  package='cafm.identity.user',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16user_app_service.proto\x12\x12\x63\x61\x66m.identity.user\x1a\nuser.proto\x1a\x0border.proto\"M\n+UserAppService_userByNameAndPasswordRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"V\n,UserAppService_userByNameAndPasswordResponse\x12&\n\x04user\x18\x01 \x01(\x0b\x32\x18.cafm.identity.user.User\",\n\x1eUserAppService_userByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"I\n\x1fUserAppService_userByIdResponse\x12&\n\x04user\x18\x01 \x01(\x0b\x32\x18.cafm.identity.user.User\"p\n\x1bUserAppService_usersRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12)\n\x05order\x18\x03 \x03(\x0b\x32\x1a.cafm.identity.order.Order\"Z\n\x1cUserAppService_usersResponse\x12\'\n\x05users\x18\x01 \x03(\x0b\x32\x18.cafm.identity.user.User\x12\x11\n\titemCount\x18\x02 \x01(\x05\x32\x94\x03\n\x0eUserAppService\x12\x9c\x01\n\x15userByNameAndPassword\x12?.cafm.identity.user.UserAppService_userByNameAndPasswordRequest\x1a@.cafm.identity.user.UserAppService_userByNameAndPasswordResponse\"\x00\x12u\n\x08userById\x12\x32.cafm.identity.user.UserAppService_userByIdRequest\x1a\x33.cafm.identity.user.UserAppService_userByIdResponse\"\x00\x12l\n\x05users\x12/.cafm.identity.user.UserAppService_usersRequest\x1a\x30.cafm.identity.user.UserAppService_usersResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[user__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_USERAPPSERVICE_USERBYNAMEANDPASSWORDREQUEST = _descriptor.Descriptor(
  name='UserAppService_userByNameAndPasswordRequest',
  full_name='cafm.identity.user.UserAppService_userByNameAndPasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.identity.user.UserAppService_userByNameAndPasswordRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='cafm.identity.user.UserAppService_userByNameAndPasswordRequest.password', index=1,
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
  serialized_start=71,
  serialized_end=148,
)


_USERAPPSERVICE_USERBYNAMEANDPASSWORDRESPONSE = _descriptor.Descriptor(
  name='UserAppService_userByNameAndPasswordResponse',
  full_name='cafm.identity.user.UserAppService_userByNameAndPasswordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='cafm.identity.user.UserAppService_userByNameAndPasswordResponse.user', index=0,
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
  serialized_start=150,
  serialized_end=236,
)


_USERAPPSERVICE_USERBYIDREQUEST = _descriptor.Descriptor(
  name='UserAppService_userByIdRequest',
  full_name='cafm.identity.user.UserAppService_userByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.identity.user.UserAppService_userByIdRequest.id', index=0,
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
  serialized_start=238,
  serialized_end=282,
)


_USERAPPSERVICE_USERBYIDRESPONSE = _descriptor.Descriptor(
  name='UserAppService_userByIdResponse',
  full_name='cafm.identity.user.UserAppService_userByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='cafm.identity.user.UserAppService_userByIdResponse.user', index=0,
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
  serialized_start=284,
  serialized_end=357,
)


_USERAPPSERVICE_USERSREQUEST = _descriptor.Descriptor(
  name='UserAppService_usersRequest',
  full_name='cafm.identity.user.UserAppService_usersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.identity.user.UserAppService_usersRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.identity.user.UserAppService_usersRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.identity.user.UserAppService_usersRequest.order', index=2,
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
  serialized_start=359,
  serialized_end=471,
)


_USERAPPSERVICE_USERSRESPONSE = _descriptor.Descriptor(
  name='UserAppService_usersResponse',
  full_name='cafm.identity.user.UserAppService_usersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='cafm.identity.user.UserAppService_usersResponse.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemCount', full_name='cafm.identity.user.UserAppService_usersResponse.itemCount', index=1,
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
  serialized_start=473,
  serialized_end=563,
)

_USERAPPSERVICE_USERBYNAMEANDPASSWORDRESPONSE.fields_by_name['user'].message_type = user__pb2._USER
_USERAPPSERVICE_USERBYIDRESPONSE.fields_by_name['user'].message_type = user__pb2._USER
_USERAPPSERVICE_USERSREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_USERAPPSERVICE_USERSRESPONSE.fields_by_name['users'].message_type = user__pb2._USER
DESCRIPTOR.message_types_by_name['UserAppService_userByNameAndPasswordRequest'] = _USERAPPSERVICE_USERBYNAMEANDPASSWORDREQUEST
DESCRIPTOR.message_types_by_name['UserAppService_userByNameAndPasswordResponse'] = _USERAPPSERVICE_USERBYNAMEANDPASSWORDRESPONSE
DESCRIPTOR.message_types_by_name['UserAppService_userByIdRequest'] = _USERAPPSERVICE_USERBYIDREQUEST
DESCRIPTOR.message_types_by_name['UserAppService_userByIdResponse'] = _USERAPPSERVICE_USERBYIDRESPONSE
DESCRIPTOR.message_types_by_name['UserAppService_usersRequest'] = _USERAPPSERVICE_USERSREQUEST
DESCRIPTOR.message_types_by_name['UserAppService_usersResponse'] = _USERAPPSERVICE_USERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserAppService_userByNameAndPasswordRequest = _reflection.GeneratedProtocolMessageType('UserAppService_userByNameAndPasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERBYNAMEANDPASSWORDREQUEST,
  '__module__' : 'user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.user.UserAppService_userByNameAndPasswordRequest)
  })
_sym_db.RegisterMessage(UserAppService_userByNameAndPasswordRequest)

UserAppService_userByNameAndPasswordResponse = _reflection.GeneratedProtocolMessageType('UserAppService_userByNameAndPasswordResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERBYNAMEANDPASSWORDRESPONSE,
  '__module__' : 'user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.user.UserAppService_userByNameAndPasswordResponse)
  })
_sym_db.RegisterMessage(UserAppService_userByNameAndPasswordResponse)

UserAppService_userByIdRequest = _reflection.GeneratedProtocolMessageType('UserAppService_userByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERBYIDREQUEST,
  '__module__' : 'user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.user.UserAppService_userByIdRequest)
  })
_sym_db.RegisterMessage(UserAppService_userByIdRequest)

UserAppService_userByIdResponse = _reflection.GeneratedProtocolMessageType('UserAppService_userByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERBYIDRESPONSE,
  '__module__' : 'user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.user.UserAppService_userByIdResponse)
  })
_sym_db.RegisterMessage(UserAppService_userByIdResponse)

UserAppService_usersRequest = _reflection.GeneratedProtocolMessageType('UserAppService_usersRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERSREQUEST,
  '__module__' : 'user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.user.UserAppService_usersRequest)
  })
_sym_db.RegisterMessage(UserAppService_usersRequest)

UserAppService_usersResponse = _reflection.GeneratedProtocolMessageType('UserAppService_usersResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERSRESPONSE,
  '__module__' : 'user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.user.UserAppService_usersResponse)
  })
_sym_db.RegisterMessage(UserAppService_usersResponse)



_USERAPPSERVICE = _descriptor.ServiceDescriptor(
  name='UserAppService',
  full_name='cafm.identity.user.UserAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=566,
  serialized_end=970,
  methods=[
  _descriptor.MethodDescriptor(
    name='userByNameAndPassword',
    full_name='cafm.identity.user.UserAppService.userByNameAndPassword',
    index=0,
    containing_service=None,
    input_type=_USERAPPSERVICE_USERBYNAMEANDPASSWORDREQUEST,
    output_type=_USERAPPSERVICE_USERBYNAMEANDPASSWORDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='userById',
    full_name='cafm.identity.user.UserAppService.userById',
    index=1,
    containing_service=None,
    input_type=_USERAPPSERVICE_USERBYIDREQUEST,
    output_type=_USERAPPSERVICE_USERBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='users',
    full_name='cafm.identity.user.UserAppService.users',
    index=2,
    containing_service=None,
    input_type=_USERAPPSERVICE_USERSREQUEST,
    output_type=_USERAPPSERVICE_USERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERAPPSERVICE)

DESCRIPTOR.services_by_name['UserAppService'] = _USERAPPSERVICE

# @@protoc_insertion_point(module_scope)
