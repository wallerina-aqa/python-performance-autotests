from grpc import Channel

from contracts.services.gateway.users.rpc_create_user_pb2 import (
    CreateUserRequest,
    CreateUserResponse,
)
from services.grpc.gateway.users.users_grpc_service import UsersGatewaygRPCService
from tools.fakers import fake


class CreateUserGatewayMethod(UsersGatewaygRPCService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.REQUEST = CreateUserRequest
        self.RESPONSE = CreateUserResponse
        self.USER_ID = None

    def send_request(self):
        self.reset_attributes("RESPONSE_DATA", "USER_ID")

        request = self.REQUEST(
            email=fake.email(),
            last_name=fake.last_name(),
            first_name=fake.first_name(),
            middle_name=fake.middle_name(),
            phone_number=fake.phone_number(),
        )

        self.RESPONSE_DATA = self.SERVICE.CreateUser(request)
        self.check_response_type(self.RESPONSE)
        self.USER_ID = self.RESPONSE_DATA.user.id
