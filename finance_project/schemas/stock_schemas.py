"""schemas for  Stock API."""

from pydantic import BaseModel,Field
from  datetime import datetime
from decimal  import  Decimal   


class UserRequestStockSchema(BaseModel):
    date: Optional(datetime) = None
    name: str = Field(..., max_length=100)
    symbol: str = Field(..., max_length=20)
    open: Decimal = Field(..., le=9999.99)
    hight: Decimal = Field(..., le=9999.99)
    low: Decimal = Field(..., le=9999.99)
    close: Decimal = Field(..., le=9999.99)

    class Config:
        orm_mode = True