from fastapi import APIRouter, Depends, HTTPException
from database.db import SessionDep
from schemas.user import UserCreate
from models.user import User
from services import user as user_service

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("/", response_model=User)
def create_user(user_in: UserCreate, session: SessionDep) -> User:
    return user_service.create_user(session, user_in)

@users_router.get("/", response_model=list[User])
def read_all_users(
        session: SessionDep,
        offset: int = 0,
        limit: int = 100,
) -> list[User]:
    return user_service.get_all_users(session, offset=offset, limit=limit)


@users_router.get("/{user_id}", response_model=User)
def read_user(
        session: SessionDep,
        user_id: int,
) -> User:
    return user_service.get_user_by_id(session, user_id)