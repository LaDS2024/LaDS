# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/routing/proto/topo_graph.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from gym_apollo.envs.modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/routing/proto/topo_graph.proto',
  package='apollo.routing',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n&modules/routing/proto/topo_graph.proto\x12\x0e\x61pollo.routing\x1a$modules/map/proto/map_geometry.proto\"\x17\n\nCurvePoint\x12\t\n\x01s\x18\x01 \x01(\x01\"`\n\nCurveRange\x12)\n\x05start\x18\x01 \x01(\x0b\x32\x1a.apollo.routing.CurvePoint\x12\'\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1a.apollo.routing.CurvePoint\"\xe9\x01\n\x04Node\x12\x0f\n\x07lane_id\x18\x01 \x01(\t\x12\x0e\n\x06length\x18\x02 \x01(\x01\x12,\n\x08left_out\x18\x03 \x03(\x0b\x32\x1a.apollo.routing.CurveRange\x12-\n\tright_out\x18\x04 \x03(\x0b\x32\x1a.apollo.routing.CurveRange\x12\x0c\n\x04\x63ost\x18\x05 \x01(\x01\x12*\n\rcentral_curve\x18\x06 \x01(\x0b\x32\x13.apollo.hdmap.Curve\x12\x18\n\nis_virtual\x18\x07 \x01(\x08:\x04true\x12\x0f\n\x07road_id\x18\x08 \x01(\t\"\xad\x01\n\x04\x45\x64ge\x12\x14\n\x0c\x66rom_lane_id\x18\x01 \x01(\t\x12\x12\n\nto_lane_id\x18\x02 \x01(\t\x12\x0c\n\x04\x63ost\x18\x03 \x01(\x01\x12:\n\x0e\x64irection_type\x18\x04 \x01(\x0e\x32\".apollo.routing.Edge.DirectionType\"1\n\rDirectionType\x12\x0b\n\x07\x46ORWARD\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\"~\n\x05Graph\x12\x15\n\rhdmap_version\x18\x01 \x01(\t\x12\x16\n\x0ehdmap_district\x18\x02 \x01(\t\x12\"\n\x04node\x18\x03 \x03(\x0b\x32\x14.apollo.routing.Node\x12\"\n\x04\x65\x64ge\x18\x04 \x03(\x0b\x32\x14.apollo.routing.Edge')
  ,
  dependencies=[modules_dot_map_dot_proto_dot_map__geometry__pb2.DESCRIPTOR,])



_EDGE_DIRECTIONTYPE = _descriptor.EnumDescriptor(
  name='DirectionType',
  full_name='apollo.routing.Edge.DirectionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FORWARD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=580,
  serialized_end=629,
)
_sym_db.RegisterEnumDescriptor(_EDGE_DIRECTIONTYPE)


_CURVEPOINT = _descriptor.Descriptor(
  name='CurvePoint',
  full_name='apollo.routing.CurvePoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='apollo.routing.CurvePoint.s', index=0,
      number=1, type=1, cpp_type=5, label=1,
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
  serialized_start=96,
  serialized_end=119,
)


_CURVERANGE = _descriptor.Descriptor(
  name='CurveRange',
  full_name='apollo.routing.CurveRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='apollo.routing.CurveRange.start', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='apollo.routing.CurveRange.end', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=217,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='apollo.routing.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lane_id', full_name='apollo.routing.Node.lane_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='apollo.routing.Node.length', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_out', full_name='apollo.routing.Node.left_out', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_out', full_name='apollo.routing.Node.right_out', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost', full_name='apollo.routing.Node.cost', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='central_curve', full_name='apollo.routing.Node.central_curve', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_virtual', full_name='apollo.routing.Node.is_virtual', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='road_id', full_name='apollo.routing.Node.road_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=220,
  serialized_end=453,
)


_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='apollo.routing.Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_lane_id', full_name='apollo.routing.Edge.from_lane_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_lane_id', full_name='apollo.routing.Edge.to_lane_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost', full_name='apollo.routing.Edge.cost', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction_type', full_name='apollo.routing.Edge.direction_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EDGE_DIRECTIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=456,
  serialized_end=629,
)


_GRAPH = _descriptor.Descriptor(
  name='Graph',
  full_name='apollo.routing.Graph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hdmap_version', full_name='apollo.routing.Graph.hdmap_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hdmap_district', full_name='apollo.routing.Graph.hdmap_district', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node', full_name='apollo.routing.Graph.node', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edge', full_name='apollo.routing.Graph.edge', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=631,
  serialized_end=757,
)

_CURVERANGE.fields_by_name['start'].message_type = _CURVEPOINT
_CURVERANGE.fields_by_name['end'].message_type = _CURVEPOINT
_NODE.fields_by_name['left_out'].message_type = _CURVERANGE
_NODE.fields_by_name['right_out'].message_type = _CURVERANGE
_NODE.fields_by_name['central_curve'].message_type = modules_dot_map_dot_proto_dot_map__geometry__pb2._CURVE
_EDGE.fields_by_name['direction_type'].enum_type = _EDGE_DIRECTIONTYPE
_EDGE_DIRECTIONTYPE.containing_type = _EDGE
_GRAPH.fields_by_name['node'].message_type = _NODE
_GRAPH.fields_by_name['edge'].message_type = _EDGE
DESCRIPTOR.message_types_by_name['CurvePoint'] = _CURVEPOINT
DESCRIPTOR.message_types_by_name['CurveRange'] = _CURVERANGE
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Edge'] = _EDGE
DESCRIPTOR.message_types_by_name['Graph'] = _GRAPH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CurvePoint = _reflection.GeneratedProtocolMessageType('CurvePoint', (_message.Message,), dict(
  DESCRIPTOR = _CURVEPOINT,
  __module__ = 'modules.routing.proto.topo_graph_pb2'
  # @@protoc_insertion_point(class_scope:apollo.routing.CurvePoint)
  ))
_sym_db.RegisterMessage(CurvePoint)

CurveRange = _reflection.GeneratedProtocolMessageType('CurveRange', (_message.Message,), dict(
  DESCRIPTOR = _CURVERANGE,
  __module__ = 'modules.routing.proto.topo_graph_pb2'
  # @@protoc_insertion_point(class_scope:apollo.routing.CurveRange)
  ))
_sym_db.RegisterMessage(CurveRange)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
  DESCRIPTOR = _NODE,
  __module__ = 'modules.routing.proto.topo_graph_pb2'
  # @@protoc_insertion_point(class_scope:apollo.routing.Node)
  ))
_sym_db.RegisterMessage(Node)

Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), dict(
  DESCRIPTOR = _EDGE,
  __module__ = 'modules.routing.proto.topo_graph_pb2'
  # @@protoc_insertion_point(class_scope:apollo.routing.Edge)
  ))
_sym_db.RegisterMessage(Edge)

Graph = _reflection.GeneratedProtocolMessageType('Graph', (_message.Message,), dict(
  DESCRIPTOR = _GRAPH,
  __module__ = 'modules.routing.proto.topo_graph_pb2'
  # @@protoc_insertion_point(class_scope:apollo.routing.Graph)
  ))
_sym_db.RegisterMessage(Graph)


# @@protoc_insertion_point(module_scope)
