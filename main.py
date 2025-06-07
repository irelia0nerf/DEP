from fastapi import FastAPI
from app.routers import (
    score,
    scorelab,
    gas_monitor,
    compliance,
    dfc,
    mirror_engine,
    sentinela,
    sigilmesh,
)


app = FastAPI()

app.include_router(scorelab.router)
app.include_router(score.router)
app.include_router(gas_monitor.router)
app.include_router(compliance.router)
app.include_router(dfc.router)
app.include_router(mirror_engine.router)
app.include_router(sentinela.router)
app.include_router(sigilmesh.router)


@app.get("/")
async def root():
    return {"status": "FoundLab DEP API online"}
