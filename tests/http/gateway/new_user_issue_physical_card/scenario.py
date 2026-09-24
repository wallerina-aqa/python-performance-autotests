import httpx
from locust import task

from locust_settings.http.http_gateway_tasksets import GatewayHTTPSequentialTaskSet
from locust_settings.user import LocustBaseUser


class IssuePhysicalCardSequentialTaskSet(GatewayHTTPSequentialTaskSet):
    user_id: str | None = None
    account_id: str | None = None

    @task
    def create_user(self):
        try:
            self.create_user_client.send_request()
        except httpx.RequestError:
            return

        self.user_id = self.create_user_client.USER_ID

    @task
    def open_debit_card_account(self):
        if self.user_id is None:
            return

        try:
            self.open_debit_card_account_client.send_request(user_id=self.user_id)
        except httpx.RequestError:
            return

        self.account_id = self.open_debit_card_account_client.account_id

    @task
    def issue_physical_card(self):
        if self.user_id is None or self.account_id is None:
            return

        try:
            self.issue_physical_card_client.send_request(
                user_id=self.user_id, account_id=self.account_id
            )
        except httpx.RequestError:
            return


class IssuePhysicalCardScenarioUser(LocustBaseUser):
    tasks = [IssuePhysicalCardSequentialTaskSet]
