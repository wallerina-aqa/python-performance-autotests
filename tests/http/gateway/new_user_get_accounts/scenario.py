import httpx
from locust import task

from locust_settings.http.http_gateway_tasksets import GatewayHTTPTaskSet
from locust_settings.user import LocustBaseUser


class GetAccountsTaskSet(GatewayHTTPTaskSet):
    user_id: str | None = None

    @task(2)
    def create_user(self):
        try:
            self.create_user_client.send_request()
        except httpx.RequestError:
            return

        self.user_id = self.create_user_client.USER_ID

    @task(2)
    def open_deposit_account(self):
        if self.user_id is None:
            return

        try:
            self.open_deposit_account_client.send_request(user_id=self.user_id)
        except httpx.RequestError:
            return

    @task(6)
    def get_accounts(self):
        if self.user_id is None:
            return

        try:
            self.get_accounts_client.send_request(user_id=self.user_id)
        except httpx.RequestError:
            return


class GetAccountsScenarioUser(LocustBaseUser):
    tasks = [GetAccountsTaskSet]
