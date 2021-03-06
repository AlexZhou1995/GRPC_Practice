# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DisStorage.proto

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
  name='DisStorage.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x44isStorage.proto\"1\n\x07usrInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02pw\x18\x02 \x01(\t\x12\x0c\n\x04mess\x18\x03 \x01(\t\"K\n\tloginInfo\x12\x11\n\tloginFlag\x18\x01 \x01(\x05\x12\n\n\x02IP\x18\x02 \x01(\t\x12\x11\n\taccessNum\x18\x03 \x01(\x05\x12\x0c\n\x04mess\x18\x04 \x01(\t\".\n\nlogoutInfo\x12\x12\n\nlogoutFlag\x18\x01 \x01(\x05\x12\x0c\n\x04mess\x18\x02 \x01(\t\";\n\x08\x66ileList\x12\x0f\n\x07\x66ileNum\x18\x01 \x01(\x05\x12\x10\n\x08nameList\x18\x02 \x03(\t\x12\x0c\n\x04mess\x18\x03 \x01(\t\"\\\n\x08\x66ileData\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\x12\r\n\x05\x62lock\x18\x02 \x01(\x0c\x12\x10\n\x08\x62lockNum\x18\x03 \x01(\x05\x12\x0f\n\x07usrName\x18\x04 \x01(\t\x12\x0c\n\x04mess\x18\x05 \x01(\t\"M\n\x08\x66ileInfo\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\x12\x10\n\x08\x62lockNum\x18\x02 \x01(\x05\x12\x0f\n\x07usrName\x18\x03 \x01(\t\x12\x0c\n\x04mess\x18\x04 \x01(\t\"\x18\n\x08nodeInfo\x12\x0c\n\x04mess\x18\x01 \x01(\t\"\'\n\tnodeState\x12\x0c\n\x04usrs\x18\x01 \x03(\t\x12\x0c\n\x04mess\x18\x02 \x01(\t2\xf1\x01\n\tDisServer\x12\"\n\x08usrLogin\x12\x08.usrInfo\x1a\n.loginInfo\"\x00\x12$\n\tusrLogout\x12\x08.usrInfo\x1a\x0b.logoutInfo\"\x00\x12$\n\x0bgetFileList\x12\x08.usrInfo\x1a\t.fileList\"\x00\x12&\n\nuploadFile\x12\t.fileData\x1a\t.fileInfo\"\x00(\x01\x12(\n\x0c\x64ownloadFile\x12\t.fileInfo\x1a\t.fileData\"\x00\x30\x01\x12\"\n\x08getState\x12\x08.usrInfo\x1a\n.nodeState\"\x00\x32\xf3\x01\n\tCtrServer\x12\"\n\x08usrLogin\x12\x08.usrInfo\x1a\n.loginInfo\"\x00\x12$\n\tusrLogout\x12\x08.usrInfo\x1a\x0b.logoutInfo\"\x00\x12$\n\x0bgetFileList\x12\x08.usrInfo\x1a\t.fileList\"\x00\x12&\n\nuploadFile\x12\t.fileData\x1a\t.fileInfo\"\x00(\x01\x12(\n\x0c\x64ownloadFile\x12\t.fileInfo\x1a\t.fileData\"\x00\x30\x01\x12$\n\x0bgetNodeInfo\x12\x08.usrInfo\x1a\t.nodeInfo\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_USRINFO = _descriptor.Descriptor(
  name='usrInfo',
  full_name='usrInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='usrInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pw', full_name='usrInfo.pw', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mess', full_name='usrInfo.mess', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=20,
  serialized_end=69,
)


_LOGININFO = _descriptor.Descriptor(
  name='loginInfo',
  full_name='loginInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='loginFlag', full_name='loginInfo.loginFlag', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IP', full_name='loginInfo.IP', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accessNum', full_name='loginInfo.accessNum', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mess', full_name='loginInfo.mess', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=71,
  serialized_end=146,
)


_LOGOUTINFO = _descriptor.Descriptor(
  name='logoutInfo',
  full_name='logoutInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='logoutFlag', full_name='logoutInfo.logoutFlag', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mess', full_name='logoutInfo.mess', index=1,
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
  serialized_start=148,
  serialized_end=194,
)


_FILELIST = _descriptor.Descriptor(
  name='fileList',
  full_name='fileList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileNum', full_name='fileList.fileNum', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nameList', full_name='fileList.nameList', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mess', full_name='fileList.mess', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=196,
  serialized_end=255,
)


