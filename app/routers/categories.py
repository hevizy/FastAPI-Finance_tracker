from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from database.db import SessionDep
from schemas.category import CategoryCreate
from models.category import Category

from services import category as category_service

categories_router = APIRouter(prefix="/categories", tags=["categories"])

@categories_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Category)
def create_category(category_in: CategoryCreate, session: SessionDep) -> Category:
    return category_service.create_category(session, category_in)

@categories_router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(session: SessionDep, category_id: int) -> None:
    return category_service.delete_category(session, category_id)
@categories_router.get("/", response_model=list[Category])
def read_categories(
        session: SessionDep,
        offset: int = 0,
        limit: int = 100,
) -> list[Category]:
    return category_service.get_all_category(session, offset=offset, limit=limit)

@categories_router.get("/{category_id}", response_model=Category)
def read_category(
        session: SessionDep,
        category_id: int,
) -> Category:
    return category_service.get_category_by_id(session, category_id)