import httpx

from services.http.gateway.users.users_api import UsersGatewayAPI


class GetUserGatewayAPI(UsersGatewayAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.PATH = "/{user_id}"
        self.GET_USER_PATH_NAME = self.USERS_PATH_NAME + self.PATH

    def send_request(self, user_id: str):
        self.reset_attributes("RESPONSE_DATA")

        extensions = {"path_name": self.GET_USER_PATH_NAME}
        response = self.CLIENT.get(f"{self.USERS_API}/{user_id}", extensions=extensions)
        self.get_response_data(response)
