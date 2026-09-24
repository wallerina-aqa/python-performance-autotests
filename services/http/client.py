import logging

import httpx

from config import settings
from locust_settings.http.http_locust import (
    locust_request_event_hook,
    locust_response_event_hook,
)


def create_http_client(
    event_hooks: dict | None = None,
) -> httpx.Client:
    return httpx.Client(
        base_url=settings.base_url,
        event_hooks=event_hooks,
    )


def create_locust_http_client(environment) -> httpx.Client:
    logging.getLogger("httpx").setLevel(logging.WARNING)

    return create_http_client(
        event_hooks={
            "request": [locust_request_event_hook],
            "response": [locust_response_event_hook(environment)],
        }
    )
