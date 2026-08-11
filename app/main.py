from fastapi import FastAPI
from routers.users import users_router
from routers.categories import categories_router
from routers.transactions import transactions_router

app = FastAPI()

app.include_router(users_router)
app.include_router(categories_router)
app.include_router(transactions_router)
@app.get("/")
async def root():
    return {"message": "Hello fastAPI"}