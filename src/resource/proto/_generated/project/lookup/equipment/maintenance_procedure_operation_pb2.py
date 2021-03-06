# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/lookup/equipment/maintenance_procedure_operation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project.lookup.equipment import maintenance_procedure_operation_parameter_pb2 as project_dot_lookup_dot_equipment_dot_maintenance__procedure__operation__parameter__pb2
from project.lookup.equipment import maintenance_procedure_operation_label_pb2 as project_dot_lookup_dot_equipment_dot_maintenance__procedure__operation__label__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/lookup/equipment/maintenance_procedure_operation.proto',
  package='cafm.project.lookup.equipment',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>project/lookup/equipment/maintenance_procedure_operation.proto\x12\x1d\x63\x61\x66m.project.lookup.equipment\x1aHproject/lookup/equipment/maintenance_procedure_operation_parameter.proto\x1a\x44project/lookup/equipment/maintenance_procedure_operation_label.proto\"\xca\x02\n\x1dMaintenanceProcedureOperation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12y\n*maintenance_procedure_operation_parameters\x18\x05 \x03(\x0b\x32\x45.cafm.project.lookup.equipment.MaintenanceProcedureOperationParameter\x12q\n&maintenance_procedure_operation_labels\x18\x06 \x03(\x0b\x32\x41.cafm.project.lookup.equipment.MaintenanceProcedureOperationLabelb\x06proto3'
  ,
  dependencies=[project_dot_lookup_dot_equipment_dot_maintenance__procedure__operation__parameter__pb2.DESCRIPTOR,project_dot_lookup_dot_equipment_dot_maintenance__procedure__operation__label__pb2.DESCRIPTOR,])




_MAINTENANCEPROCEDUREOPERATION = _descriptor.Descriptor(
  name='MaintenanceProcedureOperation',
  full_name='cafm.project.lookup.equipment.MaintenanceProcedureOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.lookup.equipment.MaintenanceProcedureOperation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.lookup.equipment.MaintenanceProcedureOperation.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cafm.project.lookup.equipment.MaintenanceProcedureOperation.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='cafm.project.lookup.equipment.MaintenanceProcedureOperation.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maintenance_procedure_operation_parameters', full_name='cafm.project.lookup.equipment.MaintenanceProcedureOperation.maintenance_procedure_operation_parameters', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maintenance_procedure_operation_labels', full_name='cafm.project.lookup.equipment.MaintenanceProcedureOperation.maintenance_procedure_operation_labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=242,
  serialized_end=572,
)

_MAINTENANCEPROCEDUREOPERATION.fields_by_name['maintenance_procedure_operation_parameters'].message_type = project_dot_lookup_dot_equipment_dot_maintenance__procedure__operation__parameter__pb2._MAINTENANCEPROCEDUREOPERATIONPARAMETER
_MAINTENANCEPROCEDUREOPERATION.fields_by_name['maintenance_procedure_operation_labels'].message_type = project_dot_lookup_dot_equipment_dot_maintenance__procedure__operation__label__pb2._MAINTENANCEPROCEDUREOPERATIONLABEL
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperation'] = _MAINTENANCEPROCEDUREOPERATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MaintenanceProcedureOperation = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperation', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATION,
  '__module__' : 'project.lookup.equipment.maintenance_procedure_operation_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.equipment.MaintenanceProcedureOperation)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperation)


# @@protoc_insertion_point(module_scope)
