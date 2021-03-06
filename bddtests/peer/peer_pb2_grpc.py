import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import peer.proposal_pb2 as peer_dot_proposal__pb2
import peer.proposal_response_pb2 as peer_dot_proposal__response__pb2


class EndorserStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ProcessProposal = channel.unary_unary(
        '/protos.Endorser/ProcessProposal',
        request_serializer=peer_dot_proposal__pb2.SignedProposal.SerializeToString,
        response_deserializer=peer_dot_proposal__response__pb2.ProposalResponse.FromString,
        )


class EndorserServicer(object):

  def ProcessProposal(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EndorserServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ProcessProposal': grpc.unary_unary_rpc_method_handler(
          servicer.ProcessProposal,
          request_deserializer=peer_dot_proposal__pb2.SignedProposal.FromString,
          response_serializer=peer_dot_proposal__response__pb2.ProposalResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protos.Endorser', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
