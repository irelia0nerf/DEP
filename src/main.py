from fastapi import FastAPI
from src.routers import score

app = FastAPI()

app.include_router(score.router)


@app.get("/")
async def root():
    return {"status": "FoundLab DEP API online"}
