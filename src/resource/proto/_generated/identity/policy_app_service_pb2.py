# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: identity/policy_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from identity import user_includes_roles_pb2 as identity_dot_user__includes__roles__pb2
from identity import user_includes_realms_and_roles_pb2 as identity_dot_user__includes__realms__and__roles__pb2
from identity import realm_includes_users_include_roles_pb2 as identity_dot_realm__includes__users__include__roles__pb2
from identity import project_includes_realms_include_users_include_roles_pb2 as identity_dot_project__includes__realms__include__users__include__roles__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='identity/policy_app_service.proto',
  package='cafm.identity.policy',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!identity/policy_app_service.proto\x12\x14\x63\x61\x66m.identity.policy\x1a\"identity/user_includes_roles.proto\x1a-identity/user_includes_realms_and_roles.proto\x1a\x31identity/realm_includes_users_include_roles.proto\x1a\x42identity/project_includes_realms_include_users_include_roles.proto\"1\n/PolicyAppService_usersIncludeAccessRolesRequest\"\x98\x01\n0PolicyAppService_usersIncludeAccessRolesResponse\x12J\n\x19user_includes_roles_items\x18\x01 \x03(\x0b\x32\'.cafm.identity.policy.UserIncludesRoles\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"+\n)PolicyAppService_usersIncludeRolesRequest\"\x92\x01\n*PolicyAppService_usersIncludeRolesResponse\x12J\n\x19user_includes_roles_items\x18\x01 \x03(\x0b\x32\'.cafm.identity.policy.UserIncludesRoles\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"4\n2PolicyAppService_usersIncludeRealmsAndRolesRequest\"\xa9\x01\n3PolicyAppService_usersIncludeRealmsAndRolesResponse\x12X\n\x1eusers_include_realms_and_roles\x18\x01 \x03(\x0b\x32\x30.cafm.identity.policy.UserIncludesRealmsAndRoles\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"8\n6PolicyAppService_realmsIncludeUsersIncludeRolesRequest\"\xb5\x01\n7PolicyAppService_realmsIncludeUsersIncludeRolesResponse\x12`\n\"realms_include_users_include_roles\x18\x01 \x03(\x0b\x32\x34.cafm.identity.policy.RealmIncludesUsersIncludeRoles\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"G\nEPolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesRequest\"\xe5\x01\nFPolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse\x12\x80\x01\n3projects_include_realms_include_users_include_roles\x18\x01 \x03(\x0b\x32\x43.cafm.identity.policy.ProjectIncludesRealmsIncludeUsersIncludeRoles\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\x32\xd4\x07\n\x10PolicyAppService\x12\xad\x01\n\x1ausers_include_access_roles\x12\x45.cafm.identity.policy.PolicyAppService_usersIncludeAccessRolesRequest\x1a\x46.cafm.identity.policy.PolicyAppService_usersIncludeAccessRolesResponse\"\x00\x12\x9a\x01\n\x13users_include_roles\x12?.cafm.identity.policy.PolicyAppService_usersIncludeRolesRequest\x1a@.cafm.identity.policy.PolicyAppService_usersIncludeRolesResponse\"\x00\x12\xb7\x01\n\x1eusers_include_realms_and_roles\x12H.cafm.identity.policy.PolicyAppService_usersIncludeRealmsAndRolesRequest\x1aI.cafm.identity.policy.PolicyAppService_usersIncludeRealmsAndRolesResponse\"\x00\x12\xc3\x01\n\"realms_include_users_include_roles\x12L.cafm.identity.policy.PolicyAppService_realmsIncludeUsersIncludeRolesRequest\x1aM.cafm.identity.policy.PolicyAppService_realmsIncludeUsersIncludeRolesResponse\"\x00\x12\xf2\x01\n3projects_include_realms_include_users_include_roles\x12[.cafm.identity.policy.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesRequest\x1a\\.cafm.identity.policy.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[identity_dot_user__includes__roles__pb2.DESCRIPTOR,identity_dot_user__includes__realms__and__roles__pb2.DESCRIPTOR,identity_dot_realm__includes__users__include__roles__pb2.DESCRIPTOR,identity_dot_project__includes__realms__include__users__include__roles__pb2.DESCRIPTOR,])




