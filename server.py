import signal
import grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection

import otus_pb2_grpc,  otus_pb2


class RegisterServicer(otus_pb2_grpc.UserActionsServicer):
    users = {}
    count = 1

    def RegisterUser(self, request, context):
        user = {'lastname': request.lastname, 'firstname': request.firstname, 'age': request.age,
                'isMarried': request.isMarried, 'id': RegisterServicer.count}

        RegisterServicer.count += 1

        print(f'User added: {user}')

        RegisterServicer.users[user['id']] = user
        return otus_pb2.Id(Id=user['id'])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    otus_pb2_grpc.add_UserActionsServicer_to_server(RegisterServicer(), server)

    def handle_sigint(sig, frame):
        print("Caught SIGINT, shutting down server...")
        server.stop(0)
    signal.signal(signal.SIGINT, handle_sigint)

    service_names = (
        otus_pb2.DESCRIPTOR.services_by_name['UserActions'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(service_names, server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server listening on :50051")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()