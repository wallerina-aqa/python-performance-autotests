from pydantic import BaseModel, HttpUrl, Field


class DocumentGatewaySchema(BaseModel):
    url: HttpUrl = Field(min_length=1, max_length=2083)
    document: str


class TariffDocumentResponseSchema(BaseModel):
    tariff: DocumentGatewaySchema


class ContractDocumentResponseSchema(BaseModel):
    contract: DocumentGatewaySchema
