# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/maintenance_procedure_operation_label_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import maintenance_procedure_operation_label_pb2 as project_dot_maintenance__procedure__operation__label__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/maintenance_procedure_operation_label_app_service.proto',
  package='cafm.project.maintenance_procedure_operation_label',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?project/maintenance_procedure_operation_label_app_service.proto\x12\x32\x63\x61\x66m.project.maintenance_procedure_operation_label\x1a\x33project/maintenance_procedure_operation_label.proto\x1a\x0border.proto\"h\nZMaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xe5\x01\n[MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdResponse\x12\x85\x01\n%maintenance_procedure_operation_label\x18\x01 \x01(\x0b\x32V.cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabel\"\xad\x01\nWMaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xfd\x01\nXMaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsResponse\x12\x86\x01\n&maintenance_procedure_operation_labels\x18\x01 \x03(\x0b\x32V.cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabel\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\";\n9MaintenanceProcedureOperationLabelAppService_newIdRequest\"H\n:MaintenanceProcedureOperationLabelAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xb9\x07\n,MaintenanceProcedureOperationLabelAppService\x12\xd2\x02\n+maintenance_procedure_operation_label_by_id\x12\x8e\x01.cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdRequest\x1a\x8f\x01.cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdResponse\"\x00\x12\xc7\x02\n&maintenance_procedure_operation_labels\x12\x8b\x01.cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsRequest\x1a\x8c\x01.cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsResponse\"\x00\x12\xe9\x01\n\x06new_id\x12m.cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_newIdRequest\x1an.cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[project_dot_maintenance__procedure__operation__label__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELBYIDREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdRequest',
  full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdRequest.id', index=0,
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
  serialized_start=185,
  serialized_end=289,
)


_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELBYIDRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdResponse',
  full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenance_procedure_operation_label', full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdResponse.maintenance_procedure_operation_label', index=0,
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
  serialized_start=292,
  serialized_end=521,
)


_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELSREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsRequest',
  full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsRequest.orders', index=2,
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
  serialized_start=524,
  serialized_end=697,
)


_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELSRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsResponse',
  full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenance_procedure_operation_labels', full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsResponse.maintenance_procedure_operation_labels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsResponse.total_item_count', index=1,
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
  serialized_start=700,
  serialized_end=953,
)


_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationLabelAppService_newIdRequest',
  full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_newIdRequest',
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
  serialized_start=955,
  serialized_end=1014,
)


_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationLabelAppService_newIdResponse',
  full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_newIdResponse.id', index=0,
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
  serialized_start=1016,
  serialized_end=1088,
)

_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELBYIDRESPONSE.fields_by_name['maintenance_procedure_operation_label'].message_type = project_dot_maintenance__procedure__operation__label__pb2._MAINTENANCEPROCEDUREOPERATIONLABEL
_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELSREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELSRESPONSE.fields_by_name['maintenance_procedure_operation_labels'].message_type = project_dot_maintenance__procedure__operation__label__pb2._MAINTENANCEPROCEDUREOPERATIONLABEL
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdRequest'] = _MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELBYIDREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdResponse'] = _MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELBYIDRESPONSE
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsRequest'] = _MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELSREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsResponse'] = _MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELSRESPONSE
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationLabelAppService_newIdRequest'] = _MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationLabelAppService_newIdResponse'] = _MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELBYIDREQUEST,
  '__module__' : 'project.maintenance_procedure_operation_label_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdRequest)

MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELBYIDRESPONSE,
  '__module__' : 'project.maintenance_procedure_operation_label_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdResponse)

MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELSREQUEST,
  '__module__' : 'project.maintenance_procedure_operation_label_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsRequest)

MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELSRESPONSE,
  '__module__' : 'project.maintenance_procedure_operation_label_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsResponse)

MaintenanceProcedureOperationLabelAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationLabelAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'project.maintenance_procedure_operation_label_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_newIdRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationLabelAppService_newIdRequest)

MaintenanceProcedureOperationLabelAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationLabelAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'project.maintenance_procedure_operation_label_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService_newIdResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationLabelAppService_newIdResponse)



_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE = _descriptor.ServiceDescriptor(
  name='MaintenanceProcedureOperationLabelAppService',
  full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1091,
  serialized_end=2044,
  methods=[
  _descriptor.MethodDescriptor(
    name='maintenance_procedure_operation_label_by_id',
    full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService.maintenance_procedure_operation_label_by_id',
    index=0,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELBYIDREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='maintenance_procedure_operation_labels',
    full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService.maintenance_procedure_operation_labels',
    index=1,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELSREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONLABELSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_id',
    full_name='cafm.project.maintenance_procedure_operation_label.MaintenanceProcedureOperationLabelAppService.new_id',
    index=2,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE)

DESCRIPTOR.services_by_name['MaintenanceProcedureOperationLabelAppService'] = _MAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE

# @@protoc_insertion_point(module_scope)
