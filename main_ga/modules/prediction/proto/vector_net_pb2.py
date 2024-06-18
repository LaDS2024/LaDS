# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/prediction/proto/vector_net.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/prediction/proto/vector_net.proto',
  package='apollo.prediction',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n)modules/prediction/proto/vector_net.proto\x12\x11\x61pollo.prediction\"\x1b\n\x08VNVector\x12\x0f\n\x07\x65lement\x18\x01 \x03(\x01\"W\n\x08Polyline\x12+\n\x06vector\x18\x01 \x03(\x0b\x32\x1b.apollo.prediction.VNVector\x12\x0e\n\x06p_id_x\x18\x02 \x01(\x01\x12\x0e\n\x06p_id_y\x18\x03 \x01(\x01\"<\n\x0b\x43\x61rPosition\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\x0b\n\x03phi\x18\x03 \x01(\x01\x12\n\n\x02id\x18\x04 \x01(\t\"w\n\x10VectorNetFeature\x12\x34\n\x0c\x63\x61r_position\x18\x01 \x01(\x0b\x32\x1e.apollo.prediction.CarPosition\x12-\n\x08polyline\x18\x02 \x03(\x0b\x32\x1b.apollo.prediction.Polyline\":\n\nWorldCoord\x12,\n\x04pose\x18\x01 \x03(\x0b\x32\x1e.apollo.prediction.CarPosition')
)




_VNVECTOR = _descriptor.Descriptor(
  name='VNVector',
  full_name='apollo.prediction.VNVector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='element', full_name='apollo.prediction.VNVector.element', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=64,
  serialized_end=91,
)


_POLYLINE = _descriptor.Descriptor(
  name='Polyline',
  full_name='apollo.prediction.Polyline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vector', full_name='apollo.prediction.Polyline.vector', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p_id_x', full_name='apollo.prediction.Polyline.p_id_x', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p_id_y', full_name='apollo.prediction.Polyline.p_id_y', index=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=180,
)


_CARPOSITION = _descriptor.Descriptor(
  name='CarPosition',
  full_name='apollo.prediction.CarPosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='apollo.prediction.CarPosition.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='apollo.prediction.CarPosition.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phi', full_name='apollo.prediction.CarPosition.phi', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.prediction.CarPosition.id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=182,
  serialized_end=242,
)


_VECTORNETFEATURE = _descriptor.Descriptor(
  name='VectorNetFeature',
  full_name='apollo.prediction.VectorNetFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='car_position', full_name='apollo.prediction.VectorNetFeature.car_position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='polyline', full_name='apollo.prediction.VectorNetFeature.polyline', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=244,
  serialized_end=363,
)


_WORLDCOORD = _descriptor.Descriptor(
  name='WorldCoord',
  full_name='apollo.prediction.WorldCoord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pose', full_name='apollo.prediction.WorldCoord.pose', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=365,
  serialized_end=423,
)

_POLYLINE.fields_by_name['vector'].message_type = _VNVECTOR
_VECTORNETFEATURE.fields_by_name['car_position'].message_type = _CARPOSITION
_VECTORNETFEATURE.fields_by_name['polyline'].message_type = _POLYLINE
_WORLDCOORD.fields_by_name['pose'].message_type = _CARPOSITION
DESCRIPTOR.message_types_by_name['VNVector'] = _VNVECTOR
DESCRIPTOR.message_types_by_name['Polyline'] = _POLYLINE
DESCRIPTOR.message_types_by_name['CarPosition'] = _CARPOSITION
DESCRIPTOR.message_types_by_name['VectorNetFeature'] = _VECTORNETFEATURE
DESCRIPTOR.message_types_by_name['WorldCoord'] = _WORLDCOORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VNVector = _reflection.GeneratedProtocolMessageType('VNVector', (_message.Message,), dict(
  DESCRIPTOR = _VNVECTOR,
  __module__ = 'modules.prediction.proto.vector_net_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.VNVector)
  ))
_sym_db.RegisterMessage(VNVector)

Polyline = _reflection.GeneratedProtocolMessageType('Polyline', (_message.Message,), dict(
  DESCRIPTOR = _POLYLINE,
  __module__ = 'modules.prediction.proto.vector_net_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.Polyline)
  ))
_sym_db.RegisterMessage(Polyline)

CarPosition = _reflection.GeneratedProtocolMessageType('CarPosition', (_message.Message,), dict(
  DESCRIPTOR = _CARPOSITION,
  __module__ = 'modules.prediction.proto.vector_net_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.CarPosition)
  ))
_sym_db.RegisterMessage(CarPosition)

VectorNetFeature = _reflection.GeneratedProtocolMessageType('VectorNetFeature', (_message.Message,), dict(
  DESCRIPTOR = _VECTORNETFEATURE,
  __module__ = 'modules.prediction.proto.vector_net_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.VectorNetFeature)
  ))
_sym_db.RegisterMessage(VectorNetFeature)

WorldCoord = _reflection.GeneratedProtocolMessageType('WorldCoord', (_message.Message,), dict(
  DESCRIPTOR = _WORLDCOORD,
  __module__ = 'modules.prediction.proto.vector_net_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.WorldCoord)
  ))
_sym_db.RegisterMessage(WorldCoord)


# @@protoc_insertion_point(module_scope)
