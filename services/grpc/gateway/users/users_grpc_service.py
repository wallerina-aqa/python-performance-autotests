from grpc import Channel

from contracts.services.gateway.users.users_gateway_service_pb2_grpc import (
    UsersGatewayServiceStub,
)
from services.grpc.base_service import BaseService


class UsersGatewaygRPCService(BaseService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.SERVICE = UsersGatewayServiceStub(self.CHANNEL)
