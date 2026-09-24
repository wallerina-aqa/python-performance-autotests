import httpx

from schemas.operations_schemas import OperationsResponseSchema
from services.http.gateway.operations.operations_api import OperationsGatewayAPI


class GetOperationsGatewayAPI(OperationsGatewayAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.GET_OPERATIONS_PATH_NAME = self.OPERATIONS_PATH_NAME
        self.GET_OPERATIONS_API = self.OPERATIONS_API
        self.SCHEMA = OperationsResponseSchema

    def send_request(self, account_id: str):
        self.reset_attributes("RESPONSE_DATA")

        params = self.create_params(account_id)
        extensions = {"path_name": self.GET_OPERATIONS_PATH_NAME}

        response = self.CLIENT.get(
            self.GET_OPERATIONS_API, params=params, extensions=extensions
        )
        self.get_response_data(response)
