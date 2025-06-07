from fastapi import FastAPI
from app.routers import score
from app.routers import scorelab

app = FastAPI()
app.include_router(score.router)
app.include_router(scorelab.router)


@app.get("/")
def root():
    return {"status": "FoundLab DEP API online"}
