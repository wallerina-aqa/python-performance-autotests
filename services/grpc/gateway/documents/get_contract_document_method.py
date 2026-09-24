from grpc import Channel

from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import (
    GetContractDocumentRequest,
    GetContractDocumentResponse,
)
from services.grpc.gateway.documents.documents_grpc_service import (
    DocumentsGatewaygRPCService,
)


class GetContractDocumentGatewayMethod(DocumentsGatewaygRPCService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.REQUEST = GetContractDocumentRequest
        self.RESPONSE = GetContractDocumentResponse

    def send_request(self, account_id: str):
        self.reset_attributes("RESPONSE_DATA")

        request = self.REQUEST(account_id=account_id)
        self.RESPONSE_DATA = self.SERVICE.GetContractDocument(request)
        self.check_response_type(self.RESPONSE)
