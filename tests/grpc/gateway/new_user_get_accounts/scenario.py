from locust import task

from locust_settings.grpc.grpc_gateway_tasksets import GatewayGRPCTaskSet
from locust_settings.user import LocustBaseUser


class GetAccountsTaskSet(GatewayGRPCTaskSet):
    user_id: str | None = None

    @task(2)
    def create_user(self):
        self.create_user_client.send_request()
        self.user_id = self.create_user_client.USER_ID

    @task(2)
    def open_deposit_account(self):
        if self.user_id is None:
            return

        self.open_deposit_account_client.send_request(user_id=self.user_id)

    @task(6)
    def get_accounts(self):
        if self.user_id is None:
            return

        self.get_accounts_client.send_request(user_id=self.user_id)


class GetAccountsScenarioUser(LocustBaseUser):
    tasks = [GetAccountsTaskSet]
