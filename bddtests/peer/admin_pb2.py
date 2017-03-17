# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/admin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='peer/admin.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x10peer/admin.proto\x12\x06protos\x1a\x1bgoogle/protobuf/empty.proto\"\x9a\x01\n\x0cServerStatus\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.protos.ServerStatus.StatusCode\"Y\n\nStatusCode\x12\r\n\tUNDEFINED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\x0b\n\x07STOPPED\x10\x02\x12\n\n\x06PAUSED\x10\x03\x12\t\n\x05\x45RROR\x10\x04\x12\x0b\n\x07UNKNOWN\x10\x05\"8\n\x0fLogLevelRequest\x12\x12\n\nlog_module\x18\x01 \x01(\t\x12\x11\n\tlog_level\x18\x02 \x01(\t\"9\n\x10LogLevelResponse\x12\x12\n\nlog_module\x18\x01 \x01(\t\x12\x11\n\tlog_level\x18\x02 \x01(\t2\xd5\x02\n\x05\x41\x64min\x12;\n\tGetStatus\x12\x16.google.protobuf.Empty\x1a\x14.protos.ServerStatus\"\x00\x12=\n\x0bStartServer\x12\x16.google.protobuf.Empty\x1a\x14.protos.ServerStatus\"\x00\x12<\n\nStopServer\x12\x16.google.protobuf.Empty\x1a\x14.protos.ServerStatus\"\x00\x12H\n\x11GetModuleLogLevel\x12\x17.protos.LogLevelRequest\x1a\x18.protos.LogLevelResponse\"\x00\x12H\n\x11SetModuleLogLevel\x12\x17.protos.LogLevelRequest\x1a\x18.protos.LogLevelResponse\"\x00\x42+Z)github.com/hyperledger/fabric/protos/peerb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SERVERSTATUS_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='protos.ServerStatus.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STARTED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=123,
  serialized_end=212,
)
_sym_db.RegisterEnumDescriptor(_SERVERSTATUS_STATUSCODE)


_SERVERSTATUS = _descriptor.Descriptor(
  name='ServerStatus',
  full_name='protos.ServerStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='protos.ServerStatus.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVERSTATUS_STATUSCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=212,
)


_LOGLEVELREQUEST = _descriptor.Descriptor(
  name='LogLevelRequest',
  full_name='protos.LogLevelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_module', full_name='protos.LogLevelRequest.log_module', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_level', full_name='protos.LogLevelRequest.log_level', index=1,
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
  serialized_start=214,
  serialized_end=270,
)


_LOGLEVELRESPONSE = _descriptor.Descriptor(
  name='LogLevelResponse',
  full_name='protos.LogLevelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_module', full_name='protos.LogLevelResponse.log_module', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_level', full_name='protos.LogLevelResponse.log_level', index=1,
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
  serialized_start=272,
  serialized_end=329,
)

_SERVERSTATUS.fields_by_name['status'].enum_type = _SERVERSTATUS_STATUSCODE
_SERVERSTATUS_STATUSCODE.containing_type = _SERVERSTATUS
DESCRIPTOR.message_types_by_name['ServerStatus'] = _SERVERSTATUS
DESCRIPTOR.message_types_by_name['LogLevelRequest'] = _LOGLEVELREQUEST
DESCRIPTOR.message_types_by_name['LogLevelResponse'] = _LOGLEVELRESPONSE

ServerStatus = _reflection.GeneratedProtocolMessageType('ServerStatus', (_message.Message,), dict(
  DESCRIPTOR = _SERVERSTATUS,
  __module__ = 'peer.admin_pb2'
  # @@protoc_insertion_point(class_scope:protos.ServerStatus)
  ))
_sym_db.RegisterMessage(ServerStatus)

LogLevelRequest = _reflection.GeneratedProtocolMessageType('LogLevelRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOGLEVELREQUEST,
  __module__ = 'peer.admin_pb2'
  # @@protoc_insertion_point(class_scope:protos.LogLevelRequest)
  ))
_sym_db.RegisterMessage(LogLevelRequest)

LogLevelResponse = _reflection.GeneratedProtocolMessageType('LogLevelResponse', (_message.Message,), dict(
  DESCRIPTOR = _LOGLEVELRESPONSE,
  __module__ = 'peer.admin_pb2'
  # @@protoc_insertion_point(class_scope:protos.LogLevelResponse)
  ))
