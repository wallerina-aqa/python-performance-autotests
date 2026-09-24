from grpc import Channel

from contracts.services.gateway.operations.rpc_get_operation_pb2 import (
    GetOperationRequest,
    GetOperationResponse,
)
from services.grpc.gateway.operations.operations_grpc_service import (
    OperationsGatewaygRPCService,
)


class GetOperationGatewayMethod(OperationsGatewaygRPCService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.REQUEST = GetOperationRequest
        self.RESPONSE = GetOperationResponse

    def send_request(self, operation_id: str):
        self.reset_attributes("RESPONSE_DATA")

        request = self.REQUEST(id=operation_id)
        self.RESPONSE_DATA = self.SERVICE.GetOperation(request)
        self.check_response_type(self.RESPONSE)
