from fastapi import FastAPI
from app.api.v1 import router as api_router

app = FastAPI(
    title = "RFBF Backend",
    description = "A clean, scalable, easy spinup FastAPI Backend",
    version = "1.0.0"
)

# Include primary router
app.include_router(api_router, prefix="/api")

