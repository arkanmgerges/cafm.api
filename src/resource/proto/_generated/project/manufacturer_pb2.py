# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/manufacturer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/manufacturer.proto',
  package='cafm.project.manufacturer',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1aproject/manufacturer.proto\x12\x19\x63\x61\x66m.project.manufacturer\"(\n\x0cManufacturer\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3'
)




_MANUFACTURER = _descriptor.Descriptor(
  name='Manufacturer',
  full_name='cafm.project.manufacturer.Manufacturer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.manufacturer.Manufacturer.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.manufacturer.Manufacturer.name', index=1,
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
  serialized_start=57,
  serialized_end=97,
)

DESCRIPTOR.message_types_by_name['Manufacturer'] = _MANUFACTURER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Manufacturer = _reflection.GeneratedProtocolMessageType('Manufacturer', (_message.Message,), {
  'DESCRIPTOR' : _MANUFACTURER,
  '__module__' : 'project.manufacturer_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.manufacturer.Manufacturer)
  })
_sym_db.RegisterMessage(Manufacturer)


# @@protoc_insertion_point(module_scope)
