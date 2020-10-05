# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resource_type_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='resource_type_app_service.proto',
  package='cafm.identity.resourceType',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fresource_type_app_service.proto\x12\x1b\x63oral.identity.resourceType\"@\n0ResourceTypeAppService_resourceTypeByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"M\n1ResourceTypeAppService_resourceTypeByNameResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t2\xd0\x01\n\x16ResourceTypeAppService\x12\xb5\x01\n\x12resourceTypeByName\x12M.cafm.identity.resourceType.ResourceTypeAppService_resourceTypeByNameRequest\x1aN.cafm.identity.resourceType.ResourceTypeAppService_resourceTypeByNameResponse\"\x00\x62\x06proto3'
)




_RESOURCETYPEAPPSERVICE_RESOURCETYPEBYNAMEREQUEST = _descriptor.Descriptor(
  name='ResourceTypeAppService_resourceTypeByNameRequest',
  full_name='cafm.identity.resourceType.ResourceTypeAppService_resourceTypeByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.identity.resourceType.ResourceTypeAppService_resourceTypeByNameRequest.name', index=0,
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
  serialized_start=64,
  serialized_end=128,
)


_RESOURCETYPEAPPSERVICE_RESOURCETYPEBYNAMERESPONSE = _descriptor.Descriptor(
  name='ResourceTypeAppService_resourceTypeByNameResponse',
  full_name='cafm.identity.resourceType.ResourceTypeAppService_resourceTypeByNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.identity.resourceType.ResourceTypeAppService_resourceTypeByNameResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.identity.resourceType.ResourceTypeAppService_resourceTypeByNameResponse.name', index=1,
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
  serialized_start=130,
  serialized_end=207,
)

DESCRIPTOR.message_types_by_name['ResourceTypeAppService_resourceTypeByNameRequest'] = _RESOURCETYPEAPPSERVICE_RESOURCETYPEBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['ResourceTypeAppService_resourceTypeByNameResponse'] = _RESOURCETYPEAPPSERVICE_RESOURCETYPEBYNAMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourceTypeAppService_resourceTypeByNameRequest = _reflection.GeneratedProtocolMessageType('ResourceTypeAppService_resourceTypeByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCETYPEAPPSERVICE_RESOURCETYPEBYNAMEREQUEST,
  '__module__' : 'resource_type_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.resourceType.ResourceTypeAppService_resourceTypeByNameRequest)
  })
_sym_db.RegisterMessage(ResourceTypeAppService_resourceTypeByNameRequest)

ResourceTypeAppService_resourceTypeByNameResponse = _reflection.GeneratedProtocolMessageType('ResourceTypeAppService_resourceTypeByNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCETYPEAPPSERVICE_RESOURCETYPEBYNAMERESPONSE,
  '__module__' : 'resource_type_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.resourceType.ResourceTypeAppService_resourceTypeByNameResponse)
  })
_sym_db.RegisterMessage(ResourceTypeAppService_resourceTypeByNameResponse)



_RESOURCETYPEAPPSERVICE = _descriptor.ServiceDescriptor(
  name='ResourceTypeAppService',
  full_name='cafm.identity.resourceType.ResourceTypeAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=210,
  serialized_end=418,
  methods=[
  _descriptor.MethodDescriptor(
    name='resourceTypeByName',
    full_name='cafm.identity.resourceType.ResourceTypeAppService.resourceTypeByName',
    index=0,
    containing_service=None,
    input_type=_RESOURCETYPEAPPSERVICE_RESOURCETYPEBYNAMEREQUEST,
    output_type=_RESOURCETYPEAPPSERVICE_RESOURCETYPEBYNAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RESOURCETYPEAPPSERVICE)

DESCRIPTOR.services_by_name['ResourceTypeAppService'] = _RESOURCETYPEAPPSERVICE

# @@protoc_insertion_point(module_scope)
