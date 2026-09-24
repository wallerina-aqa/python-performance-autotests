import httpx

from schemas.cards_schemas import IssueCardRequestSchema
from services.http.gateway.cards.cards_api import CardsGatewayAPI


class IssueVirtualCardGatewayAPI(CardsGatewayAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.PATH = "/issue-virtual-card"
        self.ISSUE_VIRTUAL_CARD_PATH_NAME = self.CARDS_PATH_NAME + self.PATH
        self.ISSUE_VIRTUAL_CARD_API = self.CARDS_API + self.PATH

    def send_request(self, user_id: str, account_id: str):
        self.reset_attributes("RESPONSE_DATA")

        owner_data = IssueCardRequestSchema(
            user_id=user_id, account_id=account_id
        ).model_dump(by_alias=True)
        extensions = {"path_name": self.ISSUE_VIRTUAL_CARD_PATH_NAME}

        response = self.CLIENT.post(
            self.ISSUE_VIRTUAL_CARD_API, json=owner_data, extensions=extensions
        )
        self.get_response_data(response)
