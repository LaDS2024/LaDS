# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/canbus/proto/sensor_canbus_conf.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from gym_apollo.envs.modules.drivers.canbus.proto import \
    can_card_parameter_pb2 as modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/drivers/canbus/proto/sensor_canbus_conf.proto',
  package='apollo.drivers.canbus',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n5modules/drivers/canbus/proto/sensor_canbus_conf.proto\x12\x15\x61pollo.drivers.canbus\x1a\x35modules/drivers/canbus/proto/can_card_parameter.proto\"\x9d\x01\n\x10SensorCanbusConf\x12\x43\n\x12\x63\x61n_card_parameter\x18\x01 \x01(\x0b\x32\'.apollo.drivers.canbus.CANCardParameter\x12 \n\x11\x65nable_debug_mode\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\"\n\x13\x65nable_receiver_log\x18\x03 \x01(\x08:\x05\x66\x61lse')
  ,
  dependencies=[modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2.DESCRIPTOR,])




_SENSORCANBUSCONF = _descriptor.Descriptor(
  name='SensorCanbusConf',
  full_name='apollo.drivers.canbus.SensorCanbusConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='can_card_parameter', full_name='apollo.drivers.canbus.SensorCanbusConf.can_card_parameter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_debug_mode', full_name='apollo.drivers.canbus.SensorCanbusConf.enable_debug_mode', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_receiver_log', full_name='apollo.drivers.canbus.SensorCanbusConf.enable_receiver_log', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=136,
  serialized_end=293,
)

_SENSORCANBUSCONF.fields_by_name['can_card_parameter'].message_type = modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2._CANCARDPARAMETER
DESCRIPTOR.message_types_by_name['SensorCanbusConf'] = _SENSORCANBUSCONF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SensorCanbusConf = _reflection.GeneratedProtocolMessageType('SensorCanbusConf', (_message.Message,), dict(
  DESCRIPTOR = _SENSORCANBUSCONF,
  __module__ = 'modules.drivers.canbus.proto.sensor_canbus_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.canbus.SensorCanbusConf)
  ))
_sym_db.RegisterMessage(SensorCanbusConf)


# @@protoc_insertion_point(module_scope)
