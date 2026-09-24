from grpc import Channel

from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse,
)
from services.grpc.gateway.operations.operations_grpc_service import (
    OperationsGatewaygRPCService,
)


class GetOperationReceiptGatewayMethod(OperationsGatewaygRPCService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.REQUEST = GetOperationReceiptRequest
        self.RESPONSE = GetOperationReceiptResponse

    def send_request(self, operation_id: str):
        self.reset_attributes("RESPONSE_DATA")

        request = self.REQUEST(operation_id=operation_id)
        self.RESPONSE_DATA = self.SERVICE.GetOperationReceipt(request)
        self.check_response_type(self.RESPONSE)
