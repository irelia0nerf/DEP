from fastapi import APIRouter

router = APIRouter(prefix="/internal/v1/score_engine")


@router.get("/ping")
async def ping():
    return {"module": "score_engine", "status": "ok"}
