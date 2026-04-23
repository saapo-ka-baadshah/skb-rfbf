from fastapi import APIRouter
from app.schemas.ResponseBase import ResponseBase

router = APIRouter()

@router.get("/slope", response_model=ResponseBase)
def calculate_slope(x1: int, x2: int, y1: int, y2: int):
    slope = (y2 - y1) / (x2 - x1)
    return { "message": str(slope), "status": 200 }

