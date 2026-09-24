from enum import Enum
from time import time_ns

from faker import Faker
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper


class Fake:
    def __init__(self, faker):
        self.faker = faker

    def email(self) -> str:
        local_part, domain = self.faker.email().split("@", maxsplit=1)
        suffix = str(time_ns())[-8:]
        return f"{local_part}_{suffix}@{domain}"

    def first_name(self) -> str:
        return self.faker.first_name()

    def middle_name(self) -> str:
        return self.faker.first_name()

    def last_name(self) -> str:
        return self.faker.last_name()

    def phone_number(self) -> str:
        return self.faker.phone_number()

    def category(self) -> str:
        # fmt: off
        CATEGORIES = [
            "alcohol", "air_tickets", "beauty", "books", "cafes", "cinema", "clothing",
            "education", "electricity", "electronics", "fast_food", "flowers",
            "gaming", "gas_stations", "government_services", "groceries", "healthcare",
            "home_goods", "hotels", "internet", "insurance", "marketplace", "mobile",
            "parking", "pets", "pharmacies", "public_transport", "restaurants",
            "subscriptions", "sports", "supermarket", "taxi", "tolls", "travel",
            "utilities", "water"
        ]
        # fmt: on

        return self.faker.random_element(CATEGORIES)

    def amount(self, min_value: float = 1, max_value: float = 50_000) -> float:
        return self.faker.pyfloat(
            min_value=min_value, max_value=max_value, right_digits=2, positive=True
        )

    def enum(self, values: type[Enum]) -> Enum:
        return self.faker.random_element(list(values))

    def proto_enum(self, value: EnumTypeWrapper) -> int:
        return self.faker.random_element(value.values())


fake = Fake(faker=Faker())
