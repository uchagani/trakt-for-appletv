# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DeviceInfoMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import ProtocolMessage_pb2 as ProtocolMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DeviceInfoMessage.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x17\x44\x65viceInfoMessage.proto\x1a\x15ProtocolMessage.proto\"\xd3\x01\n\x11\x44\x65viceInfoMessage\x12\x18\n\x10uniqueIdentifier\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x1a\n\x12localizedModelName\x18\x03 \x01(\t\x12\x1a\n\x12systemBuildVersion\x18\x04 \x02(\t\x12#\n\x1b\x61pplicationBundleIdentifier\x18\x05 \x02(\t\x12 \n\x18\x61pplicationBundleVersion\x18\x06 \x01(\t\x12\x17\n\x0fprotocolVersion\x18\x07 \x02(\x05:?\n\x11\x64\x65viceInfoMessage\x12\x10.ProtocolMessage\x18\x14 \x01(\x0b\x32\x12.DeviceInfoMessage')
  ,
  dependencies=[ProtocolMessage__pb2.DESCRIPTOR,])


DEVICEINFOMESSAGE_FIELD_NUMBER = 20
deviceInfoMessage = _descriptor.FieldDescriptor(
  name='deviceInfoMessage', full_name='deviceInfoMessage', index=0,
  number=20, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_DEVICEINFOMESSAGE = _descriptor.Descriptor(
  name='DeviceInfoMessage',
  full_name='DeviceInfoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uniqueIdentifier', full_name='DeviceInfoMessage.uniqueIdentifier', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='DeviceInfoMessage.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='localizedModelName', full_name='DeviceInfoMessage.localizedModelName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='systemBuildVersion', full_name='DeviceInfoMessage.systemBuildVersion', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applicationBundleIdentifier', full_name='DeviceInfoMessage.applicationBundleIdentifier', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applicationBundleVersion', full_name='DeviceInfoMessage.applicationBundleVersion', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocolVersion', full_name='DeviceInfoMessage.protocolVersion', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=262,
)

DESCRIPTOR.message_types_by_name['DeviceInfoMessage'] = _DEVICEINFOMESSAGE
DESCRIPTOR.extensions_by_name['deviceInfoMessage'] = deviceInfoMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceInfoMessage = _reflection.GeneratedProtocolMessageType('DeviceInfoMessage', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEINFOMESSAGE,
  __module__ = 'DeviceInfoMessage_pb2'
  # @@protoc_insertion_point(class_scope:DeviceInfoMessage)
  ))
_sym_db.RegisterMessage(DeviceInfoMessage)

deviceInfoMessage.message_type = _DEVICEINFOMESSAGE
ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(deviceInfoMessage)

# @@protoc_insertion_point(module_scope)
