from fastapi import APIRouter
from app.schemas.ResponseBase import ResponseBase

router = APIRouter()

@router.get("/", response_model=ResponseBase)
async def status():
    """Health check endpoint for the API."""
    return { "message": "OK", "status": 200 }

