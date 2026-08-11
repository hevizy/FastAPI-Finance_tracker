from fastapi import HTTPException
from sqlmodel import Session, select
from models.category import Category
from schemas.category import CategoryCreate

def create_category(session: Session, category_in: CategoryCreate) -> Category:
    category = Category(
        name=category_in.name,
        type=category_in.type,
        user_id=1 #!!! В дальнейшем нужно использовать айди зарегестрированного пользователя
    )
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

def get_all_category(session: Session, offset: int, limit: int) -> list[Category]:
    categories = session.exec(select(Category).offset(offset).limit(limit)).all()
    return categories

def get_category_by_id(session: Session, category_id: int) -> Category:
    category = session.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category
