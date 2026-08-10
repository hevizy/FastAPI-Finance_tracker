from fastapi import APIRouter, Depends, HTTPException
from database.db import SessionDep
from schemas.user import UserCreate
from models.user import User

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("/", response_model=User)
def create_user(user_in: UserCreate, session: SessionDep) -> User:
    db_user = User(
        email=user_in.email,
        username=user_in.username,
        hashed_password=user_in.hashed_password,
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@users_router.get("/", response_model=list[User])
def read_all_users(
        session: SessionDep,
        offset: int = 0,
        limit: int = 100,
) -> list[User]:
    users = session.query(User).offset(offset).limit(limit).all()
    return users


@users_router.get("/{user_id}", response_model=User)
def read_user(
        session: SessionDep,
        user_id: int,
) -> User:
    user = session.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user