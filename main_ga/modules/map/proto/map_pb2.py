# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/map/proto/map.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from  modules.map.proto import map_crosswalk_pb2 as modules_dot_map_dot_proto_dot_map__crosswalk__pb2, \
    map_yield_sign_pb2 as modules_dot_map_dot_proto_dot_map__yield__sign__pb2, \
    map_parking_space_pb2 as modules_dot_map_dot_proto_dot_map__parking__space__pb2, \
    map_clear_area_pb2 as modules_dot_map_dot_proto_dot_map__clear__area__pb2, \
    map_stop_sign_pb2 as modules_dot_map_dot_proto_dot_map__stop__sign__pb2, \
    map_rsu_pb2 as modules_dot_map_dot_proto_dot_map__rsu__pb2, \
    map_speed_bump_pb2 as modules_dot_map_dot_proto_dot_map__speed__bump__pb2, \
    map_road_pb2 as modules_dot_map_dot_proto_dot_map__road__pb2, \
    map_pnc_junction_pb2 as modules_dot_map_dot_proto_dot_map__pnc__junction__pb2, \
    map_junction_pb2 as modules_dot_map_dot_proto_dot_map__junction__pb2, \
    map_lane_pb2 as modules_dot_map_dot_proto_dot_map__lane__pb2, \
    map_signal_pb2 as modules_dot_map_dot_proto_dot_map__signal__pb2, \
    map_overlap_pb2 as modules_dot_map_dot_proto_dot_map__overlap__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/map/proto/map.proto',
  package='apollo.hdmap',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1bmodules/map/proto/map.proto\x12\x0c\x61pollo.hdmap\x1a&modules/map/proto/map_clear_area.proto\x1a%modules/map/proto/map_crosswalk.proto\x1a$modules/map/proto/map_junction.proto\x1a modules/map/proto/map_lane.proto\x1a#modules/map/proto/map_overlap.proto\x1a\"modules/map/proto/map_signal.proto\x1a&modules/map/proto/map_speed_bump.proto\x1a%modules/map/proto/map_stop_sign.proto\x1a&modules/map/proto/map_yield_sign.proto\x1a modules/map/proto/map_road.proto\x1a)modules/map/proto/map_parking_space.proto\x1a(modules/map/proto/map_pnc_junction.proto\x1a\x1fmodules/map/proto/map_rsu.proto\"\x1a\n\nProjection\x12\x0c\n\x04proj\x18\x01 \x01(\t\"\xeb\x01\n\x06Header\x12\x0f\n\x07version\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\x0c\x12,\n\nprojection\x18\x03 \x01(\x0b\x32\x18.apollo.hdmap.Projection\x12\x10\n\x08\x64istrict\x18\x04 \x01(\x0c\x12\x12\n\ngeneration\x18\x05 \x01(\x0c\x12\x11\n\trev_major\x18\x06 \x01(\x0c\x12\x11\n\trev_minor\x18\x07 \x01(\x0c\x12\x0c\n\x04left\x18\x08 \x01(\x01\x12\x0b\n\x03top\x18\t \x01(\x01\x12\r\n\x05right\x18\n \x01(\x01\x12\x0e\n\x06\x62ottom\x18\x0b \x01(\x01\x12\x0e\n\x06vendor\x18\x0c \x01(\x0c\"\xc4\x04\n\x03Map\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.apollo.hdmap.Header\x12*\n\tcrosswalk\x18\x02 \x03(\x0b\x32\x17.apollo.hdmap.Crosswalk\x12(\n\x08junction\x18\x03 \x03(\x0b\x32\x16.apollo.hdmap.Junction\x12 \n\x04lane\x18\x04 \x03(\x0b\x32\x12.apollo.hdmap.Lane\x12)\n\tstop_sign\x18\x05 \x03(\x0b\x32\x16.apollo.hdmap.StopSign\x12$\n\x06signal\x18\x06 \x03(\x0b\x32\x14.apollo.hdmap.Signal\x12&\n\x05yield\x18\x07 \x03(\x0b\x32\x17.apollo.hdmap.YieldSign\x12&\n\x07overlap\x18\x08 \x03(\x0b\x32\x15.apollo.hdmap.Overlap\x12+\n\nclear_area\x18\t \x03(\x0b\x32\x17.apollo.hdmap.ClearArea\x12+\n\nspeed_bump\x18\n \x03(\x0b\x32\x17.apollo.hdmap.SpeedBump\x12 \n\x04road\x18\x0b \x03(\x0b\x32\x12.apollo.hdmap.Road\x12\x31\n\rparking_space\x18\x0c \x03(\x0b\x32\x1a.apollo.hdmap.ParkingSpace\x12/\n\x0cpnc_junction\x18\r \x03(\x0b\x32\x19.apollo.hdmap.PNCJunction\x12\x1e\n\x03rsu\x18\x0e \x03(\x0b\x32\x11.apollo.hdmap.RSU')
  ,
  dependencies=[modules_dot_map_dot_proto_dot_map__clear__area__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__crosswalk__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__junction__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__lane__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__overlap__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__signal__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__speed__bump__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__stop__sign__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__yield__sign__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__road__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__parking__space__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__pnc__junction__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__rsu__pb2.DESCRIPTOR,])




