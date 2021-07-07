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
  serialized_pb=b'\n#project/equipment_app_service.proto\x12\x16\x63\x61\x66m.project.equipment\x1a\x17project/equipment.proto\x1a\x0border.proto\"6\n(EquipmentAppService_equipmentByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"a\n)EquipmentAppService_equipmentByIdResponse\x12\x34\n\tequipment\x18\x01 \x01(\x0b\x32!.cafm.project.equipment.Equipment\"{\n%EquipmentAppService_equipmentsRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"y\n&EquipmentAppService_equipmentsResponse\x12\x35\n\nequipments\x18\x01 \x03(\x0b\x32!.cafm.project.equipment.Equipment\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"\xa4\x01\n8EquipmentAppService_linkedEquipmentsByEquipmentIdRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\x12\x14\n\x0c\x65quipment_id\x18\x04 \x01(\t\"\x8c\x01\n9EquipmentAppService_linkedEquipmentsByEquipmentIdResponse\x12\x35\n\nequipments\x18\x01 \x03(\x0b\x32!.cafm.project.equipment.Equipment\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"\"\n EquipmentAppService_newIdRequest\"/\n!EquipmentAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\x8e\x05\n\x13\x45quipmentAppService\x12\x98\x01\n\x0f\x65quipment_by_id\x12@.cafm.project.equipment.EquipmentAppService_equipmentByIdRequest\x1a\x41.cafm.project.equipment.EquipmentAppService_equipmentByIdResponse\"\x00\x12\x8d\x01\n\nequipments\x12=.cafm.project.equipment.EquipmentAppService_equipmentsRequest\x1a>.cafm.project.equipment.EquipmentAppService_equipmentsResponse\"\x00\x12\xca\x01\n!linked_equipments_by_equipment_id\x12P.cafm.project.equipment.EquipmentAppService_linkedEquipmentsByEquipmentIdRequest\x1aQ.cafm.project.equipment.EquipmentAppService_linkedEquipmentsByEquipmentIdResponse\"\x00\x12\x7f\n\x06new_id\x12\x38.cafm.project.equipment.EquipmentAppService_newIdRequest\x1a\x39.cafm.project.equipment.EquipmentAppService_newIdResponse\"\x00\x62\x06proto3'
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
      name='result_from', full_name='cafm.project.equipment.EquipmentAppService_equipmentsRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.equipment.EquipmentAppService_equipmentsRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.equipment.EquipmentAppService_equipmentsRequest.orders', index=2,
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
  serialized_end=379,
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
      name='total_item_count', full_name='cafm.project.equipment.EquipmentAppService_equipmentsResponse.total_item_count', index=1,
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
  serialized_start=381,
  serialized_end=502,
)


_EQUIPMENTAPPSERVICE_LINKEDEQUIPMENTSBYEQUIPMENTIDREQUEST = _descriptor.Descriptor(
  name='EquipmentAppService_linkedEquipmentsByEquipmentIdRequest',
  full_name='cafm.project.equipment.EquipmentAppService_linkedEquipmentsByEquipmentIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.equipment.EquipmentAppService_linkedEquipmentsByEquipmentIdRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.equipment.EquipmentAppService_linkedEquipmentsByEquipmentIdRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.equipment.EquipmentAppService_linkedEquipmentsByEquipmentIdRequest.orders', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='equipment_id', full_name='cafm.project.equipment.EquipmentAppService_linkedEquipmentsByEquipmentIdRequest.equipment_id', index=3,
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
  serialized_start=505,
  serialized_end=669,
)


_EQUIPMENTAPPSERVICE_LINKEDEQUIPMENTSBYEQUIPMENTIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentAppService_linkedEquipmentsByEquipmentIdResponse',
  full_name='cafm.project.equipment.EquipmentAppService_linkedEquipmentsByEquipmentIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipments', full_name='cafm.project.equipment.EquipmentAppService_linkedEquipmentsByEquipmentIdResponse.equipments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.equipment.EquipmentAppService_linkedEquipmentsByEquipmentIdResponse.total_item_count', index=1,
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
  serialized_start=672,
  serialized_end=812,
)


_EQUIPMENTAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='EquipmentAppService_newIdRequest',
  full_name='cafm.project.equipment.EquipmentAppService_newIdRequest',
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
  serialized_start=814,
  serialized_end=848,
)


_EQUIPMENTAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentAppService_newIdResponse',
  full_name='cafm.project.equipment.EquipmentAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment.EquipmentAppService_newIdResponse.id', index=0,
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
  serialized_start=850,
  serialized_end=897,
)

