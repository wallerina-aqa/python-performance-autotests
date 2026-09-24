import httpx

from services.http.gateway.operations.operations_api import OperationsGatewayAPI


class GetOperationGatewayAPI(OperationsGatewayAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.PATH = "/{operation_id}"
        self.GET_OPERATION_PATH_NAME = self.OPERATIONS_PATH_NAME + self.PATH

    def send_request(self, operation_id: str):
        self.reset_attributes("RESPONSE_DATA")

        extensions = {"path_name": self.GET_OPERATION_PATH_NAME}
        response = self.CLIENT.get(
            f"{self.OPERATIONS_API}/{operation_id}", extensions=extensions
        )
        self.get_operation_response_data(response)
