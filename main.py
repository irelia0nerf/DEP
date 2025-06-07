from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from src.scorelab_core.router import router as scorelab_core_router
from src.dfc.router import router as dfc_router
from src.sherlock.router import router as sherlock_router
from src.sentinela.router import router as sentinela_router
from src.sigilmesh.router import router as sigilmesh_router
from src.score_engine.router import router as score_engine_router
from src.mirror_engine.router import router as mirror_engine_router
from src.gasmonitor.router import router as gasmonitor_router
from src.kyc_ai.router import router as kyc_ai_router

app = FastAPI()

client = AsyncIOMotorClient("mongodb://localhost:27017")
app.state.db = client["foundlab_dep"]

for r in [
    scorelab_core_router,
    dfc_router,
    sherlock_router,
    sentinela_router,
    sigilmesh_router,
    score_engine_router,
    mirror_engine_router,
    gasmonitor_router,
    kyc_ai_router,
]:
    app.include_router(r)


@app.get("/")
async def root():
    return {"status": "FoundLab DEP API online"}
