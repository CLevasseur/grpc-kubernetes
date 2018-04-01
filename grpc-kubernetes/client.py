from __future__ import print_function
import argparse

import grpc

import service_pb2
import service_pb2_grpc


def run(server_ip):
    channel = grpc.insecure_channel('%s:30100' % server_ip)
    stub = service_pb2_grpc.MyServiceStub(channel)
    response = stub.handle_request(service_pb2.Request(name='you'))
    print("received: " + response.message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--server-ip', type=str, required=True)
    args = parser.parse_args()
    run(args.server_ip)
