from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    email: str = Field(alias="email")
    password: str = Field(alias="password")
    username: str = Field(alias="username", min_length=3, max_length=30)
    hashed_password: str
