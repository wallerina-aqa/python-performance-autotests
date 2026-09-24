import grpc

from services.grpc.client import create_grpc_channel


class BaseService:
    def __init__(self, channel: grpc.Channel | None = None):
        self.CHANNEL = channel or create_grpc_channel()
        self.RESPONSE_DATA = None

    def reset_attributes(self, *attributes):
        for attribute in attributes:
            if not hasattr(self, attribute):
                raise AttributeError(
                    f"{type(self).__name__} has no attribute {attribute!r}"
                )
            setattr(self, attribute, None)

    def check_response_type(self, response_type):
        if self.RESPONSE_DATA is None:
            raise ValueError("RESPONSE_DATA is empty. Call send_request() first.")
        assert isinstance(self.RESPONSE_DATA, response_type), (
            f'Should be "{response_type.__name__}", '
            f'but got "{type(self.RESPONSE_DATA).__name__}"'
        )