_POLICYAPPSERVICE_USERSINCLUDEACCESSROLESREQUEST = _descriptor.Descriptor(
  name='PolicyAppService_usersIncludeAccessRolesRequest',
  full_name='cafm.identity.policy.PolicyAppService_usersIncludeAccessRolesRequest',
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
  serialized_start=261,
  serialized_end=310,
)


_POLICYAPPSERVICE_USERSINCLUDEACCESSROLESRESPONSE = _descriptor.Descriptor(
  name='PolicyAppService_usersIncludeAccessRolesResponse',
  full_name='cafm.identity.policy.PolicyAppService_usersIncludeAccessRolesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_includes_roles_items', full_name='cafm.identity.policy.PolicyAppService_usersIncludeAccessRolesResponse.user_includes_roles_items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.identity.policy.PolicyAppService_usersIncludeAccessRolesResponse.total_item_count', index=1,
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
  serialized_start=313,
  serialized_end=465,
)


_POLICYAPPSERVICE_USERSINCLUDEROLESREQUEST = _descriptor.Descriptor(
  name='PolicyAppService_usersIncludeRolesRequest',
  full_name='cafm.identity.policy.PolicyAppService_usersIncludeRolesRequest',
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
  serialized_start=467,
  serialized_end=510,
)


_POLICYAPPSERVICE_USERSINCLUDEROLESRESPONSE = _descriptor.Descriptor(
  name='PolicyAppService_usersIncludeRolesResponse',
  full_name='cafm.identity.policy.PolicyAppService_usersIncludeRolesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_includes_roles_items', full_name='cafm.identity.policy.PolicyAppService_usersIncludeRolesResponse.user_includes_roles_items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.identity.policy.PolicyAppService_usersIncludeRolesResponse.total_item_count', index=1,
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
  serialized_start=513,
  serialized_end=659,
)


_POLICYAPPSERVICE_USERSINCLUDEREALMSANDROLESREQUEST = _descriptor.Descriptor(
  name='PolicyAppService_usersIncludeRealmsAndRolesRequest',
  full_name='cafm.identity.policy.PolicyAppService_usersIncludeRealmsAndRolesRequest',
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
  serialized_start=661,
  serialized_end=713,
)


_POLICYAPPSERVICE_USERSINCLUDEREALMSANDROLESRESPONSE = _descriptor.Descriptor(
  name='PolicyAppService_usersIncludeRealmsAndRolesResponse',
  full_name='cafm.identity.policy.PolicyAppService_usersIncludeRealmsAndRolesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='users_include_realms_and_roles', full_name='cafm.identity.policy.PolicyAppService_usersIncludeRealmsAndRolesResponse.users_include_realms_and_roles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.identity.policy.PolicyAppService_usersIncludeRealmsAndRolesResponse.total_item_count', index=1,
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
  serialized_start=716,
  serialized_end=885,
)


_POLICYAPPSERVICE_REALMSINCLUDEUSERSINCLUDEROLESREQUEST = _descriptor.Descriptor(
  name='PolicyAppService_realmsIncludeUsersIncludeRolesRequest',
  full_name='cafm.identity.policy.PolicyAppService_realmsIncludeUsersIncludeRolesRequest',
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
  serialized_start=887,
  serialized_end=943,
)


_POLICYAPPSERVICE_REALMSINCLUDEUSERSINCLUDEROLESRESPONSE = _descriptor.Descriptor(
  name='PolicyAppService_realmsIncludeUsersIncludeRolesResponse',
  full_name='cafm.identity.policy.PolicyAppService_realmsIncludeUsersIncludeRolesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='realms_include_users_include_roles', full_name='cafm.identity.policy.PolicyAppService_realmsIncludeUsersIncludeRolesResponse.realms_include_users_include_roles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.identity.policy.PolicyAppService_realmsIncludeUsersIncludeRolesResponse.total_item_count', index=1,
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
  serialized_start=946,
  serialized_end=1127,
)


