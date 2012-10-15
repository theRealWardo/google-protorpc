# Generated by the protocol buffer compiler.  DO NOT EDIT!

from libs.google.protobuf import descriptor
from libs.google.protobuf import message
from libs.google.protobuf import reflection
from libs.google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='protorpc/protorpc_test.proto',
  package='protorpc',
  serialized_pb='\n\x1cprotorpc/protorpc_test.proto\x12\x08protorpc\" \n\rNestedMessage\x12\x0f\n\x07\x61_value\x18\x01 \x02(\t\"m\n\x10HasNestedMessage\x12\'\n\x06nested\x18\x01 \x01(\x0b\x32\x17.protorpc.NestedMessage\x12\x30\n\x0frepeated_nested\x18\x02 \x03(\x0b\x32\x17.protorpc.NestedMessage\"(\n\nHasDefault\x12\x1a\n\x07\x61_value\x18\x01 \x01(\t:\ta default\"\x97\x02\n\x0fOptionalMessage\x12\x14\n\x0c\x64ouble_value\x18\x01 \x01(\x01\x12\x13\n\x0b\x66loat_value\x18\x02 \x01(\x02\x12\x13\n\x0bint64_value\x18\x03 \x01(\x03\x12\x14\n\x0cuint64_value\x18\x04 \x01(\x04\x12\x13\n\x0bint32_value\x18\x05 \x01(\x05\x12\x12\n\nbool_value\x18\x06 \x01(\x08\x12\x14\n\x0cstring_value\x18\x07 \x01(\t\x12\x13\n\x0b\x62ytes_value\x18\x08 \x01(\x0c\x12\x38\n\nenum_value\x18\n \x01(\x0e\x32$.protorpc.OptionalMessage.SimpleEnum\" \n\nSimpleEnum\x12\x08\n\x04VAL1\x10\x01\x12\x08\n\x04VAL2\x10\x02\"\x97\x02\n\x0fRepeatedMessage\x12\x14\n\x0c\x64ouble_value\x18\x01 \x03(\x01\x12\x13\n\x0b\x66loat_value\x18\x02 \x03(\x02\x12\x13\n\x0bint64_value\x18\x03 \x03(\x03\x12\x14\n\x0cuint64_value\x18\x04 \x03(\x04\x12\x13\n\x0bint32_value\x18\x05 \x03(\x05\x12\x12\n\nbool_value\x18\x06 \x03(\x08\x12\x14\n\x0cstring_value\x18\x07 \x03(\t\x12\x13\n\x0b\x62ytes_value\x18\x08 \x03(\x0c\x12\x38\n\nenum_value\x18\n \x03(\x0e\x32$.protorpc.RepeatedMessage.SimpleEnum\" \n\nSimpleEnum\x12\x08\n\x04VAL1\x10\x01\x12\x08\n\x04VAL2\x10\x02\"y\n\x18HasOptionalNestedMessage\x12)\n\x06nested\x18\x01 \x01(\x0b\x32\x19.protorpc.OptionalMessage\x12\x32\n\x0frepeated_nested\x18\x02 \x03(\x0b\x32\x19.protorpc.OptionalMessage')



_OPTIONALMESSAGE_SIMPLEENUM = descriptor.EnumDescriptor(
  name='SimpleEnum',
  full_name='protorpc.OptionalMessage.SimpleEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='VAL1', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='VAL2', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=477,
  serialized_end=509,
)

_REPEATEDMESSAGE_SIMPLEENUM = descriptor.EnumDescriptor(
  name='SimpleEnum',
  full_name='protorpc.RepeatedMessage.SimpleEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='VAL1', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='VAL2', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=477,
  serialized_end=509,
)


_NESTEDMESSAGE = descriptor.Descriptor(
  name='NestedMessage',
  full_name='protorpc.NestedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='a_value', full_name='protorpc.NestedMessage.a_value', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=42,
  serialized_end=74,
)


_HASNESTEDMESSAGE = descriptor.Descriptor(
  name='HasNestedMessage',
  full_name='protorpc.HasNestedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='nested', full_name='protorpc.HasNestedMessage.nested', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='repeated_nested', full_name='protorpc.HasNestedMessage.repeated_nested', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=76,
  serialized_end=185,
)


