# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/equipment_input_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import equipment_input_pb2 as project_dot_equipment__input__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/equipment_input_app_service.proto',
  package='cafm.project.equipment_input',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)project/equipment_input_app_service.proto\x12\x1c\x63\x61\x66m.project.equipment_input\x1a\x1dproject/equipment_input.proto\x1a\x0border.proto\"@\n2EquipmentInputAppService_equipmentInputByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"{\n3EquipmentInputAppService_equipmentInputByIdResponse\x12\x44\n\x0e\x65quipmentInput\x18\x01 \x01(\x0b\x32,.cafm.project.equipment_input.EquipmentInput\"\x82\x01\n/EquipmentInputAppService_equipmentInputsRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\x8c\x01\n0EquipmentInputAppService_equipmentInputsResponse\x12\x45\n\x0f\x65quipmentInputs\x18\x01 \x03(\x0b\x32,.cafm.project.equipment_input.EquipmentInput\x12\x11\n\titemCount\x18\x02 \x01(\x05\"\xa4\x01\n<EquipmentInputAppService_equipmentInputsByEquipmentIdRequest\x12\x13\n\x0b\x65quipmentId\x18\x01 \x01(\t\x12\x12\n\nresultFrom\x18\x02 \x01(\x05\x12\x12\n\nresultSize\x18\x03 \x01(\x05\x12\'\n\x05order\x18\x04 \x03(\x0b\x32\x18.cafm.common.order.Order\"\x99\x01\n=EquipmentInputAppService_equipmentInputsByEquipmentIdResponse\x12\x45\n\x0f\x65quipmentInputs\x18\x01 \x03(\x0b\x32,.cafm.project.equipment_input.EquipmentInput\x12\x11\n\titemCount\x18\x02 \x01(\x05\"\'\n%EquipmentInputAppService_newIdRequest\"4\n&EquipmentInputAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\x80\x06\n\x18\x45quipmentInputAppService\x12\xbb\x01\n\x12\x65quipmentInputById\x12P.cafm.project.equipment_input.EquipmentInputAppService_equipmentInputByIdRequest\x1aQ.cafm.project.equipment_input.EquipmentInputAppService_equipmentInputByIdResponse\"\x00\x12\xb2\x01\n\x0f\x65quipmentInputs\x12M.cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsRequest\x1aN.cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsResponse\"\x00\x12\xd9\x01\n\x1c\x65quipmentInputsByEquipmentId\x12Z.cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsByEquipmentIdRequest\x1a[.cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsByEquipmentIdResponse\"\x00\x12\x94\x01\n\x05newId\x12\x43.cafm.project.equipment_input.EquipmentInputAppService_newIdRequest\x1a\x44.cafm.project.equipment_input.EquipmentInputAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[project_dot_equipment__input__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTBYIDREQUEST = _descriptor.Descriptor(
  name='EquipmentInputAppService_equipmentInputByIdRequest',
  full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputByIdRequest.id', index=0,
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
  serialized_start=119,
  serialized_end=183,
)


_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTBYIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentInputAppService_equipmentInputByIdResponse',
  full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipmentInput', full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputByIdResponse.equipmentInput', index=0,
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
  serialized_start=185,
  serialized_end=308,
)


_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSREQUEST = _descriptor.Descriptor(
  name='EquipmentInputAppService_equipmentInputsRequest',
  full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsRequest.order', index=2,
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
  serialized_start=311,
  serialized_end=441,
)


_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSRESPONSE = _descriptor.Descriptor(
  name='EquipmentInputAppService_equipmentInputsResponse',
  full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipmentInputs', full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsResponse.equipmentInputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemCount', full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsResponse.itemCount', index=1,
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
  serialized_start=444,
  serialized_end=584,
)


_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSBYEQUIPMENTIDREQUEST = _descriptor.Descriptor(
  name='EquipmentInputAppService_equipmentInputsByEquipmentIdRequest',
  full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsByEquipmentIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipmentId', full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsByEquipmentIdRequest.equipmentId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsByEquipmentIdRequest.resultFrom', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsByEquipmentIdRequest.resultSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsByEquipmentIdRequest.order', index=3,
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
  serialized_start=587,
  serialized_end=751,
)


_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSBYEQUIPMENTIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentInputAppService_equipmentInputsByEquipmentIdResponse',
  full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsByEquipmentIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipmentInputs', full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsByEquipmentIdResponse.equipmentInputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemCount', full_name='cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsByEquipmentIdResponse.itemCount', index=1,
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
  serialized_start=754,
  serialized_end=907,
)


_EQUIPMENTINPUTAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='EquipmentInputAppService_newIdRequest',
  full_name='cafm.project.equipment_input.EquipmentInputAppService_newIdRequest',
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
  serialized_start=909,
  serialized_end=948,
)


_EQUIPMENTINPUTAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentInputAppService_newIdResponse',
  full_name='cafm.project.equipment_input.EquipmentInputAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_input.EquipmentInputAppService_newIdResponse.id', index=0,
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
  serialized_start=950,
  serialized_end=1002,
)

