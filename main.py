from fastapi import FastAPI
from app.routers import score, scorelab, sigilmesh


from fastapi import FastAPI
from app.routers import score

app = FastAPI()

app.include_router(score.router)

app.include_router(scorelab.router)

app.include_router(sigilmesh.router)


@app.get("/")
def root():
    return {"status": "FoundLab DEP API online"}