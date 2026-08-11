from fastapi import HTTPException
from sqlmodel import Session, select
from models.transaction import Transaction
from schemas.transaction import TransactionCreate

def create_transaction(session: Session, transaction_in: TransactionCreate) -> Transaction:
    transaction = Transaction(
        amount=transaction_in.amount,
        type=transaction_in.type,
        description=transaction_in.description,
        user_id=1, #!!! Использовать айди пользователя который создал транзакцию
        category_id=1 #!!!Использовать айди категории, которую выбрал пользователь
    )
    session.add(transaction)
    session.commit()
    session.refresh(transaction)

    return transaction

def delete_transaction(session: Session, transaction_id: int):
    transaction = session.get(Transaction, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    session.delete(transaction)
    session.commit()
    return {"status": "success", "message": "Transaction successfully deleted"}


def get_all_transactions(session: Session, offset: int, limit: int) -> list[Transaction]:
    transactions = session.exec(select(Transaction).offset(offset).limit(limit)).all()
    return transactions

def get_transaction_by_id(session: Session, transaction_id: int) -> Transaction:
    transaction = session.get(Transaction, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction