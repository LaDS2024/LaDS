# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/lidar/proto/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from  modules.drivers.lidar.proto import \
    hesai_config_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_hesai__config__pb2, \
    robosense_config_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_robosense__config__pb2, \
    velodyne_config_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_velodyne__config__pb2, \
    lidar_parameter_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_lidar__parameter__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/drivers/lidar/proto/config.proto',
  package='apollo.drivers.lidar',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n(modules/drivers/lidar/proto/config.proto\x12\x14\x61pollo.drivers.lidar\x1a.modules/drivers/lidar/proto/hesai_config.proto\x1a\x31modules/drivers/lidar/proto/velodyne_config.proto\x1a\x31modules/drivers/lidar/proto/lidar_parameter.proto\x1a\x32modules/drivers/lidar/proto/robosense_config.proto\"\xdd\x01\n\x06\x63onfig\x12>\n\x05\x62rand\x18\x01 \x01(\x0e\x32/.apollo.drivers.lidar.LidarParameter.LidarBrand\x12+\n\x05hesai\x18\x02 \x01(\x0b\x32\x1c.apollo.drivers.hesai.Config\x12\x33\n\trobosense\x18\x03 \x01(\x0b\x32 .apollo.drivers.robosense.Config\x12\x31\n\x08velodyne\x18\x04 \x01(\x0b\x32\x1f.apollo.drivers.velodyne.Config')
  ,
  dependencies=[modules_dot_drivers_dot_lidar_dot_proto_dot_hesai__config__pb2.DESCRIPTOR,modules_dot_drivers_dot_lidar_dot_proto_dot_velodyne__config__pb2.DESCRIPTOR,modules_dot_drivers_dot_lidar_dot_proto_dot_lidar__parameter__pb2.DESCRIPTOR,modules_dot_drivers_dot_lidar_dot_proto_dot_robosense__config__pb2.DESCRIPTOR,])




_CONFIG = _descriptor.Descriptor(
  name='config',
  full_name='apollo.drivers.lidar.config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='brand', full_name='apollo.drivers.lidar.config.brand', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hesai', full_name='apollo.drivers.lidar.config.hesai', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='robosense', full_name='apollo.drivers.lidar.config.robosense', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velodyne', full_name='apollo.drivers.lidar.config.velodyne', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=269,
  serialized_end=490,
)

_CONFIG.fields_by_name['brand'].enum_type = modules_dot_drivers_dot_lidar_dot_proto_dot_lidar__parameter__pb2._LIDARPARAMETER_LIDARBRAND
_CONFIG.fields_by_name['hesai'].message_type = modules_dot_drivers_dot_lidar_dot_proto_dot_hesai__config__pb2._CONFIG
_CONFIG.fields_by_name['robosense'].message_type = modules_dot_drivers_dot_lidar_dot_proto_dot_robosense__config__pb2._CONFIG
_CONFIG.fields_by_name['velodyne'].message_type = modules_dot_drivers_dot_lidar_dot_proto_dot_velodyne__config__pb2._CONFIG
DESCRIPTOR.message_types_by_name['config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

config = _reflection.GeneratedProtocolMessageType('config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'modules.drivers.lidar.proto.config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.lidar.config)
  ))
_sym_db.RegisterMessage(config)


# @@protoc_insertion_point(module_scope)
