from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(alias="email", unique=True)
    username: str = Field(alias="username", min_length=3, max_length=30)
    hashed_password: str = Field(alias="password")
    created_at: datetime = Field(default_factory=datetime.now)