_POLICYAPPSERVICE_PROJECTSINCLUDEREALMSINCLUDEUSERSINCLUDEROLESREQUEST = _descriptor.Descriptor(
  name='PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesRequest',
  full_name='cafm.identity.policy.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesRequest',
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
  serialized_start=1129,
  serialized_end=1200,
)


_POLICYAPPSERVICE_PROJECTSINCLUDEREALMSINCLUDEUSERSINCLUDEROLESRESPONSE = _descriptor.Descriptor(
  name='PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse',
  full_name='cafm.identity.policy.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='projects_include_realms_include_users_include_roles', full_name='cafm.identity.policy.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse.projects_include_realms_include_users_include_roles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.identity.policy.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse.total_item_count', index=1,
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
  serialized_start=1203,
  serialized_end=1432,
)

_POLICYAPPSERVICE_USERSINCLUDEACCESSROLESRESPONSE.fields_by_name['user_includes_roles_items'].message_type = identity_dot_user__includes__roles__pb2._USERINCLUDESROLES
_POLICYAPPSERVICE_USERSINCLUDEROLESRESPONSE.fields_by_name['user_includes_roles_items'].message_type = identity_dot_user__includes__roles__pb2._USERINCLUDESROLES
_POLICYAPPSERVICE_USERSINCLUDEREALMSANDROLESRESPONSE.fields_by_name['users_include_realms_and_roles'].message_type = identity_dot_user__includes__realms__and__roles__pb2._USERINCLUDESREALMSANDROLES
_POLICYAPPSERVICE_REALMSINCLUDEUSERSINCLUDEROLESRESPONSE.fields_by_name['realms_include_users_include_roles'].message_type = identity_dot_realm__includes__users__include__roles__pb2._REALMINCLUDESUSERSINCLUDEROLES
_POLICYAPPSERVICE_PROJECTSINCLUDEREALMSINCLUDEUSERSINCLUDEROLESRESPONSE.fields_by_name['projects_include_realms_include_users_include_roles'].message_type = identity_dot_project__includes__realms__include__users__include__roles__pb2._PROJECTINCLUDESREALMSINCLUDEUSERSINCLUDEROLES
DESCRIPTOR.message_types_by_name['PolicyAppService_usersIncludeAccessRolesRequest'] = _POLICYAPPSERVICE_USERSINCLUDEACCESSROLESREQUEST
DESCRIPTOR.message_types_by_name['PolicyAppService_usersIncludeAccessRolesResponse'] = _POLICYAPPSERVICE_USERSINCLUDEACCESSROLESRESPONSE
DESCRIPTOR.message_types_by_name['PolicyAppService_usersIncludeRolesRequest'] = _POLICYAPPSERVICE_USERSINCLUDEROLESREQUEST
DESCRIPTOR.message_types_by_name['PolicyAppService_usersIncludeRolesResponse'] = _POLICYAPPSERVICE_USERSINCLUDEROLESRESPONSE
DESCRIPTOR.message_types_by_name['PolicyAppService_usersIncludeRealmsAndRolesRequest'] = _POLICYAPPSERVICE_USERSINCLUDEREALMSANDROLESREQUEST
DESCRIPTOR.message_types_by_name['PolicyAppService_usersIncludeRealmsAndRolesResponse'] = _POLICYAPPSERVICE_USERSINCLUDEREALMSANDROLESRESPONSE
DESCRIPTOR.message_types_by_name['PolicyAppService_realmsIncludeUsersIncludeRolesRequest'] = _POLICYAPPSERVICE_REALMSINCLUDEUSERSINCLUDEROLESREQUEST
DESCRIPTOR.message_types_by_name['PolicyAppService_realmsIncludeUsersIncludeRolesResponse'] = _POLICYAPPSERVICE_REALMSINCLUDEUSERSINCLUDEROLESRESPONSE
DESCRIPTOR.message_types_by_name['PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesRequest'] = _POLICYAPPSERVICE_PROJECTSINCLUDEREALMSINCLUDEUSERSINCLUDEROLESREQUEST
DESCRIPTOR.message_types_by_name['PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse'] = _POLICYAPPSERVICE_PROJECTSINCLUDEREALMSINCLUDEUSERSINCLUDEROLESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PolicyAppService_usersIncludeAccessRolesRequest = _reflection.GeneratedProtocolMessageType('PolicyAppService_usersIncludeAccessRolesRequest', (_message.Message,), {
  'DESCRIPTOR' : _POLICYAPPSERVICE_USERSINCLUDEACCESSROLESREQUEST,
  '__module__' : 'identity.policy_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.policy.PolicyAppService_usersIncludeAccessRolesRequest)
  })
