from grpc import Channel

from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import (
    IssuePhysicalCardRequest,
    IssuePhysicalCardResponse,
)
from services.grpc.gateway.cards.cards_grpc_service import CardsGatewaygRPCService


class IssuePhysicalCardGatewayMethod(CardsGatewaygRPCService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.REQUEST = IssuePhysicalCardRequest
        self.RESPONSE = IssuePhysicalCardResponse

    def send_request(self, user_id: str, account_id: str):
        self.reset_attributes("RESPONSE_DATA")

        request = self.REQUEST(user_id=user_id, account_id=account_id)
        self.RESPONSE_DATA = self.SERVICE.IssuePhysicalCard(request)
        self.check_response_type(self.RESPONSE)
