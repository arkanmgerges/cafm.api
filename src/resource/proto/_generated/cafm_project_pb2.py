# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cafm_project.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project.lookup.equipment import equipment_lookup_app_service_pb2 as project_dot_lookup_dot_equipment_dot_equipment__lookup__app__service__pb2
from project.lookup.subcontractor import subcontractor_lookup_app_service_pb2 as project_dot_lookup_dot_subcontractor_dot_subcontractor__lookup__app__service__pb2
from project.lookup.user import user_lookup_app_service_pb2 as project_dot_lookup_dot_user_dot_user__lookup__app__service__pb2
from project.lookup.daily_check_procedure import daily_check_procedure_lookup_app_service_pb2 as project_dot_lookup_dot_daily__check__procedure_dot_daily__check__procedure__lookup__app__service__pb2
from project.lookup.project import project_lookup_app_service_pb2 as project_dot_lookup_dot_project_dot_project__lookup__app__service__pb2
from project.lookup.organization import organization_lookup_app_service_pb2 as project_dot_lookup_dot_organization_dot_organization__lookup__app__service__pb2
from project import equipment_app_service_pb2 as project_dot_equipment__app__service__pb2
from project import project_app_service_pb2 as project_dot_project__app__service__pb2
from project import user_app_service_pb2 as project_dot_user__app__service__pb2
from project import subcontractor_app_service_pb2 as project_dot_subcontractor__app__service__pb2
from project import equipment_model_app_service_pb2 as project_dot_equipment__model__app__service__pb2
from project import manufacturer_app_service_pb2 as project_dot_manufacturer__app__service__pb2
from project import equipment_project_category_app_service_pb2 as project_dot_equipment__project__category__app__service__pb2
from project import equipment_category_app_service_pb2 as project_dot_equipment__category__app__service__pb2
from project import equipment_category_group_app_service_pb2 as project_dot_equipment__category__group__app__service__pb2
from project import unit_app_service_pb2 as project_dot_unit__app__service__pb2
from project import equipment_input_app_service_pb2 as project_dot_equipment__input__app__service__pb2
from project import maintenance_procedure_app_service_pb2 as project_dot_maintenance__procedure__app__service__pb2
from project import maintenance_procedure_operation_app_service_pb2 as project_dot_maintenance__procedure__operation__app__service__pb2
from project import maintenance_procedure_operation_parameter_app_service_pb2 as project_dot_maintenance__procedure__operation__parameter__app__service__pb2
from project import daily_check_procedure_app_service_pb2 as project_dot_daily__check__procedure__app__service__pb2
from project import daily_check_procedure_operation_app_service_pb2 as project_dot_daily__check__procedure__operation__app__service__pb2
from project import daily_check_procedure_operation_parameter_app_service_pb2 as project_dot_daily__check__procedure__operation__parameter__app__service__pb2
from project import standard_maintenance_procedure_app_service_pb2 as project_dot_standard__maintenance__procedure__app__service__pb2
from project import standard_maintenance_procedure_operation_app_service_pb2 as project_dot_standard__maintenance__procedure__operation__app__service__pb2
from project import standard_maintenance_procedure_operation_parameter_app_service_pb2 as project_dot_standard__maintenance__procedure__operation__parameter__app__service__pb2
from project import standard_equipment_app_service_pb2 as project_dot_standard__equipment__app__service__pb2
from project import standard_equipment_category_app_service_pb2 as project_dot_standard__equipment__category__app__service__pb2
from project import standard_equipment_category_group_app_service_pb2 as project_dot_standard__equipment__category__group__app__service__pb2
from project import subcontractor_category_app_service_pb2 as project_dot_subcontractor__category__app__service__pb2
from project import organization_app_service_pb2 as project_dot_organization__app__service__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cafm_project.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x63\x61\x66m_project.proto\x1a;project/lookup/equipment/equipment_lookup_app_service.proto\x1a\x43project/lookup/subcontractor/subcontractor_lookup_app_service.proto\x1a\x31project/lookup/user/user_lookup_app_service.proto\x1aSproject/lookup/daily_check_procedure/daily_check_procedure_lookup_app_service.proto\x1a\x37project/lookup/project/project_lookup_app_service.proto\x1a\x41project/lookup/organization/organization_lookup_app_service.proto\x1a#project/equipment_app_service.proto\x1a!project/project_app_service.proto\x1a\x1eproject/user_app_service.proto\x1a\'project/subcontractor_app_service.proto\x1a)project/equipment_model_app_service.proto\x1a&project/manufacturer_app_service.proto\x1a\x34project/equipment_project_category_app_service.proto\x1a,project/equipment_category_app_service.proto\x1a\x32project/equipment_category_group_app_service.proto\x1a\x1eproject/unit_app_service.proto\x1a)project/equipment_input_app_service.proto\x1a/project/maintenance_procedure_app_service.proto\x1a\x39project/maintenance_procedure_operation_app_service.proto\x1a\x43project/maintenance_procedure_operation_parameter_app_service.proto\x1a/project/daily_check_procedure_app_service.proto\x1a\x39project/daily_check_procedure_operation_app_service.proto\x1a\x43project/daily_check_procedure_operation_parameter_app_service.proto\x1a\x38project/standard_maintenance_procedure_app_service.proto\x1a\x42project/standard_maintenance_procedure_operation_app_service.proto\x1aLproject/standard_maintenance_procedure_operation_parameter_app_service.proto\x1a,project/standard_equipment_app_service.proto\x1a\x35project/standard_equipment_category_app_service.proto\x1a;project/standard_equipment_category_group_app_service.proto\x1a\x30project/subcontractor_category_app_service.proto\x1a&project/organization_app_service.protob\x06proto3'
  ,
  dependencies=[project_dot_lookup_dot_equipment_dot_equipment__lookup__app__service__pb2.DESCRIPTOR,project_dot_lookup_dot_subcontractor_dot_subcontractor__lookup__app__service__pb2.DESCRIPTOR,project_dot_lookup_dot_user_dot_user__lookup__app__service__pb2.DESCRIPTOR,project_dot_lookup_dot_daily__check__procedure_dot_daily__check__procedure__lookup__app__service__pb2.DESCRIPTOR,project_dot_lookup_dot_project_dot_project__lookup__app__service__pb2.DESCRIPTOR,project_dot_lookup_dot_organization_dot_organization__lookup__app__service__pb2.DESCRIPTOR,project_dot_equipment__app__service__pb2.DESCRIPTOR,project_dot_project__app__service__pb2.DESCRIPTOR,project_dot_user__app__service__pb2.DESCRIPTOR,project_dot_subcontractor__app__service__pb2.DESCRIPTOR,project_dot_equipment__model__app__service__pb2.DESCRIPTOR,project_dot_manufacturer__app__service__pb2.DESCRIPTOR,project_dot_equipment__project__category__app__service__pb2.DESCRIPTOR,project_dot_equipment__category__app__service__pb2.DESCRIPTOR,project_dot_equipment__category__group__app__service__pb2.DESCRIPTOR,project_dot_unit__app__service__pb2.DESCRIPTOR,project_dot_equipment__input__app__service__pb2.DESCRIPTOR,project_dot_maintenance__procedure__app__service__pb2.DESCRIPTOR,project_dot_maintenance__procedure__operation__app__service__pb2.DESCRIPTOR,project_dot_maintenance__procedure__operation__parameter__app__service__pb2.DESCRIPTOR,project_dot_daily__check__procedure__app__service__pb2.DESCRIPTOR,project_dot_daily__check__procedure__operation__app__service__pb2.DESCRIPTOR,project_dot_daily__check__procedure__operation__parameter__app__service__pb2.DESCRIPTOR,project_dot_standard__maintenance__procedure__app__service__pb2.DESCRIPTOR,project_dot_standard__maintenance__procedure__operation__app__service__pb2.DESCRIPTOR,project_dot_standard__maintenance__procedure__operation__parameter__app__service__pb2.DESCRIPTOR,project_dot_standard__equipment__app__service__pb2.DESCRIPTOR,project_dot_standard__equipment__category__app__service__pb2.DESCRIPTOR,project_dot_standard__equipment__category__group__app__service__pb2.DESCRIPTOR,project_dot_subcontractor__category__app__service__pb2.DESCRIPTOR,project_dot_organization__app__service__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
