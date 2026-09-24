from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from schemas.documents_schemas import DocumentGatewaySchema
from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationGatewaySchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str
    category: str
    created_at: datetime
    account_id: str


class OperationsResponseSchema(BaseModel):
    operations: list[OperationGatewaySchema]


class OperationsSummaryGatewaySchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    spent_amount: float
    received_amount: float
    cashback_amount: float


class OperationsSummaryResponseSchema(BaseModel):
    summary: OperationsSummaryGatewaySchema


class OperationReceiptResponseSchema(BaseModel):
    receipt: DocumentGatewaySchema


class OperationResponseSchema(BaseModel):
    operation: OperationGatewaySchema


class MakeOperationRequestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str
    account_id: str


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    category: str = Field(default_factory=fake.category)
