# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
# To regenerate run
# python -m grpc.tools.protoc --python_out=. --grpc_python_out=. -I. tensorflow_serving/apis/prediction_service.proto
import grpc

from tensorflow_serving.apis import predict_pb2 as tensorflow__serving_dot_apis_dot_predict__pb2


class PredictionServiceStub(object):
  """open source marker; do not remove
  PredictionService provides access to machine-learned models loaded by
  model_servers.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Predict = channel.unary_unary(
        '/tensorflow.serving.PredictionService/Predict',
        request_serializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictRequest.SerializeToString,
        response_deserializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictResponse.FromString,
        )
    self.PredictAlphafm = channel.unary_unary(
        '/tensorflow.serving.PredictionService/PredictAlphafm',
        request_serializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictRequest.SerializeToString,
        response_deserializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictResponse.FromString,
        )
    self.PredictAlphafmSoftmax = channel.unary_unary(
        '/tensorflow.serving.PredictionService/PredictAlphafmSoftmax',
        request_serializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictRequest.SerializeToString,
        response_deserializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictResponse.FromString,
        )


class PredictionServiceServicer(object):
  """open source marker; do not remove
  PredictionService provides access to machine-learned models loaded by
  model_servers.
  """

  def Predict(self, request, context):
    """Predict -- provides access to loaded machine-learned model.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PredictAlphafm(self, request, context):
    """PredictAlphafm
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PredictAlphafmSoftmax(self, request, context):
    """PredictAlphafmSoftmax
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PredictionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Predict': grpc.unary_unary_rpc_method_handler(
          servicer.Predict,
          request_deserializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictRequest.FromString,
          response_serializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictResponse.SerializeToString,
      ),
      'PredictAlphafm': grpc.unary_unary_rpc_method_handler(
          servicer.PredictAlphafm,
          request_deserializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictRequest.FromString,
          response_serializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictResponse.SerializeToString,
      ),
      'PredictAlphafmSoftmax': grpc.unary_unary_rpc_method_handler(
          servicer.PredictAlphafmSoftmax,
          request_deserializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictRequest.FromString,
          response_serializer=tensorflow__serving_dot_apis_dot_predict__pb2.PredictResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tensorflow.serving.PredictionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
