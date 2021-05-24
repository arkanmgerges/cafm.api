# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/subcontractor_lookup.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import country_lookup_pb2 as project_dot_country__lookup__pb2
from project import city_lookup_pb2 as project_dot_city__lookup__pb2
from project import state_lookup_pb2 as project_dot_state__lookup__pb2
from project import subcontractor_category_lookup_pb2 as project_dot_subcontractor__category__lookup__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/subcontractor_lookup.proto',
  package='cafm.project.lookup',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"project/subcontractor_lookup.proto\x12\x13\x63\x61\x66m.project.lookup\x1a\x1cproject/country_lookup.proto\x1a\x19project/city_lookup.proto\x1a\x1aproject/state_lookup.proto\x1a+project/subcontractor_category_lookup.proto\"\xbc\x03\n\x13SubcontractorLookup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ompanyName\x18\x02 \x01(\t\x12\x12\n\nwebsiteUrl\x18\x03 \x01(\t\x12\x15\n\rcontactPerson\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x13\n\x0bphoneNumber\x18\x06 \x01(\t\x12\x12\n\naddressOne\x18\x07 \x01(\t\x12\x12\n\naddressTwo\x18\x08 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12\x12\n\npostalCode\x18\n \x01(\t\x12O\n\x15subcontractorCategory\x18\x0b \x01(\x0b\x32\x30.cafm.project.lookup.SubcontractorCategoryLookup\x12\x33\n\x07\x63ountry\x18\x0c \x01(\x0b\x32\".cafm.project.lookup.CountryLookup\x12/\n\x05state\x18\r \x01(\x0b\x32 .cafm.project.lookup.StateLookup\x12-\n\x04\x63ity\x18\x0e \x01(\x0b\x32\x1f.cafm.project.lookup.CityLookupb\x06proto3'
  ,
  dependencies=[project_dot_country__lookup__pb2.DESCRIPTOR,project_dot_city__lookup__pb2.DESCRIPTOR,project_dot_state__lookup__pb2.DESCRIPTOR,project_dot_subcontractor__category__lookup__pb2.DESCRIPTOR,])




_SUBCONTRACTORLOOKUP = _descriptor.Descriptor(
  name='SubcontractorLookup',
  full_name='cafm.project.lookup.SubcontractorLookup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.lookup.SubcontractorLookup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='companyName', full_name='cafm.project.lookup.SubcontractorLookup.companyName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='websiteUrl', full_name='cafm.project.lookup.SubcontractorLookup.websiteUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contactPerson', full_name='cafm.project.lookup.SubcontractorLookup.contactPerson', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='cafm.project.lookup.SubcontractorLookup.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phoneNumber', full_name='cafm.project.lookup.SubcontractorLookup.phoneNumber', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addressOne', full_name='cafm.project.lookup.SubcontractorLookup.addressOne', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addressTwo', full_name='cafm.project.lookup.SubcontractorLookup.addressTwo', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cafm.project.lookup.SubcontractorLookup.description', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='postalCode', full_name='cafm.project.lookup.SubcontractorLookup.postalCode', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subcontractorCategory', full_name='cafm.project.lookup.SubcontractorLookup.subcontractorCategory', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country', full_name='cafm.project.lookup.SubcontractorLookup.country', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='cafm.project.lookup.SubcontractorLookup.state', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='city', full_name='cafm.project.lookup.SubcontractorLookup.city', index=13,
      number=14, type=11, cpp_type=10, label=1,
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
  serialized_start=190,
  serialized_end=634,
)

_SUBCONTRACTORLOOKUP.fields_by_name['subcontractorCategory'].message_type = project_dot_subcontractor__category__lookup__pb2._SUBCONTRACTORCATEGORYLOOKUP
_SUBCONTRACTORLOOKUP.fields_by_name['country'].message_type = project_dot_country__lookup__pb2._COUNTRYLOOKUP
_SUBCONTRACTORLOOKUP.fields_by_name['state'].message_type = project_dot_state__lookup__pb2._STATELOOKUP
_SUBCONTRACTORLOOKUP.fields_by_name['city'].message_type = project_dot_city__lookup__pb2._CITYLOOKUP
DESCRIPTOR.message_types_by_name['SubcontractorLookup'] = _SUBCONTRACTORLOOKUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubcontractorLookup = _reflection.GeneratedProtocolMessageType('SubcontractorLookup', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTORLOOKUP,
  '__module__' : 'project.subcontractor_lookup_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.SubcontractorLookup)
  })
_sym_db.RegisterMessage(SubcontractorLookup)


# @@protoc_insertion_point(module_scope)