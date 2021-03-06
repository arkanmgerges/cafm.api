# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/standard_maintenance_procedure.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/standard_maintenance_procedure.proto',
  package='cafm.project.standard_maintenance_procedure',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,project/standard_maintenance_procedure.proto\x12+cafm.project.standard_maintenance_procedure\"\xc6\x01\n\x1cStandardMaintenanceProcedure\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x10\n\x08sub_type\x18\x04 \x01(\t\x12\x11\n\tfrequency\x18\x05 \x01(\t\x12\x12\n\nstart_date\x18\x06 \x01(\x05\x12\x17\n\x0forganization_id\x18\x07 \x01(\t\x12,\n$standard_equipment_category_group_id\x18\x08 \x01(\tb\x06proto3'
)




_STANDARDMAINTENANCEPROCEDURE = _descriptor.Descriptor(
  name='StandardMaintenanceProcedure',
  full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sub_type', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure.sub_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure.frequency', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure.start_date', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure.organization_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='standard_equipment_category_group_id', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure.standard_equipment_category_group_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=94,
  serialized_end=292,
)

DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedure'] = _STANDARDMAINTENANCEPROCEDURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StandardMaintenanceProcedure = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedure', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDURE,
  '__module__' : 'project.standard_maintenance_procedure_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedure)


# @@protoc_insertion_point(module_scope)
