from pydantic import BaseModel, Field
from enum import Enum

class TransactionsTypeEnum(str, Enum):
    income = "income"
    expense = "expense"

class TransactionCreate(BaseModel):
    amount: float = Field(default=None)
    type: TransactionsTypeEnum
    description: str = Field(default=None, min_length=2, max_length=50)

