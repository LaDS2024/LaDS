# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/proto/pad_msg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from gym_apollo.envs.modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/planning/proto/pad_msg.proto',
  package='apollo.planning',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n$modules/planning/proto/pad_msg.proto\x12\x0f\x61pollo.planning\x1a!modules/common/proto/header.proto\"c\n\nPadMessage\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12.\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x1e.apollo.planning.DrivingAction*t\n\rDrivingAction\x12\x08\n\x04NONE\x10\x64\x12\n\n\x06\x46OLLOW\x10\x00\x12\x0f\n\x0b\x43HANGE_LEFT\x10\x01\x12\x10\n\x0c\x43HANGE_RIGHT\x10\x02\x12\r\n\tPULL_OVER\x10\x03\x12\x08\n\x04STOP\x10\x04\x12\x11\n\rRESUME_CRUISE\x10\x05')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,])

_DRIVINGACTION = _descriptor.EnumDescriptor(
  name='DrivingAction',
  full_name='apollo.planning.DrivingAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOLLOW', index=1, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_LEFT', index=2, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_RIGHT', index=3, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PULL_OVER', index=4, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=5, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESUME_CRUISE', index=6, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=193,
  serialized_end=309,
)
_sym_db.RegisterEnumDescriptor(_DRIVINGACTION)

DrivingAction = enum_type_wrapper.EnumTypeWrapper(_DRIVINGACTION)
NONE = 100
FOLLOW = 0
CHANGE_LEFT = 1
CHANGE_RIGHT = 2
PULL_OVER = 3
STOP = 4
RESUME_CRUISE = 5



_PADMESSAGE = _descriptor.Descriptor(
  name='PadMessage',
  full_name='apollo.planning.PadMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.planning.PadMessage.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='apollo.planning.PadMessage.action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=191,
)

_PADMESSAGE.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_PADMESSAGE.fields_by_name['action'].enum_type = _DRIVINGACTION
DESCRIPTOR.message_types_by_name['PadMessage'] = _PADMESSAGE
DESCRIPTOR.enum_types_by_name['DrivingAction'] = _DRIVINGACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PadMessage = _reflection.GeneratedProtocolMessageType('PadMessage', (_message.Message,), dict(
  DESCRIPTOR = _PADMESSAGE,
  __module__ = 'modules.planning.proto.pad_msg_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.PadMessage)
  ))
_sym_db.RegisterMessage(PadMessage)


# @@protoc_insertion_point(module_scope)
