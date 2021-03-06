# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/maintenance_procedure_operation_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import maintenance_procedure_operation_pb2 as project_dot_maintenance__procedure__operation__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/maintenance_procedure_operation_app_service.proto',
  package='cafm.project.maintenance_procedure_operation',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9project/maintenance_procedure_operation_app_service.proto\x12,cafm.project.maintenance_procedure_operation\x1a-project/maintenance_procedure_operation.proto\x1a\x0border.proto\"^\nPMaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xc9\x01\nQMaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse\x12t\n\x1fmaintenance_procedure_operation\x18\x01 \x01(\x0b\x32K.cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperation\"\xa3\x01\nMMaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xe1\x01\nNMaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse\x12u\n maintenance_procedure_operations\x18\x01 \x03(\x0b\x32K.cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperation\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"\xdd\x01\neMaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest\x12 \n\x18maintenance_procedure_id\x18\x01 \x01(\t\x12\x13\n\x0bresult_from\x18\x02 \x01(\x05\x12\x13\n\x0bresult_size\x18\x03 \x01(\x05\x12(\n\x06orders\x18\x04 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xf9\x01\nfMaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse\x12u\n maintenance_procedure_operations\x18\x01 \x03(\x0b\x32K.cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperation\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"6\n4MaintenanceProcedureOperationAppService_newIdRequest\"C\n5MaintenanceProcedureOperationAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xbe\t\n\'MaintenanceProcedureOperationAppService\x12\xaa\x02\n%maintenance_procedure_operation_by_id\x12~.cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest\x1a\x7f.cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse\"\x00\x12\x9f\x02\n maintenance_procedure_operations\x12{.cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest\x1a|.cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse\"\x00\x12\xed\x02\n<maintenance_procedure_operations_by_maintenance_procedure_id\x12\x93\x01.cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest\x1a\x94\x01.cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse\"\x00\x12\xd3\x01\n\x06new_id\x12\x62.cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_newIdRequest\x1a\x63.cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[project_dot_maintenance__procedure__operation__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONBYIDREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest',
  full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest.id', index=0,
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
  serialized_start=167,
  serialized_end=261,
)


_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONBYIDRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse',
  full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenance_procedure_operation', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse.maintenance_procedure_operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=264,
  serialized_end=465,
)


_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest',
  full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest.orders', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=468,
  serialized_end=631,
)


_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse',
  full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenance_procedure_operations', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse.maintenance_procedure_operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse.total_item_count', index=1,
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
  serialized_start=634,
  serialized_end=859,
)


_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSBYMAINTENANCEPROCEDUREIDREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest',
  full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenance_procedure_id', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest.maintenance_procedure_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest.result_from', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest.result_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest.orders', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=862,
  serialized_end=1083,
)


_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSBYMAINTENANCEPROCEDUREIDRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse',
  full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenance_procedure_operations', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse.maintenance_procedure_operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse.total_item_count', index=1,
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
  serialized_start=1086,
  serialized_end=1335,
)


_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationAppService_newIdRequest',
  full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_newIdRequest',
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
  serialized_start=1337,
  serialized_end=1391,
)


_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationAppService_newIdResponse',
  full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_newIdResponse.id', index=0,
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
  serialized_start=1393,
  serialized_end=1460,
)

_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONBYIDRESPONSE.fields_by_name['maintenance_procedure_operation'].message_type = project_dot_maintenance__procedure__operation__pb2._MAINTENANCEPROCEDUREOPERATION
_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSRESPONSE.fields_by_name['maintenance_procedure_operations'].message_type = project_dot_maintenance__procedure__operation__pb2._MAINTENANCEPROCEDUREOPERATION
_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSBYMAINTENANCEPROCEDUREIDREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSBYMAINTENANCEPROCEDUREIDRESPONSE.fields_by_name['maintenance_procedure_operations'].message_type = project_dot_maintenance__procedure__operation__pb2._MAINTENANCEPROCEDUREOPERATION
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest'] = _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONBYIDREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse'] = _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONBYIDRESPONSE
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest'] = _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse'] = _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSRESPONSE
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest'] = _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSBYMAINTENANCEPROCEDUREIDREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse'] = _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSBYMAINTENANCEPROCEDUREIDRESPONSE
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationAppService_newIdRequest'] = _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationAppService_newIdResponse'] = _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONBYIDREQUEST,
  '__module__' : 'project.maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest)

MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONBYIDRESPONSE,
  '__module__' : 'project.maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse)

MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSREQUEST,
  '__module__' : 'project.maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest)

MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSRESPONSE,
  '__module__' : 'project.maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse)

MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSBYMAINTENANCEPROCEDUREIDREQUEST,
  '__module__' : 'project.maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest)

MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSBYMAINTENANCEPROCEDUREIDRESPONSE,
  '__module__' : 'project.maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse)

MaintenanceProcedureOperationAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'project.maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_newIdRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationAppService_newIdRequest)

MaintenanceProcedureOperationAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'project.maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService_newIdResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationAppService_newIdResponse)



_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE = _descriptor.ServiceDescriptor(
  name='MaintenanceProcedureOperationAppService',
  full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1463,
  serialized_end=2677,
  methods=[
  _descriptor.MethodDescriptor(
    name='maintenance_procedure_operation_by_id',
    full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService.maintenance_procedure_operation_by_id',
    index=0,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONBYIDREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='maintenance_procedure_operations',
    full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService.maintenance_procedure_operations',
    index=1,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='maintenance_procedure_operations_by_maintenance_procedure_id',
    full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService.maintenance_procedure_operations_by_maintenance_procedure_id',
    index=2,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSBYMAINTENANCEPROCEDUREIDREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONSBYMAINTENANCEPROCEDUREIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_id',
    full_name='cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService.new_id',
    index=3,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAINTENANCEPROCEDUREOPERATIONAPPSERVICE)

DESCRIPTOR.services_by_name['MaintenanceProcedureOperationAppService'] = _MAINTENANCEPROCEDUREOPERATIONAPPSERVICE

# @@protoc_insertion_point(module_scope)
