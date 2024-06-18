# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common/vehicle_state/proto/vehicle_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from  modules.canbus.proto import chassis_pb2 as modules_dot_canbus_dot_proto_dot_chassis__pb2
from  modules.localization.proto import pose_pb2 as modules_dot_localization_dot_proto_dot_pose__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/common/vehicle_state/proto/vehicle_state.proto',
  package='apollo.common',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n6modules/common/vehicle_state/proto/vehicle_state.proto\x12\rapollo.common\x1a\"modules/canbus/proto/chassis.proto\x1a%modules/localization/proto/pose.proto\"\xb3\x03\n\x0cVehicleState\x12\x0c\n\x01x\x18\x01 \x01(\x01:\x01\x30\x12\x0c\n\x01y\x18\x02 \x01(\x01:\x01\x30\x12\x0c\n\x01z\x18\x03 \x01(\x01:\x01\x30\x12\x14\n\ttimestamp\x18\x04 \x01(\x01:\x01\x30\x12\x0f\n\x04roll\x18\x05 \x01(\x01:\x01\x30\x12\x10\n\x05pitch\x18\x06 \x01(\x01:\x01\x30\x12\x0e\n\x03yaw\x18\x07 \x01(\x01:\x01\x30\x12\x12\n\x07heading\x18\x08 \x01(\x01:\x01\x30\x12\x10\n\x05kappa\x18\t \x01(\x01:\x01\x30\x12\x1a\n\x0flinear_velocity\x18\n \x01(\x01:\x01\x30\x12\x1b\n\x10\x61ngular_velocity\x18\x0b \x01(\x01:\x01\x30\x12\x1e\n\x13linear_acceleration\x18\x0c \x01(\x01:\x01\x30\x12\x31\n\x04gear\x18\r \x01(\x0e\x32#.apollo.canbus.Chassis.GearPosition\x12\x38\n\x0c\x64riving_mode\x18\x0e \x01(\x0e\x32\".apollo.canbus.Chassis.DrivingMode\x12\'\n\x04pose\x18\x0f \x01(\x0b\x32\x19.apollo.localization.Pose\x12\x1b\n\x13steering_percentage\x18\x10 \x01(\x01')
  ,
  dependencies=[modules_dot_canbus_dot_proto_dot_chassis__pb2.DESCRIPTOR,modules_dot_localization_dot_proto_dot_pose__pb2.DESCRIPTOR,])




_VEHICLESTATE = _descriptor.Descriptor(
  name='VehicleState',
  full_name='apollo.common.VehicleState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='apollo.common.VehicleState.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='apollo.common.VehicleState.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='apollo.common.VehicleState.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='apollo.common.VehicleState.timestamp', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roll', full_name='apollo.common.VehicleState.roll', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='apollo.common.VehicleState.pitch', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yaw', full_name='apollo.common.VehicleState.yaw', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='apollo.common.VehicleState.heading', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kappa', full_name='apollo.common.VehicleState.kappa', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_velocity', full_name='apollo.common.VehicleState.linear_velocity', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_velocity', full_name='apollo.common.VehicleState.angular_velocity', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_acceleration', full_name='apollo.common.VehicleState.linear_acceleration', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gear', full_name='apollo.common.VehicleState.gear', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='driving_mode', full_name='apollo.common.VehicleState.driving_mode', index=13,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pose', full_name='apollo.common.VehicleState.pose', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steering_percentage', full_name='apollo.common.VehicleState.steering_percentage', index=15,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=149,
  serialized_end=584,
)

_VEHICLESTATE.fields_by_name['gear'].enum_type = modules_dot_canbus_dot_proto_dot_chassis__pb2._CHASSIS_GEARPOSITION
_VEHICLESTATE.fields_by_name['driving_mode'].enum_type = modules_dot_canbus_dot_proto_dot_chassis__pb2._CHASSIS_DRIVINGMODE
_VEHICLESTATE.fields_by_name['pose'].message_type = modules_dot_localization_dot_proto_dot_pose__pb2._POSE
DESCRIPTOR.message_types_by_name['VehicleState'] = _VEHICLESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VehicleState = _reflection.GeneratedProtocolMessageType('VehicleState', (_message.Message,), dict(
  DESCRIPTOR = _VEHICLESTATE,
  __module__ = 'modules.common.vehicle_state.proto.vehicle_state_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.VehicleState)
  ))
_sym_db.RegisterMessage(VehicleState)


# @@protoc_insertion_point(module_scope)
