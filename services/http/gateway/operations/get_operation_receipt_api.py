import httpx

from schemas.operations_schemas import OperationReceiptResponseSchema
from services.http.gateway.operations.operations_api import OperationsGatewayAPI


class GetOperationReceiptGatewayAPI(OperationsGatewayAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.PATH = "/operation-receipt"
        self.GET_OPERATION_RECEIPT_PATH_NAME = (
            self.OPERATIONS_PATH_NAME + self.PATH + "/{operation_id}"
        )
        self.SCHEMA = OperationReceiptResponseSchema

    def send_request(self, operation_id: str):
        self.reset_attributes("RESPONSE_DATA")

        extensions = {"path_name": self.GET_OPERATION_RECEIPT_PATH_NAME}
        response = self.CLIENT.get(
            f"{self.OPERATIONS_API}{self.PATH}/{operation_id}",
            extensions=extensions,
        )
        self.get_response_data(response)
