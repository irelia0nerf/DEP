from fastapi import APIRouter

router = APIRouter(prefix="/internal/v1/scorelab_core")

@router.get("/ping")
async def ping():
    return {"module": "scorelab_core", "status": "ok"}
