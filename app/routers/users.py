from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from database.db import SessionDep
from schemas.user import UserCreate
from models.user import User
from services import user as user_service

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(session: SessionDep, user_in: UserCreate) -> User:
    return user_service.create_user(session, user_in)


@users_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(session: SessionDep, user_id: int):
    return user_service.delete_user(session, user_id)


@users_router.get("/", response_model=list[User], status_code=status.HTTP_200_OK)
def read_all_users(session: SessionDep, offset: int = 0, limit: int = 100) -> list[User]:
    return user_service.get_all_users(session, offset=offset, limit=limit)


@users_router.get("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def read_user(session: SessionDep, user_id: int) -> User:
    return user_service.get_user_by_id(session, user_id)
