# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: identity.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eidentity.proto\"\x17\n\x06hrData\x12\r\n\x05hr_id\x18\x01 \x01(\t\"+\n\x07iamData\x12\r\n\x05hr_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t2T\n\x08Identity\x12\"\n\x0bgetIdentity\x12\x07.hrData\x1a\x08.iamData\"\x00\x12$\n\renterIdentity\x12\x07.hrData\x1a\x08.iamData\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'identity_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HRDATA._serialized_start=18
  _HRDATA._serialized_end=41
  _IAMDATA._serialized_start=43
  _IAMDATA._serialized_end=86
  _IDENTITY._serialized_start=88
  _IDENTITY._serialized_end=172
# @@protoc_insertion_point(module_scope)
