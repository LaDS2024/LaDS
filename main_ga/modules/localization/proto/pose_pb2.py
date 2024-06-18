# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/localization/proto/pose.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/localization/proto/pose.proto',
  package='apollo.localization',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n%modules/localization/proto/pose.proto\x12\x13\x61pollo.localization\x1a#modules/common/proto/geometry.proto\"\xa7\x03\n\x04Pose\x12)\n\x08position\x18\x01 \x01(\x0b\x32\x17.apollo.common.PointENU\x12.\n\x0borientation\x18\x02 \x01(\x0b\x32\x19.apollo.common.Quaternion\x12/\n\x0flinear_velocity\x18\x03 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x33\n\x13linear_acceleration\x18\x04 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x30\n\x10\x61ngular_velocity\x18\x05 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x0f\n\x07heading\x18\x06 \x01(\x01\x12\x37\n\x17linear_acceleration_vrf\x18\x07 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x34\n\x14\x61ngular_velocity_vrf\x18\x08 \x01(\x0b\x32\x16.apollo.common.Point3D\x12,\n\x0c\x65uler_angles\x18\t \x01(\x0b\x32\x16.apollo.common.Point3D')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_geometry__pb2.DESCRIPTOR,])




_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='apollo.localization.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='apollo.localization.Pose.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='apollo.localization.Pose.orientation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_velocity', full_name='apollo.localization.Pose.linear_velocity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_acceleration', full_name='apollo.localization.Pose.linear_acceleration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_velocity', full_name='apollo.localization.Pose.angular_velocity', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='apollo.localization.Pose.heading', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_acceleration_vrf', full_name='apollo.localization.Pose.linear_acceleration_vrf', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_velocity_vrf', full_name='apollo.localization.Pose.angular_velocity_vrf', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='euler_angles', full_name='apollo.localization.Pose.euler_angles', index=8,
      number=9, type=11, cpp_type=10, label=1,
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
  serialized_start=100,
  serialized_end=523,
)

_POSE.fields_by_name['position'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINTENU
_POSE.fields_by_name['orientation'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._QUATERNION
_POSE.fields_by_name['linear_velocity'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_POSE.fields_by_name['linear_acceleration'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_POSE.fields_by_name['angular_velocity'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_POSE.fields_by_name['linear_acceleration_vrf'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_POSE.fields_by_name['angular_velocity_vrf'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_POSE.fields_by_name['euler_angles'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
DESCRIPTOR.message_types_by_name['Pose'] = _POSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), dict(
  DESCRIPTOR = _POSE,
  __module__ = 'modules.localization.proto.pose_pb2'
  # @@protoc_insertion_point(class_scope:apollo.localization.Pose)
  ))
_sym_db.RegisterMessage(Pose)


# @@protoc_insertion_point(module_scope)
