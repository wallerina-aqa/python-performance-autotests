import httpx
from pydantic import BaseModel

from services.http.client import create_http_client


class BaseAPI:
    def __init__(self, client: httpx.Client | None = None):
        self.CLIENT = client or create_http_client()
        self.SCHEMA: type[BaseModel] | None = None
        self.RESPONSE_DATA = None

    def reset_attributes(self, *attributes):
        for attribute in attributes:
            if not hasattr(self, attribute):
                raise AttributeError(
                    f"{type(self).__name__} has no attribute {attribute!r}"
                )
            setattr(self, attribute, None)

    def get_response_data(self, response):
        content_type = response.headers.get("content-type", "")
        if "application/json" not in content_type:
            raise ValueError(
                f"Expected application/json content type, but got {content_type!r}"
            )

        if self.SCHEMA is None:
            raise ValueError("SCHEMA is not set.")
        self.RESPONSE_DATA = self.SCHEMA(**response.json())
