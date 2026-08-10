from pydantic import BaseModel, Field
from enum import Enum

class CategoryTypeEnum(str, Enum):
    income = "income"
    expense = "expense"

class CategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    type: CategoryTypeEnum

