import httpx

from schemas.documents_schemas import ContractDocumentResponseSchema
from services.http.gateway.documents.documents_api import DocumentsGatewayAPI


class GetContractDocumentGatewayAPI(DocumentsGatewayAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.PATH = "/contract-document"
        self.GET_CONTRACT_DOCUMENT_PATH_NAME = (
            self.DOCUMENTS_PATH_NAME + self.PATH + "/{account_id}"
        )
        self.SCHEMA = ContractDocumentResponseSchema

    def send_request(self, account_id: str):
        self.reset_attributes("RESPONSE_DATA")

        extensions = {"path_name": self.GET_CONTRACT_DOCUMENT_PATH_NAME}
        response = self.CLIENT.get(
            f"{self.DOCUMENTS_API}{self.PATH}/{account_id}",
            extensions=extensions,
        )
        self.get_response_data(response)
