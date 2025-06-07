from fastapi import APIRouter

router = APIRouter(prefix="/internal/v1/gasmonitor")


@router.get("/ping")
async def ping():
    return {"module": "gasmonitor", "status": "ok"}
