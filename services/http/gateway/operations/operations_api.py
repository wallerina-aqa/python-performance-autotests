import httpx

from schemas.operations_schemas import OperationResponseSchema
from services.http.base_api import BaseAPI


class OperationsGatewayAPI(BaseAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.OPERATIONS_PATH_NAME = self.OPERATIONS_API = "/operations"

    @staticmethod
    def create_params(account_id: str):
        return {"accountId": account_id}

    def get_operation_response_data(self, response):
        self.SCHEMA = OperationResponseSchema
        self.get_response_data(response)

    @property
    def operation_id(self):
        return self.RESPONSE_DATA.operation.id
