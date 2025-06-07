from fastapi import APIRouter


router = APIRouter(prefix="/internal/v1/sigilmesh")


@router.get("/ping")
async def ping():
    return {"module": "sigilmesh", "status": "ok"}
