# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: personBlueprint.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='personBlueprint.proto',
  package='persona',
  syntax='proto3',
  serialized_pb=_b('\n\x15personBlueprint.proto\x12\x07persona\"\xe7\x0c\n\x07Persona\x12\"\n\x04\x44NAs\x18\x01 \x03(\x0b\x32\x14.persona.Persona.DNA\x12\x10\n\x08physical\x18\x02 \x01(\t\x12!\n\x03\x61ge\x18\x03 \x01(\x0b\x32\x14.persona.Persona.Age\x1a\x89\x06\n\x03\x44NA\x12\x0b\n\x03\x44NA\x18\x01 \x01(\t\x12*\n\x06layers\x18\x03 \x03(\x0b\x32\x1a.persona.Persona.DNA.Layer\x12\x34\n\x0b\x63onnections\x18\x05 \x03(\x0b\x32\x1f.persona.Persona.DNA.Connection\x1a\xc9\x02\n\x05Layer\x12\x11\n\tlayerName\x18\x01 \x01(\t\x12,\n\tlayerSize\x18\x02 \x03(\x0b\x32\x19.persona.Persona.DNA.Size\x12\x34\n\x0b\x63onnections\x18\x03 \x03(\x0b\x32\x1f.persona.Persona.DNA.Connection\x12\x41\n\x10layerConvolution\x18\x06 \x01(\x0b\x32%.persona.Persona.DNA.LayerConvolutionH\x00\x12?\n\x0flayerActivation\x18\x07 \x01(\x0b\x32$.persona.Persona.DNA.LayerActivationH\x00\x12\x39\n\x0clayerDropout\x18\x08 \x01(\x0b\x32!.persona.Persona.DNA.LayerDropoutH\x00\x42\n\n\x08SubLayer\x1a}\n\x10LayerConvolution\x12\x1c\n\x14\x63onvolutionDimension\x18\x01 \x01(\x04\x12\x0f\n\x07\x66ilters\x18\x02 \x01(\x04\x12\x12\n\nkernelSize\x18\x03 \x03(\x04\x12\x12\n\nborderMode\x18\x04 \x01(\t\x12\x12\n\ninputShape\x18\x05 \x03(\x04\x1a)\n\x0fLayerActivation\x12\x16\n\x0e\x61\x63tivationType\x18\x01 \x01(\t\x1a&\n\x0cLayerDropout\x12\x16\n\x0e\x64ropPercentage\x18\x01 \x01(\x01\x1a\x43\n\nConnection\x12\x17\n\x0fsourceLayerName\x18\x01 \x01(\t\x12\x1c\n\x14\x64\x65stinationLayerName\x18\x02 \x01(\t\x1a\x30\n\x04Size\x12\x11\n\tdimension\x18\x01 \x01(\x04\x12\x15\n\rdimensionSize\x18\x02 \x01(\x04\x1ax\n\x03\x41ge\x12\x0b\n\x03old\x18\x01 \x01(\x04\x12\x15\n\rlearningCycle\x18\x02 \x01(\x04\x12\x19\n\x11learningBatchSize\x18\x03 \x01(\x04\x12\x32\n\x0c\x65nvironments\x18\x04 \x03(\x0b\x32\x1c.persona.Persona.Environment\x1a\xfc\x04\n\x0b\x45nvironment\x12\x0f\n\x07society\x18\x01 \x01(\t\x12\x35\n\x07library\x18\x02 \x01(\x0b\x32$.persona.Persona.Environment.Library\x1a\xa4\x04\n\x07Library\x12<\n\x07sources\x18\x01 \x03(\x0b\x32+.persona.Persona.Environment.Library.Source\x1a\xda\x03\n\x06Source\x12\x12\n\nsourceName\x18\x01 \x01(\t\x12\x1e\n\x16teachingDataPercentage\x18\x02 \x01(\x02\x12 \n\x18validationDataPercentage\x18\x03 \x01(\x02\x12\x1a\n\x12testDataPercentage\x18\x04 \x01(\x02\x12\x61\n\x16sourceConnectionLayers\x18\x05 \x03(\x0b\x32\x41.persona.Persona.Environment.Library.Source.SourceConnectionLayer\x1a\xfa\x01\n\x15SourceConnectionLayer\x12\x1a\n\x12\x63onnectedLayerName\x18\x06 \x01(\t\x12\x64\n\x0bimageSource\x18\x01 \x01(\x0b\x32M.persona.Persona.Environment.Library.Source.SourceConnectionLayer.ImageSourceH\x00\x1aL\n\x0bImageSource\x12\x12\n\nimageWidth\x18\x01 \x01(\x04\x12\x13\n\x0bimageHeight\x18\x02 \x01(\x04\x12\x14\n\x0cimageProcess\x18\x03 \x03(\tB\x11\n\x0fSourceParameterb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PERSONA_DNA_LAYER = _descriptor.Descriptor(
  name='Layer',
  full_name='persona.Persona.DNA.Layer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layerName', full_name='persona.Persona.DNA.Layer.layerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layerSize', full_name='persona.Persona.DNA.Layer.layerSize', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connections', full_name='persona.Persona.DNA.Layer.connections', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layerConvolution', full_name='persona.Persona.DNA.Layer.layerConvolution', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layerActivation', full_name='persona.Persona.DNA.Layer.layerActivation', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layerDropout', full_name='persona.Persona.DNA.Layer.layerDropout', index=5,
      number=8, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='SubLayer', full_name='persona.Persona.DNA.Layer.SubLayer',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=255,
  serialized_end=584,
)

