# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/daily_check_procedure_operation_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import (
    daily_check_procedure_operation_pb2 as project_dot_daily__check__procedure__operation__pb2,
)
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="project/daily_check_procedure_operation_app_service.proto",
    package="cafm.project.daily_check_procedure_operation",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n9project/daily_check_procedure_operation_app_service.proto\x12,cafm.project.daily_check_procedure_operation\x1a-project/daily_check_procedure_operation.proto\x1a\x0border.proto"\\\nNDailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t"\xc3\x01\nODailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse\x12p\n\x1c\x64\x61ilyCheckProcedureOperation\x18\x01 \x01(\x0b\x32J.cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperation"\x9e\x01\nKDailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order"\xd4\x01\nLDailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse\x12q\n\x1d\x64\x61ilyCheckProcedureOperations\x18\x01 \x03(\x0b\x32J.cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperation\x12\x11\n\titemCount\x18\x02 \x01(\x05"\xd4\x01\nbDailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest\x12\x1d\n\x15\x64\x61ilyCheckProcedureId\x18\x01 \x01(\t\x12\x12\n\nresultFrom\x18\x02 \x01(\x05\x12\x12\n\nresultSize\x18\x03 \x01(\x05\x12\'\n\x05order\x18\x04 \x03(\x0b\x32\x18.cafm.common.order.Order"\xeb\x01\ncDailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse\x12q\n\x1d\x64\x61ilyCheckProcedureOperations\x18\x01 \x03(\x0b\x32J.cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperation\x12\x11\n\titemCount\x18\x02 \x01(\x05"5\n3DailyCheckProcedureOperationAppService_newIdRequest"B\n4DailyCheckProcedureOperationAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\x9c\t\n&DailyCheckProcedureOperationAppService\x12\xa1\x02\n dailyCheckProcedureOperationById\x12|.cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdRequest\x1a}.cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse"\x00\x12\x98\x02\n\x1d\x64\x61ilyCheckProcedureOperations\x12y.cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest\x1az.cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse"\x00\x12\xdf\x02\n4dailyCheckProcedureOperationsByDailyCheckProcedureId\x12\x90\x01.cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest\x1a\x91\x01.cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse"\x00\x12\xd0\x01\n\x05newId\x12\x61.cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_newIdRequest\x1a\x62.cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_newIdResponse"\x00\x62\x06proto3',
    dependencies=[
        project_dot_daily__check__procedure__operation__pb2.DESCRIPTOR,
        order__pb2.DESCRIPTOR,
    ],
)


_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONBYIDREQUEST = _descriptor.Descriptor(
    name="DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdRequest",
    full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdRequest.id",
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
    serialized_start=167,
    serialized_end=259,
)


_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONBYIDRESPONSE = _descriptor.Descriptor(
    name="DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse",
    full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="dailyCheckProcedureOperation",
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse.dailyCheckProcedureOperation",
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
    serialized_start=262,
    serialized_end=457,
)


_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSREQUEST = _descriptor.Descriptor(
    name="DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest",
    full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="resultFrom",
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest.resultFrom",
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
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest.resultSize",
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
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest.order",
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
    serialized_start=460,
    serialized_end=618,
)


_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSRESPONSE = _descriptor.Descriptor(
    name="DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse",
    full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="dailyCheckProcedureOperations",
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse.dailyCheckProcedureOperations",
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
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse.itemCount",
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
    serialized_start=621,
    serialized_end=833,
)


_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSBYDAILYCHECKPROCEDUREIDREQUEST = _descriptor.Descriptor(
    name="DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest",
    full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="dailyCheckProcedureId",
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest.dailyCheckProcedureId",
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
        _descriptor.FieldDescriptor(
            name="resultFrom",
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest.resultFrom",
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
            name="resultSize",
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest.resultSize",
            index=2,
            number=3,
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
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest.order",
            index=3,
            number=4,
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
    serialized_start=836,
    serialized_end=1048,
)


_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSBYDAILYCHECKPROCEDUREIDRESPONSE = _descriptor.Descriptor(
    name="DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse",
    full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="dailyCheckProcedureOperations",
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse.dailyCheckProcedureOperations",
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
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse.itemCount",
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
    serialized_start=1051,
    serialized_end=1286,
)


_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
    name="DailyCheckProcedureOperationAppService_newIdRequest",
    full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_newIdRequest",
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
    serialized_start=1288,
    serialized_end=1341,
)


_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
    name="DailyCheckProcedureOperationAppService_newIdResponse",
    full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_newIdResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_newIdResponse.id",
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
    serialized_start=1343,
    serialized_end=1409,
)

_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONBYIDRESPONSE.fields_by_name[
    "dailyCheckProcedureOperation"
].message_type = (
    project_dot_daily__check__procedure__operation__pb2._DAILYCHECKPROCEDUREOPERATION
)
_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSREQUEST.fields_by_name[
    "order"
].message_type = order__pb2._ORDER
_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSRESPONSE.fields_by_name[
    "dailyCheckProcedureOperations"
].message_type = (
    project_dot_daily__check__procedure__operation__pb2._DAILYCHECKPROCEDUREOPERATION
)
_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSBYDAILYCHECKPROCEDUREIDREQUEST.fields_by_name[
    "order"
].message_type = order__pb2._ORDER
_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSBYDAILYCHECKPROCEDUREIDRESPONSE.fields_by_name[
    "dailyCheckProcedureOperations"
].message_type = (
    project_dot_daily__check__procedure__operation__pb2._DAILYCHECKPROCEDUREOPERATION
)
DESCRIPTOR.message_types_by_name[
    "DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdRequest"
] = _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONBYIDREQUEST
DESCRIPTOR.message_types_by_name[
    "DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse"
] = _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONBYIDRESPONSE
DESCRIPTOR.message_types_by_name[
    "DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest"
] = _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name[
    "DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse"
] = _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSRESPONSE
DESCRIPTOR.message_types_by_name[
    "DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest"
] = _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSBYDAILYCHECKPROCEDUREIDREQUEST
DESCRIPTOR.message_types_by_name[
    "DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse"
] = _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSBYDAILYCHECKPROCEDUREIDRESPONSE
DESCRIPTOR.message_types_by_name[
    "DailyCheckProcedureOperationAppService_newIdRequest"
] = _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name[
    "DailyCheckProcedureOperationAppService_newIdResponse"
] = _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdRequest = _reflection.GeneratedProtocolMessageType(
    "DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONBYIDREQUEST,
        "__module__": "project.daily_check_procedure_operation_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdRequest)
    },
)
_sym_db.RegisterMessage(
    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdRequest
)

DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse = _reflection.GeneratedProtocolMessageType(
    "DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONBYIDRESPONSE,
        "__module__": "project.daily_check_procedure_operation_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse)
    },
)
_sym_db.RegisterMessage(
    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse
)

DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest = _reflection.GeneratedProtocolMessageType(
    "DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSREQUEST,
        "__module__": "project.daily_check_procedure_operation_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest)
    },
)
_sym_db.RegisterMessage(
    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest
)

DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse = _reflection.GeneratedProtocolMessageType(
    "DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSRESPONSE,
        "__module__": "project.daily_check_procedure_operation_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse)
    },
)
_sym_db.RegisterMessage(
    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse
)

DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest = _reflection.GeneratedProtocolMessageType(
    "DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSBYDAILYCHECKPROCEDUREIDREQUEST,
        "__module__": "project.daily_check_procedure_operation_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest)
    },
)
_sym_db.RegisterMessage(
    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest
)

DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse = _reflection.GeneratedProtocolMessageType(
    "DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSBYDAILYCHECKPROCEDUREIDRESPONSE,
        "__module__": "project.daily_check_procedure_operation_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse)
    },
)
_sym_db.RegisterMessage(
    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse
)

DailyCheckProcedureOperationAppService_newIdRequest = _reflection.GeneratedProtocolMessageType(
    "DailyCheckProcedureOperationAppService_newIdRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_NEWIDREQUEST,
        "__module__": "project.daily_check_procedure_operation_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_newIdRequest)
    },
)
_sym_db.RegisterMessage(DailyCheckProcedureOperationAppService_newIdRequest)

DailyCheckProcedureOperationAppService_newIdResponse = _reflection.GeneratedProtocolMessageType(
    "DailyCheckProcedureOperationAppService_newIdResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_NEWIDRESPONSE,
        "__module__": "project.daily_check_procedure_operation_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService_newIdResponse)
    },
)
_sym_db.RegisterMessage(DailyCheckProcedureOperationAppService_newIdResponse)


_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE = _descriptor.ServiceDescriptor(
    name="DailyCheckProcedureOperationAppService",
    full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=1412,
    serialized_end=2592,
    methods=[
        _descriptor.MethodDescriptor(
            name="dailyCheckProcedureOperationById",
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService.dailyCheckProcedureOperationById",
            index=0,
            containing_service=None,
            input_type=_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONBYIDREQUEST,
            output_type=_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONBYIDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="dailyCheckProcedureOperations",
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService.dailyCheckProcedureOperations",
            index=1,
            containing_service=None,
            input_type=_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSREQUEST,
            output_type=_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="dailyCheckProcedureOperationsByDailyCheckProcedureId",
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService.dailyCheckProcedureOperationsByDailyCheckProcedureId",
            index=2,
            containing_service=None,
            input_type=_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSBYDAILYCHECKPROCEDUREIDREQUEST,
            output_type=_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONSBYDAILYCHECKPROCEDUREIDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="newId",
            full_name="cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperationAppService.newId",
            index=3,
            containing_service=None,
            input_type=_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_NEWIDREQUEST,
            output_type=_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE_NEWIDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_DAILYCHECKPROCEDUREOPERATIONAPPSERVICE)

DESCRIPTOR.services_by_name[
    "DailyCheckProcedureOperationAppService"
] = _DAILYCHECKPROCEDUREOPERATIONAPPSERVICE

# @@protoc_insertion_point(module_scope)
