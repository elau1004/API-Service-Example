# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf_grpc.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13protobuf_grpc.proto\"P\n\x04Name\x12\x0b\n\x03use\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\r\n\x05given\x18\x03 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x04 \x01(\t\x12\x0e\n\x06\x61\x63tive\x18\x05 \x01(\t\"S\n\x07Telecom\x12\x0e\n\x06system\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0b\n\x03use\x18\x03 \x01(\t\x12\x0c\n\x04rank\x18\x04 \x01(\x05\x12\x0e\n\x06\x61\x63tive\x18\x05 \x01(\t\"\xd4\x01\n\x07\x41\x64\x64ress\x12\x0b\n\x03use\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x0c\n\x04line\x18\x04 \x01(\t\x12\x0c\n\x04\x63ity\x18\x05 \x01(\t\x12\r\n\x05state\x18\x06 \x01(\t\x12\x0f\n\x07zipcode\x18\x07 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x08 \x01(\t\x12$\n\x06period\x18\t \x03(\x0b\x32\x14.Address.PeriodEntry\x1a-\n\x0bPeriodEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"f\n\x07\x43ontact\x12\x10\n\x08relation\x18\x01 \x01(\t\x12\x13\n\x04name\x18\x02 \x01(\x0b\x32\x05.Name\x12\x19\n\x07telecom\x18\x03 \x01(\x0b\x32\x08.Telecom\x12\x19\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x08.Address\"\xe1\x01\n\x07Patient\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06\x61\x63tive\x18\x02 \x01(\x08\x12\x14\n\x05names\x18\x03 \x03(\x0b\x32\x05.Name\x12\x1a\n\x08telecoms\x18\x04 \x03(\x0b\x32\x08.Telecom\x12\x0e\n\x06gender\x18\x05 \x01(\t\x12\x12\n\nbirth_date\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65\x63\x65\x61sed_on\x18\x07 \x01(\t\x12\x1b\n\taddresses\x18\x08 \x03(\x0b\x32\x08.Address\x12\x16\n\x0emarital_status\x18\t \x01(\t\x12\x1a\n\x08\x63ontacts\x18\n \x03(\x0b\x32\x08.Contact\"*\n\x08Patients\x12\x1e\n\x0c\x61ll_patients\x18\x01 \x03(\x0b\x32\x08.Patient')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf_grpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ADDRESS_PERIODENTRY']._options = None
  _globals['_ADDRESS_PERIODENTRY']._serialized_options = b'8\001'
  _globals['_NAME']._serialized_start=23
  _globals['_NAME']._serialized_end=103
  _globals['_TELECOM']._serialized_start=105
  _globals['_TELECOM']._serialized_end=188
  _globals['_ADDRESS']._serialized_start=191
  _globals['_ADDRESS']._serialized_end=403
  _globals['_ADDRESS_PERIODENTRY']._serialized_start=358
  _globals['_ADDRESS_PERIODENTRY']._serialized_end=403
  _globals['_CONTACT']._serialized_start=405
  _globals['_CONTACT']._serialized_end=507
  _globals['_PATIENT']._serialized_start=510
  _globals['_PATIENT']._serialized_end=735
  _globals['_PATIENTS']._serialized_start=737
  _globals['_PATIENTS']._serialized_end=779
# @@protoc_insertion_point(module_scope)