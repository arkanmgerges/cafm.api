# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/lookup/equipment/maintenance_procedure_operation_parameter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project.lookup.equipment import unit_pb2 as project_dot_lookup_dot_equipment_dot_unit__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/lookup/equipment/maintenance_procedure_operation_parameter.proto',
  package='cafm.project.lookup.equipment',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nHproject/lookup/equipment/maintenance_procedure_operation_parameter.proto\x12\x1d\x63\x61\x66m.project.lookup.equipment\x1a#project/lookup/equipment/unit.proto\"\x99\x01\n&MaintenanceProcedureOperationParameter\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08minValue\x18\x03 \x01(\x02\x12\x10\n\x08maxValue\x18\x04 \x01(\x02\x12\x31\n\x04unit\x18\x05 \x01(\x0b\x32#.cafm.project.lookup.equipment.Unitb\x06proto3'
  ,
  dependencies=[project_dot_lookup_dot_equipment_dot_unit__pb2.DESCRIPTOR,])




_MAINTENANCEPROCEDUREOPERATIONPARAMETER = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameter',
  full_name='cafm.project.lookup.equipment.MaintenanceProcedureOperationParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.lookup.equipment.MaintenanceProcedureOperationParameter.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.lookup.equipment.MaintenanceProcedureOperationParameter.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minValue', full_name='cafm.project.lookup.equipment.MaintenanceProcedureOperationParameter.minValue', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maxValue', full_name='cafm.project.lookup.equipment.MaintenanceProcedureOperationParameter.maxValue', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unit', full_name='cafm.project.lookup.equipment.MaintenanceProcedureOperationParameter.unit', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=145,
  serialized_end=298,
)

_MAINTENANCEPROCEDUREOPERATIONPARAMETER.fields_by_name['unit'].message_type = project_dot_lookup_dot_equipment_dot_unit__pb2._UNIT
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameter'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MaintenanceProcedureOperationParameter = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameter', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETER,
  '__module__' : 'project.lookup.equipment.maintenance_procedure_operation_parameter_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.equipment.MaintenanceProcedureOperationParameter)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameter)


# @@protoc_insertion_point(module_scope)
