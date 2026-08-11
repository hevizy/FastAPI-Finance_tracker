from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

class TransactionsTypeEnum(str, Enum):
    income = "income"
    expense = "expense"

class TransactionBase(BaseModel):
    amount: float
    type: TransactionsTypeEnum
    description: str | None = Field(default=None, min_length=2, max_length=100)
    category_id: int = Field(alias="category_id")

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int = Field(alias="id")
    date_created: datetime = Field(alias="date_created")
    user_id: int = Field(alias="user_id")

    model_config = ConfigDict(from_attributes=True)


