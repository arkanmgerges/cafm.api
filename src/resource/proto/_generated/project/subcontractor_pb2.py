# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/subcontractor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/subcontractor.proto',
  package='cafm.project.subcontractor',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bproject/subcontractor.proto\x12\x1a\x63\x61\x66m.project.subcontractor\"\xa5\x02\n\rSubcontractor\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ompanyName\x18\x02 \x01(\t\x12\x12\n\nwebsiteUrl\x18\x03 \x01(\t\x12\x15\n\rcontactPerson\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x13\n\x0bphoneNumber\x18\x06 \x01(\t\x12\x12\n\naddressOne\x18\x07 \x01(\t\x12\x12\n\naddressTwo\x18\x08 \x01(\t\x12\x1f\n\x17subcontractorCategoryId\x18\t \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\n \x01(\t\x12\x11\n\tcountryId\x18\x0b \x01(\x05\x12\x0e\n\x06\x63ityId\x18\x0c \x01(\x05\x12\x0f\n\x07stateId\x18\r \x01(\x05\x12\x12\n\npostalCode\x18\x0e \x01(\tb\x06proto3'
)




_SUBCONTRACTOR = _descriptor.Descriptor(
  name='Subcontractor',
  full_name='cafm.project.subcontractor.Subcontractor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.subcontractor.Subcontractor.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='companyName', full_name='cafm.project.subcontractor.Subcontractor.companyName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='websiteUrl', full_name='cafm.project.subcontractor.Subcontractor.websiteUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contactPerson', full_name='cafm.project.subcontractor.Subcontractor.contactPerson', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='cafm.project.subcontractor.Subcontractor.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phoneNumber', full_name='cafm.project.subcontractor.Subcontractor.phoneNumber', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addressOne', full_name='cafm.project.subcontractor.Subcontractor.addressOne', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addressTwo', full_name='cafm.project.subcontractor.Subcontractor.addressTwo', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subcontractorCategoryId', full_name='cafm.project.subcontractor.Subcontractor.subcontractorCategoryId', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cafm.project.subcontractor.Subcontractor.description', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='countryId', full_name='cafm.project.subcontractor.Subcontractor.countryId', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cityId', full_name='cafm.project.subcontractor.Subcontractor.cityId', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stateId', full_name='cafm.project.subcontractor.Subcontractor.stateId', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='postalCode', full_name='cafm.project.subcontractor.Subcontractor.postalCode', index=13,
      number=14, type=9, cpp_type=9, label=1,
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
  serialized_start=60,
  serialized_end=353,
)

DESCRIPTOR.message_types_by_name['Subcontractor'] = _SUBCONTRACTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Subcontractor = _reflection.GeneratedProtocolMessageType('Subcontractor', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTOR,
  '__module__' : 'project.subcontractor_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.subcontractor.Subcontractor)
  })
_sym_db.RegisterMessage(Subcontractor)


# @@protoc_insertion_point(module_scope)