_PERSONA_DNA_LAYERCONVOLUTION = _descriptor.Descriptor(
  name='LayerConvolution',
  full_name='persona.Persona.DNA.LayerConvolution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='convolutionDimension', full_name='persona.Persona.DNA.LayerConvolution.convolutionDimension', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filters', full_name='persona.Persona.DNA.LayerConvolution.filters', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kernelSize', full_name='persona.Persona.DNA.LayerConvolution.kernelSize', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='borderMode', full_name='persona.Persona.DNA.LayerConvolution.borderMode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputShape', full_name='persona.Persona.DNA.LayerConvolution.inputShape', index=4,
      number=5, type=4, cpp_type=4, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=586,
  serialized_end=711,
)

_PERSONA_DNA_LAYERACTIVATION = _descriptor.Descriptor(
  name='LayerActivation',
  full_name='persona.Persona.DNA.LayerActivation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activationType', full_name='persona.Persona.DNA.LayerActivation.activationType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=713,
  serialized_end=754,
)

_PERSONA_DNA_LAYERDROPOUT = _descriptor.Descriptor(
  name='LayerDropout',
  full_name='persona.Persona.DNA.LayerDropout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dropPercentage', full_name='persona.Persona.DNA.LayerDropout.dropPercentage', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=756,
  serialized_end=794,
)

_PERSONA_DNA_CONNECTION = _descriptor.Descriptor(
  name='Connection',
  full_name='persona.Persona.DNA.Connection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sourceLayerName', full_name='persona.Persona.DNA.Connection.sourceLayerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destinationLayerName', full_name='persona.Persona.DNA.Connection.destinationLayerName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=796,
  serialized_end=863,
)

_PERSONA_DNA_SIZE = _descriptor.Descriptor(
  name='Size',
  full_name='persona.Persona.DNA.Size',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dimension', full_name='persona.Persona.DNA.Size.dimension', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dimensionSize', full_name='persona.Persona.DNA.Size.dimensionSize', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=865,
  serialized_end=913,
)

_PERSONA_DNA = _descriptor.Descriptor(
  name='DNA',
  full_name='persona.Persona.DNA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='DNA', full_name='persona.Persona.DNA.DNA', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layers', full_name='persona.Persona.DNA.layers', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connections', full_name='persona.Persona.DNA.connections', index=2,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSONA_DNA_LAYER, _PERSONA_DNA_LAYERCONVOLUTION, _PERSONA_DNA_LAYERACTIVATION, _PERSONA_DNA_LAYERDROPOUT, _PERSONA_DNA_CONNECTION, _PERSONA_DNA_SIZE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=913,
)

