import httpx

from schemas.operations_schemas import OperationsSummaryResponseSchema
from services.http.gateway.operations.operations_api import OperationsGatewayAPI


class GetOperationsSummaryGatewayAPI(OperationsGatewayAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.PATH = "/operations-summary"
        self.GET_OPERATIONS_SUMMARY_PATH_NAME = self.OPERATIONS_PATH_NAME + self.PATH
        self.GET_OPERATIONS_SUMMARY_API = self.OPERATIONS_API + self.PATH
        self.SCHEMA = OperationsSummaryResponseSchema

    def send_request(self, account_id: str):
        self.reset_attributes("RESPONSE_DATA")

        params = self.create_params(account_id=account_id)
        extensions = {"path_name": self.GET_OPERATIONS_SUMMARY_PATH_NAME}

        response = self.CLIENT.get(
            self.GET_OPERATIONS_SUMMARY_API, params=params, extensions=extensions
        )
        self.get_response_data(response)
