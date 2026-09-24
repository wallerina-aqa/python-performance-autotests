from grpc import Channel

from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse,
)
from contracts.services.operations.operation_pb2 import OperationStatus
from services.grpc.gateway.operations.operations_grpc_service import (
    OperationsGatewaygRPCService,
)
from tools.fakers import fake


class MakeTopUpOperationGatewayMethod(OperationsGatewaygRPCService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.REQUEST = MakeTopUpOperationRequest
        self.RESPONSE = MakeTopUpOperationResponse

    def send_request(self, card_id: str, account_id: str):
        self.reset_attributes("RESPONSE_DATA")

        request = self.REQUEST(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
        )
        self.RESPONSE_DATA = self.SERVICE.MakeTopUpOperation(request)
        self.check_response_type(self.RESPONSE)
