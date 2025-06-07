from fastapi import APIRouter

from app.services import sentinela

router = APIRouter(prefix="/internal/v1/sentinela")


@router.post("/start")
async def start():
    await sentinela.start_monitoring()
    return {"status": "started"}


@router.post("/stop")
async def stop():
    await sentinela.stop_monitoring()
    return {"status": "stopped"}
