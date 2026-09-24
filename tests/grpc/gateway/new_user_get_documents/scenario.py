from locust import task

from locust_settings.grpc.grpc_gateway_tasksets import GatewayGRPCSequentialTaskSet
from locust_settings.user import LocustBaseUser


class GetDocumentsSequentialTaskSet(GatewayGRPCSequentialTaskSet):
    user_id: str | None = None
    account_id: str | None = None

    @task
    def create_user(self):
        self.create_user_client.send_request()
        self.user_id = self.create_user_client.USER_ID

    @task
    def open_savings_account(self):
        if self.user_id is None:
            return

        self.open_savings_account_client.send_request(user_id=self.user_id)
        self.account_id = self.open_savings_account_client.account_id

    @task
    def get_documents(self):
        if self.account_id is None:
            return

        self.get_tariff_document_client.send_request(account_id=self.account_id)
        self.get_contract_document_client.send_request(account_id=self.account_id)


class GetDocumentsScenarioUser(LocustBaseUser):
    tasks = [GetDocumentsSequentialTaskSet]
