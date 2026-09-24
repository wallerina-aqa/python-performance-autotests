from seeds.schemas.plan import SeedAccountsPlan, SeedUsersPlan, SeedsPlan
from seeds.schemas.result import (
    SeedCardResult,
    SeedOperationResult,
    SeedAccountResult,
    SeedUserResult,
    SeedsResult,
)
from services.grpc.gateway.accounts.open_credit_card_account_method import (
    OpenCreditCardAccountGatewayMethod,
)
from services.grpc.gateway.accounts.open_debit_card_account_method import (
    OpenDebitCardAccountGatewayMethod,
)
from services.grpc.gateway.accounts.open_deposit_account_method import (
    OpenDepositAccountGatewayMethod,
)
from services.grpc.gateway.accounts.open_savings_account_method import (
    OpenSavingsAccountGatewayMethod,
)
from services.grpc.gateway.cards.issue_physical_card_method import (
    IssuePhysicalCardGatewayMethod,
)
from services.grpc.gateway.cards.issue_virtual_card_method import (
    IssueVirtualCardGatewayMethod,
)
from services.grpc.gateway.operations.make_cash_withdrawal_operation_method import (
    MakeCashWithdrawalOperationGatewayMethod,
)
from services.grpc.gateway.operations.make_purchase_operation_method import (
    MakePurchaseOperationGatewayMethod,
)
from services.grpc.gateway.operations.make_top_up_operation_method import (
    MakeTopUpOperationGatewayMethod,
)
from services.grpc.gateway.operations.make_transfer_operation_method import (
    MakeTransferOperationGatewayMethod,
)
from services.grpc.gateway.users.create_user_method import CreateUserGatewayMethod
from services.http.gateway.accounts.open_credit_card_account_api import (
    OpenCreditCardAccountGatewayAPI,
)
from services.http.gateway.accounts.open_debit_card_account_api import (
    OpenDebitCardAccountGatewayAPI,
)
from services.http.gateway.accounts.open_deposit_account_api import (
    OpenDepositAccountGatewayAPI,
)
from services.http.gateway.accounts.open_savings_account_api import (
    OpenSavingsAccountGatewayAPI,
)
from services.http.gateway.cards.issue_physical_card_api import (
    IssuePhysicalCardGatewayAPI,
)
from services.http.gateway.cards.issue_virtual_card_api import (
    IssueVirtualCardGatewayAPI,
)
from services.http.gateway.operations.make_cash_withdrawal_operation_api import (
    MakeCashWithdrawalOperationGatewayAPI,
)
from services.http.gateway.operations.make_purchase_operation_api import (
    MakePurchaseOperationGatewayAPI,
)
from services.http.gateway.operations.make_top_up_operation_api import (
    MakeTopUpOperationGatewayAPI,
)
from services.http.gateway.operations.make_transfer_operation_api import (
    MakeTransferOperationGatewayAPI,
)
from services.http.gateway.users.create_user_api import CreateUserGatewayAPI


