from sqlmodel import Session, select
from models.user import User
from schemas.user import UserCreate
from core import security

def create_user(session: Session, user_in: UserCreate) -> User:
    hashed_pswd = security.get_password_hash(user_in.password)

    db_user = User(
        email=user_in.email,
        username=user_in.username,
        hashed_password=hashed_pswd
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user

def get_all_users(session: Session, offset: int, limit: int) -> list[User]:
    statement = select(User).offset(offset).limit(limit)
    return session.exec(statement).all()

def get_user_by_email(session: Session, user_email: str) -> User:
    return session.get(User, user_email)

def get_user_by_id(session: Session, user_id: int) -> User:
    return session.get(User, user_id)

