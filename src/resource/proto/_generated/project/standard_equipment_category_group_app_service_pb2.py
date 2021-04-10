# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/standard_equipment_category_group_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import standard_equipment_category_group_pb2 as project_dot_standard__equipment__category__group__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/standard_equipment_category_group_app_service.proto',
  package='cafm.project.standard_equipment_category_group',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;project/standard_equipment_category_group_app_service.proto\x12.cafm.project.standard_equipment_category_group\x1a/project/standard_equipment_category_group.proto\x1a\x0border.proto\"`\nRStandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xcd\x01\nSStandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse\x12v\n\x1estandardEquipmentCategoryGroup\x18\x01 \x01(\x0b\x32N.cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroup\"\xa2\x01\nOStandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xde\x01\nPStandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse\x12w\n\x1fstandardEquipmentCategoryGroups\x18\x01 \x03(\x0b\x32N.cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroup\x12\x11\n\titemCount\x18\x02 \x01(\x05\"7\n5StandardEquipmentCategoryGroupAppService_newIdRequest\"D\n6StandardEquipmentCategoryGroupAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xe3\x06\n(StandardEquipmentCategoryGroupAppService\x12\xb1\x02\n\"standardEquipmentCategoryGroupById\x12\x82\x01.cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest\x1a\x83\x01.cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse\"\x00\x12\xa7\x02\n\x1fstandardEquipmentCategoryGroups\x12\x7f.cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest\x1a\x80\x01.cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse\"\x00\x12\xd8\x01\n\x05newId\x12\x65.cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_newIdRequest\x1a\x66.cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[project_dot_standard__equipment__category__group__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPBYIDREQUEST = _descriptor.Descriptor(
  name='StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest',
  full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest.id', index=0,
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
  serialized_start=173,
  serialized_end=269,
)


_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPBYIDRESPONSE = _descriptor.Descriptor(
  name='StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse',
  full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='standardEquipmentCategoryGroup', full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse.standardEquipmentCategoryGroup', index=0,
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
  serialized_start=272,
  serialized_end=477,
)


_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPSREQUEST = _descriptor.Descriptor(
  name='StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest',
  full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest.order', index=2,
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
  serialized_start=480,
  serialized_end=642,
)


_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPSRESPONSE = _descriptor.Descriptor(
  name='StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse',
  full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='standardEquipmentCategoryGroups', full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse.standardEquipmentCategoryGroups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemCount', full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse.itemCount', index=1,
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
  serialized_start=645,
  serialized_end=867,
)


_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='StandardEquipmentCategoryGroupAppService_newIdRequest',
  full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_newIdRequest',
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
  serialized_start=869,
  serialized_end=924,
)


_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='StandardEquipmentCategoryGroupAppService_newIdResponse',
  full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_newIdResponse.id', index=0,
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
  serialized_start=926,
  serialized_end=994,
)

_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPBYIDRESPONSE.fields_by_name['standardEquipmentCategoryGroup'].message_type = project_dot_standard__equipment__category__group__pb2._STANDARDEQUIPMENTCATEGORYGROUP
_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPSREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPSRESPONSE.fields_by_name['standardEquipmentCategoryGroups'].message_type = project_dot_standard__equipment__category__group__pb2._STANDARDEQUIPMENTCATEGORYGROUP
DESCRIPTOR.message_types_by_name['StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest'] = _STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPBYIDREQUEST
DESCRIPTOR.message_types_by_name['StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse'] = _STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPBYIDRESPONSE
DESCRIPTOR.message_types_by_name['StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest'] = _STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPSREQUEST
DESCRIPTOR.message_types_by_name['StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse'] = _STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPSRESPONSE
DESCRIPTOR.message_types_by_name['StandardEquipmentCategoryGroupAppService_newIdRequest'] = _STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['StandardEquipmentCategoryGroupAppService_newIdResponse'] = _STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest = _reflection.GeneratedProtocolMessageType('StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPBYIDREQUEST,
  '__module__' : 'project.standard_equipment_category_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest)
  })
_sym_db.RegisterMessage(StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest)

StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse = _reflection.GeneratedProtocolMessageType('StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPBYIDRESPONSE,
  '__module__' : 'project.standard_equipment_category_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse)
  })
_sym_db.RegisterMessage(StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse)

StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest = _reflection.GeneratedProtocolMessageType('StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPSREQUEST,
  '__module__' : 'project.standard_equipment_category_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest)
  })
_sym_db.RegisterMessage(StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest)

StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse = _reflection.GeneratedProtocolMessageType('StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPSRESPONSE,
  '__module__' : 'project.standard_equipment_category_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse)
  })
_sym_db.RegisterMessage(StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse)

StandardEquipmentCategoryGroupAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('StandardEquipmentCategoryGroupAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'project.standard_equipment_category_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_newIdRequest)
  })
_sym_db.RegisterMessage(StandardEquipmentCategoryGroupAppService_newIdRequest)

StandardEquipmentCategoryGroupAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('StandardEquipmentCategoryGroupAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'project.standard_equipment_category_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService_newIdResponse)
  })
_sym_db.RegisterMessage(StandardEquipmentCategoryGroupAppService_newIdResponse)



_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE = _descriptor.ServiceDescriptor(
  name='StandardEquipmentCategoryGroupAppService',
  full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=997,
  serialized_end=1864,
  methods=[
  _descriptor.MethodDescriptor(
    name='standardEquipmentCategoryGroupById',
    full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService.standardEquipmentCategoryGroupById',
    index=0,
    containing_service=None,
    input_type=_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPBYIDREQUEST,
    output_type=_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='standardEquipmentCategoryGroups',
    full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService.standardEquipmentCategoryGroups',
    index=1,
    containing_service=None,
    input_type=_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPSREQUEST,
    output_type=_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_STANDARDEQUIPMENTCATEGORYGROUPSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='newId',
    full_name='cafm.project.standard_equipment_category_group.StandardEquipmentCategoryGroupAppService.newId',
    index=2,
    containing_service=None,
    input_type=_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDREQUEST,
    output_type=_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE)

DESCRIPTOR.services_by_name['StandardEquipmentCategoryGroupAppService'] = _STANDARDEQUIPMENTCATEGORYGROUPAPPSERVICE

# @@protoc_insertion_point(module_scope)