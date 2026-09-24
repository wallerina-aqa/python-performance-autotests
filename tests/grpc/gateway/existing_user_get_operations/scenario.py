from locust import events, task
from locust.env import Environment

from locust_settings.grpc.grpc_gateway_tasksets import GatewayGRPCTaskSet
from locust_settings.user import LocustBaseUser
from seeds.builder import build_grpc_seeds_builder
from seeds.scenarios.existing_user_get_operations import (
    ExistingUserGetOperationsSeedsScenario,
)
from seeds.schemas.result import SeedUserResult


@events.init.add_listener
def init(environment: Environment, **kwargs):
    seeds_scenario = ExistingUserGetOperationsSeedsScenario(
        builder=build_grpc_seeds_builder()
    )
    seeds_scenario.build()
    environment.seeds = seeds_scenario.load()


class GetOperationsTaskSet(GatewayGRPCTaskSet):
    seed_user: SeedUserResult
    user_id: str
    account_id: str

    def on_start(self) -> None:
        super().on_start()
        self.seed_user = self.user.environment.seeds.get_random_user()
        self.user_id = self.seed_user.user_id
        self.account_id = self.seed_user.credit_card_accounts[0].account_id

    @task
    def get_accounts(self):
        self.get_accounts_client.send_request(user_id=self.user_id)

    @task(4)
    def get_operations(self):
        self.get_operations_client.send_request(account_id=self.account_id)

    @task(2)
    def get_operations_summary(self):
        self.get_operations_summary_client.send_request(account_id=self.account_id)


class GetOperationsScenarioUser(LocustBaseUser):
    tasks = [GetOperationsTaskSet]
