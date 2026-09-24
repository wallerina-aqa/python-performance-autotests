import httpx

from schemas.accounts_schemas import AccountResponseSchema
from services.http.base_api import BaseAPI


class AccountsGatewayAPI(BaseAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.ACCOUNTS_PATH_NAME = self.ACCOUNTS_API = "/accounts"

    def get_account_response_data(self, response):
        self.SCHEMA = AccountResponseSchema
        self.get_response_data(response)

    @property
    def account_id(self):
        if self.RESPONSE_DATA is None:
            raise ValueError("RESPONSE_DATA is empty. Call send_request() first.")
        return self.RESPONSE_DATA.account.id

    @property
    def card_id(self):
        if self.RESPONSE_DATA is None:
            raise ValueError("RESPONSE_DATA is empty. Call send_request() first.")
        return self.RESPONSE_DATA.account.cards[0].id
