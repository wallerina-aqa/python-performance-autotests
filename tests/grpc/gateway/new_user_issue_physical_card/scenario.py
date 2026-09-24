from locust import task

from locust_settings.grpc.grpc_gateway_tasksets import GatewayGRPCSequentialTaskSet
from locust_settings.user import LocustBaseUser


class IssuePhysicalCardSequentialTaskSet(GatewayGRPCSequentialTaskSet):
    user_id: str | None = None
    account_id: str | None = None

    @task
    def create_user(self):
        self.create_user_client.send_request()
        self.user_id = self.create_user_client.USER_ID

    @task
    def open_debit_card_account(self):
        if self.user_id is None:
            return

        self.open_debit_card_account_client.send_request(user_id=self.user_id)
        self.account_id = self.open_debit_card_account_client.account_id

    @task
    def issue_physical_card(self):
        if self.user_id is None or self.account_id is None:
            return

        self.issue_physical_card_client.send_request(
            user_id=self.user_id, account_id=self.account_id
        )


class IssuePhysicalCardScenarioUser(LocustBaseUser):
    tasks = [IssuePhysicalCardSequentialTaskSet]