_HASDEFAULT = descriptor.Descriptor(
  name='HasDefault',
  full_name='protorpc.HasDefault',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='a_value', full_name='protorpc.HasDefault.a_value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("a default", "utf-8"),
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
  serialized_start=187,
  serialized_end=227,
)


_OPTIONALMESSAGE = descriptor.Descriptor(
  name='OptionalMessage',
  full_name='protorpc.OptionalMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='double_value', full_name='protorpc.OptionalMessage.double_value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='float_value', full_name='protorpc.OptionalMessage.float_value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='int64_value', full_name='protorpc.OptionalMessage.int64_value', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='uint64_value', full_name='protorpc.OptionalMessage.uint64_value', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='int32_value', full_name='protorpc.OptionalMessage.int32_value', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bool_value', full_name='protorpc.OptionalMessage.bool_value', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='string_value', full_name='protorpc.OptionalMessage.string_value', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bytes_value', full_name='protorpc.OptionalMessage.bytes_value', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enum_value', full_name='protorpc.OptionalMessage.enum_value', index=8,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OPTIONALMESSAGE_SIMPLEENUM,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=230,
  serialized_end=509,
)


_REPEATEDMESSAGE = descriptor.Descriptor(
  name='RepeatedMessage',
  full_name='protorpc.RepeatedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='double_value', full_name='protorpc.RepeatedMessage.double_value', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='float_value', full_name='protorpc.RepeatedMessage.float_value', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='int64_value', full_name='protorpc.RepeatedMessage.int64_value', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='uint64_value', full_name='protorpc.RepeatedMessage.uint64_value', index=3,
      number=4, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='int32_value', full_name='protorpc.RepeatedMessage.int32_value', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bool_value', full_name='protorpc.RepeatedMessage.bool_value', index=5,
      number=6, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='string_value', full_name='protorpc.RepeatedMessage.string_value', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bytes_value', full_name='protorpc.RepeatedMessage.bytes_value', index=7,
      number=8, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enum_value', full_name='protorpc.RepeatedMessage.enum_value', index=8,
      number=10, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REPEATEDMESSAGE_SIMPLEENUM,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=512,
  serialized_end=791,
)


_HASOPTIONALNESTEDMESSAGE = descriptor.Descriptor(
  name='HasOptionalNestedMessage',
  full_name='protorpc.HasOptionalNestedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='nested', full_name='protorpc.HasOptionalNestedMessage.nested', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='repeated_nested', full_name='protorpc.HasOptionalNestedMessage.repeated_nested', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=793,
  serialized_end=914,
)


_HASNESTEDMESSAGE.fields_by_name['nested'].message_type = _NESTEDMESSAGE
_HASNESTEDMESSAGE.fields_by_name['repeated_nested'].message_type = _NESTEDMESSAGE
_OPTIONALMESSAGE.fields_by_name['enum_value'].enum_type = _OPTIONALMESSAGE_SIMPLEENUM
_OPTIONALMESSAGE_SIMPLEENUM.containing_type = _OPTIONALMESSAGE;
_REPEATEDMESSAGE.fields_by_name['enum_value'].enum_type = _REPEATEDMESSAGE_SIMPLEENUM
_REPEATEDMESSAGE_SIMPLEENUM.containing_type = _REPEATEDMESSAGE;
_HASOPTIONALNESTEDMESSAGE.fields_by_name['nested'].message_type = _OPTIONALMESSAGE
_HASOPTIONALNESTEDMESSAGE.fields_by_name['repeated_nested'].message_type = _OPTIONALMESSAGE

class NestedMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NESTEDMESSAGE

  # @@protoc_insertion_point(class_scope:protorpc.NestedMessage)

class HasNestedMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HASNESTEDMESSAGE

  # @@protoc_insertion_point(class_scope:protorpc.HasNestedMessage)

class HasDefault(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HASDEFAULT

  # @@protoc_insertion_point(class_scope:protorpc.HasDefault)

class OptionalMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPTIONALMESSAGE

  # @@protoc_insertion_point(class_scope:protorpc.OptionalMessage)

class RepeatedMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REPEATEDMESSAGE

  # @@protoc_insertion_point(class_scope:protorpc.RepeatedMessage)

class HasOptionalNestedMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HASOPTIONALNESTEDMESSAGE

  # @@protoc_insertion_point(class_scope:protorpc.HasOptionalNestedMessage)

# @@protoc_insertion_point(module_scope)
