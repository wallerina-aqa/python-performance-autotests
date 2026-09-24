import httpx
from locust import TaskSet, SequentialTaskSet, User

from services.http.client import create_locust_http_client
from services.http.gateway.accounts.get_accounts_api import GetAccountsGatewayAPI
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
from services.http.gateway.documents.get_contract_document_api import (
    GetContractDocumentGatewayAPI,
)
from services.http.gateway.documents.get_tariff_document_api import (
    GetTariffDocumentGatewayAPI,
)
from services.http.gateway.operations.get_operation_api import GetOperationGatewayAPI
from services.http.gateway.operations.get_operation_receipt_api import (
    GetOperationReceiptGatewayAPI,
)
from services.http.gateway.operations.get_operations_api import GetOperationsGatewayAPI
from services.http.gateway.operations.get_operations_summary_api import (
    GetOperationsSummaryGatewayAPI,
)
from services.http.gateway.operations.make_bill_payment_operation_api import (
    MakeBillPaymentOperationGatewayAPI,
)
from services.http.gateway.operations.make_cashback_operation_api import (
    MakeCashbackOperationGatewayAPI,
)
from services.http.gateway.operations.make_cash_withdrawal_operation_api import (
    MakeCashWithdrawalOperationGatewayAPI,
)
from services.http.gateway.operations.make_fee_operation_api import (
    MakeFeeOperationGatewayAPI,
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
from services.http.gateway.users.get_user_api import GetUserGatewayAPI


class GatewayHTTPClientsMixin:
    user: User
    http_client: httpx.Client

    create_user_client: CreateUserGatewayAPI
    get_user_client: GetUserGatewayAPI

    get_accounts_client: GetAccountsGatewayAPI
    open_debit_card_account_client: OpenDebitCardAccountGatewayAPI
    open_credit_card_account_client: OpenCreditCardAccountGatewayAPI
    open_deposit_account_client: OpenDepositAccountGatewayAPI
    open_savings_account_client: OpenSavingsAccountGatewayAPI

    issue_physical_card_client: IssuePhysicalCardGatewayAPI
    issue_virtual_card_client: IssueVirtualCardGatewayAPI

    get_contract_document_client: GetContractDocumentGatewayAPI
    get_tariff_document_client: GetTariffDocumentGatewayAPI

    get_operation_client: GetOperationGatewayAPI
    get_operation_receipt_client: GetOperationReceiptGatewayAPI
    get_operations_client: GetOperationsGatewayAPI
    get_operations_summary_client: GetOperationsSummaryGatewayAPI
    make_bill_payment_operation_client: MakeBillPaymentOperationGatewayAPI
    make_cashback_operation_client: MakeCashbackOperationGatewayAPI
    make_cash_withdrawal_operation_client: MakeCashWithdrawalOperationGatewayAPI
    make_fee_operation_client: MakeFeeOperationGatewayAPI
    make_purchase_operation_client: MakePurchaseOperationGatewayAPI
    make_top_up_operation_client: MakeTopUpOperationGatewayAPI
    make_transfer_operation_client: MakeTransferOperationGatewayAPI

    def initialize_clients(self) -> None:
        self.http_client = create_locust_http_client(self.user.environment)

        self.create_user_client = CreateUserGatewayAPI(client=self.http_client)
        self.get_user_client = GetUserGatewayAPI(client=self.http_client)

        self.get_accounts_client = GetAccountsGatewayAPI(client=self.http_client)
        self.open_credit_card_account_client = OpenCreditCardAccountGatewayAPI(
            client=self.http_client
        )
        self.open_debit_card_account_client = OpenDebitCardAccountGatewayAPI(
            client=self.http_client
        )
        self.open_deposit_account_client = OpenDepositAccountGatewayAPI(
            client=self.http_client
        )
        self.open_savings_account_client = OpenSavingsAccountGatewayAPI(
            client=self.http_client
        )

        self.issue_physical_card_client = IssuePhysicalCardGatewayAPI(
            client=self.http_client
        )
        self.issue_virtual_card_client = IssueVirtualCardGatewayAPI(
            client=self.http_client
        )

        self.get_contract_document_client = GetContractDocumentGatewayAPI(
            client=self.http_client
        )
        self.get_tariff_document_client = GetTariffDocumentGatewayAPI(
            client=self.http_client
        )

        self.get_operation_client = GetOperationGatewayAPI(client=self.http_client)
        self.get_operation_receipt_client = GetOperationReceiptGatewayAPI(
            client=self.http_client
        )
        self.get_operations_client = GetOperationsGatewayAPI(client=self.http_client)
        self.get_operations_summary_client = GetOperationsSummaryGatewayAPI(
            client=self.http_client
        )
        self.make_bill_payment_operation_client = MakeBillPaymentOperationGatewayAPI(
            client=self.http_client
        )
        self.make_cashback_operation_client = MakeCashbackOperationGatewayAPI(
            client=self.http_client
        )
        self.make_cash_withdrawal_operation_client = (
            MakeCashWithdrawalOperationGatewayAPI(client=self.http_client)
        )
        self.make_fee_operation_client = MakeFeeOperationGatewayAPI(
            client=self.http_client
        )
        self.make_purchase_operation_client = MakePurchaseOperationGatewayAPI(
            client=self.http_client
        )
        self.make_top_up_operation_client = MakeTopUpOperationGatewayAPI(
            client=self.http_client
        )
        self.make_transfer_operation_client = MakeTransferOperationGatewayAPI(
            client=self.http_client
        )

    def close_clients(self) -> None:
        self.http_client.close()


class GatewayHTTPTaskSet(GatewayHTTPClientsMixin, TaskSet):
    def on_start(self) -> None:
        self.initialize_clients()

    def on_stop(self) -> None:
        self.close_clients()


class GatewayHTTPSequentialTaskSet(GatewayHTTPClientsMixin, SequentialTaskSet):
    def on_start(self) -> None:
        self.initialize_clients()

    def on_stop(self) -> None:
        self.close_clients()
