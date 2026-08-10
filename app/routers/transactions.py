from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from database.db import SessionDep
from schemas.transaction import TransactionCreate
from models.transaction import Transaction

transactions_router = APIRouter(prefix="/transactions",tags=["transactions"],)

@transactions_router.post("/", response_model=Transaction)
def create_transaction(transaction_in: TransactionCreate, session: SessionDep) -> Transaction:
    db_transaction = Transaction(
        amount = transaction_in.amount,
        type = transaction_in.type,
        description = transaction_in.description,
        category_id=0,
        user_id=0
    )
    session.add(db_transaction)
    session.commit()
    session.refresh(db_transaction)
    return db_transaction

@transactions_router.get("/", response_model=list[Transaction])
def read_transactions(
        session: SessionDep,
        offset: int = 0,
        limit: int = 100,
) -> list[Transaction]:
    transactions = session.query(Transaction).offset(offset).limit(limit).all()
    return transactions

@transactions_router.get("/{id}", response_model=Transaction)
def read_transaction(
        session: SessionDep,
        transaction_id: int,
) -> Transaction:
    transaction = session.query(Transaction).filter(Transaction.id == transaction_id).one_or_none()
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Transaction not found")
    return transaction