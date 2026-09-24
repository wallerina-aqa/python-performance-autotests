from grpc import Channel

from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import (
    AccountsGatewayServiceStub,
)
from services.grpc.base_service import BaseService


class AccountsGatewaygRPCService(BaseService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.SERVICE = AccountsGatewayServiceStub(self.CHANNEL)

    @property
    def account_id(self):
        if self.RESPONSE_DATA is None:
            raise ValueError("RESPONSE_DATA is empty. Call send_request() first.")
        return self.RESPONSE_DATA.account.id

    @property
    def card_id(self):
        if self.RESPONSE_DATA is None:
            raise ValueError("RESPONSE_DATA is empty. Call send_request() first.")
        return self.RESPONSE_DATA.account.cards[0].id
