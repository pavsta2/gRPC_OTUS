import grpc
from otus_pb2_grpc import UserActionsStub
import otus_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = UserActionsStub(channel)


def register_user(lastname, firstname, age, isMarried):
    request = otus_pb2.User(lastname=lastname,
                            firstname=firstname,
                            age=age,
                            isMarried=isMarried)
    return stub.RegisterUser(request)


def get_user(id_):
    request = otus_pb2.Id(Id=id_)
    return stub.GetUser(request)


def del_user(id_):
    request = otus_pb2.Id(Id=id_)
    return stub.DeleteUser(request)