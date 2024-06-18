# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/control/proto/control_common_conf.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from  modules.canbus.proto import chassis_pb2 as modules_dot_canbus_dot_proto_dot_chassis__pb2
from  modules.control.proto import pad_msg_pb2 as modules_dot_control_dot_proto_dot_pad__msg__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/control/proto/control_common_conf.proto',
  package='apollo.control',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n/modules/control/proto/control_common_conf.proto\x12\x0e\x61pollo.control\x1a\"modules/canbus/proto/chassis.proto\x1a#modules/control/proto/pad_msg.proto\"\xde\t\n\x11\x43ontrolCommonConf\x12!\n\x15\x63ontrol_test_duration\x18\x01 \x01(\x01:\x02-1\x12\x1f\n\x10\x65nable_csv_debug\x18\x02 \x01(\x08:\x05\x66\x61lse\x12+\n\x1c\x65nable_speed_station_preview\x18\x03 \x01(\x08:\x05\x66\x61lse\x12#\n\x14is_control_test_mode\x18\x04 \x01(\x08:\x05\x66\x61lse\x12*\n\x1buse_preview_speed_for_table\x18\x05 \x01(\x08:\x05\x66\x61lse\x12+\n\x1c\x65nable_input_timestamp_check\x18\x06 \x01(\x08:\x05\x66\x61lse\x12%\n\x19max_localization_miss_num\x18\x07 \x01(\x05:\x02\x32\x30\x12 \n\x14max_chassis_miss_num\x18\x08 \x01(\x05:\x02\x32\x30\x12!\n\x15max_planning_miss_num\x18\t \x01(\x05:\x02\x32\x30\x12+\n\x1dmax_acceleration_when_stopped\x18\n \x01(\x01:\x04\x30.01\x12\x1d\n\x10steer_angle_rate\x18\x0b \x01(\x01:\x03\x31\x30\x30\x12#\n\x15\x65nable_gain_scheduler\x18\x0c \x01(\x08:\x04true\x12\x1d\n\x0fset_steer_limit\x18\r \x01(\x08:\x04true\x12\"\n\x13\x65nable_slope_offset\x18\x0e \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x10lock_steer_speed\x18\x0f \x01(\x01:\x05\x30.081\x12\x32\n#enable_navigation_mode_error_filter\x18\x10 \x01(\x08:\x05\x66\x61lse\x12\x34\n&enable_navigation_mode_position_update\x18\x11 \x01(\x08:\x04true\x12%\n\x17\x65nable_persistent_estop\x18\x12 \x01(\x08:\x04true\x12\x16\n\x0e\x63ontrol_period\x18\x13 \x01(\x01\x12!\n\x19max_planning_interval_sec\x18\x14 \x01(\x01\x12$\n\x1cmax_planning_delay_threshold\x18\x15 \x01(\x01\x12\x38\n\x0c\x64riving_mode\x18\x16 \x01(\x0e\x32\".apollo.canbus.Chassis.DrivingMode\x12-\n\x06\x61\x63tion\x18\x17 \x01(\x0e\x32\x1d.apollo.control.DrivingAction\x12\x18\n\x10soft_estop_brake\x18\x18 \x01(\x01\x12\'\n\x1fmax_steering_percentage_allowed\x18\x1a \x01(\x05\x12\x1f\n\x17max_status_interval_sec\x18\x1b \x01(\x01\x12\x19\n\x11trajectory_period\x18\x1e \x01(\x01\x12\x16\n\x0e\x63hassis_period\x18\x1f \x01(\x01\x12\x1b\n\x13localization_period\x18  \x01(\x01\x12 \n\x18minimum_speed_resolution\x18! \x01(\x01\x12\x1b\n\x13query_relative_time\x18# \x01(\x01\x12 \n\x18minimum_speed_protection\x18$ \x01(\x01\x12)\n\x1cmax_path_remain_when_stopped\x18% \x01(\x01:\x03\x30.3')
  ,
  dependencies=[modules_dot_canbus_dot_proto_dot_chassis__pb2.DESCRIPTOR,modules_dot_control_dot_proto_dot_pad__msg__pb2.DESCRIPTOR,])




