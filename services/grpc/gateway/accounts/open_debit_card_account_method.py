from grpc import Channel

from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
    OpenDebitCardAccountResponse,
)
from services.grpc.gateway.accounts.accounts_grpc_service import (
    AccountsGatewaygRPCService,
)


class OpenDebitCardAccountGatewayMethod(AccountsGatewaygRPCService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.REQUEST = OpenDebitCardAccountRequest
        self.RESPONSE = OpenDebitCardAccountResponse

    def send_request(self, user_id: str):
        self.reset_attributes("RESPONSE_DATA")

        request = self.REQUEST(user_id=user_id)
        self.RESPONSE_DATA = self.SERVICE.OpenDebitCardAccount(request)
        self.check_response_type(self.RESPONSE)
