# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: otus.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'otus.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\notus.proto\"K\n\x04User\x12\x10\n\x08lastname\x18\x01 \x01(\t\x12\x11\n\tfirstname\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\x11\n\tisMarried\x18\x04 \x01(\x08\"\x10\n\x02Id\x12\n\n\x02Id\x18\x01 \x01(\x03\x32X\n\x0bUserActions\x12\x1a\n\x0cRegisterUser\x12\x05.User\x1a\x03.Id\x12\x15\n\x07GetUser\x12\x03.Id\x1a\x05.User\x12\x16\n\nDeleteUser\x12\x03.Id\x1a\x03.Idb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'otus_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USER']._serialized_start=14
  _globals['_USER']._serialized_end=89
  _globals['_ID']._serialized_start=91
  _globals['_ID']._serialized_end=107
  _globals['_USERACTIONS']._serialized_start=109
  _globals['_USERACTIONS']._serialized_end=197
# @@protoc_insertion_point(module_scope)
