from fastapi import APIRouter

test_router = APIRouter(prefix="/test")

@test_router.get("/", tags=["test"])
def test_route():
    return {"status": "ok"}