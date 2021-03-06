# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: beidoumessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='beidoumessage.proto',
  package='',
  serialized_pb='\n\x13\x62\x65idoumessage.proto\"\xf9\x01\n\rCommunication\x12\x13\n\x0bmessageform\x18\x01 \x01(\r\x12\x17\n\x0fmessagecategory\x18\x02 \x01(\r\x12\x12\n\nencryption\x18\x03 \x01(\r\x12\x10\n\x08sendaddr\x18\x04 \x01(\r\x12\x10\n\x08recvaddr\x18\x05 \x01(\r\x12\x15\n\rsendtime_hour\x18\x06 \x01(\r\x12\x17\n\x0fsendtime_minute\x18\x07 \x01(\r\x12\x17\n\x0fsendtime_second\x18\x08 \x01(\r\x12\x15\n\rmessagelength\x18\t \x01(\r\x12\x0b\n\x03key\x18\n \x01(\x0c\x12\x15\n\rmessagebuffer\x18\x0b \x01(\x0c\"\xe9\x03\n\x0cPositioninfo\x12\x0e\n\x06userid\x18\x01 \x01(\r\x12\x12\n\nencryption\x18\x02 \x01(\r\x12\x10\n\x08\x61\x63\x63uracy\x18\x03 \x01(\r\x12\x18\n\x10\x65mergencypostion\x18\x04 \x01(\r\x12\x1a\n\x12multivaluesolution\x18\x05 \x01(\r\x12\x0b\n\x03key\x18\x06 \x01(\x0c\x12\x16\n\x0e\x61pplytime_hour\x18\x07 \x01(\r\x12\x18\n\x10\x61pplytime_minute\x18\x08 \x01(\r\x12\x18\n\x10\x61pplytime_second\x18\t \x01(\r\x12\x18\n\x10\x61pplytime_tenths\x18\n \x01(\r\x12\x18\n\x10longitude_degree\x18\x0b \x01(\r\x12\x18\n\x10longitude_minute\x18\x0c \x01(\r\x12\x18\n\x10longitude_second\x18\r \x01(\r\x12\x18\n\x10longitude_tenths\x18\x0e \x01(\r\x12\x17\n\x0flatitude_degree\x18\x0f \x01(\r\x12\x17\n\x0flatitude_minute\x18\x10 \x01(\r\x12\x17\n\x0flatitude_second\x18\x11 \x01(\r\x12\x17\n\x0flatitude_tenths\x18\x12 \x01(\r\x12\x16\n\x0egeodeticheight\x18\x13 \x01(\x05\x12\x16\n\x0e\x64\x65tlaelevation\x18\x14 \x01(\x05\"\x8c\x01\n\x14\x43ommunicationreceipt\x12\x10\n\x08sendaddr\x18\x01 \x01(\r\x12\x10\n\x08recvaddr\x18\x02 \x01(\r\x12\x18\n\x10receipttime_hour\x18\x03 \x01(\r\x12\x1a\n\x12receipttime_minute\x18\x04 \x01(\r\x12\x1a\n\x12receipttime_second\x18\x05 \x01(\r\"\xa5\x01\n\rBeidoumessage\x12\x13\n\x0bmessagetype\x18\x01 \x01(\r\x12%\n\rcommuincation\x18\x02 \x01(\x0b\x32\x0e.Communication\x12\x33\n\x14\x63ommunicationreceipt\x18\x03 \x01(\x0b\x32\x15.Communicationreceipt\x12#\n\x0cpositioninfo\x18\x04 \x01(\x0b\x32\r.Positioninfo')




