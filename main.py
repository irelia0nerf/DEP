from fastapi import FastAPI
from app.routers import score
from app.routers import scorelab
from app.routers import frontend

app = FastAPI()
app.include_router(score.router)
app.include_router(scorelab.router)
app.include_router(frontend.router)


@app.get("/")
def root():
    return {"status": "FoundLab DEP API online"}
