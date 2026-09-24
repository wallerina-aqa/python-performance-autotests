import httpx

from schemas.accounts_schemas import AccountsResponseSchema
from services.http.gateway.accounts.accounts_api import AccountsGatewayAPI


class GetAccountsGatewayAPI(AccountsGatewayAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.GET_ACCOUNTS_PATH_NAME = self.ACCOUNTS_PATH_NAME
        self.GET_ACCOUNTS_API = self.ACCOUNTS_API
        self.SCHEMA = AccountsResponseSchema

    @staticmethod
    def create_params(user_id: str):
        return {"userId": user_id}

    def send_request(self, user_id: str):
        self.reset_attributes("RESPONSE_DATA")

        params = self.create_params(user_id=user_id)
        extensions = {"path_name": self.GET_ACCOUNTS_PATH_NAME}

        response = self.CLIENT.get(
            self.GET_ACCOUNTS_API, params=params, extensions=extensions
        )
        self.get_response_data(response)
