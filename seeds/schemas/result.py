import random

from pydantic import BaseModel, Field


class SeedCardResult(BaseModel):
    card_id: str


class SeedOperationResult(BaseModel):
    operation_id: str


class SeedAccountResult(BaseModel):
    account_id: str
    physical_cards: list[SeedCardResult] = Field(default_factory=list)
    virtual_cards: list[SeedCardResult] = Field(default_factory=list)
    top_up_operations: list[SeedOperationResult] = Field(default_factory=list)
    purchase_operations: list[SeedOperationResult] = Field(default_factory=list)
    transfer_operations: list[SeedOperationResult] = Field(default_factory=list)
    cash_withdrawal_operations: list[SeedOperationResult] = Field(default_factory=list)


class SeedUserResult(BaseModel):
    user_id: str
    deposit_accounts: list[SeedAccountResult] = Field(default_factory=list)
    savings_accounts: list[SeedAccountResult] = Field(default_factory=list)
    debit_card_accounts: list[SeedAccountResult] = Field(default_factory=list)
    credit_card_accounts: list[SeedAccountResult] = Field(default_factory=list)


class SeedsResult(BaseModel):
    users: list[SeedUserResult] = Field(default_factory=list)

    def get_next_user(self) -> SeedUserResult:
        return self.users.pop(0)

    def get_random_user(self) -> SeedUserResult:
        return random.choice(self.users)