_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTBYIDRESPONSE.fields_by_name['equipmentInput'].message_type = project_dot_equipment__input__pb2._EQUIPMENTINPUT
_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSRESPONSE.fields_by_name['equipmentInputs'].message_type = project_dot_equipment__input__pb2._EQUIPMENTINPUT
_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSBYEQUIPMENTIDREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSBYEQUIPMENTIDRESPONSE.fields_by_name['equipmentInputs'].message_type = project_dot_equipment__input__pb2._EQUIPMENTINPUT
DESCRIPTOR.message_types_by_name['EquipmentInputAppService_equipmentInputByIdRequest'] = _EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTBYIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentInputAppService_equipmentInputByIdResponse'] = _EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTBYIDRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentInputAppService_equipmentInputsRequest'] = _EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSREQUEST
DESCRIPTOR.message_types_by_name['EquipmentInputAppService_equipmentInputsResponse'] = _EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentInputAppService_equipmentInputsByEquipmentIdRequest'] = _EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSBYEQUIPMENTIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentInputAppService_equipmentInputsByEquipmentIdResponse'] = _EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSBYEQUIPMENTIDRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentInputAppService_newIdRequest'] = _EQUIPMENTINPUTAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentInputAppService_newIdResponse'] = _EQUIPMENTINPUTAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquipmentInputAppService_equipmentInputByIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentInputAppService_equipmentInputByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTBYIDREQUEST,
  '__module__' : 'project.equipment_input_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_input.EquipmentInputAppService_equipmentInputByIdRequest)
  })
_sym_db.RegisterMessage(EquipmentInputAppService_equipmentInputByIdRequest)

EquipmentInputAppService_equipmentInputByIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentInputAppService_equipmentInputByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTBYIDRESPONSE,
  '__module__' : 'project.equipment_input_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_input.EquipmentInputAppService_equipmentInputByIdResponse)
  })
_sym_db.RegisterMessage(EquipmentInputAppService_equipmentInputByIdResponse)

EquipmentInputAppService_equipmentInputsRequest = _reflection.GeneratedProtocolMessageType('EquipmentInputAppService_equipmentInputsRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSREQUEST,
  '__module__' : 'project.equipment_input_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsRequest)
  })
_sym_db.RegisterMessage(EquipmentInputAppService_equipmentInputsRequest)

EquipmentInputAppService_equipmentInputsResponse = _reflection.GeneratedProtocolMessageType('EquipmentInputAppService_equipmentInputsResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSRESPONSE,
  '__module__' : 'project.equipment_input_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsResponse)
  })
_sym_db.RegisterMessage(EquipmentInputAppService_equipmentInputsResponse)

EquipmentInputAppService_equipmentInputsByEquipmentIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentInputAppService_equipmentInputsByEquipmentIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSBYEQUIPMENTIDREQUEST,
  '__module__' : 'project.equipment_input_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsByEquipmentIdRequest)
  })
_sym_db.RegisterMessage(EquipmentInputAppService_equipmentInputsByEquipmentIdRequest)

EquipmentInputAppService_equipmentInputsByEquipmentIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentInputAppService_equipmentInputsByEquipmentIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSBYEQUIPMENTIDRESPONSE,
  '__module__' : 'project.equipment_input_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_input.EquipmentInputAppService_equipmentInputsByEquipmentIdResponse)
  })
_sym_db.RegisterMessage(EquipmentInputAppService_equipmentInputsByEquipmentIdResponse)

EquipmentInputAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentInputAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTINPUTAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'project.equipment_input_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_input.EquipmentInputAppService_newIdRequest)
  })
_sym_db.RegisterMessage(EquipmentInputAppService_newIdRequest)

EquipmentInputAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentInputAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTINPUTAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'project.equipment_input_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_input.EquipmentInputAppService_newIdResponse)
  })
_sym_db.RegisterMessage(EquipmentInputAppService_newIdResponse)



_EQUIPMENTINPUTAPPSERVICE = _descriptor.ServiceDescriptor(
  name='EquipmentInputAppService',
  full_name='cafm.project.equipment_input.EquipmentInputAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1005,
  serialized_end=1773,
  methods=[
  _descriptor.MethodDescriptor(
    name='equipmentInputById',
    full_name='cafm.project.equipment_input.EquipmentInputAppService.equipmentInputById',
    index=0,
    containing_service=None,
    input_type=_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTBYIDREQUEST,
    output_type=_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='equipmentInputs',
    full_name='cafm.project.equipment_input.EquipmentInputAppService.equipmentInputs',
    index=1,
    containing_service=None,
    input_type=_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSREQUEST,
    output_type=_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='equipmentInputsByEquipmentId',
    full_name='cafm.project.equipment_input.EquipmentInputAppService.equipmentInputsByEquipmentId',
    index=2,
    containing_service=None,
    input_type=_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSBYEQUIPMENTIDREQUEST,
    output_type=_EQUIPMENTINPUTAPPSERVICE_EQUIPMENTINPUTSBYEQUIPMENTIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='newId',
    full_name='cafm.project.equipment_input.EquipmentInputAppService.newId',
    index=3,
    containing_service=None,
    input_type=_EQUIPMENTINPUTAPPSERVICE_NEWIDREQUEST,
    output_type=_EQUIPMENTINPUTAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EQUIPMENTINPUTAPPSERVICE)

DESCRIPTOR.services_by_name['EquipmentInputAppService'] = _EQUIPMENTINPUTAPPSERVICE

# @@protoc_insertion_point(module_scope)