_EQUIPMENTAPPSERVICE_EQUIPMENTBYIDRESPONSE.fields_by_name['equipment'].message_type = project_dot_equipment__pb2._EQUIPMENT
_EQUIPMENTAPPSERVICE_EQUIPMENTSREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_EQUIPMENTAPPSERVICE_EQUIPMENTSRESPONSE.fields_by_name['equipments'].message_type = project_dot_equipment__pb2._EQUIPMENT
_EQUIPMENTAPPSERVICE_LINKEDEQUIPMENTSBYEQUIPMENTIDREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_EQUIPMENTAPPSERVICE_LINKEDEQUIPMENTSBYEQUIPMENTIDRESPONSE.fields_by_name['equipments'].message_type = project_dot_equipment__pb2._EQUIPMENT
DESCRIPTOR.message_types_by_name['EquipmentAppService_equipmentByIdRequest'] = _EQUIPMENTAPPSERVICE_EQUIPMENTBYIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentAppService_equipmentByIdResponse'] = _EQUIPMENTAPPSERVICE_EQUIPMENTBYIDRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentAppService_equipmentsRequest'] = _EQUIPMENTAPPSERVICE_EQUIPMENTSREQUEST
DESCRIPTOR.message_types_by_name['EquipmentAppService_equipmentsResponse'] = _EQUIPMENTAPPSERVICE_EQUIPMENTSRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentAppService_linkedEquipmentsByEquipmentIdRequest'] = _EQUIPMENTAPPSERVICE_LINKEDEQUIPMENTSBYEQUIPMENTIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentAppService_linkedEquipmentsByEquipmentIdResponse'] = _EQUIPMENTAPPSERVICE_LINKEDEQUIPMENTSBYEQUIPMENTIDRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentAppService_newIdRequest'] = _EQUIPMENTAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentAppService_newIdResponse'] = _EQUIPMENTAPPSERVICE_NEWIDRESPONSE
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

EquipmentAppService_linkedEquipmentsByEquipmentIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentAppService_linkedEquipmentsByEquipmentIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTAPPSERVICE_LINKEDEQUIPMENTSBYEQUIPMENTIDREQUEST,
  '__module__' : 'project.equipment_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment.EquipmentAppService_linkedEquipmentsByEquipmentIdRequest)
  })
_sym_db.RegisterMessage(EquipmentAppService_linkedEquipmentsByEquipmentIdRequest)

EquipmentAppService_linkedEquipmentsByEquipmentIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentAppService_linkedEquipmentsByEquipmentIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTAPPSERVICE_LINKEDEQUIPMENTSBYEQUIPMENTIDRESPONSE,
  '__module__' : 'project.equipment_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment.EquipmentAppService_linkedEquipmentsByEquipmentIdResponse)
  })
_sym_db.RegisterMessage(EquipmentAppService_linkedEquipmentsByEquipmentIdResponse)

EquipmentAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'project.equipment_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment.EquipmentAppService_newIdRequest)
  })
_sym_db.RegisterMessage(EquipmentAppService_newIdRequest)

EquipmentAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'project.equipment_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment.EquipmentAppService_newIdResponse)
  })
_sym_db.RegisterMessage(EquipmentAppService_newIdResponse)



_EQUIPMENTAPPSERVICE = _descriptor.ServiceDescriptor(
  name='EquipmentAppService',
  full_name='cafm.project.equipment.EquipmentAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=900,
  serialized_end=1554,
  methods=[
  _descriptor.MethodDescriptor(
    name='equipment_by_id',
    full_name='cafm.project.equipment.EquipmentAppService.equipment_by_id',
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
  _descriptor.MethodDescriptor(
    name='linked_equipments_by_equipment_id',
    full_name='cafm.project.equipment.EquipmentAppService.linked_equipments_by_equipment_id',
    index=2,
    containing_service=None,
    input_type=_EQUIPMENTAPPSERVICE_LINKEDEQUIPMENTSBYEQUIPMENTIDREQUEST,
    output_type=_EQUIPMENTAPPSERVICE_LINKEDEQUIPMENTSBYEQUIPMENTIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_id',
    full_name='cafm.project.equipment.EquipmentAppService.new_id',
    index=3,
    containing_service=None,
    input_type=_EQUIPMENTAPPSERVICE_NEWIDREQUEST,
    output_type=_EQUIPMENTAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EQUIPMENTAPPSERVICE)

DESCRIPTOR.services_by_name['EquipmentAppService'] = _EQUIPMENTAPPSERVICE

# @@protoc_insertion_point(module_scope)
