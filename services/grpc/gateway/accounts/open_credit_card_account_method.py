from grpc import Channel

from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import (
    OpenCreditCardAccountRequest,
    OpenCreditCardAccountResponse,
)
from services.grpc.gateway.accounts.accounts_grpc_service import (
    AccountsGatewaygRPCService,
)


class OpenCreditCardAccountGatewayMethod(AccountsGatewaygRPCService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.REQUEST = OpenCreditCardAccountRequest
        self.RESPONSE = OpenCreditCardAccountResponse

    def send_request(self, user_id: str):
        self.reset_attributes("RESPONSE_DATA")

        request = self.REQUEST(user_id=user_id)
        self.RESPONSE_DATA = self.SERVICE.OpenCreditCardAccount(request)
        self.check_response_type(self.RESPONSE)
