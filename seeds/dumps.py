import os

from seeds.schemas.result import SeedsResult
from tools.logger import get_logger

logger = get_logger("SEEDS_DUMPS")


def save_seeds_result(result: SeedsResult, scenario: str):
    if not os.path.exists("dumps"):
        os.mkdir("dumps")

    seeds_file = f"./dumps/{scenario}_seeds.json"
    with open(seeds_file, "w+", encoding="utf-8") as file:
        file.write(result.model_dump_json())

    logger.debug(f"Seeding result saved to file: {seeds_file}")


def load_seeds_result(scenario: str) -> SeedsResult:
    seeds_file = f"./dumps/{scenario}_seeds.json"
    with open(seeds_file, encoding="utf-8") as file:
        seeds_json = SeedsResult.model_validate_json(file.read())

    logger.debug(f"Seeding result loaded from file: {seeds_file}")
    return seeds_json