class SeedsBuilder:
    def __init__(
        self,
        issue_physical_card_client,
        issue_virtual_card_client,
        make_top_up_operation_client,
        make_purchase_operation_client,
        make_transfer_operation_client,
        make_cash_withdrawal_operation_client,
        open_debit_card_account_client,
        open_credit_card_account_client,
        open_deposit_account_client,
        open_savings_account_client,
        create_user_client,
    ):
        self.issue_physical_card_client = issue_physical_card_client
        self.issue_virtual_card_client = issue_virtual_card_client
        self.make_top_up_operation_client = make_top_up_operation_client
        self.make_purchase_operation_client = make_purchase_operation_client
        self.make_transfer_operation_client = make_transfer_operation_client
        self.make_cash_withdrawal_operation_client = (
            make_cash_withdrawal_operation_client
        )
        self.open_debit_card_account_client = open_debit_card_account_client
        self.open_credit_card_account_client = open_credit_card_account_client
        self.open_deposit_account_client = open_deposit_account_client
        self.open_savings_account_client = open_savings_account_client
        self.create_user_client = create_user_client

    def build_physical_card_result(
        self, user_id: str, account_id: str
    ) -> SeedCardResult:
        self.issue_physical_card_client.send_request(
            user_id=user_id, account_id=account_id
        )
        return SeedCardResult(card_id=self.issue_physical_card_client.card_id)

    def build_virtual_card_result(
        self, user_id: str, account_id: str
    ) -> SeedCardResult:
        self.issue_virtual_card_client(user_id=user_id, account_id=account_id)
        return SeedCardResult(card_id=self.issue_virtual_card_client.card_id)

    def build_top_up_operation_result(
        self, card_id: str, account_id: str
    ) -> SeedOperationResult:
        self.make_top_up_operation_client.send_request(
            card_id=card_id, account_id=account_id
        )
        return SeedOperationResult(
            operation_id=self.make_top_up_operation_client.operation_id
        )

    def build_purchase_operation_result(
        self, card_id: str, account_id: str
    ) -> SeedOperationResult:
        self.make_purchase_operation_client.send_request(
            card_id=card_id, account_id=account_id
        )
        return SeedOperationResult(
            operation_id=self.make_purchase_operation_client.operation_id
        )

    def build_transfer_operation_result(
        self, card_id: str, account_id: str
    ) -> SeedOperationResult:
        self.make_transfer_operation_client.send_request(
            card_id=card_id, account_id=account_id
        )
        return SeedOperationResult(
            operation_id=self.make_transfer_operation_client.operation_id
        )

    def build_cash_withdrawal_operation_result(
        self, card_id: str, account_id: str
    ) -> SeedOperationResult:
        self.make_cash_withdrawal_operation_client.send_request(
            card_id=card_id, account_id=account_id
        )
        return SeedOperationResult(
            operation_id=self.make_cash_withdrawal_operation_client.operation_id
        )

    def build_debit_card_account_result(
        self, plan: SeedAccountsPlan, user_id: str
    ) -> SeedAccountResult:
        self.open_debit_card_account_client.send_request(user_id=user_id)
        card_id = self.open_debit_card_account_client.card_id
        account_id = self.open_debit_card_account_client.account_id

        return SeedAccountResult(
            account_id=account_id,
            physical_cards=[
                self.build_physical_card_result(user_id=user_id, account_id=account_id)
                for _ in range(plan.physical_cards.count)
            ],
            virtual_cards=[
                self.build_virtual_card_result(user_id=user_id, account_id=account_id)
                for _ in range(plan.virtual_cards.count)
            ],
            top_up_operations=[
                self.build_top_up_operation_result(
                    card_id=card_id, account_id=account_id
                )
                for _ in range(plan.top_up_operations.count)
            ],
            purchase_operations=[
                self.build_purchase_operation_result(
                    card_id=card_id, account_id=account_id
                )
                for _ in range(plan.purchase_operations.count)
            ],
            transfer_operations=[
                self.build_transfer_operation_result(
                    card_id=card_id, account_id=account_id
                )
                for _ in range(plan.transfer_operations.count)
            ],
            cash_withdrawal_operations=[
                self.build_cash_withdrawal_operation_result(
                    card_id=card_id, account_id=account_id
                )
                for _ in range(plan.cash_withdrawal_operations.count)
            ],
        )

    def build_credit_card_account_result(
        self, plan: SeedAccountsPlan, user_id: str
    ) -> SeedAccountResult:
        self.open_credit_card_account_client.send_request(user_id=user_id)
        card_id = self.open_credit_card_account_client.card_id
        account_id = self.open_credit_card_account_client.account_id

        return SeedAccountResult(
            account_id=account_id,
            physical_cards=[
                self.build_physical_card_result(user_id=user_id, account_id=account_id)
                for _ in range(plan.physical_cards.count)
            ],
            virtual_cards=[
                self.build_virtual_card_result(user_id=user_id, account_id=account_id)
                for _ in range(plan.virtual_cards.count)
            ],
            top_up_operations=[
                self.build_top_up_operation_result(
                    card_id=card_id, account_id=account_id
                )
                for _ in range(plan.top_up_operations.count)
            ],
            purchase_operations=[
                self.build_purchase_operation_result(
                    card_id=card_id, account_id=account_id
                )
                for _ in range(plan.purchase_operations.count)
            ],
            transfer_operations=[
                self.build_transfer_operation_result(
                    card_id=card_id, account_id=account_id
                )
                for _ in range(plan.transfer_operations.count)
            ],
            cash_withdrawal_operations=[
                self.build_cash_withdrawal_operation_result(
                    card_id=card_id, account_id=account_id
                )
                for _ in range(plan.cash_withdrawal_operations.count)
            ],
        )

    def build_deposit_account_result(self, user_id: str) -> SeedAccountResult:
        self.open_deposit_account_client.send_request(user_id=user_id)
        return SeedAccountResult(account_id=self.open_deposit_account_client.account_id)

    def build_savings_account_result(self, user_id: str) -> SeedAccountResult:
        self.open_savings_account_client.send_request(user_id=user_id)
        return SeedAccountResult(account_id=self.open_savings_account_client.account_id)

    def build_user(self, plan: SeedUsersPlan) -> SeedUserResult:
        self.create_user_client.send_request()

        user_id = self.create_user_client.USER_ID

        return SeedUserResult(
            user_id=user_id,
            savings_accounts=[
                self.build_savings_account_result(user_id=user_id)
                for _ in range(plan.savings_accounts.count)
            ],
            deposit_accounts=[
                self.build_deposit_account_result(user_id=user_id)
                for _ in range(plan.deposit_accounts.count)
            ],
            debit_card_accounts=[
                self.build_debit_card_account_result(
                    plan=plan.debit_card_accounts, user_id=user_id
                )
                for _ in range(plan.debit_card_accounts.count)
            ],
            credit_card_accounts=[
                self.build_credit_card_account_result(
                    plan=plan.credit_card_accounts, user_id=user_id
                )
                for _ in range(plan.credit_card_accounts.count)
            ],
        )

    def build(self, plan: SeedsPlan) -> SeedsResult:
        return SeedsResult(
            users=[self.build_user(plan=plan.users) for _ in range(plan.users.count)]
        )