_PERSONA_AGE = _descriptor.Descriptor(
  name='Age',
  full_name='persona.Persona.Age',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='old', full_name='persona.Persona.Age.old', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='learningCycle', full_name='persona.Persona.Age.learningCycle', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='learningBatchSize', full_name='persona.Persona.Age.learningBatchSize', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='environments', full_name='persona.Persona.Age.environments', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=915,
  serialized_end=1035,
)

_PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER_IMAGESOURCE = _descriptor.Descriptor(
  name='ImageSource',
  full_name='persona.Persona.Environment.Library.Source.SourceConnectionLayer.ImageSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='imageWidth', full_name='persona.Persona.Environment.Library.Source.SourceConnectionLayer.ImageSource.imageWidth', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageHeight', full_name='persona.Persona.Environment.Library.Source.SourceConnectionLayer.ImageSource.imageHeight', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageProcess', full_name='persona.Persona.Environment.Library.Source.SourceConnectionLayer.ImageSource.imageProcess', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1579,
  serialized_end=1655,
)

_PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER = _descriptor.Descriptor(
  name='SourceConnectionLayer',
  full_name='persona.Persona.Environment.Library.Source.SourceConnectionLayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connectedLayerName', full_name='persona.Persona.Environment.Library.Source.SourceConnectionLayer.connectedLayerName', index=0,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageSource', full_name='persona.Persona.Environment.Library.Source.SourceConnectionLayer.imageSource', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER_IMAGESOURCE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='SourceParameter', full_name='persona.Persona.Environment.Library.Source.SourceConnectionLayer.SourceParameter',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1424,
  serialized_end=1674,
)

_PERSONA_ENVIRONMENT_LIBRARY_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='persona.Persona.Environment.Library.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sourceName', full_name='persona.Persona.Environment.Library.Source.sourceName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='teachingDataPercentage', full_name='persona.Persona.Environment.Library.Source.teachingDataPercentage', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='validationDataPercentage', full_name='persona.Persona.Environment.Library.Source.validationDataPercentage', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='testDataPercentage', full_name='persona.Persona.Environment.Library.Source.testDataPercentage', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sourceConnectionLayers', full_name='persona.Persona.Environment.Library.Source.sourceConnectionLayers', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1200,
  serialized_end=1674,
)

_PERSONA_ENVIRONMENT_LIBRARY = _descriptor.Descriptor(
  name='Library',
  full_name='persona.Persona.Environment.Library',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sources', full_name='persona.Persona.Environment.Library.sources', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSONA_ENVIRONMENT_LIBRARY_SOURCE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1126,
  serialized_end=1674,
)

_PERSONA_ENVIRONMENT = _descriptor.Descriptor(
  name='Environment',
  full_name='persona.Persona.Environment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='society', full_name='persona.Persona.Environment.society', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='library', full_name='persona.Persona.Environment.library', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSONA_ENVIRONMENT_LIBRARY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1038,
  serialized_end=1674,
)

_PERSONA = _descriptor.Descriptor(
  name='Persona',
  full_name='persona.Persona',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='DNAs', full_name='persona.Persona.DNAs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='physical', full_name='persona.Persona.physical', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='age', full_name='persona.Persona.age', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSONA_DNA, _PERSONA_AGE, _PERSONA_ENVIRONMENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=1674,
)

_PERSONA_DNA_LAYER.fields_by_name['layerSize'].message_type = _PERSONA_DNA_SIZE
_PERSONA_DNA_LAYER.fields_by_name['connections'].message_type = _PERSONA_DNA_CONNECTION
_PERSONA_DNA_LAYER.fields_by_name['layerConvolution'].message_type = _PERSONA_DNA_LAYERCONVOLUTION
_PERSONA_DNA_LAYER.fields_by_name['layerActivation'].message_type = _PERSONA_DNA_LAYERACTIVATION
_PERSONA_DNA_LAYER.fields_by_name['layerDropout'].message_type = _PERSONA_DNA_LAYERDROPOUT
_PERSONA_DNA_LAYER.containing_type = _PERSONA_DNA
_PERSONA_DNA_LAYER.oneofs_by_name['SubLayer'].fields.append(
  _PERSONA_DNA_LAYER.fields_by_name['layerConvolution'])
