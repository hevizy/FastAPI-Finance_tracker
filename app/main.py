from fastapi import FastAPI

from app.routers.test_routes import test_router
app = FastAPI()

app.include_router(test_router)
@app.get("/")
async def root():
    return {"message": "Hello fastAPI"}