_FILEDATA = _descriptor.Descriptor(
  name='fileData',
  full_name='fileData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileName', full_name='fileData.fileName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='block', full_name='fileData.block', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blockNum', full_name='fileData.blockNum', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usrName', full_name='fileData.usrName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mess', full_name='fileData.mess', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=257,
  serialized_end=349,
)


_FILEINFO = _descriptor.Descriptor(
  name='fileInfo',
  full_name='fileInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileName', full_name='fileInfo.fileName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blockNum', full_name='fileInfo.blockNum', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usrName', full_name='fileInfo.usrName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mess', full_name='fileInfo.mess', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=351,
  serialized_end=428,
)


_NODEINFO = _descriptor.Descriptor(
  name='nodeInfo',
  full_name='nodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mess', full_name='nodeInfo.mess', index=0,
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
  serialized_start=430,
  serialized_end=454,
)


_NODESTATE = _descriptor.Descriptor(
  name='nodeState',
  full_name='nodeState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='usrs', full_name='nodeState.usrs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mess', full_name='nodeState.mess', index=1,
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
  serialized_start=456,
  serialized_end=495,
)

DESCRIPTOR.message_types_by_name['usrInfo'] = _USRINFO
DESCRIPTOR.message_types_by_name['loginInfo'] = _LOGININFO
DESCRIPTOR.message_types_by_name['logoutInfo'] = _LOGOUTINFO
DESCRIPTOR.message_types_by_name['fileList'] = _FILELIST
DESCRIPTOR.message_types_by_name['fileData'] = _FILEDATA
DESCRIPTOR.message_types_by_name['fileInfo'] = _FILEINFO
DESCRIPTOR.message_types_by_name['nodeInfo'] = _NODEINFO
DESCRIPTOR.message_types_by_name['nodeState'] = _NODESTATE

usrInfo = _reflection.GeneratedProtocolMessageType('usrInfo', (_message.Message,), dict(
  DESCRIPTOR = _USRINFO,
  __module__ = 'DisStorage_pb2'
  # @@protoc_insertion_point(class_scope:usrInfo)
  ))
_sym_db.RegisterMessage(usrInfo)

loginInfo = _reflection.GeneratedProtocolMessageType('loginInfo', (_message.Message,), dict(
  DESCRIPTOR = _LOGININFO,
  __module__ = 'DisStorage_pb2'
  # @@protoc_insertion_point(class_scope:loginInfo)
  ))
_sym_db.RegisterMessage(loginInfo)

logoutInfo = _reflection.GeneratedProtocolMessageType('logoutInfo', (_message.Message,), dict(
  DESCRIPTOR = _LOGOUTINFO,
  __module__ = 'DisStorage_pb2'
  # @@protoc_insertion_point(class_scope:logoutInfo)
  ))
_sym_db.RegisterMessage(logoutInfo)

fileList = _reflection.GeneratedProtocolMessageType('fileList', (_message.Message,), dict(
  DESCRIPTOR = _FILELIST,
  __module__ = 'DisStorage_pb2'
  # @@protoc_insertion_point(class_scope:fileList)
  ))
_sym_db.RegisterMessage(fileList)

fileData = _reflection.GeneratedProtocolMessageType('fileData', (_message.Message,), dict(
  DESCRIPTOR = _FILEDATA,
  __module__ = 'DisStorage_pb2'
  # @@protoc_insertion_point(class_scope:fileData)
  ))
_sym_db.RegisterMessage(fileData)

fileInfo = _reflection.GeneratedProtocolMessageType('fileInfo', (_message.Message,), dict(
  DESCRIPTOR = _FILEINFO,
  __module__ = 'DisStorage_pb2'
  # @@protoc_insertion_point(class_scope:fileInfo)
  ))
_sym_db.RegisterMessage(fileInfo)

nodeInfo = _reflection.GeneratedProtocolMessageType('nodeInfo', (_message.Message,), dict(
  DESCRIPTOR = _NODEINFO,
  __module__ = 'DisStorage_pb2'
  # @@protoc_insertion_point(class_scope:nodeInfo)
  ))
_sym_db.RegisterMessage(nodeInfo)

nodeState = _reflection.GeneratedProtocolMessageType('nodeState', (_message.Message,), dict(
  DESCRIPTOR = _NODESTATE,
  __module__ = 'DisStorage_pb2'
  # @@protoc_insertion_point(class_scope:nodeState)
  ))
