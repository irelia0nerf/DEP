from fastapi import FastAPI
from app.routers import (
    score,
    scorelab,
    gas_monitor,
    mirror_engine,
    compliance,
    dfc,
    sigilmesh,
    sentinela,
)

app = FastAPI()

app.include_router(score.router)
app.include_router(scorelab.router)
app.include_router(gas_monitor.router)
app.include_router(mirror_engine.router)
app.include_router(compliance.router)
app.include_router(dfc.router)
app.include_router(sigilmesh.router)
app.include_router(sentinela.router)


@app.get("/")
def root():
    return {"status": "FoundLab DEP API online"}