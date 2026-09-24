from grpc import Channel

from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import (
    CardsGatewayServiceStub,
)
from services.grpc.base_service import BaseService


class CardsGatewaygRPCService(BaseService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.SERVICE = CardsGatewayServiceStub(self.CHANNEL)

    @property
    def card_id(self):
        if self.RESPONSE_DATA is None:
            raise ValueError("RESPONSE_DATA is empty. Call send_request() first.")
        return self.RESPONSE_DATA.card.id
