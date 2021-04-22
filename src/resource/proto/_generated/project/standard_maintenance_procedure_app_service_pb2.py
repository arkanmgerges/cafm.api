# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/standard_maintenance_procedure_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import (
    standard_maintenance_procedure_pb2 as project_dot_standard__maintenance__procedure__pb2,
)
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="project/standard_maintenance_procedure_app_service.proto",
    package="cafm.project.standard_maintenance_procedure",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n8project/standard_maintenance_procedure_app_service.proto\x12+cafm.project.standard_maintenance_procedure\x1a,project/standard_maintenance_procedure.proto\x1a\x0border.proto"\\\nNStandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t"\xc2\x01\nOStandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse\x12o\n\x1cstandardMaintenanceProcedure\x18\x01 \x01(\x0b\x32I.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure"\x9e\x01\nKStandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order"\xd3\x01\nLStandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse\x12p\n\x1dstandardMaintenanceProcedures\x18\x01 \x03(\x0b\x32I.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure\x12\x11\n\titemCount\x18\x02 \x01(\x05"5\n3StandardMaintenanceProcedureAppService_newIdRequest"B\n4StandardMaintenanceProcedureAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xb4\x06\n&StandardMaintenanceProcedureAppService\x12\x9f\x02\n standardMaintenanceProcedureById\x12{.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest\x1a|.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse"\x00\x12\x96\x02\n\x1dstandardMaintenanceProcedures\x12x.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest\x1ay.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse"\x00\x12\xce\x01\n\x05newId\x12`.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdRequest\x1a\x61.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdResponse"\x00\x62\x06proto3',
    dependencies=[
        project_dot_standard__maintenance__procedure__pb2.DESCRIPTOR,
        order__pb2.DESCRIPTOR,
    ],
)


_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDREQUEST = _descriptor.Descriptor(
    name="StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest",
    full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=164,
    serialized_end=256,
)


_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDRESPONSE = _descriptor.Descriptor(
    name="StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse",
    full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="standardMaintenanceProcedure",
            full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse.standardMaintenanceProcedure",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=259,
    serialized_end=453,
)


_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESREQUEST = _descriptor.Descriptor(
    name="StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest",
    full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="resultFrom",
            full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest.resultFrom",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="resultSize",
            full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest.resultSize",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="order",
            full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest.order",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=456,
    serialized_end=614,
)


_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESRESPONSE = _descriptor.Descriptor(
    name="StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse",
    full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="standardMaintenanceProcedures",
            full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse.standardMaintenanceProcedures",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="itemCount",
            full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse.itemCount",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=617,
    serialized_end=828,
)


_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
    name="StandardMaintenanceProcedureAppService_newIdRequest",
    full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=830,
    serialized_end=883,
)


_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
    name="StandardMaintenanceProcedureAppService_newIdResponse",
    full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdResponse.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=885,
    serialized_end=951,
)

_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDRESPONSE.fields_by_name[
    "standardMaintenanceProcedure"
].message_type = (
    project_dot_standard__maintenance__procedure__pb2._STANDARDMAINTENANCEPROCEDURE
)
_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESREQUEST.fields_by_name[
    "order"
].message_type = order__pb2._ORDER
_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESRESPONSE.fields_by_name[
    "standardMaintenanceProcedures"
].message_type = (
    project_dot_standard__maintenance__procedure__pb2._STANDARDMAINTENANCEPROCEDURE
)
DESCRIPTOR.message_types_by_name[
    "StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest"
] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDREQUEST
DESCRIPTOR.message_types_by_name[
    "StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse"
] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDRESPONSE
DESCRIPTOR.message_types_by_name[
    "StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest"
] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESREQUEST
DESCRIPTOR.message_types_by_name[
    "StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse"
] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESRESPONSE
DESCRIPTOR.message_types_by_name[
    "StandardMaintenanceProcedureAppService_newIdRequest"
] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name[
    "StandardMaintenanceProcedureAppService_newIdResponse"
] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest = _reflection.GeneratedProtocolMessageType(
    "StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDREQUEST,
        "__module__": "project.standard_maintenance_procedure_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest)
    },
)
_sym_db.RegisterMessage(
    StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest
)

StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse = _reflection.GeneratedProtocolMessageType(
    "StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDRESPONSE,
        "__module__": "project.standard_maintenance_procedure_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse)
    },
)
_sym_db.RegisterMessage(
    StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse
)

StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest = _reflection.GeneratedProtocolMessageType(
    "StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESREQUEST,
        "__module__": "project.standard_maintenance_procedure_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest)
    },
)
_sym_db.RegisterMessage(
    StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest
)

StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse = _reflection.GeneratedProtocolMessageType(
    "StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESRESPONSE,
        "__module__": "project.standard_maintenance_procedure_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse)
    },
)
_sym_db.RegisterMessage(
    StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse
)

StandardMaintenanceProcedureAppService_newIdRequest = _reflection.GeneratedProtocolMessageType(
    "StandardMaintenanceProcedureAppService_newIdRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDREQUEST,
        "__module__": "project.standard_maintenance_procedure_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdRequest)
    },
)
_sym_db.RegisterMessage(StandardMaintenanceProcedureAppService_newIdRequest)

StandardMaintenanceProcedureAppService_newIdResponse = _reflection.GeneratedProtocolMessageType(
    "StandardMaintenanceProcedureAppService_newIdResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDRESPONSE,
        "__module__": "project.standard_maintenance_procedure_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdResponse)
    },
)
_sym_db.RegisterMessage(StandardMaintenanceProcedureAppService_newIdResponse)


_STANDARDMAINTENANCEPROCEDUREAPPSERVICE = _descriptor.ServiceDescriptor(
    name="StandardMaintenanceProcedureAppService",
    full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=954,
    serialized_end=1774,
    methods=[
        _descriptor.MethodDescriptor(
            name="standardMaintenanceProcedureById",
            full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService.standardMaintenanceProcedureById",
            index=0,
            containing_service=None,
            input_type=_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDREQUEST,
            output_type=_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="standardMaintenanceProcedures",
            full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService.standardMaintenanceProcedures",
            index=1,
            containing_service=None,
            input_type=_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESREQUEST,
            output_type=_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="newId",
            full_name="cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService.newId",
            index=2,
            containing_service=None,
            input_type=_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDREQUEST,
            output_type=_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_STANDARDMAINTENANCEPROCEDUREAPPSERVICE)

DESCRIPTOR.services_by_name[
    "StandardMaintenanceProcedureAppService"
] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE

# @@protoc_insertion_point(module_scope)
