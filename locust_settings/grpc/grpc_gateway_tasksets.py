from grpc import Channel
from locust import User, TaskSet, SequentialTaskSet

from services.grpc.client import create_locust_grpc_channel
from services.grpc.gateway.accounts.get_accounts_method import GetAccountsGatewayMethod
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
from services.grpc.gateway.documents.get_contract_document_method import (
    GetContractDocumentGatewayMethod,
)
from services.grpc.gateway.documents.get_tariff_document_method import (
    GetTariffDocumentGatewayMethod,
)
from services.grpc.gateway.operations.get_operation_method import (
    GetOperationGatewayMethod,
)
from services.grpc.gateway.operations.get_operation_receipt_method import (
    GetOperationReceiptGatewayMethod,
)
from services.grpc.gateway.operations.get_operations_method import (
    GetOperationsGatewayMethod,
)
from services.grpc.gateway.operations.get_operations_summary_method import (
    GetOperationsSummaryGatewayMethod,
)
from services.grpc.gateway.operations.make_bill_payment_operation_method import (
    MakeBillPaymentOperationGatewayMethod,
)
from services.grpc.gateway.operations.make_cash_withdrawal_operation_method import (
    MakeCashWithdrawalOperationGatewayMethod,
)
from services.grpc.gateway.operations.make_cashback_operation_method import (
    MakeCashbackOperationGatewayMethod,
)
from services.grpc.gateway.operations.make_fee_operation_method import (
    MakeFeeOperationGatewayMethod,
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
from services.grpc.gateway.users.get_user_method import GetUserGatewayMethod


class GatewayGRPCClientsMixin:
    user: User
    grpc_channel: Channel

    create_user_client: CreateUserGatewayMethod
    get_user_client: GetUserGatewayMethod

    get_accounts_client: GetAccountsGatewayMethod
    open_credit_card_account_client: OpenCreditCardAccountGatewayMethod
    open_debit_card_account_client: OpenDebitCardAccountGatewayMethod
    open_deposit_account_client: OpenDepositAccountGatewayMethod
    open_savings_account_client: OpenSavingsAccountGatewayMethod

    issue_physical_card_client: IssuePhysicalCardGatewayMethod
    issue_virtual_card_client: IssueVirtualCardGatewayMethod

    get_contract_document_client: GetContractDocumentGatewayMethod
    get_tariff_document_client: GetTariffDocumentGatewayMethod

    get_operation_client: GetOperationGatewayMethod
    get_operation_receipt_client: GetOperationReceiptGatewayMethod
    get_operations_client: GetOperationsGatewayMethod
    get_operations_summary_client: GetOperationsSummaryGatewayMethod
    make_bill_payment_operation_client: MakeBillPaymentOperationGatewayMethod
    make_cashback_operation_client: MakeCashbackOperationGatewayMethod
    make_cash_withdrawal_operation_client: MakeCashWithdrawalOperationGatewayMethod
    make_fee_operation_client: MakeFeeOperationGatewayMethod
    make_purchase_operation_client: MakePurchaseOperationGatewayMethod
    make_top_up_operation_client: MakeTopUpOperationGatewayMethod
    make_transfer_operation_client: MakeTransferOperationGatewayMethod

    def initialize_clients(self) -> None:
        self.grpc_channel = create_locust_grpc_channel(self.user.environment)

        self.create_user_client = CreateUserGatewayMethod(channel=self.grpc_channel)
        self.get_user_client = GetUserGatewayMethod(channel=self.grpc_channel)

        self.get_accounts_client = GetAccountsGatewayMethod(channel=self.grpc_channel)
        self.open_debit_card_account_client = OpenDebitCardAccountGatewayMethod(
            channel=self.grpc_channel
        )
        self.open_credit_card_account_client = OpenCreditCardAccountGatewayMethod(
            channel=self.grpc_channel
        )
        self.open_deposit_account_client = OpenDepositAccountGatewayMethod(
            channel=self.grpc_channel
        )
        self.open_savings_account_client = OpenSavingsAccountGatewayMethod(
            channel=self.grpc_channel
        )

        self.issue_physical_card_client = IssuePhysicalCardGatewayMethod(
            channel=self.grpc_channel
        )
        self.issue_virtual_card_client = IssueVirtualCardGatewayMethod(
            channel=self.grpc_channel
        )

        self.get_contract_document_client = GetContractDocumentGatewayMethod(
            channel=self.grpc_channel
        )
        self.get_tariff_document_client = GetTariffDocumentGatewayMethod(
            channel=self.grpc_channel
        )

        self.get_operation_client = GetOperationGatewayMethod(channel=self.grpc_channel)
        self.get_operation_receipt_client = GetOperationReceiptGatewayMethod(
            channel=self.grpc_channel
        )
        self.get_operations_client = GetOperationsGatewayMethod(
            channel=self.grpc_channel
        )
        self.get_operations_summary_client = GetOperationsSummaryGatewayMethod(
            channel=self.grpc_channel
        )
        self.make_bill_payment_operation_client = MakeBillPaymentOperationGatewayMethod(
            channel=self.grpc_channel
        )
        self.make_cashback_operation_client = MakeCashbackOperationGatewayMethod(
            channel=self.grpc_channel
        )
        self.make_cash_withdrawal_operation_client = (
            MakeCashWithdrawalOperationGatewayMethod(channel=self.grpc_channel)
        )
        self.make_fee_operation_client = MakeFeeOperationGatewayMethod(
            channel=self.grpc_channel
        )
        self.make_purchase_operation_client = MakePurchaseOperationGatewayMethod(
            channel=self.grpc_channel
        )
        self.make_top_up_operation_client = MakeTopUpOperationGatewayMethod(
            channel=self.grpc_channel
        )
        self.make_transfer_operation_client = MakeTransferOperationGatewayMethod(
            channel=self.grpc_channel
        )

    def close_clients(self) -> None:
        self.grpc_channel.close()


class GatewayGRPCTaskSet(GatewayGRPCClientsMixin, TaskSet):
    def on_start(self) -> None:
        self.initialize_clients()

    def on_stop(self) -> None:
        self.close_clients()


class GatewayGRPCSequentialTaskSet(GatewayGRPCClientsMixin, SequentialTaskSet):
    def on_start(self) -> None:
        self.initialize_clients()

    def on_stop(self) -> None:
        self.close_clients()
