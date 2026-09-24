from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class IssueCardRequestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )
    user_id: str
    account_id: str


class CardType(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"


class CardStatus(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"


class CardPaymentSystem(StrEnum):
    UNSPECIFIED = "UNSPECIFIED"
    MASTERCARD = "MASTERCARD"
    VISA = "VISA"


class CardGatewaySchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)
    id: str
    pin: str
    cvv: str
    type: CardType
    status: CardStatus
    account_id: str
    card_number: str
    card_holder: str
    expiry_date: date
    payment_system: CardPaymentSystem


class IssueCardResponseSchema(BaseModel):
    card: CardGatewaySchema
