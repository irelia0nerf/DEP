from fastapi import APIRouter


router = APIRouter(prefix="/internal/v1/dfc")


@router.get("/ping")
async def ping():
    return {"module": "dfc", "status": "ok"}
