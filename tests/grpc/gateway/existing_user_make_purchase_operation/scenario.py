from locust import events, task
from locust.env import Environment

from locust_settings.grpc.grpc_gateway_tasksets import GatewayGRPCTaskSet
from locust_settings.user import LocustBaseUser
from seeds.builder import build_grpc_seeds_builder
from seeds.scenarios.existing_user_make_purchase_operation import (
    ExistingUserMakePurchaseOperationSeedsScenario,
)
from seeds.schemas.result import SeedUserResult


@events.init.add_listener
def init(environment: Environment, **kwargs):
    seeds_scenario = ExistingUserMakePurchaseOperationSeedsScenario(
        builder=build_grpc_seeds_builder()
    )
    seeds_scenario.build()
    environment.seeds = seeds_scenario.load()


class MakePurchaseOperationTaskSet(GatewayGRPCTaskSet):
    seed_user: SeedUserResult
    user_id: str
    card_id: str
    account_id: str

    def on_start(self) -> None:
        super().on_start()
        self.seed_user = self.user.environment.seeds.get_random_user()
        self.user_id = self.seed_user.user_id
        self.card_id = self.seed_user.credit_card_accounts[0].physical_cards[0].card_id
        self.account_id = self.seed_user.credit_card_accounts[0].account_id

    @task
    def make_purchase_operation(self):
        self.make_purchase_operation_client.send_request(
            card_id=self.card_id, account_id=self.account_id
        )

    @task(2)
    def get_accounts(self):
        self.get_accounts_client.send_request(user_id=self.user_id)

    @task(2)
    def get_operations(self):
        self.get_operations_client.send_request(account_id=self.account_id)

    @task(2)
    def get_operations_summary(self):
        self.get_operations_summary_client.send_request(account_id=self.account_id)


class MakePurchaseOperationScenarioUser(LocustBaseUser):
    tasks = [MakePurchaseOperationTaskSet]