_sym_db.RegisterMessage(LogLevelResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/hyperledger/fabric/protos/peer'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class AdminStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetStatus = channel.unary_unary(
          '/protos.Admin/GetStatus',
          request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
          response_deserializer=ServerStatus.FromString,
          )
      self.StartServer = channel.unary_unary(
          '/protos.Admin/StartServer',
          request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
          response_deserializer=ServerStatus.FromString,
          )
      self.StopServer = channel.unary_unary(
          '/protos.Admin/StopServer',
          request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
          response_deserializer=ServerStatus.FromString,
          )
      self.GetModuleLogLevel = channel.unary_unary(
          '/protos.Admin/GetModuleLogLevel',
          request_serializer=LogLevelRequest.SerializeToString,
          response_deserializer=LogLevelResponse.FromString,
          )
      self.SetModuleLogLevel = channel.unary_unary(
          '/protos.Admin/SetModuleLogLevel',
          request_serializer=LogLevelRequest.SerializeToString,
          response_deserializer=LogLevelResponse.FromString,
          )


  class AdminServicer(object):
    """Interface exported by the server.
    """

    def GetStatus(self, request, context):
      """Return the serve status.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def StartServer(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def StopServer(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetModuleLogLevel(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def SetModuleLogLevel(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_AdminServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetStatus': grpc.unary_unary_rpc_method_handler(
            servicer.GetStatus,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=ServerStatus.SerializeToString,
        ),
        'StartServer': grpc.unary_unary_rpc_method_handler(
            servicer.StartServer,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=ServerStatus.SerializeToString,
        ),
        'StopServer': grpc.unary_unary_rpc_method_handler(
            servicer.StopServer,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=ServerStatus.SerializeToString,
        ),
        'GetModuleLogLevel': grpc.unary_unary_rpc_method_handler(
            servicer.GetModuleLogLevel,
            request_deserializer=LogLevelRequest.FromString,
            response_serializer=LogLevelResponse.SerializeToString,
        ),
        'SetModuleLogLevel': grpc.unary_unary_rpc_method_handler(
            servicer.SetModuleLogLevel,
            request_deserializer=LogLevelRequest.FromString,
            response_serializer=LogLevelResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'protos.Admin', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaAdminServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """Interface exported by the server.
    """
    def GetStatus(self, request, context):
      """Return the serve status.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def StartServer(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def StopServer(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetModuleLogLevel(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def SetModuleLogLevel(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaAdminStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """Interface exported by the server.
    """
    def GetStatus(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Return the serve status.
      """
      raise NotImplementedError()
    GetStatus.future = None
    def StartServer(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    StartServer.future = None
    def StopServer(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    StopServer.future = None
    def GetModuleLogLevel(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetModuleLogLevel.future = None
    def SetModuleLogLevel(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    SetModuleLogLevel.future = None


  def beta_create_Admin_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('protos.Admin', 'GetModuleLogLevel'): LogLevelRequest.FromString,
      ('protos.Admin', 'GetStatus'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
      ('protos.Admin', 'SetModuleLogLevel'): LogLevelRequest.FromString,
      ('protos.Admin', 'StartServer'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
      ('protos.Admin', 'StopServer'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
    }
    response_serializers = {
      ('protos.Admin', 'GetModuleLogLevel'): LogLevelResponse.SerializeToString,
      ('protos.Admin', 'GetStatus'): ServerStatus.SerializeToString,
      ('protos.Admin', 'SetModuleLogLevel'): LogLevelResponse.SerializeToString,
      ('protos.Admin', 'StartServer'): ServerStatus.SerializeToString,
      ('protos.Admin', 'StopServer'): ServerStatus.SerializeToString,
    }
    method_implementations = {
      ('protos.Admin', 'GetModuleLogLevel'): face_utilities.unary_unary_inline(servicer.GetModuleLogLevel),
      ('protos.Admin', 'GetStatus'): face_utilities.unary_unary_inline(servicer.GetStatus),
      ('protos.Admin', 'SetModuleLogLevel'): face_utilities.unary_unary_inline(servicer.SetModuleLogLevel),
      ('protos.Admin', 'StartServer'): face_utilities.unary_unary_inline(servicer.StartServer),
      ('protos.Admin', 'StopServer'): face_utilities.unary_unary_inline(servicer.StopServer),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Admin_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('protos.Admin', 'GetModuleLogLevel'): LogLevelRequest.SerializeToString,
      ('protos.Admin', 'GetStatus'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ('protos.Admin', 'SetModuleLogLevel'): LogLevelRequest.SerializeToString,
      ('protos.Admin', 'StartServer'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ('protos.Admin', 'StopServer'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
    }
    response_deserializers = {
      ('protos.Admin', 'GetModuleLogLevel'): LogLevelResponse.FromString,
      ('protos.Admin', 'GetStatus'): ServerStatus.FromString,
      ('protos.Admin', 'SetModuleLogLevel'): LogLevelResponse.FromString,
      ('protos.Admin', 'StartServer'): ServerStatus.FromString,
      ('protos.Admin', 'StopServer'): ServerStatus.FromString,
    }
    cardinalities = {
      'GetModuleLogLevel': cardinality.Cardinality.UNARY_UNARY,
      'GetStatus': cardinality.Cardinality.UNARY_UNARY,
      'SetModuleLogLevel': cardinality.Cardinality.UNARY_UNARY,
      'StartServer': cardinality.Cardinality.UNARY_UNARY,
      'StopServer': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'protos.Admin', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
