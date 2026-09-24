from grpc import Channel

from contracts.services.gateway.operations.rpc_get_operations_pb2 import (
    GetOperationsRequest,
    GetOperationsResponse,
)
from services.grpc.gateway.operations.operations_grpc_service import (
    OperationsGatewaygRPCService,
)


class GetOperationsGatewayMethod(OperationsGatewaygRPCService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.REQUEST = GetOperationsRequest
        self.RESPONSE = GetOperationsResponse

    def send_request(self, account_id: str):
        self.reset_attributes("RESPONSE_DATA")

        request = self.REQUEST(account_id=account_id)
        self.RESPONSE_DATA = self.SERVICE.GetOperations(request)
        self.check_response_type(self.RESPONSE)
