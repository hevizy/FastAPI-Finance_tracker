from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(alias="username", min_length=1, max_length=30)

class UserCreate(UserBase):
    password: str = Field(alias="password", min_length=8)

class UserResponse(UserBase):
    id: int = Field(alias="id")
    created_at: datetime = Field(alias="created_at")

    model_config = ConfigDict(from_attributes=True)

