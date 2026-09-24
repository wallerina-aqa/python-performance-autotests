import httpx

from schemas.cards_schemas import IssueCardResponseSchema
from services.http.base_api import BaseAPI


class CardsGatewayAPI(BaseAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.CARDS_PATH_NAME = self.CARDS_API = "/cards"
        self.SCHEMA = IssueCardResponseSchema

    @property
    def card_id(self):
        return self.RESPONSE_DATA.card.id
