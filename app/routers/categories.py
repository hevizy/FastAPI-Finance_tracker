from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from database.db import SessionDep
from schemas.category import CategoryCreate
from models.category import Category

categories_router = APIRouter(prefix="/categories", tags=["categories"])

@categories_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Category)
def create_category(category_in: CategoryCreate, session: SessionDep) -> Category:
    db_category = Category(
        name=category_in.name,
        type=category_in.type,
        user_id=0
    )
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category

@categories_router.get("/", response_model=list[Category])
def read_categories(
        session: SessionDep,
        offset: int = 0,
        limit: int = 100,
) -> list[Category]:
    categories = session.query(Category).offset(offset).limit(limit).all()
    return categories

@categories_router.get("/{category_id}", response_model=Category)
def read_category(
        session: SessionDep,
        category_id: int,
) -> Category:
    category = session.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category