_PROJECTION = _descriptor.Descriptor(
  name='Projection',
  full_name='apollo.hdmap.Projection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proj', full_name='apollo.hdmap.Projection.proj', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=540,
  serialized_end=566,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='apollo.hdmap.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='apollo.hdmap.Header.version', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='apollo.hdmap.Header.date', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='projection', full_name='apollo.hdmap.Header.projection', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='district', full_name='apollo.hdmap.Header.district', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generation', full_name='apollo.hdmap.Header.generation', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rev_major', full_name='apollo.hdmap.Header.rev_major', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rev_minor', full_name='apollo.hdmap.Header.rev_minor', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left', full_name='apollo.hdmap.Header.left', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top', full_name='apollo.hdmap.Header.top', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right', full_name='apollo.hdmap.Header.right', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='apollo.hdmap.Header.bottom', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vendor', full_name='apollo.hdmap.Header.vendor', index=11,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=569,
  serialized_end=804,
)


_MAP = _descriptor.Descriptor(
  name='Map',
  full_name='apollo.hdmap.Map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.hdmap.Map.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crosswalk', full_name='apollo.hdmap.Map.crosswalk', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='junction', full_name='apollo.hdmap.Map.junction', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane', full_name='apollo.hdmap.Map.lane', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_sign', full_name='apollo.hdmap.Map.stop_sign', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signal', full_name='apollo.hdmap.Map.signal', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yield', full_name='apollo.hdmap.Map.yield', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overlap', full_name='apollo.hdmap.Map.overlap', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clear_area', full_name='apollo.hdmap.Map.clear_area', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed_bump', full_name='apollo.hdmap.Map.speed_bump', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='road', full_name='apollo.hdmap.Map.road', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parking_space', full_name='apollo.hdmap.Map.parking_space', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pnc_junction', full_name='apollo.hdmap.Map.pnc_junction', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rsu', full_name='apollo.hdmap.Map.rsu', index=13,
      number=14, type=11, cpp_type=10, label=3,
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
  serialized_start=807,
  serialized_end=1387,
)

_HEADER.fields_by_name['projection'].message_type = _PROJECTION
_MAP.fields_by_name['header'].message_type = _HEADER
_MAP.fields_by_name['crosswalk'].message_type = modules_dot_map_dot_proto_dot_map__crosswalk__pb2._CROSSWALK
_MAP.fields_by_name['junction'].message_type = modules_dot_map_dot_proto_dot_map__junction__pb2._JUNCTION
_MAP.fields_by_name['lane'].message_type = modules_dot_map_dot_proto_dot_map__lane__pb2._LANE
_MAP.fields_by_name['stop_sign'].message_type = modules_dot_map_dot_proto_dot_map__stop__sign__pb2._STOPSIGN
_MAP.fields_by_name['signal'].message_type = modules_dot_map_dot_proto_dot_map__signal__pb2._SIGNAL
_MAP.fields_by_name['yield'].message_type = modules_dot_map_dot_proto_dot_map__yield__sign__pb2._YIELDSIGN
_MAP.fields_by_name['overlap'].message_type = modules_dot_map_dot_proto_dot_map__overlap__pb2._OVERLAP
_MAP.fields_by_name['clear_area'].message_type = modules_dot_map_dot_proto_dot_map__clear__area__pb2._CLEARAREA
_MAP.fields_by_name['speed_bump'].message_type = modules_dot_map_dot_proto_dot_map__speed__bump__pb2._SPEEDBUMP
_MAP.fields_by_name['road'].message_type = modules_dot_map_dot_proto_dot_map__road__pb2._ROAD
_MAP.fields_by_name['parking_space'].message_type = modules_dot_map_dot_proto_dot_map__parking__space__pb2._PARKINGSPACE
_MAP.fields_by_name['pnc_junction'].message_type = modules_dot_map_dot_proto_dot_map__pnc__junction__pb2._PNCJUNCTION
_MAP.fields_by_name['rsu'].message_type = modules_dot_map_dot_proto_dot_map__rsu__pb2._RSU
DESCRIPTOR.message_types_by_name['Projection'] = _PROJECTION
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Map'] = _MAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Projection = _reflection.GeneratedProtocolMessageType('Projection', (_message.Message,), dict(
  DESCRIPTOR = _PROJECTION,
  __module__ = 'modules.map.proto.map_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.Projection)
  ))
_sym_db.RegisterMessage(Projection)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'modules.map.proto.map_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.Header)
  ))
_sym_db.RegisterMessage(Header)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), dict(
  DESCRIPTOR = _MAP,
  __module__ = 'modules.map.proto.map_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.Map)
  ))
_sym_db.RegisterMessage(Map)


# @@protoc_insertion_point(module_scope)
