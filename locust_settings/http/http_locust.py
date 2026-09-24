import time

from httpx import Request, Response, HTTPError
from locust.env import Environment


def locust_request_event_hook(request: Request) -> None:
    request.extensions["start_time"] = time.perf_counter()


def locust_response_event_hook(environment: Environment):
    def inner(response: Response) -> None:
        exception: HTTPError | None = None

        try:
            response.raise_for_status()
        except HTTPError as error:
            exception = error

        request = response.request
        path_name = request.extensions.get("path_name", request.url.path)
        start_time = request.extensions.get("start_time", time.perf_counter())

        response_time = (time.perf_counter() - start_time) * 1000
        response_length = len(response.read())

        if environment.events is None:
            raise RuntimeError("Locust events are not initialized")

        environment.events.request.fire(
            name=f"{request.method} {path_name}",
            request_type="HTTP",
            response_time=response_time,
            response_length=response_length,
            response=response,
            context=None,
            exception=exception,
        )

    return inner
