from datetime import datetime
from typing import Optional
from enum import Enum

from sqlmodel import Field, SQLModel

class TransactionTypeEnum(str, Enum):
    income = "income"
    expense = "expense"

class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float = Field(nullable=False)
    category_id: int = Field(foreign_key="category.id")
    type: TransactionTypeEnum = Field(nullable=False)
    description: str = Field(default=None, nullable=True)
    date_created: datetime = Field(default_factory=datetime.now)
    user_id: int = Field(foreign_key="user.id")