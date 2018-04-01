import time
from concurrent import futures

import grpc

import service_pb2
import service_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Service(service_pb2_grpc.MyServiceServicer):

    def handle_request(self, request, context):
        return service_pb2.Response(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MyServiceServicer_to_server(Service(), server)
    server.add_insecure_port('[::]:80')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

