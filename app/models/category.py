from typing import Optional
from enum import Enum

from sqlmodel import Field, SQLModel

class CategoryTypeEnum(str, Enum):
    income = "income"
    expense = "expense"

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default=None, min_length=5, max_length=50)
    type: CategoryTypeEnum = Field(default=CategoryTypeEnum.income)
    user_id: int = Field(foreign_key="user.id")