_CONTROLCOMMONCONF = _descriptor.Descriptor(
  name='ControlCommonConf',
  full_name='apollo.control.ControlCommonConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='control_test_duration', full_name='apollo.control.ControlCommonConf.control_test_duration', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(-1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_csv_debug', full_name='apollo.control.ControlCommonConf.enable_csv_debug', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_speed_station_preview', full_name='apollo.control.ControlCommonConf.enable_speed_station_preview', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_control_test_mode', full_name='apollo.control.ControlCommonConf.is_control_test_mode', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_preview_speed_for_table', full_name='apollo.control.ControlCommonConf.use_preview_speed_for_table', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_input_timestamp_check', full_name='apollo.control.ControlCommonConf.enable_input_timestamp_check', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_localization_miss_num', full_name='apollo.control.ControlCommonConf.max_localization_miss_num', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=20,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_chassis_miss_num', full_name='apollo.control.ControlCommonConf.max_chassis_miss_num', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=20,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_planning_miss_num', full_name='apollo.control.ControlCommonConf.max_planning_miss_num', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=20,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_acceleration_when_stopped', full_name='apollo.control.ControlCommonConf.max_acceleration_when_stopped', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.01),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steer_angle_rate', full_name='apollo.control.ControlCommonConf.steer_angle_rate', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(100),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_gain_scheduler', full_name='apollo.control.ControlCommonConf.enable_gain_scheduler', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_steer_limit', full_name='apollo.control.ControlCommonConf.set_steer_limit', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_slope_offset', full_name='apollo.control.ControlCommonConf.enable_slope_offset', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lock_steer_speed', full_name='apollo.control.ControlCommonConf.lock_steer_speed', index=14,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.081),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_navigation_mode_error_filter', full_name='apollo.control.ControlCommonConf.enable_navigation_mode_error_filter', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_navigation_mode_position_update', full_name='apollo.control.ControlCommonConf.enable_navigation_mode_position_update', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_persistent_estop', full_name='apollo.control.ControlCommonConf.enable_persistent_estop', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='control_period', full_name='apollo.control.ControlCommonConf.control_period', index=18,
      number=19, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_planning_interval_sec', full_name='apollo.control.ControlCommonConf.max_planning_interval_sec', index=19,
      number=20, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_planning_delay_threshold', full_name='apollo.control.ControlCommonConf.max_planning_delay_threshold', index=20,
      number=21, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='driving_mode', full_name='apollo.control.ControlCommonConf.driving_mode', index=21,
      number=22, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='apollo.control.ControlCommonConf.action', index=22,
      number=23, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='soft_estop_brake', full_name='apollo.control.ControlCommonConf.soft_estop_brake', index=23,
      number=24, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_steering_percentage_allowed', full_name='apollo.control.ControlCommonConf.max_steering_percentage_allowed', index=24,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_status_interval_sec', full_name='apollo.control.ControlCommonConf.max_status_interval_sec', index=25,
      number=27, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trajectory_period', full_name='apollo.control.ControlCommonConf.trajectory_period', index=26,
      number=30, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chassis_period', full_name='apollo.control.ControlCommonConf.chassis_period', index=27,
      number=31, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localization_period', full_name='apollo.control.ControlCommonConf.localization_period', index=28,
      number=32, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minimum_speed_resolution', full_name='apollo.control.ControlCommonConf.minimum_speed_resolution', index=29,
      number=33, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query_relative_time', full_name='apollo.control.ControlCommonConf.query_relative_time', index=30,
      number=35, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minimum_speed_protection', full_name='apollo.control.ControlCommonConf.minimum_speed_protection', index=31,
      number=36, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_path_remain_when_stopped', full_name='apollo.control.ControlCommonConf.max_path_remain_when_stopped', index=32,
      number=37, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.3),
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
  serialized_start=141,
  serialized_end=1387,
)

_CONTROLCOMMONCONF.fields_by_name['driving_mode'].enum_type = modules_dot_canbus_dot_proto_dot_chassis__pb2._CHASSIS_DRIVINGMODE
_CONTROLCOMMONCONF.fields_by_name['action'].enum_type = modules_dot_control_dot_proto_dot_pad__msg__pb2._DRIVINGACTION
DESCRIPTOR.message_types_by_name['ControlCommonConf'] = _CONTROLCOMMONCONF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ControlCommonConf = _reflection.GeneratedProtocolMessageType('ControlCommonConf', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLCOMMONCONF,
  __module__ = 'modules.control.proto.control_common_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.control.ControlCommonConf)
  ))
_sym_db.RegisterMessage(ControlCommonConf)


# @@protoc_insertion_point(module_scope)