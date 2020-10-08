# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth_app_service.proto',
  package='cafm.identity.auth',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x61uth_app_service.proto\x12\x12\x63\x61\x66m.identity.auth\"Y\n7AuthAppService_authenticateUserByNameAndPasswordRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"I\n8AuthAppService_authenticateUserByNameAndPasswordResponse\x12\r\n\x05token\x18\x01 \x01(\t\"6\n%AuthAppService_isAuthenticatedRequest\x12\r\n\x05token\x18\x01 \x01(\t\":\n&AuthAppService_isAuthenticatedResponse\x12\x10\n\x08response\x18\x01 \x01(\x08\"-\n\x1c\x41uthAppService_logoutRequest\x12\r\n\x05token\x18\x01 \x01(\t\"\x1f\n\x1d\x41uthAppService_logoutResponse2\xd1\x03\n\x0e\x41uthAppService\x12\xc0\x01\n!authenticateUserByNameAndPassword\x12K.cafm.identity.auth.AuthAppService_authenticateUserByNameAndPasswordRequest\x1aL.cafm.identity.auth.AuthAppService_authenticateUserByNameAndPasswordResponse\"\x00\x12\x8a\x01\n\x0fisAuthenticated\x12\x39.cafm.identity.auth.AuthAppService_isAuthenticatedRequest\x1a:.cafm.identity.auth.AuthAppService_isAuthenticatedResponse\"\x00\x12o\n\x06logout\x12\x30.cafm.identity.auth.AuthAppService_logoutRequest\x1a\x31.cafm.identity.auth.AuthAppService_logoutResponse\"\x00\x62\x06proto3'
)




_AUTHAPPSERVICE_AUTHENTICATEUSERBYNAMEANDPASSWORDREQUEST = _descriptor.Descriptor(
  name='AuthAppService_authenticateUserByNameAndPasswordRequest',
  full_name='cafm.identity.auth.AuthAppService_authenticateUserByNameAndPasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.identity.auth.AuthAppService_authenticateUserByNameAndPasswordRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='cafm.identity.auth.AuthAppService_authenticateUserByNameAndPasswordRequest.password', index=1,
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
  serialized_start=46,
  serialized_end=135,
)


_AUTHAPPSERVICE_AUTHENTICATEUSERBYNAMEANDPASSWORDRESPONSE = _descriptor.Descriptor(
  name='AuthAppService_authenticateUserByNameAndPasswordResponse',
  full_name='cafm.identity.auth.AuthAppService_authenticateUserByNameAndPasswordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='cafm.identity.auth.AuthAppService_authenticateUserByNameAndPasswordResponse.token', index=0,
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
  serialized_start=137,
  serialized_end=210,
)


_AUTHAPPSERVICE_ISAUTHENTICATEDREQUEST = _descriptor.Descriptor(
  name='AuthAppService_isAuthenticatedRequest',
  full_name='cafm.identity.auth.AuthAppService_isAuthenticatedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='cafm.identity.auth.AuthAppService_isAuthenticatedRequest.token', index=0,
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
  serialized_start=212,
  serialized_end=266,
)


_AUTHAPPSERVICE_ISAUTHENTICATEDRESPONSE = _descriptor.Descriptor(
  name='AuthAppService_isAuthenticatedResponse',
  full_name='cafm.identity.auth.AuthAppService_isAuthenticatedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='cafm.identity.auth.AuthAppService_isAuthenticatedResponse.response', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=268,
  serialized_end=326,
)


_AUTHAPPSERVICE_LOGOUTREQUEST = _descriptor.Descriptor(
  name='AuthAppService_logoutRequest',
  full_name='cafm.identity.auth.AuthAppService_logoutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='cafm.identity.auth.AuthAppService_logoutRequest.token', index=0,
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
  serialized_start=328,
  serialized_end=373,
)


_AUTHAPPSERVICE_LOGOUTRESPONSE = _descriptor.Descriptor(
  name='AuthAppService_logoutResponse',
  full_name='cafm.identity.auth.AuthAppService_logoutResponse',
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
  serialized_start=375,
  serialized_end=406,
)

