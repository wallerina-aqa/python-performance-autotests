from enum import StrEnum

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from schemas.cards_schemas import CardGatewaySchema


class OpenAccountRequestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )
    user_id: str


class AccountType(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"
    DEPOSIT = "DEPOSIT"
    SAVINGS = "SAVINGS"


class AccountStatus(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    ACTIVE = "ACTIVE"
    PENDING_CLOSURE = "PENDING_CLOSURE"
    CLOSED = "CLOSED"


class AccountGatewaySchema(BaseModel):
    id: str
    type: AccountType
    cards: list[CardGatewaySchema]
    status: AccountStatus
    balance: float


class AccountResponseSchema(BaseModel):
    account: AccountGatewaySchema


class AccountsResponseSchema(BaseModel):
    accounts: list[AccountGatewaySchema]
