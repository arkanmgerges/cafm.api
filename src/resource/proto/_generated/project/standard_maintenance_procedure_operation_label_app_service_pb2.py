# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/standard_maintenance_procedure_operation_label_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import standard_maintenance_procedure_operation_label_pb2 as project_dot_standard__maintenance__procedure__operation__label__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/standard_maintenance_procedure_operation_label_app_service.proto',
  package='cafm.project.standard_maintenance_procedure_operation_label',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nHproject/standard_maintenance_procedure_operation_label_app_service.proto\x12;cafm.project.standard_maintenance_procedure_operation_label\x1a<project/standard_maintenance_procedure_operation_label.proto\x1a\x0border.proto\"x\njStandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x8f\x02\nkStandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse\x12\x9f\x01\n.standard_maintenance_procedure_operation_label\x18\x01 \x01(\x0b\x32g.cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabel\"\xbd\x01\ngStandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xa7\x02\nhStandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse\x12\xa0\x01\n/standard_maintenance_procedure_operation_labels\x18\x01 \x03(\x0b\x32g.cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabel\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"C\nAStandardMaintenanceProcedureOperationLabelAppService_newIdRequest\"P\nBStandardMaintenanceProcedureOperationLabelAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xd9\x08\n4StandardMaintenanceProcedureOperationLabelAppService\x12\x8d\x03\n4standard_maintenance_procedure_operation_label_by_id\x12\xa7\x01.cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest\x1a\xa8\x01.cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse\"\x00\x12\x82\x03\n/standard_maintenance_procedure_operation_labels\x12\xa4\x01.cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest\x1a\xa5\x01.cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse\"\x00\x12\x8b\x02\n\x06new_id\x12~.cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_newIdRequest\x1a\x7f.cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[project_dot_standard__maintenance__procedure__operation__label__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELBYIDREQUEST = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest',
  full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest.id', index=0,
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
  serialized_start=212,
  serialized_end=332,
)


_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELBYIDRESPONSE = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse',
  full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='standard_maintenance_procedure_operation_label', full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse.standard_maintenance_procedure_operation_label', index=0,
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
  serialized_start=335,
  serialized_end=606,
)


_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELSREQUEST = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest',
  full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest.orders', index=2,
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
  serialized_start=609,
  serialized_end=798,
)


_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELSRESPONSE = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse',
  full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='standard_maintenance_procedure_operation_labels', full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse.standard_maintenance_procedure_operation_labels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse.total_item_count', index=1,
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
  serialized_start=801,
  serialized_end=1096,
)


_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationLabelAppService_newIdRequest',
  full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_newIdRequest',
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
  serialized_start=1098,
  serialized_end=1165,
)


_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationLabelAppService_newIdResponse',
  full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_newIdResponse.id', index=0,
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
  serialized_start=1167,
  serialized_end=1247,
)

_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELBYIDRESPONSE.fields_by_name['standard_maintenance_procedure_operation_label'].message_type = project_dot_standard__maintenance__procedure__operation__label__pb2._STANDARDMAINTENANCEPROCEDUREOPERATIONLABEL
_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELSREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELSRESPONSE.fields_by_name['standard_maintenance_procedure_operation_labels'].message_type = project_dot_standard__maintenance__procedure__operation__label__pb2._STANDARDMAINTENANCEPROCEDUREOPERATIONLABEL
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELBYIDREQUEST
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELBYIDRESPONSE
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELSREQUEST
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELSRESPONSE
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationLabelAppService_newIdRequest'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationLabelAppService_newIdResponse'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELBYIDREQUEST,
  '__module__' : 'project.standard_maintenance_procedure_operation_label_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest)

StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELBYIDRESPONSE,
  '__module__' : 'project.standard_maintenance_procedure_operation_label_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse)

StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELSREQUEST,
  '__module__' : 'project.standard_maintenance_procedure_operation_label_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest)

StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELSRESPONSE,
  '__module__' : 'project.standard_maintenance_procedure_operation_label_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse)

StandardMaintenanceProcedureOperationLabelAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationLabelAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'project.standard_maintenance_procedure_operation_label_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_newIdRequest)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationLabelAppService_newIdRequest)

StandardMaintenanceProcedureOperationLabelAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationLabelAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'project.standard_maintenance_procedure_operation_label_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService_newIdResponse)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationLabelAppService_newIdResponse)



_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE = _descriptor.ServiceDescriptor(
  name='StandardMaintenanceProcedureOperationLabelAppService',
  full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1250,
  serialized_end=2363,
  methods=[
  _descriptor.MethodDescriptor(
    name='standard_maintenance_procedure_operation_label_by_id',
    full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService.standard_maintenance_procedure_operation_label_by_id',
    index=0,
    containing_service=None,
    input_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELBYIDREQUEST,
    output_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='standard_maintenance_procedure_operation_labels',
    full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService.standard_maintenance_procedure_operation_labels',
    index=1,
    containing_service=None,
    input_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELSREQUEST,
    output_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_id',
    full_name='cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService.new_id',
    index=2,
    containing_service=None,
    input_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDREQUEST,
    output_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE)

DESCRIPTOR.services_by_name['StandardMaintenanceProcedureOperationLabelAppService'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONLABELAPPSERVICE

# @@protoc_insertion_point(module_scope)