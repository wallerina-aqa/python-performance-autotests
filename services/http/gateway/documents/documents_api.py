import httpx

from services.http.base_api import BaseAPI


class DocumentsGatewayAPI(BaseAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.DOCUMENTS_PATH_NAME = self.DOCUMENTS_API = "/documents"