def build_http_seeds_builder():
    return SeedsBuilder(
        issue_physical_card_client=IssuePhysicalCardGatewayAPI(),
        issue_virtual_card_client=IssueVirtualCardGatewayAPI(),
        make_top_up_operation_client=MakeTopUpOperationGatewayAPI(),
        make_purchase_operation_client=MakePurchaseOperationGatewayAPI(),
        make_transfer_operation_client=MakeTransferOperationGatewayAPI(),
        make_cash_withdrawal_operation_client=MakeCashWithdrawalOperationGatewayAPI(),
        open_debit_card_account_client=OpenDebitCardAccountGatewayAPI(),
        open_credit_card_account_client=OpenCreditCardAccountGatewayAPI(),
        open_deposit_account_client=OpenDepositAccountGatewayAPI(),
        open_savings_account_client=OpenSavingsAccountGatewayAPI(),
        create_user_client=CreateUserGatewayAPI(),
    )


def build_grpc_seeds_builder() -> SeedsBuilder:
    return SeedsBuilder(
        issue_physical_card_client=IssuePhysicalCardGatewayMethod(),
        issue_virtual_card_client=IssueVirtualCardGatewayMethod(),
        make_top_up_operation_client=MakeTopUpOperationGatewayMethod(),
        make_purchase_operation_client=MakePurchaseOperationGatewayMethod(),
        make_transfer_operation_client=MakeTransferOperationGatewayMethod(),
        make_cash_withdrawal_operation_client=MakeCashWithdrawalOperationGatewayMethod(),
        open_debit_card_account_client=OpenDebitCardAccountGatewayMethod(),
        open_credit_card_account_client=OpenCreditCardAccountGatewayMethod(),
        open_deposit_account_client=OpenDepositAccountGatewayMethod(),
        open_savings_account_client=OpenSavingsAccountGatewayMethod(),
        create_user_client=CreateUserGatewayMethod(),
    )
