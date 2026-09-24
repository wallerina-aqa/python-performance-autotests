import httpx
from locust import task

from locust_settings.http.http_gateway_tasksets import GatewayHTTPSequentialTaskSet
from locust_settings.user import LocustBaseUser


class MakeTopUpOperationSequentialTaskSet(GatewayHTTPSequentialTaskSet):
    user_id: str | None = None
    card_id: str | None = None
    account_id: str | None = None
    operation_id: str | None = None

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

        self.card_id = self.open_debit_card_account_client.card_id
        self.account_id = self.open_debit_card_account_client.account_id

    @task
    def make_top_up_operation(self):
        if self.account_id is None or self.card_id is None:
            return

        try:
            self.make_top_up_operation_client.send_request(
                card_id=self.card_id, account_id=self.account_id
            )
        except httpx.RequestError:
            return

        self.operation_id = self.make_top_up_operation_client.operation_id

    @task
    def get_operations(self):
        if self.account_id is None:
            return

        try:
            self.get_operations_client.send_request(account_id=self.account_id)
        except httpx.RequestError:
            return

    @task
    def get_operations_summary(self):
        if self.account_id is None:
            return

        try:
            self.get_operations_summary_client.send_request(account_id=self.account_id)
        except httpx.RequestError:
            return

    @task
    def get_operation(self):
        if self.operation_id is None:
            return

        try:
            self.get_operation_client.send_request(operation_id=self.operation_id)
        except httpx.RequestError:
            return


class MakeTopUpOperationScenarioUser(LocustBaseUser):
    tasks = [MakeTopUpOperationSequentialTaskSet]
