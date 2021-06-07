# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/lookup/daily_check_procedure/daily_check_procedure_lookup_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project.lookup.daily_check_procedure import daily_check_procedure_pb2 as project_dot_lookup_dot_daily__check__procedure_dot_daily__check__procedure__pb2
import order_pb2 as order__pb2
import filter_pb2 as filter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/lookup/daily_check_procedure/daily_check_procedure_lookup_app_service.proto',
  package='cafm.project.lookup.daily_check_procedure',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nSproject/lookup/daily_check_procedure/daily_check_procedure_lookup_app_service.proto\x12)cafm.project.lookup.daily_check_procedure\x1a@project/lookup/daily_check_procedure/daily_check_procedure.proto\x1a\x0border.proto\x1a\x0c\x66ilter.proto\"\xb2\x01\n1DailyCheckProcedureLookupAppService_lookupRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x04 \x03(\x0b\x32\x18.cafm.common.order.Order\x12+\n\x07\x66ilters\x18\x05 \x03(\x0b\x32\x1a.cafm.common.filter.Filter\"\xb0\x01\n2DailyCheckProcedureLookupAppService_lookupResponse\x12\x62\n\x1a\x64\x61ilyCheckProcedureLookups\x18\x01 \x03(\x0b\x32>.cafm.project.lookup.daily_check_procedure.DailyCheckProcedure\x12\x16\n\x0etotalItemCount\x18\x02 \x01(\x05\x32\xef\x01\n#DailyCheckProcedureLookupAppService\x12\xc7\x01\n\x06lookup\x12\\.cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService_lookupRequest\x1a].cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService_lookupResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[project_dot_lookup_dot_daily__check__procedure_dot_daily__check__procedure__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,filter__pb2.DESCRIPTOR,])




_DAILYCHECKPROCEDURELOOKUPAPPSERVICE_LOOKUPREQUEST = _descriptor.Descriptor(
  name='DailyCheckProcedureLookupAppService_lookupRequest',
  full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService_lookupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService_lookupRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService_lookupRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService_lookupRequest.orders', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filters', full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService_lookupRequest.filters', index=3,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=224,
  serialized_end=402,
)


_DAILYCHECKPROCEDURELOOKUPAPPSERVICE_LOOKUPRESPONSE = _descriptor.Descriptor(
  name='DailyCheckProcedureLookupAppService_lookupResponse',
  full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService_lookupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dailyCheckProcedureLookups', full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService_lookupResponse.dailyCheckProcedureLookups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalItemCount', full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService_lookupResponse.totalItemCount', index=1,
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
  serialized_start=405,
  serialized_end=581,
)

_DAILYCHECKPROCEDURELOOKUPAPPSERVICE_LOOKUPREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_DAILYCHECKPROCEDURELOOKUPAPPSERVICE_LOOKUPREQUEST.fields_by_name['filters'].message_type = filter__pb2._FILTER
_DAILYCHECKPROCEDURELOOKUPAPPSERVICE_LOOKUPRESPONSE.fields_by_name['dailyCheckProcedureLookups'].message_type = project_dot_lookup_dot_daily__check__procedure_dot_daily__check__procedure__pb2._DAILYCHECKPROCEDURE
DESCRIPTOR.message_types_by_name['DailyCheckProcedureLookupAppService_lookupRequest'] = _DAILYCHECKPROCEDURELOOKUPAPPSERVICE_LOOKUPREQUEST
DESCRIPTOR.message_types_by_name['DailyCheckProcedureLookupAppService_lookupResponse'] = _DAILYCHECKPROCEDURELOOKUPAPPSERVICE_LOOKUPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyCheckProcedureLookupAppService_lookupRequest = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureLookupAppService_lookupRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDURELOOKUPAPPSERVICE_LOOKUPREQUEST,
  '__module__' : 'project.lookup.daily_check_procedure.daily_check_procedure_lookup_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService_lookupRequest)
  })
_sym_db.RegisterMessage(DailyCheckProcedureLookupAppService_lookupRequest)

DailyCheckProcedureLookupAppService_lookupResponse = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureLookupAppService_lookupResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDURELOOKUPAPPSERVICE_LOOKUPRESPONSE,
  '__module__' : 'project.lookup.daily_check_procedure.daily_check_procedure_lookup_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService_lookupResponse)
  })
_sym_db.RegisterMessage(DailyCheckProcedureLookupAppService_lookupResponse)



_DAILYCHECKPROCEDURELOOKUPAPPSERVICE = _descriptor.ServiceDescriptor(
  name='DailyCheckProcedureLookupAppService',
  full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=584,
  serialized_end=823,
  methods=[
  _descriptor.MethodDescriptor(
    name='lookup',
    full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureLookupAppService.lookup',
    index=0,
    containing_service=None,
    input_type=_DAILYCHECKPROCEDURELOOKUPAPPSERVICE_LOOKUPREQUEST,
    output_type=_DAILYCHECKPROCEDURELOOKUPAPPSERVICE_LOOKUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DAILYCHECKPROCEDURELOOKUPAPPSERVICE)

DESCRIPTOR.services_by_name['DailyCheckProcedureLookupAppService'] = _DAILYCHECKPROCEDURELOOKUPAPPSERVICE

# @@protoc_insertion_point(module_scope)
