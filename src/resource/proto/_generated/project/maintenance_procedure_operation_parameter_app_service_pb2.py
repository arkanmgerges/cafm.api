# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/maintenance_procedure_operation_parameter_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import maintenance_procedure_operation_parameter_pb2 as project_dot_maintenance__procedure__operation__parameter__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/maintenance_procedure_operation_parameter_app_service.proto',
  package='cafm.project.maintenance_procedure_operation_parameter',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCproject/maintenance_procedure_operation_parameter_app_service.proto\x12\x36\x63\x61\x66m.project.maintenance_procedure_operation_parameter\x1a\x37project/maintenance_procedure_operation_parameter.proto\x1a\x0border.proto\"p\nbMaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xf6\x01\ncMaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse\x12\x8e\x01\n&maintenanceProcedureOperationParameter\x18\x01 \x01(\x0b\x32^.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameter\"\xb2\x01\n_MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\x87\x02\n`MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse\x12\x8f\x01\n\'maintenanceProcedureOperationParameters\x18\x01 \x03(\x0b\x32^.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameter\x12\x11\n\titemCount\x18\x02 \x01(\x05\"\xfd\x01\n\x80\x01MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest\x12\'\n\x1fmaintenanceProcedureOperationId\x18\x01 \x01(\t\x12\x12\n\nresultFrom\x18\x02 \x01(\x05\x12\x12\n\nresultSize\x18\x03 \x01(\x05\x12\'\n\x05order\x18\x04 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xa9\x02\n\x81\x01MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse\x12\x8f\x01\n\'maintenanceProcedureOperationParameters\x18\x01 \x03(\x0b\x32^.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameter\x12\x11\n\titemCount\x18\x02 \x01(\x05\x32\xc7\t\n0MaintenanceProcedureOperationParameterAppService\x12\xe9\x02\n*maintenanceProcedureOperationParameterById\x12\x9a\x01.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest\x1a\x9b\x01.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse\"\x00\x12\xe0\x02\n\'maintenanceProcedureOperationParameters\x12\x97\x01.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest\x1a\x98\x01.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse\"\x00\x12\xc3\x03\nHmaintenanceProcedureOperationParametersByMaintenanceProcedureOperationId\x12\xb8\x01.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest\x1a\xb9\x01.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[project_dot_maintenance__procedure__operation__parameter__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest.id', index=0,
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
  serialized_start=197,
  serialized_end=309,
)


_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenanceProcedureOperationParameter', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse.maintenanceProcedureOperationParameter', index=0,
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
  serialized_start=312,
  serialized_end=558,
)


_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest.order', index=2,
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
  serialized_start=561,
  serialized_end=739,
)


_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenanceProcedureOperationParameters', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse.maintenanceProcedureOperationParameters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemCount', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse.itemCount', index=1,
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
  serialized_start=742,
  serialized_end=1005,
)


_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenanceProcedureOperationId', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest.maintenanceProcedureOperationId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest.resultFrom', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest.resultSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest.order', index=3,
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
  serialized_start=1008,
  serialized_end=1261,
)


_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenanceProcedureOperationParameters', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse.maintenanceProcedureOperationParameters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemCount', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse.itemCount', index=1,
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
  serialized_start=1264,
  serialized_end=1561,
)

_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDRESPONSE.fields_by_name['maintenanceProcedureOperationParameter'].message_type = project_dot_maintenance__procedure__operation__parameter__pb2._MAINTENANCEPROCEDUREOPERATIONPARAMETER
_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSRESPONSE.fields_by_name['maintenanceProcedureOperationParameters'].message_type = project_dot_maintenance__procedure__operation__parameter__pb2._MAINTENANCEPROCEDUREOPERATIONPARAMETER
_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDRESPONSE.fields_by_name['maintenanceProcedureOperationParameters'].message_type = project_dot_maintenance__procedure__operation__parameter__pb2._MAINTENANCEPROCEDUREOPERATIONPARAMETER
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDRESPONSE
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSRESPONSE
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDREQUEST,
  '__module__' : 'project.maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest)

MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDRESPONSE,
  '__module__' : 'project.maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse)

MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSREQUEST,
  '__module__' : 'project.maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest)

MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSRESPONSE,
  '__module__' : 'project.maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse)

MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDREQUEST,
  '__module__' : 'project.maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest)

MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDRESPONSE,
  '__module__' : 'project.maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse)



_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE = _descriptor.ServiceDescriptor(
  name='MaintenanceProcedureOperationParameterAppService',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1564,
  serialized_end=2787,
  methods=[
  _descriptor.MethodDescriptor(
    name='maintenanceProcedureOperationParameterById',
    full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService.maintenanceProcedureOperationParameterById',
    index=0,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='maintenanceProcedureOperationParameters',
    full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService.maintenanceProcedureOperationParameters',
    index=1,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='maintenanceProcedureOperationParametersByMaintenanceProcedureOperationId',
    full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService.maintenanceProcedureOperationParametersByMaintenanceProcedureOperationId',
    index=2,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE)

DESCRIPTOR.services_by_name['MaintenanceProcedureOperationParameterAppService'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE

# @@protoc_insertion_point(module_scope)