_PERSONA_DNA_LAYER.fields_by_name['layerConvolution'].containing_oneof = _PERSONA_DNA_LAYER.oneofs_by_name['SubLayer']
_PERSONA_DNA_LAYER.oneofs_by_name['SubLayer'].fields.append(
  _PERSONA_DNA_LAYER.fields_by_name['layerActivation'])
_PERSONA_DNA_LAYER.fields_by_name['layerActivation'].containing_oneof = _PERSONA_DNA_LAYER.oneofs_by_name['SubLayer']
_PERSONA_DNA_LAYER.oneofs_by_name['SubLayer'].fields.append(
  _PERSONA_DNA_LAYER.fields_by_name['layerDropout'])
_PERSONA_DNA_LAYER.fields_by_name['layerDropout'].containing_oneof = _PERSONA_DNA_LAYER.oneofs_by_name['SubLayer']
_PERSONA_DNA_LAYERCONVOLUTION.containing_type = _PERSONA_DNA
_PERSONA_DNA_LAYERACTIVATION.containing_type = _PERSONA_DNA
_PERSONA_DNA_LAYERDROPOUT.containing_type = _PERSONA_DNA
_PERSONA_DNA_CONNECTION.containing_type = _PERSONA_DNA
_PERSONA_DNA_SIZE.containing_type = _PERSONA_DNA
_PERSONA_DNA.fields_by_name['layers'].message_type = _PERSONA_DNA_LAYER
_PERSONA_DNA.fields_by_name['connections'].message_type = _PERSONA_DNA_CONNECTION
_PERSONA_DNA.containing_type = _PERSONA
_PERSONA_AGE.fields_by_name['environments'].message_type = _PERSONA_ENVIRONMENT
_PERSONA_AGE.containing_type = _PERSONA
_PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER_IMAGESOURCE.containing_type = _PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER
_PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER.fields_by_name['imageSource'].message_type = _PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER_IMAGESOURCE
_PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER.containing_type = _PERSONA_ENVIRONMENT_LIBRARY_SOURCE
_PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER.oneofs_by_name['SourceParameter'].fields.append(
  _PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER.fields_by_name['imageSource'])
_PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER.fields_by_name['imageSource'].containing_oneof = _PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER.oneofs_by_name['SourceParameter']
_PERSONA_ENVIRONMENT_LIBRARY_SOURCE.fields_by_name['sourceConnectionLayers'].message_type = _PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER
_PERSONA_ENVIRONMENT_LIBRARY_SOURCE.containing_type = _PERSONA_ENVIRONMENT_LIBRARY
_PERSONA_ENVIRONMENT_LIBRARY.fields_by_name['sources'].message_type = _PERSONA_ENVIRONMENT_LIBRARY_SOURCE
_PERSONA_ENVIRONMENT_LIBRARY.containing_type = _PERSONA_ENVIRONMENT
_PERSONA_ENVIRONMENT.fields_by_name['library'].message_type = _PERSONA_ENVIRONMENT_LIBRARY
_PERSONA_ENVIRONMENT.containing_type = _PERSONA
_PERSONA.fields_by_name['DNAs'].message_type = _PERSONA_DNA
_PERSONA.fields_by_name['age'].message_type = _PERSONA_AGE
DESCRIPTOR.message_types_by_name['Persona'] = _PERSONA

