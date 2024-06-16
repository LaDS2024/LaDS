# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/contrib/lgsvl_msgs/proto/detection2d.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from gym_apollo.envs.modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/contrib/lgsvl_msgs/proto/detection2d.proto',
  package='apollo.contrib.lgsvl_msgs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n2modules/contrib/lgsvl_msgs/proto/detection2d.proto\x12\x19\x61pollo.contrib.lgsvl_msgs\x1a!modules/common/proto/header.proto\"D\n\rBoundingBox2D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\"*\n\x07Vector3\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"p\n\x05Twist\x12\x32\n\x06linear\x18\x01 \x01(\x0b\x32\".apollo.contrib.lgsvl_msgs.Vector3\x12\x33\n\x07\x61ngular\x18\x02 \x01(\x0b\x32\".apollo.contrib.lgsvl_msgs.Vector3\"\xca\x01\n\x0b\x44\x65tection2D\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\n\n\x02id\x18\x02 \x01(\r\x12\r\n\x05label\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x01\x12\x36\n\x04\x62\x62ox\x18\x05 \x01(\x0b\x32(.apollo.contrib.lgsvl_msgs.BoundingBox2D\x12\x32\n\x08velocity\x18\x06 \x01(\x0b\x32 .apollo.contrib.lgsvl_msgs.Twistb\x06proto3')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,])




_BOUNDINGBOX2D = _descriptor.Descriptor(
  name='BoundingBox2D',
  full_name='apollo.contrib.lgsvl_msgs.BoundingBox2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='apollo.contrib.lgsvl_msgs.BoundingBox2D.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='apollo.contrib.lgsvl_msgs.BoundingBox2D.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='apollo.contrib.lgsvl_msgs.BoundingBox2D.width', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='apollo.contrib.lgsvl_msgs.BoundingBox2D.height', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=184,
)


_VECTOR3 = _descriptor.Descriptor(
  name='Vector3',
  full_name='apollo.contrib.lgsvl_msgs.Vector3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='apollo.contrib.lgsvl_msgs.Vector3.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='apollo.contrib.lgsvl_msgs.Vector3.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='apollo.contrib.lgsvl_msgs.Vector3.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=228,
)


_TWIST = _descriptor.Descriptor(
  name='Twist',
  full_name='apollo.contrib.lgsvl_msgs.Twist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='linear', full_name='apollo.contrib.lgsvl_msgs.Twist.linear', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular', full_name='apollo.contrib.lgsvl_msgs.Twist.angular', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=342,
)


_DETECTION2D = _descriptor.Descriptor(
  name='Detection2D',
  full_name='apollo.contrib.lgsvl_msgs.Detection2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.contrib.lgsvl_msgs.Detection2D.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.contrib.lgsvl_msgs.Detection2D.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='apollo.contrib.lgsvl_msgs.Detection2D.label', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='apollo.contrib.lgsvl_msgs.Detection2D.score', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bbox', full_name='apollo.contrib.lgsvl_msgs.Detection2D.bbox', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='apollo.contrib.lgsvl_msgs.Detection2D.velocity', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=547,
)

_TWIST.fields_by_name['linear'].message_type = _VECTOR3
_TWIST.fields_by_name['angular'].message_type = _VECTOR3
_DETECTION2D.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_DETECTION2D.fields_by_name['bbox'].message_type = _BOUNDINGBOX2D
_DETECTION2D.fields_by_name['velocity'].message_type = _TWIST
DESCRIPTOR.message_types_by_name['BoundingBox2D'] = _BOUNDINGBOX2D
DESCRIPTOR.message_types_by_name['Vector3'] = _VECTOR3
DESCRIPTOR.message_types_by_name['Twist'] = _TWIST
DESCRIPTOR.message_types_by_name['Detection2D'] = _DETECTION2D
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BoundingBox2D = _reflection.GeneratedProtocolMessageType('BoundingBox2D', (_message.Message,), dict(
  DESCRIPTOR = _BOUNDINGBOX2D,
  __module__ = 'modules.contrib.lgsvl_msgs.proto.detection2d_pb2'
  # @@protoc_insertion_point(class_scope:apollo.contrib.lgsvl_msgs.BoundingBox2D)
  ))
_sym_db.RegisterMessage(BoundingBox2D)

Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR3,
  __module__ = 'modules.contrib.lgsvl_msgs.proto.detection2d_pb2'
  # @@protoc_insertion_point(class_scope:apollo.contrib.lgsvl_msgs.Vector3)
  ))
_sym_db.RegisterMessage(Vector3)

Twist = _reflection.GeneratedProtocolMessageType('Twist', (_message.Message,), dict(
  DESCRIPTOR = _TWIST,
  __module__ = 'modules.contrib.lgsvl_msgs.proto.detection2d_pb2'
  # @@protoc_insertion_point(class_scope:apollo.contrib.lgsvl_msgs.Twist)
  ))
_sym_db.RegisterMessage(Twist)

Detection2D = _reflection.GeneratedProtocolMessageType('Detection2D', (_message.Message,), dict(
  DESCRIPTOR = _DETECTION2D,
  __module__ = 'modules.contrib.lgsvl_msgs.proto.detection2d_pb2'
  # @@protoc_insertion_point(class_scope:apollo.contrib.lgsvl_msgs.Detection2D)
  ))
_sym_db.RegisterMessage(Detection2D)


# @@protoc_insertion_point(module_scope)
