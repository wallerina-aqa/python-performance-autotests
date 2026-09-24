from grpc import Channel

from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import (
    DocumentsGatewayServiceStub,
)
from services.grpc.base_service import BaseService


class DocumentsGatewaygRPCService(BaseService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.SERVICE = DocumentsGatewayServiceStub(self.CHANNEL)
