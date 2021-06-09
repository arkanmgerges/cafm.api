# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/building_level.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import building_level_room_pb2 as project_dot_building__level__room__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/building_level.proto',
  package='cafm.project.project',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cproject/building_level.proto\x12\x14\x63\x61\x66m.project.project\x1a!project/building_level_room.proto\"\x9c\x01\n\rBuildingLevel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x62uilding_ids\x18\x03 \x03(\t\x12\x45\n\x14\x62uilding_level_rooms\x18\x04 \x03(\x0b\x32\'.cafm.project.project.BuildingLevelRoom\x12\x14\n\x0cis_sub_level\x18\x05 \x01(\x08\x62\x06proto3'
  ,
  dependencies=[project_dot_building__level__room__pb2.DESCRIPTOR,])




_BUILDINGLEVEL = _descriptor.Descriptor(
  name='BuildingLevel',
  full_name='cafm.project.project.BuildingLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.project.BuildingLevel.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.project.BuildingLevel.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='building_ids', full_name='cafm.project.project.BuildingLevel.building_ids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='building_level_rooms', full_name='cafm.project.project.BuildingLevel.building_level_rooms', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_sub_level', full_name='cafm.project.project.BuildingLevel.is_sub_level', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=90,
  serialized_end=246,
)

_BUILDINGLEVEL.fields_by_name['building_level_rooms'].message_type = project_dot_building__level__room__pb2._BUILDINGLEVELROOM
DESCRIPTOR.message_types_by_name['BuildingLevel'] = _BUILDINGLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuildingLevel = _reflection.GeneratedProtocolMessageType('BuildingLevel', (_message.Message,), {
  'DESCRIPTOR' : _BUILDINGLEVEL,
  '__module__' : 'project.building_level_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.project.BuildingLevel)
  })
_sym_db.RegisterMessage(BuildingLevel)


# @@protoc_insertion_point(module_scope)