Persona = _reflection.GeneratedProtocolMessageType('Persona', (_message.Message,), dict(

  DNA = _reflection.GeneratedProtocolMessageType('DNA', (_message.Message,), dict(

    Layer = _reflection.GeneratedProtocolMessageType('Layer', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_LAYER,
      __module__ = 'personBlueprint_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.Layer)
      ))
    ,

    LayerConvolution = _reflection.GeneratedProtocolMessageType('LayerConvolution', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_LAYERCONVOLUTION,
      __module__ = 'personBlueprint_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.LayerConvolution)
      ))
    ,

    LayerActivation = _reflection.GeneratedProtocolMessageType('LayerActivation', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_LAYERACTIVATION,
      __module__ = 'personBlueprint_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.LayerActivation)
      ))
    ,

    LayerDropout = _reflection.GeneratedProtocolMessageType('LayerDropout', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_LAYERDROPOUT,
      __module__ = 'personBlueprint_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.LayerDropout)
      ))
    ,

    Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_CONNECTION,
      __module__ = 'personBlueprint_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.Connection)
      ))
    ,

    Size = _reflection.GeneratedProtocolMessageType('Size', (_message.Message,), dict(
      DESCRIPTOR = _PERSONA_DNA_SIZE,
      __module__ = 'personBlueprint_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.DNA.Size)
      ))
    ,
    DESCRIPTOR = _PERSONA_DNA,
    __module__ = 'personBlueprint_pb2'
    # @@protoc_insertion_point(class_scope:persona.Persona.DNA)
    ))
  ,

  Age = _reflection.GeneratedProtocolMessageType('Age', (_message.Message,), dict(
    DESCRIPTOR = _PERSONA_AGE,
    __module__ = 'personBlueprint_pb2'
    # @@protoc_insertion_point(class_scope:persona.Persona.Age)
    ))
  ,

  Environment = _reflection.GeneratedProtocolMessageType('Environment', (_message.Message,), dict(

    Library = _reflection.GeneratedProtocolMessageType('Library', (_message.Message,), dict(

      Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), dict(

        SourceConnectionLayer = _reflection.GeneratedProtocolMessageType('SourceConnectionLayer', (_message.Message,), dict(

          ImageSource = _reflection.GeneratedProtocolMessageType('ImageSource', (_message.Message,), dict(
            DESCRIPTOR = _PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER_IMAGESOURCE,
            __module__ = 'personBlueprint_pb2'
            # @@protoc_insertion_point(class_scope:persona.Persona.Environment.Library.Source.SourceConnectionLayer.ImageSource)
            ))
          ,
          DESCRIPTOR = _PERSONA_ENVIRONMENT_LIBRARY_SOURCE_SOURCECONNECTIONLAYER,
          __module__ = 'personBlueprint_pb2'
          # @@protoc_insertion_point(class_scope:persona.Persona.Environment.Library.Source.SourceConnectionLayer)
          ))
        ,
        DESCRIPTOR = _PERSONA_ENVIRONMENT_LIBRARY_SOURCE,
        __module__ = 'personBlueprint_pb2'
        # @@protoc_insertion_point(class_scope:persona.Persona.Environment.Library.Source)
        ))
      ,
      DESCRIPTOR = _PERSONA_ENVIRONMENT_LIBRARY,
      __module__ = 'personBlueprint_pb2'
      # @@protoc_insertion_point(class_scope:persona.Persona.Environment.Library)
      ))
    ,
    DESCRIPTOR = _PERSONA_ENVIRONMENT,
    __module__ = 'personBlueprint_pb2'
    # @@protoc_insertion_point(class_scope:persona.Persona.Environment)
    ))
  ,
  DESCRIPTOR = _PERSONA,
  __module__ = 'personBlueprint_pb2'
  # @@protoc_insertion_point(class_scope:persona.Persona)
  ))
_sym_db.RegisterMessage(Persona)
_sym_db.RegisterMessage(Persona.DNA)
_sym_db.RegisterMessage(Persona.DNA.Layer)
_sym_db.RegisterMessage(Persona.DNA.LayerConvolution)
_sym_db.RegisterMessage(Persona.DNA.LayerActivation)
_sym_db.RegisterMessage(Persona.DNA.LayerDropout)
_sym_db.RegisterMessage(Persona.DNA.Connection)
_sym_db.RegisterMessage(Persona.DNA.Size)
_sym_db.RegisterMessage(Persona.Age)
_sym_db.RegisterMessage(Persona.Environment)
_sym_db.RegisterMessage(Persona.Environment.Library)
_sym_db.RegisterMessage(Persona.Environment.Library.Source)
_sym_db.RegisterMessage(Persona.Environment.Library.Source.SourceConnectionLayer)
_sym_db.RegisterMessage(Persona.Environment.Library.Source.SourceConnectionLayer.ImageSource)


# @@protoc_insertion_point(module_scope)
