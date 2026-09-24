from pydantic import BaseModel, EmailStr, ConfigDict, Field
from pydantic.alias_generators import to_camel

from tools.fakers import fake


class UserRequestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    email: EmailStr = Field(default_factory=fake.email)
    last_name: str = Field(default_factory=fake.last_name)
    first_name: str = Field(default_factory=fake.first_name)
    middle_name: str = Field(default_factory=fake.middle_name)
    phone_number: str = Field(default_factory=fake.phone_number)


class UserGatewaySchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class UserResponseSchema(BaseModel):
    user: UserGatewaySchema
