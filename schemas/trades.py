from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class BaseTradeSchema(BaseModel):
    symbol: str
    shares: int
    price: int
    type: str
    timestamp: datetime


class CreateTradeSchema(BaseTradeSchema):
    pass


class UpdateTradeSchema(BaseTradeSchema):
    symbol: str | None=None
    shares: int | None=None
    price: int | None=None
    type: str | None=None
    timestamp: datetime | None=None


class GetTradeSchema(BaseTradeSchema):
    id: UUID

    class Config:
        from_attributes = True