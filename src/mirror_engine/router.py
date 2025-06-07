from fastapi import APIRouter

router = APIRouter(prefix="/internal/v1/mirror_engine")

@router.get("/ping")
async def ping():
    return {"module": "mirror_engine", "status": "ok"}