_sym_db.RegisterMessage(nodeState)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class DisServerStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.usrLogin = channel.unary_unary(
        '/DisServer/usrLogin',
        request_serializer=usrInfo.SerializeToString,
        response_deserializer=loginInfo.FromString,
        )
    self.usrLogout = channel.unary_unary(
        '/DisServer/usrLogout',
        request_serializer=usrInfo.SerializeToString,
        response_deserializer=logoutInfo.FromString,
        )
    self.getFileList = channel.unary_unary(
        '/DisServer/getFileList',
        request_serializer=usrInfo.SerializeToString,
        response_deserializer=fileList.FromString,
        )
    self.uploadFile = channel.stream_unary(
        '/DisServer/uploadFile',
        request_serializer=fileData.SerializeToString,
        response_deserializer=fileInfo.FromString,
        )
    self.downloadFile = channel.unary_stream(
        '/DisServer/downloadFile',
        request_serializer=fileInfo.SerializeToString,
        response_deserializer=fileData.FromString,
        )
    self.getState = channel.unary_unary(
        '/DisServer/getState',
        request_serializer=usrInfo.SerializeToString,
        response_deserializer=nodeState.FromString,
        )


class DisServerServicer(object):

  def usrLogin(self, request, context):
    """User login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def usrLogout(self, request, context):
    """logout
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getFileList(self, request, context):
    """get all file names
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def uploadFile(self, request_iterator, context):
    """upload
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def downloadFile(self, request, context):
    """download
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getState(self, request, context):
    """getNodeState
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DisServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'usrLogin': grpc.unary_unary_rpc_method_handler(
          servicer.usrLogin,
          request_deserializer=usrInfo.FromString,
          response_serializer=loginInfo.SerializeToString,
      ),
      'usrLogout': grpc.unary_unary_rpc_method_handler(
          servicer.usrLogout,
          request_deserializer=usrInfo.FromString,
          response_serializer=logoutInfo.SerializeToString,
      ),
      'getFileList': grpc.unary_unary_rpc_method_handler(
          servicer.getFileList,
          request_deserializer=usrInfo.FromString,
          response_serializer=fileList.SerializeToString,
      ),
      'uploadFile': grpc.stream_unary_rpc_method_handler(
          servicer.uploadFile,
          request_deserializer=fileData.FromString,
          response_serializer=fileInfo.SerializeToString,
      ),
      'downloadFile': grpc.unary_stream_rpc_method_handler(
          servicer.downloadFile,
          request_deserializer=fileInfo.FromString,
          response_serializer=fileData.SerializeToString,
      ),
      'getState': grpc.unary_unary_rpc_method_handler(
          servicer.getState,
          request_deserializer=usrInfo.FromString,
          response_serializer=nodeState.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'DisServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaDisServerServicer(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def usrLogin(self, request, context):
    """User login
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def usrLogout(self, request, context):
    """logout
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getFileList(self, request, context):
    """get all file names
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def uploadFile(self, request_iterator, context):
    """upload
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def downloadFile(self, request, context):
    """download
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getState(self, request, context):
    """getNodeState
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaDisServerStub(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def usrLogin(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """User login
    """
    raise NotImplementedError()
  usrLogin.future = None
  def usrLogout(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """logout
    """
    raise NotImplementedError()
  usrLogout.future = None
  def getFileList(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """get all file names
    """
    raise NotImplementedError()
  getFileList.future = None
  def uploadFile(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
    """upload
    """
    raise NotImplementedError()
  uploadFile.future = None
  def downloadFile(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """download
    """
    raise NotImplementedError()
  def getState(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """getNodeState
    """
    raise NotImplementedError()
  getState.future = None


def beta_create_DisServer_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_deserializers = {
    ('DisServer', 'downloadFile'): fileInfo.FromString,
    ('DisServer', 'getFileList'): usrInfo.FromString,
    ('DisServer', 'getState'): usrInfo.FromString,
    ('DisServer', 'uploadFile'): fileData.FromString,
    ('DisServer', 'usrLogin'): usrInfo.FromString,
    ('DisServer', 'usrLogout'): usrInfo.FromString,
  }
  response_serializers = {
    ('DisServer', 'downloadFile'): fileData.SerializeToString,
    ('DisServer', 'getFileList'): fileList.SerializeToString,
    ('DisServer', 'getState'): nodeState.SerializeToString,
    ('DisServer', 'uploadFile'): fileInfo.SerializeToString,
    ('DisServer', 'usrLogin'): loginInfo.SerializeToString,
    ('DisServer', 'usrLogout'): logoutInfo.SerializeToString,
  }
  method_implementations = {
    ('DisServer', 'downloadFile'): face_utilities.unary_stream_inline(servicer.downloadFile),
    ('DisServer', 'getFileList'): face_utilities.unary_unary_inline(servicer.getFileList),
    ('DisServer', 'getState'): face_utilities.unary_unary_inline(servicer.getState),
    ('DisServer', 'uploadFile'): face_utilities.stream_unary_inline(servicer.uploadFile),
    ('DisServer', 'usrLogin'): face_utilities.unary_unary_inline(servicer.usrLogin),
    ('DisServer', 'usrLogout'): face_utilities.unary_unary_inline(servicer.usrLogout),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_DisServer_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_serializers = {
    ('DisServer', 'downloadFile'): fileInfo.SerializeToString,
    ('DisServer', 'getFileList'): usrInfo.SerializeToString,
    ('DisServer', 'getState'): usrInfo.SerializeToString,
    ('DisServer', 'uploadFile'): fileData.SerializeToString,
    ('DisServer', 'usrLogin'): usrInfo.SerializeToString,
    ('DisServer', 'usrLogout'): usrInfo.SerializeToString,
  }
  response_deserializers = {
    ('DisServer', 'downloadFile'): fileData.FromString,
    ('DisServer', 'getFileList'): fileList.FromString,
    ('DisServer', 'getState'): nodeState.FromString,
    ('DisServer', 'uploadFile'): fileInfo.FromString,
    ('DisServer', 'usrLogin'): loginInfo.FromString,
    ('DisServer', 'usrLogout'): logoutInfo.FromString,
  }
  cardinalities = {
    'downloadFile': cardinality.Cardinality.UNARY_STREAM,
    'getFileList': cardinality.Cardinality.UNARY_UNARY,
    'getState': cardinality.Cardinality.UNARY_UNARY,
    'uploadFile': cardinality.Cardinality.STREAM_UNARY,
    'usrLogin': cardinality.Cardinality.UNARY_UNARY,
    'usrLogout': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'DisServer', cardinalities, options=stub_options)


class CtrServerStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.usrLogin = channel.unary_unary(
        '/CtrServer/usrLogin',
        request_serializer=usrInfo.SerializeToString,
        response_deserializer=loginInfo.FromString,
        )
    self.usrLogout = channel.unary_unary(
        '/CtrServer/usrLogout',
        request_serializer=usrInfo.SerializeToString,
        response_deserializer=logoutInfo.FromString,
        )
    self.getFileList = channel.unary_unary(
        '/CtrServer/getFileList',
        request_serializer=usrInfo.SerializeToString,
        response_deserializer=fileList.FromString,
        )
    self.uploadFile = channel.stream_unary(
        '/CtrServer/uploadFile',
        request_serializer=fileData.SerializeToString,
        response_deserializer=fileInfo.FromString,
        )
    self.downloadFile = channel.unary_stream(
        '/CtrServer/downloadFile',
        request_serializer=fileInfo.SerializeToString,
        response_deserializer=fileData.FromString,
        )
    self.getNodeInfo = channel.unary_unary(
        '/CtrServer/getNodeInfo',
        request_serializer=usrInfo.SerializeToString,
        response_deserializer=nodeInfo.FromString,
        )


class CtrServerServicer(object):

  def usrLogin(self, request, context):
    """User login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def usrLogout(self, request, context):
    """logout
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getFileList(self, request, context):
    """get all file names
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def uploadFile(self, request_iterator, context):
    """upload
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def downloadFile(self, request, context):
    """download
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getNodeInfo(self, request, context):
    """node info
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CtrServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'usrLogin': grpc.unary_unary_rpc_method_handler(
          servicer.usrLogin,
          request_deserializer=usrInfo.FromString,
          response_serializer=loginInfo.SerializeToString,
      ),
      'usrLogout': grpc.unary_unary_rpc_method_handler(
          servicer.usrLogout,
          request_deserializer=usrInfo.FromString,
          response_serializer=logoutInfo.SerializeToString,
      ),
      'getFileList': grpc.unary_unary_rpc_method_handler(
          servicer.getFileList,
          request_deserializer=usrInfo.FromString,
          response_serializer=fileList.SerializeToString,
      ),
      'uploadFile': grpc.stream_unary_rpc_method_handler(
          servicer.uploadFile,
          request_deserializer=fileData.FromString,
          response_serializer=fileInfo.SerializeToString,
      ),
      'downloadFile': grpc.unary_stream_rpc_method_handler(
          servicer.downloadFile,
          request_deserializer=fileInfo.FromString,
          response_serializer=fileData.SerializeToString,
      ),
      'getNodeInfo': grpc.unary_unary_rpc_method_handler(
          servicer.getNodeInfo,
          request_deserializer=usrInfo.FromString,
          response_serializer=nodeInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'CtrServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaCtrServerServicer(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def usrLogin(self, request, context):
    """User login
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def usrLogout(self, request, context):
    """logout
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getFileList(self, request, context):
    """get all file names
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def uploadFile(self, request_iterator, context):
    """upload
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def downloadFile(self, request, context):
    """download
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getNodeInfo(self, request, context):
    """node info
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaCtrServerStub(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def usrLogin(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """User login
    """
    raise NotImplementedError()
  usrLogin.future = None
  def usrLogout(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """logout
    """
    raise NotImplementedError()
  usrLogout.future = None
  def getFileList(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """get all file names
    """
    raise NotImplementedError()
  getFileList.future = None
  def uploadFile(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
    """upload
    """
    raise NotImplementedError()
  uploadFile.future = None
  def downloadFile(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """download
    """
    raise NotImplementedError()
  def getNodeInfo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """node info
    """
    raise NotImplementedError()
  getNodeInfo.future = None


def beta_create_CtrServer_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_deserializers = {
    ('CtrServer', 'downloadFile'): fileInfo.FromString,
    ('CtrServer', 'getFileList'): usrInfo.FromString,
    ('CtrServer', 'getNodeInfo'): usrInfo.FromString,
    ('CtrServer', 'uploadFile'): fileData.FromString,
    ('CtrServer', 'usrLogin'): usrInfo.FromString,
    ('CtrServer', 'usrLogout'): usrInfo.FromString,
  }
  response_serializers = {
    ('CtrServer', 'downloadFile'): fileData.SerializeToString,
    ('CtrServer', 'getFileList'): fileList.SerializeToString,
    ('CtrServer', 'getNodeInfo'): nodeInfo.SerializeToString,
    ('CtrServer', 'uploadFile'): fileInfo.SerializeToString,
    ('CtrServer', 'usrLogin'): loginInfo.SerializeToString,
    ('CtrServer', 'usrLogout'): logoutInfo.SerializeToString,
  }
  method_implementations = {
    ('CtrServer', 'downloadFile'): face_utilities.unary_stream_inline(servicer.downloadFile),
    ('CtrServer', 'getFileList'): face_utilities.unary_unary_inline(servicer.getFileList),
    ('CtrServer', 'getNodeInfo'): face_utilities.unary_unary_inline(servicer.getNodeInfo),
    ('CtrServer', 'uploadFile'): face_utilities.stream_unary_inline(servicer.uploadFile),
    ('CtrServer', 'usrLogin'): face_utilities.unary_unary_inline(servicer.usrLogin),
    ('CtrServer', 'usrLogout'): face_utilities.unary_unary_inline(servicer.usrLogout),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_CtrServer_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_serializers = {
    ('CtrServer', 'downloadFile'): fileInfo.SerializeToString,
    ('CtrServer', 'getFileList'): usrInfo.SerializeToString,
    ('CtrServer', 'getNodeInfo'): usrInfo.SerializeToString,
    ('CtrServer', 'uploadFile'): fileData.SerializeToString,
    ('CtrServer', 'usrLogin'): usrInfo.SerializeToString,
    ('CtrServer', 'usrLogout'): usrInfo.SerializeToString,
  }
  response_deserializers = {
    ('CtrServer', 'downloadFile'): fileData.FromString,
    ('CtrServer', 'getFileList'): fileList.FromString,
    ('CtrServer', 'getNodeInfo'): nodeInfo.FromString,
    ('CtrServer', 'uploadFile'): fileInfo.FromString,
    ('CtrServer', 'usrLogin'): loginInfo.FromString,
    ('CtrServer', 'usrLogout'): logoutInfo.FromString,
  }
  cardinalities = {
    'downloadFile': cardinality.Cardinality.UNARY_STREAM,
    'getFileList': cardinality.Cardinality.UNARY_UNARY,
    'getNodeInfo': cardinality.Cardinality.UNARY_UNARY,
    'uploadFile': cardinality.Cardinality.STREAM_UNARY,
    'usrLogin': cardinality.Cardinality.UNARY_UNARY,
    'usrLogout': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'CtrServer', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
