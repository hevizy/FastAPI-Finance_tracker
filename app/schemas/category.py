from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

class CategoryTypeEnum(str, Enum):
    income = "income"
    expense = "expense"

class CategoryBase(BaseModel):
    name: str = Field(min_length=1, max_length=50, description="Category name")
    type: CategoryTypeEnum

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)



