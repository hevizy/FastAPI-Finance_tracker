from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from database.db import SessionDep
from schemas.transaction import TransactionCreate
from models.transaction import Transaction

from services import transaction as transaction_service

transactions_router = APIRouter(prefix="/transactions", tags=["transactions"])


@transactions_router.post("/", response_model=Transaction, status_code=status.HTTP_201_CREATED)
def create_transaction(session: SessionDep, transaction_in: TransactionCreate) -> Transaction:
    return transaction_service.create_transaction(session, transaction_in)


@transactions_router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_transaction(session: SessionDep, transaction_id: int):
    return transaction_service.delete_transaction(session, transaction_id)


@transactions_router.get("/", response_model=list[Transaction], status_code=status.HTTP_200_OK)
def read_transactions(session: SessionDep, offset: int = 0, limit: int = 100) -> list[Transaction]:
    return transaction_service.get_all_transactions(session, offset, limit)


@transactions_router.get("/{transaction_id}", response_model=Transaction, status_code=status.HTTP_200_OK)
def read_transaction(session: SessionDep, transaction_id: int) -> Transaction:
    return transaction_service.get_transaction_by_id(session, transaction_id)
