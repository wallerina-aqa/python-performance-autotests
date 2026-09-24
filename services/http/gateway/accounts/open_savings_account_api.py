import httpx

from schemas.accounts_schemas import OpenAccountRequestSchema
from services.http.gateway.accounts.accounts_api import AccountsGatewayAPI


class OpenSavingsAccountGatewayAPI(AccountsGatewayAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.PATH = "/open-savings-account"
        self.OPEN_SAVINGS_ACCOUNT_PATH_NAME = self.ACCOUNTS_PATH_NAME + self.PATH
        self.OPEN_SAVINGS_ACCOUNT_API = self.ACCOUNTS_API + self.PATH

    def send_request(self, user_id: str):
        self.reset_attributes("RESPONSE_DATA")

        user_data = OpenAccountRequestSchema(user_id=user_id).model_dump(by_alias=True)

        extensions = {"path_name": self.OPEN_SAVINGS_ACCOUNT_PATH_NAME}
        response = self.CLIENT.post(
            self.OPEN_SAVINGS_ACCOUNT_API, json=user_data, extensions=extensions
        )
        self.get_account_response_data(response)
