from grpc import Channel

from contracts.services.gateway.users.rpc_get_user_pb2 import (
    GetUserRequest,
    GetUserResponse,
)
from services.grpc.gateway.users.users_grpc_service import UsersGatewaygRPCService


class GetUserGatewayMethod(UsersGatewaygRPCService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.REQUEST = GetUserRequest
        self.RESPONSE = GetUserResponse

    def send_request(self, user_id: str):
        self.reset_attributes("RESPONSE_DATA")

        request = self.REQUEST(id=user_id)
        self.RESPONSE_DATA = self.SERVICE.GetUser(request)
        self.check_response_type(self.RESPONSE)
