from fastapi import APIRouter

router = APIRouter(prefix="/internal/v1/kyc_ai")

@router.get("/ping")
async def ping():
    return {"module": "kyc_ai", "status": "ok"}
