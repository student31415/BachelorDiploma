# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: product_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15product_service.proto\"%\n\tProductId\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x0c\n\x04GUID\x18\x02 \x01(\t\"4\n\x07Product\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\r\n\x05Price\x18\x02 \x01(\x02\x12\x0c\n\x04GUID\x18\x03 \x01(\t26\n\x0eProductService\x12$\n\nGetProduct\x12\n.ProductId\x1a\x08.Product\"\x00\x62\x06proto3')



_PRODUCTID = DESCRIPTOR.message_types_by_name['ProductId']
_PRODUCT = DESCRIPTOR.message_types_by_name['Product']
ProductId = _reflection.GeneratedProtocolMessageType('ProductId', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTID,
  '__module__' : 'product_service_pb2'
  # @@protoc_insertion_point(class_scope:ProductId)
  })
_sym_db.RegisterMessage(ProductId)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'product_service_pb2'
  # @@protoc_insertion_point(class_scope:Product)
  })
_sym_db.RegisterMessage(Product)

_PRODUCTSERVICE = DESCRIPTOR.services_by_name['ProductService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRODUCTID._serialized_start=25
  _PRODUCTID._serialized_end=62
  _PRODUCT._serialized_start=64
  _PRODUCT._serialized_end=116
  _PRODUCTSERVICE._serialized_start=118
  _PRODUCTSERVICE._serialized_end=172
# @@protoc_insertion_point(module_scope)
