import grpc

# noinspection PyUnresolvedReferences
import grpc.experimental.gevent as grpc_gevent
from grpc import Channel
from locust.env import Environment

from config import settings
from locust_settings.grpc.grpc_locust import LocustInterceptor

grpc_gevent.init_gevent()


def create_grpc_channel() -> Channel:
    return grpc.insecure_channel(settings.host_port)


def create_locust_grpc_channel(
    environment: Environment,
) -> Channel:
    interceptor = LocustInterceptor(environment)

    channel = create_grpc_channel()

    return grpc.intercept_channel(channel, interceptor)
