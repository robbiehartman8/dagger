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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eidentity.proto\"R\n\x08readData\x12\x12\n\x05hr_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0bidentity_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_hr_idB\x0e\n\x0c_identity_id\"\\\n\tgetUserId\x12\x13\n\x0bidentity_id\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x13\n\x0bmiddle_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\"F\n\x06userId\x12\x13\n\x0bidentity_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x16\n\x0estatus_message\x18\x03 \x01(\t\"\x8b\x06\n\x06hrData\x12\r\n\x05hr_id\x18\x01 \x01(\t\x12\x18\n\x10legal_first_name\x18\x02 \x01(\t\x12\x19\n\x11legal_middle_name\x18\x03 \x01(\t\x12\x17\n\x0flegal_last_name\x18\x04 \x01(\t\x12\x1c\n\x14preferred_first_name\x18\x05 \x01(\t\x12\x1d\n\x15preferred_middle_name\x18\x06 \x01(\t\x12\x1b\n\x13preferred_last_name\x18\x07 \x01(\t\x12\x16\n\x0ejob_title_code\x18\x08 \x01(\t\x12\x1d\n\x15job_title_description\x18\t \x01(\t\x12\x17\n\x0fjob_title_level\x18\n \x01(\t\x12\x15\n\rlocation_code\x18\x0b \x01(\t\x12\x15\n\rlocation_name\x18\x0c \x01(\t\x12\x18\n\x10location_address\x18\r \x01(\t\x12\x19\n\x11phone_number_work\x18\x0e \x01(\t\x12 \n\x18phone_number_work_mobile\x18\x0f \x01(\t\x12\x19\n\x11phone_number_home\x18\x10 \x01(\t\x12 \n\x18phone_number_home_mobile\x18\x11 \x01(\t\x12\x1a\n\x12\x65mail_work_primary\x18\x12 \x01(\t\x12\x1a\n\x12\x65mail_home_primary\x18\x13 \x01(\t\x12\x0e\n\x06status\x18\x14 \x01(\t\x12\x17\n\x0fhire_start_date\x18\x15 \x01(\t\x12\x18\n\x10termination_date\x18\x16 \x01(\t\x12#\n\x1bleave_of_absense_start_date\x18\x17 \x01(\t\x12!\n\x19leave_of_absense_end_date\x18\x18 \x01(\t\x12\x15\n\remployee_type\x18\x19 \x01(\t\x12\x13\n\x0b\x63ost_center\x18\x1a \x01(\t\x12\x19\n\x11\x64\x65partment_number\x18\x1b \x01(\t\x12\x17\n\x0f\x64\x65partment_name\x18\x1c \x01(\t\x12\x15\n\rmanager_hr_id\x18\x1d \x01(\t\"\\\n\rhrDataMessage\x12\x13\n\x0bidentity_id\x18\x01 \x01(\t\x12\r\n\x05hr_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x16\n\x0estatus_message\x18\x04 \x01(\t\"\x9c\x07\n\x0cidentityData\x12\x13\n\x0bidentity_id\x18\x01 \x01(\t\x12\x11\n\tcreate_ts\x18\x02 \x01(\t\x12\r\n\x05hr_id\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x18\n\x10legal_first_name\x18\x05 \x01(\t\x12\x19\n\x11legal_middle_name\x18\x06 \x01(\t\x12\x17\n\x0flegal_last_name\x18\x07 \x01(\t\x12\x1c\n\x14preferred_first_name\x18\x08 \x01(\t\x12\x1d\n\x15preferred_middle_name\x18\t \x01(\t\x12\x1b\n\x13preferred_last_name\x18\n \x01(\t\x12\x1a\n\x12use_preferred_name\x18\x0b \x01(\t\x12\x16\n\x0ejob_title_code\x18\x0c \x01(\t\x12\x1d\n\x15job_title_description\x18\r \x01(\t\x12\x17\n\x0fjob_title_level\x18\x0e \x01(\t\x12\x15\n\rlocation_code\x18\x0f \x01(\t\x12\x15\n\rlocation_name\x18\x10 \x01(\t\x12\x18\n\x10location_address\x18\x11 \x01(\t\x12\x19\n\x11phone_number_work\x18\x12 \x01(\t\x12 \n\x18phone_number_work_mobile\x18\x13 \x01(\t\x12\x19\n\x11phone_number_home\x18\x14 \x01(\t\x12 \n\x18phone_number_home_mobile\x18\x15 \x01(\t\x12\x1a\n\x12\x65mail_work_primary\x18\x16 \x01(\t\x12\x1a\n\x12\x65mail_home_primary\x18\x17 \x01(\t\x12\x0e\n\x06status\x18\x18 \x01(\t\x12\x17\n\x0fhire_start_date\x18\x19 \x01(\t\x12\x18\n\x10termination_date\x18\x1a \x01(\t\x12#\n\x1bleave_of_absense_start_date\x18\x1b \x01(\t\x12!\n\x19leave_of_absense_end_date\x18\x1c \x01(\t\x12\x15\n\remployee_type\x18\x1d \x01(\t\x12\x13\n\x0b\x63ost_center\x18\x1e \x01(\t\x12\x19\n\x11\x64\x65partment_number\x18\x1f \x01(\t\x12\x17\n\x0f\x64\x65partment_name\x18  \x01(\t\x12\x1b\n\x13manager_identity_id\x18! \x01(\t\x12\x15\n\rmanager_hr_id\x18\" \x01(\t\x12\x17\n\x0fmanager_user_id\x18# \x01(\t\"T\n\ndeleteData\x12\x12\n\x05hr_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0bidentity_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_hr_idB\x0e\n\x0c_identity_id\"\'\n\rdeleteMessage\x12\x16\n\x0estatus_message\x18\x01 \x01(\t2\xc1\x01\n\x08Identity\x12\x31\n\x14\x63reateUpdateIdentity\x12\x07.hrData\x1a\x0e.hrDataMessage\"\x00\x12*\n\x0creadIdentity\x12\t.readData\x1a\r.identityData\"\x00\x12/\n\x0e\x64\x65leteIdentity\x12\x0b.deleteData\x1a\x0e.deleteMessage\"\x00\x12%\n\x0c\x61ppearUserId\x12\n.getUserId\x1a\x07.userId\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'identity_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _READDATA._serialized_start=18
  _READDATA._serialized_end=100
  _GETUSERID._serialized_start=102
  _GETUSERID._serialized_end=194
  _USERID._serialized_start=196
  _USERID._serialized_end=266
  _HRDATA._serialized_start=269
  _HRDATA._serialized_end=1048
  _HRDATAMESSAGE._serialized_start=1050
  _HRDATAMESSAGE._serialized_end=1142
  _IDENTITYDATA._serialized_start=1145
  _IDENTITYDATA._serialized_end=2069
  _DELETEDATA._serialized_start=2071
  _DELETEDATA._serialized_end=2155
  _DELETEMESSAGE._serialized_start=2157
  _DELETEMESSAGE._serialized_end=2196
  _IDENTITY._serialized_start=2199
  _IDENTITY._serialized_end=2392
# @@protoc_insertion_point(module_scope)
