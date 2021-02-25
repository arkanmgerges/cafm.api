# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/equipment_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import equipment_pb2 as project_dot_equipment__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/equipment_app_service.proto',
  package='cafm.project.equipment',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#project/equipment_app_service.proto\x12\x16\x63\x61\x66m.project.equipment\x1a\x17project/equipment.proto\x1a\x0border.proto\"6\n(EquipmentAppService_equipmentByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"a\n)EquipmentAppService_equipmentByIdResponse\x12\x34\n\tequipment\x18\x01 \x01(\x0b\x32!.cafm.project.equipment.Equipment\"x\n%EquipmentAppService_equipmentsRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"r\n&EquipmentAppService_equipmentsResponse\x12\x35\n\nequipments\x18\x01 \x03(\x0b\x32!.cafm.project.equipment.Equipment\x12\x11\n\titemCount\x18\x02 \x01(\x05\x32\xbe\x02\n\x13\x45quipmentAppService\x12\x96\x01\n\requipmentById\x12@.cafm.project.equipment.EquipmentAppService_equipmentByIdRequest\x1a\x41.cafm.project.equipment.EquipmentAppService_equipmentByIdResponse\"\x00\x12\x8d\x01\n\nequipments\x12=.cafm.project.equipment.EquipmentAppService_equipmentsRequest\x1a>.cafm.project.equipment.EquipmentAppService_equipmentsResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[project_dot_equipment__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_EQUIPMENTAPPSERVICE_EQUIPMENTBYIDREQUEST = _descriptor.Descriptor(
  name='EquipmentAppService_equipmentByIdRequest',
  full_name='cafm.project.equipment.EquipmentAppService_equipmentByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment.EquipmentAppService_equipmentByIdRequest.id', index=0,
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
  serialized_start=101,
  serialized_end=155,
)


_EQUIPMENTAPPSERVICE_EQUIPMENTBYIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentAppService_equipmentByIdResponse',
  full_name='cafm.project.equipment.EquipmentAppService_equipmentByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipment', full_name='cafm.project.equipment.EquipmentAppService_equipmentByIdResponse.equipment', index=0,
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
  serialized_start=157,
  serialized_end=254,
)


_EQUIPMENTAPPSERVICE_EQUIPMENTSREQUEST = _descriptor.Descriptor(
  name='EquipmentAppService_equipmentsRequest',
  full_name='cafm.project.equipment.EquipmentAppService_equipmentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.equipment.EquipmentAppService_equipmentsRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.equipment.EquipmentAppService_equipmentsRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.equipment.EquipmentAppService_equipmentsRequest.order', index=2,
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
  serialized_start=256,
  serialized_end=376,
)


_EQUIPMENTAPPSERVICE_EQUIPMENTSRESPONSE = _descriptor.Descriptor(
  name='EquipmentAppService_equipmentsResponse',
  full_name='cafm.project.equipment.EquipmentAppService_equipmentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipments', full_name='cafm.project.equipment.EquipmentAppService_equipmentsResponse.equipments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemCount', full_name='cafm.project.equipment.EquipmentAppService_equipmentsResponse.itemCount', index=1,
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
  serialized_start=378,
  serialized_end=492,
)

_EQUIPMENTAPPSERVICE_EQUIPMENTBYIDRESPONSE.fields_by_name['equipment'].message_type = project_dot_equipment__pb2._EQUIPMENT
_EQUIPMENTAPPSERVICE_EQUIPMENTSREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_EQUIPMENTAPPSERVICE_EQUIPMENTSRESPONSE.fields_by_name['equipments'].message_type = project_dot_equipment__pb2._EQUIPMENT
DESCRIPTOR.message_types_by_name['EquipmentAppService_equipmentByIdRequest'] = _EQUIPMENTAPPSERVICE_EQUIPMENTBYIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentAppService_equipmentByIdResponse'] = _EQUIPMENTAPPSERVICE_EQUIPMENTBYIDRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentAppService_equipmentsRequest'] = _EQUIPMENTAPPSERVICE_EQUIPMENTSREQUEST
DESCRIPTOR.message_types_by_name['EquipmentAppService_equipmentsResponse'] = _EQUIPMENTAPPSERVICE_EQUIPMENTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquipmentAppService_equipmentByIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentAppService_equipmentByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTAPPSERVICE_EQUIPMENTBYIDREQUEST,
  '__module__' : 'project.equipment_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment.EquipmentAppService_equipmentByIdRequest)
  })
_sym_db.RegisterMessage(EquipmentAppService_equipmentByIdRequest)

EquipmentAppService_equipmentByIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentAppService_equipmentByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTAPPSERVICE_EQUIPMENTBYIDRESPONSE,
  '__module__' : 'project.equipment_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment.EquipmentAppService_equipmentByIdResponse)
  })
_sym_db.RegisterMessage(EquipmentAppService_equipmentByIdResponse)

EquipmentAppService_equipmentsRequest = _reflection.GeneratedProtocolMessageType('EquipmentAppService_equipmentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTAPPSERVICE_EQUIPMENTSREQUEST,
  '__module__' : 'project.equipment_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment.EquipmentAppService_equipmentsRequest)
  })
_sym_db.RegisterMessage(EquipmentAppService_equipmentsRequest)

EquipmentAppService_equipmentsResponse = _reflection.GeneratedProtocolMessageType('EquipmentAppService_equipmentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTAPPSERVICE_EQUIPMENTSRESPONSE,
  '__module__' : 'project.equipment_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment.EquipmentAppService_equipmentsResponse)
  })
_sym_db.RegisterMessage(EquipmentAppService_equipmentsResponse)



_EQUIPMENTAPPSERVICE = _descriptor.ServiceDescriptor(
  name='EquipmentAppService',
  full_name='cafm.project.equipment.EquipmentAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=495,
  serialized_end=813,
  methods=[
  _descriptor.MethodDescriptor(
    name='equipmentById',
    full_name='cafm.project.equipment.EquipmentAppService.equipmentById',
    index=0,
    containing_service=None,
    input_type=_EQUIPMENTAPPSERVICE_EQUIPMENTBYIDREQUEST,
    output_type=_EQUIPMENTAPPSERVICE_EQUIPMENTBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='equipments',
    full_name='cafm.project.equipment.EquipmentAppService.equipments',
    index=1,
    containing_service=None,
    input_type=_EQUIPMENTAPPSERVICE_EQUIPMENTSREQUEST,
    output_type=_EQUIPMENTAPPSERVICE_EQUIPMENTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EQUIPMENTAPPSERVICE)

DESCRIPTOR.services_by_name['EquipmentAppService'] = _EQUIPMENTAPPSERVICE

# @@protoc_insertion_point(module_scope)
