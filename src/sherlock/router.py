from fastapi import APIRouter

router = APIRouter(prefix="/internal/v1/sherlock")


@router.get("/ping")
async def ping():
    return {"module": "sherlock", "status": "ok"}
