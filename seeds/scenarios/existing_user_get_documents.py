from seeds.builder import build_grpc_seeds_builder
from seeds.scenario import SeedsScenario
from seeds.schemas.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan


class ExistingUserGetDocumentsSeedsScenario(SeedsScenario):
    @property
    def plan(self) -> SeedsPlan:
        return SeedsPlan(
            users=SeedUsersPlan(
                count=100,
                savings_accounts=SeedAccountsPlan(count=1),
                debit_card_accounts=SeedAccountsPlan(count=1),
            ),
        )

    @property
    def scenario(self) -> str:
        return "existing_user_get_documents"


if __name__ == "__main__":
    seeds_scenario = ExistingUserGetDocumentsSeedsScenario(
        builder=build_grpc_seeds_builder()
    )
    seeds_scenario.build()