_sym_db.RegisterMessage(PolicyAppService_usersIncludeAccessRolesRequest)

PolicyAppService_usersIncludeAccessRolesResponse = _reflection.GeneratedProtocolMessageType('PolicyAppService_usersIncludeAccessRolesResponse', (_message.Message,), {
  'DESCRIPTOR' : _POLICYAPPSERVICE_USERSINCLUDEACCESSROLESRESPONSE,
  '__module__' : 'identity.policy_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.policy.PolicyAppService_usersIncludeAccessRolesResponse)
  })
_sym_db.RegisterMessage(PolicyAppService_usersIncludeAccessRolesResponse)

PolicyAppService_usersIncludeRolesRequest = _reflection.GeneratedProtocolMessageType('PolicyAppService_usersIncludeRolesRequest', (_message.Message,), {
  'DESCRIPTOR' : _POLICYAPPSERVICE_USERSINCLUDEROLESREQUEST,
  '__module__' : 'identity.policy_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.policy.PolicyAppService_usersIncludeRolesRequest)
  })
_sym_db.RegisterMessage(PolicyAppService_usersIncludeRolesRequest)

PolicyAppService_usersIncludeRolesResponse = _reflection.GeneratedProtocolMessageType('PolicyAppService_usersIncludeRolesResponse', (_message.Message,), {
  'DESCRIPTOR' : _POLICYAPPSERVICE_USERSINCLUDEROLESRESPONSE,
  '__module__' : 'identity.policy_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.policy.PolicyAppService_usersIncludeRolesResponse)
  })
_sym_db.RegisterMessage(PolicyAppService_usersIncludeRolesResponse)

PolicyAppService_usersIncludeRealmsAndRolesRequest = _reflection.GeneratedProtocolMessageType('PolicyAppService_usersIncludeRealmsAndRolesRequest', (_message.Message,), {
  'DESCRIPTOR' : _POLICYAPPSERVICE_USERSINCLUDEREALMSANDROLESREQUEST,
  '__module__' : 'identity.policy_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.policy.PolicyAppService_usersIncludeRealmsAndRolesRequest)
  })
_sym_db.RegisterMessage(PolicyAppService_usersIncludeRealmsAndRolesRequest)

PolicyAppService_usersIncludeRealmsAndRolesResponse = _reflection.GeneratedProtocolMessageType('PolicyAppService_usersIncludeRealmsAndRolesResponse', (_message.Message,), {
  'DESCRIPTOR' : _POLICYAPPSERVICE_USERSINCLUDEREALMSANDROLESRESPONSE,
  '__module__' : 'identity.policy_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.policy.PolicyAppService_usersIncludeRealmsAndRolesResponse)
  })
_sym_db.RegisterMessage(PolicyAppService_usersIncludeRealmsAndRolesResponse)

PolicyAppService_realmsIncludeUsersIncludeRolesRequest = _reflection.GeneratedProtocolMessageType('PolicyAppService_realmsIncludeUsersIncludeRolesRequest', (_message.Message,), {
  'DESCRIPTOR' : _POLICYAPPSERVICE_REALMSINCLUDEUSERSINCLUDEROLESREQUEST,
  '__module__' : 'identity.policy_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.policy.PolicyAppService_realmsIncludeUsersIncludeRolesRequest)
  })