DESCRIPTOR.message_types_by_name['AuthAppService_authenticateUserByNameAndPasswordRequest'] = _AUTHAPPSERVICE_AUTHENTICATEUSERBYNAMEANDPASSWORDREQUEST
DESCRIPTOR.message_types_by_name['AuthAppService_authenticateUserByNameAndPasswordResponse'] = _AUTHAPPSERVICE_AUTHENTICATEUSERBYNAMEANDPASSWORDRESPONSE
DESCRIPTOR.message_types_by_name['AuthAppService_isAuthenticatedRequest'] = _AUTHAPPSERVICE_ISAUTHENTICATEDREQUEST
DESCRIPTOR.message_types_by_name['AuthAppService_isAuthenticatedResponse'] = _AUTHAPPSERVICE_ISAUTHENTICATEDRESPONSE
DESCRIPTOR.message_types_by_name['AuthAppService_logoutRequest'] = _AUTHAPPSERVICE_LOGOUTREQUEST
DESCRIPTOR.message_types_by_name['AuthAppService_logoutResponse'] = _AUTHAPPSERVICE_LOGOUTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthAppService_authenticateUserByNameAndPasswordRequest = _reflection.GeneratedProtocolMessageType('AuthAppService_authenticateUserByNameAndPasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHAPPSERVICE_AUTHENTICATEUSERBYNAMEANDPASSWORDREQUEST,
  '__module__' : 'auth_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.auth.AuthAppService_authenticateUserByNameAndPasswordRequest)
  })
_sym_db.RegisterMessage(AuthAppService_authenticateUserByNameAndPasswordRequest)

AuthAppService_authenticateUserByNameAndPasswordResponse = _reflection.GeneratedProtocolMessageType('AuthAppService_authenticateUserByNameAndPasswordResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHAPPSERVICE_AUTHENTICATEUSERBYNAMEANDPASSWORDRESPONSE,
  '__module__' : 'auth_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.auth.AuthAppService_authenticateUserByNameAndPasswordResponse)
  })
_sym_db.RegisterMessage(AuthAppService_authenticateUserByNameAndPasswordResponse)

AuthAppService_isAuthenticatedRequest = _reflection.GeneratedProtocolMessageType('AuthAppService_isAuthenticatedRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHAPPSERVICE_ISAUTHENTICATEDREQUEST,
  '__module__' : 'auth_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.auth.AuthAppService_isAuthenticatedRequest)
  })
_sym_db.RegisterMessage(AuthAppService_isAuthenticatedRequest)

AuthAppService_isAuthenticatedResponse = _reflection.GeneratedProtocolMessageType('AuthAppService_isAuthenticatedResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHAPPSERVICE_ISAUTHENTICATEDRESPONSE,
  '__module__' : 'auth_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.auth.AuthAppService_isAuthenticatedResponse)
  })
_sym_db.RegisterMessage(AuthAppService_isAuthenticatedResponse)

AuthAppService_logoutRequest = _reflection.GeneratedProtocolMessageType('AuthAppService_logoutRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHAPPSERVICE_LOGOUTREQUEST,
  '__module__' : 'auth_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.auth.AuthAppService_logoutRequest)
  })
_sym_db.RegisterMessage(AuthAppService_logoutRequest)

AuthAppService_logoutResponse = _reflection.GeneratedProtocolMessageType('AuthAppService_logoutResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHAPPSERVICE_LOGOUTRESPONSE,
  '__module__' : 'auth_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.auth.AuthAppService_logoutResponse)
  })
_sym_db.RegisterMessage(AuthAppService_logoutResponse)



_AUTHAPPSERVICE = _descriptor.ServiceDescriptor(
  name='AuthAppService',
  full_name='cafm.identity.auth.AuthAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=409,
  serialized_end=874,
  methods=[
  _descriptor.MethodDescriptor(
    name='authenticateUserByNameAndPassword',
    full_name='cafm.identity.auth.AuthAppService.authenticateUserByNameAndPassword',
    index=0,
    containing_service=None,
    input_type=_AUTHAPPSERVICE_AUTHENTICATEUSERBYNAMEANDPASSWORDREQUEST,
    output_type=_AUTHAPPSERVICE_AUTHENTICATEUSERBYNAMEANDPASSWORDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='isAuthenticated',
    full_name='cafm.identity.auth.AuthAppService.isAuthenticated',
    index=1,
    containing_service=None,
    input_type=_AUTHAPPSERVICE_ISAUTHENTICATEDREQUEST,
    output_type=_AUTHAPPSERVICE_ISAUTHENTICATEDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='logout',
    full_name='cafm.identity.auth.AuthAppService.logout',
    index=2,
    containing_service=None,
    input_type=_AUTHAPPSERVICE_LOGOUTREQUEST,
    output_type=_AUTHAPPSERVICE_LOGOUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHAPPSERVICE)

DESCRIPTOR.services_by_name['AuthAppService'] = _AUTHAPPSERVICE

# @@protoc_insertion_point(module_scope)
