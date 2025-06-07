
from fastapi import FastAPI

from app.routers import (
    compliance,
    dfc,
    gas_monitor,
    mirror_engine,
    score,
    sentinela,
    sigilmesh,
)

app = FastAPI()

app.include_router(score.router)
app.include_router(dfc.router)
app.include_router(mirror_engine.router)
app.include_router(gas_monitor.router)
app.include_router(sigilmesh.router)
app.include_router(sentinela.router)
app.include_router(compliance.router)


@app.get("/")
def root():
    return {"status": "FoundLab DEP API online"}