_sym_db.RegisterMessage(PolicyAppService_realmsIncludeUsersIncludeRolesRequest)

PolicyAppService_realmsIncludeUsersIncludeRolesResponse = _reflection.GeneratedProtocolMessageType('PolicyAppService_realmsIncludeUsersIncludeRolesResponse', (_message.Message,), {
  'DESCRIPTOR' : _POLICYAPPSERVICE_REALMSINCLUDEUSERSINCLUDEROLESRESPONSE,
  '__module__' : 'identity.policy_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.policy.PolicyAppService_realmsIncludeUsersIncludeRolesResponse)
  })
_sym_db.RegisterMessage(PolicyAppService_realmsIncludeUsersIncludeRolesResponse)

PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesRequest = _reflection.GeneratedProtocolMessageType('PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesRequest', (_message.Message,), {
  'DESCRIPTOR' : _POLICYAPPSERVICE_PROJECTSINCLUDEREALMSINCLUDEUSERSINCLUDEROLESREQUEST,
  '__module__' : 'identity.policy_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.policy.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesRequest)
  })
_sym_db.RegisterMessage(PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesRequest)

PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse = _reflection.GeneratedProtocolMessageType('PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse', (_message.Message,), {
  'DESCRIPTOR' : _POLICYAPPSERVICE_PROJECTSINCLUDEREALMSINCLUDEUSERSINCLUDEROLESRESPONSE,
  '__module__' : 'identity.policy_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.policy.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse)
  })
_sym_db.RegisterMessage(PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse)



_POLICYAPPSERVICE = _descriptor.ServiceDescriptor(
  name='PolicyAppService',
  full_name='cafm.identity.policy.PolicyAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1435,
  serialized_end=2415,
  methods=[
  _descriptor.MethodDescriptor(
    name='users_include_access_roles',
    full_name='cafm.identity.policy.PolicyAppService.users_include_access_roles',
    index=0,
    containing_service=None,
    input_type=_POLICYAPPSERVICE_USERSINCLUDEACCESSROLESREQUEST,
    output_type=_POLICYAPPSERVICE_USERSINCLUDEACCESSROLESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='users_include_roles',
    full_name='cafm.identity.policy.PolicyAppService.users_include_roles',
    index=1,
    containing_service=None,
    input_type=_POLICYAPPSERVICE_USERSINCLUDEROLESREQUEST,
    output_type=_POLICYAPPSERVICE_USERSINCLUDEROLESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='users_include_realms_and_roles',
    full_name='cafm.identity.policy.PolicyAppService.users_include_realms_and_roles',
    index=2,
    containing_service=None,
    input_type=_POLICYAPPSERVICE_USERSINCLUDEREALMSANDROLESREQUEST,
    output_type=_POLICYAPPSERVICE_USERSINCLUDEREALMSANDROLESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='realms_include_users_include_roles',
    full_name='cafm.identity.policy.PolicyAppService.realms_include_users_include_roles',
    index=3,
    containing_service=None,
    input_type=_POLICYAPPSERVICE_REALMSINCLUDEUSERSINCLUDEROLESREQUEST,
    output_type=_POLICYAPPSERVICE_REALMSINCLUDEUSERSINCLUDEROLESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='projects_include_realms_include_users_include_roles',
    full_name='cafm.identity.policy.PolicyAppService.projects_include_realms_include_users_include_roles',
    index=4,
    containing_service=None,
    input_type=_POLICYAPPSERVICE_PROJECTSINCLUDEREALMSINCLUDEUSERSINCLUDEROLESREQUEST,
    output_type=_POLICYAPPSERVICE_PROJECTSINCLUDEREALMSINCLUDEUSERSINCLUDEROLESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_POLICYAPPSERVICE)

DESCRIPTOR.services_by_name['PolicyAppService'] = _POLICYAPPSERVICE

# @@protoc_insertion_point(module_scope)
