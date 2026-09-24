import httpx

from schemas.users_schemas import UserRequestSchema
from services.http.gateway.users.users_api import UsersGatewayAPI


class CreateUserGatewayAPI(UsersGatewayAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.CREATE_USER_PATH_NAME = self.USERS_PATH_NAME
        self.CREATE_USER_API = self.USERS_API
        self.USER_ID = None

    def send_request(self):
        self.reset_attributes("RESPONSE_DATA", "USER_ID")

        user_data = UserRequestSchema().model_dump(by_alias=True)
        extensions = {"path_name": self.CREATE_USER_PATH_NAME}

        response = self.CLIENT.post(
            self.CREATE_USER_API, json=user_data, extensions=extensions
        )
        self.get_response_data(response)
        self.USER_ID = self.RESPONSE_DATA.user.id