_COMMUNICATION = _descriptor.Descriptor(
  name='Communication',
  full_name='Communication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messageform', full_name='Communication.messageform', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='messagecategory', full_name='Communication.messagecategory', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encryption', full_name='Communication.encryption', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sendaddr', full_name='Communication.sendaddr', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recvaddr', full_name='Communication.recvaddr', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sendtime_hour', full_name='Communication.sendtime_hour', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sendtime_minute', full_name='Communication.sendtime_minute', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sendtime_second', full_name='Communication.sendtime_second', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='messagelength', full_name='Communication.messagelength', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='Communication.key', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='messagebuffer', full_name='Communication.messagebuffer', index=10,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=24,
  serialized_end=273,
)


_POSITIONINFO = _descriptor.Descriptor(
  name='Positioninfo',
  full_name='Positioninfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='Positioninfo.userid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encryption', full_name='Positioninfo.encryption', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='Positioninfo.accuracy', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='emergencypostion', full_name='Positioninfo.emergencypostion', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multivaluesolution', full_name='Positioninfo.multivaluesolution', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='Positioninfo.key', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applytime_hour', full_name='Positioninfo.applytime_hour', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applytime_minute', full_name='Positioninfo.applytime_minute', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applytime_second', full_name='Positioninfo.applytime_second', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applytime_tenths', full_name='Positioninfo.applytime_tenths', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude_degree', full_name='Positioninfo.longitude_degree', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude_minute', full_name='Positioninfo.longitude_minute', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude_second', full_name='Positioninfo.longitude_second', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude_tenths', full_name='Positioninfo.longitude_tenths', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude_degree', full_name='Positioninfo.latitude_degree', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude_minute', full_name='Positioninfo.latitude_minute', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude_second', full_name='Positioninfo.latitude_second', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude_tenths', full_name='Positioninfo.latitude_tenths', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='geodeticheight', full_name='Positioninfo.geodeticheight', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='detlaelevation', full_name='Positioninfo.detlaelevation', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=276,
  serialized_end=765,
)


_COMMUNICATIONRECEIPT = _descriptor.Descriptor(
  name='Communicationreceipt',
  full_name='Communicationreceipt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sendaddr', full_name='Communicationreceipt.sendaddr', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recvaddr', full_name='Communicationreceipt.recvaddr', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receipttime_hour', full_name='Communicationreceipt.receipttime_hour', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receipttime_minute', full_name='Communicationreceipt.receipttime_minute', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receipttime_second', full_name='Communicationreceipt.receipttime_second', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=768,
  serialized_end=908,
)


_BEIDOUMESSAGE = _descriptor.Descriptor(
  name='Beidoumessage',
  full_name='Beidoumessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messagetype', full_name='Beidoumessage.messagetype', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commuincation', full_name='Beidoumessage.commuincation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='communicationreceipt', full_name='Beidoumessage.communicationreceipt', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='positioninfo', full_name='Beidoumessage.positioninfo', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=911,
  serialized_end=1076,
)

_BEIDOUMESSAGE.fields_by_name['commuincation'].message_type = _COMMUNICATION
_BEIDOUMESSAGE.fields_by_name['communicationreceipt'].message_type = _COMMUNICATIONRECEIPT
_BEIDOUMESSAGE.fields_by_name['positioninfo'].message_type = _POSITIONINFO
DESCRIPTOR.message_types_by_name['Communication'] = _COMMUNICATION
DESCRIPTOR.message_types_by_name['Positioninfo'] = _POSITIONINFO
DESCRIPTOR.message_types_by_name['Communicationreceipt'] = _COMMUNICATIONRECEIPT
DESCRIPTOR.message_types_by_name['Beidoumessage'] = _BEIDOUMESSAGE

class Communication(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMUNICATION

  # @@protoc_insertion_point(class_scope:Communication)

class Positioninfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POSITIONINFO

  # @@protoc_insertion_point(class_scope:Positioninfo)

class Communicationreceipt(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMUNICATIONRECEIPT

  # @@protoc_insertion_point(class_scope:Communicationreceipt)

class Beidoumessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BEIDOUMESSAGE

  # @@protoc_insertion_point(class_scope:Beidoumessage)


# @@protoc_insertion_point(module_scope)
