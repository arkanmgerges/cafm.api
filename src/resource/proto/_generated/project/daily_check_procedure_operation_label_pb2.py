# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/daily_check_procedure_operation_label.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/daily_check_procedure_operation_label.proto',
  package='cafm.project.daily_check_procedure_operation_label',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3project/daily_check_procedure_operation_label.proto\x12\x32\x63\x61\x66m.project.daily_check_procedure_operation_label\"\x82\x01\n!DailyCheckProcedureOperationLabel\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x16\n\x0egenerate_alert\x18\x03 \x01(\x05\x12*\n\"daily_check_procedure_operation_id\x18\x04 \x01(\tb\x06proto3'
)




_DAILYCHECKPROCEDUREOPERATIONLABEL = _descriptor.Descriptor(
  name='DailyCheckProcedureOperationLabel',
  full_name='cafm.project.daily_check_procedure_operation_label.DailyCheckProcedureOperationLabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.daily_check_procedure_operation_label.DailyCheckProcedureOperationLabel.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='cafm.project.daily_check_procedure_operation_label.DailyCheckProcedureOperationLabel.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='generate_alert', full_name='cafm.project.daily_check_procedure_operation_label.DailyCheckProcedureOperationLabel.generate_alert', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='daily_check_procedure_operation_id', full_name='cafm.project.daily_check_procedure_operation_label.DailyCheckProcedureOperationLabel.daily_check_procedure_operation_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=108,
  serialized_end=238,
)

DESCRIPTOR.message_types_by_name['DailyCheckProcedureOperationLabel'] = _DAILYCHECKPROCEDUREOPERATIONLABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyCheckProcedureOperationLabel = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureOperationLabel', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREOPERATIONLABEL,
  '__module__' : 'project.daily_check_procedure_operation_label_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation_label.DailyCheckProcedureOperationLabel)
  })
_sym_db.RegisterMessage(DailyCheckProcedureOperationLabel)


# @@protoc_insertion_point(module_scope)
