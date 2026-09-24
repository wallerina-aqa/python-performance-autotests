from grpc import Channel

from contracts.services.gateway.accounts.rpc_get_accounts_pb2 import (
    GetAccountsRequest,
    GetAccountsResponse,
)
from services.grpc.gateway.accounts.accounts_grpc_service import (
    AccountsGatewaygRPCService,
)


class GetAccountsGatewayMethod(AccountsGatewaygRPCService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.REQUEST = GetAccountsRequest
        self.RESPONSE = GetAccountsResponse

    def send_request(self, user_id: str):
        self.reset_attributes("RESPONSE_DATA")

        request = self.REQUEST(user_id=user_id)
        self.RESPONSE_DATA = self.SERVICE.GetAccounts(request)
        self.check_response_type(self.RESPONSE)
