# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: report_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14report_service.proto\"$\n\x08ReportId\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x0c\n\x04GUID\x18\x02 \x01(\t\"p\n\x06Report\x12\x11\n\tOrderName\x18\x01 \x01(\t\x12\x0f\n\x07OrderId\x18\x02 \x01(\x05\x12\x10\n\x08UserName\x18\x03 \x01(\t\x12\x13\n\x0bProductName\x18\x04 \x01(\t\x12\r\n\x05\x43ount\x18\x05 \x01(\x05\x12\x0c\n\x04GUID\x18\x06 \x01(\t22\n\rReportService\x12!\n\tGetReport\x12\t.ReportId\x1a\x07.Report\"\x00\x62\x06proto3')



_REPORTID = DESCRIPTOR.message_types_by_name['ReportId']
_REPORT = DESCRIPTOR.message_types_by_name['Report']
ReportId = _reflection.GeneratedProtocolMessageType('ReportId', (_message.Message,), {
  'DESCRIPTOR' : _REPORTID,
  '__module__' : 'report_service_pb2'
  # @@protoc_insertion_point(class_scope:ReportId)
  })
_sym_db.RegisterMessage(ReportId)

Report = _reflection.GeneratedProtocolMessageType('Report', (_message.Message,), {
  'DESCRIPTOR' : _REPORT,
  '__module__' : 'report_service_pb2'
  # @@protoc_insertion_point(class_scope:Report)
  })
_sym_db.RegisterMessage(Report)

_REPORTSERVICE = DESCRIPTOR.services_by_name['ReportService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REPORTID._serialized_start=24
  _REPORTID._serialized_end=60
  _REPORT._serialized_start=62
  _REPORT._serialized_end=174
  _REPORTSERVICE._serialized_start=176
  _REPORTSERVICE._serialized_end=226
# @@protoc_insertion_point(module_scope)
