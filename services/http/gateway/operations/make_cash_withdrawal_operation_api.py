import httpx

from schemas.operations_schemas import MakeOperationRequestSchema
from services.http.gateway.operations.operations_api import OperationsGatewayAPI


class MakeCashWithdrawalOperationGatewayAPI(OperationsGatewayAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.PATH = "/make-cash-withdrawal-operation"
        self.MAKE_CASH_WITHDRAWAL_OPERATION_PATH_NAME = (
            self.OPERATIONS_PATH_NAME + self.PATH
        )
        self.MAKE_CASH_WITHDRAWAL_OPERATION_API = self.OPERATIONS_API + self.PATH

    def send_request(self, card_id: str, account_id: str):
        self.reset_attributes("RESPONSE_DATA")

        operation_data = MakeOperationRequestSchema(
            card_id=card_id, account_id=account_id
        )
        extensions = {"path_name": self.MAKE_CASH_WITHDRAWAL_OPERATION_PATH_NAME}

        response = self.CLIENT.post(
            self.MAKE_CASH_WITHDRAWAL_OPERATION_API,
            json=operation_data.model_dump(by_alias=True),
            extensions=extensions,
        )
        self.get_operation_response_data(response)
