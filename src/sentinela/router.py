from fastapi import APIRouter

router = APIRouter(prefix="/internal/v1/sentinela")


@router.get("/ping")
async def ping():
    return {"module": "sentinela", "status": "ok"}
