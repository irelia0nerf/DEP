from fastapi import FastAPI
from app.routers import scorelab

app = FastAPI(title="FoundLab DEP API")
app.include_router(scorelab.router, prefix="/internal/v1")


@app.get("/health")
async def healthcheck():
    return {"status": "ok"}
